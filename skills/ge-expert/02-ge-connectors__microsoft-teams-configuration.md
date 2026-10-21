# Gemini Enterprise: connectors and data stores / Microsoft Teams configuration to Salesforce configuration
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 533-572, extracted 2026-10-18

Contains:
- Microsoft Teams configuration (pages 533-541) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config
- Notion connector: overview (pages 542-543) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion
- Set up a Notion data store (pages 544-548) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/data-store
- Notion configuration (pages 549-550) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/config
- Salesforce connector: overview (pages 551-552) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce
- Set up a Salesforce data store (pages 553-559) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store
- Salesforce configuration (pages 560-572) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration

## Microsoft Teams configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config

This page describes how to set up authentication and permissions before creating the Microsoft Teams data store. 

### Set up authentication and permissions

You must set up authentication and permissions in Microsoft 365, which is crucial to allow Gemini Enterprise to access Microsoft Teams data. 

#### Entra app registration for Microsoft Teams data store

You must set up a Microsoft Entra application registration to enable secure access to Microsoft Teams before you create the Gemini Enterprise data store. 

To register Gemini Enterprise as an OAuth 2.0 application in Microsoft Entra, do the following: 

1. Navigate to Microsoft Entra admin center (https://entra.microsoft.com). 

2. In the menu, expand the **Entra ID** section and select **App registrations** . 

3. On the **App registrations** page, select **New registration** . 

4. On the **Register an application** page, create an app registration by doing the following: 

   - a. In the **Name** section, enter a display name for the application. 

_Register an application page_ 

- b. In the **Supported account types** section, select **Accounts in the organizational directory only** . This option restricts access to users within your organization's Microsoft Entra tenant, which is appropriate for an enterprise application. 

- c. In the **Redirect URI** section, select **Web** and enter the following URL as web callback URL (or redirect URL): 

```
https://vertexaisearch.cloud.google.com/oauth-redirect
```

- d. Click **Register** . Microsoft Entra creates your app and displays it on the **All applications** page. 

#### Create an OAuth 2.0 configuration

To create a connection using the OAuth 2.0 authentication method, obtain a client ID, client secret, and tenant ID from your Microsoft Entra application registration page by following these steps. 

Obtain client ID and client secret 

To obtain the client ID and secret for the app (#entra-app-registration), do the following: 

1. Navigate to Microsoft Entra admin center (https://entra.microsoft.com). 

2. In the menu, expand the **Entra ID** section and select **App registrations** . 

3. On the **App registrations** page, select **All applications** . 

4. Open the application you created. 

5. On the app page, select **Certificates & secrets** . 

6. Click **New client secret** . 

7. To obtain the client secret, do the following in the **Add a client secret** dialog: 

   - a. Enter a description for the secret. 

_Add a client secret dialog_ 

- b. Select an expiry duration. It's recommended to select the default value. 

c. Click **Add** . 

   - d. Copy the client secret from the **Value** column. 

8. To obtain the client ID, do the following: 

a. On the app page, select **Overview** . 

b. Copy the **Application (client) ID** . 

Obtain tenant ID 

Your tenant ID can be found in the **Tenant ID** box on the overview page (https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView) in the Microsoft Entra admin center. 

_Get the tenant ID_ 

#### Configure the Microsoft Graph permissions

To configure the required Microsoft Graph permissions for the app (#entra-app-registration), do the following: 

1. Navigate to Microsoft Entra admin center (https://entra.microsoft.com). 

2. In the navigation menu, expand the **Entra ID** section and select **App registrations** . 

3. On the **App registrations** page, select **All applications** . 

4. Open the application you created. 

5. On the app page, select **API permissions** . 

6. Click **Add a permission** . 

7. In the **Request API permissions** page, select **Microsoft Graph** , and select **Delegated permissions** . 

8. Search for and select the following permissions for your connection mode. Ensure that an administrator grants consent (#grant-admin-consent) for all the delegated permissions listed in the following table. Once consent is granted, the **Status** column displays **Granted** with a green tick mark (✓). 

|Connection<br>mode|Permission|Permission<br>type|Purpose|
|---|---|---|---|
|Federated<br>search|`Channel.Read`<br>`Basic.All`|Delegated|Allows the app to read the names and<br>descriptions of channels.|
||`Channel`<br>`Member.Read.`<br>`All`|Delegated|Allows the app to read the members of<br>channels.|
||`Channel`<br>`Message.`<br>`Read.All`|Delegated|Allows the app to read user channel messages.|
||`Chat.Read`|Delegated|Allows the app to read all chats.|
||`Chat.Read`<br>`Basic`|Delegated|Allows the app to read basic properties of<br>chats.|
||`ChatMessage.`<br>`Read`|Delegated|Allows the app to read all one-to-one and group<br>chat messages.|
||`Group.Read.`<br>`All`|Delegated|Allows the app to read the Microsoft Purview<br>sensitivity labels assigned to a team's parent<br>Microsoft 365 group, which are used to apply<br>Sensitive Data Protection (redaction) to<br>Microsoft Teams content.|
||`Schedule.`<br>`Read.All`|Delegated|Allows the app to read schedules, schedule<br>groups, and shifts for teams.|
||`Team.Read`<br>`Basic.All`|Delegated|Allows the app to read the names and<br>description of teams.|
||`TeamMember.`<br>`Read.All`|Delegated|Allows the app to read the members of teams.|
||`User.Read.`<br>`All`|Delegated|Allows the app to read all users' full profiles.|

|Connection<br>mode|Permission|Permission<br>type|Purpose|
|---|---|---|---|
|Federated<br>search and<br>actions|`Channel.`<br>`Create`<br>`Channel.Read`<br>`Basic.All`|Delegated <br>Delegated|Allows the app to create channels in Microsoft<br>Teams. Required for the create channel action.<br> Allows the app to read the names and<br>descriptions of channels.|
||`Channel`<br>`Member.Read.`<br>`All`|Delegated|Allows the app to read the members of<br>channels.|
||`Channel`<br>`Member.Read`<br>`Write.All`|Delegated|Allows the app to add and remove members<br>from channels. Required for the add member to<br>channel action.|
||`Channel`<br>`Message.`<br>`Read.All`|Delegated|Allows the app to read user channel messages.|
||`Channel`<br>`Message.Read`<br>`Write`|Delegated|Allows the app to update channel messages.<br>Required for the update channel message<br>action.|
||`Channel`<br>`Message.Send`|Delegated|Allows the app to send messages in any<br>channel.|
||`Channel`<br>`Settings.`<br>`ReadWrite.`<br>`All`|Delegated|Allows the app to read and update the settings<br>of channels. Required for the update channel<br>action.|
||`Chat.Create`|Delegated|Allows the app to create new chats. Required<br>for the create chat action.|
||`Chat.Read`|Delegated|Allows the app to read all chats.|
||`Chat.Read`<br>`Basic`|Delegated|Allows the app to read basic properties of<br>chats.|
||`Chat.Read`<br>`Write`|Delegated|Allows the app to read and write one-to-one<br>and group chat threads, including chat<br>messages. Required for the update chat and<br>update chat message actions.|

|Connection<br>mode|Permission|Permission<br>type|Purpose|
|---|---|---|---|
||`ChatMessage.`<br>`Read`|Delegated|Allows the app to read all one-to-one and group<br>chat messages.|
||`ChatMessage.`<br>`Send`|Delegated|Allows the app to send chat messages.|
||`Group.Read.`<br>`All`|Delegated|Allows the app to read the Microsoft Purview<br>sensitivity labels assigned to a team's parent<br>Microsoft 365 group, which are used to apply<br>Sensitive Data Protection (redaction) to<br>Microsoft Teams content.|
||`Schedule.`<br>`Read.All`|Delegated|Allows the app to read schedules, schedule<br>groups, and shifts for teams.|
||`Schedule.`<br>`ReadWrite.`<br>`All`|Delegated|Allows the app to create and update schedules,<br>shifts, and time-off entries for teams. Required<br>for the create schedule, create time off entry,<br>and update time off entry actions.|
||`Team.Read`<br>`Basic.All`|Delegated|Allows the app to read the names and<br>description of teams.|
||`TeamMember.`<br>`Read.All`|Delegated|Allows the app to read the members of teams.|
||`User.Read.`<br>`All`|Delegated|Allows the app to read all users' full profiles.|

**Note:** If you only intend to use the data store for search and not to perform any actions that modify content in Microsoft Teams, you can limit the scope to the **`Read.All`** permissions. Other permissions are required for actions 

(/gemini/enterprise/docs/connectors/ms-teams#supported-actions) that involve updating content in Microsoft Teams. 

9. Click **Add Permissions** . 

#### Grant administrator consent for permissions

To grant administrator consent for permissions, do the following: 

1. Sign in to Microsoft Entra admin center (https://entra.microsoft.com) as a global or application administrator. 

2. In the navigation menu, expand the **Entra ID** section and select **App registrations** . 

3. On the **App registrations** page, select **All applications** . 

4. Open the application you created. 

5. On the app page, select **API permissions** . 

6. Click the **Grant admin consent for** button. 

_Grant admin consent_ 

7. Select **Yes** in the dialog to confirm the consent action. 

Last updated 2026-10-14 UTC. 



## Notion connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion

The Notion data store for Gemini Enterprise lets you access and perform actions on your Notion data. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported actions

When the Notion data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create comment|Creates a new comment on a Notion page or block.|
|Create database|Creates a new database in Notion.|
|Update database|Updates the attributes of a database in Notion.|
|Create page|Creates a new page in Notion.|
|Update page|Updates attributes of a Notion page.|

**Note:** Additional read-only actions are also available. 

### Required permissions

To enable Gemini Enterprise to perform federated search and actions using Notion, you need to configure the necessary permissions within your Notion instance. 

The following table details the required permissions based on the connection mode: 

|Connection mode|Scope|Purpose|
|---|---|---|
|Federated search|`Read content`|Required to perform searching across Notion<br>data.|
|Federated search and<br>actions|`Read content`|Required to perform searching across Notion<br>data.|
||`Insert content`|Required to perform creating comments in<br>Notion.|
||`Read comments`|Required to fetch and list existing comments.|
||`Insert`<br>`comments`|Required to create comments.|

### Limitations

The Notion data store is supported only in `Global` , `US` , and `EU` locations. 

### What's next

- To configure a Notion integration for connecting to Gemini Enterprise, see Notion configuration (/gemini/enterprise/docs/connectors/notion/config). 

Last updated 2026-10-14 UTC. 



## Set up a Notion data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/data-store

This page describes how to create a data store and connect Notion to Gemini Enterprise. 

**Note:** To enforce data source access control and to secure data in Gemini Enterprise, ensure that you have configured your identity provider 

(/gemini/enterprise/docs/configure-identity-provider). 

### Before you begin

Before you set up your Notion data store, do the following: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   - b. Locate the user account and click **Edit** . 

   - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

      - (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. In the Notion settings, create a Notion OAuth integration. Obtain the authentication credentials, and set the required permissions. For more information, see Notion confgurationi (/gemini/enterprise/docs/notion/config). 

### Create the Notion data store

To create a Notion data store, do the following: 

1. In the Google Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. On the **Select a data source** page, enter _Notion_ into the search field. The Notion card displays. 

6. Click **Select** . 

7. In the **Data** section, fill in the following fields: 

   - a. For the **Connector mode** field, select **Federated search** , and click **Continue** . 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions 

(https://cloud.google.com/products#product-launch-stages). 

- b. Under **Authentication settings** , enter the values that you copied when you created an integration in the Notion settings: 

   - For **Client ID** , enter the Notion integration's **OAuth Client ID** . 

   - For **Client Secret** , enter the Notion integration's **OAuth Client Secret** . 

For more information about creating a Notion integration, see Notion configuration (/gemini/enterprise/docs/connectors/notion/config). 

Click **Login** . 

- c. Click **Continue** . 

- d. In the **Entities to search** section, select the entity types that you want Gemini Enterprise to search. 

e. Click **Continue** . 

8. In the **Actions** section, for **Select Notion actions to enable** , choose the actions from the category to enable them for the data store. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

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

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Notion data store is ready to be used. 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Notion and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Notion API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

Your query string is sent to the third-party search backend (Notion API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Notion. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Notion API. 

### What's next

- To provide a user interface for querying your data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Notion data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Notion configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/notion/config

This page describes how to set up authentication and permissions before creating a Notion data store for use with Gemini Enterprise. 

### Set up authentication and permissions

To connect Notion to Gemini Enterprise, you must create a Notion OAuth integration. Notion integrations can be either _public_ or _internal_ . To connect Gemini Enterprise, you must create a public integration. 

**Note:** A public Notion integration isn't visible or accessible outside your organization unless you submit it for publishing. You don't need to publish your integration in order to connect Notion to Gemini Enterprise. 

#### Create a Notion integration

1. Navigate to the Notion Integrations dashboard 

   - (https://www.notion.so/profile/integrations). 

2. Click **New integration** . Fill in the following fields: 

      - a. For **Associated workspace** , select your Notion workspace. 

      - b. In the **Type** list, select **Public** . 

3. Fill in required organizational fields such as **Company name** , **Website** , and **Privacy policy** . 

4. In the **OAuth domain & URIs** section, enter the OAuth redirect URIs for Gemini Enterprise: 

      - a. In the **Redirect URIs** field, enter 

`https://vertexaisearch.cloud.google.com/console/oauth/default_oauth. html` , and press `Enter` . 

- b. Again, in the **Redirect URIs** field, enter 

   - `https://vertexaisearch.cloud.google.com/oauth-redirect` , and press 

5. Click **Save** . 

#### Configure permissions and get credentials

1. In the settings page for your new integration, under **Configuration** , copy the **OAuth Client ID** and **OAuth Client Secret** values. 

2. In the **Capabilities** section, under **Content Requests** , select the **Read content** capability. 

3. Click **Save changes** . 

You can now create a data store to connect Notion to Gemini Enterprise. For more information, see Set up a Notion data store 

(/gemini/enterprise/docs/connectors/notion/data-store). 

Last updated 2026-10-14 UTC. 



## Salesforce connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce

**Private preview:** Creating and using a data store using data ingestion is in private preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

The Salesforce data store for Gemini Enterprise lets you search and interact with Salesforce data. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported actions

When the Salesforce data store is enabled, you can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create case|Creates a case in Salesforce.|

### Limitations

- Enforcing a VPC Service Controls perimeter on existing Salesforce data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- When creating a new application or adding a data store to an existing application, it's recommended that you add a data store with actions belonging to a single connector type. For example, don't associate two Salesforce data stores with actions enabled to the same application. 

- The Salesforce data store is supported only in Global, US, and EU locations. 

### What's next

- To create and configure a data store with Salesforce, see Set up a Salesforce data store (/gemini/enterprise/docs/connectors/salesforce/set-up-data-store). 

Last updated 2026-10-15 UTC. 



## Set up a Salesforce data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/set-up-data-store

**Private preview:** Creating and using a data store using data ingestion is in private preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

This page describes how to create a data store and connect Salesforce to Gemini Enterprise. 

### Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have configured your identity provider (/gemini/enterprise/docs/configure-identity-provider). 

Before you set up your connection, do the following: 

Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Locate the user account and click **Edit** . 

3. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

(https://cloud.google.com/gemini/enterprise/docs/access-control). 

- Set up your Salesforce account and obtain authentication credentials (/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration#obtainauthentication-credentials) 

### Create Salesforce federated data store

To create a Salesforce data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Salesforce** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Authentication settings** section, configure authentication based on your chosen connection mode. For more information about obtaining authentication credentials, see Salesforce configuration 

      - (/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration). 

         - **Instance URL** : The base URL of your Salesforce instance. 

         - **Client ID** : The OAuth client ID for your application. 

         - **Client Secret** : The OAuth client secret for your application. 

         - Click **Login** and complete the Salesforce sign-in. 

   - b. Click **Continue** . 

- c. In the **Advanced options** section, if you want to use the Salesforce sandbox instance, select the **Use Sandbox** checkbox. 

- d. Click **Continue** . 

- e. In the **Entities to search** section, select at least one entity. 

**Note:** You must select at least one entity to create the Salesforce data store. However, the Salesforce data store will search across all entities in your Salesforce app regardless of your selection. 

7. Click **Continue** . 

8. If you selected **Federated search** , navigate to **Actions** and select the required actions to enable for the data store from the **Select Salesforce actions to enable** list. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

   - a. Click **Continue** . 

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

12. Click **Continue** . 

13. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Salesforce connector is ready to be used. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Salesforce data store 

(/gemini/enterprise/docs/connect-existing-data-store), and authorize 

(/gemini/enterprise/docs/connect-existing-data-store#user_authorization) the application to access Salesforce before executing any queries. 

For more information, see What's next (#whats-next). 

<sup>Create Salesforce data ingestion data store</sup> 

If you want to create a data ingestion data store, follow these steps. Otherwise, you can skip this section. 

To use the console to sync data from Salesforce to Gemini Enterprise, follow these steps: 

1. In the console, go to the **Gemini Enterprise** page. 

Go to Console (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Click **Create Data Store** . 

4. On the **Select a data source** page, scroll or search for **Salesforce V2** to connect your third-party source. 

5. In the **Authentications** section, select the authentication method and enter the authentication information. For more information about obtaining authentication credentials, see Configure Salesforce for data ingestion data store 

   - (/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration#expandable-1). 

6. In the **Destinations** section, select **Public** or **Private** . 

      - a. For the **Public** destination type, you are not required to create the setup for service attachment. In the **Login URL** field, enter your login URL to the Salesforce server. 

      - b. For the **Private** destination type, enter all the required information: 

         - i. **Service attachment** : Enter your service attachment. 

         - ii. **Base domain name** : Enter your base domain. 

         - iii. **Login URL** : Enter your login URL to the Salesforce server. 

7. Click **Continue** . 

8. In the **Entities to sync** section, do the following: 

      - a. Select the entities you want to sync. 

            - Optional: **URL field name** : Enter a column name to override the default entity URL with a custom URL from the Salesforce table. 

      - b. Optional: To add custom entities, click **Add entities manually** . The custom entity name must be in the following format **<var>custom_object_name</var>__c** . 

      - c. Select the **Sync frequency** for **Full sync** and the **Incremental sync frequency** for **Incremental data sync** . For more information, see Sync 

schedules 

(/gemini/enterprise/docs/introduction-to-connectors-and-data-stores#syncschedules) 

9. Click **Continue** . 

10. In the **Configure your data connector** section, do the following: 

   - a. Select a region for your data store. 

   - b. Enter a name for your data store. 

   - c. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

11. To check the status of your ingestion, go to the **Data Stores** page and click your data store name. The **Connector state** changes from **Creating** to **Running** when it starts synchronizing data. 

For more information, see What's next (#whats-next). 

### What's next

- To provide a user interface for querying your Salesforce data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Salesforce data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 



## Salesforce configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/salesforce/salesforce-configuration

**Private preview:** Creating and using a data store using data ingestion is in private preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

### Before you begin

Use either a Salesforce enterprise or a Salesforce developer edition. Trial accounts are not supported. 

### Configure Salesforce for federated data store

To configure Salesforce for a federated data store, you must obtain authentication credentials by using the OAuth 2.0 Web Server Flow authentication method. The following sections guide you through setting up the necessary components and obtaining these credentials. 

#### Create and configure an external client app

1. In your Salesforce app, click the setup icon, and select **Setup** . 

2. Enter **Apps** in the quick find box and select **App manager** . 

3. Select **New external client app** . 

4. Enter the required basic information ( **Name** , **API name** , and **Contact email** ). 

5. In the **API (Enable OAuth settings)** section, configure the following OAuth settings. For more information, see Enable OAuth Settings for API Integration (https://help.salesforce.com/s/articleView? 

id=xcloud.connected_app_create_api_integration.htm&type=5) 

- a. Select the **Enable OAuth** checkbox. 

- b. Enter the **Callback URL** as 

   - `https://vertexaisearch.cloud.google.com/oauth-redirect` . 

- c. In the **Selected OAuth scopes** section, add the **Manage user data via APIs (api)** , and **Perform requests at any time (refresh_token, offline_access)** scopes. For more information, see OAuth Tokens and Scopes 

(https://help.salesforce.com/s/articleView? language=en_US&id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5) 

   - d. In the **Flow enablement** section, select the following checkboxes: 

      - i. **Enable Authorization Code and Credentials flow** 

      - ii. **Require user credentials in the POST body for authorization code and credentials flow** 

   - e. In the **Security** section, select the following checkboxes: 

      - i. **Require secret for Web Server Flow** 

      - ii. **Require secret for Refresh Token Flow** 

6. Click **Create** . 

#### Pre-authorize external client app access

After creating the external client app, authorize specific users or permission sets to access it. 

1. In your Salesforce app, enter **External client app** in the quick find box and select **External client app manager** . 

2. Click the name of your external client app that you created. 

3. Select the **Policies** tab and click **Edit** . 

4. In the **OAuth policies** section: 

   - a. In the **Permitted users** field, select **Admin approved users are preauthorized** . 

   - b. In the **App Authorization** section, in the **Refresh token policy** field, select **Refresh token is valid until revoked** . 

5. In the **App policies** section, select the profiles or permission sets authorized for this connection. 

6. Click **Save** . 

7. Navigate to the **Settings > OAuth settings** , click **Consumer key and secret** , and copy and store the consumer key and consumer secret to be used as authentication credentials. 

#### Find your Salesforce base URL

1. In your Salesforce app, click the setup icon, and select **Setup** . 

2. In the quick find box, search for and select **My Domain** . 

3. From the **Current My Domain URL** field, copy and store the URL. This is the base URL of your Salesforce instance and is required as an authentication credential when you create a data store. 

#### Configure permissions

To verify that the user configuring the connector has the required minimum data fetching permissions, complete the following steps: 

1. In your Salesforce app, enter **Profiles** in the Quick Find box and select **Profiles** . 

2. Select the user profile running the connector. 

3. Navigate to the **Standard object permissions** section and verify the permissions. 

4. Verify that the selected user has access to the required permissions. This process must be repeated for each entity you intend to ingest. 

      - **Note:** Check whether the default access at the user's profile level is set to **Private** . When an entity's access is set to **Private** , your Google Cloud connector cannot access the required object and logs an error. 

5. To allow access to the object, create a permission set and share it with the user: 

   - a. Enter **Permission sets** in the Quick Find box and select **Permission sets** . 

   - b. Click **New** . 

   - c. Enter a name and save the permission set. 

   - d. Open the created permission set and navigate to the **Apps** section. 

   - e. Select **Object settings** . 

   - f. Select the **View all records** checkbox. 

   - g. In the **Field permissions** section, grant **Read** access to all fields you want to synchronize. 

   - h. Save the settings and navigate back. 

6. Enable system permissions: 

   - a. In the **System** section, select **System permissions** . 

   - b. Enable the **API enabled** permission. 

7. Assign the user to the permission set: 

   - a. Enter **Users** in the Quick find box and select **Users** . 

   - b. Select the user. 

   - c. In the **Permission set assignments** section, select **Edit assignments** . 

   - d. Add the recently created permission set to the **Enabled permission sets** section. 

For more information, see Data access in Salesforce 

(https://developer.salesforce.com/docs/atlas.en- 

us.salesforce_record_access_under_the_hood.meta/salesforce_record_access_under_the_hood/ uth_intro.htm) 

and Organization-Wide Sharing Defaults 

(https://trailhead.salesforce.com/content/learn/modules/lex_implementation_user_setup_mgmt /lex_implementation_user_setup_mgmt_configure_user_access-hoc) 

<sup>Configure Salesforce for data ingestion data store</sup> 

To configure Salesforce for a data ingestion data store, follow the steps in this section. 

#### Supported versions

The Salesforce V2 connector supports SOAP API version 30.0 or later. 

#### Generate a service attachment

To generate a service attachment, perform the following steps: 

- For **Public** endpoint: If the Salesforce data center **Destination type** is **Public** , you are not required to create the setup for service attachment. Instead, you can use your public URL in the **Domain URL** field of the Google Cloud console. 

For **Private** endpoint: 

1. Use PSC (/vpc/docs/private-service-connect) to enable connections from private instances to Google Cloud. 

2. Create a Virtual Private Cloud network and the required subnets. 

3. Create a Virtual Machine (VM) instance and install the backend service. 

4. Optional: Set up a health check 

   - (/load-balancing/docs/internal#health-checking) probe to monitor backend health. 

5. Add a load balancer to route traffic to the VM or backend. 

6. Define firewall rules to allow traffic between the PSC endpoint and the backend. 

7. Publish the endpoint (/vpc/docs/configure-private-service-connect-producer) by creating a PSC service attachment. 

**Note:** Creating a PSC setup is not mandatory for VPC-SC enabled projects. 

#### Generate authentication credentials

Data ingestion data stores can use any of the following supported authentication types: 

OAuth 2.0 - Client credentials (#set-up-oauth-client-credentials) 

- OAuth 2.0 - JWT bearer (#set-up-jwt-bearer-authentication) 

Username and password (#set-up-username-and-password-authentication) 

**Note:** If you are using OAuth authentication, you must install the external client app in your Salesforce account after creating the connection. See Install the OAuth connected app (#post-setup). 

#### Set up for OAuth 2.0 - Client credentials authentication

You must set up Gemini Enterprise as an external client app (connected app (https://help.salesforce.com/s/articleView?id=xcloud.connected_app_create.htm&type=5)) in Salesforce to obtain the following authentication information: 

- Consumer ID or client ID 

- Consumer secret or client key 

Create and configure an external client app 

1. In your Salesforce app, click the setup icon, and select **Setup** . 

2. Enter **Apps** in the quick find box and select **App manager** . 

3. Select **New external client app** . 

4. Enter the required basic information ( **Name** , **API name** , and **Contact email** ). 

5. In the **API (Enable OAuth settings)** section, configure the following OAuth settings. For more information, see Enable OAuth Settings for API Integration (https://help.salesforce.com/s/articleView? id=xcloud.connected_app_create_api_integration.htm&type=5) 

   - a. Select the **Enable OAuth** checkbox. 

   - b. Enter the **Callback URL** as 

      - `https://vertexaisearch.cloud.google.com/oauth-redirect` . 

   - c. In the **Selected OAuth scopes** section, add the **Full access (full)** , **Manage user data via APIs (api)** , and **Perform requests at any time (refresh_token, offline_access)** scopes. For more information, see OAuth Tokens and Scopes 

(https://help.salesforce.com/s/articleView? language=en_US&id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5) 

- d. In the **Flow enablement** section, select the **Enable client credentials flow** checkbox. 

6. Click **Create** . 

Pre-authorize external client app access 

After creating the external client app, authorize specific users or permission sets to access it. 

1. In your Salesforce app, enter **External client app** in the quick find box and select **External client app manager** . 

2. Click the name of your external client app that you created. 

3. Select the **Policies** tab and click **Edit** . 

4. In the **OAuth policies** section: 

      - a. In the **Permitted users** field, select **Admin approved users are preauthorized** . 

      - b. Under **OAuth flow and external client enhancement** , select **Enable client credentials flow** and enter the user's email ID. 

      - c. In the **Refresh token policy** field, select **Refresh token is valid until revoked** . 

   5. In the **App policies** section, select the profiles or permission sets authorized for this connection. 

   6. Click **Save** . 

   7. Navigate to the **Settings > OAuth settings** , click **Consumer key and secret** , and copy and store the consumer key and consumer secret to be used as authentication credentials. 

- Configure permissions 

To verify that the user configuring the connector has the required minimum data fetching permissions, complete the following steps: 

1. In your Salesforce app, enter **Profiles** in the Quick Find box and select **Profiles** . 

2. Select the user profile running the connector. 

3. Navigate to the **Standard object permissions** section and verify the permissions. 

4. Verify that the selected user has access to the required permissions. This process must be repeated for each entity you intend to ingest. 

**Note:** Check whether the default access at the user's profile level is set to **Private** . When an entity's access is set to **Private** , your Google Cloud connector cannot access the required object and logs an error. 

5. To allow access to the object, create a permission set and share it with the user: 

   - a. Enter **Permission sets** in the Quick Find box and select **Permission sets** . 

   - b. Click **New** . 

   - c. Enter a name and save the permission set. 

   - d. Open the created permission set and navigate to the **Apps** section. 

   - e. Select **Object settings** . 

   - f. Select the **View all records** checkbox. 

   - g. In the **Field permissions** section, grant **Read** access to all fields you want to synchronize. 

   - h. Save the settings and navigate back. 

6. Enable system permissions: 

   - a. In the **System** section, select **System permissions** . 

   - b. Enable the following minimum permissions: 

      - **API enabled** 

      - **View all users** 

      - **View roles and role hierarchy** 

      - **View setup and configuration** 

7. Assign the user to the permission set: 

   - a. Enter **Users** in the Quick find box and select **Users** . 

   - b. Select the user. 

   - c. In the **Permission set assignments** section, select **Edit assignments** . 

   - d. Add the recently created permission set to the **Enabled permission sets** section. 

For more information, see Data access in Salesforce 

(https://developer.salesforce.com/docs/atlas.en- 

us.salesforce_record_access_under_the_hood.meta/salesforce_record_access_under_the_hood/ uth_intro.htm) 

and Organization-Wide Sharing Defaults 

(https://trailhead.salesforce.com/content/learn/modules/lex_implementation_user_setup_mgmt /lex_implementation_user_setup_mgmt_configure_user_access-hoc) 

#### Set up for OAuth 2.0 - JWT bearer authentication

You must set up Gemini Enterprise as an external client app (connected app) in Salesforce to obtain the following authentication information: 

Customer key 

Public key 

Username 

Generate private key and public certificate 

1. Generate a 2048-bit RSA private key by executing the following command: **openssl genrsa -out server.key 2048** 

This command creates a file named **server.key** , which contains your private key. Keep this file secure and confidential. 

2. Generate a self-signed public certificate by executing the following command: **openssl req -new -x509 -sha256 -days 3650 -key server.key -out server.crt** 

This command generates a file named **server.crt** , which is your public certificate. You can upload this certificate to Salesforce during the external client app (connected app) configuration. 

Create and configure external client app 

1. In your Salesforce app, click the setup icon, and then select **Setup** . 

2. Enter **Apps** in the quick find box and select **App manager** . 

3. Select **New external client app** . 

4. Enter the required basic information for your external client app (connected app), such as the **External client app name** , **API name** , and **Contact email** . 

5. In the **API (Enable OAuth settings)** section, configure the following OAuth settings. For more information, see Enable OAuth Settings for API Integration (https://help.salesforce.com/s/articleView? 

id=xcloud.connected_app_create_api_integration.htm&type=5) 

- a. Select the **Enable OAuth** checkbox. 

- b. Enter the **Callback URL** as 

`https://vertexaisearch.cloud.google.com/oauth-redirect` . 

- c. In the **Selected OAuth scopes** section, add **Full access (full)** , **Manage user data via APIs (api)** , and **Perform requests at any time (refresh_token, offline_access)** . For more information, see OAuth Tokens and Scopes 

(https://help.salesforce.com/s/articleView? 

id=xcloud.remoteaccess_oauth_tokens_scopes.htm&type=5) 

- d. In the Flow enablement section: 

   - i. Select **Enable JWT bearer flow** . 

   - ii. Upload the **server.crt** generated in the Generate private key and public certificate (#generate-private-key-cert) section. 

Get login URL 

To get the login URL for your Salesforce instance, do the following: 

1. In your Salesforce app, enter **My domain** in the quick find box and select **My domain** . 

2. Copy the domain ending in **my.salesforce.com** . 

3. Add **https://** to the beginning of the copied domain. This is the instance URL that you need to create the Salesforce connector in Gemini Enterprise. The instance URL must be in the following format: **https://DOMAIN_NAME.my.salesforce.com** . 

#### Install the OAuth connected app

You must install the external client app that you created. Navigate to the **Connected Apps OAuth Usage** page in your Salesforce account and install the app. For more information, see Connected App Usage Restrictions Change (https://help.salesforce.com/s/articleView?id=005132365&type=1). 

#### Set up for username and password authentication

For username and password authentication, use an existing security token, or reset the security token to receive a new one in your registered email. 

To reset your security token: 

1. In your Salesforce app, click your profile icon and select **Settings** . 

_Settings_ 

2. Navigate to **Reset my security token** and click **Reset security token** . 

<!-- Start of picture text -->
Reset security token<br><!-- End of picture text -->

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC.
