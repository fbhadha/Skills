# Gemini Enterprise: platform, security, agents, cost, monitoring / Agents overview to Tutorial: Host an agent on Cloud Run
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 440-479, extracted 2026-10-18

Contains:
- Agents overview (pages 440-444) https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview
- Register and manage Dialogflow agents (pages 445-450) https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent
- Register and manage A2A agents (pages 451-461) https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent
- Register and manage (pages 462-469) https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent
- Configure cross-project access (pages 470-471) https://docs.cloud.google.com/gemini/enterprise/docs/configure-cross-project-adk-agents
- Register and manage (pages 472-474) https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/register-and-manage-an-a2ui-agent
- Tutorial: Host an agent on Cloud Run (pages 475-479) https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/tutorial-host-agent-cloud-run

## Agents overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/agents-overview

Gemini Enterprise provides centralized oversight and management for agents used by your organization, including those from Google, third parties, and internal teams. 

### Agent types

The following table details the different types of agents available in Gemini Enterprise, the Gemini Enterprise tools that are used to create the agent, and the admin configurations required to view and manage them on the web app. 

|Agent type|Gemini Enterprise<br>tool|Description|
|---|---|---|
|Employee-made<br>agents from your<br>organization|Workflow Builder|This interactive, no-code, low-code tool lets users in your<br>organization create, launch, and manage single and<br>multi-step agents on the Gemini Enterprise web app. For<br>more information, see<br>Workflow Builder overview<br>(/gemini/enterprise/docs/workflow-builder).<br>A Gemini Enterprise admin must enable this feature on<br>the web app by turning on the Enable Workflow Builder<br>toggle in the End user features control page. For more<br>information, see<br>Manage web app features<br>(/gemini/enterprise/docs/manage-web-app-features).|
|Google-made<br>agents|Core Assistant|Handles interactions when users talk to the Gemini<br>Enterprise engine without specifying any other agent.<br>For more information, see<br>Core Assistant agent<br>(/gemini/enterprise/docs/core-assistant).|
||Deep Research|Helps users perform in-depth exploration of topics. For<br>more information, see<br>Get reports with Deep Research<br>(/gemini/enterprise/docs/research-assistant).|

