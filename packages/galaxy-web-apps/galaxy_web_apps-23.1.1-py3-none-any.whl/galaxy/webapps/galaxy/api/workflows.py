"""
API operations for Workflows
"""

import json
import logging
import os
from io import BytesIO
from typing import (
    Any,
    Dict,
    List,
    Optional,
)

from fastapi import (
    Body,
    Path,
    Query,
    Response,
    status,
)
from gxformat2._yaml import ordered_dump
from markupsafe import escape
from pydantic import Extra
from starlette.responses import StreamingResponse

from galaxy import (
    exceptions,
    model,
    util,
)
from galaxy.files.uris import (
    stream_url_to_str,
    validate_uri_access,
)
from galaxy.managers.context import ProvidesUserContext
from galaxy.managers.jobs import (
    fetch_job_states,
    invocation_job_source_iter,
)
from galaxy.managers.workflows import (
    MissingToolsException,
    RefactorRequest,
    WorkflowCreateOptions,
    WorkflowUpdateOptions,
)
from galaxy.model.base import transaction
from galaxy.model.item_attrs import UsesAnnotations
from galaxy.model.store import BcoExportOptions
from galaxy.schema.fields import DecodedDatabaseIdField
from galaxy.schema.invocation import InvocationMessageResponseModel
from galaxy.schema.schema import (
    AsyncFile,
    AsyncTaskResultSummary,
    SetSlugPayload,
    ShareWithPayload,
    ShareWithStatus,
    SharingStatus,
    StoreContentSource,
    WorkflowSortByEnum,
)
from galaxy.structured_app import StructuredApp
from galaxy.tool_shed.galaxy_install.install_manager import InstallRepositoryManager
from galaxy.tools import recommendations
from galaxy.tools.parameters import populate_state
from galaxy.tools.parameters.basic import workflow_building_modes
from galaxy.util.sanitize_html import sanitize_html
from galaxy.version import VERSION
from galaxy.web import (
    expose_api,
    expose_api_anonymous,
    expose_api_anonymous_and_sessionless,
    expose_api_raw,
    expose_api_raw_anonymous_and_sessionless,
    format_return_as_json,
)
from galaxy.webapps.base.controller import (
    SharableMixin,
    url_for,
    UsesStoredWorkflowMixin,
)
from galaxy.webapps.base.webapp import GalaxyWebTransaction
from galaxy.webapps.galaxy.api import (
    BaseGalaxyAPIController,
    depends,
    DependsOnTrans,
    IndexQueryTag,
    Router,
    search_query_param,
)
from galaxy.webapps.galaxy.services.base import (
    ConsumesModelStores,
    ServesExportStores,
)
from galaxy.webapps.galaxy.services.invocations import (
    InvocationIndexPayload,
    InvocationSerializationParams,
    InvocationsService,
    PrepareStoreDownloadPayload,
    WriteInvocationStoreToPayload,
)
from galaxy.webapps.galaxy.services.workflows import (
    WorkflowIndexPayload,
    WorkflowsService,
)
from galaxy.workflow.extract import extract_workflow
from galaxy.workflow.modules import module_factory
from galaxy.workflow.run import queue_invoke
from galaxy.workflow.run_request import build_workflow_run_configs

log = logging.getLogger(__name__)

router = Router(tags=["workflows"])


class CreateInvocationFromStore(StoreContentSource):
    history_id: Optional[str]

    class Config:
        extra = Extra.allow


