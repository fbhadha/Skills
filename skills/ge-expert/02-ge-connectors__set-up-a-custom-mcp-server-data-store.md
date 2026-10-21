# Gemini Enterprise: connectors and data stores / Set up a custom MCP server data store to Overview of managed policy constraints
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 613-653, extracted 2026-10-18

Contains:
- Set up a custom MCP server data store (pages 613-622) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server
- Configure citations for custom MCP data stores (pages 623-636) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/configure-citations-for-custom-mcp-data-stores
- Override constraint for custom MCP data stores (pages 637-642) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores
- Import MCP servers from Agent Registry (pages 643-648) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/import-govern-mcp-server-agent-registry
- Overview of managed policy constraints (pages 649-653) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview

## Set up a custom MCP server data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

**Key Term:** In the Model Context Protocol (MCP) specification, capabilities are called _tools_ . In Gemini Enterprise data stores, these tools are referred to as _actions_ . The two terms can be used interchangeably. 

This page explains how to connect your data sources using a custom Model Context Protocol (MCP) server, letting Gemini Enterprise securely access your company's private data. 

The custom MCP data store lets you integrate public tools, as well as MCPcompliant third-party systems, directly into Gemini Enterprise. This approach provides a unified method to connect legacy systems when standard connectors are unavailable. With this integration, your AI agents can access business-critical information and specialized logic within your infrastructure. 

### Limitations

The custom MCP server has the following limitations: 

- **Server-Sent Events (SSE)** : The old `SSE` transport is not supported. The connector exclusively supports the new `StreamableHTTP` transport. 

- **TLS certificate requirement** : Both public and private MCP servers must be configured with a TLS certificate signed by a publicly trusted Certificate Authority (CA). Self-signed certificates are not supported. 

