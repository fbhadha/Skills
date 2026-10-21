# Agent Platform, Model Armor and data governance / Integrate Model Armor with Gemini Enterprise to Data residency and endpoints
Source: 03-Agent-Platform-Model-Armor-and-data-governance.pdf, pages 85-109, extracted 2026-10-18

Contains:
- Integrate Model Armor with Gemini Enterprise (pages 85-88) https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration
- Integrate Model Armor with Agent Gateway (pages 89-100) https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration
- Data residency and endpoints (pages 101-109) https://docs.cloud.google.com/model-armor/data-residency

## Integrate Model Armor with Gemini Enterprise

URL: https://docs.cloud.google.com/model-armor/model-armor-gemini-enterprise-integration

Integrating Model Armor with Gemini Enterprise (/gemini/enterprise/docs) lets you screen user prompts to and responses from your AI agents, mitigating risks such as prompt injection, harmful content, and sensitive data leakage. After the integration is set up, it applies to all user interactions. 

### Before you begin

Create a Model Armor template and ensure that it is in the same Google Cloud project as Gemini Enterprise. The location of the template and the Gemini Enterprise instance must match. For more information about supported locations, see Model Armor locations (/model-armor/locations) and Gemini Enterprise locations (/gemini/enterprise/docs/locations). 

#### Required roles

Before you integrate Model Armor with Gemini Enterprise, ensure that you have the required role. 

To get the permissions that you need to create and manage Model Armor templates, ask your administrator to grant you the Model Armor Admin 