class WorkflowsAPIController(
    BaseGalaxyAPIController,
    UsesStoredWorkflowMixin,
    UsesAnnotations,
    SharableMixin,
    ServesExportStores,
    ConsumesModelStores,
):
    service: WorkflowsService = depends(WorkflowsService)
    invocations_service: InvocationsService = depends(InvocationsService)

    def __init__(self, app: StructuredApp):
        super().__init__(app)
        self.history_manager = app.history_manager
        self.workflow_manager = app.workflow_manager
        self.workflow_contents_manager = app.workflow_contents_manager
        self.tool_recommendations = recommendations.ToolRecommendations()

    @expose_api
    def set_workflow_menu(self, trans: GalaxyWebTransaction, payload=None, **kwd):
        """
        Save workflow menu to be shown in the tool panel
        PUT /api/workflows/menu
        """
        payload = payload or {}
        user = trans.user
        workflow_ids = payload.get("workflow_ids")
        if workflow_ids is None:
            workflow_ids = []
        elif type(workflow_ids) != list:
            workflow_ids = [workflow_ids]
        workflow_ids_decoded = []
        # Decode the encoded workflow ids
        for ids in workflow_ids:
            workflow_ids_decoded.append(trans.security.decode_id(ids))
        sess = trans.sa_session
        # This explicit remove seems like a hack, need to figure out
        # how to make the association do it automatically.
        for m in user.stored_workflow_menu_entries:
            sess.delete(m)
        user.stored_workflow_menu_entries = []
        q = sess.query(model.StoredWorkflow)
        # To ensure id list is unique
        seen_workflow_ids = set()
        for wf_id in workflow_ids_decoded:
            if wf_id in seen_workflow_ids:
                continue
            else:
                seen_workflow_ids.add(wf_id)
            m = model.StoredWorkflowMenuEntry()
            m.stored_workflow = q.get(wf_id)
            user.stored_workflow_menu_entries.append(m)
        with transaction(sess):
            sess.commit()
        message = "Menu updated."
        trans.set_message(message)
        return {"message": message, "status": "done"}

    @expose_api_anonymous_and_sessionless
    def show(self, trans: GalaxyWebTransaction, id, **kwd):
        """
        GET /api/workflows/{encoded_workflow_id}

        :param  instance:                 true if fetch by Workflow ID instead of StoredWorkflow id, false
                                          by default.
        :type   instance:                 boolean

        Displays information needed to run a workflow.
        """
        stored_workflow = self.__get_stored_workflow(trans, id, **kwd)
        if stored_workflow.importable is False and stored_workflow.user != trans.user and not trans.user_is_admin:
            if (
                trans.sa_session.query(model.StoredWorkflowUserShareAssociation)
                .filter_by(user=trans.user, stored_workflow=stored_workflow)
                .count()
                == 0
            ):
                message = "Workflow is neither importable, nor owned by or shared with current user"
                raise exceptions.ItemAccessibilityException(message)
        if kwd.get("legacy", False):
            style = "legacy"
        else:
            style = "instance"
        version = kwd.get("version")
        if version is None and util.string_as_bool(kwd.get("instance", "false")):
            # A Workflow instance may not be the latest workflow version attached to StoredWorkflow.
            # This figures out the correct version so that we return the correct Workflow and version.
            workflow_id = self.decode_id(id)
            for i, workflow in enumerate(reversed(stored_workflow.workflows)):
                if workflow.id == workflow_id:
                    version = i
                    break
        return self.workflow_contents_manager.workflow_to_dict(trans, stored_workflow, style=style, version=version)

    @expose_api
    def create(self, trans: GalaxyWebTransaction, payload=None, **kwd):
        """
        POST /api/workflows

        Create workflows in various ways.

        :param  from_history_id:             Id of history to extract a workflow from.
        :type   from_history_id:             str

        :param  job_ids:                     If from_history_id is set - optional list of jobs to include when extracting a workflow from history
        :type   job_ids:                     str

        :param  dataset_ids:                 If from_history_id is set - optional list of HDA "hid"s corresponding to workflow inputs when extracting a workflow from history
        :type   dataset_ids:                 str

        :param  dataset_collection_ids:      If from_history_id is set - optional list of HDCA "hid"s corresponding to workflow inputs when extracting a workflow from history
        :type   dataset_collection_ids:      str

        :param  workflow_name:               If from_history_id is set - name of the workflow to create when extracting a workflow from history
        :type   workflow_name:               str

        """
        ways_to_create = {
            "archive_file",
            "archive_source",
            "from_history_id",
            "from_path",
            "shared_workflow_id",
            "workflow",
        }

        if trans.user_is_bootstrap_admin:
            raise exceptions.RealUserRequiredException("Only real users can create or run workflows.")

        if payload is None or len(ways_to_create.intersection(payload)) == 0:
            message = f"One parameter among - {', '.join(ways_to_create)} - must be specified"
            raise exceptions.RequestParameterMissingException(message)

        if len(ways_to_create.intersection(payload)) > 1:
            message = f"Only one parameter among - {', '.join(ways_to_create)} - must be specified"
            raise exceptions.RequestParameterInvalidException(message)

        if "archive_source" in payload or "archive_file" in payload:
            archive_source = payload.get("archive_source")
            archive_file = payload.get("archive_file")
            archive_data = None
            if archive_source:
                validate_uri_access(archive_source, trans.user_is_admin, trans.app.config.fetch_url_allowlist_ips)
                if archive_source.startswith("file://"):
                    workflow_src = {"src": "from_path", "path": archive_source[len("file://") :]}
                    payload["workflow"] = workflow_src
                    return self.__api_import_new_workflow(trans, payload, **kwd)
                elif archive_source == "trs_tool":
                    server = None
                    trs_tool_id = None
                    trs_version_id = None
                    import_source = None
                    if "trs_url" in payload:
                        parts = self.app.trs_proxy.match_url(payload["trs_url"])
                        if parts:
                            server = self.app.trs_proxy.server_from_url(parts["trs_base_url"])
                            trs_tool_id = parts["tool_id"]
                            trs_version_id = parts["version_id"]
                            payload["trs_tool_id"] = trs_tool_id
                            payload["trs_version_id"] = trs_version_id
                        else:
                            raise exceptions.MessageException("Invalid TRS URL.")
                    else:
                        trs_server = payload.get("trs_server")
                        server = self.app.trs_proxy.get_server(trs_server)
                        trs_tool_id = payload.get("trs_tool_id")
                        trs_version_id = payload.get("trs_version_id")

                    archive_data = server.get_version_descriptor(trs_tool_id, trs_version_id)
                else:
                    try:
                        archive_data = stream_url_to_str(
                            archive_source, trans.app.file_sources, prefix="gx_workflow_download"
                        )
                        import_source = "URL"
                    except Exception:
                        raise exceptions.MessageException(f"Failed to open URL '{escape(archive_source)}'.")
            elif hasattr(archive_file, "file"):
                uploaded_file = archive_file.file
                uploaded_file_name = uploaded_file.name
                if os.path.getsize(os.path.abspath(uploaded_file_name)) > 0:
                    archive_data = util.unicodify(uploaded_file.read())
                    import_source = "uploaded file"
                else:
                    raise exceptions.MessageException("You attempted to upload an empty file.")
            else:
                raise exceptions.MessageException("Please provide a URL or file.")
            return self.__api_import_from_archive(trans, archive_data, import_source, payload=payload)

        if "from_history_id" in payload:
            from_history_id = payload.get("from_history_id")
            from_history_id = self.decode_id(from_history_id)
            history = self.history_manager.get_accessible(from_history_id, trans.user, current_history=trans.history)

            job_ids = [self.decode_id(_) for _ in payload.get("job_ids", [])]
            dataset_ids = payload.get("dataset_ids", [])
            dataset_collection_ids = payload.get("dataset_collection_ids", [])
            workflow_name = payload["workflow_name"]
            stored_workflow = extract_workflow(
                trans=trans,
                user=trans.user,
                history=history,
                job_ids=job_ids,
                dataset_ids=dataset_ids,
                dataset_collection_ids=dataset_collection_ids,
                workflow_name=workflow_name,
            )
            item = stored_workflow.to_dict(value_mapper={"id": trans.security.encode_id})
            item["url"] = url_for("workflow", id=item["id"])
            return item

        if "from_path" in payload:
            from_path = payload.get("from_path")
            object_id = payload.get("object_id")
            workflow_src = {"src": "from_path", "path": from_path}
            if object_id is not None:
                workflow_src["object_id"] = object_id
            payload["workflow"] = workflow_src
            return self.__api_import_new_workflow(trans, payload, **kwd)

        if "shared_workflow_id" in payload:
            workflow_id = payload["shared_workflow_id"]
            return self.__api_import_shared_workflow(trans, workflow_id, payload)

        if "workflow" in payload:
            return self.__api_import_new_workflow(trans, payload, **kwd)

        # This was already raised above, but just in case...
        raise exceptions.RequestParameterMissingException("No method for workflow creation supplied.")

    @expose_api_raw_anonymous_and_sessionless
    def workflow_dict(self, trans: GalaxyWebTransaction, workflow_id, **kwd):
        """
        GET /api/workflows/{encoded_workflow_id}/download

        Returns a selected workflow.

        :type   style:  str
        :param  style:  Style of export. The default is 'export', which is the meant to be used
                        with workflow import endpoints. Other formats such as 'instance', 'editor',
                        'run' are more tied to the GUI and should not be considered stable APIs.
                        The default format for 'export' is specified by the
                        admin with the `default_workflow_export_format` config
                        option. Style can be specified as either 'ga' or 'format2' directly
                        to be explicit about which format to download.

        :param  instance:                 true if fetch by Workflow ID instead of StoredWorkflow id, false
                                          by default.
        :type   instance:                 boolean
        """
        stored_workflow = self.__get_stored_accessible_workflow(trans, workflow_id, **kwd)

        style = kwd.get("style", "export")
        download_format = kwd.get("format")
        version = kwd.get("version")
        history_id = kwd.get("history_id")
        history = None
        if history_id:
            history = self.history_manager.get_accessible(
                self.decode_id(history_id), trans.user, current_history=trans.history
            )
        ret_dict = self.workflow_contents_manager.workflow_to_dict(
            trans, stored_workflow, style=style, version=version, history=history
        )
        if download_format == "json-download":
            sname = stored_workflow.name
            sname = "".join(c in util.FILENAME_VALID_CHARS and c or "_" for c in sname)[0:150]
            if ret_dict.get("format-version", None) == "0.1":
                extension = "ga"
            else:
                extension = "gxwf.json"
            trans.response.headers[
                "Content-Disposition"
            ] = f'attachment; filename="Galaxy-Workflow-{sname}.{extension}"'
            trans.response.set_content_type("application/galaxy-archive")

        if style == "format2" and download_format != "json-download":
            return ordered_dump(ret_dict)
        else:
            return format_return_as_json(ret_dict, pretty=True)

    @expose_api
    def import_new_workflow_deprecated(self, trans: GalaxyWebTransaction, payload, **kwd):
        """
        POST /api/workflows/upload
        Importing dynamic workflows from the api. Return newly generated workflow id.
        Author: rpark

        # currently assumes payload['workflow'] is a json representation of a workflow to be inserted into the database

        Deprecated in favor to POST /api/workflows with encoded 'workflow' in
        payload the same way.
        """
        return self.__api_import_new_workflow(trans, payload, **kwd)

    @expose_api
    def update(self, trans: GalaxyWebTransaction, id, payload, **kwds):
        """
        PUT /api/workflows/{id}

        Update the workflow stored with ``id``.

        :type   id:      str
        :param  id:      the encoded id of the workflow to update
        :param  instance: true if fetch by Workflow ID instead of StoredWorkflow id, false by default.
        :type   instance: boolean
        :type   payload: dict
        :param  payload: a dictionary containing any or all the

            :workflow:

                the json description of the workflow as would be
                produced by GET workflows/<id>/download or
                given to `POST workflows`

                The workflow contents will be updated to target this.

            :name:

                optional string name for the workflow, if not present in payload,
                name defaults to existing name

            :annotation:

                optional string annotation for the workflow, if not present in payload,
                annotation defaults to existing annotation

            :menu_entry:

                optional boolean marking if the workflow should appear in the user\'s menu,
                if not present, workflow menu entries are not modified

            :tags:

                optional list containing list of tags to add to the workflow (overwriting
                existing tags), if not present, tags are not modified

            :from_tool_form:

                True iff encoded state coming in is encoded for the tool form.


        :rtype:     dict
        :returns:   serialized version of the workflow
        """
        stored_workflow = self.__get_stored_workflow(trans, id, **kwds)
        workflow_dict = payload.get("workflow", {})
        workflow_dict.update({k: v for k, v in payload.items() if k not in workflow_dict})
        if workflow_dict:
            require_flush = False
            raw_workflow_description = self.__normalize_workflow(trans, workflow_dict)
            workflow_dict = raw_workflow_description.as_dict
            new_workflow_name = workflow_dict.get("name")
            old_workflow = stored_workflow.latest_workflow
            name_updated = new_workflow_name and new_workflow_name != stored_workflow.name
            steps_updated = "steps" in workflow_dict
            if name_updated and not steps_updated:
                sanitized_name = sanitize_html(new_workflow_name or old_workflow.name)
                workflow = old_workflow.copy(user=trans.user)
                workflow.stored_workflow = stored_workflow
                workflow.name = sanitized_name
                stored_workflow.name = sanitized_name
                stored_workflow.latest_workflow = workflow
                trans.sa_session.add(workflow, stored_workflow)
                require_flush = True

            if "hidden" in workflow_dict and stored_workflow.hidden != workflow_dict["hidden"]:
                stored_workflow.hidden = workflow_dict["hidden"]
                require_flush = True

            if "published" in workflow_dict and stored_workflow.published != workflow_dict["published"]:
                stored_workflow.published = workflow_dict["published"]
                require_flush = True

            if "importable" in workflow_dict and stored_workflow.importable != workflow_dict["importable"]:
                stored_workflow.importable = workflow_dict["importable"]
                require_flush = True

            if "annotation" in workflow_dict and not steps_updated:
                newAnnotation = sanitize_html(workflow_dict["annotation"])
                self.add_item_annotation(trans.sa_session, trans.user, stored_workflow, newAnnotation)
                require_flush = True

            if "menu_entry" in workflow_dict or "show_in_tool_panel" in workflow_dict:
                show_in_panel = workflow_dict.get("menu_entry") or workflow_dict.get("show_in_tool_panel")
                stored_workflow_menu_entries = trans.user.stored_workflow_menu_entries
                decoded_id = trans.security.decode_id(id)
                if show_in_panel:
                    workflow_ids = [wf.stored_workflow_id for wf in stored_workflow_menu_entries]
                    if decoded_id not in workflow_ids:
                        menu_entry = model.StoredWorkflowMenuEntry()
                        menu_entry.stored_workflow = stored_workflow
                        stored_workflow_menu_entries.append(menu_entry)
                        trans.sa_session.add(menu_entry)
                        require_flush = True
                else:
                    # remove if in list
                    entries = {x.stored_workflow_id: x for x in stored_workflow_menu_entries}
                    if decoded_id in entries:
                        stored_workflow_menu_entries.remove(entries[decoded_id])
                        require_flush = True
            # set tags
            if "tags" in workflow_dict:
                trans.tag_handler.set_tags_from_list(
                    user=trans.user,
                    item=stored_workflow,
                    new_tags_list=workflow_dict["tags"],
                )

            if require_flush:
                with transaction(trans.sa_session):
                    trans.sa_session.commit()

            if "steps" in workflow_dict:
                try:
                    workflow_update_options = WorkflowUpdateOptions(**payload)
                    workflow, errors = self.workflow_contents_manager.update_workflow_from_raw_description(
                        trans,
                        stored_workflow,
                        raw_workflow_description,
                        workflow_update_options,
                    )
                except MissingToolsException:
                    raise exceptions.MessageException(
                        "This workflow contains missing tools. It cannot be saved until they have been removed from the workflow or installed."
                    )

        else:
            message = "Updating workflow requires dictionary containing 'workflow' attribute with new JSON description."
            raise exceptions.RequestParameterInvalidException(message)
        return self.workflow_contents_manager.workflow_to_dict(trans, stored_workflow, style="instance")

    @expose_api
    def refactor(self, trans, id, payload, **kwds):
        """
        * PUT /api/workflows/{id}/refactor
            updates the workflow stored with ``id``

        :type   id:      str
        :param  id:      the encoded id of the workflow to update
        :param  instance:                 true if fetch by Workflow ID instead of StoredWorkflow id, false
                                          by default.
        :type   instance:                 boolean
        :type   payload: dict
        :param  payload: a dictionary containing list of actions to apply.
        :rtype:     dict
        :returns:   serialized version of the workflow
        """
        stored_workflow = self.__get_stored_workflow(trans, id, **kwds)
        refactor_request = RefactorRequest(**payload)
        return self.workflow_contents_manager.refactor(trans, stored_workflow, refactor_request)

    @expose_api
    def build_module(self, trans: GalaxyWebTransaction, payload=None):
        """
        POST /api/workflows/build_module
        Builds module models for the workflow editor.
        """
        # payload is tool state
        if payload is None:
            payload = {}
        inputs = payload.get("inputs", {})
        trans.workflow_building_mode = workflow_building_modes.ENABLED
        module = module_factory.from_dict(trans, payload, from_tool_form=True)
        if "tool_state" not in payload:
            module_state: Dict[str, Any] = {}
            populate_state(trans, module.get_inputs(), inputs, module_state, check=False)
            module.recover_state(module_state, from_tool_form=True)
        step_dict = {
            "name": module.get_name(),
            "tool_state": module.get_state(),
            "content_id": module.get_content_id(),
            "inputs": module.get_all_inputs(connectable_only=True),
            "outputs": module.get_all_outputs(),
            "config_form": module.get_config_form(),
        }
        if payload["type"] == "tool":
            step_dict["tool_version"] = module.get_version()
        return step_dict

    @expose_api
    def get_tool_predictions(self, trans: ProvidesUserContext, payload, **kwd):
        """
        POST /api/workflows/get_tool_predictions

        Fetch predicted tools for a workflow

        :type   payload: dict
        :param  payload:

            a dictionary containing two parameters
            'tool_sequence' - comma separated sequence of tool ids
            'remote_model_url' - (optional) path to the deep learning model
        """
        remote_model_url = payload.get("remote_model_url", trans.app.config.tool_recommendation_model_path)
        tool_sequence = payload.get("tool_sequence", "")
        if "tool_sequence" not in payload or remote_model_url is None:
            return
        tool_sequence, recommended_tools = self.tool_recommendations.get_predictions(
            trans, tool_sequence, remote_model_url
        )
        return {"current_tool": tool_sequence, "predicted_data": recommended_tools}

    #
    # -- Helper methods --
    #
    def __api_import_from_archive(self, trans: GalaxyWebTransaction, archive_data, source=None, payload=None):
        payload = payload or {}
        try:
            data = json.loads(archive_data)
        except Exception:
            if "GalaxyWorkflow" in archive_data:
                data = {"yaml_content": archive_data}
            else:
                raise exceptions.MessageException("The data content does not appear to be a valid workflow.")
        if not data:
            raise exceptions.MessageException("The data content is missing.")
        raw_workflow_description = self.__normalize_workflow(trans, data)
        workflow_create_options = WorkflowCreateOptions(**payload)
        workflow, missing_tool_tups = self._workflow_from_dict(
            trans, raw_workflow_description, workflow_create_options, source=source
        )
        workflow_id = workflow.id
        workflow = workflow.latest_workflow

        response = {
            "message": f"Workflow '{escape(workflow.name)}' imported successfully.",
            "status": "success",
            "id": trans.security.encode_id(workflow_id),
        }
        if workflow.has_errors:
            response["message"] = "Imported, but some steps in this workflow have validation errors."
            response["status"] = "error"
        elif len(workflow.steps) == 0:
            response["message"] = "Imported, but this workflow has no steps."
            response["status"] = "error"
        elif workflow.has_cycles:
            response["message"] = "Imported, but this workflow contains cycles."
            response["status"] = "error"
        return response

    def __api_import_new_workflow(self, trans: GalaxyWebTransaction, payload, **kwd):
        data = payload["workflow"]
        raw_workflow_description = self.__normalize_workflow(trans, data)
        workflow_create_options = WorkflowCreateOptions(**payload)
        workflow, missing_tool_tups = self._workflow_from_dict(
            trans,
            raw_workflow_description,
            workflow_create_options,
        )
        # galaxy workflow newly created id
        workflow_id = workflow.id
        # api encoded, id
        encoded_id = trans.security.encode_id(workflow_id)
        item = workflow.to_dict(value_mapper={"id": trans.security.encode_id})
        item["annotations"] = [x.annotation for x in workflow.annotations]
        item["url"] = url_for("workflow", id=encoded_id)
        item["owner"] = workflow.user.username
        item["number_of_steps"] = len(workflow.latest_workflow.steps)
        return item

    def __normalize_workflow(self, trans: GalaxyWebTransaction, as_dict):
        return self.workflow_contents_manager.normalize_workflow_format(trans, as_dict)

    @expose_api
    def import_shared_workflow_deprecated(self, trans: GalaxyWebTransaction, payload, **kwd):
        """
        POST /api/workflows/import
        Import a workflow shared by other users.

        :param  workflow_id:      the workflow id (required)
        :type   workflow_id:      str

        :raises: exceptions.MessageException, exceptions.ObjectNotFound
        """
        # Pull parameters out of payload.
        workflow_id = payload.get("workflow_id", None)
        if workflow_id is None:
            raise exceptions.ObjectAttributeMissingException("Missing required parameter 'workflow_id'.")
        self.__api_import_shared_workflow(trans, workflow_id, payload)

    def __api_import_shared_workflow(self, trans: GalaxyWebTransaction, workflow_id, payload, **kwd):
        try:
            stored_workflow = self.get_stored_workflow(trans, workflow_id, check_ownership=False)
        except Exception:
            raise exceptions.ObjectNotFound("Malformed workflow id specified.")
        if stored_workflow.importable is False:
            raise exceptions.ItemAccessibilityException(
                "The owner of this workflow has disabled imports via this link."
            )
        elif stored_workflow.deleted:
            raise exceptions.ItemDeletionException("You can't import this workflow because it has been deleted.")
        imported_workflow = self._import_shared_workflow(trans, stored_workflow)
        item = imported_workflow.to_dict(value_mapper={"id": trans.security.encode_id})
        encoded_id = trans.security.encode_id(imported_workflow.id)
        item["url"] = url_for("workflow", id=encoded_id)
        return item

    @expose_api
    def invoke(self, trans: GalaxyWebTransaction, workflow_id, payload, **kwd):
        """
        POST /api/workflows/{encoded_workflow_id}/invocations

        Schedule the workflow specified by `workflow_id` to run.

        .. note:: This method takes the same arguments as
            :func:`galaxy.webapps.galaxy.api.workflows.WorkflowsAPIController.create` above.

        :raises: exceptions.MessageException, exceptions.RequestParameterInvalidException
        """
        # Get workflow + accessibility check.
        stored_workflow = self.__get_stored_accessible_workflow(trans, workflow_id, instance=kwd.get("instance", False))
        workflow = stored_workflow.latest_workflow
        run_configs = build_workflow_run_configs(trans, workflow, payload)
        is_batch = payload.get("batch")
        if not is_batch and len(run_configs) != 1:
            raise exceptions.RequestParameterInvalidException("Must specify 'batch' to use batch parameters.")

        require_exact_tool_versions = util.string_as_bool(payload.get("require_exact_tool_versions", "true"))
        tools = self.workflow_contents_manager.get_all_tools(workflow)
        missing_tools = [
            tool
            for tool in tools
            if not self.app.toolbox.has_tool(
                tool["tool_id"], tool_version=tool["tool_version"], exact=require_exact_tool_versions
            )
        ]
        if missing_tools:
            missing_tools_message = "Workflow was not invoked; the following required tools are not installed: "
            if require_exact_tool_versions:
                missing_tools_message += ", ".join(
                    [f"{tool['tool_id']} (version {tool['tool_version']})" for tool in missing_tools]
                )
            else:
                missing_tools_message += ", ".join([tool["tool_id"] for tool in missing_tools])
            raise exceptions.MessageException(missing_tools_message)

        invocations = []
        for run_config in run_configs:
            workflow_scheduler_id = payload.get("scheduler", None)
            # TODO: workflow scheduler hints
            work_request_params = dict(scheduler=workflow_scheduler_id)
            workflow_invocation = queue_invoke(
                trans=trans,
                workflow=workflow,
                workflow_run_config=run_config,
                request_params=work_request_params,
                flush=False,
            )
            invocations.append(workflow_invocation)

        with transaction(trans.sa_session):
            trans.sa_session.commit()
        encoded_invocations = []
        for invocation in invocations:
            as_dict = workflow_invocation.to_dict()
            as_dict = self.encode_all_ids(trans, as_dict, recursive=True)
            as_dict["messages"] = [
                InvocationMessageResponseModel.parse_obj(message).__root__.dict() for message in invocation.messages
            ]
            encoded_invocations.append(as_dict)

        if is_batch:
            return encoded_invocations
        else:
            return encoded_invocations[0]

    @expose_api
    def index_invocations(self, trans: GalaxyWebTransaction, **kwd):
        """
        GET /api/workflows/{workflow_id}/invocations
        GET /api/invocations

        Get the list of a user's workflow invocations. If workflow_id is supplied
        (either via URL or query parameter) it should be an encoded StoredWorkflow id
        and returned invocations will be restricted to that workflow. history_id (an encoded
        History id) can be used to further restrict the query. If neither a workflow_id or
        history_id is supplied, all the current user's workflow invocations will be indexed
        (as determined by the invocation being executed on one of the user's histories).

        :param  workflow_id:      an encoded stored workflow id to restrict query to
        :type   workflow_id:      str

        :param  instance:         true if fetch by Workflow ID instead of StoredWorkflow id, false
                                  by default.
        :type   instance:         boolean

        :param  history_id:       an encoded history id to restrict query to
        :type   history_id:       str

        :param  job_id:           an encoded job id to restrict query to
        :type   job_id:           str

        :param  user_id:          an encoded user id to restrict query to, must be own id if not admin user
        :type   user_id:          str

        :param  view:             level of detail to return per invocation 'element' or 'collection'.
        :type   view:             str

        :param  step_details:     If 'view' is 'element', also include details on individual steps.
        :type   step_details:     bool

        :raises: exceptions.MessageException, exceptions.ObjectNotFound
        """
        invocation_payload = InvocationIndexPayload(**kwd)
        serialization_params = InvocationSerializationParams(**kwd)
        invocations, total_matches = self.invocations_service.index(trans, invocation_payload, serialization_params)
        trans.response.headers["total_matches"] = total_matches
        return invocations

    @expose_api_anonymous
    def create_invocations_from_store(self, trans, payload, **kwd):
        """
        POST /api/invocations/from_store

        Create invocation(s) from a supplied model store.

        Input can be an archive describing a Galaxy model store containing an
        workflow invocation - for instance one created with with write_store
        or prepare_store_download endpoint.
        """
        create_payload = CreateInvocationFromStore(**payload)
        serialization_params = InvocationSerializationParams(**payload)
        # refactor into a service...
        return self._create_from_store(trans, create_payload, serialization_params)

    def _create_from_store(
        self, trans, payload: CreateInvocationFromStore, serialization_params: InvocationSerializationParams
    ):
        history = self.history_manager.get_owned(
            self.decode_id(payload.history_id), trans.user, current_history=trans.history
        )
        object_tracker = self.create_objects_from_store(
            trans,
            payload,
            history=history,
        )
        return self.invocations_service.serialize_workflow_invocations(
            object_tracker.invocations_by_key.values(), serialization_params
        )

    @expose_api
    def show_invocation(self, trans: GalaxyWebTransaction, invocation_id, **kwd):
        """
        GET /api/workflows/{workflow_id}/invocations/{invocation_id}
        GET /api/invocations/{invocation_id}

        Get detailed description of workflow invocation

        :param  invocation_id:      the invocation id (required)
        :type   invocation_id:      str

        :param  step_details:       fetch details about individual invocation steps
                                    and populate a steps attribute in the resulting
                                    dictionary. Defaults to false.
        :type   step_details:       bool

        :param  legacy_job_state:   If step_details is true, and this is set to true
                                    populate the invocation step state with the job state
                                    instead of the invocation step state. This will also
                                    produce one step per job in mapping jobs to mimic the
                                    older behavior with respect to collections. Partially
                                    scheduled steps may provide incomplete information
                                    and the listed steps outputs are the mapped over
                                    step outputs but the individual job outputs
                                    when this is set - at least for now.
        :type   legacy_job_state:   bool

        :raises: exceptions.MessageException, exceptions.ObjectNotFound
        """
        decoded_workflow_invocation_id = self.decode_id(invocation_id)
        workflow_invocation = self.workflow_manager.get_invocation(trans, decoded_workflow_invocation_id, eager=True)
        if not workflow_invocation:
            raise exceptions.ObjectNotFound()

        return self.__encode_invocation(workflow_invocation, **kwd)

    @expose_api
    def cancel_invocation(self, trans: ProvidesUserContext, invocation_id, **kwd):
        """
        DELETE /api/workflows/{workflow_id}/invocations/{invocation_id}
        DELETE /api/invocations/{invocation_id}
        Cancel the specified workflow invocation.

        :param  invocation_id:      the usage id (required)
        :type   invocation_id:      str

        :raises: exceptions.MessageException, exceptions.ObjectNotFound
        """
        decoded_workflow_invocation_id = self.decode_id(invocation_id)
        workflow_invocation = self.workflow_manager.cancel_invocation(trans, decoded_workflow_invocation_id)
        return self.__encode_invocation(workflow_invocation, **kwd)

    @expose_api
    def show_invocation_report(self, trans: GalaxyWebTransaction, invocation_id, **kwd):
        """
        GET /api/workflows/{workflow_id}/invocations/{invocation_id}/report
        GET /api/invocations/{invocation_id}/report

        Get JSON summarizing invocation for reporting.
        """
        kwd["format"] = "json"
        return self.workflow_manager.get_invocation_report(trans, invocation_id, **kwd)

    @expose_api_raw
    def show_invocation_report_pdf(self, trans: GalaxyWebTransaction, invocation_id, **kwd):
        """
        GET /api/workflows/{workflow_id}/invocations/{invocation_id}/report.pdf
        GET /api/invocations/{invocation_id}/report.pdf

        Get JSON summarizing invocation for reporting.
        """
        kwd["format"] = "pdf"
        trans.response.set_content_type("application/pdf")
        return self.workflow_manager.get_invocation_report(trans, invocation_id, **kwd)

    @expose_api
    def invocation_step(self, trans, invocation_id, step_id, **kwd):
        """
        GET /api/workflows/{workflow_id}/invocations/{invocation_id}/steps/{step_id}
        GET /api/invocations/{invocation_id}/steps/{step_id}

        :param  invocation_id:      the invocation id (required)
        :type   invocation_id:      str

        :param  step_id:      encoded id of the WorkflowInvocationStep (required)
        :type   step_id:      str

        :param  payload:       payload containing update action information
                               for running workflow.

        :raises: exceptions.MessageException, exceptions.ObjectNotFound
        """
        decoded_invocation_step_id = self.decode_id(step_id)
        invocation_step = self.workflow_manager.get_invocation_step(trans, decoded_invocation_step_id)
        return self.__encode_invocation_step(trans, invocation_step)

    @expose_api_anonymous_and_sessionless
    def invocation_step_jobs_summary(self, trans: GalaxyWebTransaction, invocation_id, **kwd):
        """
        GET /api/workflows/{workflow_id}/invocations/{invocation_id}/step_jobs_summary
        GET /api/invocations/{invocation_id}/step_jobs_summary

        return job state summary info aggregated across per step of the workflow invocation

        Warning: We allow anyone to fetch job state information about any object they
        can guess an encoded ID for - it isn't considered protected data. This keeps
        polling IDs as part of state calculation for large histories and collections as
        efficient as possible.

        :param  invocation_id:    the invocation id (required)
        :type   invocation_id:    str

        :rtype:     dict[]
        :returns:   an array of job summary object dictionaries for each step
        """
        decoded_invocation_id = self.decode_id(invocation_id)
        ids = []
        types = []
        for job_source_type, job_source_id, _ in invocation_job_source_iter(trans.sa_session, decoded_invocation_id):
            ids.append(job_source_id)
            types.append(job_source_type)
        return [self.encode_all_ids(trans, s) for s in fetch_job_states(trans.sa_session, ids, types)]

    @expose_api_anonymous_and_sessionless
    def invocation_jobs_summary(self, trans: GalaxyWebTransaction, invocation_id, **kwd):
        """
        GET /api/workflows/{workflow_id}/invocations/{invocation_id}/jobs_summary
        GET /api/invocations/{invocation_id}/jobs_summary

        return job state summary info aggregated across all current jobs of workflow invocation

        Warning: We allow anyone to fetch job state information about any object they
        can guess an encoded ID for - it isn't considered protected data. This keeps
        polling IDs as part of state calculation for large histories and collections as
        efficient as possible.

        :param  invocation_id:    the invocation id (required)
        :type   invocation_id:    str

        :rtype:     dict
        :returns:   a job summary object merged for all steps in workflow invocation
        """
        ids = [self.decode_id(invocation_id)]
        types = ["WorkflowInvocation"]
        return [self.encode_all_ids(trans, s) for s in fetch_job_states(trans.sa_session, ids, types)][0]

    @expose_api
    def update_invocation_step(self, trans: GalaxyWebTransaction, invocation_id, step_id, payload, **kwd):
        """
        PUT /api/workflows/{workflow_id}/invocations/{invocation_id}/steps/{step_id}
        PUT /api/invocations/{invocation_id}/steps/{step_id}

        Update state of running workflow step invocation - still very nebulous
        but this would be for stuff like confirming paused steps can proceed
        etc....

        :param  invocation_id:      the usage id (required)
        :type   invocation_id:      str

        :param  step_id:      encoded id of the WorkflowInvocationStep (required)
        :type   step_id:      str

        :raises: exceptions.MessageException, exceptions.ObjectNotFound
        """
        decoded_invocation_step_id = self.decode_id(step_id)
        action = payload.get("action", None)

        invocation_step = self.workflow_manager.update_invocation_step(
            trans,
            decoded_invocation_step_id,
            action=action,
        )
        return self.__encode_invocation_step(trans, invocation_step)

    def _workflow_from_dict(self, trans, data, workflow_create_options, source=None):
        """Creates a workflow from a dict.

        Created workflow is stored in the database and returned.
        """
        publish = workflow_create_options.publish
        importable = workflow_create_options.is_importable
        if publish and not importable:
            raise exceptions.RequestParameterInvalidException("Published workflow must be importable.")

        workflow_contents_manager = self.app.workflow_contents_manager
        raw_workflow_description = workflow_contents_manager.ensure_raw_description(data)
        created_workflow = workflow_contents_manager.build_workflow_from_raw_description(
            trans,
            raw_workflow_description,
            workflow_create_options,
            source=source,
        )
        if importable:
            self._make_item_accessible(trans.sa_session, created_workflow.stored_workflow)
            with transaction(trans.sa_session):
                trans.sa_session.commit()

        self._import_tools_if_needed(trans, workflow_create_options, raw_workflow_description)
        return created_workflow.stored_workflow, created_workflow.missing_tools

    def _import_tools_if_needed(self, trans, workflow_create_options, raw_workflow_description):
        if not workflow_create_options.import_tools:
            return

        if not trans.user_is_admin:
            raise exceptions.AdminRequiredException()

        data = raw_workflow_description.as_dict

        tools = {}
        for key in data["steps"]:
            item = data["steps"][key]
            if item is not None:
                if "tool_shed_repository" in item:
                    tool_shed_repository = item["tool_shed_repository"]
                    if (
                        "owner" in tool_shed_repository
                        and "changeset_revision" in tool_shed_repository
                        and "name" in tool_shed_repository
                        and "tool_shed" in tool_shed_repository
                    ):
                        toolstr = (
                            tool_shed_repository["owner"]
                            + tool_shed_repository["changeset_revision"]
                            + tool_shed_repository["name"]
                            + tool_shed_repository["tool_shed"]
                        )
                        tools[toolstr] = tool_shed_repository

        irm = InstallRepositoryManager(self.app)
        install_options = workflow_create_options.install_options
        for k in tools:
            item = tools[k]
            tool_shed_url = f"https://{item['tool_shed']}/"
            name = item["name"]
            owner = item["owner"]
            changeset_revision = item["changeset_revision"]
            irm.install(tool_shed_url, name, owner, changeset_revision, install_options)

    def __encode_invocation_step(self, trans: ProvidesUserContext, invocation_step):
        return self.encode_all_ids(trans, invocation_step.to_dict("element"), True)

    def __get_stored_accessible_workflow(self, trans, workflow_id, **kwd):
        instance = util.string_as_bool(kwd.get("instance", "false"))
        return self.workflow_manager.get_stored_accessible_workflow(trans, workflow_id, by_stored_id=not instance)

    def __get_stored_workflow(self, trans, workflow_id, **kwd):
        instance = util.string_as_bool(kwd.get("instance", "false"))
        return self.workflow_manager.get_stored_workflow(trans, workflow_id, by_stored_id=not instance)

    def __encode_invocation(self, invocation, **kwd):
        params = InvocationSerializationParams(**kwd)
        return self.invocations_service.serialize_workflow_invocation(invocation, params)


