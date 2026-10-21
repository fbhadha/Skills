# Gemini Enterprise: platform, security, agents, cost, monitoring / Share agents from Google Cloud console to Configure field settings
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 547-577, extracted 2026-10-18

Contains:
- Share agents from Google Cloud console (pages 547-553) https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents
- Call a specific agent with the StreamAssist API (pages 554-563) https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-streamassist
- Call an agent using its registry A2A endpoint (pages 564-574) https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-a2a
- Configure field settings (pages 575-577) https://docs.cloud.google.com/gemini/enterprise/docs/configure-field-settings

## Share agents from Google Cloud console

URL: https://docs.cloud.google.com/gemini/enterprise/docs/share-custom-agents

This page explains how to share agents with users in your organization and how administrators can transfer ownership of shared agents. As an administrator, you can share the available agents (Google-made, employee-made, and custom-made) with individual users, groups, Workforce Identity Pool groups, or all users in your organization, and transfer ownership of shared employee-made agents to yourself or another user. For more information about the different types of agents available in Gemini Enterprise, see Agents overview (/gemini/enterprise/docs/agents-overview#types-of-agents). 

**Note:** To share employee-made agents, you must have one or more agents created using Workflow Builder in your Gemini Enterprise web app. For information about creating agents using Workflow Builder, see Create an agent using Workflow Builder (/gemini/enterprise/docs/workflow-builder/create-chat-agent). 

### Before you begin

Before you can share an agent, you must meet the following requirements: 

1. You must have an existing Gemini Enterprise web app. To create a new app, see Create an app (/gemini/enterprise/docs/create-app). 

2. To share custom agents, you must have registered or added the custom agents to Gemini Enterprise using any of the following options: 

   - Register and manage A2A agents (/gemini/enterprise/docs/register-and-manage-an-a2a-agent) 

   - Register and manage ADK agents hosted on Agent Runtime on Gemini Enterprise Agent Platform (/gemini/enterprise/docs/register-and-manage-an-adk-agent) 

   - Add and manage A2A agents from Google Cloud Marketplace (/gemini/enterprise/docs/register-and-manage-marketplace-agents) 

Register and manage Dialogflow agents 

(/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent) 

### Share an agent

To share an agent, follow these steps: 

Console 

- (#console) 

   1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to **Gemini Enterprise** (https://console.cloud.google.com/gemini-enterprise/products) 

1. Select your project. 

2. Click your app from the **Name** column. The navigation menu updates. 

3. Click **Agents** from the navigation menu. 

4. Click the **Display name** of the agent that you want to share. 

5. Click the **User permissions** tab, and the **Permissioned users** page displays. 

6. Click **Add user** . The **Add user permissions roles to agent** dialog displays. 

7. Configure the permission details: 

   - a. Select one of the following options in the **Member type** section: 

      - **User** : An individual end user. For this member type to function, you must include the correct IAM role. For more information, see IAM roles and permissions (/gemini/enterprise/docs/access-control). 

      - **Group** : A collection of end users. For this member type to function, you must include the correct IAM role. For more information, see IAM roles and permissions 

      - (/gemini/enterprise/docs/access-control). 

      - **Principal** : A single identity in a Workforce Identity Pool group, which includes external groups that aren't managed by Google. 

**Workforce identity pool** : All identities in a Workforce Identity Pool. 

**All users** : All users in the organization. 

- b. Enter the unique member identification, and select a role: 

|Member type|Description|
|---|---|
|User|Enter email addresses in the Member field.<br>Select a role in the Assign role field.|
|Group|Enter email addresses in the Member field.<br>Select a role in the Assign role field.|
|Principal|A single identity within a WIF.|
|Workforce identity pool|Enter_Principal identifier_in the Member field.<br>Select a role in the Assign role field.|
||For examples of principal sets, see<br>Principal sets<br>(#principal_sets).|
|All users|Select a role in the Assign role field.|

8. Click **Save** . 

Principal sets 

The following are examples of principal sets that you can specify for the **Workforce identity pool** member type: 

|Principal set|Description|
|---|---|
|`//iam.googleapis.com/locations/global/workforcePools/`<br>_`POOL_ID`_`/subject/`_`SUBJECT_ID`_|A single identity in a WIF.|
|`//iam.googleapis.com/locations/global/workforcePools/`<br>_`POOL_ID`_`/group/`_`GROUP_ID`_|All workforce identities in a<br>group.|
|`//iam.googleapis.com/locations/global/workforcePools/`<br>_`POOL_ID`_`/attribute.`_`ATTRIBUTE_NAME`_`/`_`ATTRIBUTE_VALUE`_|All workforce identities with a<br>specific attribute value.|
|`//iam.googleapis.com/locations/global/workforcePools/`<br>_`POOL_ID`_`/*`|All identities in a workforce<br>identity pool.|

Replace the following placeholders with values in the code sample: 

- _`PROJECT_NUMBER`_ : the number used in the resource path to identify a specific Google Cloud project. 

- _`GROUP_ID`_ : a specific group identifier from an external Identity Provider (IdP), letting you grant access to all members of that group. 

- _`POOL_ID`_ : the unique ID for the workforce identity pool that you create in Google Cloud. 

- _`SUBJECT_ID`_ : the unique subject identifier for a single identity within a workforce identity pool. 

- _`ATTRIBUTE_NAME`_ : a user-defined name of a custom attribute that you have mapped from an external Identity Provider (IdP). 

- _`ATTRIBUTE_VALUE`_ : the specific value of the `ATTRIBUTE_NAME` used to restrict access. 

### Transfer agent ownership

As an administrator, you can transfer ownership of a shared agent to another user in your organization or to yourself. This capability is useful in scenarios such as: 

- **Departing employees:** Transferring agents created by employees who leave the organization to active team members to ensure uninterrupted maintenance. 

- **Contractor handoffs:** Handing over agents created by temporary or contract workers to full-time staff. 

- **Team restructuring:** Reassigning agent responsibilities as roles or projects evolve. 

#### Considerations and limitations

Before transferring agent ownership, note the following considerations and limitations: 

- **Administrator permission:** Only administrators with the Gemini Enterprise Admin (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role ( `roles/discoveryengine.agentspaceAdmin` ) or the Discovery Engine Admin (/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) role 

( `roles/discoveryengine.admin` ) can transfer agent ownership. The current agent owner cannot transfer ownership unless they are also an administrator. 

- **Shared agents only:** You can only transfer ownership of agents that are already shared. On the **Agents** page in the Google Cloud console, the agent's **Sharing** column must display **Enabled** . Private (unshared) agents cannot be transferred. 

- **Single owner:** Each agent has exactly one owner. When ownership is transferred, the selected recipient becomes the sole owner of the agent. 

- **Previous owner access:** When ownership is transferred, the previous owner is demoted to a user on the agent with the `agentUser` role. They retain permission to query and run the agent, but can no longer edit the agent's configuration or settings. 

- **Supported agent types:** Ownership transfer is supported for employee-made agents (low-code and workflow agents created in the web app). 

- **Agents with schedules or triggers:** If the transferred agent has a schedule trigger or event trigger, the transfer operation marks them as disabled schedules or events. The new owner must enable the schedule or event trigger before being able to use the agent. 

#### Transfer ownership of an agent

To transfer ownership of an agent, follow these steps: 

Console 

- (#console) 

   1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to **Gemini Enterprise** (https://console.cloud.google.com/gemini-enterprise/products) 

2. Select your project. 

3. Click your app from the **Name** column. The navigation menu updates. 

4. Click **Agents** from the navigation menu. 

5. Click the **Display name** of the shared agent. 

6. Click the **User permissions** tab. The **Permissioned users** list displays. 

7. Click **Transfer ownership** . The **Transfer ownership** dialog opens. 

8. Under **Transfer ownership to** , choose one of the following options: 

   - **Myself** : Transfer ownership of the agent to your current administrator account. This option is disabled if you already own the agent. 

   - **Another user** : Transfer ownership to another user in your organization. 

9. If you selected **Another user** , specify the new owner: 

   - **Google Identity and Cloud Identity:** Enter the user's email address in the **New owner email** field (for example, `user@example.com` ) . 

**Workforce Identity Federation (WIF) accounts:** Enter the single identity principal identifier in the **New owner principal** field: 

```
//iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/
SUBJECT_ID
```

Alternatively, you can include the `principal:` prefix: 

```
principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/
subject/SUBJECT_ID
```

Replace the following: 

- _POOL_ID_ : The unique ID of your workforce identity pool. 

- _SUBJECT_ID_ : The user's subject identifier in the workforce identity pool. 

**Note:** Workforce Identity Federation principal identifiers are case-sensitive. Ensure that the identifier matches the exact casing configured in your identity provider's **`google.subject`** mapping. 

10. Click **Transfer ownership** . 

The agent's owner is updated. The previous owner is retained as a permissioned user with the `agentUser` role. 

**Note:** If the transferred agent has a schedule trigger or event trigger, the transfer operation marks them as disabled schedules or events. The new owner must enable the trigger before being able to use the agent. 

Last updated 2026-10-14 UTC. 



## Call a specific agent with the StreamAssist API

URL: https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-streamassist

To call a specific registered agent, supply the optional `agentsSpec` field in your `streamAssist` REST API request or client library call. The AgentsSpec API (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/str eamAssist#AgentsSpec) 

defines the specification of agents that are used to serve the request. The assistant routes queries directly to that agent and preserves session context across turns. 

### At a glance

|Specification|Details|
|---|---|
|API method|`projects.locations.collections.engines.assistants.streamAssist`|
|Endpoint<br>versions|`v1alpha`for discovering agent IDs;`v1`for calling`streamAssist`|
|Key paramete|r`agentsSpec.agentSpecs[].agentId`|
|Supported<br>agent types|Core Assistant(/gemini/enterprise/docs/core-assistant),<br>Deep Research<br>(/gemini/enterprise/docs/research-assistant),<br>Workflow Builder<br>(/gemini/enterprise/docs/workflow-builder) chat agents (formerly low-code),<br>and Workflow Builder workflows (see<br>Call a workflow(#workflows))|
|Required IAM<br>permission|`discoveryengine.assistants.assist`|
|Required<br>OAuth scope|`https://www.googleapis.com/auth/cloud-platform`|

### Before you begin

1. Enable the **Discovery Engine API** ( `discoveryengine.googleapis.com` ) in your Google Cloud project. 

2. Ensure your principal (user account or service account) has a role granting the `discoveryengine.assistants.assist` IAM permission, such as **Discovery Engine Editor** ( `roles/discoveryengine.editor` ) or **Gemini Enterprise Admin** ( `roles/discoveryengine.agentspaceAdmin` ). 

3. Verify that your Gemini Enterprise app (engine) is created and contains at least one registered agent. 

4. If you authenticate using Application Default Credentials (ADC), ensure your client sends the quota project header: `-H "X-Goog-User-Project: PROJECT_ID"` . 

### Find your app ID and location

The `streamAssist` URL requires your engine ID and its location ( `global` , `us` , or `eu` ). If you only know the app's display name, list the engines in your project to locate the underlying ID: 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collec
tions/default_collection/engines"
```

In the response, the engine `name` format is 

`projects/{project}/locations/{location}/collections/default_collection/engine s/{ENGINE_ID}` . The `ENGINE_ID` segment is the `APP_ID` required in the call. 

**Note:** The engine ID typically has a numeric suffix appended to the display name (for example, **`my-app_1234567890`** ). 

### Find the agent ID

The `agentId` is the final segment of the agent's full resource name in the Discovery Engine API: 

```
projects/{project}/locations/{location}/collections/{collection}/engines/{engin
e}/assistants/{assistant}/agents/{AGENT_ID}
```

Registered agents use a long numeric ID (for example, `15492003793394502655` ) rather than a friendly display name. Supply only this final `{AGENT_ID}` numeric string in your request. 

To list the agents registered to your app and discover their numeric IDs, call the `agents` collection on the `v1alpha` endpoint: 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://LOCATION-
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/c
ollections/default_collection/engines/APP_ID/assistants/default_assistant/agent
s"
```

**Important:** The **`agents`** collection is served exclusively on the **`v1alpha`** endpoint. Calling this list endpoint on **`v1`** or **`v1beta`** returns an HTTP **`404 Not Found`** error. However, the **`streamAssist`** invocation call itself operates on **`v1`** . 

Each returned agent resource includes the following fields: 

- `name` : The full resource path ending in `{AGENT_ID}` . 

- `displayName` : The human-readable name shown in the Google Cloud console. `state` : The operational state (such as `ENABLED` or `PRIVATE` ). 

A definition object indicating the agent type (such as `a2aAgentDefinition` , `lowCodeAgentDefinition` , or `workflowAgentDefinition` ) . 

See `agents` REST API reference 

(https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.coll ections.engines.assistants.agents) 

for the complete agent resource schema. 

### Send queries to agents

To send queries to a specific agent, you must construct your request with the appropriate `agentsSpec` and execute it using REST or client libraries. 

**Note** : If an agent relies on internal connectors or data stores (such as Document Q&A agents), invoking it without configured data sources generates a "no data sources configured" response rather than an API error. 

#### Request body structure

To route a query to a specific agent, include the optional `agentsSpec` object in your POST request body: 

```
{
 "query": {
   "text": "QUERY_TEXT"
 },
 "session": "SESSION_RESOURCE_NAME",
 "agentsSpec": {
   "agentSpecs": [
     {
       "agentId": "AGENT_ID"
     }
   ]
 }
}
```

Field reference 

- **`agentsSpec`** _(object, optional)_ : Specification of agents used to serve the request. 

- **`agentsSpec.agentSpecs[]`** _(array, optional)_ : A list of agent specifications. You can specify multiple agents in this array. 

- **`agentsSpec.agentSpecs[].agentId`** _(string, required within the spec)_ : The ID identifying the registered agent resource. Must conform to RFC-1034 with a maximum length of 63 characters. 

See `streamAssist` REST API reference 

(https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collectio ns.engines.assistants/streamAssist) for the complete request schema. 

#### Call streamAssist

RESTPython (#python) (#rest) 

The following `curl` command sends a query to a specific agent using the REST API: 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/c
ollections/default_collection/engines/APP_ID/assistants/default_assistant:
streamAssist" \
 -d '{
   "query": {
     "text": "List all contact cards."
   },
   "agentsSpec": {
     "agentSpecs": [
       {
         "agentId": "AGENT_ID"
       }
     ]
   }
 }'
```

Replace the following placeholders: 

- **`LOCATION`** : The multi-region for both the hostname and resource path ( `global` , `us` , or `eu` ) . If your app resides in the `global` location, omit the location prefix from the hostname ( `discoveryengine.googleapis.com` ). 

- **`PROJECT_ID`** : Your Google Cloud project ID. 

- **`APP_ID`** : Your Gemini Enterprise engine ID (discovered in Find your app ID and location (#find-app-id)). 

- **`AGENT_ID`** : The numeric agent ID (discovered in Find the agent ID (#find-agent-id)). 

#### Understand the streaming response

The `streamAssist` endpoint returns a stream of JSON chunks over REST, or an iterator of response objects in client libraries: 

- **Answer text** : Incremental response text arrives in 

- `answer.replies[].groundedContent.content.text` . Concatenate these text fragments in receipt order to reconstruct the complete answer. 

- **Reasoning fragments** : Fragments marked with `"thought": true` represent the model's internal reasoning process. Filter out these fragments when presenting the final output to end users. 

- **Execution state** : The `answer.state` field progresses from `IN_PROGRESS` to a terminal state: 

   - `SUCCEEDED` : The request completed and generated an answer. 

   - `SKIPPED` : The query was ignored or bypassed. Inspect `assistSkippedReasons` for details (such as `NON_ASSIST_SEEKING_QUERY_IGNORED` for brief greetings). 

`FAILED` : The invocation encountered an execution error. 

- **Session continuity** : The terminal chunk includes `sessionInfo.session` (the session resource name) and an `assistToken` . 

#### Continue the conversation in the same session

To maintain context across turns, pass the `session` string from `sessionInfo` in subsequent requests: 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/collec
tions/default_collection/engines/APP_ID/assistants/default_assistant:streamAssi
st" \
 -d '{
   "session":
"projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/
APP_ID/sessions/SESSION_ID",
   "query": {
     "text": "Who is John Doe?"
   },
   "agentsSpec": {
     "agentSpecs": [
       {
         "agentId": "AGENT_ID"
       }
     ]
   }
 }'
```

If you omit the `session` field or specify `-` as the session ID, the API generates a new, isolated session automatically. 

### Call a workflow

To run a Workflow Builder workflow, send the same request with the workflow's ID in `agentsSpec.agentSpecs[].agentId` . Each call starts a manual run of the workflow. 

- **Version that runs** : If the workflow is published, the call runs its published version. Changes saved in Workflow Builder but not yet published don't affect API callers until you publish them. If the workflow has never been published, the call runs its draft. 

- **Who can call it** : The workflow's owner and admins can call it. Other users can call a published workflow after it's shared with them. Only the owner or an admin can call a workflow that has never been published; other callers receive `HTTP 403` . 

- **Triggers** : The workflow must have exactly one manual trigger. Calls fail for a workflow that combines a manual trigger with any other trigger, or that has more than one manual trigger. 

- **Inputs** : You can't set the manual trigger's input variables through `streamAssist` . If the manual trigger has a required input, the run fails, even if the input has a default value. Optional inputs are empty, and their default values aren't applied. The query text is passed to the workflow's LLM nodes, so you can include data there, but it doesn't fill input variables. 

### Limitations

- The following limitations apply when calling agents with `streamAssist` : 

   - **Unsupported agent types** : A2A or ADK agents registered to a Gemini Enterprise app are not supported through `streamAssist` . To call an A2A agent directly using its registry endpoint, see Call an agent using its registry A2A endpoint (/gemini/enterprise/docs/invoke-agent-a2a). 

   - **Mutative actions** : The `streamAssist` API is optimized for conversational queries and read-only retrieval over connectors. Programmatic execution of mutative tools and actions (such as email drafting, calendar event creation, or chat messaging) is not supported over `streamAssist` . Attempting to invoke an agent workflow that executes mutative actions may result in silent failures or ungrounded execution loops. 

### Troubleshooting

|Symptom|Likely cause|Resolution|
|---|---|---|
|HTTP 404 when listing<br>agents|Calling`agents`on the`v1`or<br>`v1beta`endpoint.|Send the list request to the`v1alpha`<br>endpoint instead.|
|Response appears<br>generic despite setting<br>`agentsSpec`|Invalid numeric`agentId`, or<br>the query is too generic to<br>trigger domain behavior.|Confirm the exact numeric ID from the<br>`v1alpha`agent list; send a domain-<br>specific query; check response text for<br>agent-specific wording.|
|No error returned, but<br>target agent did not<br>execute|Malformed`agentId`caused<br>a silent fallback to default<br>orchestration.|Verify that the`agentId`consists of digits<br>only and exactly matches an ID from the<br>registry list.|
|Response state returns<br>`SKIPPED`|Input evaluated as a non-<br>assist-seeking query (such<br>as a brief greeting).|Send a substantive task query; inspect<br>`assistSkippedReasons`in the response<br>payload.|
|`HTTP 401`or`HTTP 403`<br>`Permission Denied`|Missing OAuth scope,<br>insufficient IAM role, or<br>missing quota project<br>header.|Verify the caller has`discoveryengine.`<br>`assistants.assist`; ensure OAuth scope<br>includes`cloud-platform`; add`-H "X-`<br>`Goog-User-Project: PROJECT_ID"`if<br>using ADC.|
|`HTTP 403`with`Only the`<br>`agent owner or an`<br>`admin can run a`<br>`draft of this agent.`|<br>The workflow has never<br>been published, and the<br>caller isn't its owner or an<br>admin.|Publish the workflow in Workflow Builder<br>and share it with the caller.|
|`HTTP 403`with`User`<br>`does not have`<br>`permission to access`<br>`the Agent.`|<br>The workflow isn't shared<br>with the caller.|Share the workflow with the caller.|
|Workflow behaves like<br>an older version|The call runs the published<br>version, not unpublished<br>changes in Workflow<br>Builder.|Publish the workflow.|
|Workflow call ends with<br>`answer.state` `FAILED`<br>and an`INTERNAL`error|The workflow has a manual<br>trigger plus another trigger,<br>or more than one manual<br>trigger.|Keep a single manual trigger.|

### What's next

Get search results from StreamAssist 

- (/gemini/enterprise/docs/get-answers-from-streamassist) 

streamAssist REST API reference 

(https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.coll ections.engines.assistants/streamAssist) 

Agents overview (/gemini/enterprise/docs/agents-overview) 

Last updated 2026-10-14 UTC. 



## Call an agent using its registry A2A endpoint

URL: https://docs.cloud.google.com/gemini/enterprise/docs/invoke-agent-a2a

Agent2Agent (A2A) agents in Agent Registry advertise protocol interfaces containing an endpoint URL and a protocol binding (such as `HTTP_JSON` ). You can discover an agent's URL in the registry to call its A2A methods from custom orchestrators or clients. 

### At a glance

|Specification|Details|
|---|---|
|Discovery API|`agentregistry.googleapis.com`(`v1`)|
|Invocation proxy host|`LOCATION-discoveryengine.googleapis.com`|
|Protocol binding|`HTTP_JSON`|
|URL project identifier|Google Cloud project number (not project ID)|
|Supported A2A<br>methods|`GET /v1/card`,`POST /v1/message:send`,`POST /v1/message:stream`|
|Required message<br>schema|`message.role = "ROLE_USER"`,`content[].text`, unique`messageId`|
|Required IAM<br>permissions|`roles/agentregistry.viewer`(discovery) and`discoveryengine.`<br>`assistants.assist`(invocation)|

### Before you begin

1. Enable the **Agent Registry API** ( `agentregistry.googleapis.com` ) and **Discovery Engine API** ( `discoveryengine.googleapis.com` ) in your Google Cloud project. 

2. If the agent was not created directly in your Gemini Enterprise app, import the agent from Agent Registry and grant end users access to it. For instructions, see Import A2A agents from Agent Registry 

   - (/gemini/enterprise/docs/import-govern-agent-registry). 

3. Grant your caller principal appropriate IAM permissions: 

      - **To read the registry** : Agent Registry Viewer 

      - ( `roles/agentregistry.viewer` ) . 

      - **To invoke the agent** : Discovery Engine Editor ( `roles/discoveryengine.editor` ) or a custom role including `discoveryengine.assistants.assist` . 

4. If you authenticate using Application Default Credentials (ADC), configure your client to send the quota project header: `-H "X-Goog-User-Project: PROJECT_ID"` . 

5. Optionally, install the Agent Development Kit (ADK) library if you plan to wrap remote agents as programmatic sub-agents: `pip install "googleadk[a2a]>=1.29.0"` . 

### Step 1: Discover the agent and its A2A endpoint

To invoke an A2A agent, first discover its advertised `url` in Agent Registry. List the agents in your registry location (such as `us` or `eu` , passed as a path parameter on the global `agentregistry.googleapis.com` host): 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://agentregistry.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION
/agents?pageSize=100"
```

You can also search for an agent by display name prefix using the Google Cloud CLI: 

```
gcloud agent-registry agents search \
```

- `--project=PROJECT_ID \` 

- `--location=LOCATION \` 

```
 --search-string="displayName:My_Agent_*"
```

**Note:** If the **`agent-registry`** command group is unrecognized, run **`gcloud components update`** to update your CLI distribution. 

In the returned agent resource, inspect the `protocols` array. Locate the entry where `type` equals `A2A_AGENT` and `interfaces[].protocolBinding` equals `HTTP_JSON` . Extract the corresponding `url` : 

```
{
 "name": "projects/PROJECT_ID/locations/LOCATION/agents/AGENT_RESOURCE_ID",
 "displayName": "My Agent",
 "protocols": [
   {
     "type": "A2A_AGENT",
     "protocolVersion": "0.3.0",
     "interfaces": [
       {
         "url": "https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/co
llections/default_collection/engines/ENGINE_ID/assistants/default_assistant/age
nts/AGENT_ID/a2a",
         "protocolBinding": "HTTP_JSON"
       }
     ]
   }
 ]
}
```

**Important:** Use the returned **`url`** string verbatim. For Gemini Enterprise agents, this URL routes traffic through the Discovery Engine A2A proxy and embeds your Google Cloud project 

**number** rather than project ID. Not all registered agents expose an A2A interface; if **`protocols`** is empty or omits **`A2A_AGENT`** , the agent cannot be invoked over A2A. 

See `projects.locations.agents` REST API reference 

(/agent-registry/reference/rest/v1/projects.locations.agents) for the complete agent resource schema. 

### Step 2: Fetch the agent card

The agent card provides metadata describing the agent's identity, description, and input/output capabilities. To retrieve the card, send an HTTP GET request to the `/v1/card` path appended to the agent's A2A endpoint URL: 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"A2A_ENDPOINT_URL/v1/card"
```

Example response payload: 

```
{
 "name": "My Agent",
 "description": "What the agent does.",
 "url": "A2A_ENDPOINT_URL",
 "capabilities": {},
 "defaultInputModes": ["text"],
 "defaultOutputModes": ["text"],
 "preferredTransport": "HTTP+JSON"
}
```

**Note:** Ensure you request **`/v1/card`** . Alternative path variations (such as **`/v1:getCard`** , **`/v1/getCard`** , or **`/.well-known/agent-card.json`** ) return an HTTP **`404 Not Found`** error on the HTTP+JSON protocol binding. 

### Step 3: Send a message

To send a user query to the agent, make a POST request to `/v1/message:send` . The request body must conform to the A2A message schema, requiring `role` set to `ROLE_USER` , a `content` array containing text parts, and a uniquely generated `messageId` : 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"A2A_ENDPOINT_URL/v1/message:send" \
 -d '{
   "message": {
     "role": "ROLE_USER",
     "content": [
       {
         "text": "What can you help me with?"
       }
     ],
     "messageId": "UNIQUE_UUID_STRING"
   }
 }'
```

In the response payload, the agent's reply is returned within the `message` object: 

```
{
 "message": {
   "contextId":
"projects/PROJECT_NUMBER/locations/LOCATION/collections/default_collection/engi
nes/ENGINE_ID/sessions/SESSION_ID",
   "role": "ROLE_AGENT",
   "content": [
     {
       "text": "I am an AI assistant..."
     }
   ]
 }
}
```

Concatenate the text strings inside `content[].text` to display the complete response. To continue the conversation within the same session, save the returned `contextId` string and supply it as `message.contextId` in your next request. 

See A2A `message:send` REST API reference 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants.ag ents.a2a.v1.message/send) 

for the complete message payload schema. 

### Stream responses incrementally

For streaming output, send a POST request with an identical message body to `/v1/message:stream` : 

```
curl -N -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"A2A_ENDPOINT_URL/v1/message:stream" \
 -d '{
   "message": {
     "role": "ROLE_USER",
     "content": [
       {
         "text": "Say hello."
       }
     ],
     "messageId": "UNIQUE_UUID_STRING"
   }
 }'
```

The endpoint returns a JSON array of streamed chunk objects over HTTP. Append the `content[].text` fragments sequentially as they arrive. Streamed chunks also contain `metadata.sessionInfo` and `metadata.assistToken` . 

See A2A `message:stream` REST API reference 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants.ag ents.a2a.v1.message/stream) 

for the streaming payload specification. 

### Call an A2A endpoint using Python

This Python script resolves an A2A endpoint in Agent Registry and sends a message using raw HTTP requests: 

```
Install dependencies: pip install google-auth requests
import uuid
import google.auth
from google.auth.transport.requests import AuthorizedSession
TODO(developer): Replace placeholder values with your project ID and
location.
project_id = "PROJECT_ID"
location = "LOCATION"          # Registry location (for example: "us" or "eu")
target_display_name = "My Agent"
query_text = "What can you help me with?"
Initialize credentials and authorized session
creds, _ = google.auth.default(
   scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
session = AuthorizedSession(creds)
Step 1: Resolve the A2A endpoint URL from the Agent Registry
registry_url = (
   f"https://agentregistry.googleapis.com/v1/"
   f"projects/{project_id}/locations/{location}/agents"
)
response = session.get(registry_url)
response.raise_for_status()
agents = response.json().get("agents", [])
def get_a2a_url(agent_resource):
   for proto in agent_resource.get("protocols") or []:
       if proto.get("type") == "A2A_AGENT":
           for iface in proto.get("interfaces", []):
               if iface.get("protocolBinding") == "HTTP_JSON":
                   return iface.get("url")
   return None
target_agent = next(
   (a for a in agents if a.get("displayName") == target_display_name),
   None
)
if not target_agent:
   raise SystemExit(f"Agent '{target_display_name}' not found in registry.")
endpoint_url = get_a2a_url(target_agent)
if not endpoint_url:
   raise SystemExit("Target agent does not publish an HTTP_JSON A2A
endpoint.")
Step 2: Fetch and verify the agent card
card_resp = session.get(f"{endpoint_url}/v1/card")
card_resp.raise_for_status()
card = card_resp.json()
print("Resolved Agent:", card.get("name"))
Step 3: Send an A2A message
body = {
   "message": {
       "role": "ROLE_USER",
       "content": [{"text": query_text}],
       "messageId": str(uuid.uuid4()),
   }
}
send_resp = session.post(f"{endpoint_url}/v1/message:send", json=body)
send_resp.raise_for_status()
reply_message = send_resp.json().get("message", {})
full_reply_text = "".join(
   part.get("text", "") for part in reply_message.get("content", [])
)
print("Agent Reply:", full_reply_text)
```

### Simplify orchestration using the ADK

The Agent Development Kit (ADK) resolves registry endpoints automatically and wraps remote A2A agents as sub-agents: 

```
from google.adk.integrations.agent_registry import AgentRegistry
Initialize registry client
registry = AgentRegistry(project_id="PROJECT_ID", location="LOCATION")
Resolve remote A2A agent directly by resource name
remote_agent = registry.get_remote_a2a_agent(
   agent_name="agents/AGENT_RESOURCE_ID"
)
```

**Note:** This integration requires **`google-adk[a2a]>=1.29.0`** . For more details, see Resolve endpoints and build orchestrators (/agent-registry/resolve-endpoints-and-build-orchestrators) . 

### Additional notes

A2A endpoints have the following behaviors: 

- **Strict path naming** : Only `GET {url}/v1/card` , `POST {url}/v1/message:send` , and `POST {url}/v1/message:stream` are supported for HTTP+JSON bindings. 

- **Strict schema validation** : Passing plain `"user"` as the role returns an HTTP `400 Bad Request` error. You must pass the enum string `"ROLE_USER"` . Similarly, message text must reside inside the `content` array rather than `parts` , and `messageId` is strictly required. 

- **Non-A2A agent invocation error** : If an agent lacks an `A2A_AGENT` protocol entry in the registry (such as certain prebuilt or managed agents), calling `getCard` on its proxy URL returns `501 UNIMPLEMENTED` ( _"... is not supported yet"_ ), and calling `message:send` returns `400 INVALID_ARGUMENT` ( _"Unsupported agent"_ ). 

- **Project number in URL** : The registry returns an A2A URL containing the project number rather than the project ID. Do not alter this numeric string 

when making HTTP requests. 

### Troubleshooting

Use the following table to troubleshoot common A2A endpoint errors: 

|Symptom|Likely cause|Resolution|
|---|---|---|
|HTTP 404 on<br>`getCard`request|Using an incorrect path alias<br>(such as`/v1:getCard`or`/.`<br>`well-known/agent-card.`<br>`json`).|<br>Send the GET request strictly to`GET {url}/`<br>`v1/card`.|
|HTTP 400 *"Unknow<br>name 'parts'"*|n<br>Using old or generative AI<br>client body formatting.|Place text strings inside`content`, not`parts`.|
|HTTP 400 invalid<br>enum value for`rol`|`e`<br>Passing lowercase`"user"`o<br>`"user_role"`.|r<br>Set`message.role`exactly to`"ROLE_USER"`.|
|HTTP 501 *"is not<br>supported yet"*|Calling`getCard`on an agen<br>that does not publish an<br>A2A interface.|t<br>Inspect the registry resource's`protocols`<br>array to confirm`A2A_AGENT`support before<br>calling.|
|HTTP 400<br>*"Unsupported<br>agent"*|Calling`message:send`on a<br>non-A2A agent.|Choose an agent whose registry definition<br>includes an active`A2A_AGENT`protocol<br>binding.|
|`HTTP 401`or`HTTP`<br>`403 Permission`<br>`Denied`|Missing OAuth scopes,<br>missing IAM roles, or<br>missing quota project<br>header.|Check caller IAM roles (`agentregistry.`<br>`viewer`and`assistants.assist`); verify<br>`cloud-platform`scope; pass`-H "X-Goog-`<br>`User-Project: PROJECT_ID"`if using ADC.|

### Related resources

- Agent Registry overview (/gemini-enterprise-agent-platform/govern/agent-registry) 

- Search for agents and tools in Agent Registry (/agent-registry/search-agents-and-tools) 

Resolve endpoints and build orchestrators (ADK) 

(/agent-registry/resolve-endpoints-and-build-orchestrators) 

A2A message:send REST API reference 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistan ts.agents.a2a.v1.message/send) 

Last updated 2026-10-14 UTC. 



## Configure field settings

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-field-settings

This page shows you how to configure the fields to set up an app for structured data or for unstructured data with metadata. 

Field settings help determine how Gemini Enterprise uses fields in its results. You can use the **Schema** tab in the Google Cloud console to configure field settings for structured data and unstructured data with metadata. 

Configuring field settings is available only for apps with data stores that have either structured data or unstructured data with metadata. 

The following field settings are available: 

|Field setting|Definition|Use<br>case|
|---|---|---|
|Indexable|If a field is set to Indexable, Gemini Enterprise can filter, order, and facet<br>using this field. Setting boolean and object fields to indexable is not<br>supported.|Search|
|Searchable|If a field is set to Searchable, recall for that field in Gemini Enterprise<br>queries is improved. Only fields with text values can be set to Searchable.|Search|
|Dynamic<br>facetable|If a field is set to Dynamic Facetable, Gemini Enterprise can use that field<br>as a dynamic facet. Dynamic facets can be automatically added to a<br>search based on previous user behavior such as facet clicks and views.<br>This setting is applicable only to fields that are indexable.|Search|
|Retrievable|If a field is set to Retrievable, Gemini Enterprise returns the field in search<br>results.|Search|
|Completable|If a field is set to Completable, Gemini Enterprise uses the field's contents<br>as search query suggestions. For more information, see<br>Configure<br>autocomplete(/gemini/enterprise/docs/configure-autocomplete).|Search|

### Limitations

Field settings have the following limitations: 

- You can configure up to 50 fields as indexable, searchable, retrievable, or dynamic facetable. 

- To configure a field as dynamic facetable, it must first be configured as indexable. 

- Changing the indexable setting requires re-indexing the data, which can take hours, especially for large data stores. 

### Update field settings

To update field settings: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the app that you want to edit. 

3. Click **Data** . 

4. Click the **Schema** tab. This tab shows current field settings. 

5. Click **Edit** . 

6. Select or clear field settings that you need to update. Some field settings are not supported. For example, numerical fields cannot be set to **Searchable** . 

7. Click **Save** to apply your changes. 

### What's next

- Update a schema for structured data (/gemini/enterprise/docs/update-schemas) Configure results for the UI (/gemini/enterprise/docs/configure-ui-results) 

- Preview search results (/gemini/enterprise/docs/preview-search-results) 

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC.