|Agent type|Gemini Enterprise<br>tool|Description|
|---|---|---|
|Custom agents<br>from your<br>organization|ADK agents hosted<br>on Agent Runtime<br>on Gemini<br>Enterprise Agent<br>Platform|<br>Gemini Enterprise admins can register custom agents<br>built by your organization and hosted on Agent Runtime,<br>making them available to users on the Gemini Enterprise<br>web app. For more information, see<br>Register and<br>manage ADK agents<br>(/gemini/enterprise/docs/register-and-manage-an-adk-<br>agent)<br>.|
||Agent2Agent<br>(A2A)|Gemini Enterprise admins can register custom agents<br>built using the<br>Agent2Agent (A2A) Protocol<br>(https://a2a-protocol.org), making them available to<br>users on the Gemini Enterprise web app. For more<br>information, see<br>Register and manage A2A agents<br>(/gemini/enterprise/docs/register-and-manage-an-a2a-<br>agent)<br>.<br>Also, A2A agents in<br>Agent Registry<br>(/agent-registry/overview) can be discovered and added<br>to apps in Gemini Enterprise. For more information, see<br>Import A2A agents from Agent Registry<br>(/gemini/enterprise/docs/import-govern-agent-registry).|
||Dialogflow|Gemini Enterprise admins can register conversational<br>agents built with Dialogflow, making them available to<br>users on the Gemini Enterprise web app. For more<br>information, see<br>Register and manage Dialogflow agents<br>(/gemini/enterprise/docs/register-and-manage-a-<br>dialogflow-agent)<br>.|

### View agents

To view the agents that are registered or available, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that has the agents. 

3. Click **Agents** . The **Agents** page is displayed. 

### Agent identity

As a Gemini Enterprise administrator, you can view an agent's identity. This is typically the agent's SPIFFE ID. However, the SPIFFE ID is only visible if the publisher has made it available. If the SPIFFE ID is not published, the Agent Registry resource ID is displayed as a fallback. 

The following image shows an example of an agent's details displaying a SPIFFE ID: 

### Manage agents

A Gemini Enterprise admin can manage the lifecycle of the available agents from the **Agents** page in the Gemini Enterprise console and can perform the following tasks: 

|Task|Description|
|---|---|
|Update an agent|You can update the details of an agent. For more information, see:<br>Update an A2A agent<br>(/gemini/enterprise/docs/register-and-manage-an-a2a-<br>agent#update_an_a2a_agent)<br>Update an ADK agent<br>(/gemini/enterprise/docs/register-and-manage-an-adk-<br>agent#update_an_adk_agent)<br>Update a Dialogflow agent<br>(/gemini/enterprise/docs/register-and-manage-a-dialogflow-<br>agent#update-a-dialogflow-agent)|
|Test an agent|Test your agents before your end users find problems.<br>On the Agents page, click next to the agent that you want to test, and then<br>click Preview. This opens the agent in the Gemini Enterprise app.|
|Invoke an agent<br>programmatically|Call a specific registered agent from custom applications, orchestrators, or<br>scripts. For instructions, see:<br>Call a specific agent with the StreamAssist API<br>(/gemini/enterprise/docs/invoke-agent-streamassist)<br>Call an agent using its registry A2A endpoint<br>(/gemini/enterprise/docs/invoke-agent-a2a)|
|Share an agent or<br>transfer ownership|<br>You can share available agents or transfer ownership of shared agents in<br>your Google Cloud console. For more information, see<br>Share agents from<br>Google Cloud console(/gemini/enterprise/docs/share-custom-agents).|
|Configure agent<br>sharing by end<br>users and review<br>their requests to<br>share|For agents created using Workflow Builder, you can let end users share their<br>agents with other users in the organization through email addresses or<br>groups.<br>You can also configure whether sharing requires administrator review and<br>approval.<br>For more information, see the settings Enable agent sharing, Enable agent<br>sharing without admin approval, and Enable End Users to share with Groups<br>in<br>Manage features on the web app<br>(/gemini/enterprise/docs/manage-web-app-features). Also see<br>Share an<br>agent(/gemini/enterprise/docs/workflow-builder/share-chat-agent).|

|Task|Description|
|---|---|
|Delete an agent|You can delete an agent from the Agents page. After an agent is deleted, it<br>is removed from the Agents page and the Gemini Enterprise web app.|
||On the Agents page, click next to the agent you want to delete, and then<br>click Delete.|

### Agent states

This table describes each state that an agent might be in. In the Google Cloud console on the **Agents** page, you can see the state listed for each agent in the **Agent state** column of the **Agents** table. 

|State|Description|
|---|---|
|Private|The agent is intended for personal use and is available exclusively to its<br>creator. After the agent's status is changed to_Enabled_, the agent is visible<br>to other users on the Gemini Enterprise web app.|
|Suspended|The agent is temporarily deactivated. It remains visible in the Agent Gallery<br>with a message explaining its deactivation. Although users can't interact<br>with the agent, owners and admins retain full access.|
|Enabled|The agent is active and available for use on the Gemini Enterprise web app.<br>Authorized users can interact with the agent as intended.|
|Disabled|The agent is inactive and hidden from the Agent Gallery. Interaction isn't<br>available for any user until the owner or admin re-enables the agent.|

Last updated 2026-10-14 UTC. 



## Register and manage Dialogflow agents

URL: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

This page describes how to register and use Dialogflow agents with Gemini Enterprise. 

### Overview

To use a Dialogflow agent with Gemini Enterprise, you must first deploy then register your agent. Registering your Dialogflow agent links your deployed agent to Gemini Enterprise so that they can communicate. 

### Before you begin

Before registering your Dialogflow agent, you must ensure that these steps are completed: 

- Deploy your Dialogflow agent. To view the Dialogflow and conversational agents dashboard, see Conversational agents (https://conversational-agents.cloud.google.com). 

- The Gemini Enterprise Admin (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

- Enable the Discovery Engine API. To enable the Discovery Engine API for the Google Cloud project, in the Google Cloud console, go to the **Discovery Engine API** page. 

Go to Discovery Engine API (https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics) 

- Create a Gemini Enterprise app. For more information, see Create an app (/gemini/enterprise/docs/create-app). 

### Register a Dialogflow agent with Gemini Enterprise

You can register your Dialogflow agent with Gemini Enterprise using the Google Cloud console or the REST API. Registration makes your agent available to users within a Gemini Enterprise app. 

**Agent registration quota and licensing:** Registering an agent with an app consumes one unit of your project's pooled daily agent creation quota ( **`discoveryengine.googleapis.com/agents_tier_enterprise_regional`** ). Quota is determined by the number of Gemini Enterprise Standard licenses (1 creation per user per day, pooled) or Plus licenses (10 per user per day, pooled) distributed to the project. Frontline licenses provide 0 creation quota. 

If you register a backend agent across multiple Gemini Enterprise apps or engines in the same project, each registration API call ( **`agents.create`** ) counts as an agent creation against this daily quota. Automated deployment scripts or CI/CD pipelines registering an agent across many apps can encounter **`HTTP 429 RESOURCE_EXHAUSTED: Agent creation quota exceeded`** if the number of registration calls in a day exceeds the number of distributed Standard licenses. Ensure your project has sufficient Standard licenses distributed before executing multi-app rollouts. For more details, see Daily creation quotas (/gemini/enterprise/docs/workflow-builder/quotas-and-limits#creation-quotas). 

Consolecurl  (#curl) (#console) 

To register a Dialogflow agent using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to **Gemini Enterprise** (https://console.cloud.google.com/gemini-enterprise/products) 

2. Select your project. 

3. Click the name of the app that you want to register the agent with. 

4. Click **Agents > Add Agents** . The **Choose an agent type** pane appears. 

5. On the **Custom agent via Dialogflow** card, click **Add** to register your Dialogflow agent with Gemini Enterprise. The **Configuration** pane opens. 

6. To configure your agent, follow these steps: 

   - a. Enter a name in the **Your agent name** field. This value appears in Gemini Enterprise as the display name of your agent. 

   - b. Enter a description in the **Describe your agent** field. This value is used by an LLM to determine whether to invoke your agent in response to a user query. 

   - c. Enter the resource path of the Dialogflow agent that you want to register with Gemini Enterprise in the **Dialogflow agent source** field. 

Use this format: `projects/{project}/locations/{location}/agents/{agent}` 

The **Agent availability** option, **When selected** , is set by default. 

- d. Click **Create** . 

The successful response to this command returns all fields of the newly created Dialogflow agent resource, which includes its unique resource name in the name field. This resource name can be used for future updates or references. 

### List agents connected to an app

The following code sample demonstrates how you can get the details of all the agents connected to your app: 

REST (#rest) 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
fault_collection/engines/APP_ID/assistants/default_assistant/agents"
```

Replace the variables with values: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` . 

_APP_ID_ : the ID of your Gemini Enterprise app. 

If your agent isn't prebuilt by Google, the response includes a `name` field in the first few lines. The value of this field contains the Agent ID at the end of the path. For example, in the following response, the Agent ID is `12345678901234567890` : 

```
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890",
...
}
```

### View details of a Dialogflow agent

The following code sample demonstrates how you can retrieve the details of an agent that was registered with Gemini Enterprise: 

REST 

(#rest) 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
fault_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
```

Replace the variables with values: 

- _ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

- `global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

- _PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` . 

- _APP_ID_ : the ID of your Gemini Enterprise app. 

- _AGENT_ID_ : the ID of the agent. You can find the agent ID by listing the agents connected to your app (#list_agents_connected_to_an_app). 

### Update a Dialogflow agent

All of the fields that were supplied during agent registration can be updated. The following fields are mandatory during the update process: 

- `displayName` 

- `description` 

- `reasoning_engine` 

When updating a field, all fields and their values must be redefined in the update request, even if no changes are made to a particular field. 

This code sample demonstrates how you can update the registration of your Dialogflow agent: 

curl 

(#curl) 

```
 curl -X PATCH \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
   -H "Content-Type: application/json" \
   -H "X-Goog-User-Project:PROJECT_ID" \
 "https://discoveryengine.googleapis.com/v1alpha/AGENT_RESOURCE_NAME" \
   -d '{
     "displayName": "DISPLAY_NAME",
     "description": "DESCRIPTION",
     "icon": {
       "uri": "ICON_URI"
     },
     "dialogflowAgentDefinition": {
       "dialogflowAgent":
"projects/PROJECT_ID/locations/REASONING_ENGINE_LOCATION/agents/DIALOGFLOW_AGENT_ID"
     }
   }'
```

Replace the variables with values: 

- _PROJECT_ID_ : the ID of your Google Cloud project. 

- _AGENT_RESOURCE_NAME_ : the resource name of the agent registration to be updated. 

- _DISPLAY_NAME_ :tThe display name of the agent. 

- _DESCRIPTION_ : the description of the agent that's displayed in Gemini Enterprise. The description is only for the user's benefit. 

- _ICON_URI_ : the public URI of an icon that displays next to your Dialogflow agent's name. You can also provide a Base64-encoded image in `icon.content` . 

- _REASONING_ENGINE_LOCATION_ : the cloud location of the reasoning engine that you're creating an agent at. 

- _DIALOGFLOW_AGENT_ID_ : the unique identifier of your Dialogflow agent. 

### Delete a Dialogflow agent

The following code sample demonstrates how you can delete an agent that is connected to your app: 

REST 

(#rest) 

```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
fault_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
```

Replace the variables with values: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

- `eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` 

- _APP_ID_ : the ID of your Gemini Enterprise app. 

- _AGENT_ID_ : the ID of the agent. You can find the agent ID by listing the agents connected to your app (#list_agents_connected_to_an_app). 

<sup>Example command and result</sup> 

```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890"
{
 "name": "projects/123456/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890/operations/delete-agent-
12345678901234567890",
 "done": true
}
```

Last updated 2026-10-14 UTC. 



## Register and manage A2A agents

URL: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-a2a-agent

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

Agent2Agent (A2A) Protocol (https://a2a-protocol.org/) is an open communication protocol and a universal language for agents. The protocol enables agents from different builders and platforms to discover each other, collaborate, and securely delegate tasks. This document explains how Gemini Enterprise administrators can connect agents that are built using A2A and hosted on any platform to Gemini Enterprise, making them available to users in the Gemini Enterprise web app. 

**Note:** To secure A2A agents, developers must configure Model Armor using the REST API within their agent's application code. The Model Armor settings in the Google Cloud console for Gemini Enterprise don't automatically protect A2A agents. 

### Before you begin

Make sure you have the following: 

- The Gemini Enterprise Admin (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

- Enable the Discovery Engine API. To enable the Discovery Engine API for the Google Cloud project, in the Google Cloud console, go to the **Discovery Engine API** page. 

Go to Discovery Engine API (https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics) 

- An existing Gemini Enterprise app. To create an app, see Create an app (/gemini/enterprise/docs/create-app). 

- An agent that uses the A2A protocol. 

- Gemini Enterprise supports the A2A v0.3 streaming mechanism. 

If you use A2A v1.0.0 or later, then use the compatibility packages provided by the SDK to make sure that your agent functions with the earlier mechanism (for example, the `a2acompat/a2av0` package for Go or the `a2a.compat.v0_3` package for Python). 

**Tip:** You must host and maintain your A2A agents for them to function within Gemini Enterprise. 

- If your A2A agent is hosted on Cloud Run, uses a default `.run.app` URL directly, and requires authentication, grant the Cloud Run Invoker ( `roles/run.invoker` ) role to the Discovery Engine 

service agent (this doesn't apply when Cloud Run is behind Apigee, a load balancer, or a custom domain): 

```
gcloud projects add-iam-policy-binding <var>PROJECT_ID</var> \
  --member="serviceAccount:service-<var>PROJECT_NUMBER</var>@gcp-sa-
discoveryengine.iam.gserviceaccount.com" \
  --role="roles/run.invoker"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

_`PROJECT_NUMBER`_ : the number of your Google Cloud project. 

### Configure authentication and authorization

Depending on your agent hosting environment and security requirements, you can configure how Gemini Enterprise authenticates with your agent, how your agent accesses resources on behalf of the end user, and how to secure your agent endpoint. 

#### How Gemini Enterprise authenticates with your agent

When Gemini Enterprise invokes an A2A agent, it can send authentication and authorization data in request headers depending on your hosting and security configuration: 

|Header|Description|
|---|---|
|`X-Serverless-Authorization`|Service-to-service IAM authentication (for Cloud Run).|
||If your A2A agent is hosted on Cloud Run and your agent URL is a default<br>`.run.app`URL, Gemini Enterprise automatically generates a Google-signed OIDC<br>ID token for the Discovery Engine service agent (`service-`_`PROJECT_NUMBER`_`@gcp-`<br>`sa-discoveryengine.iam.gserviceaccount.com`) with your agent URL as the<br>audience, and attaches it in the`X-Serverless-Authorization`header. If your<br>agent URL uses Apigee, a load balancer, or a custom domain, Gemini Enterprise<br>doesn't send this header.|
||When Gemini Enterprise calls a default`.run.app`URL directly, the Cloud Run<br>ingress infrastructure consumes this header to verify that the service agent has<br>the`roles/run.invoker`IAM role (see<br>Before you begin(#cloud-run-invoker))<br>before forwarding the request to your application container.|

|Header|Description|
|---|---|
|`Authorization`|End-user OAuth 2.0 authorization (for user context and API access).|
||If you configure OAuth 2.0 credentials for your A2A agent (see<br>Configure OAuth<br>2.0 for end-user authorization(#authorize-your-agent)), Gemini Enterprise<br>acquires an OAuth 2.0 access token or ID token on behalf of the signed-in end<br>user after they grant consent, and sends it in the standard`Authorization`header<br>(for example,`Bearer`_`USER_OAUTH_TOKEN`_).|
||Cloud Run forwards the`Authorization`header directly to your container, allowing<br>your agent application code to read the user token and call downstream APIs on<br>behalf of the user.|

**Note:** Because Cloud Run consumes **`X-Serverless-Authorization`** for service-level IAM authentication and leaves the standard **`Authorization`** header intact for your container code, you can secure your agent as a private Cloud Run service while also receiving end-user OAuth tokens without header collisions. 

#### Configure OAuth 2.0 for end-user authorization (optional)

For A2A agents, configure OAuth 2.0 credentials if your agent must access Google Cloud resources or perform operations on behalf of the end user. For more information about how authentication and authorization headers work, see How Gemini Enterprise authenticates with your agent (#auth-headers). 

Follow these steps to create an OAuth client ID: 

1. In the Google Cloud console, on the **APIs & Services** page, go to the **Credentials** page. 

Go to Credentials (https://console.cloud.google.com/apis/credentials) 

2. Select the Google Cloud project, which has the data source that you want the agent to access. For example, select the project that contains the BigQuery dataset that you want the agent to query. 

3. Click **Create credentials** and select **OAuth client ID** . 

4. In **Application type** , select **Web application** . 

5. In the **Authorized redirect URIs** section, add the following URIs: 

```
https://vertexaisearch.cloud.google.com/oauth-redirect
https://vertexaisearch.cloud.google.com/static/oauth/oauth.html
```

6. Click **Create** . 

7. In the **OAuth client created** panel, click **Download JSON** . The downloaded JSON includes the `Client ID` , `Authorization URI` , `Token URI` , and `Client secret` for the selected Google Cloud project. You need these details to create an authorization resource. 

#### Secure your A2A agent endpoint

For the authentication headers that Gemini Enterprise sends to your A2A agent, see How Gemini Enterprise authenticates with your agent (#auth-headers). When you secure your agent endpoint, or an API gateway in front of it, consider the following: 

- **Agent card security schemes** : Gemini Enterprise doesn't use the `securitySchemes` and `security` fields of your agent card to authenticate with your agent. 

- **API keys and custom headers** : Gemini Enterprise doesn't support the `apiKey` security scheme, and doesn't provide a way to add static API keys or other custom header values to the requests that it sends to your agent. 

- **Service agent ID token** : Gemini Enterprise sends the `X-Serverless-Authorization` header only when your agent URL is a default Cloud Run URL that ends in `.run.app` . If your agent URL uses a custom domain, a load balancer, or an API gateway, Gemini Enterprise doesn't send this header. 

- **End-user token** : If you confgure OAuth 2.0 for your agenti (#authorize-your-agent), Gemini Enterprise sends the end user's token from your OAuth 2.0 provider in the `Authorization` header. 

Secure an agent endpoint with Apigee 

If you expose your A2A agent through an Apigee (/apigee/docs) API proxy, the proxy receives the enduser token in the `Authorization` header but doesn't receive the `X-Serverless-Authorization` header. To secure the proxy, do the following: 

1. Configure OAuth 2.0 for end-user authorization (#authorize-your-agent) for your agent (using either a Google Cloud OAuth 2.0 client ID or a third-party OAuth 2.0 provider), and provide those OAuth 2.0 details when you register the agent (#register-agent). Configuring OAuth 2.0 is required when securing an Apigee API proxy; don't skip the authorization step during registration. 

2. In your agent card, set `url` to the URL of your Apigee API proxy. 

3. In the API proxy, validate the end-user token in the `Authorization` header before you forward the request to your agent. Choose the Apigee policy based on the token format that your OAuth 2.0 provider issues: 

   - **Third-party OAuth 2.0 providers that issue signed JWT access tokens** : Use the VerifyJWT policy (/apigee/docs/api-platform/reference/policies/verify-jwt-policy) to verify the token signature against your provider's public JSON Web Key Set (JWKS) URI and validate the issuer ( `iss` ) and audience ( `aud` ) claims. 

   - **Google OAuth 2.0** **(** **`accounts.google.com` )** : Google OAuth 2.0 access tokens ( `ya29...` ) are opaque tokens rather than signed JWTs. Use a ServiceCallout policy (/apigee/docs/api-platform/reference/policies/service-callout-policy) to call `https://oauth2.googleapis.com/tokeninfo` and verify the audience ( `aud` ) and `scope` fields. 

### Register an A2A agent with Gemini Enterprise

You can register your A2A agent with Gemini Enterprise using either the Google Cloud console or the REST API. This makes the agent available to users within a Gemini Enterprise app. 

**Important:** Traffic to A2A Agents added through this method do not go through Agent Gateway 

(/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-ge-deploy) and Agent Gateway policies do not apply. 

**Agent registration quota and licensing:** Registering an agent with an app consumes one unit of your project's pooled daily agent creation quota ( **`discoveryengine.googleapis.com/agents_tier_enterprise_regional`** ). Quota is determined by the number of Gemini Enterprise Standard licenses (1 creation per user per day, pooled) or Plus licenses (10 per user per day, pooled) distributed to the project. Frontline licenses provide 0 creation quota. 

If you register a backend agent across multiple Gemini Enterprise apps or engines in the same project, each registration API call ( **`agents.create`** ) counts as an agent creation against this daily quota. Automated deployment scripts or CI/CD pipelines registering an agent across many apps can encounter **`HTTP 429 RESOURCE_EXHAUSTED: Agent creation quota exceeded`** if the number of registration calls in a day exceeds the number of distributed Standard licenses. Ensure your project has sufficient Standard licenses distributed before executing multi-app rollouts. For more details, see Daily creation quotas 

(/gemini/enterprise/docs/workflow-builder/quotas-and-limits#creation-quotas). 

ConsoleREST (#rest) (#console) 

To register an A2A agent using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to register the agent with. 

3. Click **Agents > Add Agents** . 

4. In the **Choose an agent type** section, click **Add** for **Custom agent via A2A** . 

5. In the **Agent card JSON** field, enter the agent card details in JSON format. For a complete list of available fields, see the Agent2Agent (A2A) Protocol Official Specification (https://a2a-protocol.org/latest/specification/). The following example only uses the required fields. 

For example: 

```
{
 "protocolVersion": "0.3",
 "name": "Hello World Agent",
 "description": "Just a hello world agent",
 "url": "https://example.com/myagent",
 "iconUrl":
"data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTkiIGhlaWdodD0iOTkiIHN0eWxlPSJiYWNrZ3JvdW5kL
WNvbG9yOmdyYXk7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zMyAwaDMzd
jMzSDMzeiBNMCAzM2gzM3YzM0gweiBNNjYgMzNoMzN2MzNINjZ6IE0zMyA2NmgzM3YzM0gzM3oiIGZpbGw9ImJsd
WUiLz48L3N2Zz4=",
 "version": "1.0.0",
 "capabilities": {
 },
 "skills": [
   {
     "id": "data-analysis",
     "name": "Data Analysis",
     "description": "Data analysis",
     "tags": []
   }
 ],
 "defaultInputModes": [
   "text/plain"
 ],
 "defaultOutputModes": [
   "text/plain"
 ]
}
```

6. Click **Preview agent details > Next** . 

7. Complete the setup using one of the following methods: 

If you want the agent to access Google Cloud resources on behalf of you, or if your agent endpoint requires an `Authorization` header (for example, when securing an Apigee API proxy (#secure-endpoint-apigee)), follow these steps: 

- a. Enter **Client ID** , **Client secret** , **Authorization URI** , and **Token URI** that you generated in Confgure OAuth 2.0 for endi -user authorization (optional) (#authorize-your-agent). 

- b. Enter the **Scopes** . 

- c. Click **Finish** . 

If you don't want the agent to access Google Cloud resources on behalf of you and your agent endpoint doesn't require an `Authorization` header, click **Skip & Finish** . 

### List agents connected to an app

The following code sample demonstrates how you can get the details of all the agents connected to your app: 

REST 

(#rest) 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
```

Replace the variables with values: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` . 

_APP_ID_ : the ID of your Gemini Enterprise app. 

If your agent isn't prebuilt by Google, the response includes a `name` field in the first few lines. The value of this field contains the Agent ID at the end of the path. For example, in the following response, the Agent ID is `12345678901234567890` : 

```
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890",
}
```

<sup>Example command and result</sup> 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents"
```

`{` 

```
 "name": "projects/123456/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890",
 "displayName": "Hello World Agent",
 "description": "Just a hello world agent",
 "createTime": "2025-10-20T20:53:35.490600996Z",
 "state": "ENABLED",
 "a2aAgentDefinition": {
   "jsonAgentCard": "{\"name\":\"Hello World Agent\",\"description\":\"Just a hello world
agent\",\"url\":\"https://example.com/myagent\",\"version\":\"1.0.0\",\"capabilities\":
{},\"default_input_modes\":[\"text\"],\"default_output_modes\":[\"text\"],\"skills\":
[{\"id\":\"chat\",\"name\":\"Chat Skill\",\"description\":\"Chat with the Gemini
agent.\",\"tags\":[\"chat\"],\"examples\":[\"Hello, world!\"]}]}"
 }
}
```

### View the details of an A2A agent

The following code sample demonstrates how you can retrieve the details of an agent that was registered with Gemini Enterprise: 

REST 

(#rest) 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
fault_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
```

Replace the variables with values: 

- _ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` . 

_APP_ID_ : the ID of your Gemini Enterprise app. 

- _AGENT_ID_ : the ID of the agent. You can find the agent ID by listing the agents connected to your app (#list_agents_connected_to_an_app). 

<sup>Example command and result</sup> 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890"
{
 "name": "projects/123456/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890",
 "displayName": "Hello World Agent",
 "description": "Just a hello world agent",
 "createTime": "2025-10-20T20:53:35.490600996Z",
 "state": "ENABLED",
 "a2aAgentDefinition": {
   "jsonAgentCard": "{\"name\":\"Hello World Agent\",\"description\":\"Just a hello world
agent\",\"url\":\"https://example.com/myagent\",\"version\":\"1.0.0\",\"capabilities\":
{},\"default_input_modes\":[\"text\"],\"default_output_modes\":[\"text\"],\"skills\":
[{\"id\":\"chat\",\"name\":\"Chat Skill\",\"description\":\"Chat with the Gemini
agent.\",\"tags\":[\"chat\"],\"examples\":[\"Hello, world!\"]}]}"
 }
}
```

### Update an A2A agent

You can modify the details of an existing A2A agent registered with Gemini Enterprise using either the Google Cloud console or the REST API. 

ConsoleREST (#rest) (#console) 

To update an A2A agent using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that includes the agent you want to update. 

3. Click **Agents** . 

4. Click the name of the **A2A (Custom)** agent to update, and then click **Edit** . 

5. In the **Agent card JSON** field, update the agent card details in JSON format. For a complete list of available fields, see the Agent2Agent (A2A) Protocol Official Specification (https://a2a-protocol.org/latest/specification/). The following example only uses the required fields. 

For example: 

```
{
 "protocolVersion": "0.3",
 "name": "Hello World Agent",
 "description": "Just a hello world agent",
 "url": "https://example.com/myagent",
 "iconUrl":
"data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iOTkiIGhlaWdodD0iOTkiIHN0eWxlPSJiYWNrZ3JvdW5kL
WNvbG9yOmdyYXk7IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPjxwYXRoIGQ9Ik0zMyAwaDMzd
jMzSDMzeiBNMCAzM2gzM3YzM0gweiBNNjYgMzNoMzN2MzNINjZ6IE0zMyA2NmgzM3YzM0gzM3oiIGZpbGw9ImJsd
WUiLz48L3N2Zz4=",
 "version": "1.1.0",
 "capabilities": {
 },
 "skills": [
   {
     "id": "data-analysis",
     "name": "Data Analysis",
     "description": "Data analysis",
     "tags": []
   }
 ],
 "defaultInputModes": [
   "text/plain"
 ],
 "defaultOutputModes": [
   "text/plain"
 ]
}
```

6. Click **Save** . 

### Delete an A2A agent

The following code sample demonstrates how you can delete an agent that is connected to your app: 

REST 

(#rest) 

```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
fault_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
```

Replace the variables with values: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

- `eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` 

- _APP_ID_ : the ID of your Gemini Enterprise app. 

- _AGENT_ID_ : the ID of the agent. You can find the agent ID by listing the agents connected to your app (#list_agents_connected_to_an_app). 

<sup>Example command and result</sup> 

```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890"
{
 "name": "projects/123456/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890/operations/delete-agent-
12345678901234567890",
 "done": true
}
```

### What's next

Use the agent that you registered with Gemini Enterprise on the web app. 

Last updated 2026-10-14 UTC. 



## Register and manage

URL: https://docs.cloud.google.com/gemini/enterprise/docs/register-and-manage-an-adk-agent

This page explains how administrators register ADK agents from Agent Runtime for use in the Gemini Enterprise web app. 

For ADK agents that are deployed on Agent Runtime (/gemini-enterprise-agent-platform/overview), you can use a single Agents CLI in Agent Platform (https://google.github.io/agents-cli) command to register the agents with Gemini Enterprise. 

When you register ADK agents hosted on Agent Runtime with a Gemini Enterprise app and make these agents available to end users on the Gemini Enterprise web app: 

The Agent Runtime service processes the agent queries. 

- The Agent Runtime ML processing terms apply. For more information, see Agent Runtime limitations (/gemini/enterprise/docs/locations#agent_engine_limitations). 

The following table describes how ADK agents are governed to ensure secure and controlled deployment and usage. 

|Agent governance|Description|
|---|---|
|Secure communication|The connection between Agent Runtime and Gemini Enterprise is compliant with VPC Service<br>Controls (VPC-SC), ensuring secure data exchange.|
|Cross-project agent<br>support|You can connect ADK agents hosted in a different Google Cloud. Gemini Enterprise uses<br>Google Cloud's secure private networking for these cross-project connections. For more<br>information, see<br>Configure cross-project ADK agent access<br>(/gemini/enterprise/docs/configure-cross-project-adk-agents).|
|Personalized<br>interactions|ADK agents receive the user's email address from Gemini Enterprise. This allows agents to<br>recognize individual users and provide personalized responses based on their identity and<br>permissions.|

**Note:** To secure ADK agents, developers must configure Model Armor using the REST API within their agent's application code. The Model Armor settings in the Google Cloud console for Gemini Enterprise don't automatically protect ADK agents. 

### Before you begin

Make sure you have the following: 

The Gemini Enterprise Admin (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

- Enable the Discovery Engine API. To enable the Discovery Engine API for the Google Cloud project, in the Google Cloud console, go to the **Discovery Engine API** page. 

Go to Discovery Engine API (https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com/metrics) 

- An existing Gemini Enterprise app. To create an app, see Create an app (/gemini/enterprise/docs/create-app). 

- An ADK agent that is hosted on the Agent Runtime. For more information, see Overview of Agent Development Kit (/agent-builder/agent-development-kit/overview). 

   - If you don't have an agent, follow the steps in the `adk-samples` GitHub Repository (https://github.com/google/adk-samples/tree/main/python/agents/fun-facts) to deploy a `fun_facts` agent to Agent Runtime. You can then register the agent with Gemini Enterprise. 

**Tip:** You must host and maintain your ADK agents on Agent Runtime for them to function within Gemini Enterprise. 

- If your ADK agent is hosted in a different Google Cloud project than your Gemini Enterprise app, you must grant necessary permissions. For more information, see Grant permissions for cross- project ADK agent access (/gemini/enterprise/docs/configure-cross-project-adk-agents). 

### Configure authorization details (optional)

**Tip:** If the agent must access Google Cloud resources on behalf of a user, then you must configure the authorization details. 

Follow these steps to obtain the authorization details. 

1. In the Google Cloud console, on the **APIs & Services** page, go to the **Credentials** page. 

Go to Credentials (https://console.cloud.google.com/apis/credentials) 

2. Select the Google Cloud project, which has the data source that you want the agent to access. For example, select the project that contains the BigQuery dataset that you want the agent to query. 

3. Click **Create credentials** and select **OAuth client ID** . 

4. In **Application type** , select **Web application** . 

5. In the **Authorized redirect URIs** section, add the following URIs: 

```
https://vertexaisearch.cloud.google.com/oauth-redirect
https://vertexaisearch.cloud.google.com/static/oauth/oauth.html
```

6. Click **Create** . 

7. In the **OAuth client created** panel, click **Download JSON** . The downloaded JSON includes the `Client ID` , `Authorization URI` , `Token URI` , and `Client secret` for the selected Google Cloud project. You need these details to create an authorization resource. 

### Register an ADK agent with Gemini Enterprise

You can register your ADK agent with Gemini Enterprise using either the Google Cloud console or the REST API. This makes the agent available to users within a Gemini Enterprise app. 

**Agent registration quota and licensing:** Registering an agent with an app consumes one unit of your project's pooled daily agent creation quota ( **`discoveryengine.googleapis.com/agents_tier_enterprise_regional`** ). Quota is determined by the number of Gemini Enterprise Standard licenses (1 creation per user per day, pooled) or Plus licenses (10 per user per day, pooled) distributed to the project. Frontline licenses provide 0 creation quota. 

If you register a backend agent across multiple Gemini Enterprise apps or engines in the same project, each registration API call ( **`agents.create`** ) counts as an agent creation against this daily quota. Automated deployment scripts or CI/CD pipelines registering an agent across many apps can encounter **`HTTP 429 RESOURCE_EXHAUSTED: Agent creation quota exceeded`** if the number of registration calls in a day exceeds the number of distributed Standard licenses. Ensure your project has sufficient Standard licenses distributed before executing multi-app rollouts. For more details, see Daily creation quotas 

(/gemini/enterprise/docs/workflow-builder/quotas-and-limits#creation-quotas). 

ConsoleREST (#rest) (#console) 

To register an ADK agent using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to register the agent with. 

3. Click **Agents** . The **Agents** page displays. 

4. Click **Add agent** . The **Add an agent** panel displays. 

5. Click **Add** for **Custom agent via Agent Runtime** . The **Authorizations** page displays. 

6. If you want the agent to access Google Cloud resources on your behalf, then each resource needs an authorization. To set up an authorization for a single resource, follow these steps: 

   - a. Click **Add authorization** . 

   - b. Enter a unique value for **Authorization name** . An ID is generated based on the name, and it can't be changed later. 

   - c. Enter the values that you generated in Configure authorization details (optional) (#authorize-your-agent) in the following fields: 

- i. Enter the value in the **Client ID** field. 

- ii. Enter the value in the **Client secret** field. 

- iii. Enter the value in the **Token URI** field. 

- iv. Enter the value in the **Authorization URI** field. Construct the Authorization URI using the details from your OAuth credentials JSON file. Copy the following template, and replace the placeholders with your specific values. 

```
https://accounts.google.com/o/oauth2/v2/auth?
client_id=YOUR_CLIENT_ID&redirect_uri=https%3A%2F%2Fvertexaisearch.cloud.googl
e.com%2Fstatic%2Foauth%2Foauth.html&scope=YOUR_CUSTOM_SCOPES&include_granted_s
copes=true&response_type=code&access_type=offline&prompt=consent
```

      - v. Click **Done** . 

7. Click **Next** . 

8. To configure your agent, follow these steps: 

   - a. Enter a name in the **Agent name** field. This value appears in the Gemini Enterprise web app as the display name of your agent. 

   - b. Enter a description in the **Describe your agent** field. This value is used by an LLM to determine whether to invoke your agent in response to a user query. 

   - c. Enter the **Agent Runtime** resource path. The resource path has the following format: 

```
projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID
```

For more information on how to list the agents hosted on Agent Runtime and get the resource path, see List deployed agents 

(/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents#list). 

- d. Click **Create** . 

### Share agents with users

To allow users to access an agent using the Gemini Enterprise web app, see Share an agent 

(/gemini/enterprise/docs/share-custom-agents#share_an_agent). 

### List agents connected to an app

The following code sample demonstrates how you can get the details of all the agents connected to your app: 

REST (#rest) 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
fault_collection/engines/APP_ID/assistants/default_assistant/agents"
```

Replace the variables with values: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` . 

_APP_ID_ : the ID of your Gemini Enterprise app. 

If your agent isn't prebuilt by Google, the response includes a `name` field in the first few lines. The value of this field contains the Agent ID at the end of the path. For example, in the following response, the Agent ID is `12345678901234567890` : 

```
{
"name": "projects/123456/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890",
...
}
```

### View the details of an ADK agent

The following code sample demonstrates how you can retrieve the details of an agent that was registered with Gemini Enterprise: 

REST 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
fault_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
```

Replace the variables with values: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` . 

_APP_ID_ : the ID of your Gemini Enterprise app. 

- _AGENT_ID_ : the ID of the agent. You can find the agent ID by listing the agents connected to your app (#list_agents_connected_to_an_app). 

### Update an ADK agent

You can modify the details of an existing agent registered with Gemini Enterprise using either the Google Cloud console or the REST API. 

ConsoleREST (#rest) (#console) 

To update the agent using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that includes the agent you want to update. 

3. Click **Agents** . 

4. Click the name of the **Agent Runtime** agent that you want to update, and then click **Edit** . 

5. Update the **Display name** , **Description** , or the **Agent Runtime reasoning engine** . 

The resource path has the following format: 

```
projects/PROJECT_ID/locations/LOCATION/reasoningEngines/RESOURCE_ID
```

For more information on how to list the agents hosted on Agent Runtime and get the resource path, see List deployed agents 

(/gemini-enterprise-agent-platform/scale/runtime/manage-deployed-agents#list). 

6. Click **Save** . 

### Delete an ADK agent

The following code sample demonstrates how you can delete an agent that is connected to your app: 

REST 

(#rest) 

```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/de
fault_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID"
```

Replace the variables with values: 

_ENDPOINT_LOCATION_ : the multi-region for your API request. Specify one of the following values: 

- `us` for the US multi-region 

- `eu` for the EU multi-region 

- `global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

- _PROJECT_ID_ : the ID of your Google Cloud project. 

_LOCATION_ : the multi-region of your app: `global` , `us` , or `eu` 

_APP_ID_ : the ID of your Gemini Enterprise app. 

- _AGENT_ID_ : the ID of the agent. You can find the agent ID by listing the agents connected to your app (#list_agents_connected_to_an_app). 

<sup>Example command and result</sup> 

```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://global-discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890"
{
 "name": "projects/123456/locations/global/collections/default_collection/engines/my-
app/assistants/default_assistant/agents/12345678901234567890/operations/delete-agent-
12345678901234567890",
 "done": true
}
```

### Agent Runtime location

When registering or updating an agent, the Agent Runtime location must be compatible with the location of your Gemini Enterprise app. Mismatched locations result in an error. 

Refer to the following table for compatibility requirements: 

|Gemini Enterprise app location|Allowed Agent Runtime location(s)|
|---|---|
|`global`|Any supported Google Cloud region|
|`us`|Any region starting with`us-`, such as`us-central1`or`us-`<br>`east4`|
|`eu`|Any region starting with`europe-`, such as`europe-west1`<br>or`europe-west3`|

Last updated 2026-10-14 UTC. 



## Configure cross-project access

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-cross-project-adk-agents

This page explains how administrators can grant permission for Gemini Enterprise to access an ADK agent that runs within Agent Runtime on Gemini Enterprise Agent Platform in a different Google Cloud project. 

### Identify the Gemini Enterprise service agent

To find the service agent email address for your Gemini Enterprise app project: 

1. In the Google Cloud console, go to the project that contains your Gemini Enterprise app. 

2. From the project list, find the project number. 

3. Construct the service agent email address using the following format: 

```
service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com
```

Replace _`PROJECT_NUMBER`_ with the project number from the previous step. 

#### Grant permissions in the agent project

Grant the Gemini Enterprise service agent permissions in the project where the ADK agent is hosted with Agent Runtime: 

1. In the Google Cloud console, go to the project where the ADK agent is hosted with Agent Runtime. 

2. Go to **IAM & Admin > IAM** . 

3. Click **Grant Access** . 

4. In the **New principals** field, enter the service agent email address that you identified in the previous section. 

5. In the **Select a role** list, search for and select **Discovery Engine Service Agent** ( `roles/discoveryengine.serviceAgent` ) . 

6. Click **Save** . 

### What's next

- After granting these permissions, you can Register the ADK agent (/gemini/enterprise/docs/register-and-manage-an-adk-agent#register-an-adk-agent) in your Gemini Enterprise app, using the agent's resource path from the agent project. 

Last updated 2026-10-14 UTC. 



## Register and manage

URL: https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/register-and-manage-an-a2ui-agent

A Gemini Enterprise administrator can register an agent that uses Agent to UI (A2UI) (https://a2ui.org/introduction/what-is-a2ui/) to build custom interfaces and the Agent2Agent (A2A) Protocol (https://a2a-protocol.org/) for communication with Gemini Enterprise. 

Gemini Enterprise supports all the standard A2UI components. These components render using Gemini Enterprise's built-in styling. For information and examples using the basic catalog, see the A2UI components basic catalog 

(https://a2ui-composer.ag-ui.com/basic-catalog) and the A2UI components custom catalog (https://a2ui-composer.ag-ui.com/custom-catalog). For information on material catalog components, see Material catalog components (/gemini/enterprise/docs/a2ui-agents/a2ui-component-galleryreference#material_catalog_components) 

**Note:** Gemini Enterprise supports A2UI versions v0.9 and v0.8. For more information about A2UI versions, see Specification Versions (https://a2ui.org/#specification-versions) in the A2UI documentation. 

### Register an agent using A2UI and A2A

To register your agent and enable it to interact with Gemini Enterprise using A2UI and the A2A Protocol, follow these steps: 

#### Configure your agent to use A2UI and the A2A protocols

Implement the specifications and libraries provided by Agent to UI (A2UI) (https://a2ui.org/introduction/what-is-a2ui/) for building interactive user interfaces and the Agent2Agent (A2A) Protocol (https://a2a-protocol.org/) for secure and standardized communication. This ensures that your agent can render user interfaces and communicate effectively with Gemini Enterprise. 

#### Host your agent

Deploy your configured agent to a publicly accessible endpoint. You can use Google Cloud resources for hosting, such as: 

- **Agent Runtime on Gemini Enterprise Agent Platform** : A fully managed service designed for deploying and scaling AI agents. 

- **Cloud Run** : A serverless compute platform that lets you run containerized applications, which provides flexibility and automatic scaling. 

Your agent must be accessible to Gemini Enterprise for A2A Protocol communication. 

**Tip:** You must host and maintain your agents for them to function within Gemini Enterprise. 

#### Register the agent as an A2A agent with Gemini Enterprise

After your agent is hosted and accessible, a Gemini Enterprise administrator must register it with Gemini Enterprise as an A2A agent. For more information, see Register and manage A2A agents 

(/gemini/enterprise/docs/register-and-manage-an-a2a-agent). 

#### Manage agents

After registering your agents with Gemini Enterprise, a Gemini Enterprise administrator can view and manage the agents on the **Agents** page. For more information, see Agents overview (/gemini/enterprise/docs/agents-overview). 

### What's next

- For a reference of available A2UI components, see A2UI component gallery reference (/gemini/enterprise/docs/a2ui-agents/a2ui-component-gallery-reference). 

Last updated 2026-10-14 UTC. 



## Tutorial: Host an agent on Cloud Run

URL: https://docs.cloud.google.com/gemini/enterprise/docs/a2ui-agents/tutorial-host-agent-cloud-run

This tutorial explains how to deploy an Agent-to-Agent (A2A) agent, built with the Agent Development Kit (ADK) and the A2UI extension, to Cloud Run. You also learn how to register the deployed agent with Gemini Enterprise. 

**Note:** Gemini Enterprise supports A2UI versions v0.9 and v0.8. For more information about A2UI versions, see Specification Versions (https://a2ui.org/#specification-versions) in the A2UI documentation. 

This example uses publicly available sample code. The sample code for this tutorial has the following folder structure. 

<sup>Tutorial folder structure</sup> 

The project has the following folder structure: 

|File/Directory|Description|
|---|---|
|`/samples/community/agent/adk/gemini_enterprise/`<br>`v0_9`|Directory containing example configurations and data for this tutorial.|
|`__init__.py`|Marks the directory as a Python package.|
|`__main__.py`|The entry point to run the agent locally.|
|`agent.py`|Defines the agent, its skills, and behavior.|
|`agent_executor.py`|Manages the execution flow and tool interactions.|
|`deploy.sh`|Script to build and deploy the agent to Cloud Run.|
|`examples/`|Directory containing component template examples.|
|`gemini_enterprise_composite_catalog.json`|Component catalog defining standard Material and custom Gemini Enterprise<br>components.|
|`main.py`|The main application entry point (FastAPI app).|
|`prompt_builder.py`|Helper to construct prompts for the model.|
|`pyproject.toml`|Project configuration and dependencies.|
|`examples/0.9/material_table_orders.json`|Sample UI template containing the layout and mock data for the recent orders demo.|
|`tools.py`|Defines the tools (functions) the agent can use.|

### Before you begin

Before you begin, make sure you have the following: 

The Discovery Engine Admin (/gemini/enterprise/docs/access-control#discoveryengine.admin) role. 

An existing Gemini Enterprise app. To create an app, see Create an app (/gemini/enterprise/docs/create-app). 

- Clone the repository and navigate to the `v0_9` sample directory: 

```
git clone https://github.com/a2ui-project/a2ui.git
cd a2ui/samples/community/agent/adk/gemini_enterprise/v0_9
```

### Enable APIs

Enable the following APIs for your project: 

ConsoleREST (#rest) (#console) 

Enable the following APIs: 

- Vertex AI API Cloud Build API Artifact Registry API Cloud Run API Cloud Logging API Discovery Engine API Cloud Storage API 

- Identity and Access Management (IAM) API 

Enable APIs (https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,cloudbuild.googleapis.com,artifactregistry.g 

### Grant permissions

Grant permission to the Cloud Run Invoker ( `roles/run.invoker` ) role. 

```
gcloud projects add-iam-policy-binding PROJECT_ID \
  --member="serviceAccount:service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com" \
  --role="roles/run.invoker"
```

Replace the following: 

_PROJECT_ID_ : the ID of your project. 

_PROJECT_NUMBER_ : Your Google Cloud project number. 

### Deploy the agent

The `deploy.sh` script automates the deployment process. To deploy your agent, run the script from the project directory with your Google Cloud ID and a name for your new service. You can also optionally specify the Gemini model to use. 

The script performs the following actions: 

1. **Builds** a container image from your source code. 

2. **Pushes** the image to Artifact Registry. 

3. **Deploys** the image to Cloud Run. 

4. **Sets** environment variables, including the `MODEL` and the public `AGENT_URL` of the service itself. 

Replace the following: 

_PROJECT_ID_ : the ID of your project. 

_MODEL_NAME_ : Optional. This is the third argument to the script. Supported values are `gemini-2.5-pro` and `gemini-2.5flash` . If not provided, the script defaults to `gemini-2.5-flash` . 

Once the script completes, it prints the service URL of your deployed agent. You need this **Service URL** in the next step. 

### Register agent with Gemini Enterprise

Now that your agent is deployed, you need to register it with Gemini Enterprise to make it discoverable. 

Run the following `curl` command, replacing the placeholders with your own values: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"
https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/collections/default_collectio
n/engines/ENGINE_ID/assistants/default_assistant/agents -d '{
 "name": "a2ui-demo-agent",
 "displayName": "A2UI v0.9 Demo Agent",
 "description": "A demo agent that showcases A2UI v0.9 UI templates.",
 "a2aAgentDefinition": {
     "jsonAgentCard": "{\"protocolVersion\": \"0.3.0\", \"name\": \"A2UI v0.9 Demo\", \"description\": \"A demo agent
that showcases A2UI v0.9 UIs built from the Material component catalog and Gemini Enterprise custom components (Canvas,
Iframe). Ask it what can you do? to see the available demos.\", \"url\": \"AGENT_URL\", \"version\": \"1.0.0\",
\"capabilities\": {\"streaming\": true, \"preferredTransport\": \"JSONRPC\", \"extensions\": [{\"uri\":
\"https://a2ui.org/a2a-extension/a2ui/v0.9\", \"description\": \"Ability to render A2UI v0.9\", \"required\": false,
\"params\": {\"supportedCatalogIds\":
[\"https://www.gstatic.com/vertexaisearch/a2ui/v0_9/gemini_enterprise_composite_catalog.json\"]}}]}, \"skills\":
[{\"id\": \"a2ui_demo\", \"name\": \"A2UI v0.9 Component Demo\", \"description\": \"Demonstrates A2UI v0.9 UIs built
from the Material catalog and Gemini Enterprise custom components: cards, forms & inputs, tabs, tables, progress
indicators, dialogs & menus, the Canvas side panel, and the Iframe (IFrameSrcdoc / IFrameUrl) components.\"}],
\"defaultInputModes\": [\"text/plain\"], \"defaultOutputModes\": [\"text/plain\"]}"
   }
}'
```

Replace the following: 

_`PROJECT_NUMBER`_ : Your Google Cloud project number. 

_`LOCATION`_ : The multi-region of your data store: `global` , `us` , or `eu` 

_`ENGINE_ID`_ : The ID of the app with which you want to register the agent. 

_`AGENT_URL`_ : The service URL of your deployed agent. 

#### Unregister agent (Optional)

If you want to unregister the agent, run the following `curl` command: 

```
curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"
https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER/locations/LOCATION/collections/default_collectio
n/engines/ENGINE_ID/assistants/default_assistant/agents/AGENT_ID
```

Replace the following: 

_`PROJECT_NUMBER`_ : Your Google Cloud project number. 

_`LOCATION`_ : The multi-region of your data store: `global` , `us` , or `eu` 

- _`ENGINE_ID`_ : The ID of the app with which the agent is registered. 

- _`AGENT_ID`_ : The ID of the agent that you want to delete. 

### Use the agent on the Gemini Enterprise web app

After an agent is created and registered, you can start using and interacting with it on the Gemini Enterprise web app. 

#### Get the web app URL

To use the agent, you first need to get the web app URL. A Gemini Enterprise administrator can get and share the web app URL by following these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you registered the agent with. 

3. Click **Integrations** . 

4. Copy the **The link to your web app:** and share it with the users in the organization. 

#### Use the agent

To use and interact with the agent, do the following: 

1. Open the web app URL in a new browser tab. 

2. In the web app navigation menu, click **Agents** . 

3. Go to the **From your organization** section, and click the agent that you created. 

4. This opens the conversational interface for the agent. Start asking questions and interacting with the agent. 

For example, you can use a prompt like `Show me the recent orders table` to get information on recent orders that are part of the sample data. The agent retrieves the order information from `material_table_orders.json` and renders the list in the chat using custom UI components, as shown in the following example: 

Last updated 2026-10-14 UTC.
