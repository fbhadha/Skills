# Gemini Enterprise: connectors and data stores / View data store sync activity and set up alerts to Set up a Confluence Cloud data store
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 243-278, extracted 2026-10-18

Contains:
- View data store sync activity and set up alerts (pages 243-248) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-periodic-data-alerts
- Configure static IP egress (pages 249-251) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress
- Box connector: overview (pages 252-253) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box
- Set up a Box data store (pages 254-258) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box/set-up-data-store
- Confluence Cloud connector: overview (pages 259-265) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud
- Set up a Confluence Cloud data store (pages 266-278) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/set-up-data-store

## View data store sync activity and set up alerts

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-periodic-data-alerts

This page describes how to view the status, activity logs, and sync activity of a third-party data store, and how to configure alerts for the data store. 

### View data store details and status

After connecting your third-party data source to Gemini Enterprise by creating a data store, you can view the status of the data store by going to the **Data stores** page and clicking the data store name. 

_The data store console_ 

#### View data store states

The **Connector state** field shows the status of the data store. See the following table for information about possible data store states. 

|State|Description|
|---|---|
|Creating|The data store is being created.|
|Creating (with<br>errors)|The data store is being created, but some errors have occurred.|
|Initialization<br>failed|The data store failed to be created.|
|[Action required]|User actions that must be completed before the data store can start syncing<br>data.|
|Updating|The data store is being updated.|
|Failed during<br>setup|The data store encountered some errors during setup.|
|Failed during sync|The data store encountered some errors during sync.|
|Authorization<br>issues|The data store failed with authorization related errors.|
|Quota issues|The data store failed with quota related errors.|
|Failed|The data sync run failed.|
|Running|The data sync run is in progress.|
|Running (with<br>errors)|The data sync run is in progress, but some errors have occurred (possibly<br>including fatal errors).|
|Warning|The data store's latest sync run encountered fatal errors.|
|Active|The data store was successfully created and is awaiting the next sync run.<br>The last sync run encountered no fatal errors.|
|Paused|The data sync run is paused.|
|Paused (with<br>errors)|The data sync run is paused, and some errors have occurred.|

#### View data store sync activity

In the **Data Ingestion Activity** tab, you can see the data store's latest sync activity. Each sync run is listed, with the following fields: 

- **Connector run** : the date and time of the sync run. 

- **Status** : the status of the sync run. 

- **Last update time** : the date and time of the last change in the sync run. 

- **Sync type** : the type of sync ( **Full** or **Incremental** ). 

- **Items succeeded (%)** : the percentage of entities that were successfully synced. 

- **Items failed** : the number of entities that failed to sync. 

- **Details** : More information about the sync run. If there are more details available, you can click to expand the field and view them. 

For information about the possible values of the **Status** field for a sync run, see the following table. 

|Status|Description|
|---|---|
|Running|The data sync is ongoing. At least one entity is still being synced.|
|Running with<br>errors|The data sync is ongoing. At least one entity is still being synced. Sync for<br>some entities failed, or encountered nonfatal errors.|
|Succeeded|The data sync has completed successfully. All of the entities were<br>successfully synced.|
|Succeeded with<br>errors|The data sync has completed, but some entity sync runs failed or<br>encountered nonfatal errors.|
|Failed|All entities failed to sync.|
|Cancelled|The data sync was scheduled, but syncs for all entities have been cancelled.|
|Overrun|The data sync is ongoing, but has taken longer than expected and continues<br>to run at the time that the next run is scheduled.|

For each sync run in the table, you can expand the row by clicking the date and time under **Connector run** . This shows you the details of each specific entity type included in the sync run. For more information, see the following table. 

|Field|Description|
|---|---|
|Status|Succeeded: The entity sync completed, and at least 99% of the documents<br>are successfully indexed.|
||Succeeded with errors: The entity sync completed, but less than 99% of the<br>documents are successfully indexed.<br>Failed: The entity sync terminated with fatal failures.|
|Last update<br>time|The date and time of the last change in the sync run for this entity.|
|Sync type|The type of sync (Full or Incremental).|
|Items<br>Succeeded (%)|The percentage of items (documents) successfully indexed. This percentage<br>may change over time as the sync run progresses.|
|Items Failed|The number of items (documents) that failed to index.|
|Details / View<br>Details|This button opens up a side-panel that shows a link to view logs for this entity<br>sync run, as well as more details about the error.|

