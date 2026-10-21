# Gemini Enterprise: connectors and data stores / Connect Microsoft Entra ID to Add filters to a Microsoft OneDrive data store
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 415-454, extracted 2026-10-18

Contains:
- Connect Microsoft Entra ID (pages 415-426) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id
- Microsoft Learn connector: overview (pages 427-428) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/microsoft-learn
- Set up a Microsoft Learn data store (pages 429-433) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/microsoft-learn/set-up-data-store
- OneDrive connector: overview (pages 434-439) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive
- Set up a Microsoft OneDrive data store (pages 440-450) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store
- Add filters to a Microsoft OneDrive data store (pages 451-454) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/add-filters-to-onedrive-data-store

## Connect Microsoft Entra ID

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id

This page describes how to connect Microsoft Entra ID to Gemini Enterprise. 

After you set up your data source and import data the first time, the data store syncs data from that source at a frequency that you select during setup. 

**Note:** After you connect Microsoft Entra ID to your app, Google strongly recommends that you enable Knowledge Graph to significantly enhance search quality for your users. For more information, see Knowledge Graph: Powering intelligent and context-aware search (/gemini/enterprise/docs/use-knowledge-graph-search). 

### Supported versions

The Entra ID connector supports all hosted versions of Entra ID through the Microsoft Graph API v1.0. 

### Before you begin

Before you set up your data store and import data, you must obtain a client ID and secret for authentication and configure the minimum required permissions for the application. This section provides information about how to complete these tasks. 

#### Set up access control for Entra ID

To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider (/gemini/enterprise/docs/configure-identity-provider). 

#### Obtain a client ID and client secret