(/iam/docs/roles-permissions/modelarmor#modelarmor.admin) ( `roles/modelarmor.admin` ) IAM role on Model Armor templates. For more information about granting roles, see Manage access to projects, folders, and organizations 

(/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through custom roles (/iam/docs/creating-custom-roles) or other predefined roles (/iam/docs/roles-overview#predefined). 

### Enable the integration

To enable Gemini Enterprise with Model Armor, your security administrator creates policies in Model Armor and your Gemini Enterprise administrator applies these policies to the Gemini Enterprise instance. 

1. Create a Model Armor template (/model-armor/manage-templates). 

2. Enable and configure Model Armor in Gemini Enterprise (/gemini/enterprise/docs/enable-model-armor). 

### Limitations and considerations

Consider the following limitations and considerations when integrating Model Armor with Gemini Enterprise: 

- **De-identification and masking** : When Model Armor uses a Sensitive Data Protection template for scanning prompts or responses, Model Armor checks if the content matches the infoType detector criteria defined in the template. Although Sensitive Data Protection supports de-identification based on the template configuration, Model Armor doesn't pass de-identified or masked data back to Gemini Enterprise. If the content triggers any infoType detectors from Sensitive Data Protection and the enforcement type is 

- `INSPECT_AND_BLOCK` , Gemini Enterprise blocks the request or response rather than de-identifying it. 

- **Document and image screening** : In addition to text prompts, the integration supports documents 

- (/model-armor/overview#ma-support-screening-pdfs) (such as PDFs) and images. The integration screens the following files only when you upload them to the Gemini Enterprise assistant 

- (/gemini/enterprise/docs/assistant-chat#upload_and_chat_about_files): 

   - Images that you upload directly. 

   - Images contained inside other files and documents that you upload directly. 

If a file or an image inside a document violates your configured policies, the entire file or document is discarded and excluded from the request. 

- **Screened agents and interactions** : Screening applies to the Gemini Enterprise assistant, employee-made agents (created in the Gemini Enterprise app using the Workflow Builder), and Google-made agents. Interactions with custom agents from your organization (such as ADK, A2A, and Dialogflow) are not screened. 

- **Token limits and quotas** : There are no token limits when you use Model Armor with Gemini Enterprise. However, the total throughput of Model Armor evaluations is governed by Gemini Enterprise system quotas 

- (/gemini/enterprise/docs/quotas-and-overages) and Model Armor API rate limits 

- (/model-armor/quotas#quotas). 

- **Service Level Agreement (SLA)** : Gemini Enterprise provides a Service Level Agreement (https://cloud.google.com/terms/gemini/enterprise/sla). When Gemini Enterprise is configured to use Model Armor, blocked queries don't count as SLA violations, regardless of whether the **fail-open** or **fail-closed** mode is used. 

- **Compliance** : Both Gemini Enterprise and Model Armor offer various compliance certifications. When used together, the effective compliance certifications are the common subset of both products. Review the compliance certifications for both products to ensure that they meet your regulatory requirements. 

### How it works

After the integration is configured, Gemini Enterprise routes user inputs and assistant outputs through the Model Armor API for screening using the selected templates. The Gemini Enterprise authenticates to Model Armor using the service agent. Model Armor responds based on the filter configuration defined in the template, which Gemini Enterprise acts upon by either blocking the request or response or allowing it. 

For example, Gemini Enterprise might detect a request containing personally identifiable information and route it to Model Armor for screening. If the Model Armor template is configured to block personally identifiable information (PII), it tells Gemini Enterprise to block the request. 

### Logging

Model Armor generates platform logs for sanitization requests and their responses in Cloud Logging. You need the Private Logs Viewer 

( `roles/logging.privateLogViewer` ) IAM role to view the Model Armor audit logs. For more information about the auto-generated audit logs, see Model Armor audit logging (/model-armor/audit-logging-model-armor). 

To log the sanitize operations, set the `templateMetadata.logSanitizeOperations` field to `true` . For more information, see Configure logging in templates (/model-armor/configure-logging#configure-logging-templates). 

### What's next

- Enable Model Armor in Gemini Enterprise 

- (/gemini/enterprise/docs/enable-model-armor) 

- Correlate Model Armor logs with Gemini Enterprise logs 

- (/gemini/enterprise/docs/correlate-model-armor-logs) 

Last updated 2026-10-13 UTC. 



## Integrate Model Armor with Agent Gateway

URL: https://docs.cloud.google.com/model-armor/model-armor-agent-gateway-integration

Gemini Enterprise Agent Platform is a platform for building and managing enterprise-grade AI agents. Agent Gateway 

(/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) serves as a control plane that manages, secures, and governs how AI agents connect and interact within the Google Cloud environment and with external agents, AI applications, and LLMs. The integration of Model Armor and Agent Gateway embeds Model Armor's screening capabilities directly into the communication pathways Gemini Enterprise Agent Platform manages. When content passes through Agent Gateway, it invokes Model Armor to enforce your predefined security templates. You can configure your template to either block and redact content that violates policies, or to only inspect content and log any violations that are detected. This mitigates risks such as prompt injection, jailbreaks, exposure to harmful content, and sensitive data leakage. 

When Model Armor detects policy violations in content passing through Agent Gateway, it can be configured to log these events. You can view these findings on the **Model Armor** page in the Google Cloud console (Go to Model Armor (https://console.cloud.google.com/security/model-armor)). These findings are also surfaced in Security Command Center. For more information, see Review findings in the Google Cloud console 

(/security-command-center/docs/concepts-vulnerabilities-findings#review-ma-findings). 

When using the real-time streaming mode, Model Armor supports unlimited tokens in the stream, making it suitable for long-running interactions and model responses. 

### Limitations

Consider the following limitations when integrating Model Armor with Agent Gateway: 

- **Streaming support for agents** : Model Armor only supports streaming sanitization using the `streamQuery` method for agents built with the Agent Development Kit. 

- **Cross-project template usage** : When using a Model Armor template in one project to sanitize requests for a service, like Agent Gateway, in a different project, the API quota for Model Armor needs to be sufficient in both the project hosting the template and the project hosting the calling service. For more information, see Manage quota (/model-armor/integrations#manage-quota). 

- **Regional alignment** : Model Armor and the services it integrates with must be deployed within the same Google Cloud region. Cross-region calls to Model Armor are not supported. 

- **Egress integration compatibility** : Model Armor's inline protection on egress traffic is limited to integrations with MCP servers, services following the OpenAI format (/vertex-ai/generative-ai/docs/start/openai), and A2A through Agent Gateway. 

- **Ingress integration compatibility** : Inline ingress protection with Model Armor is only supported for agents built using ADK. 

- **No document support** : Sanitizing prompts and responses that contain documents or file uploads (such as PDFs) isn't supported in this integration. To screen documents, call the Model Armor REST API 

- (/model-armor/sanitize-prompts-responses#file-prompts) directly. 

- **Supported payloads** : For a list of supported payloads, see Supported and unsupported payloads (#supported-unsupported-payloads) in this document. 

### Configure Model Armor on a gateway

To configure Model Armor on a gateway, follow these steps: 

1. Enable the Model Armor API (/model-armor/manage-templates#enable-apis) in the project where you want to create the Model Armor templates. 

2. Create one or more Model Armor templates (/model-armor/manage-templates#create-ma-template) in the same region where 

you plan to add the gateway. You can use the same template for both ingress and egress traffic. 

Take note of the template names. To copy the name of a template in the Google Cloud console, view the template's details 

(/model-armor/manage-templates#view-ma-template) and click **Copy to clipboard** next to the template name. 

3. Set up Agent Gateway in the same region where the Model Armor templates are stored. For the Client-to-Agent (ingress) gateway 

(/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway#configclient-to-agent) 

- , specify the Model Armor templates that you created for ingress traffic. For the Agent-to-Anywhere (egress) gateway 

(/gemini-enterprise-agent-platform/govern/gateways/set-up-agent-gateway#configagent-to-anywhere) 

, specify the Model Armor templates that you created for egress traffic. You can use the same template for both traffic flows. 

4. Grant the required IAM roles to the appropriate service agents: 

**Client-to-Agent (ingress)** : Grant the AI Platform Reasoning Engine Service Agent 

(/gemini-enterprise-agent-platform/scale/runtime/manage-agent-access#serviceagent) 

service agent the following roles: 

- The Model Armor Callout User ( `roles/modelarmor.calloutUser` ) role in the project that contains the AI agent. 

- The Model Armor User ( `roles/modelarmor.user` ) role in the project that contains the Model Armor template. 

```
gcloud projects add-iam-policy-binding AGENT_RUNTIME_PROJECT_ID \
   --member=serviceAccount:service-AGENT_RUNTIME_PROJECT_NUMBER@gcp-
sa-aiplatform-re.iam.gserviceaccount.com \
   --role=roles/modelarmor.calloutUser
gcloud projects add-iam-policy-binding MODEL_ARMOR_PROJECT_ID \
   --member=serviceAccount:service-AGENT_RUNTIME_PROJECT_NUMBER@gcp-
sa-aiplatform-re.iam.gserviceaccount.com \
   --role=roles/modelarmor.user
```

Replace the following: 

   - _`AGENT_RUNTIME_PROJECT_ID`_ : The project ID of the project where you created the agent. 

   - _`AGENT_RUNTIME_PROJECT_NUMBER`_ : The project number of the project where you created the agent. 

   - _`MODEL_ARMOR_PROJECT_ID`_ : The project ID of the project that contains the Model Armor template. 

- **Agent-to-Anywhere (egress)** : Grant the Service Extensions service agent the following roles: 

   - The Model Armor Callout User ( `roles/modelarmor.calloutUser` ) and Service Usage Consumer 

   - ( `roles/serviceusage.serviceUsageConsumer` ) roles in the project that contains the gateway. 

   - The Model Armor User ( `roles/modelarmor.user` ) role in the project that contains the Model Armor template. 

```
gcloud projects add-iam-policy-binding GATEWAY_PROJECT_ID \
   --member=serviceAccount:service-GATEWAY_PROJECT_NUMBER@gcp-sa-
dep.iam.gserviceaccount.com \
   --role=roles/modelarmor.calloutUser
gcloud projects add-iam-policy-binding GATEWAY_PROJECT_ID \
   --member=serviceAccount:service-GATEWAY_PROJECT_NUMBER@gcp-sa-
dep.iam.gserviceaccount.com \
   --role=roles/serviceusage.serviceUsageConsumer
gcloud projects add-iam-policy-binding MODEL_ARMOR_PROJECT_ID \
   --member=serviceAccount:service-GATEWAY_PROJECT_NUMBER@gcp-sa-
dep.iam.gserviceaccount.com \
   --role=roles/modelarmor.user
```

Replace the following: 

- _`GATEWAY_PROJECT_ID`_ : The project ID of the project where you created the gateway. 

- _`GATEWAY_PROJECT_NUMBER`_ : The project number of the project where you created the gateway. 

- _`MODEL_ARMOR_PROJECT_ID`_ : The project ID of the project that contains the Model Armor template. 

For instructions, see Delegate authorization to Model Armor (/gemini-enterprise-agent-platform/govern/gateways/delegateauthorization#configure-authz-ma) 

For general information about how to grant a role, see Grant a single IAM role (/iam/docs/granting-changing-revoking-access#grant-single-role). 

### Ingress and egress traffic

In the context of Agent Gateway and Model Armor integration, the terms _ingress_ and _egress_ are used from the perspective of the AI agent's interactions: 

- **Ingress Traffic (Client-to-Agent):** Refers to the communication flow between a client and the agent. Model Armor can protect both the incoming requests from the client to the agent and the outgoing responses from the agent back to the client. 

- **Egress Traffic (Agent-to-Anywhere):** Refers to the communication flow between the agent and an external system. Model Armor can protect both the outgoing requests from the agent to the external system and the incoming responses from the external system back to the agent. 

#### Client-to-Agent (ingress) protection

You define templates that Model Armor uses to evaluate: 

- Incoming requests from the _client_ (end users or calling applications) to your AI agent. 

- Outgoing responses from the AI agent back to the client. 

You can apply a single template to both directions or configure different templates for each. 

Traffic flow for Client-to-Agent 

1. A client sends a prompt to the agent. Agent Gateway intercepts the request and sends the payload to Model Armor. 

2. Model Armor screens the request. If blocked, the client receives an error. 

3. If allowed, the request reaches the AI agent. 

4. The AI agent generates a response. Agent Gateway intercepts this response before it reaches the client. 

5. Model Armor screens the response, and Agent Gateway either allows or blocks it based on the verdict. 

#### Agent-to-Anywhere (egress) protection

You define templates that Model Armor uses to evaluate: 

- Outgoing requests from your AI agent to external systems. 

Incoming responses from external systems back to your AI agent. 

This protection applies to communications with systems including: 

- External LLMs and third-party AI agents 

- Model Context Protocol (MCP) servers 

- Other AI agents 

Traffic flow for Agent-to-Anywhere 

1. The AI agent initiates a request to an external system. Agent Gateway intercepts the outgoing traffic. 

2. Model Armor screens the outgoing payload. If blocked, the connection is terminated. 

3. If allowed, the request is sent to the external system. 

4. The external system sends a response back. Agent Gateway intercepts this incoming response. 

5. Model Armor screens the response payload, and Agent Gateway either allows it to reach the agent or blocks it. 

For more information, see Configure Model Armor on a gateway (/gemini-enterprise-agent-platform/govern/configure-model-armor). 

### Track and debug streaming requests

To facilitate tracking and debugging of streaming requests, Model Armor uses a correlation ID and a trace ID. 

#### Use a trace ID

A trace ID connects all events for a single request as it travels across multiple services in a distributed system. This includes the security enforcements that Model Armor applies within the request path of the Agent Gateway resource. 

Each trace contains one or more spans, where each span ID represents a specific operation or unit of work within the trace. Logs generated during the execution of a request are associated with the specific span ID of the operation performing the work. 

A trace ID is handled in two ways: 

- **Automatic** : When Google Cloud Observability is enabled, Agent Gateway automatically generates a trace ID and propagates it through the system. 

- **User-provided** : You can override the system-generated trace ID by providing your own using the traceparent HTTP header in your requests. 

The following code sample shows how to pass a custom trace ID in a request to the `streamQuery` method: 

```
curl -X POST \
 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
 -H "Content-Type: application/json" \
 -H "traceparent: 00-98adffecc8dd095968a06c44216190f6-5b565a8342378cd7-
01" \
 "https://LOCATION-
aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/reason
ingEngines/REASONING_ENGINE_ID:streamQuery?alt=sse"
```

Replace the following: 

- _`LOCATION`_ : the region where the reasoning engine is located. 

- _`PROJECT_ID`_ : the ID of your Google Cloud project. 

- _`REASONING_ENGINE_ID`_ : the ID of your reasoning engine. 

Using a trace ID is the recommended method to correlate logs and traces end-toend from the caller through Agent Gateway to Model Armor and any downstream agents. This is essential for debugging, understanding security actions, and monitoring performance. For more information, see View Model Armor trace spans (/gemini-enterprise-agent-platform/govern/view-model-armor-spans). 

To view sanitization operation logs for a specific trace ID, use the following query in the Logs Explorer: 

```
jsonPayload.@type="type.googleapis.com/google.cloud.modelarmor.logging.v1.Sanit
izeOperationLogEntry"
trace:TRACE_ID
```

Replace _`TRACE_ID`_ with the trace ID of your request. 

#### Use a correlation ID

A correlation ID links together all log entries in Cloud Logging that pertain to a single streaming sanitization session, from the initial request to the final response. It is an internal identifier primarily used within Model Armor logs, specifically for ingress streaming sessions. For more information, see Correlate logs and related events (/model-armor/configure-logging#correlate-logs-and-events). 

### Supported and unsupported payloads

This section lists the types of payloads that Model Armor sanitizes. 

#### Client-to-Agent (ingress) traffic

For Client-to-Agent (ingress) traffic using the ADK protocol, Model Armor sanitizes only `reasoningEngines.streamQuery` 

(/vertex-ai/generative- 

ai/docs/reference/rest/v1/projects.locations.reasoningEngines/streamQuery) 

requests and responses for agents that were built using Agent Development Kit (ADK) and are running on Agent Runtime. 

All other `ReasoningEngine` 

(/vertex-ai/generative-ai/docs/reference/rest/v1/projects.locations.reasoningEngines) payloads and `ReasoningEngine` error responses aren't sent to Model Armor. Non-ADK payloads (such as Langchain payloads) are also not sent to Model Armor. 

#### Agent-to-Anywhere (egress) traffic

For Agent-to-Anywhere (egress) traffic, the following payloads are supported. 

A2A payloads 

Model Armor sanitizes only the following payloads of the A2A v1 protocol (https://a2a-protocol.org/latest/): 

- Send Message (https://a2a-protocol.org/latest/specification/#311-send-message) operations 

- Agent Card (https://a2a-protocol.org/latest/specification/#441-agentcard) 

Get Extended Agent Card 

- (https://a2a-protocol.org/latest/specification/#3111-get-extended-agent-card) operations 

- JSON-RPC (https://a2a-protocol.org/latest/specification/#9-json-rpc-protocol-binding) protocol bindings 

HTTP+JSON/REST 

(https://a2a-protocol.org/latest/specification/#11-httpjsonrest-protocol-binding) protocol bindings 

Model Armor allows the following A2A payloads without sanitization: 

- Payloads from A2A versions earlier than v1 

- `SendStreamingMessage` 

- (https://a2a-protocol.org/latest/specification/#942-sendstreamingmessage) 

- `GetTask` (https://a2a-protocol.org/latest/specification/#943-gettask) 

- `ListTasks` (https://a2a-protocol.org/latest/specification/#944-listtasks) 

- `CancelTask` (https://a2a-protocol.org/latest/specification/#945-canceltask) 

- `SubscribeToTask` (https://a2a-protocol.org/latest/specification/#946-subscribetotask) 

- CRUD methods 

- (https://a2a-protocol.org/latest/specification/#1047-createtaskpushnotificationconfig) on `TaskPushNotificationConfig` 

- Payloads using A2A gRPC 

(https://a2a-protocol.org/latest/specification/#10-grpc-protocol-binding) protocol binding (protobuf on the wire) 

- A2A error payloads 

MCP payloads 

Model Armor sanitizes only the following MCP payloads: 

- `tools/call` request and response 

- `prompts/get` request and response 

- MCP tool execution errors 

- (https://modelcontextprotocol.io/specification/2025-11-25/server/tools#error-handling) (target for prompt injection by malicious MCP tools authors) 

Model Armor allows the following payloads without sanitization: 

- `tools/list` 

`resources/*` 

`notifications/*` 

Streamable HTTP/SSE for MCP 

MCP protocol errors (for example, all errors other than tool execution errors) 

External LLM payloads 

Model Armor sanitizes only the following payloads of the OpenAI API protocol (egress), which includes GPT models on `openai.com` as well as any other models through OpenAI API-compatible LLM servers (such as vLLM 

(https://docs.vllm.ai/en/latest/serving/openai_compatible_server/#supported-apis)). Payloads that aren't listed here are allowed without sanitization. 

Chat completions 

(https://developers.openai.com/api/reference/resources/chat/subresources/completions): Create, Delete, Get, List, and Update (non-streaming variants only) 

Get chat messages 

- (https://developers.openai.com/api/reference/resources/chat/subresources/completions/s ubresources/messages) 

- Responses (https://developers.openai.com/api/reference/resources/responses): Create, Get, and Delete (non-streaming variants only) 

OpenAI API errors 

(https://community.openai.com/t/error-code-for-openai-chat-completion/1102402) (including vLLM's variant (https://github.com/vllm-project/vllm/issues/12886)) 

Legacy Completions 

(https://developers.openai.com/api/reference/resources/beta/subresources/assistants) 

Legacy Assistants 

(https://developers.openai.com/api/reference/resources/beta/subresources/assistants/me thods/create) 

: Create, Delete, List, Modify, and Retrieve 

Legacy Messages 

(https://developers.openai.com/api/reference/resources/beta/subresources/threads/subre sources/messages) 

: Create, Delete, List, Modify, and Retrieve 

Legacy Threads 

- (https://developers.openai.com/api/reference/resources/beta/subresources/threads/meth ods/create) 

- : Create, Delete, Modify, and Retrieve 

Embeddings 

(https://developers.openai.com/api/reference/resources/embeddings/methods/create): Create 

Last updated 2026-10-13 UTC. 



## Data residency and endpoints

URL: https://docs.cloud.google.com/model-armor/data-residency

This document explains when data residency is enforced in each location where Model Armor is available. Data residency lets you specify a geographic region where your data is stored and processed, which helps ensure that your data remains in that location. Model Armor helps provide control over where your data is handled, supporting compliance with various regulations. 

Model Armor processes the following types of data: 

- **Core data** : The primary data that Model Armor processes, most relevant to data residency, which includes prompts, responses, and input files. Model Armor processes core data but doesn't store it at rest. For more information, see Data handling and storage (/model-armor/overview#data-handling). 

- **Configuration data** : Template and floor setting configurations such as rules, filters, and thresholds that Model Armor uses to scan prompts and responses. Model Armor processes and stores configuration data at rest. 

### Data residency enforcement for templates

This section indicates the data residency controls enforced by Model Armor templates for each supported Google Cloud location. Model Armor maintains data residency at the jurisdiction level, for example, a specific country like India, or a multi-region like `eu` . 

**Note:** The information in this section also applies to all Model Armor integrations (/model-armor/integrations)—except for the integration with Google and Google Cloud MCP servers, which doesn't support Model Armor templates. 

Model Armor works in the following regions and multi-regions. However, by default, Model Armor has limited feature support in some regions to maintain strict data residency, including in-jurisdiction data processing. For information about the regions with full and limited support, see Feature availability by region (/model-armor/feature-availability-by-region). 

If you must use a limited-support region but you want to prioritize comprehensive security filtering over strict data residency, you can disable data residency enforcement (/model-armor/manage-templates#set-data-residency-compliance) in your Model Armor template. 

|Region/multi-<br>region|Jurisdiction|At<br>rest|In<br>use<br>In<br>trans|it<sup>Feature support1</sup>|
|---|---|---|---|---|
|`asia-`<br>`northeast1`|Japan<br>(/assured-workloads/docs/control-<br>packages/japan-data-boundary)|Yes|Yes Yes|Limited support<br>(/model-armor/feature-<br>availability-by-<br>region#limited-support)|
|`asia-`<br>`northeast3`|South Korea<br>(/assured-workloads/docs/control-<br>packages/south-korea-data-<br>boundary)|Yes|Yes Yes|Limited support<br>(/model-armor/feature-<br>availability-by-<br>region#limited-support)|
|`asia-south1`|India<br>(/assured-workloads/docs/control-<br>packages/india-data-boundary)|Yes|Yes Yes|Limited support<br>(/model-armor/feature-<br>availability-by-<br>region#limited-support)|
|`asia-`<br>`southeast1`|Singapore<br>(/assured-workloads/docs/control-<br>packages/singapore-data-<br>boundary)|Yes|Yes Yes|Limited support<br>(/model-armor/feature-<br>availability-by-<br>region#limited-support)|
|`australia-`<br>`southeast2`|Australia<br>(/assured-workloads/docs/control-<br>packages/australia-data-boundary)|Yes|Yes Yes|Limited support<br>(/model-armor/feature-<br>availability-by-<br>region#limited-support)|
|`eu`|European Union<br>(/assured-workloads/docs/control-<br>packages/eu-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|
|`europe-`<br>`southwest1`|European Union<br>(/assured-workloads/docs/control-<br>packages/eu-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|

|Region/multi-<br>region|Jurisdiction|At<br>rest|In<br>use<br>In<br>trans|it<sup>Feature support1</sup>|
|---|---|---|---|---|
|`europe-west1`|European Union<br>(/assured-workloads/docs/control-<br>packages/eu-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|
|`europe-west2`|United Kingdom<br>(/assured-workloads/docs/control-<br>packages/uk-data-boundary)|Yes|Yes Yes|Limited support<br>(/model-armor/feature-<br>availability-by-<br>region#limited-support)|
|`europe-west3`|European Union<br>(/assured-workloads/docs/control-<br>packages/eu-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|
|`europe-west4`|European Union<br>(/assured-workloads/docs/control-<br>packages/eu-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|
|`europe-west9`|European Union<br>(/assured-workloads/docs/control-<br>packages/eu-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|
|`northamerica-`<br>`northeast2`|Canada<br>(/assured-workloads/docs/control-<br>packages/canada-data-boundary)|Yes|Yes Yes|Limited support<br>(/model-armor/feature-<br>availability-by-<br>region#limited-support)|
|`us`|United States<br>(/assured-workloads/docs/control-<br>packages/us-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|
|`us-central1`|United States<br>(/assured-workloads/docs/control-<br>packages/us-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|

|Region/multi-<br>region|Jurisdiction|At<br>rest|In<br>use<br>In<br>trans|it<sup>Feature support1</sup>|
|---|---|---|---|---|
|`us-east1`|United States<br>(/assured-workloads/docs/control-<br>packages/us-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|
|`us-east4`|United States<br>(/assured-workloads/docs/control-<br>packages/us-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|
|`us-west1`|United States<br>(/assured-workloads/docs/control-<br>packages/us-data-boundary)|Yes|Yes Yes|Full support<br>(/model-armor/feature-<br>availability-by-region#full-<br>support)|

1The **Feature support** column is relevant only to Model Armor configurations that use templates. For Model Armor configurations that use floor settings, all features are available but data residency enforcement for data in use and in transit varies by location. 

The **Jurisdiction** column indicates the geographical boundary (for example, a country or a multi-region like `eu` or `us` ) within which Model Armor ensures data residency compliance for the supported states (at rest, in use, and in transit) as indicated in the table. 

The **Region/multi-region** column lists the specific Google Cloud region or multiregion identifier. 

When data residency is enforced for a region in Model Armor, it helps ensure that data remains within a specified jurisdiction while in at least one of the following states: 

- **At rest** : Stored data remains within the specific Google Cloud region listed. **In use** and **In transit** : Data residency enforcement for these states within the specified jurisdiction depends on the values in the **In use** and **In transit** columns: 

   - **Yes** : Data residency is enforced for the _In use_ and _In transit_ states within the listed jurisdiction. This means that the data remains within the 

boundaries of the listed jurisdiction while being processed or transmitted (not necessarily within that single region). 

- **No** : Data residency is not enforced for the _In use_ and _In transit_ states within the listed jurisdiction. This means that the data might be processed or transmitted outside of the jurisdiction. 

**Note:** For Assured Workloads, Model Armor maintains data residency within the selected jurisdiction for supported locations (/model-armor/locations) for data in use. For more information, see Assured Workloads Service Specific Terms 

(https://cloud.google.com/terms/service-terms#37). 

### Data residency for Model Armor integrations using floor settings

The following sections explain how data residency is enforced for Model Armor floor settings across integrations. 

#### Integration with Gemini Enterprise Agent Platform

If you use floor settings for the Agent Platform integration 

(/model-armor/model-armor-vertex-integration), all Model Armor features are available in the following locations. However, data residency enforcement for data in use and in transit varies by region. 

**Note:** Floor settings for the Agent Platform integration don't apply to requests sent to Agent Platform multi-regional endpoints 

(/gemini-enterprise-agent-platform/resources/locations#multi-region_endpoints), such as **`aiplatform.us.rep.googleapis.com`** or **`aiplatform.eu.rep.googleapis.com`** . 

<sup>Show supported regions</sup> 

|Region|Jurisdiction|At<br>rest|In<br>use|In<br>transit|
|---|---|---|---|---|
|`asia-northeast1`|Japan<br>(/assured-workloads/docs/control-packages/japan-data-<br>boundary)|Yes|No|No|
|`asia-northeast3`|South Korea<br>(/assured-workloads/docs/control-packages/south-korea-<br>data-boundary)|Yes|No|No|
|`asia-south1`|India<br>(/assured-workloads/docs/control-packages/india-data-<br>boundary)|Yes|No|No|
|`asia-southeast1`|Singapore<br>(/assured-workloads/docs/control-packages/singapore-<br>data-boundary)|Yes|No|No|
|`australia-`<br>`southeast2`|Australia<br>(/assured-workloads/docs/control-packages/australia-<br>data-boundary)|Yes|No|No|
|`europe-`<br>`southwest1`|European Union<br>(/assured-workloads/docs/control-packages/eu-data-<br>boundary)|Yes|Yes|Yes|
|`europe-west1`|European Union<br>(/assured-workloads/docs/control-packages/eu-data-<br>boundary)|Yes|Yes|Yes|
|`europe-west2`|United Kingdom<br>(/assured-workloads/docs/control-packages/uk-data-<br>boundary)|Yes|No|No|
|`europe-west3`|European Union<br>(/assured-workloads/docs/control-packages/eu-data-<br>boundary)|Yes|Yes|Yes|
|`europe-west4`|European Union<br>(/assured-workloads/docs/control-packages/eu-data-<br>boundary)|Yes|Yes|Yes|
|`europe-west9`|European Union<br>(/assured-workloads/docs/control-packages/eu-data-<br>boundary)|Yes|Yes|Yes|

|Region|Jurisdiction|At<br>rest|In<br>use|In<br>transit|
|---|---|---|---|---|
|`northamerica-`<br>`northeast2`|Canada<br>(/assured-workloads/docs/control-packages/canada-data-<br>boundary)|Yes|No|No|
|`us-central1`|United States<br>(/assured-workloads/docs/control-packages/us-data-<br>boundary)|Yes|Yes|Yes|
|`us-east1`|United States<br>(/assured-workloads/docs/control-packages/us-data-<br>boundary)|Yes|Yes|Yes|
|`us-east4`|United States<br>(/assured-workloads/docs/control-packages/us-data-<br>boundary)|Yes|Yes|Yes|
|`us-west1`|United States<br>(/assured-workloads/docs/control-packages/us-data-<br>boundary)|Yes|Yes|Yes|

#### Integration with Google and Google Cloud MCP servers

Model Armor is a regionalized service, but it's not available in every Google Cloud region where Google and Google Cloud MCP servers operate. If you enable Model Armor for an MCP-supported service 

(/model-armor/model-armor-mcp-google-cloud-integration) in a jurisdiction where Model Armor isn't present, Model Armor is called depending on whether the MCPsupported service uses _cross-jurisdictional routing_ or _data residency compliant routing_ . 

Google and Google Cloud MCP servers with cross-jurisdictional routing 

For Google and Google Cloud MCP servers 

(/model-armor/model-armor-mcp-google-cloud-integration) with cross-jurisdictional routing (/mcp/model-armor-supported-products#cross-jurisdictional-routing), Model Armor is always called if enabled. Cross-jurisdictional calls might impact data residency compliance for in-use and in-transit data. 

To see which Google and Google Cloud MCP servers use cross-jurisdictional routing, see Products with Model Armor support 

(/mcp/model-armor-supported-products#products-with-ma-support). 

Google and Google Cloud MCP servers with data residency compliant routing 

For Google and Google Cloud MCP servers with data residency compliant routing (/mcp/model-armor-supported-products#drz-compliant), Model Armor can be called in any region or multi-region within the European Union and the United States jurisdictions. Data residency is enforced for data at rest, in use, and in transit. 

To see which Google and Google Cloud MCP servers use data residency compliant routing, see Products with Model Armor support 

(/mcp/model-armor-supported-products#products-with-ma-support). 

### Regional and multi-regional endpoints

Regional and multi-regional endpoints provide access to resources in a specific location. When you use a regional or multi-regional endpoint, your request is routed directly to the endpoint's location. 

Each regional or multi-regional endpoint uses the following format: 

```
modelarmor.LOCATION.rep.googleapis.com
```

Replace _`LOCATION`_ with a supported Model Armor region or multi-region. 

To create, update, or use templates to sanitize content, you must use a regional or multi-regional endpoint that matches the template's location. 

Regional and multi-regional Model Armor endpoints don't support managing floor settings. 

For general information about using regional and multi-regional endpoints, see Google Cloud API endpoint overview (/docs/security/compliance/endpoints). 

#### VPC network requirements

To access Model Armor regional endpoints from within a VPC network, you must create a Private Service Connect endpoint 

(/vpc/docs/access-regional-google-apis-endpoints#create-regional-endpoint) to the Model Armor APIs. This is required to prevent certificate errors when regional endpoints are accessed using Private Google Access or VPC Service Controls. For more information, see Troubleshoot Model Armor issues 

(/model-armor/troubleshooting#ma-certificate-error) and About accessing regional endpoints through Private Service Connect endpoints 

(/vpc/docs/about-accessing-regional-google-apis-endpoints). 

### Global endpoint

The global endpoint ( `modelarmor.googleapis.com` ) is supported only for managing Model Armor floor settings (/model-armor/configure-floor-settings). 

The global Model Armor endpoint doesn't support managing Model Armor templates or sanitizing prompts and responses. 

For general information about global endpoints, see Google Cloud API endpoint overview (/docs/security/compliance/endpoints). 

Last updated 2026-10-13 UTC.
