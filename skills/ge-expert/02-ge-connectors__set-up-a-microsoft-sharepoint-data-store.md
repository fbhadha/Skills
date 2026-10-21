# Gemini Enterprise: connectors and data stores / Set up a Microsoft SharePoint data store to Set up a Microsoft Teams data store
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 495-532, extracted 2026-10-18

Contains:
- Set up a Microsoft SharePoint data store (pages 495-506) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store
- Add filters to a Microsoft SharePoint data store (pages 507-510) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store
- Microsoft SharePoint configuration (pages 511-520) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config
- Microsoft Teams connector: overview (pages 521-526) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams
- Set up a Microsoft Teams data store (pages 527-532) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/set-up-data-store

## Set up a Microsoft SharePoint data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store

This page describes how to create a data store and connect Microsoft SharePoint to Gemini Enterprise. 

### Before you begin

**Note:** To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider (/gemini/enterprise/docs/configure-identity-provider). 

Ensure the following before you set up your Microsoft SharePoint federated connection: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   - b. Locate the user account and click **Edit** . 

   - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Register Gemini Enterprise as an OAuth 2.0 application in Microsoft Entra ID (/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config) and obtain the following credentials (/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#obtain-client-idand-client-secret) : 

Client ID 

Client secret 

Tenant ID 

      - Instance URI 

3. Configure the Microsoft API permissions 

   - (/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#configure-apipermissions) 

with the consent of a Microsoft SharePoint admin. 

### Create Microsoft SharePoint data store

To create a Microsoft SharePoint data store, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Microsoft SharePoint** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Connector mode** section, select **Federated search** or **Data ingestion** as the connection mode. 

   - b. Click **Continue** . 

   - c. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

      - i. Provide the following authentication details as necessary: 

- **Client ID:** The unique identifier of the application registered in your organization's Microsoft Entra ID. 

- **Client secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID. 

- **Tenant ID:** The unique identifier for your organization in Microsoft Entra admin center. 

- **Instance URI** : The base URL for your Microsoft SharePoint instance (e.g., `https://{your-domain}.sharepoint.com` ). 

- **Microsoft SharePoint Environment Type:** Select the environment that hosts your Microsoft 365 tenant: 

   - Select **Standard** (the default) if you connect to standard commercial Microsoft 365 or Government Community Cloud (GCC). 

   - Select **US Government** if you connect to a Microsoft 365 US Government sovereign cloud (GCC High or DoD). 

For more information, see Obtain client credentials 

(/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#obtainclient-id-and-client-secret) 

**Note:** These settings apply only to Microsoft 365 US Government (sovereign cloud) customers. If you connect to a US Government cloud, use the matching combination; otherwise keep the defaults ( **Standard** and **Global** ): 

- **GCC** : Environment Type **Standard** , Cloud Environment **GCC** . 

- **GCC High** : Environment Type **US Government** , Cloud Environment **GCC High** . 

- **DoD** : Environment Type **US Government** , Cloud Environment **DoD** . 

If you selected **Data ingestion** with **Federated credentials** authentication method, copy the **Subject identifier** and use it to add federated credential for data ingestion 

(/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#addfed-credentials) 

- **Subject identifier:** The unique ID of the service account you plan to use. 

If you selected **Federated search** , click **Login** and complete the third-party sign-in. 

- d. Click **Continue** . 

- e. If you selected **Federated search** , the **Destinations** section appears. Enter the base URL for the site. 

f. Click **Continue** . 

- g. In the **Advanced options** section, select your **Microsoft 365 Cloud Environment** : 

   - If you connect to a Microsoft 365 US Government instance, select the option that matches it: **GCC** , **GCC High** , or **DoD** . 

   - Otherwise, keep the default, **Global** . 

- h. If you selected **Federated search** , in the **Advanced options** section, you can refine the scope of your searches and actions by specifying which Microsoft SharePoint sites or specific paths to include or exclude. You can only mutate or retrieve data within the included paths. Requests for out-of-scope data either fail or return no results. 

You can add filters to the data store using the Google Cloud console or API: 

ConsoleREST (#rest) (#console) 

Note: When entering multiple sites, separate each URL with a comma. You can also copy and paste a list of URLs directly from a CSV file. 

i. In the Site filter section: 

- Choose the filter type: **Include in search** or **Exclude from search** . 

In the **Site URL filter** field, enter the exact Microsoft SharePoint site URLs to filter, in the format `https://{your-tenant}.sharepoint.com/sites/{yoursite-name}` . 

**Note:** Enter the exact site URLs. Subpaths, folders, or document libraries are not supported in this specific field. 

ii. In the Path filter section: 

Choose the filter type: **Include in search** or **Exclude from search** . 

In the **Path filter** field, enter the full SharePoint paths. 

**Note:** This field supports subpaths, folders, and document libraries, in the format, `https://{yourtenant}.sharepoint.com/sites/{your-site-name}/{yourfolder-name}/` . Any content under the specified path will be filtered. 

For more details on filter types and adding filters, see Add filters to Microsoft SharePoint data store 

(/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store). 

7. Click **Continue** . 

   - a. In the **Entities to search** (if you selected **Federated search** ) or **Entities to sync** (if you selected **Data ingestion** ) section: 

      - i. Select all the required entities. 

      - ii. If you selected **Federated search** , proceed to the next step. 

iii. If you selected **Data ingestion** , continue with the following steps: 

i. Optional: To sync specific projects, do the following: 

i. Click **Filter** . 

- ii. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included 

in the index, select the **Include to the index** checkbox. 

iii. Enter the keys. Press enter after each key. 

   - iv. Click **Save** . 

- ii. To configure the sync schedule, do the following: 

   - i. In the **Sync frequency** list, select the sync frequency. 

      - To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options** . 

   - ii. In the **Incremental sync frequency** list, select the incremental sync frequency. For more information, see Sync schedules 

(https://cloud.google.com/gemini/enterprise/docs/introduction-toconnectors-and-data-stores#sync-schedules) 

8. Click **Continue** . 

9. In the **Actions** section: 

- a. If you selected **Federated search** : 

   - i. From **Select Microsoft SharePoint actions to enable** , select the actions from the category to enable them for the connector. 

- b. If you selected **Data ingestion** : 

   - i. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

      - i. Provide the following authentication details as necessary: 

         - **Client ID:** The unique identifier of the application registered in your organization's Microsoft Entra ID. 

         - **Client Secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID. 

         - **Tenant ID:** The unique identifier for your organization in Microsoft Entra admin center. 

- **Instance URI** : The base URL for your Microsoft SharePoint instance (e.g., `https://{your-domain}.sharepoint.com` ). 

For more information, see Obtain client credentials 

(/gemini/enterprise/docs/connectors/ms-sharepoint/third-partyconfig#obtain-client-id-and-client-secret) 

   - ii. Click **Continue** . 

   - iii. In the **Destinations** section, enter the base URL for the site. 

   - iv. Click **Continue** . 

   - v. From **Select Microsoft SharePoint actions to enable** , select the actions from the category to enable them for the connector. 

10. Click **Continue** . 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

(/gemini/enterprise/docs/manage-actions). 

**Warning:** 

   - **Default write actions:** When creating and configuring the data store, ensure that any default _write_ actions are explicitly disabled if you only intend to grant read access. Leaving write actions enabled without the corresponding write scopes in Microsoft Entra ID results in authentication and sync errors. 

11. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see Configure static IP egress (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

12. In the **Configuration** section: 

- a. From the **Multi-region** list, select the location for your data connector. 

- b. In the **Your data connector name** field, enter a name for your connector. 

- c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

   - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a single-region key for third-party connectors 

   - (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

   - Select **Google-managed encryption key** or **Cloud KMS key** . If you selected **Cloud KMS key** : 

      - In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys (/gemini/enterprise/docs/cmek). 

13. Click **Continue** . 

14. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

15. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Microsoft SharePoint connector is ready to be used. 

For an ingestion connector created with Microsoft SharePoint, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Microsoft SharePoint data store 

(/gemini/enterprise/docs/connect-existing-data-store), and authorize (/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Microsoft SharePoint before executing any queries. 

### Enable real-time sync for data ingestion

**Preview — Real-time sync** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

**Note:** Real-time sync is only available for the **Data ingestion** connection mode. 

Real-time sync only syncs document entities and doesn't sync data related to identity entities. The following table shows which document events are supported with real-time sync. 

|Microsoft SharePoint entities|Create|Update|Delete|Permission changes|
|---|---|---|---|---|
|Attachments|||||
|Comments|||||
|Events|||||
|Files|||||
|Pages|||||

To enable real-time sync for your data store, follow these steps. 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Click the name of the Microsoft SharePoint data store for which you want to enable real-time sync. 

4. On the data store **Data** page, wait until the **Connector state** changes to **Active** . 

5. In the **Real-time sync** field, click **View/edit** . 

6. To enable real-time sync, click the **Enable real-time sync** toggle. 

7. In the **Client secret** field, enter a value. This value is used to verify Microsoft SharePoint webhook events. We recommend using a string of 20 characters. 

8. Click **Save** . 

Wait for the **Real-time sync** field to change to **Running** . 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Microsoft SharePoint and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Microsoft API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Microsoft API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Microsoft SharePoint. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Microsoft API. 

### What's next

- To provide a user interface for querying your Microsoft SharePoint data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Microsoft SharePoint data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions, see Manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

- To add filters to the data store, see Add flters to Microsoft SharePoint datai store 

- (/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store). 



## Add filters to a Microsoft SharePoint data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/add-filters-to-sharepoint-data-store

This page explains how to add filters to your Microsoft SharePoint data stores in Gemini Enterprise. Filters determine which information is retrieved or excluded from the Microsoft SharePoint data store when users chat with the Assistant using the Gemini Enterprise app. 

### Permissions impact on filtering

The API permissions you grant during third-party configuration impact how you can filter your Microsoft SharePoint data store: 

- **Console filtering:** To configure filters in the Google Cloud console UI, the `Sites.Selected` scope is required. 

- **API filtering:** If your application uses the `Sites.Read.All` scope, UI filtering is unavailable. You must perform all filtering programmatically using the API. 

### Filter types

You can configure the following filters within the `params` object of your data connector: 

- **Inclusion filter** **(** **`admin_filter` )** : Retrieves only specific information from the Microsoft SharePoint data store. 

- **Exclusion filter** **(** **`admin_exclusion_filter` )** : Excludes specific information from the Microsoft SharePoint data store. 

- **Legacy filter** **(** **`structured_search_filter` )** : Previously used to create a data store with filters using the API. 

### Filter keys

The filter parameters accept an object containing key-value pairs. The keys represent the SharePoint fields you want to filter on, and the values are arrays of strings containing the criteria to match. When updating filters using the API, the following keys are supported: 

||`FIL`||
|---|---|---|
|Filter<br>name|`TER`<br>`_`<br>Description|URL examples|
||`KEY`||
|Site|`Sit`<br>`e`<br>Filters search results and restricts actions to the<br>Microsoft SharePoint site URLs.|`https://{your-tenant}.`<br>`sharepoint.com/sites/`<br>`{your-site-name}`|
|Path|`Pat`<br>`h`<br>Filters search results and restricts actions to the specific<br>URL prefixes. Use this for granular control to include or<br>exclude sensitive sub-folders. The paths can point to<br>any site, subsite, folder, or file.|i<br>`https://{your-tenant}.`<br>`sharepoint.com/sites/`<br>`{your-site-name}/`<br>`Documents3/`|

#### Exclude OneDrive content

By default, the Microsoft API returns both SharePoint and OneDrive content. OneDrive personal content is hosted on a separate domain, `https://{yourtenant}-my.sharepoint.com` , and every personal site is stored under the `/personal/` path. To exclude OneDrive content from Microsoft SharePoint results, add `https://{your-tenant}-my.sharepoint.com/personal/` as a `Path` exclusion filter. 

#### Filter combinations

The following table details how different combinations of inclusion and exclusion filters behave: 

Filter combination Behavior Path (Inclusion) + Operates as a Path inclusion filter only. Site (Empty) Site (Inclusion) + Operates as a Site inclusion filter only. Path (Empty) 

Filter combination Behavior 

Site (Inclusion) + Includes a broad site while excluding specific granular paths or sensitive Path (Exclusion) folders within it. Path (Inclusion) + Includes the intersection of both filters. A path is only included if both the Site (Inclusion) path and its parent site are specified. We recommend using a single inclusion filter (Site or Path) to prevent configuration errors due to an empty intersection. 

Site (Exclusion) + Excludes any path matching either exclusion filter from the data store. Path (Exclusion) 

### Update filters in an existing data store

You can update filters in an existing data store using either the Google Cloud console or the API. 

ConsoleREST (#rest) (#console) 

To modify existing filter configurations: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Microsoft SharePoint data store. 

3. Click **View/edit parameters** . 

4. In the **View/edit parameters** panel, add or update the Microsoft SharePoint URLs and filter types. 

5. Click **Save** . 

### Verify that the data store includes the filters

You can get the details of the data store to confirm that the filters you added or updated are correctly applied using the Google Cloud console or the API: 

ConsoleREST (#rest) To view the existing filter configurations: 

1. In the Google Cloud console > navigation menu, click **Data stores** . 

2. Select your Microsoft SharePoint data store. 

3. Click **View/edit parameters** . 

In the **View/edit parameters** panel, the existing filters applied to the data store are displayed. 

### What's next

- To provide a user interface for querying your Microsoft SharePoint data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Microsoft SharePoint data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions, see Manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Microsoft SharePoint configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config

To successfully connect Gemini Enterprise with Microsoft SharePoint, you must complete the following configuration steps. 

### Set up authentication and permissions

You need to set up authentication and permissions in Microsoft Entra admin center. This is crucial for allowing the connector to access and synchronize data. 

#### Register Microsoft Entra app for Microsoft SharePoint connector

Before creating the Microsoft SharePoint connector in Gemini Enterprise, register a Microsoft Entra application to enable secure access. 

To register Gemini Enterprise as an OAuth 2.0 application in Entra, do the following: 

1. Navigate to Microsoft Entra admin center (https://entra.microsoft.com). 

2. In the navigation menu, expand the **Entra ID** and select **App registrations** . 

3. On the **App registrations** page, click **New registration** . 

4. On the **Register an application** page, do the following: 

   - a. In the **Name** field, enter a name for your app. 

   - b. In the **Supported account types** section, select **Accounts in this organizational directory only** (which may also be labeled **Single tenant only** or **Single tenant only - MSFT** depending on your tenant setup). This restricts access to users and guests within your own tenant or directory. 

   - c. In the **Redirect URI** section, do the following: 

      - i. In the platform list, select `Web` . 

      - ii. In the redirect URI field, enter 

         - `https://vertexaisearch.cloud.google.com/console/oauth/sharepoin t_oauth.html` . 

   - d. Click **Register** . Microsoft Entra creates your app and displays the overview page of your app. 

5. In the app navigation menu, click **Authentication** . 

6. Click **Add redirect URI** . 

7. In the platform selection pane, do the following: 

   - a. Select **Web** . 

   - b. In the **Redirect URI** field, enter 

`https://vertexaisearch.cloud.google.com/oauth-redirect` . 

- c. Click **Configure** . 

Add federated credential for data ingestion 

If you are using **Data ingestion** as the connection mode and **Federated credentials** as authentication method, then do the following: 

1. In the app navigation menu, click **Certificates & secrets** . 

2. Select the **Federated credentials** tab. 

3. Click **Add credential** . 

4. Select **Other issuer** from the **Federated credential scenario** list. 

5. In the **Issuer** field, enter `https://accounts.google.com` . 

6. In the **Subject identifier** field, enter the value that you get from the Google Cloud console. This value is generated during the Microsoft SharePoint data store creation 

(/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store#create-data-store) in the data section. 

7. In the **Name** field, enter a unique label for the federated credential. 

8. Click **Add** to grant access. 

#### Create an OAuth 2.0 configuration

To create a connection using the OAuth 2.0 authentication method, you need to obtain a client ID, client secret, and your Tenant ID from your Microsoft Entra application registration page. 

Obtain client ID and client secret 

1. To obtain the client ID, do the following: 

   - a. In the app navigation menu, select **Overview** . 

   - b. Copy the **Application (client) ID** . 

2. To obtain the client secret for the app, do the following: 

   - a. In the app navigation menu, select **Certificates & secrets** . 

   - b. Click **New client secret** . 

   - c. In the client secret pane, do the following: 

      - i. In the **Description** field, enter a description for the secret. 

      - ii. In the **Expires** list, select an expiry duration. 

      - iii. Click **Add** . 

   - d. Copy the client secret from the **Value** column. 

Obtain Instance URI 

The Instance URI has one of the following formats: 

- For all first-level sites: `https://` _`DOMAIN_OR_SERVER`_ `.sharepoint.com` —for example, `mydomain.sharepoint.com` . 

- For a single site: `https://` _`DOMAIN_OR_SERVER`_ `.sharepoint.com/sites/` _`WEBSITE`_ — for example, `mydomain.sharepoint.com/sites/sample-site` . 

Obtain Tenant ID 

Your tenant ID can be found in the **Tenant ID** box on the overview page (https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView) in the Microsoft Entra admin center. 

#### Configure Microsoft API permissions

To configure the required API permissions for the app, do the following: 

1. Navigate to the app page. 

2. In the app navigation menu, select **API permissions** . 

3. Click **Add permissions** . 

4. In the **Request API permissions** pane, select **Microsoft Graph** . 

5. Search for and select the following permissions based on your connection mode: 

For the **Federated search** connection mode, no Graph API permissions are required. 

For the **Data ingestion** connection mode with **Federated credentials** : 

|Permission|Type<br>Description|
|---|---|
|`GroupMember.`<br>`Read.All`|ApplicationAllows the connector to read memberships and basic group<br>properties for all groups without a signed-in user.|
|`User.Read`|Delegated Allows the connector to read the profile of signed-in users.<br>It also allows the connector to read basic company<br>information of signed-in users.|
|Site control<br>options||
|Option 1:`Sites.`<br>`FullControl.All`|ApplicationAllows the connector to have full control of all site<br>collections.|
|Option 2:`Sites.`<br>`Selected`|ApplicationAllows the connector to access a subset of site collections.<br>The specific site collections and the permissions granted<br>can be configured in SharePoint Online.|
|Profile reading<br>options||
|Option 1:`User.`<br>`Read.All`|ApplicationAllows the connector to read user profiles.|

Option 2: `User.` ApplicationAllows the connector to read a basic set of profile `ReadBasic.All` properties of other users in the organization. 

For the **Data ingestion** connection mode with **OAuth 2.0 refresh token** : 

|Permission|Type|Description|
|---|---|---|
|`GroupMember.`<br>`Read.All`|Applicat|ionAllows the connector to read memberships and basic group<br>properties for all groups without a signed-in user.|
|`User.Read`|Delegat|ed Allows the connector to read the profile of signed-in users.<br>It also allows the connector to read basic company<br>information of signed-in users.|
|`User.Read.All`|Applicat      i|ionAllows the connector to read user profiles.|
|Site control<br>options|||
|Option 1:`Sites.`<br>`FullControl.All`|Applicat|ionAllows the connector to have full control of all site<br>collections.|
|Option 2:`Sites.`<br>`Selected`|Applicat|ionAllows the connector to access a subset of site collections.<br>The specific site collections and the permissions granted<br>can be configured in SharePoint Online.|

If you enable **Actions** for either the **Federated search** or **Data ingestion** connection mode, also select the following permissions: 

|Permission|Type|Description|
|---|---|---|
|`Sites.Read`<br>`Write.All`|Delega|tedAllows the connector to edit or delete documents and list<br>items in all site collections on behalf of the signed-in user.|
|`Files.Read`<br>`Write`|Delega|tedAllows the connector to read (download), create (upload),<br>update, and delete the signed-in user's files.|
|`Files.Read`|Delega|tedAllows the connector to read (download), create (upload),<br>i|
|`Write.All`||update, and delete all files the signed-in user can access.|
|`Sites.Manage.`<br>`All`|Delega|tedAllows the connector to create or delete document libraries<br>and lists in all site collections on behalf of the user.|

6. Click **Add Permissions** . 

7. In the **Request API permissions** pane, select **Microsoft SharePoint** . 

8. Search for and select the following permissions based on your connection mode: 

For the **Federated search** connection mode: 

|Permission|Type|Description|
|---|---|---|
|`Sites.`|Delegat|edAllows the connector to run search queries and to read basic site|
|`Search.All`||info on behalf of the current signed-in user. Search results are<br>based on the user's permissions instead of the app's permissions.|
|`AllSites.`|Delegat|edAllows the connector to read documents and list items in all site|
|`Read`||collections on behalf of the signed-in user.|

For the **Data ingestion** connection mode with **Federated credentials** : 

|Permission|Type|Description|
|---|---|---|
|Site control<br>options|||
|Option 1:`Sites.`<br>`FullControl.`<br>`All`|Applicat|ionAllows the connector to have full control of all site<br>collections.|
|Option 2:`Sites.`<br>`Selected`|Applicat|ionAllows the connector to access a subset of site collections<br>with a signed-in user. The specific site collections and the<br>permissions granted can be configured in SharePoint Online.|

For the **Data ingestion** connection mode with **OAuth 2.0 refresh token** : 

|Permission|Type|Description|
|---|---|---|
|Site control<br>options|||
|Option 1:`All`|Delega|tedAllows the connector to have full control of all site collections|
|`Sites.Full`<br>`Control`||on behalf of the signed-in user.|

Option 2: `Sites.` DelegatedAllows the connector to access a subset of site collections `Selected` with a signed-in user. The specific site collections and the permissions granted can be configured in SharePoint Online. 

If you enable **Actions** for either the **Federated search** or **Data ingestion** connection mode, also select the following permissions: 

Permission Type Description `AllSites.` DelegatedAllows the connector to create, read, update, delete, upload, and `Write` download documents and list items in all site collections on behalf of the signed-in user. 

9. Click **Add Permissions** . 

**Note:** When you use **`Sites.Selected`** , you must grant **`fullcontrol`** (#grant-fullcontrol) permission to the selected sites. Additionally, for this permission to take effect, you must do at least one of the following when creating the SharePoint data store (/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store) in Gemini Enterprise: 

Use a specific site URL as your SharePoint connector instance URL—for example, **`mydomain.sharepoint.com/sites/sample-site`** . 

Provide precise **`siteName`** filters when setting up the Gemini Enterprise data store. 

10. Grant administrator consent. For information about how to grant consent, see Grant tenant-wide administrator consent to an application 

(https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent? pivots=portal) 

in the Microsoft Entra documentation. 

**Caution:** 

- **Tenant-wide administrator consent (CRITICAL):** You **must** grant tenant-wide administrator consent in Microsoft Entra ID for the registered application. Lack of administrator consent is a common failure point that prevents the connector from authenticating. 

**Dual App IDs:** Note that Gemini Enterprise uses different Microsoft Entra App IDs for different features. You need one App ID for the backend 'Data store' connection and a separate App ID to enable the 'Upload from OneDrive/SharePoint' button in the chat interface. Both applications require administrator consent. 

#### Grant `fullcontrol` permission to selected sites

If you choose the `Sites.Selected` option to grant control over selected sites in Microsoft Graph, you must grant the `fullcontrol` permission to the Gemini Enterprise application. You can do so using one of the following methods: 

PowerShell 

Microsoft Graph 

PowerShellMicrosoft Graph… (#powershell) 

For a generic syntax to grant permissions using PnP PowerShell, see Granting permissions using PnP PowerShell 

(https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins-modernize/understandingrsc-for-msgraph-and-sharepoint-online#granting-permissions-via-pnp-powershell) . 

1. To grant the `FullControl` permission run the following command in the PowerShell : 

```
Grant-PnPAzureADAppSitePermission -AppId CLIENT_ID -DisplayName
DISPLAY_NAME -Permissions FullControl -Site SITE_URL
```

Replace the following: 

- _`CLIENT_ID`_ : the client ID of the Microsoft Entra application. 

- _`SITE_URL`_ : the site URL for your SharePoint site, for example, `https://example.sharepoint.com/sites/ExampleSite1` . 

- _`DISPLAY_NAME`_ : the display name for the Microsoft Entra application. 

### Troubleshooting

This section describes how to resolve common issues with the Microsoft SharePoint connector. 

#### Users see "Need admin approval" when they connect

When users connect to Microsoft SharePoint from the Gemini Enterprise web app for the first time, Microsoft might show a **Need admin approval** screen. This happens if Gemini Enterprise requests administrator-level permissions, or if your Microsoft Entra tenant prohibits users from authorizing third-party apps without prior tenant-wide administrator consent. 

To resolve this issue, an administrator must complete the first authorization. After that, other users in your tenant can connect without the approval screen. 

1. Ask a Microsoft Entra ID administrator who can grant tenant-wide consent to sign in to the Gemini Enterprise web app and connect to Microsoft SharePoint. 

2. On the permissions screen, have the administrator select **Consent on behalf of your organization** , and then click **Accept** . 

3. Ask users to connect again. 

For more information, see Grant tenant-wide admin consent 

(https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent? pivots=portal) 

in the Microsoft Entra documentation. 

**Note:** Deleting and re-creating the data store doesn't resolve this issue, because consent is granted in your Microsoft Entra tenant, not to the data store. 



## Microsoft Teams connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams

The Microsoft Teams data store for Gemini Enterprise lets you search and perform actions on your channels, chats, and schedules. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported Microsoft Teams versions

The Microsoft Teams data store supports Microsoft Teams version 2.1 and later. 

### Supported actions

When the Microsoft Teams data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Send channel<br>message|Sends a message to a specified channel.|
|Send chat message|Sends a message in a chat.|
|Update channel<br>message|Updates an existing message in a specified channel.|
|Update chat message|Updates an existing message in a chat.|
|Create channel|Creates a new channel in a specified team.|

|Action|Description|
|---|---|
|Update channel|Updates an existing channel's display name, description, or type in a<br>specified team.|
|Create chat|Creates a new one-to-one or group chat.|
|Update chat|Updates metadata of an existing chat, such as the topic.|
|Add member to<br>channel|Adds a member to an existing channel.|
|Create schedule|Creates a new schedule for a team in the Shifts application.|
|Create time off entry|Creates a time-off entry for a team member.|
|Update time off entry|Updates an existing time-off entry for a team member.|

**Note:** Additional read-only actions are also available. 

### Required permissions

To enable Gemini Enterprise to perform federated search and actions using Microsoft Teams, you need the following graph permissions. 

**Note:** An administrator must grant consent (/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#grant-admin-consent) for all the delegated permissions listed below. Once consent is granted, the "Status" column will display "Granted" with a green tick mark (✓). 

|Connection<br>mode|Permission|Permission<br>type|Purpose|
|---|---|---|---|
|Federated<br>search|`Channel.Read`<br>`Basic.All`|Delegated|Allows the app to read the names and descriptions<br>of channels.|
||`Channel`<br>`Member.Read.`<br>`All`|Delegated|Allows the app to read the members of channels.|
||`Channel`<br>`Message.Read.`<br>`All`|Delegated|Allows the app to read user channel messages.|
||`Chat.Read`|Delegated|Allows the app to read all chats.|
||`Chat.Read`<br>`Basic`|Delegated|Allows the app to read basic properties of chats.|
||`ChatMessage.`<br>`Read`|Delegated|Allows the app to read all one-to-one and group<br>chats messages.|
||`Group.Read.`<br>`All`|Delegated|Allows the app to read the Microsoft Purview<br>sensitivity labels assigned to a team's parent<br>Microsoft 365 group, which are used to apply<br>Sensitive Data Protection (redaction) to Microsoft<br>Teams content.|
||`Schedule.`<br>`Read.All`|Delegated|Allows the app to read schedules, schedule groups,<br>and shifts for teams.|
||`Team.Read`<br>`Basic.All`|Delegated|Allows the app to read the names and description of<br>teams.|
||`TeamMember.`<br>`Read.All`|Delegated|Allows the app to read the members of teams.|
||`User.Read.All`|Delegated|Allows the app to read all users' full profiles.|

|Connection<br>mode|Permission|Permission<br>type|Purpose|
|---|---|---|---|
|Federated<br>search and<br>|`Channel.`<br>`Create`|Delegated|Allows the app to create channels in Microsoft<br>Teams. Required for the create channel action.|
|actions|`Channel.Read`<br>`Basic.All`|Delegated|Allows the app to read the names and descriptions<br>of channels.|
||`Channel`<br>`Member.Read.`<br>`All`|Delegated|Allows the app to read the members of channels.|
||`Channel`<br>`Member.Read`<br>`Write.All`|Delegated|Allows the app to add and remove members from<br>channels. Required for the add member to channel<br>action.|
||`Channel`<br>`Message.Read.`<br>`All`|Delegated|Allows the app to read user channel messages.|
||`Channel`<br>`Message.Read`<br>`Write`|Delegated|Allows the app to update channel messages.<br>Required for the update channel message action.|
||`Channel`<br>`Message.Send`|Delegated|Allows the app to send messages in any channel.|
||`Channel`<br>`Settings.Read`<br>`Write.All`|Delegated|Allows the app to read and update the settings of<br>channels. Required for the update channel action.|
||`Chat.Create`|Delegated|Allows the app to create new chats. Required for the<br>create chat action.|
||`Chat.Read`|Delegated|Allows the app to read all chats.|
||`Chat.Read`<br>`Basic`|Delegated|Allows the app to read basic properties of chats.|
||`Chat.Read`<br>`Write`|Delegated|Allows the app to read and write one-to-one and<br>group chat threads, including chat messages.<br>Required for the update chat and update chat<br>message actions.|
||`ChatMessage.`<br>`Read`|Delegated|Allows the app to read all one-to-one and group chat<br>messages.|

|Connection<br>mode|Permission|Permission<br>type|Purpose|
|---|---|---|---|
||`ChatMessage.`<br>`Send`|Delegated|Allows the app to send chat messages.|
||`Group.Read.`<br>`All`|Delegated|Allows the app to read the Microsoft Purview<br>sensitivity labels assigned to a team's parent<br>Microsoft 365 group, which are used to apply<br>Sensitive Data Protection (redaction) to Microsoft<br>Teams content.|
||`Schedule.`<br>`Read.All`|Delegated|Allows the app to read schedules, schedule groups,<br>and shifts for teams.|
||`Schedule.Read`<br>`Write.All`|Delegated|Allows the app to create and update schedules,<br>shifts, and time-off entries for teams. Required for<br>the create schedule, create time off entry, and<br>update time off entry actions.|
||`Team.Read`<br>`Basic.All`|Delegated|Allows the app to read the names and description of<br>teams.|
||`TeamMember.`<br>`Read.All`|Delegated|Allows the app to read the members of teams.|
||`User.Read.All`|Delegated|Allows the app to read all users' full profiles.|

For information about how to configure these permissions, see Configure the Microsoft Graph permissions 

(/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#microsoft-graph-minimumpermissions) 

. For a detailed reference on graph permissions, see the Microsoft documentation on Minimum graph permissions reference 

(https://learn.microsoft.com/en-us/graph/permissions-reference). 

### Limitations

The Microsoft Teams data store for Gemini Enterprise has the following limitations: 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a 

single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Microsoft Teams data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Microsoft Teams data store is supported only in the `global` , `us` , and `eu` locations. 

### What's next

- To create and configure a data store with Microsoft Teams, see Set up a Microsoft Teams data store 

- (/gemini/enterprise/docs/connectors/ms-teams/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Microsoft Teams data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-teams/set-up-data-store

This page describes how to create a data store and connect Microsoft Teams to Gemini Enterprise. 

### Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have configured your identity provider (/gemini/enterprise/docs/configure-identity-provider). 

Before you set up your Microsoft Teams data store, ensure the following: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   - b. Locate the user account and click **Edit** . 

   - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Register Gemini Enterprise as an OAuth 2.0 application in Microsoft Entra ID (/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#entra-app-registration) and obtain the following credentials (/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#obtain-client-id-andclient-secret) 

: 

- Client ID 

- Client secret 

Tenant ID 

3. Configure the Microsoft Graph application permissions (/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#microsoft-graphminimum-permissions) 

with the consent of a Microsoft Teams administrator. 

4. Add the following URL as web callback URL: 

https://vertexaisearch.cloud.google.com/oauth-redirect 

#### Create the Microsoft Teams data store

To create the Microsoft Teams data store, perform the following steps: 

1. In the Google Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** , search for **Microsoft Teams** , and click **Select** . 

6. In the **Data** section: 

   - a. In the connection mode section, choose **Federated search** . 

   - b. In the **Authentication settings** section, configure authentication: 

      - i. Provide the following authentication details: 

         - **Client ID:** The unique identifier of the application registered in Microsoft Entra ID. 

         - **Client Secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID. 

         - **Tenant ID:** The unique identifier for your Microsoft 365 or Azure environment. 

For information on how to obtain the client ID, client secret, and tenant ID, see Obtain client ID and client secret 

(/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#obtainclient-id-and-client-secret) 

and Obtain tenant ID 

(/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#obtaintenant-id) 

- . For the permissions required to perform search and actions, see Required permissions 

(/gemini/enterprise/docs/connectors/ms-teams#set-up-permissions). 

- ii. Click **Login** and complete the Microsoft sign-in. 

iii. Click **Continue** . 

   - c. In the **Advanced options** section: 

      - i. **Azure Tenant** : Enter the tenant ID. This is a required field and must match the **Tenant ID** provided in the **Authentication settings** section. 

      - ii. **Include All Groups** : Optional: Enable this checkbox to list all the groups in your organizations or only groups the logged in user is a member of. 

      - iii. **Include All Users** : Optional: Enable this checkbox to list all the users in your organizations or only the logged in users. 

      - iv. Click **Continue** . 

   - d. In the **Entities to search** section, select all the entities to search from the list. You must select at least one entity. 

7. Click **Continue** . 

8. In the **Actions** section, for **Select Microsoft Teams actions to enable** , choose the actions from the category to enable them for the data store. 

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

      - Select **Google-managed encryption key** or **Cloud KMS key** . If you selected **Cloud KMS key** : 

         - In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

12. Click **Continue** . 

13. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Microsoft Teams connector is ready to be used. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Microsoft Teams data store 

(/gemini/enterprise/docs/connect-existing-data-store), and authorize 

(/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to Microsoft Teams before executing any queries. 

For information on permissions required to perform search, see Configure the Microsoft Graph permissions 

(/gemini/enterprise/docs/connectors/ms-teams/ms-teams-config#microsoft-graph-minimumpermissions) 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Microsoft Teams and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Microsoft API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Microsoft API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Microsoft Teams. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Microsoft API. 

### What's next

- To provide a user interface for querying your data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Microsoft Teams data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions, see Manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC.