StoredWorkflowIDPathParam: DecodedDatabaseIdField = Path(
    ..., title="Stored Workflow ID", description="The encoded database identifier of the Stored Workflow."
)

InvocationIDPathParam: DecodedDatabaseIdField = Path(
    ..., title="Invocation ID", description="The encoded database identifier of the Invocation."
)

DeletedQueryParam: bool = Query(
    default=False, title="Display deleted", description="Whether to restrict result to deleted workflows."
)

HiddenQueryParam: bool = Query(
    default=False, title="Display hidden", description="Whether to restrict result to hidden workflows."
)

MissingToolsQueryParam: bool = Query(
    default=False,
    title="Display missing tools",
    description="Whether to include a list of missing tools per workflow entry",
)

ShowPublishedQueryParam: Optional[bool] = Query(default=None, title="Include published workflows.", description="")

ShowSharedQueryParam: Optional[bool] = Query(
    default=None, title="Include workflows shared with authenticated user.", description=""
)

SortByQueryParam: Optional[WorkflowSortByEnum] = Query(
    default=None,
    title="Sort workflow index by this attribute",
    description="In unspecified, default ordering depends on other parameters but generally the user's own workflows appear first based on update time",
)

SortDescQueryParam: Optional[bool] = Query(
    default=None,
    title="Sort Descending",
    description="Sort in descending order?",
)

