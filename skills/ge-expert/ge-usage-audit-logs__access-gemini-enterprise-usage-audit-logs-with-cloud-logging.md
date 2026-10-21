# Gemini Enterprise Docs (Monitor usage) / Access Gemini Enterprise usage audit logs with Cloud Logging
Source: https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs, page last updated 2026-10-14, extracted 2026-10-19

This page describes how to set up and access usage audit logs for
Gemini Enterprise.

**Note:** Fields that can contain sensitive data are logged only when **Enable
logging of prompt inputs and response outputs** is turned on. For more
information, see [Logged information](#logged-information).

## Key concepts

This section introduces key concepts related to observability in
Gemini Enterprise.

| Concept | Description |
| --- | --- |
| Usage audit logs | Usage audit logs are records of administrative activities and accesses within your Google Cloud resources. They provide detailed information about who performed what action, when, and from where. These logs are essential for security auditing, compliance, and understanding how your resources are being used. |

## Before you begin

Before configuring audit logs, ensure that you have the following:

- Turn on the observability settings. For more information, see
  [Turn on observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings#turn_on_observability_settings).
- To turn on the audit logging, you must have the
  [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin)
  IAM role (`roles/discoveryengine.agentspaceAdmin`).
- To access Cloud Logging, you must have the
  [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer)
  IAM role (`roles/logging.viewer`).
- Ensure you have created a Gemini Enterprise app. To create one, see
  [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

## Logged information

The following table summarizes the usage data logged by Gemini Enterprise.
Each field is labeled as follows:

- **Sensitive**: The field can contain prompts, responses, or other customer
  content. It's logged only when the **Enable logging of prompt inputs and
  response outputs** setting is turned on. When the setting is off, text
  values are replaced with `<elided>` and other values are omitted. For more
  information, see
  [Turn on observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings#turn_on_observability_settings).
- **Not sensitive**: The field is logged whether or not the setting is
  turned on.
- **Partially sensitive**: Only the listed subfields are sensitive. All other
  subfields are not sensitive.

**Service path**

Logged data

**SearchService.Search**

Logs the data on the sources used for grounding or as LLM input.

Request:

- `query` (sensitive)
- `user_info` (partially sensitive). Only the following subfields are sensitive:
  - `time_zone`
  - `precise_location`

Response:

- `attribution_token` (not sensitive)
- `results.id` (not sensitive)
- `results.document.name` (not sensitive)

**AssistantService.Assist**

Logs the request and response from the Gemini Enterprise assistant.

Request:

- `name` (not sensitive)
- `query.text` (sensitive)
- `query.parts` (sensitive)

Response:

- `assist_token` (not sensitive)
- `answer.name` (not sensitive)
- `answer.state` (not sensitive)
- `answer.replies.grounded_content.text` (sensitive)
- `answer.replies.grounded_content.text_grounding_metadata.segments` (sensitive)
- `answer.replies.grounded_content.text_grounding_metadata.references` (partially sensitive). All subfields are sensitive except `document_metadata.document` and `document_metadata.uri`.
- `answer.skipped_reasons` (not sensitive)
- `agent_info.agent` (not sensitive)
- `agent_info.display_name` (sensitive)
- `agent_info.core_assistant` (not sensitive)
- `agent_info.agent_kind` (not sensitive)
- `agent_info.spiffe_id` (not sensitive)

**AssistantService.StreamAssist**

Request:

- `name` (not sensitive)
- `query.text` (sensitive)
- `query.parts` (sensitive)
- `agents_spec` (partially sensitive). Only the following subfields are sensitive:
  - `agent_specs.input_variables`
  - `agent_specs.node_context.node_input`
  - `agent_specs.node_context.agent_description`
  - `agent_specs.node_context.node_instruction`
  - `agent_specs.artifact_spec.tagged_artifact_content`

Response:

- `assist_token` (not sensitive)
- `answer.name` (not sensitive)
- `answer.state` (not sensitive)
- `answer.replies.grounded_content.text` (sensitive)
- `answer.replies.grounded_content.text_grounding_metadata.segments` (sensitive)
- `answer.replies.grounded_content.text_grounding_metadata.references` (partially sensitive). All subfields are sensitive except `document_metadata.document` and `document_metadata.uri`.
- `answer.skipped_reasons` (not sensitive)
- `agent_info.agent` (not sensitive)
- `agent_info.display_name` (sensitive)
- `agent_info.core_assistant` (not sensitive)
- `agent_info.agent_kind` (not sensitive)
- `agent_info.spiffe_id` (not sensitive)
- `model_info.model` (not sensitive)
- `model_info.requested_model` (not sensitive)
- `model_info.model_selection_mode` (not sensitive)

`model_info.model` is the model that the assistant ran for
the turn. When the request doesn't pin a model,
`model_selection_mode` is
`MODEL_SELECTION_MODE_AUTO` and
`requested_model` is empty; when the request pins one,
`model_selection_mode` is
`MODEL_SELECTION_MODE_EXPLICIT` and
`requested_model` holds the model that was asked for.

A turn can hand off to a specialized agent that runs a different
model. `model_info.model` doesn't report that agent's
model, and a turn that does all of its work in such an agent leaves
`model_info.model` empty.

**ConversationSearchService.AnswerQuery**

Request:

- `serving_config` (not sensitive)
- `query.query_id` (not sensitive)
- `query.text` (sensitive)
- `session` (not sensitive)
- `user_pseudo_id` (not sensitive)
- `end_user_spec` (partially sensitive). Only the following subfields are sensitive:
  - `end_user_metadata.chunk_info.content`
  - `end_user_metadata.chunk_info.document_metadata.title`
- `answer_generation_spec.model_spec.model_version` (not sensitive)
- `answer_generation_spec.prompt_spec.preamble` (sensitive)
- `answer_generation_spec.include_citations` (not sensitive)
- `answer_generation_spec.answer_language_code` (sensitive)
- `answer_generation_spec.ignore_adversarial_query` (not sensitive)
- `answer_generation_spec.ignore_non_answer_seeking_query` (not sensitive)
- `answer_generation_spec.ignore_jail_breaking_query` (not sensitive)

Response:

- `answer` (partially sensitive). Only the following subfields are sensitive:
  - `answer_text`
  - `grounding_supports`
  - `references`
  - `blob_attachments`
  - `steps.actions`
- `answer_query_token` (not sensitive)

**EngineService.CreateEngine**

Request:

- `engine_id` (not sensitive)
- `engine.name` (not sensitive)
- `engine.create_time` (not sensitive)
- `engine.display_name` (not sensitive)
- `engine.update_time` (not sensitive)
- `engine.data_store_ids` (not sensitive)
- `engine.data_stores` (not sensitive)

Response:

- `engine_id` (not sensitive)
- `engine.name` (not sensitive)
- `engine.create_time` (not sensitive)
- `engine.display_name` (not sensitive)
- `engine.update_time` (not sensitive)
- `engine.data_store_ids` (not sensitive)
- `engine.data_stores` (not sensitive)

**EngineService.UpdateEngine**

Request:

- `engine.name` (not sensitive)
- `engine.create_time` (not sensitive)
- `engine.display_name` (not sensitive)
- `engine.update_time` (not sensitive)
- `engine.data_store_ids` (not sensitive)
- `engine.data_stores` (not sensitive)
- `update_mask` (not sensitive)

Response:

- `engine.name` (not sensitive)
- `engine.create_time` (not sensitive)
- `engine.display_name` (not sensitive)
- `engine.update_time` (not sensitive)
- `engine.data_store_ids` (not sensitive)
- `engine.data_stores` (not sensitive)

**AgentService.SetIamPolicy**

Request:

- `policy.bindings.roles` (not sensitive)
- `policy.bindings.members` (not sensitive)

Response:

- `policy.bindings.roles` (not sensitive)
- `policy.bindings.members` (not sensitive)

**AgentService.CreateAgent**

Request:

- `parent` (not sensitive)
- `agent_id` (not sensitive)
- `agent.name` (not sensitive)
- `agent.display_name` (sensitive)
- `agent.create_time` (not sensitive)
- `agent.update_time` (not sensitive)
- `agent.definition_case` (not sensitive)

Response:

- `agent.name` (not sensitive)
- `agent.display_name` (sensitive)
- `agent.create_time` (not sensitive)
- `agent.update_time` (not sensitive)
- `agent.definition_case` (not sensitive)

**AgentService.UpdateAgent**

Request:

- `agent.name` (not sensitive)
- `agent.display_name` (sensitive)
- `agent.create_time` (not sensitive)
- `agent.update_time` (not sensitive)
- `agent.definition_case` (not sensitive)
- `update_mask` (not sensitive)

Response:

- `agent.name` (not sensitive)
- `agent.display_name` (sensitive)
- `agent.create_time` (not sensitive)
- `agent.update_time` (not sensitive)
- `agent.definition_case` (not sensitive)

**AgentService.DeleteAgent**

Request:

- `name` (not sensitive)

Response:

- No fields are logged

**GroundedGenerationService.GenerateGroundedContent**

Request:

- `contents` (sensitive)
- `location` (not sensitive)
- `generation_spec` (partially sensitive). Only the following subfields are sensitive:
  - `language_code`
- `system_instruction` (sensitive)
- `safety_settings` (not sensitive)
- `user_labels` (sensitive)
- `grounding_spec.explicit_search_queries` (sensitive)
- `grounding_spec.grounding_sources` (partially sensitive). Only the following subfields are sensitive:
  - `inline_source`
  - `search_source.filter`
  - `api_source.manifest.api_spec.open_api_yaml`
  - `elastic_source.search_template`
  - `elastic_source.num_hits`
  - `parallel_ai_source.custom_configs`
  - `exa_ai_source.custom_configs`

Response:

- `content` (sensitive)
- `grounding_metadata` (partially sensitive). Only the following subfields are sensitive:
  - `support_chunks`, except `source` and `index`
  - `google_maps_support_chunks`, except `source` and `index`
  - `api_calls.request_payload`
  - `api_calls.response_body`
  - `api_calls.uri`
- `grounding_score` (not sensitive)

**DataConnectorService.UpdateDataConnector**

Request:

- `data_connector.name` (not sensitive)
- `data_connector.create_time` (not sensitive)
- `data_connector.update_time` (not sensitive)
- `data_connector.data_source` (not sensitive)
- `data_connector.refresh_interval` (not sensitive)
- `data_connector.bap_config` (not sensitive)

Response:

- `data_connector.name` (not sensitive)
- `data_connector.create_time` (not sensitive)
- `data_connector.update_time` (not sensitive)
- `data_connector.data_source` (not sensitive)
- `data_connector.refresh_interval` (not sensitive)
- `data_connector.bap_config` (not sensitive)

**AssistantService.AddContextFile**

Request:

- `name` (not sensitive)
- `file_name` (sensitive)

Response:

- `session` (not sensitive)
- `file_id` (not sensitive)

**AssistantService.UploadSessionFile**

Request:

- `name` (not sensitive)
- `blob.filename` (sensitive)

Response:

- `file_id` (not sensitive)

**UserEventService.WriteUserEvent**

Request:

- All fields in the request body (partially sensitive). Only the following subfields are sensitive:
  - `user_event.user_info.time_zone`
  - `user_event.user_info.precise_location`
  - `user_event.filter`
  - `user_event.attributes`
  - `user_event.panel.documents`
  - `user_event.panels.documents`
  - `user_event.search_info.search_query`
  - `user_event.completion_info.selected_suggestion`
  - `user_event.feedback.comment`
  - `user_event.feedback.conversation_info.query`

Response:

- No fields are logged

## Access usage audit logs

To access and view all Gemini Enterprise usage audit logs, follow these steps:

1. In the Google Cloud console, go to the **Logs Explorer** page.

   [Go to Logs Explorer](https://console.cloud.google.com/logs/query)
2. Select the Google Cloud project for which you enabled audit logging.
3. To show only Gemini Enterprise logs, enter the following query in the query
   editor field, and click **Run Query**:

   ```
     logName="projects/PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgemini_enterprise_user_activity" OR logName=~"projects/PROJECT_ID/logs/discoveryengine.googleapis.com%2Fgen_ai.*"
   ```

   Replace the following:

   - `PROJECT_ID`: the ID of your project.

## Control access to logs

You can control access to the logs in Cloud Logging. For detailed guidance
on access control methods, including using IAM conditions for
fine-grained access, see
[Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

### Default access control

By default, Gemini Enterprise sends Cloud Logging data to the `_Default`
bucket. The following IAM roles control access to this bucket:

- [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer)
  role (`roles/logging.viewer`)
- [Private Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.privateLogViewer)
  role (`roles/logging.privateLogViewer`)
- [Logs View Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor)
  role (`roles/logging.viewAccessor`)

### Fine-grained access control

If your project contains logs with varying sensitivity levels, you can use
several Google Cloud and Cloud Logging tools to configure more
fine-grained access control.

You can configure fine-grained access control using the following options:

| Option | Description |
| --- | --- |
| IAM conditions | Set up fine-grained access control using IAM conditions. For more information, see [Logging roles](https://docs.cloud.google.com/logging/docs/access-control#considerations). |
| Log views | Use log views to limit user access to a subset of logs within a log bucket. For more information, see [Configure log views on a log bucket](https://docs.cloud.google.com/logging/docs/logs-views). |
| Log sinks | Use log sinks to route sensitive logs to a separate project with more restrictive IAM access. For more information, see [Route logs to supported destinations](https://docs.cloud.google.com/logging/docs/export/configure_export_v2). |
| Tags | Use tags to manage IAM access to individual log buckets within a project. For more information, see [Use tags to manage access to log buckets](https://docs.cloud.google.com/logging/docs/manage-log-buckets-with-tags). |
| Field-level access control | Use field-level access control to hide or restrict access to specific fields within log entries. For more information, see [Configure field-level access](https://docs.cloud.google.com/logging/docs/field-level-acl). |

## What's next

- To turn off logging of prompt inputs and response outputs, see
  [Turn off observability settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings#turn_off_observability_settings).
