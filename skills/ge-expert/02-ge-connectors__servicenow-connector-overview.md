# Gemini Enterprise: connectors and data stores / ServiceNow connector: overview to Zendesk configuration
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 573-612, extracted 2026-10-18

Contains:
- ServiceNow connector: overview (pages 573-575) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow
- Set up a ServiceNow data store (pages 576-584) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/set-up-data-store
- ServiceNow configuration (pages 585-589) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config
- Slack connector: overview (pages 590-592) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack
- Set up a Slack data store (pages 593-598) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack/set-up-data-store
- Zendesk connector: overview (pages 599-601) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk
- Set up a Zendesk data store (pages 602-607) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/set-up-data-store
- Zendesk configuration (pages 608-612) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config

## ServiceNow connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow

The ServiceNow connector for Gemini Enterprise lets you search and perform actions (#supported-actions) on your data and records. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Connector types

Gemini Enterprise supports two connector types, letting you choose how you want to access your records: 

**Federated search** 

(/gemini/enterprise/docs/connectors/servicenow/third-party-config#obtain-auth-credauth-code) 

: Access your records in real-time directly from your ServiceNow app without data ingestion. This mode uses the Authorization Code grant flow, which requires a redirect-based process to obtain access tokens. 

**Data ingestion** 

(/gemini/enterprise/docs/connectors/servicenow/third-party-config#obtain-auth-cred-foringestion-connector) 

: Synchronize and index your records within a local data store for highperformance search. This mode uses Resource Owner Password Credentials (ROPC), utilizing direct credentials (username and password) to obtain secrets. 

Ensure your ServiceNow app registration is configured with the correct authentication flows based on your use case: 

- If configuring Actions, federated search, or both, configure the Authorization Code flow. 

- If configuring data ingestion only, configure the ROPC flow. 

- If configuring data ingestion along with Actions, you must support both the ROPC flow and the Authorization Code flow. 

### Supported ServiceNow versions

The ServiceNow connector supports ServiceNow API version v2 and later. 

### Supported actions

When the ServiceNow connector is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create incid|entCreate a new incident record in ServiceNow to report and track a service<br>interruption.|
|Update<br>incident|Update an existing incident in ServiceNow using its unique system ID.|

**Note:** Additional read-only actions are also available. 

### Limitations

This section outlines known issues and limitations that may affect your use of the ServiceNow data store. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing ServiceNow data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The ServiceNow data store is supported only in the `global` , `us` , and `eu` locations. 

### What's next

- To create and configure a connector with ServiceNow, see Set up a ServiceNow data store 

- (/gemini/enterprise/docs/connectors/servicenow/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a ServiceNow data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/set-up-data-store

This page describes how to create a data store and connect ServiceNow to Gemini Enterprise. 

### Before you begin

Before setting up your ServiceNow connection, ensure you have the following in place: 

- Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Locate the user account and click **Edit** . 

3. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

   - (https://cloud.google.com/gemini/enterprise/docs/access-control). 

ServiceNow OAuth registration 

(/gemini/enterprise/docs/connectors/servicenow/third-party-config#obtain-auth-cred): Register Gemini Enterprise as an OAuth 2.0 application in ServiceNow with **Broadly scoped** scope restriction. 

Set up ServiceNow account 

- (/gemini/enterprise/docs/connectors/servicenow/third-party-config#create-account) and obtain authentication credentials 

- (/gemini/enterprise/docs/connectors/servicenow/third-party-config#obtain-auth-cred). 

Set up administrator role 

- (/gemini/enterprise/docs/connectors/servicenow/third-party-config#admin-roles) and use administrator account to set the required user roles and permissions 

- (/gemini/enterprise/docs/servicenow/third-party-config#user-roles-permissions). 

Set up a Google Cloud project 

- (https://cloud.google.com/resource-manager/docs/creating-managing-projects) with an administrator account capable of managing organization-level configurations, ensuring the organization can set up a workforce pool. Make sure your organization is set up to manage a workforce pool. 

- To enable keyword search capabilities, ensure that "table indexing" is enabled on your ServiceNow instance. For information, see Configure table for indexing and searching 

(https://www.servicenow.com/docs/bundle/zurich-platformadministration/page/administer/search-administration/task/configure-single-table-forindexing.html) 

### Create ServiceNow data store

To create a ServiceNow data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **ServiceNow** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Connector mode** section, select **Data ingestion** or **Federated search** as the connection mode. 

   - b. Click **Continue** . 

   - c. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

- If you selected **Federated search** , enter the following details: 

   - **Instance URL** : The base URL of your ServiceNow instance. 

   - **Client ID** : The OAuth client ID for your application. 

   - **Client Secret** : The OAuth client secret for your application. 

   - **Auth URI** : The authorization endpoint URL provided by ServiceNow. 

   - **Token URI** : The token endpoint URL provided by ServiceNow. 

   - **User ID** : The ServiceNow user ID. 

   - **Password** : The password for the ServiceNow user. 

- If you selected **Data ingestion** , enter the following details: 

   - **Instance URL** : The base URL of your ServiceNow instance. 

   - **Client ID** : The OAuth client ID for your application. 

   - **Client Secret** : The OAuth client secret for your application. 

   - **User ID** : The ServiceNow user ID. 

**Password** : The password for the ServiceNow user. 

For more information about credentials, see ServiceNow configuration 

(/gemini/enterprise/docs/connectors/servicenow/third-party-config). 

      - If you selected **Federated Search** , click **Login** and complete the ServiceNow sign-in. 

- d. Click **Continue** . 

- e. If you selected **Federated search** , do the following: 

   - i. In the **Destinations** section: 

         - i. Enter **Instance URL** of your ServiceNow site. 

ii. Enter **Base URL** of your ServiceNow site. 

- ii. Click **Continue** . 

   - iii. Optional: In the **Advanced options** section, to expose or hide ServiceNow system tables, select the **Include system tables** checkbox. 

   - iv. Click **Continue** . 

- f. If you selected **Data ingestion** , in the **Advanced options** section do the following: 

   - i. Optional: In the **URL suffix** field, enter the URL suffix from the knowledge or catalog portal link. 

   - ii. Optional: To allow a set of static IP addresses in your system, select the **Enable Static IP Addresses** checkbox. For more information, see Configure static IP egress 

      - (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

   - iii. Optional: In the **Max QPS** field, enter the maximum queries per second to apply a rate limit on the queries that the connector sends to the ServiceNow instance. 

   - iv. Click **Continue** . 

- g. In the **Entities to search** (if you selected **Federated search** ) or **Entities to sync** (if you selected **Data ingestion** ) section select all the required entities. 

      - If you selected **Federated search** , proceed to the next step. 

      - If you selected **Data ingestion** , continue with the following steps: 

         - i. **Optional:** To sync specific projects, do the following: 

            - i. Click **Filter** . 

            - ii. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included in the index, select the **Include to the index** checkbox. 

            - iii. Enter the keys. Press enter after each key. 

            - iv. Click **Save** . 

         - ii. To configure the sync schedule, do the following: 

i. In the **Sync frequency** list, select the sync frequency. 

   - To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options** . 

- ii. In the **Incremental sync frequency** list, select the incremental sync frequency. For more information, see Sync schedules 

(https://cloud.google.com/gemini/enterprise/docs/introduction-toconnectors-and-data-stores#sync-schedules) 

7. Click **Continue** . 

8. In the **Actions** section: 

   - If you selected **Federated search** , from **Select ServiceNow actions to enable** , select the actions from the category to enable them for the connector. 

   - If you selected **Data ingestion** : 

      - a. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

      - b. Provide the following authentication details as necessary: 

         - **Instance URL** : The base URL of your ServiceNow instance. 

         - **Client ID** : The OAuth client ID for your application. 

         - **Client Secret** : The OAuth client secret for your application. 

         - **Auth URI** : The authorization endpoint URL provided by ServiceNow. 

         - **Token URI** : The token endpoint URL provided by ServiceNow. 

         - **User ID** : The ServiceNow user ID. 

         - **Password** : The password for the ServiceNow user. 

For more information about credentials, see ServiceNow configuration (/gemini/enterprise/docs/servicenow/third-party-config). 

- c. Click **Login** and sign-in to ServiceNow to verify your account. 

d. Click **Continue** . 

- e. Optional: In the **Advanced options** section, to expose or hide ServiceNow system tables, select the **Include system tables** checkbox. 

- f. Click **Continue** . 

- g. In the **Destinations** section: 

   - i. Optional: Enter **Instance URL** of your ServiceNow site. 

   - ii. Optional: Enter **Base URL** of your ServiceNow site. 

- h. Click **Continue** . 

- i. From **Select ServiceNow actions to enable** , select the actions from the category to enable them for the connector. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions 

(/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

(/gemini/enterprise/docs/manage-actions). 

9. Click **Continue** . 

10. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Your data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a single-region key for third-party connectors 

(/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

Select **Google-managed encryption key** or **Cloud KMS key** . 

If you selected **Cloud KMS key** : 

In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

11. Click **Continue** . 

12. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

13. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the ServiceNow connector is ready to be used. 

For an ingestion connector created with ServiceNow, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the ServiceNow data store 

(/gemini/enterprise/docs/connect-existing-data-store), and authorize 

(/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access ServiceNow before executing any queries. 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize ServiceNow and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the ServiceNow API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (ServiceNow API). These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to ServiceNow. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the ServiceNow API. 

### What's next

- To provide a user interface for querying your ServiceNow data, create an app (/gemini/enterprise/docs/create-app) and connect it to the ServiceNow data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions, see Manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## ServiceNow configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/servicenow/third-party-config

This page describes how to set up and configure a third-party configuration before creating the ServiceNow data store. 

### Prerequisites

To complete this setup, you need a **[ServiceNow site for _Personal Developer Instance (PDI)]** . This instance provides a dedicated environment to configure OAuth and permissions. 

- **Instance URL** : You must have a specific URL for your environment. For example, `https://your-instance.service-now.com` 

- **Credentials** : You must have administrator access to the instance. 

### Create ServiceNow account

If you don't already have an account or a PDI, follow these steps to set them up: 

1. To create a ServiceNow account in Developer Site: 

   - a. Go to the ServiceNow developer portal (https://developer.servicenow.com) and click **Sign in** . 

   - b. Select **New user? Get a ServiceNow ID** . 

   - c. Enter your information, and click **Sign Up** . Use your email and verify your account using the confirmation link sent to your email inbox. 

2. To create a Personal Developer Instance (PDI): 

   - a. **Sign in** to the ServiceNow developer portal account using your account credentials. 

   - b. After signing in, follow the portal prompts to **Request an instance** . After provisioning, a confirmation dialog states: "Your instance is ready!". 

- c. **Save your credentials** : When the instance is ready, the portal provides your **Instance URL, Admin username, and Admin password** . Save these for the next configuration steps. 

- d. To access your new environment, click the **Start Building** button on the Developer Site header. This opens your instance in a new tab. 

**Note:** Upon initial login with full administrative privileges, go to User Administration > Users to change the default admin password for security. 

_Developer instance_ 

### Configuration setup

To connect Gemini Enterprise to ServiceNow, you must configure an OAuth 2.0 application in your ServiceNow instance. The configuration steps depend on whether you are using an **Ingestion connector** or a **Federated connector** . For more information about the differences, see Connector types 

(/gemini/enterprise/docs/connectors/servicenow#connector-types). 

To view the configuration steps for your connector, select it from the following menu: 

Federated connector 

#### Set up OAuth for federated connector

To perform federated search and Actions 

(/gemini/enterprise/docs/connectors/servicenow#supported-actions), you only need to set 

up the OAuth Authorization Code grant flow. This provides the client secret required for real-time discovery and task performance. 

To create OAuth credentials for a federated connector: 

1. Navigate to **All** > **System OAuth** > **Application registry** . 

2. Click **New** > **Inbound integration experience** > **New integration** . 

3. Enter the mandatory fields: 

   - a. **Integration name** : Enter a unique name for the OAuth credential, like Gemini Enterprise OAuth Actions. 

   - b. **Active** : Select the checkbox. 

   - c. **Grant type** : Select **OAuth authorization code** . 

   - d. **Redirect URL** : Enter 

      - `https://vertexaisearch.cloud.google.com/console/oauth/default_oauth. html,https://vertexaisearch.cloud.google.com/oauth-redirect` 

   - e. **Scope and API access policy** : Ensure the **Allow access only to APIs in selected scope** checkbox is unchecked. Also, don't select any **Auth scope** . Leaving this blank ensures that the integration is **Broadly scoped** . 

4. Click **Submit** to create the credential. 

5. After submission, click the record name to view the **Client ID** and unmask the **Client secret** . Save these for later use. 

**Note:** The secret must be alphanumeric. If the generated secret contains special characters, manually change it to an alphanumeric string before saving. 

Table API access requirements 

For the LLM to successfully fetch results, end users must have the system role (typically `snc_internal` or a custom REST role) that allows them to access the Table API endpoints. 

|Endpoint|ServiceNow<br>Table|Data Retrieved|
|---|---|---|
|`/api/now/table/incident`|Incident|Tickets, status updates, and resolution details.|
|`/api/now/table/sc_`<br>`catalog`|Catalog|Definitions and structures of available Service<br>Catalogs.|
|`/api/now/table/sc_cat_`<br>`item`|Catalog Item|Individual goods or services available for request.|
|`/api/now/table/sys_`<br>`attachment`|Attachment|Metadata for files attached to records (filenames,<br>sizes).|
|`/api/now/table/kb_`<br>`knowledge`|Knowledge|Published articles, procedures, and<br>troubleshooting guides.|

Security and data privacy: End-user authentication 

The ServiceNow connector uses end-user credentials to perform queries using the Table API. Using end-user credentials ensures that the search experience maintains a strict 1:1 security parity with the ServiceNow UI. 

Security model 

When a query is posted to the ServiceNow Table API, the connector executes it within the security context of the authenticated user: 

- **Identity parity** : Because the connector uses the user's credentials, the system treats the API request the same as a query in the ServiceNow global search bar. 

- **Inherited ACLs** : ServiceNow evaluates all Access Control Lists (ACLs) at the database level. If a user doesn't have read permission for a record, the Table API returns an empty result or a 403 error for that record. 

- **User criteria enforcement** : For Knowledge ( `kb_knowledge` ) and Catalog items ( `sc_cat_item` ), ServiceNow applies user criteria. The API automatically filters out items where the user doesn't meet the "Available For" requirements. 

Last updated 2026-10-16 UTC. 



## Slack connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack

The Slack connector for Gemini Enterprise lets you search and read your Slack conversations, files, and messages using natural language. You can also perform actions such as sending and scheduling messages. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported Slack versions

The Slack data store supports the latest cloud version of Slack. 

### Supported actions

When the Slack connector is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Send Slack message|Send a Slack message.|
|Schedule Slack message|Schedule a Slack message.|
|Create Slack canvas|Create a Slack canvas.|
|Send Slack message draft|Send a Slack message draft.|

**Notes** : 

- Additional read-only actions are also available. 

The maximum file size for file uploads and downloads in Gemini Enterprise is 90 MB. 

### Rate limits

Slack supports approximately 10 requests per minute, depending on the complexity of the query. 

### Limitations

The Slack data store for Gemini Enterprise has the following limitations: 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Slack data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Slack data store is supported only in the `global` , `us` , and `eu` locations. 

- You can search for files based on their content. However, search results can vary and are not always comprehensive of the entire file content. 

### What's next

- To create and configure a connector with Slack, see Set up a Slack data store (/gemini/enterprise/docs/slack/set-up-data-store). 

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## Set up a Slack data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/slack/set-up-data-store

This page describes how to create a data store and connect Slack to Gemini Enterprise. 

### Before you begin

Before setting up your Slack connection, ensure you have the following in place: 

- Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   2. Locate the user account and click **Edit** . 

   3. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

      - (https://cloud.google.com/gemini/enterprise/docs/access-control). 

- Verify you have access to the Slack workspace you need to connect to and are signed in to your Slack account. 

- Verify that you have a Slack plan (https://app.slack.com/plans/) that includes Slack AI search. 

- Coordinate with your organization's Slack administrator to ensure that end users can authorize their accounts without disruption. Share the official Slack Help Center: Manage app approval for your workspace 

(https://slack.com/intl/en-in/help/articles/222386767-Manage-app-approval-for-yourworkspace) 

documentation for step-by-step instructions on setting up one of the following deployment options: 

- **App Pre-Approval (Recommended):** If the **Require approved apps** setting is enabled in Slack, the administrator can pre-approve the Gemini 

Enterprise app 

(https://gerestrictedw-qhw2314.slack.com/marketplace/A099QQHCXKN-geminienterprise) 

within the Slack App Marketplace. Members can install and use preapproved apps immediately. See Slack Help: Pre-approve or restrict apps (https://slack.com/help/articles/222386767-Manage-app-approval-for-yourworkspace#pre-approve-or-restrict-apps) 

- **Request-on-Demand:** If the **Require approved apps** setting is enabled in Slack, the administrator can allow members to request apps that have not been pre-approved. Members can submit requests for administrative approval. See Slack Help: Allow members to request apps (https://slack.com/help/articles/222386767-Manage-app-approval-for-yourworkspace#allow-members-to-request- 

apps:%7E:text=manage%20app%20requests-,Allow%20members%20to%20reques t%20apps,-When%20app%20approval) 

- **Direct Installation:** If the **Require approved apps** setting is disabled in Slack, members can directly install and use the app without administrator intervention. See Slack Help: Manage app approval for your workspace 

(https://slack.com/intl/en-in/help/articles/222386767-Manage-app-approval-foryour-workspace) 

### Create Slack data store

To create a Slack data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Slack** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Entities to search** section, select the entities you want to search from the following: 

      - Conversation 

      - File 

      - Message 

   - b. Optional: In the **Slack Team ID** field, enter your Slack team ID to restrict users from connecting only to a specific Slack workspace. For more information, see Restrict the connector to a specifc Slack workspacei (optional) (#restrict-slack-workspace). 

7. Click **Continue** . 

8. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see Configure static IP egress (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

9. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Your data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a single-region key for third-party connectors 

      - (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

      - Select **Google-managed encryption key** or **Cloud KMS key** . 

      - If you selected **Cloud KMS key** : 

In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

10. Click **Continue** . 

11. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

12. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Slack connector is ready to be used. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Slack data store (/gemini/enterprise/docs/connect-existing-data-store), and authorize (/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Slack before executing any queries. 

### Restrict the connector to a specific Slack workspace (optional)

The **Slack Team ID** field is optional. Use it to restrict end users to a specific Slack workspace and prevent them from linking personal or unauthorized accounts. 

- **If you provide a Team ID** : During authorization, the connector verifies that the connecting account belongs to the specified workspace. If it doesn't, the connection is rejected. 

- **If you leave this field blank** : Users can connect to any workspace that their account has permission to access. 

**Note:** The ID always begins with the letter **`T`** (for example, **`T01234567`** ). 

To find the Team ID corresponding to a specific workspace, do one of the following: 

- **Web browser address bar:** Sign in to Slack in a web browser using your workspace URL (for example, `https://example.slack.com` ) . Once the page loads, look at the address bar: the URL has the format 

- `https://app.slack.com/client/T01234567/C01234567` , and the segment beginning with `T` is your Team ID. 

- **Admin dashboard:** Enterprise Grid administrators can locate a specific workspace's Team ID from the admin dashboard at admin.slack.com (https://admin.slack.com) under **Workspaces** . 

- **Slack API:** Retrieve the Team ID programmatically using Slack's `team.info` (https://api.slack.com/methods/team.info) API method. 

Copy the value and paste it into the **Slack Team ID** field to enforce the restriction. 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Slack and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Slack API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

Your query string is sent to the third-party search backend (Slack API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Slack. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Slack API. 

### What's next

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Zendesk connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

The Zendesk data store for Gemini Enterprise lets you search and perform actions on your Zendesk data. 

### Supported Zendesk versions

The Zendesk data store supports Zendesk version 24.0.9175. 

### Supported actions

When the Zendesk data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create ticket|Creates a new ticket.|
|Update ticket|Updates an existing ticket.|
|Create category|Creates a new category.|
|Update post|Updates an existing post.|
|Update article|Updates an existing article.|
|Merge tickets|Merges multiple tickets.|
|Add a comment to a ticket|Adds a comment to a ticket.|

### Required permissions

To enable Gemini Enterprise to perform federated search and actions using Zendesk, you need to configure the necessary permissions within your Zendesk instance. 

The following table details the required permissions based on the connection mode: 

|Connection mode|Scope|Purpose|
|---|---|---|
|Federated search|`read`,<br>`users:read`|Required to perform searching across Zendesk data.|
|Federated search and|`tickets:writ`|`e`Required to perform search, create, update, and|
|actions||merge tickets.|
||`hc:write`|Required to create category and update post.|

For information about how to configure these permissions, see Configure Zendesk permissions (/gemini/enterprise/docs/connectors/zendesk/zendesk-config). 

### Limitations

The Zendesk data store for Gemini Enterprise has the following limitations: 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Zendesk data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use 

actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

The Zendesk data store is supported only in the `global` , `us` , and `eu` locations. 

### What's next

To create and configure a data store with Zendesk, see Set up a Zendesk data store (/gemini/enterprise/docs/connectors/zendesk/set-up-data-store). 

Last updated 2026-10-15 UTC. 



## Set up a Zendesk data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/set-up-data-store

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

This page describes how to create a data store and connect Zendesk to Gemini Enterprise. 

### Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have configured your identity provider 

(/gemini/enterprise/docs/configure-identity-provider). 

Before you set up your Zendesk data store, ensure the following: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   - b. Locate the user account and click **Edit** . 

   - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

      - (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Create an OAuth client 

(/gemini/enterprise/docs/connectors/zendesk/zendesk-config#create-oauth-client) and obtain the following credentials: 

Client ID 

Client secret 

3. Configure the necessary permissions 

(/gemini/enterprise/docs/connectors/zendesk/zendesk-config#set-up-permissions) within Zendesk for the OAuth application. 

4. Ensure that token access is enabled 

   - (/gemini/enterprise/docs/connectors/zendesk/zendesk-config#enable-token-access) in the Zendesk API settings. 

#### Create the Zendesk data store

To create the Zendesk data store, perform the following steps: 

1. In the Google Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** , search for **Zendesk** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Authentication settings** section, provide the following details: * **Instance URI:** Enter the Zendesk instance URI (for example, `https://[subdomain].zendesk.com` ) . * **Client ID:** The unique identifier of the application registered in Zendesk. * **Client Secret:** The secret key generated during the OAuth 2.0 application registration process in Zendesk. 

For information on how to obtain the client ID and client secret, see Obtain client ID and client secret 

- (/gemini/enterprise/docs/connectors/zendesk/zendesk-config#create-oauth-client). 

For the permissions required to perform search, see Required permissions (/gemini/enterprise/docs/connectors/zendesk#set-up-permissions). 

- b. Click **Login** and complete the Zendesk sign-in. 

- c. Click **Continue** . 

- d. In the **Destinations** section: 

   - i. **Proxy Server** : Enter the hostname or IP address of a proxy to route HTTP traffic through, including the **Host** and **Port** . 

   - ii. **Zendesk Support URL** : Enter the instance URL, including `https://` , which is your Zendesk Support URL. 

   - iii. Click **Continue** . 

- e. Optional: In the **Advanced options** section: 

   - i. **Enable Static IP Addresses** : Registers a narrow set of static IP addresses to be added to your system's allowlist. Sync runs will fail until these IP addresses are in the allowlist. For more information, see Configure static IP egress 

      - (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

   - ii. **Max API Requests Per Minute** : The maximum number of API requests per minute to send to your Zendesk instance for each connector run. 

   - iii. Click **Continue** . 

- f. In the **Entities to search** section, select all the entities to search from the list. You must select at least one entity. 

**Note:** To avoid 404 errors for **`search articles`** and **`search community posts`** entities, ensure the Zendesk help center is enabled. For more information, see Enabling and activating your help center (https://support.zendesk.com/hc/en-us/articles/5702269234330-Enabling-andactivating-your-help-center) 

7. Click **Continue** . 

8. In the **Actions** section, for **Select Zendesk actions to enable** , choose the actions from the category to enable them for the data store. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

(/gemini/enterprise/docs/manage-actions). 

9. Click **Continue** . 

10. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Your data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a single-region key for third-party connectors 

      - (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

      - Select **Google-managed encryption key** or **Cloud KMS key** . 

      - If you selected **Cloud KMS key** : 

In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

11. Click **Continue** . 

12. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects 

(https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Zendesk connector is ready to be used. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Zendesk data store (/gemini/enterprise/docs/connect-existing-data-store) , and authorize (/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to Zendesk before executing any queries. 

For information on permissions required to perform search, see Required permissions (/gemini/enterprise/docs/connectors/zendesk#set-up-permissions). 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Zendesk and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Zendesk API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Zendesk API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Zendesk. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Zendesk API. 

### What's next

- To provide a user interface for querying your data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Zendesk data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions, see Manage actions 

- (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Zendesk configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/zendesk/zendesk-config

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up authentication and permissions before creating the Zendesk data store. 

### Enable token access

To allow the Zendesk to authenticate and interact with your Zendesk instance, you must enable token access. Follow these steps to enable token access: 

1. Navigate to your Zendesk instance and sign in with an administrator account. 

2. In the navigation menu, expand **Apps and integrations** , then select **API configuration** from **APIs** . 

3. Select the **Allow API token access** checkbox. 

4. Click **Save** . 

### Set up authentication and permissions

For secure integration using OAuth 2.0, you must register your application in Zendesk to obtain the necessary client ID and client secret. 

#### Create an OAuth client and obtain authentication credentials

To create an OAuth client in Zendesk and obtain the authentication credentials, follow these steps: 

1. Navigate to your Zendesk instance and sign in with an administrator account. 

**Note:** Your instance URL is in the format **`https://<var>yoursubdomain</var>.zendesk.com`** . 

2. Click the Zendesk Products icon, then select **Admin Center** . 

_Zendesk Admin Center_ 

3. In the navigation menu, expand **Apps and integrations** and select **OAuth clients** from **APIs** . 

4. Click **Add OAuth client** . 

5. Enter the following client details: 

   - **Name:** Enter a descriptive name for your application. 

   - Optional: **Description:** Enter a short description. 

   - Optional: **Company:** Enter your company name. 

   - Optional: **Logo:** Provide a logo, which appears on the consent screen. 

   - **Unique Identifier (Client ID):** Provide a unique name for your client. You can edit the initial suggestion, but it must be unique. 

   - **Client kind:** Select **Public** for applications running in a browser or on a mobile device, or **Confidential** for applications running on secure servers. 

   - **Redirect URLs (Required):** Enter `https://vertexaisearch.cloud.google.com/oauth-redirect` . This is the URL Zendesk redirects to after authorization, receiving the authorization code. 

6. Click **Save** to obtain the client secret. 

   - **Client ID:** The value from the **Unique Identifier** field. 

   - **Client secret:** A new **Secret** field appears. Copy this secret and save it immediately in a secure location. For security, the full secret is shown only once. If you lose it, you must regenerate it. 

_Generated client credentials_ 

7. Click **Save** again to finalize the changes. 

#### Set up permissions

To set up the required permissions, follow these steps: 

1. Navigate to your Zendesk instance and sign in with an administrator account. 

2. Click the Zendesk Products icon, then select **Admin Center** . 

3. In the navigation menu, expand **Apps and integrations** and select **OAuth Clients** from **Connections** . 

4. Click **Add client** . 

5. Enter the following client details: 

   - **Name** : Enter a descriptive name. This cannot be changed. 

   - **OAuth grant type** : Select **Authorization code** . 

   - **Client ID** : Enter the client ID obtained from the Create an OAuth client in Zendesk (#create-oauth-client) section. 

   - **Client Secret** : Enter the client secret value obtained from the Create an OAuth client in Zendesk (#create-oauth-client) section. 

   - **Authorize URL** : The authorization endpoint is typically in the format `https://<var>your-subdomain</var>.zendesk.com/oauth/authorize` . Replace `<var>your-subdomain</var>` with your actual Zendesk subdomain. 

   - **Token URL** : The token endpoint is typically in the format 

   - `https://<var>your-subdomain</var>.zendesk.com/oauth/token` . Replace `<var>your-subdomain</var>` with your actual Zendesk subdomain. 

_Add scopes_ 

**Scopes** : Enter the following scopes separated by spaces, based on your connection mode: 

|Connection mode|Scope|Purpose|
|---|---|---|
|Federated search|`read`,|Required to perform searching across Zendesk|
||`users:read`|data.|
|Federated search and|`tickets:wri`|`t`<br>Required to perform search, create, update, and|
|actions|`e`|merge tickets.|
||`hc:write`|Required to create category and update post.|

**Note:** Before you configure these details, ensure that token access (#enable-token-access) is enabled in Zendesk. 

6. Click **Save** . 

Last updated 2026-10-14 UTC.