LimitQueryParam: Optional[int] = Query(default=None, title="Limit number of queries.")

OffsetQueryParam: Optional[int] = Query(
    default=0,
    title="Number of workflows to skip in sorted query (to enable pagination).",
)

InstanceQueryParam: Optional[bool] = Query(
    default=False, title="True when fetching by Workflow ID, False when fetching by StoredWorkflow ID."
)

query_tags = [
    IndexQueryTag("name", "The stored workflow's name.", "n"),
    IndexQueryTag(
        "tag",
        "The workflow's tag, if the tag contains a colon an approach will be made to match the key and value of the tag separately.",
        "t",
    ),
    IndexQueryTag("user", "The stored workflow's owner's username.", "u"),
    IndexQueryTag(
        "is:published",
        "Include only published workflows in the final result. Be sure the the query parameter `show_published` is set to `true` if to include all published workflows and not just the requesting user's.",
    ),
    IndexQueryTag(
        "is:share_with_me",
        "Include only workflows shared with the requesting user.  Be sure the the query parameter `show_shared` is set to `true` if to include shared workflows.",
    ),
]

SearchQueryParam: Optional[str] = search_query_param(
    model_name="Stored Workflow",
    tags=query_tags,
    free_text_fields=["name", "tag", "user"],
)

SkipStepCountsQueryParam: bool = Query(
    default=False,
    title="Skip step counts.",
    description="Set this to true to skip joining workflow step counts and optimize the resulting index query. Response objects will not contain step counts.",
)