### View data store activity logs

To view activity logs for the data store, click **View logs** in the data store details page. 

_View logs for all data store sync activity_ 

This shows you all logs related to this data store, across all sync runs, including all entity sync runs. 

### Set up alerts for sync events

After connecting your third-party data source to Gemini Enterprise by creating a data store, you can enable alerts for predefined tasks. Alert notifications can be emailed to selected recipients. 

**Note:** You can't configure alerts for a federated search connector. 

#### Before you begin

To enable alerts for a data store, you need to have the following permissions or role assigned to you: 

|Permissions|`discoveryengine.googleapis.com/alertPolicies.get`|
|---|---|
||`discoveryengine.googleapis.com/dataConnectors.up`<br>`date`|
|Predefined role|`Discovery Engine User`|
||(/gemini/enterprise/docs/access-<br>control#discoveryengine.user)|

#### Enable alerts for a data source

To enable alerts for a specific data source: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data stores** . 

3. Click the name of the data store that you want the alerts configured. 

4. On the data store details page, ensure that you have enabled the **Full sync frequency** and the **Incremental sync frequency** . 

5. Click the **Alerts** tab and then click **Edit** . 

6. In the **Configure alerts** section, click the alert toggle to the on position. The following alerts are supported: 

|Alert Type|Description|
|---|---|
|Status:|The data store failed to connect or retrieve data from your data|
|Failed/Cancelled|source, or the sync run was cancelled.|
|Status: Succeeded|The data store successfully connected and retrieved data from your<br>data source.|

7. In the **Configure recipients** section, add the email addresses that must receive notifications for the enabled alerts. 

**Note:** Alert recipients are configured at the Google Cloud project level. If you add an email address to receive alert notifications for one data store, that email address also receives the alert notifications from the other data stores in your project. 

Last updated 2026-10-14 UTC. 



## Configure static IP egress

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress

Gemini Enterprise data stores send outbound requests to third-party systems from a dynamic range of Google IP addresses. If the third-party system you're connecting to requires IP allowlisting, you'll need the outbound traffic from the connector to originate from a fixed set of IP addresses. Many third-party connectors support this through a static IP egress option, that is available when creating the data store. 

When enabled, the data store routes all outbound requests to your third-party instance through a fixed, Google-managed set of IP addresses. You can then add those addresses to the allowlist on the source system. If static IP egress is not enabled, the data store continues to work using Google's dynamic egress ranges. 

This page describes how static IP egress works, how to enable it, and how to add the assigned IP addresses to the allowlist on your third-party system. 

### How static IP egress works

When you enable static IP egress on a data store: 

1. Gemini Enterprise assigns a fixed set of egress IP addresses to the data store at creation time. 

2. Post-authentication, all outbound calls from the data store to your third-party instance originate from that fixed set of IP addresses. 

3. The assigned IP addresses are visible on the data store's details page in the Google Cloud console. 

4. You add the assigned IP addresses to the allowlist on the third-party system. 

If static IP egress is _disabled_ , the connector uses Google's general dynamic egress IP ranges. 

### Supported data stores

Static IP egress is supported for most third-party data stores. 

The **Enable Static IP Addresses** checkbox appears in the data store creation flow whenever the selected data store supports the feature. If the checkbox is not displayed for a data store, that data store does not support static IP egress. 

### Enable static IP egress

You can only enable static IP egress when you create the data store. You cannot enable or disable static IP egress on an existing data store; to change the setting you must delete and recreate the data store. 

1. In the Google Cloud console, go to the **Gemini Enterprise** page and start the **Create data store** flow. For the list of thir-party data stores, see Connect a third-party data source (/gemini/enterprise/docs/connect-third-party-data-source). 

2. Select your third-party source and complete the **Authentication** step. 

3. In the **Advanced options** step of the data source configuration, select the **Enable Static IP Addresses** checkbox. 

4. Complete the remaining steps of the data store creation flow. 

After the data store is created, the assigned static IP addresses are surfaced on the data store's details page. See Retrieve the assigned static IP addresses 

(#retrieve-ips) for the exact location. 

### Retrieve the assigned static IP addresses

1. In the Google Cloud console, go to the **Gemini Enterprise** page and click **Data stores** . 

2. Click the name of the data store that you created. 

3. On the data store details page, locate the **Static IPs** section. The list of assigned egress IP addresses is displayed there. 

4. Copy the complete list of IP addresses. You need to allowlist all of them on the third-party system. 

### Limitations

- Static IP egress is configured per data store and cannot be modified after data store creation. 

- The assigned IP addresses are Google-managed and cannot be customerselected. 

- Availability of the feature for a specific data store is determined by whether the **Enable Static IP Addresses** checkbox appears in the create data store flow. 

Last updated 2026-10-14 UTC. 



## Box connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box

The Box data store for Gemini Enterprise lets you search your Box data and records. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported Box versions

The Box data store supports Box API version `2024.0` . 

### Limitations

The Box data store for Gemini Enterprise has the following limitations: 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Box data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Box data store is supported only in the `global` , `us` , and `eu` locations. 

- The Box federated data store uses Box APIs for real-time searching and does not index large volumes of data. This means it's ideal for searching up-to-date data. 

### Supported actions for Box

Box supports the tools exposed by Box as actions within the data store. For a list of supported tools, see the Box MCP tools documentation 

(https://docs.box.com/en/box-mcp/tools). 

### What's next

- To create and configure a data store with Box, see Set up a Box data store (/gemini/enterprise/docs/connectors/box/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Box data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/box/set-up-data-store

This page describes how to create a data store and connect Box to Gemini Enterprise. 

### Before you begin

Before you set up your Box connection, do the following: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

- b. Locate the user account and click **Edit** . 

- c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

(https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Configure the Box integration for Gemini Enterprise. For details, see Step 1: Configure Box integration 

(https://docs.box.com/en/box-mcp/configuring-box-mcp-server/gemini-enterprise#step1-configure-box-integration) 

in the Box documentation. 

### Create the Box data store

To create the Box data store, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Go to Gemini Enterprise (https://console.cloud.google.com/gen-app-builder/engines) 

2. Click **Data stores** in the navigation menu. 

3. Click **Create data store** . 

4. In the **Third-party connectors** section, select **Box** . 

**Note:** Box uses Google-managed OAuth. You don't need to create your own OAuth application or provide a client ID and client secret. You authorize the connector with your Box account when you enable connector in app. 

1. In the **Data** section: 

   - a. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see Configure static IP egress 

      - (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

   - b. Click **Continue** . 

   - c. In the **Entities to search** section, select the entities that you want Gemini Enterprise to search. For Box, select **Box MCP** . 

2. Click **Continue** . 

3. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data store. 

   - b. In the **Your data connector name** field, enter a name for your data store. 

   - c. Optional: In the **Tag** field, enter a stable identifier for this data store across versions. This value is immutable after you set it. 

   - d. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

         - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a single-region key for third-party connectors 

         - (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

Select **Google-managed encryption key** or **Cloud KMS key** . 

If you selected **Cloud KMS key** : 

In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

- e. Optional: In the **Sensitive Data Protection policy** section, attach an existing Sensitive Data Protection 

(https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protectionoverview) 

policy to inspect and de-identify data that Gemini Enterprise retrieves through this data store. If your organization doesn't require a Sensitive Data Protection policy, you can skip this step. 

4. Click **Create** . 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Box data store is ready to be used. 

After creating the data store, connect the data store you just created to an existing app or create a new app (/gemini/enterprise/docs/create-app) and connect (/gemini/enterprise/docs/connect-existing-data-store) it to the new app, and authorize (/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Box before executing any queries. 

### Enable actions

By default, all actions are turned off. When you connect Box, all of its tools are imported and displayed as actions in the Gemini Enterprise data store. To enable these actions for your users, follow these steps: 

1. Go to your Box data store. 

2. Click **Actions > Reload custom actions** to reauthenticate. 

**Note:** This action performs a **`tools/list`** call on the MCP server to retrieve available tools, which are then displayed on the screen. 

3. Select the actions to enable. 

4. Click **Enable actions** . 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Box and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Box API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Box API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Box. This rewritten query can incorporate information from your session's query history. As a result, 

### What's next

- To provide a user interface for querying your Box data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Box data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To view and manage the list of actions you enabled for the Box data store, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Confluence Cloud connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud

The Confluence Cloud data store for Gemini Enterprise lets you search and perform actions on your spaces, pages, and user information. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported Confluence Cloud versions

The Confluence Cloud data store supports Confluence REST API versions v1. 

### Supported actions

When the Confluence Cloud data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create page|Creates a new Confluence page in a specified space with content and a<br>title.|
|Update page|Updates the title or content of an existing Confluence page.|
|Create blog post|Creates a new Confluence blog post in a specified space with content and<br>a title.|
|Create space|Creates a new Confluence space with a specified name and key.|
|Download<br>attachment|Downloads an attachment from a Confluence page.|

Action Description 

Upload attachment Uploads an attachment to a Confluence page. 

**Notes** : 

- Additional read-only actions are also available. 

The maximum file size for file uploads and downloads in Gemini Enterprise is 200 MB. 

#### Required scopes

To enable Gemini Enterprise to perform search and data ingestion using the Confluence Cloud data store, you need the following scopes: 

|Usage<br>reason|Permission<br>Description|
|---|---|
|Data<br>ingestion|`read:content-`<br>`details:confluence`<br>Allows the data store to read content details in<br>Confluence.|
||`read:attachment:con`<br>`fluence`<br>Allows the data store to download and read attachments.|
||`read:comment:conflu`<br>`ence`<br>Allows the data store to read comments.|
||`read:page:confluenc`<br>`e`<br>Allows the data store to read pages.|
||`read:whiteboard:con`<br>`fluence`<br>Allows the data store to read whiteboards.|
||`read:space:confluen`<br>`ce`<br>Allows the data store to read spaces.|
||`read:group:confluen`<br>`ce`<br>Allows the data store to read groups.|
||`read:user:confluenc`<br>`e`<br>Allows the data store to read users.|
||`read:content.`<br>`metadata:confluence`<br>Allows the data store to read content metadata.|
||`read:configuration:`<br>`confluence`<br>Allows the data store to read configurations.|
|Federated<br>search|`search:confluence`<br>Allows the data store to perform search queries in<br>Confluence.|

|Usage<br>reason|Permission|Description|
|---|---|---|
|Actions|`write:page:confluen`<br>`ce`|Allows the data store to create and update pages in<br>Confluence.|
||`write:attachment:co`<br>`nfluence`|Allows the data store to upload attachments to Confluence<br>pages.|
||`write:blogpost:conf`<br>`luence`|Allows the data store to create and update Confluence<br>blog posts.|
||`write:space:conflue`<br>`nce`|Allows the data store to create and update Confluence<br>spaces.|
||`write:confluence-`<br>`space`|Allows the data store to manage Confluence space<br>information, including create, update, and delete<br>operations.|
||`write:confluence-`<br>`content`|Allows the data store to write content in Confluence.|
||`write:confluence-`<br>`file`|Allows the data store to upload attachments to<br>Confluence.|
||`read:attachment:con`<br>`fluence`|Allows the data store to download and read attachments.|
||`read:comment:conflu`<br>`ence`|Allows the data store to read comments.|
||`read:configuration:`<br>`confluence`|Allows the data store to read configurations.|
||`read:confluence-`<br>`content.all`|Allows the data store to read all Confluence content.|
||`read:confluence-`<br>`space.summary`|Allows the data store to read space summaries.|
||`read:content-`<br>`details:confluence`|Allows the data store to read content details in<br>Confluence.|
||`read:content.`<br>`metadata:confluence`|Allows the data store to read content metadata.|

|Usage<br>reason|Permission|Description|
|---|---|---|
||`read:group:confluen`<br>`ce`|Allows the data store to read groups.|
||`read:me`|Allows the data store to read current user information.|
||`read:page:confluenc`<br>`e`|Allows the data store to read pages.|
||`read:space:confluen`<br>`ce`|Allows the data store to read spaces.|
||`read:space-`<br>`details:confluence`|Allows the data store to read space details.|
||`read:task:confluenc`<br>`e`|Allows the data store to read tasks.|
||`read:user:confluenc`<br>`e`|Allows the data store to read users.|
||`search:confluence`|Allows the data store to perform search queries in<br>Confluence.|

For information on how to configure these scopes, see Enable OAuth 2.0 and configure scopes 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#enable-oauthscopes) 

### Rate limits for data ingestion

The Confluence Cloud data store supports a default rate limit of 20 queries per second (QPS) for data ingestion. These rate limits apply exclusively to the ingestion of data from the Confluence Cloud data store. 

### Limitations

This section outlines known issues and limitations that may affect your use of the Confluence Cloud data store. 

   - When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

   - Enforcing a VPC Service Controls perimeter on existing Confluence Cloud data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

   - The Confluence Cloud data store is supported only in the `global` , `us` , and `eu` locations. 

- The following are the limitations for the Confluence Cloud ingestion data store: 

   - The legacy user management model is not supported for integration with Confluence Cloud. Only the centralized user management model is supported. For more information, see Atlassian organization consolidation guide (https://support.atlassian.com/atlassian-cloud/kb/atlassian-organization-consolidationguide/) 

   - The appearance of the macros that you added on Confluence pages might differ from user to user based on their access permissions. 

   - The data store doesn't support incremental sync for the spaces entity. 

   - You can't use a Google Cloud service account to authenticate to Confluence Cloud. 

   - The data store doesn't include archived pages in a full sync operation, and those pages are indexed as deleted. 

   - The data store doesn't support spaces and entities shared using anonymous access, guest links, or public URLs. 

### What's next

To create and configure a data store with Confluence Cloud, see Set up a Confluence Cloud data store 

- (/gemini/enterprise/docs/connectors/confluence-cloud/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Confluence Cloud data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/set-up-data-store

This page describes how to create a data store and connect Confluence Cloud to Gemini Enterprise. 

### Before you begin

Ensure the following before you set up your Confluence Cloud federated connection: 

- Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   2. Locate the user account and click **Edit** . 

   3. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

      - (https://cloud.google.com/gemini/enterprise/docs/access-control). 

- To enforce data source access control and secure data in Google Gemini Enterprise, configure your identity provider 

- (/gemini/enterprise/docs/configure-identity-provider). 

- To set up the Confluence Cloud data store, you must use the new centralized Atlassian user management model. If you are using the original model, you need to migrate your user management before proceeding. For more information, see Site administrator role (https://support.atlassian.com/atlassian-cloud/kb/site-administrator-role-in-thecentralized-user-management-and-original-user-management-experiences/) 

Create an OAuth 2.0 app 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#create-anoauth-configuration) 

- , obtain the client ID and secret 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#obtain-client-idand-client-secret) 

- , and configure the minimum application permissions 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#configureminimum-application-permissions) 

with the consent of a Confluence Cloud administrator. 

Optional: To retrieve user email addresses from Confluence Cloud, even when settings restrict email visibility, install the User Identity Accessor for Confluence Cloud app 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#install-identityaccessor-app) 

with Confluence _Site administrator_ privileges, and then configure it (/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#configureidentity-accessor-app) 

to securely retrieve user email addresses. You might not need to install this app if email addresses are already publicly accessible. 

**Note:** Atlassian is updating user interface elements, and some elements mentioned in this documentation are being renamed (for example, **Products** is being renamed to **Apps** ). For more information, see Atlassian Administration terminology change from "products" to "apps" 

(https://community.atlassian.com/forums/Atlassian-Platform-articles/AtlassianAdministration-terminology-change-from-products-to/ba-p/2967398) 

### Create Confluence Cloud data store

To create a Confluence Cloud data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

   - (https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Confluence Cloud** , and click **Select** . 

6. In the **Data** section: 

      - a. In the **Connector mode** section, select **Data ingestion** or **Federated search** as the connection mode. 

      - b. Click **Continue** . 

      - c. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

         - If you selected **Data ingestion** : 

            - i. Select **OAuth 2.0 client credentials** or **API token** as the authentication method. 

               - If you select **OAuth 2.0 client credentials** , enter the following details: 

                  - **Client ID** : The identifier for your OAuth 2.0 app. 

                  - **Client secret** : The secret key associated with your OAuth 2.0 app. 

                  - **Instance URI** : The base URL of your Confluence Cloud instance ( For example, `https://yourdomain.atlassian.net` ). 

                  - **Instance ID** : A unique identifier for your Confluence Cloud instance. 

               - If you select **API token** , enter the following details: 

                  - **Instance URI** : The base URL of your Confluence Cloud instance ( For example, `https://yourdomain.atlassian.net` ). 

- **User account** : The Atlassian username associated with the API token. 

- **API token** : The API token generated from your Atlassian account. 

If you selected **Federated search** : 

- i. Enter the following details: 

   - **Client ID** : The identifier for your OAuth 2.0 app. 

   - **Client secret** : The secret key associated with your OAuth 2.0 app. 

   - **Instance URI** : The base URL of your Confluence Cloud instance ( For example, `https://yourdomain.atlassian.net` ). 

- ii. Click **Login** and complete the Atlassian sign-in. 

For more information about credentials, see Confluence Cloud configuration 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config). 

- d. Click **Continue** . 

- e. In the **Destinations** section, enter the URL for your Confluence Cloud endpoint. 

- f. Click **Continue** . 

- g. In the **Entities to sync** (if you selected **Data ingestion** ) or **Entities to search** (if you selected **Federated search** ) section: 

   - i. Select all the required entities. 

      - If you selected **Federated search** , proceed to the next step. 

      - If you selected **Data ingestion** , do the following: 

         - i. Optional: To sync specific projects, do the following: 

            - i. Click **Filter** . 

            - ii. To filter entities out of the index, select **Exclude from the index** , or to ensure that they are included in the 

index, select **Include in the index** . 

   - iii. Enter the space keys. Press **Enter** after each space key. The space key is the unique code in a Confluence space URL, found after `/spaces/` . (For example, in 

      - `https://company.atlassian.net/wiki/spaces/ABC/overview` , the space key is `ABC` . ) 

   - iv. Click **Save** . 

- ii. To configure the sync schedule, do the following: 

   - i. In the **Sync frequency** list, select the sync frequency. 

         - To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options** . 

   - ii. In the **Incremental sync frequency** list, select the incremental sync frequency. 

For more information, see Sync schedules 

(https://cloud.google.com/gemini/enterprise/docs/introduction-to-connectorsand-data-stores#sync-schedules) 

7. Click **Continue** . 

8. In the **Actions** section: 

If you selected **Federated search** : 

   - a. From **Select Confluence Cloud actions to enable** , select the actions from the category to enable them for the data store. 

- If you selected **Data ingestion** : 

   - a. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

   - b. Enter the following authentication details: 

      - **Client ID** : The identifier for your OAuth 2.0 app. 

      - **Client secret** : The secret key associated with your OAuth 2.0 app. 

- **Instance URI** : The base URL of your Confluence Cloud instance ( For example, `https://your-domain.atlassian.net` ). 

- **Instance ID** : A unique identifier for your Confluence Cloud instance. 

For more information about credentials, see Confluence Cloud configuration 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config). 

- c. Click **Login** and sign-in to Confluence Cloud to verify your account. 

- d. Click **Continue** . 

- e. In the **Destinations** section, enter the URL for your Confluence Cloud endpoint. 

- f. From **Select Confluence Cloud actions to enable** , select the actions from the category to enable them for the data store. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions 

(/gemini/enterprise/docs/manage-actions#add-actions). 

To view and manage the list of actions, see View and manage actions 

(/gemini/enterprise/docs/manage-actions). 

9. Click **Continue** . 

10. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see Configure static IP egress (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

11. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Your data connector name** field, enter a name for your connector. 

- c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

   - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a single-region key for third-party connectors 

   - (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

   - Select **Google-managed encryption key** or **Cloud KMS key** . 

   - If you selected **Cloud KMS key** : 

      - In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys (/gemini/enterprise/docs/cmek). 

12. Click **Continue** . 

13. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

14. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Confluence Cloud data store is ready to be used. 

For an ingestion data store created with Confluence Cloud, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Confluence Cloud data store 

(/gemini/enterprise/docs/connect-existing-data-store), and authorize 

(/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to access Confluence Cloud before executing any queries. 

### Enable real-time sync for data ingestion

**Preview — Real-time sync** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

Real-time sync only syncs document entities and doesn't sync data related to identity entities. The following table shows which document events are supported with real-time sync. 

|Confluence entities|Create|Update|Delete|Permission changes|
|---|---|---|---|---|
|Spaces|||||
|Pages|||||
|Blogs|||||
|Attachments|||||
|Comments|||||
|Whiteboards|||||

Enable real-time sync 20 minutes after creating the Confluence Cloud data store. 

To enable real-time sync for a Confluence data store, follow these steps: 

#### Generate a webhook URL

1. Navigate to the Gemini Enterprise page, and in the navigation menu, click **Data Stores** . 

2. Select a Confluence data store. 

3. Click **View/Edit** in the **Realtime sync** row. 

4. In the **View and edit realtime sync parameters** dialog, do the following: 

   - a. To turn on real-time sync, click the **Enable realtime sync** toggle. 

   - b. In the **Client secret** field, enter a placeholder value, such as `clientsecret` . 

   - c. Click **Save** . 

5. After the status of **Realtime sync** changes to `Running` , click **View/Edit** . 

6. In the **View and edit realtime sync parameters** dialog, do the following: 

   - a. Copy the **Webhook URL** . 

   - b. Click **Close** . 

#### Subscribe to events using the API

To receive real-time updates from Confluence, you must subscribe to specific events using a POST request. To make API calls, use the same administrator account used for setting up authentication and permissions in Confluence to create the data store. 

```
     curl -X POST \
INSTANCE_URL/wiki/rest/webhooks/1.0/webhook \
       -H "Content-Type: application/json" \
       -u "USERNAME:API_TOKEN" \
       -d '{
         "name": "SUBSCRIPTION_NAME",
         "url": "LISTENER_URL",
         "events": [
           "EVENT_TYPE_1",
           "EVENT_TYPE_2"
         ],
         "active": true
       }'
```

- _INSTANCE_URL_ : The base web address for your Atlassian Cloud site. 

- _USERNAME_ : The Atlassian Cloud username. 

- _API_TOKEN_ : The API token generated from your Atlassian account. For more information, see Set up an API token in Confluence 

- (/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#api-token) 

- _SUBSCRIPTION_NAME_ : A unique name for your event subscription. 

- _LISTENER_URL_ : The webhook URL copied from the Google Cloud console once Real-Time Sync (RTS) is enabled on your data store. 

- _EVENT_TYPE_ : The event types that you want to subscribe to. You can subscribe to create, update, and delete events for attachments, blog posts, pages, spaces, and comments. 

The user can subscribe to the following events: 

- `space_created` 

- `space_updated` 

- `page_created` 

- `page_updated` 

- `attachment_created` 

- `attachment_updated` 

- `comment_created` 

- `comment_updated` 

- `blog_created` 

- `blog_updated` 

**Note:** **`Whiteboard`** and **`trashed`** events are not supported. Create subscriptions only for entities already added to your data store to avoid ingesting unwanted data. 

<sup>Example command and result</sup> 

```
curl -X POST \
   https://cymbalgroup.atlassian.net/wiki/rest/webhooks/1.0/webhook \
   -H "Content-Type: application/json" \
   -u "admin1:######" \
   -d '{
     "name": "Cymbal_DCT",
     "events": [
       "attachment_created",
       "attachment_updated"
     ],
     "url": "https://rt-server-a-jx3m2-uw.a.run.app/webhook",
     "active": true
   }'
{
"name": "Cymbal_DCT",
"url": "https://cymbalgroup.atlassian.net/wiki/rest/webhooks/1.0/webhook",
"description": " Webhook for Cymbal DCT group to fetch attachments.",
"excludeBody": false,
"filters": {},
"events": [
   "attachment_created",
   "attachment_updated",
],
"enabled": true,
"self": https://rt-server-a-jx3m2-uw.a.run.app/webhook,
"lastUpdatedUser": "Cymb_389",
"lastUpdatedDisplayName": "Ariel",
"lastUpdated": 1752095647212
}
```

API error codes 

This table lists common API error codes users encounter when creating webhooks. 

|Error<br>class|Error<br>code|Error message|Troubleshooting|
|---|---|---|---|
|`403`|`FORBIDD`|Current user not permitted to use|Ensure a valid token from an|
||`EN`|Confluence.|administrator account and correct API<br>endpoint.|

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Confluence Cloud and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Atlassian API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Atlassian API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Confluence Cloud. This rewritten query can incorporate information from your session's query history. As 

a result, parts of your query history might also be included in the query sent to the Atlassian API. 

### What's next

- To provide a user interface for querying your Confluence Cloud data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Confluence Cloud data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC.