1. Create an Entra ID application: 

      - a. Sign in to Microsoft Entra administrator center (https://entra.microsoft.com) as an administrator and click **Application** . 

      - b. In the **Application** drop-down list, click **App registrations** . 

      - c. In the **App registrations** page, click **New registration** . 

      - d. Click **Add new registration** and do the following: 

         - Enter a name for the application. 

         - Under **Supported account types** , select **Single tenant only -** _TENANT_NAME_ , where _TENANT_NAME_ is the name of your Microsoft Entra tenant. 

         - Under **Redirect URI** , add a web redirect URI pointing to: `https://login.microsoftonline.com/common/oauth2/nativeclient` . 

      - e. Click **Register** . 

2. Save credentials: 

   - On your registered application window, save the following values for later use: 

      - a. Use the **Application (client) ID** to set the **Client ID** parameter. 

      - b. Use the **Directory (tenant) ID** to set the **Azure Tenant** parameter. 

3. Create client secret: 

      - a. Navigate to **Certificates & secrets** . 

      - b. Click **New client secret** and specify a duration. 

      - c. Save the client secret and copy the client secret value for later use. 

<!-- Start of picture text -->
Save the client secret value<br><!-- End of picture text -->

#### Configure the minimum permissions required for the application

1. On your registered application window, click **API permissions** . 

2. Under **Configured permissions** , select **Microsoft Graph** and configure the following permissions: 

```
User.Read
```

- `User.Read.All (Application)` 

If you want to ingest `profileCardAttributes` , then configure the following permissions: 

   - `People.Read.All (Application)` 

   - `PeopleSettings.Read.All (Application)` 

   - `PeopleSettings.Read.All (Delegated)` 

3. Grant **admin consent** for all the added permissions. An administrator's consent is required to use client credentials in the authentication flow. 

Minimum permissions 

The following table lists the minimum permissions that you require to create an Entra ID connector: 

|Permission<br>Usage<br>reason|Description|
|---|---|
|`User.Read`<br>Data<br>ingestion|Read organization details during connection<br>establishment.|
|`User.Read.All`<br>`(Application)`<br>Data<br>ingestion|Read all users in the organization.|
|`People.Read.All`<br>`(Application)`<br>Data<br>ingestion|Read all the relevant people information, such as<br>contacts, for all users in an organization.|
|`PeopleSettings.Read.All`<br>`(Application)`<br>Data<br>ingestion|Read user configurations for all the users in the<br>organization, such as profileCardSettings.|
|`PeopleSettings.Read.All`<br>`(Delegated)`<br>Data<br>ingestion|Read user configurations for all the users in the<br>organization, such as profileCardSettings.|

### Create an Entra ID data store

To use the Google Cloud console to sync data from Entra ID to Gemini Enterprise , follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Click **Create Data Store** . 

4. On the **Select a data source** page, scroll or search for **Entra ID** to connect your third-party source. 

5. Under **Authentication settings** , enter the client ID and client secret. 

6. Under **Advanced options** : 

   - If needed, click **Enable Static IP Addresses** . After creating the connector, you need to add the registered static IPs to your allowlist in 

order for sync runs to succeed. For more information, see Configure static IP egress (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

- To enable the connector to fetch extension properties 

- (https://learn.microsoft.com/en-us/graph/api/resources/extensionproperty? view=graph-rest-1.0) 

- , which are used to add a custom property to a directory object, select the **Enable Extension Properties** checkbox. 

- If you want to filter ingested user information, provide a custom SQL filter. The filter must be a valid SQL string. 

Keys in the filter string must correspond to the following fields: 

- `Id` (the user's object ID in Microsoft Entra ID) 

- `employeeType` 

- `onPremisesSyncEnabled` 

- `accountEnabled` 

The following are examples of valid SQL filters: 

```
id = 'abc' AND accountEnabled = true
employeeType='E' AND onPremisesSyncEnabled= true
```

**Note:** For information about finding the **`id`** (the user's object ID in Microsoft Entra ID), see the Microsoft Entra ID documentation (https://learn.microsoft.com/en-us/partner-center/account-settings/find-ids-anddomain-names#find-the-user-object-id) 

- In the **Azure Tenant** field, enter the Azure tenant ID that you obtained when you created an Entra ID application. 

- To apply a rate limit on the queries that the connector sends to the Entra ID instance, in the **Max QPS** field, specify the maximum queries per second. The default value is 80 QPS. 

Click **Continue** . 

7. Under **Choose entities you want to sync** : 

      - Click **User Profiles** . To filter the data based on `Id` for data ingestion, click **Filter** , and then do the following: 

         - To specify data to be included in the search index, select **Include in the index** and then specify the filter string in the **Id** field. 

         - To specify data to be excluded from the search index, select **Exclude from the index** and then specify the filter string in the **Id** field. 

      - Select the **Full sync** frequency. 

8. Click **Continue** . 

9. In **Configure your data connector** , select a region for your data store. 

10. Enter a name for your data connector. 

11. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

12. If you selected **Enable Static IP Addresses** under **Advanced options** , view the registered static IP addresses for the connector and add them to your allowlist for Entra ID. 

   - a. Go to the **Data Stores** page and click your connector name to see details about it on its **Data** page. 

   - b. In the **Static IPs** field, click **View and confirm IPs** . 

   - c. Copy the static IP addresses for the connector. 

   - d. In the Microsoft Entra administrator center, add the static IP addresses to a named or trusted location within an existing conditional access policy. For more information, see Conditional Access: Network assignment (https://learn.microsoft.com/en-us/entra/identity/conditional-access/conceptassignment-network) 

### Check the connector state

1. To check the status of your ingestion, go to the **Data Stores** page and click your connector name to see details about it on its **Data** page. The **Connector state** changes from **Creating** to **Running** when it begins to synchronize data. When ingestion is complete, the state changes to **Active** to indicate that the connection to your data source is set up and awaiting the next scheduled synchronization. 

Depending on the size of your data, ingestion can take several minutes or several hours. 

2. When the connector state changes to **Active** , navigate to the **Entity** tab. 

3. Click the **userprofiles** entity. 

4. Check the number of ingested documents and verify that it matches the number of users in Entra ID. 

The following standard user attributes are ingested as part of each user record: 

|Vertex AI schema field nam|i e Entra ID attribute name|
|---|---|
|`name.displayName`|Display Name|
|`name.familyName`|Last Name|
|`name.givenName`|First Name|
|`name.username`|User Principal Name|
|`email.value`|Email|
|`employeeId`|Employee Id|
|`personId`||
|`employeeType`|Employee type|
|`hireDate`|Employee Hire Date|
|`department`|Department|
|`organizations.jobTitle`|Job title|

|`organizations.location`|Office Location|
|---|---|
|`Phone`|Business phone|
|`managers.email`,`managers`<br>`personId`|`.`<br>Not a direct attribute (management chain from immediate<br>manager to top-level manager)|
|`directManager.personId`|Not a direct attribute (manager's`personId`)|
|`displayphoto.`|Base64-encoded profile picture|
|`imagebinary.data`||

If the Entra ID app has the required permissions to ingest custom attributes, it ingests up to 15 profile card attributes 

(https://learn.microsoft.com/en-us/graph/add-properties-profilecard#add-a-custom-attributeto-the-profile-card) 

per record. By default, the custom attributes are not searchable. 

### Configure searchable attributes

To make the custom attributes searchable, do the following: 

1. In the **userprofiles** page, navigate to the **Schema** tab. 

2. Click **Edit** . 

3. Deselect the attributes, such as **address** , from being **retrievable, searchable, and indexable** , then click **Save** . 

The **Edit** button remains inactive for a few minutes before reactivating. 

4. When the **Edit** button is in **Active** state, click **Edit** . 

5. Select the **retrievable, searchable, and indexable** boxes for the required custom attributes. 

6. Enable search. 

7. Click **Save** . 

### Test the search engine

After configuring your search engine, test its capabilities to verify whether it returns accurate results based on user access. 

1. Enable web app: 

   - a. Go to the app integration configurations and toggle to **Enable the web app** . 

2. Test web app: 

   - a. Click **Open** next to the web app link and sign in as a user. 

   - b. Verify that search results are restricted to items accessible by the user. 

### Preview people search results

1. In the search app, navigate to **Preview** and start searching within the console when using Google IdP. 

   - Alternatively, navigate to the provided link and sign in with your IdP to start searching. 

   - The search results appear as **people cards** , displaying user details such as **Name, Job title, Email, and Profile picture** . 

2. Click a **people card** to view a detailed profile page, which includes the following: 

   - **Name** 

   - **Profile picture** 

   - **Job title** 

   - **Department** 

   - **Management chain** 

   - **Direct reports** 

3. If custom attributes (profile card properties) are ingested and made indexable, searchable, and retrievable: 

- Searching by a custom attribute value returns only person profiles containing those attributes. 

- Custom attributes appear in search results, but can only be accessed through the API, not the Vertex Search user interface. 

### Configure the workforce pool for non-Google IdP without SSO

1. If your employees use a non-Google IdP, lack SSO with Google, or are not Google Workspace customers, set up a workforce pool as described in Configure access controls for custom data sources 

(/gemini/enterprise/docs/identity) to enable the employee search. 

   - The workforce pool lets you to manage and authenticate users from external identity providers, such as Azure or Okta, within Google Cloud console. 

2. To configure your workforce pool and enable the web app for seamless user access, do the following: 

      - a. Create workforce pool at the organization level in Google Cloud by following the appropriate setup manual: 

         - i. Azure OIDC setup 

            - (/iam/docs/workforce-sign-in-azure-ad#create-oidc-provider) 

         - ii. Azure SAML setup 

            - (/iam/docs/workforce-sign-in-azure-ad#create-saml-provider) 

         - iii. Okta & OIDC setup (/iam/docs/workforce-sign-in-okta#create-oidc-provider) 

         - iv. Okta & SAML setup 

            - (/iam/docs/workforce-sign-in-okta#create-saml-provider) 

      - b. Configure the workforce pool in **Gemini Enterprise** > **Settings** for the region where you create your app. 

### Recommended rate limits

The following table lists the recommended rate limits based on the number of users. Requests that exceed the limits are throttled. 

|Quota group|Requests per second|
|---|---|
|S (Fewer than 50 users)|105|
|M (50-500 users)|150|
|L (More than 500 users)|240|

### Known limitations

This following are the known limitations for the Entra ID connector: 

- Incremental sync is not supported. 

- Access Control Lists (ACLs) are not supported. All the users are accessible across the organization. 

- If you add a project to a VPC Service Controls perimeter after you create a connection, the connector sync run fails with the following error: `Connector is blocked due to the project being added to the VPC-SC perimeter. Please re-create the data store.` Recreate the data store to allow it to work within the VPC Service Controls perimeter. 

### Error messages

The following table lists the error messages that you might get when you use the Entra ID connector: 

|Error message|Description|Troubleshooting|
|---|---|---|
|Authorization_RequestDenied|The user account|Provide the<br>required scopes|
|Insufficient privileges to complete the<br>operation.|doesn't contain the<br>required scopes to|(#minimum-permissions) to the<br>user account that is used to|
||read data.|create the connection.|

|Error message|Description|Troubleshooting|
|---|---|---|
|Failed to retrieve OAuth token<br>information|The client credential<br>provided when<br>configuring the<br>connector is invalid.|Verify the following:<br>The client secret<br>corresponding to the client ID<br>is provided. When you<br>configure the connection,<br>specify the client secret value<br>and not its secret ID.|
|||The tenant ID is valid.|
|||The client secret hasn't<br>expired. If the client secret has<br>expired, edit the connection<br>and specify the new client<br>secret.|
|Connector is blocked due to the project<br>being added to the VPC-SC perimeter.<br>Please re-create the data store.|<br>The connector was<br>created before the<br>project was added to<br>a VPC Service<br>Controls perimeter.|Recreate the data store to allow it<br>to work within the VPC Service<br>Controls perimeter.|

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps in Create an app (/gemini/enterprise/docs/create-app). 

- To preview how your search results appear after your app and data store are set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Microsoft Learn connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/microsoft-learn

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

The Microsoft Learn data store for Gemini Enterprise lets you search official Microsoft/Azure documentation to find the most relevant and trustworthy content for your queries. 

### Limitations

- Enforcing a VPC Service Controls perimeter on existing Microsoft Learn data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Microsoft Learn data store is supported only in Global, US, and EU locations. 

- This connector does not require authentication (Public API). 

### What's next

- To create and configure a data store with Microsoft Learn, see Set up a Microsoft Learn data store 

- (/gemini/enterprise/docs/connectors/microsoft-learn/set-up-data-store). 

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## Set up a Microsoft Learn data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/microsoft-learn/set-up-data-store

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

This page describes how to create a data store and connect Microsoft Learn to Gemini Enterprise. 

### Before you begin

Before setting up your Microsoft Learn connection, ensure you have the following in place: 

- Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Locate the user account and click **Edit** . 

3. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions (https://cloud.google.com/gemini/enterprise/docs/access-control). 

**Note:** Microsoft Learn accesses public data from Mermaid Chart and does not require authentication. 

### Create Microsoft Learn data store

To create a Microsoft Learn data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Microsoft Learn** , and click **Select** . 

6. In the **Data** section, in the **Entities to search** section, select all the required entities. 

7. Click **Continue** . 

8. In the **Actions** section, for **Select Microsoft Learn actions to enable** , choose the actions from the category to enable them for the data store. 

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

14. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Microsoft Learn connector is ready to be used. 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Microsoft Learn and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the microsoft-learn API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (microsoft-learn API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Microsoft Learn. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the microsoftlearn API. 

### What's next

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## OneDrive connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive

The Microsoft OneDrive data store for Gemini Enterprise lets you search and perform actions on your files and folders. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported Microsoft OneDrive versions

The Microsoft OneDrive data store supports all hosted versions of Microsoft OneDrive through the Microsoft Graph API v1.0. 

### Supported actions

When the Microsoft OneDrive data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create folder|Creates a new folder at a specified path in Microsoft OneDrive.|
|Copy file|Copies a file from a source to a destination in Microsoft OneDrive.|
|Upload file|Uploads a file to a specified location in Microsoft OneDrive.|
|Download file|Downloads a file from Microsoft OneDrive to a specified location.|
|Copy folder|Copies a folder from a source to a destination in Microsoft OneDrive.|
|Move file|Moves a file from a source to a destination in Microsoft OneDrive.|

|Action|Description|
|---|---|
|Move folder|Moves a folder from a source to a destination in Microsoft OneDrive.|
|Rename file|Renames a file in Microsoft OneDrive.|
|Rename folder|Renames a folder in Microsoft OneDrive.|
|Share file or folder|Shares a file or folder with specified recipients or generates a share link.|
|Update file propertie      i|i s Updates metadata properties of a file in Microsoft OneDrive.|

**Notes** : 

- Additional read-only actions are also available. 

The maximum file size for file uploads and downloads in Gemini Enterprise is 50 MB. 

#### Required permissions

To enable Gemini Enterprise to perform search and data ingestion using the Microsoft OneDrive data store, you need the following permissions: 

Microsoft Graph API permissions 

The table below outlines the permissions required for each connection mode. 

**Note:** The following table outlines the permissions required for each connection mode. If you enable **Actions** for either the **Federated search** or **Data ingestion** connection mode, also select the permissions listed in the **Actions** row. 

|Connection<br>mode|Scope|Purpose|
|---|---|---|
|Federated<br>search|`Files.Read.`<br>`All`|(Delegated) Allows the data store to read all files that the user can<br>access.|
||`Sites.Read.`<br>`All`|(Delegated) Allows the data store to read documents and list items in<br>all site collections that the user can access.|
||`User.Read.`<br>`All`|(Delegated) Allows the data store to resolve user drive locations for<br>content discovery.|
|Data<br>ingestion|`Group`<br>`Member.`<br>`Read.All`|(Federated credentials & OAuth 2.0 refresh token) Allows the data<br>store to read memberships and basic group properties for all groups<br>without a signed-in user.|
||`User.Read`|(Federated credentials & OAuth 2.0 refresh token) Allows the data<br>store to read the profile of signed-in users. It also allows the data<br>store to read basic company information of signed-in users.|
||`User.Read.`<br>`All`|(OAuth 2.0 refresh token only) Allows the data store to read user<br>profiles.|
||`Sites.Full`<br>`Control.All`<br>(Option 1)<br>`Sites.`<br>`Selected`<br>(Option 2)|(Federated credentials & OAuth 2.0 refresh token) Option 1 allows<br>the data store to have full control of all site collections. Option 2<br>allows the data store to access a subset of site collections. The<br>specific site collections and the permissions granted can be<br>configured in Microsoft OneDrive.|
||`User.Read.`<br>`All`(Option<br>1)<br>`User.Read`<br>`Basic.All`<br>(Option 2)|(Federated credentials only) Option 1 allows the data store to read<br>user profiles. Option 2 allows the data store to read a basic set of<br>profile properties of other users in the organization.|

|Connection<br>mode|Scope|Purpose|
|---|---|---|
|Actions|`Files.Read`<br>`Write.App`<br>`Folder`|(Delegated) Allows the data store to read, create, update and delete<br>files in the Microsoft OneDrive folder.|
||`Files.Read`<br>`Write`|Delegated: Allows the data store to read, download, create, upload,<br>update, and delete the files that the user can access.|
||`Files.Read`<br>`Write.All`|(Delegated) Allows the data store to read and update files across all<br>drives the user has access to. Required for the file and folder<br>mutation actions (copy, move, rename, share, update properties)<br>that operate on files stored in drives beyond the user's own Microsoft<br>OneDrive.|

For information on how to add the permissions for Microsoft OneDrive, see Configure Microsoft OneDrive and set the necessary permissions (/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config#configure-apipermissions) 

### Limitations

This section outlines known issues and limitations that may affect your use of the Microsoft OneDrive data store. 

   - When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

   - Enforcing a VPC Service Controls perimeter on existing Microsoft OneDrive data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

   - The Microsoft OneDrive data store is supported only in the `global` , `us` , and `eu` locations. 

- The following are the limitations for the Microsoft OneDrive federated data store: 

   - **Search limitations** : Search results may vary and are not always comprehensive for all file types. Content in archived or encrypted folders may not be accessible for search. Federated search does not support searching within attachments. 

   - **Delegated access:** Access to shared Microsoft OneDrive files or folders may require specific permissions not covered by standard user authorization. 

   - **Layout parser in federated search mode:** While the layout parser is standard, its effectiveness on complex PDFs (with tables, multi-column layouts, or needing OCR) is limited in federated search mode. This mode's real-time API calls might not provide the complete data or time required for the deep analysis the layout parser performs during data ingestion. 

   - **Unsupported PDF Features:** Consequently, complex PDF structures might not be fully analyzed or searchable. This includes: 

      - Multi-column text layouts 

      - Data within embedded tables and charts 

      - Text in scanned documents requiring Optical Character Recognition (OCR) 

      - Documents with non-linear reading orders or intricate formatting. 

- The following are the limitations for the Microsoft OneDrive ingestion data store: 

   - Incremental sync does not detect folder-level actions like **Copy** , **Move** , or **Rename** . 

### Recommendation

For Microsoft OneDrive data containing PDFs with complex features (like tables, multi-column layouts, or OCR-dependent content), we recommend using data ingestion mode for effective search. This mode allows the layout parser to deeply process and index the entire document content. 

### What's next

- To create and configure a data store with Microsoft OneDrive, see Set up a Microsoft OneDrive data store 

(/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Microsoft OneDrive data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store

This page describes how to create a data store and connect Microsoft OneDrive to Gemini Enterprise. 

### Before you begin

**Note:** To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider (/gemini/enterprise/docs/configure-identity-provider). 

Ensure the following before you set up your Microsoft OneDrive connection. 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   - b. Locate the user account and click **Edit** . 

   - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Register Gemini Enterprise as an OAuth 2.0 application in Microsoft Entra ID (/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config) and obtain the following credentials (/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config#obtain-client-id-andclient-secret) 

: 

- Client ID 

Client secret 

Tenant ID 

3. Configure the Microsoft API application permissions 

(/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config#microsoft-graphminimum-permissions) 

with the consent of a Microsoft OneDrive administrator. 

### Create Microsoft OneDrive data store

To create a Microsoft OneDrive data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Microsoft OneDrive** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Connector mode** section, select **Data ingestion** or **Federated search** as the connection mode. 

   - b. Click **Continue** . 

   - c. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

      - i. Provide the following authentication details: 

         - **Client ID:** The unique identifier of the application registered in your organization's Microsoft Entra ID. 

- **Client secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID. 

- **Tenant ID:** The unique identifier for your organization in Microsoft Entra admin center. For more information, see Obtain client credentials 

(/gemini/enterprise/docs/connectors/ms-onedrive/third-partyconfig#obtain-client-id-and-client-secret) 

- **Microsoft OneDrive Environment Type:** Select the environment that hosts your Microsoft 365 tenant: 

   - Select **Standard** (the default) if you connect to standard commercial Microsoft 365 or Government Community Cloud (GCC). 

   - Select **US Government** if you connect to a Microsoft 365 US Government sovereign cloud (GCC High or DoD). 

**Note:** These settings apply only to Microsoft 365 US Government (sovereign cloud) customers. If you connect to a US Government cloud, use the matching combination; otherwise keep the defaults ( **Standard** and **Global** ): 

- **GCC** : Environment Type **Standard** , Cloud Environment **GCC** . 

- **GCC High** : Environment Type **US Government** , Cloud Environment **GCC High** . 

- **DoD** : Environment Type **US Government** , Cloud Environment **DoD** . 

If you selected **Data ingestion** with **Federated credentials** authentication method, copy the **Subject identifier** and use it to add federated credential for data ingestion 

(/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config#add-fedcredentials) 

- **Subject identifier:** The unique ID of the service account you plan to use. 

- If you selected **Federated search** , click **Login** and complete the Microsoft sign-in. 

d. Click **Continue** . 

- e. If you selected **Federated search** , do the following: 

   - i. In the **Destinations** section, enter the base URL for your Microsoft OneDrive site. 

   - ii. In the **Advanced options** section, 

      - i. Select your **Microsoft 365 Cloud Environment** : 

         - If you connect to a Microsoft 365 US Government instance, select the option that matches it: **GCC** , **GCC High** , or **DoD** . 

         - Otherwise, keep the default, **Global** . 

      - ii. Enter **Azure Tenant** , the tenant ID that you obtained when you created the Entra application. 

      - iii. You can refine the scope of your searches and actions by specifying which Microsoft OneDrive paths to include or exclude. You can only mutate or retrieve data within the included paths. Requests for out-of-scope data either fail or return no results. 

You can add filters to the data store using the Google Cloud console or API: 

ConsoleREST (#rest) (#console) 

Note: When entering multiple sites, separate each URL with a comma. You can also copy and paste a list of URLs directly from a CSV file. 

- i. In the Path filter section: 

Choose the filter type: **Include in search** or **Exclude from search** . 

In the **Path filter** field, enter the full OneDrive paths. 

**Note:** This field supports subpaths, folders, and document libraries, in the format, `https://{yourtenant}.sharepoint.com/sites/{your-sitename}/{your-folder-name}/` . Any content under the specified path will be filtered. 

For more details on filter types and adding filters, see Add filters to Microsoft OneDrive data store 

(/gemini/enterprise/docs/connectors/ms-onedrive/add-filters-to-onedrivedata-store) 

- f. If you selected **Data ingestion** , in the **Advanced options** section, do the following: 

   - i. Optional: To allow a set of static IP addresses in your system, select the **Enable Static IP Addresses** checkbox. For more information, see Configure static IP egress 

(/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

   - ii. Optional: In the **Max QPS** field, enter the maximum queries per second to apply a rate limit on the queries that the connector sends to the Microsoft OneDrive instance. 

   - iii. Optional: To attempt to decrypt all files encrypted with Microsoft Purview (https://learn.microsoft.com/en-us/purview/purview) information protection, select **Decrypt files encrypted with** **_Microsoft Purview_ information protection** checkbox. 

- g. Click **Continue** . 

- h. In the **Entities to search** (if you selected **Federated search** ) or **Entities to sync** (if you selected **Data ingestion** ) section: 

   - i. Select all the required entities. 

   - ii. If you selected **Federated search** , proceed to the next step. 

   - iii. If you selected **Data ingestion** , continue with the following steps: 

- i. Optional: To sync specific projects, do the following: 

   - i. Click **Filter** . 

   - ii. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included in the index, select the **Include to the index** checkbox. 

   - iii. Enter the keys. Press enter after each key. 

   - iv. Click **Save** . 

- ii. To configure the sync schedule, do the following: 

   - i. In the **Sync frequency** list, select the sync frequency. 

      - To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options** . 

   - ii. In the **Incremental sync frequency** list, select the incremental sync frequency. For more information, see Sync schedules 

(https://cloud.google.com/gemini/enterprise/docs/introduction-toconnectors-and-data-stores#sync-schedules) 

7. Click **Continue** . 

8. In the **Actions** section: 

   - a. If you selected **Federated search** : 

      - i. From **Select Microsoft OneDrive actions to enable** , select the actions from the category to enable them for the connector. 

   - b. If you selected **Data ingestion** : 

      - i. In the **Authentication settings** section, configure authentication based on your chosen connection mode. Provide the following authentication details: 

         - **Client ID:** The unique identifier of the application registered in your organization's Microsoft Entra ID. 

- **Client Secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID. 

- **Tenant ID:** The unique identifier for your organization in Microsoft Entra admin center. 

For more information, see Obtain client credentials 

(/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config#obtainclient-id-and-client-secret) 

- ii. Click **Login** and sign-in to Microsoft OneDrive to verify your account. 

- iii. Click **Continue** . 

- iv. In the **Advanced settings** section, enter **Azure Tenant** , the tenant ID that you obtained when you created the Entra application. 

- v. In the **Destinations** section, enter the base URL for your Microsoft OneDrive site. 

- vi. From **Select Microsoft OneDrive actions to enable** , select the actions from the category to enable them for the connector. 

9. Click **Continue** . 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

10. In the **Configuration** section: 

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

11. Click **Continue** . 

12. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

13. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Microsoft OneDrive connector is ready to be used. 

For an ingestion connector created with Microsoft OneDrive, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Microsoft OneDrive data store 

(/gemini/enterprise/docs/connect-existing-data-store), and authorize 

(/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to access Microsoft OneDrive before executing any queries. 

### Enable real-time sync for data ingestion

**Preview — Real-time sync** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

**Note:** Real-time sync is only available for the **Data ingestion** connection mode. 

To enable real-time sync for your data store, follow these steps. 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Click the name of the Microsoft OneDrive data store for which you want to enable real-time sync. 

4. On the data store **Data** page, wait until the **Connector state** changes to **Active** . 

5. In the **Real-time sync** field, click **View/edit** . 

6. To enable real-time sync, click the **Enable real-time sync** toggle. 

7. In the **Client secret** field, enter a value. This value is used to verify Microsoft OneDrive webhook events. We recommend using a string of 20 characters. 

8. Click **Save** . 

   - Wait for the **Real-time sync** field to change to **Running** . 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Microsoft OneDrive and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Microsoft API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Microsoft API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Microsoft OneDrive. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Microsoft API. 

### What's next

- To provide a user interface for querying your Microsoft OneDrive data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Microsoft OneDrive data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Add filters to a Microsoft OneDrive data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/add-filters-to-onedrive-data-store

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

This page explains how to add filters to your Microsoft OneDrive data stores in Gemini Enterprise. Filters determine which information is retrieved or excluded from the Microsoft OneDrive data store when users chat with the Assistant using the Gemini Enterprise app. 

### Filter types

You can configure the following filters within the `params` object of your data connector: 

- **Inclusion filter** **(** **`admin_filter` )** : Retrieves only specific information from the Microsoft OneDrive data store. 

- **Exclusion filter** **(** **`admin_exclusion_filter` )** : Excludes specific information from the Microsoft OneDrive data store. 

- **Legacy filter** **(** **`structured_search_filter` )** : Previously used to create a data store with filters using the API. 

### Filter keys

The filter parameters accept an object containing key-value pairs. The keys represent the Microsoft OneDrive fields you want to filter on, and the values are 

arrays of strings containing the criteria to match. When updating filters using the API, the following keys are supported: 

`FIL` Filter `TER` Description Supported URL examples name `_ KEY` Path `Pat` Filters search results and restricts actions to the • `https://tenant1-my. h` specific URL prefixes. Use this for granular control `sharepoint.com/personal/` to include or exclude specific sub-folders or files. `alice_company_com/` • `https://tenant1-my. sharepoint.com/personal/` • `https://tenant1. sharepoint.com/sites/ onboarding/Documents2/` • `https://tenant1-my. sharepoint.com/personal/ user_tenant1_com/Documents/ folder1` 

### Update filters in an existing data store

You can update filters in an existing data store using either the Google Cloud console or the API. 

ConsoleREST (#rest) (#console) 

To modify existing filter configurations: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Microsoft OneDrive data store. 

3. Click **View/edit parameters** . 

4. In the **View/edit parameters** panel, add or update the Microsoft OneDrive URLs and filter types. 

5. Click **Save** . 

### Exclude SharePoint content from OneDrive

By default, the Microsoft API returns both SharePoint and OneDrive content. To exclude SharePoint files from the search results, apply one of the following Path filters: 

#### Use an inclusion filter

If you are using inclusion filters, add the following URL to the inclusion filter list to restrict indexing to OneDrive-only data: 

```
https://{your-tenant}-my.sharepoint.com/personal/
```

#### Use an exclusion filter

If you are using exclusion filters, append the following URL to the exclusion filter list to exclude all SharePoint files from the search results: 

```
https://{your-tenant}.sharepoint.com/sites/
```

### Verify that the data store includes the filters

You can get the details of the data store to confirm that the filters you added or updated are correctly applied using the Google Cloud console or the API: 

ConsoleREST (#rest) (#console) 

To view the existing filter configurations: 

1. In the Google Cloud console > navigation menu, click **Data stores** . 

2. Select your Microsoft OneDrive data store. 

3. Click **View/edit parameters** . 

In the **View/edit parameters** panel, the existing filters applied to the data store are displayed. 

### What's next

- To provide a user interface for querying your Microsoft OneDrive data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Microsoft OneDrive data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions, see Manage actions 

- (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC.