@router.cbv
class FastAPIWorkflows:
    service: WorkflowsService = depends(WorkflowsService)

    @router.get(
        "/api/workflows",
        summary="Lists stored workflows viewable by the user.",
        response_description="A list with summary stored workflow information per viewable entry.",
    )
    def index(
        self,
        response: Response,
        trans: ProvidesUserContext = DependsOnTrans,
        show_deleted: bool = DeletedQueryParam,
        show_hidden: bool = HiddenQueryParam,
        missing_tools: bool = MissingToolsQueryParam,
        show_published: Optional[bool] = ShowPublishedQueryParam,
        show_shared: Optional[bool] = ShowSharedQueryParam,
        sort_by: Optional[WorkflowSortByEnum] = SortByQueryParam,
        sort_desc: Optional[bool] = SortDescQueryParam,
        limit: Optional[int] = LimitQueryParam,
        offset: Optional[int] = OffsetQueryParam,
        search: Optional[str] = SearchQueryParam,
        skip_step_counts: bool = SkipStepCountsQueryParam,
    ) -> List[Dict[str, Any]]:
        """Lists stored workflows viewable by the user."""
        payload = WorkflowIndexPayload.construct(
            show_published=show_published,
            show_hidden=show_hidden,
            show_deleted=show_deleted,
            show_shared=show_shared,
            missing_tools=missing_tools,
            sort_by=sort_by,
            sort_desc=sort_desc,
            limit=limit,
            offset=offset,
            search=search,
            skip_step_counts=skip_step_counts,
        )
        workflows, total_matches = self.service.index(trans, payload, include_total_count=True)
        response.headers["total_matches"] = str(total_matches)
        return workflows

    @router.get(
        "/api/workflows/{id}/sharing",
        summary="Get the current sharing status of the given item.",
    )
    def sharing(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
    ) -> SharingStatus:
        """Return the sharing status of the item."""
        return self.service.shareable_service.sharing(trans, id)

    @router.put(
        "/api/workflows/{id}/enable_link_access",
        summary="Makes this item accessible by a URL link.",
    )
    def enable_link_access(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
    ) -> SharingStatus:
        """Makes this item accessible by a URL link and return the current sharing status."""
        return self.service.shareable_service.enable_link_access(trans, id)

    @router.put(
        "/api/workflows/{id}/disable_link_access",
        summary="Makes this item inaccessible by a URL link.",
    )
    def disable_link_access(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
    ) -> SharingStatus:
        """Makes this item inaccessible by a URL link and return the current sharing status."""
        return self.service.shareable_service.disable_link_access(trans, id)

    @router.put(
        "/api/workflows/{id}/publish",
        summary="Makes this item public and accessible by a URL link.",
    )
    def publish(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
    ) -> SharingStatus:
        """Makes this item publicly available by a URL link and return the current sharing status."""
        return self.service.shareable_service.publish(trans, id)

    @router.put(
        "/api/workflows/{id}/unpublish",
        summary="Removes this item from the published list.",
    )
    def unpublish(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
    ) -> SharingStatus:
        """Removes this item from the published list and return the current sharing status."""
        return self.service.shareable_service.unpublish(trans, id)

    @router.put(
        "/api/workflows/{id}/share_with_users",
        summary="Share this item with specific users.",
    )
    def share_with_users(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
        payload: ShareWithPayload = Body(...),
    ) -> ShareWithStatus:
        """Shares this item with specific users and return the current sharing status."""
        return self.service.shareable_service.share_with_users(trans, id, payload)

    @router.put(
        "/api/workflows/{id}/slug",
        summary="Set a new slug for this shared item.",
        status_code=status.HTTP_204_NO_CONTENT,
    )
    def set_slug(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
        payload: SetSlugPayload = Body(...),
    ):
        """Sets a new slug to access this item by URL. The new slug must be unique."""
        self.service.shareable_service.set_slug(trans, id, payload)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @router.delete(
        "/api/workflows/{workflow_id}",
        summary="Add the deleted flag to a workflow.",
    )
    def delete_workflow(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        workflow_id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
    ):
        self.service.delete(trans, workflow_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @router.post(
        "/api/workflows/{workflow_id}/undelete",
        summary="Remove the deleted flag from a workflow.",
    )
    def undelete_workflow(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        workflow_id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
    ):
        self.service.undelete(trans, workflow_id)
        return Response(status_code=status.HTTP_204_NO_CONTENT)

    @router.get(
        "/api/workflows/{workflow_id}/versions",
        summary="List all versions of a workflow.",
    )
    def show_versions(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        workflow_id: DecodedDatabaseIdField = StoredWorkflowIDPathParam,
        instance: Optional[bool] = InstanceQueryParam,
    ):
        return self.service.get_versions(trans, workflow_id, instance)

    @router.get(
        "/api/workflows/menu",
        summary="Get workflows present in the tools panel.",
    )
    def get_workflow_menu(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        show_deleted: Optional[bool] = DeletedQueryParam,
        show_hidden: Optional[bool] = HiddenQueryParam,
        missing_tools: Optional[bool] = MissingToolsQueryParam,
        show_published: Optional[bool] = ShowPublishedQueryParam,
        show_shared: Optional[bool] = ShowSharedQueryParam,
    ):
        payload = WorkflowIndexPayload(
            show_published=show_published,
            show_hidden=show_hidden,
            show_deleted=show_deleted,
            show_shared=show_shared,
            missing_tools=missing_tools,
        )
        return self.service.get_workflow_menu(
            trans,
            payload=payload,
        )


@router.cbv
class FastAPIInvocations:
    invocations_service: InvocationsService = depends(InvocationsService)

    @router.post(
        "/api/invocations/{invocation_id}/prepare_store_download",
        summary="Prepare a workflow invocation export-style download.",
    )
    def prepare_store_download(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        invocation_id: DecodedDatabaseIdField = InvocationIDPathParam,
        payload: PrepareStoreDownloadPayload = Body(...),
    ) -> AsyncFile:
        return self.invocations_service.prepare_store_download(
            trans,
            invocation_id,
            payload,
        )

    @router.post(
        "/api/invocations/{invocation_id}/write_store",
        summary="Prepare a workflow invocation export-style download and write to supplied URI.",
    )
    def write_store(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        invocation_id: DecodedDatabaseIdField = InvocationIDPathParam,
        payload: WriteInvocationStoreToPayload = Body(...),
    ) -> AsyncTaskResultSummary:
        rval = self.invocations_service.write_store(
            trans,
            invocation_id,
            payload,
        )
        return rval

    # TODO: remove this endpoint after 23.1 release
    @router.get(
        "/api/invocations/{invocation_id}/biocompute",
        summary="Return a BioCompute Object for the workflow invocation.",
        deprecated=True,
    )
    def export_invocation_bco(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        invocation_id: DecodedDatabaseIdField = InvocationIDPathParam,
        merge_history_metadata: Optional[bool] = Query(default=False),
    ):
        """
        The BioCompute Object endpoints are in beta - important details such
        as how inputs and outputs are represented, how the workflow is encoded,
        and how author and version information is encoded, and how URLs are
        generated will very likely change in important ways over time.

        **Deprecation Notice**: please use the asynchronous short_term_storage export system instead.

        1. call POST `api/invocations/{id}/prepare_store_download` with payload:
            ```
            {
                model_store_format: bco.json
            }
            ```
        2. Get `storageRequestId` from response and poll GET `api/short_term_storage/${storageRequestId}/ready` until `SUCCESS`

        3. Get the resulting file with `api/short_term_storage/${storageRequestId}`
        """
        bco = self._deprecated_generate_bco(trans, invocation_id, merge_history_metadata)
        return json.loads(bco)

    # TODO: remove this endpoint after 23.1 release
    @router.get(
        "/api/invocations/{invocation_id}/biocompute/download",
        summary="Return a BioCompute Object for the workflow invocation as a file for download.",
        response_class=StreamingResponse,
        deprecated=True,
    )
    def download_invocation_bco(
        self,
        trans: ProvidesUserContext = DependsOnTrans,
        invocation_id: DecodedDatabaseIdField = InvocationIDPathParam,
        merge_history_metadata: Optional[bool] = Query(default=False),
    ):
        """
        The BioCompute Object endpoints are in beta - important details such
        as how inputs and outputs are represented, how the workflow is encoded,
        and how author and version information is encoded, and how URLs are
        generated will very likely change in important ways over time.

        **Deprecation Notice**: please use the asynchronous short_term_storage export system instead.

        1. call POST `api/invocations/{id}/prepare_store_download` with payload:
            ```
            {
                model_store_format: bco.json
            }
            ```
        2. Get `storageRequestId` from response and poll GET `api/short_term_storage/${storageRequestId}/ready` until `SUCCESS`

        3. Get the resulting file with `api/short_term_storage/${storageRequestId}`
        """
        bco = self._deprecated_generate_bco(trans, invocation_id, merge_history_metadata)
        return StreamingResponse(
            content=BytesIO(bco),
            media_type="application/json",
            headers={
                "Content-Disposition": f'attachment; filename="bco_{trans.security.encode_id(invocation_id)}.json"',
                "Access-Control-Expose-Headers": "Content-Disposition",
            },
        )

    # TODO: remove this after 23.1 release
    def _deprecated_generate_bco(
        self, trans, invocation_id: DecodedDatabaseIdField, merge_history_metadata: Optional[bool]
    ):
        export_options = BcoExportOptions(
            galaxy_url=trans.request.url_path,
            galaxy_version=VERSION,
            merge_history_metadata=merge_history_metadata or False,
        )
        return self.invocations_service.deprecated_generate_invocation_bco(trans, invocation_id, export_options)