- **Actions limit** : To ensure optimal performance, limit the number of enabled actions in your custom MCP server data store to 100 at a time. For more information, see Enable actions (#enable-actions). 

- **Existing data stores** : Connecting to an existing data store is not supported. You must create and register a new custom MCP server data store directly within your Gemini Enterprise app. 

- **VPC Service Controls** : Egress controls are enforced through organization policy constraints, such as `allowedEgressFqdns` and `allowedDataSources` , rather than runtime traffic enforcement. Custom MCP servers are supported in VPC Service Controls-enabled projects when you explicitly allow the required egress domains and data sources. For more information, see Override the organization policy for Custom MCP data stores 

- (/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custommcp-data-stores) 

### Before you begin

Before you set up your custom MCP server connection, ensure you perform the following: 

- Several organization policy constraints apply to Custom MCP data stores. You must: 

   - Override the organization policy constraint that blocks Custom MCP data store creation. For more information, see Override the organization policy for Custom MCP data stores 

   - (/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-forcustom-mcp-data-stores) 

   - Explicitly allow the fully qualified domain names (FQDNs) for your custom MCP server URL, authorization URL, and token URL. For more information, see Configure allowed egress FQDNs 

   - (/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns). 

**Note:** You only need to add the domain name, not the full URL. For example, for an MCP server URL of **`https://api.cymbal.com/mcp`** with authorization and token URLs on **`auth.cymbal.com`** , allow both **`api.cymbal.com`** and **`auth.cymbal.com`** . 

- If project enforcement is enabled or the project is VPC Service Controlsprotected, you must add `custom_mcp` to the allowed data sources. See Configure allowed data sources 

- (/gemini/enterprise/docs/connectors/configure-allowed-data-sources). 

Grant the **Discovery Engine Editor** role ( `roles/discoveryengine.editor` ). This role is required for your administrator to create the data store. 

To grant this role, do the following: 

1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Locate the user account, and click the **Edit** icon. 

3. Grant the `Discovery Engine Editor` role to your user. For more information, see IAM roles and permissions 

(https://cloud.google.com/gemini/enterprise/docs/access-control). 

Register Gemini Enterprise as an OAuth client application with your identity provider (for example, Okta, Azure AD, or Google). 

To register the app, do the following: 

1. Set the authorization redirect URL to 

`https://vertexaisearch.cloud.google.com/oauth-redirect` . 

2. Grant necessary OAuth scopes to the client app. 

After you register the client app, obtain the `client_id` and `client_secret` that are needed for configuring the custom MCP server data store in the following steps. 

If your custom MCP server is hosted on Cloud Run and requires authentication, grant the **Cloud Run Invoker** ( `roles/run.invoker` ) role to the service agent. For more information, see Set up authentication for a custom MCP server on Cloud Run (#cloud_run_authentication). 

### Set up authentication for a custom MCP server on Cloud Run

If your custom MCP server is hosted on Cloud Run and requires authentication, Gemini Enterprise can securely connect to private services that do not allow public access. 

<sup>How authentication works</sup> 

- When you connect to a Cloud Run service, Gemini Enterprise automatically sends the following authorization headers in each request: 

   - **`X-Serverless-Authorization`** : Contains a Google-signed ID token that authenticates the Gemini Enterprise service agent. 

**`Authorization`** : Preserves the user's OAuth token intact. 

**Note** : Gemini Enterprise automatically sends the Google-signed ID token only when you connect to a default Cloud Run URL that ends in **`.run.app`** . The ID token is not sent if your service uses a custom domain. 

#### Grant access to the service agent

To authorize Gemini Enterprise to invoke your private Cloud Run service, grant the **Cloud Run Invoker** ( `roles/run.invoker` ) role to the Gemini Enterprise service agent on the receiving service. 

The service agent email uses the following format: `service-` _`PROJECT_NUMBER`_ `@gcp-sa-discoveryengine.iam.gserviceaccount.com` 

Replace _`PROJECT_NUMBER`_ with the project number of the Google Cloud project that hosts your Gemini Enterprise app. 

For instructions on how to grant IAM roles on a service, see Authenticating serviceto-service (/run/docs/authenticating/service-to-service). 

### Create the custom MCP server data store

**Note:** By default, outbound traffic to your custom MCP server doesn't route through Agent Gateway (/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-ge-deploy) unless you configure egress routing in the **Advanced options** section. 

To set up the configuration flow, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data stores** . 

3. Click **Create data store** . 

4. On the **Select a data source** page, enter _Custom MCP Server_ into the **Search sources** field. The **Custom MCP Server** card displays. 

5. Click **Add MCP server** . The **MCP Server Configuration** page displays. 

6. In the **Authentication settings** section, select one of the following options: 

   - **No authentication** : Select this option if your MCP server does not require authentication. 

      - a. Enter the **MCP Server URL** . This is the endpoint where your MCP server is hosted. It must be an HTTPS URL. Gemini Enterprise only supports the `StreamableHTTP` transport. The URL often ends with `/mcp` . For example, `https://mcp.example.com/mcp` . 

**Note** : If your server is hosted on Cloud Run, enter your default service URL ending in **`.run.app`** . Gemini Enterprise automatically sends a Google-signed ID token for IAM authentication. 

- b. Click **Continue** . 

**OAuth 2.0** : Select this option to add authentication. 

- a. Enter the values in the following required fields: 

Field Description MCP Server This is the endpoint where your MCP server is hosted. It must URL be an HTTPS URL. Gemini Enterprise only supports the `StreamableHTTP` transport. The URL often ends with `/mcp` . For example, `https://mcp.example.com/mcp` . 

Note: If your server is hosted on Cloud Run, enter your default service URL ending in **`.run.app`** . Gemini Enterprise automatically sends a Google-signed ID token for IAM authentication. 

Authorization The base URL for the user to authorize Gemini Enterprise to URL access your MCP server. For example, `https://mcp.example. com/authorize` . 

Note: Enter only the base URL, without query parameters. Gemini Enterprise automatically appends standard OAuth parameters (such as **`client_id`** , **`redirect_uri`** , and **`scope`** ) during authorization. If your authorization server requires additional parameters, specify them in the Authorization URL Parameters field. Authorization Optional. Any additional parameters required by your URL authorization URL. For example, to get a refresh token from a Parameters Google MCP server, enter `&access_ type=offline&prompt=consent` . If your authorization server requires an `audience` parameter, you can add it as a parameter in this setting. For example, `&audience=https://api.your-domain.com/v1/` . Token URL The endpoint used to exchange the authorization code for an access token during OAuth authentication. For example, `https://mcp.cymbal.com/token` . Client ID The unique identifier of the OAuth app that you registered in your identity provider to represent Gemini Enterprise. 

|Field|Description|
|---|---|
|Enable PKCE<br>Support|Optional. Select this checkbox to enable Proof Key for Code<br>Exchange (PKCE, RFC 7636) for additional OAuth security. We<br>recommend this setting if your MCP server's OAuth provider<br>supports PKCE.|
|Client Secret|The confidential key associated with the OAuth app that you<br>registered in your identity provider to represent Gemini<br>Enterprise.|
|Scopes|The permissions that define what actions Gemini Enterprise is<br>allowed to perform on behalf of a user, or what data it's<br>allowed to access. The scopes are used to access the MCP<br>server. Gemini Enterprise requests these scopes during user<br>authorization. Ensure that your OAuth app is configured to use<br>these scopes.<br>When you specify scopes, consider the following:<br>Provide a space-separated list of scopes. For example, for<br>Box, you provide:`root_readwrite`<br>`manage_managed_users manage_groups`.<br>Ensure the scopes provided are sufficient to let the user<br>sign in and use the tools or actions enabled by the<br>administrator; otherwise, the agent cannot access your<br>app.<br>A common scope is`offline_access`, which lets the app<br>request a refresh token.|

   - b. Click **Verify Auth** . 

   - c. Click **Continue** . 

1. Click **Continue** . 

2. In the **Configure your data connector** section, select the **Location of your data connector** from the **Multi-region** field list. 

3. In **Your data connector name** field, enter a name for your data store. 

4. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the Data Stores page. 

**Note:** By default, no tools or actions from your custom MCP servers are enabled. You must enable the tools or actions. For more information, see Enable actions (#enable-actions). 

**Verify the state of the custom MCP server** 

To verify the state of the custom MCP server, do the following: 

1. Click your data store in the **Data stores** list. The details of your data store display. 

2. Monitor the state of your data store until it changes to `Active` . After the state of your data store changes from `Creating` to `Active` , your custom MCP server data store is ready to be used. 

### Enable actions

**Key Term:** In the Model Context Protocol (MCP) specification, capabilities are called _tools_ . In Gemini Enterprise data stores, these tools are referred to as _actions_ . The two terms can be used interchangeably. 

By default, all actions are turned off. When you connect an MCP server, all of its tools are imported and displayed as actions in the Gemini Enterprise data store. To ensure an optimal experience, you can enable up to 100 actions at a time. To enable these actions for your users, follow these steps: 

1. Go to your custom MCP server data store. 

2. Click **Actions > Reload custom actions** to reauthenticate. 

**Note:** This action performs a **`tools/list`** call on the MCP server to retrieve available tools, which are then displayed on the screen. 

3. Select the actions to enable. 

4. Click **Enable actions** . 

#### Configure annotations to skip user confirmation

When tools from your MCP server are imported as actions into the Gemini Enterprise data store, Gemini Enterprise checks their tool annotations to determine if user confirmation is required. By default, all calls to any action require confirmation from the user, because Gemini Enterprise assumes that any operation is potentially destructive and can mutate data. 

If your server provides read-only functionality (such as querying a database) and you want to skip this confirmation for a smoother user experience, you can configure annotations in the specifications of your MCP tools before they are imported as actions. 

We recommend configuring the following annotations in your MCP tool definitions to manage user confirmation for data store actions: 

- `readOnlyHint` : Add this annotation to your tool definition if the operation is non-destructive and only reads data. The tool execution bypasses user confirmation. 

- `destructiveHint` : Explicitly use this annotation if the tool modifies data. This maintains the default confirmation behavior. 

For example, in Python: 

```
@mcp.tool(annotations={
```

- `"destructiveHint": False,` 

- `"readOnlyHint": True })` 

To ensure that your changes are reflected in your setup, reload custom actions. For more information, see Enable actions (#enable-actions). 

### What's next

- To protect against malicious inputs and outputs, enable Model Armor. For more information, see Enable Model Armor 

(/gemini/enterprise/docs/enable-model-armor). 

- If you want to query your MCP server using a custom agent, instead of the Gemini Enterprise assistant, see Create an agent 

- (/gemini/enterprise/docs/workflow-builder/create-chat-agent). 

- If the data store is not connected to an app, see Connect a data store to app and authorize Gemini Enterprise 

(/gemini/enterprise/docs/connectors/connect-existing-data-store). 

- To use your agent that's connected to your custom MCP server, see Use an agent (/gemini/enterprise/docs/workflow-builder/use-chat-agent). 

- To display source citation chips when Gemini Enterprise answers a question using tools on your custom MCP server, see Configure citations for custom MCP data stores 

(/gemini/enterprise/docs/connectors/custom-mcp-server/configure-citations-for-custommcp-data-stores) 

Last updated 2026-10-16 UTC. 



## Configure citations for custom MCP data stores

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/configure-citations-for-custom-mcp-data-stores

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

**Key Term:** In the Model Context Protocol (MCP) specification, capabilities are called _tools_ . In Gemini Enterprise data stores, these tools are referred to as _actions_ . The two terms can be used interchangeably. 

Citation mappings for custom Model Context Protocol (MCP) data stores let you display source citation chips when Gemini Enterprise answers a question using tools on your custom MCP server. Because each MCP server returns results in its own JSON structure, you can configure the `citation_mappings` action parameter using the Discovery Engine REST API to specify where each tool's response stores the link, title, snippet, and ID for each result. 

You can configure `citation_mappings` only by using the `v1` REST API. This parameter isn't available in the Google Cloud console. 

### Before you begin

Before you configure citation mappings for a custom MCP data store, make sure you've completed the following prerequisites: 

- Create a custom MCP server data store and enable its actions. For more information, see Set up your custom MCP server data store 

- (/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server). 

- Ensure that you have the Discovery Engine Editor 

- (/gemini/enterprise/docs/access-control#discoveryengine.editor) or Gemini Enterprise Admin (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

- Obtain the collection ID ( _`COLLECTION_ID`_ ) for your custom MCP data store. A custom MCP data store's ID is _`COLLECTION_ID`_ `_mcp_data` , so you can take the data store ID from the Google Cloud console and remove the `_mcp_data` suffix instead of calling the `collections` API. For more information on how to find the collection ID of your data store, see Get data store and entity details (/gemini/enterprise/docs/get-datastore-details). 

### How citation mappings work

When Gemini Enterprise calls a tool on your custom MCP server to answer a user's question, the answer can display citation chips (small cards that link claims in the answer to their source documents). Citation chips are separate from inline Markdown links that a model might generate in the answer text based on its instructions. 

To build a citation chip, Gemini Enterprise extracts up to four fields from each result returned by the tool: a link ( `uri` ) , a title ( `title` ) , a short text excerpt ( `snippet` ) , and a source identifier ( `id` ). You define where these fields live in each tool's response using the following concepts: 

- **Tool** : a single function exposed by your MCP server, identified by its bare name, such as `search_docs` . 

- **Tool response** : the JSON payload the tool returns for a single call. 

- **Item** : a single result object inside the tool response. Each item becomes one citation. 

- **Role** : the citation field that a JSON Pointer populates: `items` , `uri` , `title` , `snippet` , or `id` . 

- **JSON Pointer** : a path string standardized in RFC 6901 

- (https://www.rfc-editor.org/rfc/rfc6901) that selects a value from a JSON document. For example, `/results` selects the `results` field, and `/author/name` selects `name` inside `author` . 

#### Structure of the `citation_mappings` parameter

The `citation_mappings` parameter is a JSON object. Each key is a tool name, and each value is an object that maps citation roles to JSON Pointers. 

The `items` pointer locates the list of results from the root of the tool response. The remaining four pointers ( `uri` , `title` , `snippet` , and `id` ) are evaluated relative to each individual item, not from the root of the tool response. In practice, `uri` and `title` have the greatest effect on what users see, and `uri` is required. 

The following table describes each role supported in the mapping object of a tool: 

|Role|Points to|Read from|Behavior if omitted|
|---|---|---|---|
|`item`<br>`s`|List of results|Tool<br>response|List is found automatically using common field names,<br>for example,`results`,`items`,`documents`, or`content`.|
|`uri`|Link that the citation<br>chip opens|Each item|Required. Every covered tool must provide a`uri`, either<br>directly or through the default entry (`""`).|
|`titl`<br>`e`|Title displayed on the<br>citation chip|<br>Each item|Citation chip displays`Untitled`.|
|`snip`<br>`pet`|Short text displayed<br>on the citation chip|Each item|A snippet is selected automatically from common fields<br>on the item, for example,`snippet`,`text`,`description`,<br>or`summary`.|
|`id`|A stable ID for the<br>source|Each item|The`uri`value is used as the ID.|

#### Example citation mappings

Suppose a tool named `search_docs` returns the following JSON payload: 

```
{
 "results": [
   {
     "doc_id": "kb-1042",
     "name": "Expense policy 2026",
     "link": "https://intranet.cymbal.com/kb/1234",
     "summary": "Meals are reimbursed up to 60 USD per day."
   }
 ]
}
```

The following `citation_mappings` configuration maps the fields from `search_docs` to citation chips: 

```
{
 "search_docs": {
   "items": "/results",
   "uri": "/link",
   "title": "/name",
   "snippet": "/summary",
   "id": "/doc_id"
 }
}
```

In this example, `/results` locates the list of items, and `/link` , `/name` , `/summary` , and `/doc_id` are read from each item in that list. The resulting citation chip displays `Expense policy 2026` , links to `https://intranet.cymbal.com/kb/1234` , and shows the summary as its snippet. 

If several tools return results in the same shape, you can define a default entry ( `""` ) and override specific roles only where needed: 

```
{
 "": {
   "items": "/results",
   "uri": "/link",
   "title": "/name"
 },
 "get_doc": {
   "items": ""
 }
}
```

In this configuration, `get_doc` inherits `uri` ( `/link` ) and `title` ( `/name` ) from the default entry, and overrides `items` with `""` because `get_doc` returns a single document 

object rather than a list under `/results` . 

#### Tool key rules

The following rules apply to tool keys in `citation_mappings` : 

- **Use bare tool names** : specify the tool name exactly as the MCP server declares it, without a server or connector prefix. 

- **Default entry (** **`""` )** : the empty key `""` defines a default mapping that applies to every tool on the connector. A named tool entry overrides the default entry one role at a time. For example, a tool entry that sets only `uri` inherits `items` , `title` , `snippet` , and `id` from the default entry. 

- **Unmapped tools** : when no default entry ( `""` ) is present, any tool without a named entry isn't covered by the mapping. 

- **Maximum entries** : `citation_mappings` supports up to 101 entries (up to 100 named tools plus the `""` default entry). 

#### JSON Pointer evaluation rules

JSON Pointers in `citation_mappings` follow RFC 6901 

(https://www.rfc-editor.org/rfc/rfc6901). Keep the following rules in mind when writing pointers: 

- **Empty pointer** **(** **`""` )** : an empty string `""` refers to the entire JSON document or item. For `items` , use `""` when the tool response itself is a list of items or a single result object. 

- **Leading slash (** **`/` )** : every nonempty pointer must start with `/` and can be up to 512 characters long. For example, `/results` is valid, whereas `results` is invalid. 

- **Array indices** : non-negative integers select zero-based list positions. For example, `/links/0/href` selects the `href` field of the first element in `links` . 

- **Escaped characters** : two characters must be escaped inside field names: write `~1` for `/` and `~0` for `~` . For example, a field literally named `a/b` is written as `/a~1b` . 

**Exact, case-sensitive matching** : pointer matching is exact and casesensitive. Except for `snippet` , if a pointer doesn't match a field, Gemini Enterprise doesn't guess another field: 

   - A missed `title` pointer displays `Untitled` on the citation chip. 

   - A missed `uri` pointer on an individual item means the item is still used to generate the answer, but no citation link is displayed for that item. 

   - A missed `snippet` pointer falls back to selecting a snippet automatically from common fields on the item. 

- **Single-object** **`items`** : if `items` resolves to a JSON object instead of a list, Gemini Enterprise treats that object as a single result item. 

- **Automatic fallback** : if the mapping finds nothing usable for a call—for example, if the `items` pointer matches nothing or no result item has a `uri` — the mapping steps aside and Gemini Enterprise falls back to its automatic response handling for that response. 

How MCP response wrappers are handled 

How you write the `items` pointer depends on how your MCP server formats its tool responses: 

- **JSON serialized inside a text block** : many MCP servers return JSON as a string inside a text content block ( `{"content": [{"type": "text", "text": "..."}]}` ). The `text` field must contain a valid serialized JSON string. Gemini Enterprise decodes that JSON string first, so you write pointers against the decoded JSON that the tool returns, not against the outer `content` wrapper. If a tool returns unstructured plain text, such as raw Markdown or free-form strings, JSON Pointers can't evaluate it, and `citation_mappings` doesn't extract citation chips. 

- **Structured content** : if your MCP tool returns structured content, pointers address the top-level MCP result object. To reach a list inside `structuredContent` , include `/structuredContent` in your pointer, such as `/structuredContent/results` . When `items` is `""` and `structuredContent.result` is an object, the item pointers ( `uri` , `title` , `snippet` , and `id` ) resolve against `structuredContent.result` itself. For example, a single-object tool can use `/url` instead of `/structuredContent/result/url` . 

### Set or update citation mappings

To configure `citation_mappings` on a custom MCP data store, call the `updateDataConnector` 

(/gemini/enterprise/docs/connectors/custom-mcpserver/reference/rest/v1/projects.locations.collections/updateDataConnector) method in the `v1` API with the `updateMask` query parameter set to `action_config.action_params` . 

Before running the update request, keep the following behaviors in mind: 

- **The entire mapping is replaced** : sending `citation_mappings` overwrites every existing tool entry in the mapping. To add or modify a single tool, send the complete `citation_mappings` object with your changes included. If you already have existing tools mapped, follow these steps: 

   1. Run `getDataConnector` ( `GET` ) and copy only the `citation_mappings` JSON block from `actionParams` . 

   2. Add or modify your tool's entry in that copied block. 

   3. Send the updated `citation_mappings` block in your `PATCH` request. 

**Other connector parameters are preserved** : action parameters that you omit from the request, such as OAuth settings, keep their existing values. Include only `citation_mappings` in `actionParams` . Don't copy all `actionParams` fields from a `GET` response into your `PATCH` request: on OAuth connectors, `GET` doesn't return `client_id` , so sending the `GET` output back fails with `Connector params must contain client_id` . 

- **Use the narrow update mask** : specify 

- `updateMask=action_config.action_params` . Although `updateMask=action_config` is also accepted, it rewrites other `actionConfig` fields that aren't included in your request. 

- **Changes apply to new chats** : chats that are already open keep the connector settings that they started with. Start a new chat session to test updated citation mappings. 

- **Mappings belong to a single connector** : if you delete a custom MCP data store and create it again, the recreated data store has no citation mapping, and you must configure `citation_mappings` again. 

To set or update `citation_mappings` , run the following command: 

```
curl -X PATCH \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \` 

```
 -H "X-Goog-User-Project: PROJECT_ID" \
"https://ENDPOINT/v1/projects/PROJECT_NUMBER/locations/LOCATION/collections/
COLLECTION_ID/dataConnector?updateMask=action_config.action_params" \
 -d '{
   "actionConfig": {
     "actionParams": {
       "citation_mappings": {
         "search_docs": {
           "items": "/results",
           "uri": "/link",
           "title": "/name"
         }
       }
     }
   }
 }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`ENDPOINT`_ : the API endpoint for the location of your data store: 

   - `discoveryengine.googleapis.com` for the `global` location 

   - `us-discoveryengine.googleapis.com` for the `us` multi-region 

   - `eu-discoveryengine.googleapis.com` for the `eu` multi-region 

- _`PROJECT_NUMBER`_ : the number of your Google Cloud project. 

- _`LOCATION`_ : the location of your data store ( `global` , `us` , or `eu` ) . 

- _`COLLECTION_ID`_ : the ID of the collection that contains your custom MCP data store. 

To confirm that the update worked, see Verify citation mappings (#verify-citation-mappings). 

### View citation mappings

To read the current citation mappings for a custom MCP data store, call the `getDataConnector` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections/getDataConnector) method on the data connector resource: 

```
curl -X GET \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "X-Goog-User-Project:` _`PROJECT_ID`_ `" \` 

```
"https://ENDPOINT/v1/projects/PROJECT_NUMBER/locations/LOCATION/collections/
COLLECTION_ID/dataConnector"
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`ENDPOINT`_ : the API endpoint for the location of your data store: 

   - `discoveryengine.googleapis.com` for the `global` location 

   - `us-discoveryengine.googleapis.com` for the `us` multi-region 

   - `eu-discoveryengine.googleapis.com` for the `eu` multi-region 

- _`PROJECT_NUMBER`_ : the number of your Google Cloud project. 

- _`LOCATION`_ : the location of your data store ( `global` , `us` , or `eu` ) . 

- _`COLLECTION_ID`_ : the ID of the collection that contains your custom MCP data store. 

In the response, the configured mapping appears under `actionConfig.actionParams.citation_mappings` . When no mappings are configured, including right after sending `"citation_mappings": {}` , the response omits 

`citation_mappings` from `actionConfig.actionParams` entirely rather than returning `{}` . 

### Verify citation mappings

After you set or update citation mappings, check that they work: 

1. Call `getDataConnector` as described in View citation mappings (#view-citation-mappings) and confirm that your mapping appears under `actionConfig.actionParams.citation_mappings` . 

2. In Gemini Enterprise, start a new chat. Chats that were already open keep the connector settings that they started with. 

3. Ask a question that makes the agent call one of the mapped tools. 

4. In the chat response, check for the tool execution indicator or card, such as under **Show thinking** , to confirm that the agent invoked the mapped tool. If the model answers from its own knowledge without calling the tool, citation chips don't appear. 

5. Confirm that the answer displays citation chips with the expected title, description or snippet and link. 

If citation chips don't appear, see Troubleshoot citation mappings 

(#troubleshoot-citation-mappings). 

### Remove citation mappings

To remove all citation mappings from a custom MCP data store, send an empty object ( `"citation_mappings": {}` ) in `actionConfig.actionParams` : 

```
curl -X PATCH \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \` 

- `-H "X-Goog-User-Project:` _`PROJECT_ID`_ `" \` 

```
"https://ENDPOINT/v1/projects/PROJECT_NUMBER/locations/LOCATION/collections/
COLLECTION_ID/dataConnector?updateMask=action_config.action_params" \
 -d '{
   "actionConfig": {
     "actionParams": {
       "citation_mappings": {}
     }
   }
 }'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`ENDPOINT`_ : the API endpoint for the location of your data store: 

   - `discoveryengine.googleapis.com` for the `global` location 

   - `us-discoveryengine.googleapis.com` for the `us` multi-region 

   - `eu-discoveryengine.googleapis.com` for the `eu` multi-region 

- _`PROJECT_NUMBER`_ : the number of your Google Cloud project. 

- _`LOCATION`_ : the location of your data store ( `global` , `us` , or `eu` ) . 

- _`COLLECTION_ID`_ : the ID of the collection that contains your custom MCP data store. 

### Troubleshoot citation mappings

If citation mappings are rejected by the API or citation chips don't appear as expected, check the following validation errors and common issues. 

#### Validation errors

Malformed mappings are rejected with a `400 INVALID_ARGUMENT` error. The error message identifies the tool and role at fault: 

Error message (abbreviated) Cause and resolution 

`must be an object mapping each citation_mappings` isn't a JSON object. Ensure that the `tool name to its citation field` value of `citation_mappings` is a JSON object ( `{...}` ). `pointers` 

|`declares`_`N`_`tools, more than the`<br>`supported maximum of`<br>`101`|<br>The mapping contains too many entries. Reduce the<br>number of entries to at most 100 named tools plus the<br>default entry (`""`).|
|---|---|
|`entry for tool "`_`TOOL_NAME`_`" must`<br>`be an object mapping`<br>`citation role to JSON`<br>`Pointer`|<br>A tool's value isn't a JSON object. Map each tool name to<br>an object containing role-to-pointer key-value pairs.|
|`entry for tool "`_`TOOL_NAME`_`" has`<br>`unknown citation role`<br>`"`_`ROLE`_`"`|<br>A role name is misspelled, such as`titel`instead of<br>`title`. Valid roles are`items`,`uri`,`title`,`snippet`, and<br>`id`.|
|`role "`_`ROLE`_`" on tool "`_`TOOL_NAME`_`"`<br>`must be a`<br>`string JSON Pointer`|<br>A pointer value isn't a string. Format every JSON Pointer<br>value as a JSON string.|
|`exceeds the maximum pointer`<br>`length of 512 characters`|A JSON Pointer is too long. Shorten the pointer to 512<br>characters or fewer.|
|`is not a valid RFC 6901 JSON`<br>`Pointer`|A nonempty pointer is missing a leading`/`, or contains an<br>invalid`~`escape sequence. Use`~0`for`~`and`~1`for`/`.|
|`entry for tool "`_`TOOL_NAME`_`"`<br>`declares no "uri"`<br>`role`|Neither the named tool entry nor the default entry (`""`)<br>specifies a`uri`pointer. Add a`uri`role to the tool entry or<br>the default entry.|
|`Data Connector parameters must`<br>`be one of: ... but got:`<br>`citation_mapping`|<br>The parameter name in`actionParams`is misspelled. Use<br>`citation_mappings`.|

**Note:** A default entry ( **`""`** ) is exempt from the **`uri`** requirement when named tool entries are also present, because each named tool entry can supply its own **`uri`** . 

#### Common issues

If your mapping saves without errors but citation chips don't appear or show unexpected values, check for the following common mistakes: 

- **Writing item pointers from the root of the response** : after `items` selects the list of results, role pointers ( `uri` , `title` , `snippet` , and `id` ) are read relative to a single item. Specify `/link` , not `/results/0/link` . 

- **Prefixing the tool name** : don't prefix the tool name with the MCP server name or connector name. Use the bare tool name declared by the MCP server. 

- **Sending only the changed tool in an update** : updating `citation_mappings` replaces the entire mapping object. When modifying one tool's mapping, include all other tool entries that you want to keep. 

- **Testing in an existing chat** : updated mappings apply only to new chats. Start a new chat session after updating `citation_mappings` . 

- **Confusing citation chips with inline links** : Markdown links written into the answer text by the model's instructions are separate from the source citation chips controlled by `citation_mappings` . 

### What's next

- Set up your custom MCP server data store 

- (/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server) 

- Override the organization policy for Custom MCP data stores 

- (/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custommcp-data-stores) 

Import MCP servers from Agent Registry 

- (/gemini/enterprise/docs/connectors/custom-mcp-server/import-govern-mcp-serveragent-registry) 

Last updated 2026-10-16 UTC. 



## Override constraint for custom MCP data stores

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/override-constraint-for-custom-mcp-data-stores

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

By default, Gemini Enterprise blocks the creation of Model Context Protocol (MCP) data stores using a managed organization policy constraint. To enable the creation of Custom MCP data stores, an Organization Policy Administrator must override this restriction. 

### Before you begin

- Ensure you have the **Organization Policy Administrator** role ( `roles/orgpolicy.policyAdmin` ). 

**Note:** This role might only be available to project owners and is only applicable if your project is part of an organization. 

- Understand the policy enforcement dependencies and interactions. For more information, see Overview of managed policy constraints 

- (/gemini/enterprise/docs/connectors/managed-policy-constraints-overview). 

### Example usage scenarios

To understand how these policies work together, consider an organization that wants to allow users to create a Custom MCP data store that connects to `api.cymbal.com` in a project named `cymbal-project` . 

<sup>The project is VPCSC protected</sup> 

Setup 

`cymbal-project` is protected by a VPC Service Controls perimeter (VPCSC state: Enabled). 

Requirement 

To create the data store and allow it to connect to `api.cymbal.com` , the organization administrator must: 

1. Turn off the Disable custom MCP server connector for Gemini Enterprise managed constraint to enable Custom MCP. 

2. Add `custom_mcp` to the `allowedDataSources` parameter in the Restrict allowed data sources for data connectors policy. For more information, see Configure allowed data sources (/gemini/enterprise/docs/connectors/configure-allowed-data-sources). 

3. Add `api.cymbal.com` to the `allowedEgressFqdns` parameter in the Restrict egress domains for data connectors policy. For more information, see Configure allowed egress FQDNs for data stores (/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns). 

Why 

Because VPCSC is enabled, policies are enforced automatically. 

<sup>Project not VPCSC protected, but enforced through the policy</sup> 

Setup 

`cymbal-project` is not in a VPC Service Controls perimeter (VPCSC state: Not enabled), but the administrator added it to the `enforcedProjects` parameter in both policies. 

Requirement 

To create the data store and allow it to connect to `api.cymbal.com` , the organization administrator must: 

1. Turn off the Disable custom MCP server connector for Gemini Enterprise managed constraint to enable Custom MCP. 

2. Add `custom_mcp` to the `allowedDataSources` parameter in the Restrict allowed data sources for data connectors policy. For more information, see Configure allowed data sources (/gemini/enterprise/docs/connectors/configure-allowed-data-sources) 

3. Add `api.cymbal.com` to the `allowedEgressFqdns` parameter in the Restrict egress domains for data connectors policy. For more information, see Configure allowed egress FQDNs for data stores (/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns). 

Why 

The project is opted-in to enforcement using `enforcedProjects` . 

<sup>The project is not VPCSC protected or enforced through the policy</sup> 

Setup 

`cymbal-project` is not in a VPC Service Controls perimeter (VPCSC state: Not enabled) and is not listed in the `enforcedProjects` parameter for either policy. 

Requirement 

To create the data store and allow it to connect to `api.cymbal.com` , the organization administrator must: 

1. If the Disable custom MCP server connector for Gemini Enterprise managed constraint is enabled, turn it off to enable Custom MCP. 

2. No updates are needed for the Restrict allowed data sources for data connectors policy. 

3. No updates are needed for the Restrict egress domains for data connectors policy. 

Why 

The Restrict egress domains for data connectors and Restrict allowed data sources for data connectors policies are not enforced on this project. 

### Override the constraint

To create a Custom MCP server data store in your Google Cloud project, you must override the existing managed organization policy constraint. Follow these steps: 

1. In the Google Cloud console, go to the **Organization Policies** page. 

Go to Organization Policies (https://console.cloud.google.com/iam-admin/orgpolicies) 

2. In the project selector, select the project for which you want to change enforcement. 

**Important:** Select the specific project for which you want to change enforcement. Setting the policy at the organization level changes enforcement for all projects in the organization. 

3. In the **Filter** field, enter `Disable custom MCP server connector for Gemini Enterprise` . 

4. Click the policy name to navigate to the policy details page. 

5. Click **Manage Policy** . 

6. Select the option to **Override parent's policy** . 

7. Add a new rule and set the enforcement toggle to **OFF** . 

8. Click **Set Policy** . 

### Verify the policy change

After you apply the new configuration, verify that the policy status is updated to **Not enforced** . 

The following image shows the Organization Policy Service details page with the policy set to **Not enforced** : 

### What's next

- Create a custom MCP server data store. For more information, see Set up a custom MCP server 

- (/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server). 

Last updated 2026-10-14 UTC. 



## Import MCP servers from Agent Registry

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-mcp-server/import-govern-mcp-server-agent-registry

As an administrator of Gemini Enterprise, you can add MCP servers from Agent Registry to Gemini Enterprise apps. The MCP servers are added as connected data stores. The MCP servers can be ones that you have created and added to the registry or they can be Google MCP servers that you discovered and added to the registry. 

You can apply access control policies to traffic through Agent Gateway. These policies let you enforce egress governance to control traffic to and from these MCP servers. 

### About Agent Registry

Agent Registry (/agent-registry/overview) is a centralized, queryable catalog that acts as the single source of truth for discovering, tracking, and managing A2A agents, endpoints, and MCP servers. 

The MCP servers in the registry might be MCP servers created by Google or MCP servers that you have created for your end users. 

You can add MCP servers from Agent Registry as data stores for your Gemini Enterprise apps. This makes the MCP servers available to the apps' end users. 

### About Agent Gateway

Agent Gateway 

(/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) is also part of the govern pillar of Agent Platform. Agent Gateway is the managed regional networking component of Agent Platform that acts as the traffic controller and runtime policy enforcement point for A2A agents, MCP servers, and endpoints. It secures and governs connectivity: between MCP servers and A2A agents; clients and A2A agents; A2A agents and backend tools; or A2A agents and other agents. 

Before you can add an MCP server to a Gemini Enterprise app, you need to have set up an Agent Gateway through which the MCP server traffic can be routed. See Before you begin (#prerequisites) below. 

### Regional constraints for the registry, gateway, and app

To ensure compliance with data residency requirements, both Agent Registry and Agent Gateway resources are project-and-region-specific. 

A Agent Gateway must be configured to associate with a Agent Registry that is in a region compatible with the Gemini Enterprise app's operational region. This prevents violations of data residency conventions. For example, a Gemini Enterprise app created in the US region must use an Agent Gateway configured with a US-regional Agent Registry, not a global one. 

For Gemini Enterprise apps, the regional alignment is strictly enforced through a specific binding process: 

- The Gemini Enterprise app must bind only to an Agent Gateway located within one of the allowed regions for that app. 

- The selected Agent Gateway must be associated with an Agent Registry. This Agent Registry must also be located in the same specific region as the Agent Gateway and the app. 

- This means the three components (app, gateway, and registry) must be regionally aligned. The table below provides the specific region mappings: 

|Gemini Enterprise app location|Agent Gateway location|Agent Registry location|
|---|---|---|
|`global`|`us-central1`|`us-central1`,`us`, or`global`|
|`us`|`us-central1`|`us-central1`or`us`|
|`eu`|`europe-west1`|`europe-west1`or`eu`|

### Limitations

The following limitations apply when you import MCP servers from Agent Registry and associate those MCP servers with apps: 

- You can only import MCP servers from Agent Registry if the registry is associated with the Agent Gateway set up for the same region as the Gemini Enterprise app. 

- You can apply governance policies only to MCP servers that are in the registry associated with the Agent Gateway. 

- Direct communication between Gemini Enterprise agents and Gemini Enterprise data connectors (including MCP-based connectors such as the custom MCP server) doesn't trigger Agent Gateway policy enforcement. 

### Before you begin

Before you begin, make sure you've completed the following prerequisites: 

- You have the Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

- You've set up a gateway to route agent traffic through Agent Gateway. For more information, see Route Gemini Enterprise traffic through Agent Gateway (/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-ge-deploy). 

### Add MCP servers from Agent Registry to Gemini Enterprise

After you have set up Agent Gateway (Before you begin (#prerequisites) above), then the MCP servers in the associated Agent Registry become available to add as data sources for your Gemini Enterprise apps. 

Console (#console) 

To add an MCP server from Agent Registry to a Gemini Enterprise app, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to add the MCP server to. 

3. Click **Connected data stores** . 

4. Click **+ New data store** . 

5. On the **Select a data source** page, **MCP servers** section, click **Show all** . 

Except for the Custom MCP Server 

(/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcpserver) 

   - , the MCP servers listed in the **MCP servers** section are those in Agent Registry. 

6. Click **Add tool** for the MCP server that you want to add. 

7. Review the imported information. 

8. If the MCP server doesn't require authentication, select **No authentication** , enter the MCP server URL, and click **Continue** . 

9. If the MCP server does require authentication, select **OAuth 2.0** and complete the authentication fields as follows: 

Field Description 

MCP Server URL This is the endpoint where your MCP server is hosted. It must be the same as the one in the interface URLS in the MCP Server details. Gemini Enterprise only supports the `StreamableHTTP` transport, and the URL often ends with `/mcp` . For example, `https://mcp.example.com/mcp` . 

Field Description Authorization The URL for the user to authorize Gemini Enterprise to access URL your MCP server. For example, `https://mcp.example.com/ authorize` . Make sure that the OAuth app has the following redirect URI: `https://vertexaisearch.cloud.google.com/ oauth-redirect` Note: Enter only the base URL, without query parameters. Gemini Enterprise automatically appends standard OAuth parameters (such as **`client_id`** , **`redirect_uri`** , and **`scope`** ) during authorization. If your authorization server requires additional parameters, specify them in the Authorization URL Parameters field. 

Authorization Optional. Any additional parameters required by your URL Parameters authorization URL. For example, to get a refresh token from a Google MCP server, enter `&access_ type=offline&prompt=consent` . If your authorization server requires an `audience` parameter, you can add it as a parameter in this setting. For example, `&audience=https://api.your-domain.com/v1/` . Token URL The endpoint is used for token exchange. For example, `https:// mcp.example.com/token` . Client ID The unique identifier of the OAuth app that you registered in your identity provider to represent Gemini Enterprise. Client Secret The confidential key associated with the OAuth app that you registered in your identity provider to represent Gemini Enterprise. Scopes The permissions that define what actions Gemini Enterprise is allowed to perform on behalf of a user, or what data it's allowed to access. The scopes are used to access the MCP server. Gemini Enterprise requests these scopes during user authorization. Ensure that your OAuth app is configured to use these scopes. When you specify scopes ensure that the provided scopes are sufficient to let the user sign in and use the tools or actions enabled by the administrator; otherwise, the agent cannot access your app. 

### Set up and apply egress governance policies

Using Agent Gateway, you can assess and apply semantic and IAM control policies (/gemini-enterprise-agent-platform/govern/policies/overview) to egress MCP server traffic. You can create granular egress policies to manage agent-to-MCP-server access for your MCP servers. 

You define allow and deny rules restricting an MCP server's access to specific entries within Agent Registry. 

To create and apply egress governance rules to MCP servers, do one of the following: 

- Create IAM agent policies 

- (/gemini-enterprise-agent-platform/govern/policies/configure-iam-policies) 

- Configure semantic governance policies 

- (/gemini-enterprise-agent-platform/govern/policies/configure-semantic-governance) 

Last updated 2026-10-14 UTC. 



## Overview of managed policy constraints

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/managed-policy-constraints-overview

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

This page provides an overview of managed organization policy constraints and their interactions. 

### Policy enforcement dependencies

The enforcement of managed organization policy constraints for data stores depends on several factors: the type of data source you are configuring, whether your project is protected with VPC Service Controls, and whether your project is included in the `enforcedProjects` parameter. 

|Related policy or service|Description|
|---|---|
|Restrict allowed data sources for data<br>connectors<br>(/gemini/enterprise/docs/connectors/confi<br>allowed-data-sources)|igure-<br>If you allow a data source, such as Google Drive<br>or Gmail, in the Restrict allowed data sources<br>for data connectors managed organization<br>policy constraint, then the constraint<br>automatically permits connections to its well-<br>known FQDNs. This permission means you don't<br>need to define these domains in the Restrict<br>egress domains for data connectors managed<br>policy constraint.|
||For projects where the policy is enforced<br>(VPCSC-enabled projects or projects listed in<br>`enforcedProjects`), you must use the Restrict<br>egress domains for data connectors policy to<br>explicitly allow the necessary FQDNs for third-<br>party data sources where FQDNs aren't<br>automatically allowed.|

|Related policy or service|Description|
|---|---|
|Restrict egress domains for data connectors<br>(/gemini/enterprise/docs/connectors/configure<br>allowed-egress-fqdns)|i-<br>For projects where the policy is enforced<br>(VPCSC-enabled projects or projects listed in<br>`enforcedProjects`), This managed<br>organization policy constraint lets you specify<br>which fully qualified domain names (FQDNs)<br>are permitted when adding a data store.|
|Override the organization policy for Custom<br>MCP data stores<br>(/gemini/enterprise/docs/connectors/custom-<br>mcp-server/override-constraint-for-custom-<br>mcp-data-stores)|This managed organization policy constraint<br>controls whether Custom Model Context<br>Protocol (MCP) data sources can be used.<br>Before you can create a Custom MCP data<br>store, you must turn off the`Disable custom`<br>`MCP server connector`<br>`for Gemini Enterprise`managed<br>constraint to enable Custom MCP.|
|VPC Service Controls|VPC Service Controls perimeters can protect<br>your project. For more information, see<br>Use VPC<br>Service Controls<br>(/gemini/enterprise/docs/use-vpc-service-<br>controls)<br>.|
||Enforcement of this constraint also depends on<br>whether your project is protected by a VPC<br>Service Controls (VPCSC) perimeter. For more<br>information, see<br>VPCSC interaction and<br>enforcement<br>(#vpcs-interaction-and-enforcement).|

#### VPCSC interaction and enforcement

The enforcement behavior of this constraint depends on your project's VPCSC state and whether it's included in the organization policy constraint's `enforcedProjects` parameter, as summarized in the following table: 

|VPCSC<br>state|Project included in<br>`enforcedProjects`|`allowedEgressFqdns`<br>enforcement|`allowedDataSources`<br>enforcement|
|---|---|---|---|
|Enabled|Yes|Provisioning is blocked if the<br>required domains aren't listed.|Provisioning is blocked if the<br>data source isn't listed.|
|Enabled|No|Provisioning is blocked if the<br>required domains aren't listed.|Provisioning is blocked if the<br>data source isn't listed.|
|Not<br>enabled|Yes|Provisioning is blocked if the<br>required domains aren't listed.|Provisioning is blocked if the<br>data source isn't listed.|
|Not<br>enabled|No|Provisioning is allowed even if<br>domains aren't listed.|Provisioning is allowed even if<br>data source isn't listed.|

### Example scenarios

To understand how these policies interact, consider the following examples. 

<sup>Allow Google Drive with VPCSC protection</sup> 

You want to let users create a Google Drive data store. 

Setup 

The project is protected by a VPC Service Controls perimeter, and the VPCSC state is Enabled. 

Requirement 

To create the data store, you must add `google_drive` to the Restrict allowed data sources for data connectors policy. 

Why 

The system allows the connection and automatically permits the well-known FQDNs for Google Drive. You don't need to update the Restrict egress domains for data connectors policy. 

<sup>Allowing a Custom MCP Server with VPCSC protection</sup> 

You want to allow users to create a Custom MCP data store that connects to `api.cymbal.com`. 

Setup 

The project is protected by a VPC Service Controls perimeter (VPCSC state: Enabled). 

Requirement 

To create the data store and allow it to connect to `api.cymbal.com` , you must: 

1. Turn off the Disable custom MCP server connector for Gemini Enterprise managed constraint. 

2. Add `custom_mcp` to the Restrict allowed data sources for data connectors policy. 

3. Add `api.cymbal.com` to the Restrict egress domains for data connectors policy. 

Why 

When VPC Service Controls is enabled, policies are enforced automatically. Custom MCP requires that you explicitly allow FQDNs. 

<sup>Third-party data source (Jira) without VPCSC protection</sup> 

An organization wants to allow users to create a data store for a third-party data source, Jira, in a project that is not subject to enforcement. 

Setup 

The project is not protected by a VPC Service Controls perimeter and is not listed in `enforcedProjects` . 

Requirement 

No updates are required for the organization policies. 

Why 

Because standard enforcement is disabled, you don't need to explicitly allow the data source or its FQDNs. 

Last updated 2026-10-14 UTC.
