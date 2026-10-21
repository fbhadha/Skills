# Gemini Enterprise: connectors and data stores / Configure OAuth for Google Calendar to Gmail connector: overview
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 47-84, extracted 2026-10-18

Contains:
- Configure OAuth for Google Calendar (pages 47-48) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/config
- Google Chat connector: overview (pages 49-52) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat
- Set up a Google Chat data store (pages 53-57) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/set-up-data-store
- Configure OAuth for Google Chat (pages 58-59) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/config
- Add filters to a Google Chat data store (pages 60-62) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/add-filters-to-gchat-data-store
- Google Drive connector: overview (pages 63-66) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive
- Set up a Google Drive data store (pages 67-73) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/set-up-data-store
- Configure OAuth for Google Drive (pages 74-75) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/config
- Add filters to a Google Drive data store (pages 76-80) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/add-filters-to-gdrive-data-store
- Gmail connector: overview (pages 81-84) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail

## Configure OAuth for Google Calendar

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/config

The Google Calendar connector uses a Google-managed OAuth app to access your Google Calendar data. You don't need to enable Google Calendar APIs, create your own OAuth app, add OAuth scopes, or create OAuth client credentials. 

Depending on how your organization restricts OAuth app access, a Google Workspace administrator might need to add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the connector. For instructions, see Allowlist the Google-managed OAuth app (#allowlist-oauth-app). 

**Note:** Existing Google Calendar data stores that were configured with a customer-managed OAuth app continue to function. New Google Calendar data stores use the Google-managed OAuth app described on this page. 

### Allowlist the Google-managed OAuth app

If your Google Workspace organization restricts OAuth app access, a Google Workspace administrator must add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the Google Calendar connector. 

To add the OAuth app to the allowlist, follow these steps: 

1. Sign in to the Google Admin console (https://admin.google.com) as a Google Workspace administrator. 

2. Go to **Security** > **Access and data control** > **API controls** . 

3. Under **App access control** , click **Manage app access** . 

4. Click **Configure new app** > **OAuth App Name Or Client ID** . 

5. In the search field, enter the following Gemini Enterprise OAuth client ID: 

```
502998392228-hpelhql0ouj9ckiu3l39lllsir24b02s.apps.googleusercontent.com
```

6. Select the app from the search results and click **Select** . 

7. For the access level, select **Trusted** . For details on other access levels, see Control which apps access Google Workspace data 

(https://support.google.com/a/answer/7281227). 

8. Click **Continue** and then **Finish** to save the change. 

For more information about OAuth app allowlisting, see Control which third-party & internal apps access Google Workspace data (https://support.google.com/a/answer/7281227) in the Google Workspace Admin Help. 

Last updated 2026-10-14 UTC. 



## Google Chat connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

The Google Chat connector for Gemini Enterprise lets you search and perform actions on your Google Chat data using natural language commands. 

**Note:** Gemini Enterprise has released new Google Workspace data connectors for Google Chat, Google Drive, Gmail, and Google Calendar. The new connectors use a Google-managed OAuth app, so you no longer create your own OAuth client or supply a client ID and client secret when you create the data store. For Google Chat setup instructions, see Set up a Google Chat data store (/gemini/enterprise/docs/connectors/gchat/set-up-data-store). 

### Supported actions

When the Google Chat data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Send message|Sends a Google Chat message to a conversation.|

|Action|Description|
|---|---|
|Send message<br>(Markdown)|Sends a Google Chat message to a conversation with Markdown<br>formatting.|
|List messages|Retrieves messages from a specified Google Chat conversation (space,<br>direct message, or group direct message).|
|List messages<br>(Markdown)|Retrieves messages from a specified Google Chat conversation in<br>Markdown format.|
|Search messages|Searches for Google Chat messages using keywords and filters. Works<br>across all spaces the user has access to, or can be scoped to a specific<br>conversation.|
|Search<br>conversations|Searches for Google Chat conversations by display name.|
|Create<br>conversation|Creates a Google Chat conversation (named space, direct message, or<br>group direct message).|
|Add reaction|Adds a reaction to a Google Chat message.|
|Remove reaction|Removes a reaction from a Google Chat message.|
|Add membership|Adds a member to a Google Chat conversation.|
|Remove<br>membership|Removes a user membership from a Google Chat conversation.|
|Update<br>membership|Updates a user membership in a Google Chat conversation.|
|List memberships|Lists memberships in a Google Chat conversation.|

### Required permissions

The Google-managed OAuth app requests the following OAuth scopes. Users grant these scopes when they authorize the connector: 

|Scope|Purpose|
|---|---|
|`https://www.googleapis.com/auth/chat.`<br>`spaces.readonly`|List and search Google Chat conversations.|
|`https://www.googleapis.com/auth/chat.`<br>`messages.readonly`|Read and search Google Chat messages.|
|`https://www.googleapis.com/auth/chat.`<br>`memberships.readonly`|List memberships in a Google Chat<br>conversation.|
|`https://www.googleapis.com/auth/chat.`<br>`users.readstate.readonly`|Read the user's read state for Google Chat<br>messages.|
|`https://www.googleapis.com/auth/chat.`<br>`messages.create`|Send Google Chat messages.|
|`https://www.googleapis.com/auth/chat.`<br>`spaces.create`|Create Google Chat conversations.|
|`https://www.googleapis.com/auth/chat.`<br>`memberships`|Add, remove, and update members in a<br>Google Chat conversation.|
|`https://www.googleapis.com/auth/chat.`<br>`messages.reactions.create`|Add a reaction to a Google Chat message.|
|`https://www.googleapis.com/auth/chat.`<br>`messages.reactions`|Remove a reaction from a Google Chat<br>message.|

### Limitations

- The Google Chat data store is supported only in the `global` , `us` , and `eu` locations. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- If you use security controls, be aware of their limitations related to data in Google Chat, as discussed in the following table: 

|Security control|Note the following|
|---|---|
|Data Residency (DRZ)<br>(/gemini/enterprise/docs/locations|)<br>Gemini Enterprise only guarantees data residency in<br>Google Cloud. For information about data residency an<br>Google Chat, see Google Workspace compliance<br>guidance and documentation, including<br>Data regions fo<br>Google Workspace<br>(https://support.google.com/a/answer/9223653). Also<br>review examples like<br>Choose the region where data is<br>stored(https://support.google.com/a/topic/7631290) a<br>Digital sovereignty<br>(https://workspace.google.com/intl/en_in/security/digit<br>sovereignty/)<br>.|
|Customer-managed encryption<br>keys (CMEK)<br>(/gemini/enterprise/docs/cmek)|Your keys only encrypt data within Google Cloud. Cloud<br>Key Management Service controls don't apply to data<br>stored in Google Chat.|
|Access Transparency<br>(/gemini/enterprise/docs/access-<br>transparency)|Access Transparency logs actions taken by Google<br>personnel on the Google Cloud project. You'll also need<br>to review the Access Transparency logs created by<br>Google Workspace. For more information, see<br>Access<br>Transparency log events<br>(https://support.google.com/a/answer/9230979) in the<br>Google Workspace Admin Help documentation.|

### What's next

To create and configure a data store with Google Chat, see Set up a Google Chat data store (/gemini/enterprise/docs/connectors/gchat/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Google Chat data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/set-up-data-store

This page describes how to create a data store and connect Google Chat to Gemini Enterprise. 

### Before you begin

- Sign in to the Google Cloud console using the same account associated with the Google Workspace instance you intend to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Google Chat. Personal Google Accounts (consumer accounts ending in `@gmail.com` ) don't have a customer ID and aren't supported. 

- To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider 

- (/gemini/enterprise/docs/configure-identity-provider). 

- **Enable smart features** : In your Google Workspace account, turn on both **Smart features in Google Workspace** and **Smart features in other Google products** . For details, see Turn Google Workspace smart features on or off (https://support.google.com/mail/answer/15604322). 

- **Allowlist the OAuth app (Administrators only)** : The Google Chat data store uses a Google-managed OAuth app to access your data. If your organization restricts OAuth app access, your Google Workspace administrator must add this app to your organization's allowlist. For details, see Allowlist the Google-managed OAuth app 

- (/gemini/enterprise/docs/connectors/gchat/config#allowlist-oauth-app). 

### Create the Google Chat data store

To create the Google Chat data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create (/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click + **Create data store** . 

5. In the **Source** , search for **Google Chat** , and click **Select** . 

**Note:** Administrator filters (message recency and direct-message exclusion) are no longer supported for new Google Chat data stores. Data stores that were created before this change continue to work with their existing filters. To manage filters on those legacy data stores, see Add filters to a Google Chat data store 

(/gemini/enterprise/docs/connectors/gchat/add-filters-to-gchat-data-store). 

6. In the **Actions** section, choose the actions from the list to enable them for the Google Chat connector. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

(/gemini/enterprise/docs/manage-actions). 

7. Click **Continue** . 

8. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Select **Google-managed encryption key** or **Cloud KMS key** . If you selected **Cloud KMS key** : 

In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

9. Optional: In the **Tag** field, enter a stable identifier for the data store. This identifier is used across different versions of the connector and becomes immutable after the data store is created, so choose a value that you don't need to change later. 

10. Optional: In the **Sensitive Data Protection policy** section, attach an existing Sensitive Data Protection 

   - (/sensitive-data-protection/docs/sensitive-data-protection-overview) policy to inspect and de-identify data that Gemini Enterprise retrieves through this data store. If your organization doesn't require a Sensitive Data Protection policy, you can skip this step. 

11. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. When the data store state changes from **Creating** to **Active** , the Google Chat connector is ready to be used. 

After creating the data store, connect the data store you just created to an existing app or create a new app (/gemini/enterprise/docs/create-app) and connect 

(/gemini/enterprise/docs/connect-existing-data-store) it to the new app, and authorize (/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Google Chat before executing any queries. 

### Query Execution

**Note:** For optimal response quality when querying Google Chat data, we recommend using Gemini 3.1 version. 

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

After you authorize Google Chat and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Google Chat API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

### Error messages and troubleshooting

The following table describes common error messages that you might encounter when you work with the Google Chat connector, which includes possible HTTP error codes and suggested troubleshooting steps. 

|Error code|Error message|Description|Troubleshooting|
|---|---|---|---|
|403<br>(Permission<br>Denied)|Search by<br>using service<br>account<br>credentials<br>isn't supported<br>for Google<br>Workspace<br>data stores.|<br>The engine<br>being searched<br>has Google<br>Workspace data<br>stores, and the<br>credentials<br>passed are of a<br>service account.<br>Search by using<br>service account<br>credentials on<br>Google<br>Workspace data<br>stores isn't<br>supported.|Call search using user credentials, or remove<br>Google Workspace data stores from the engine.|
|403<br>(Permission<br>Denied)|Consumer<br>accounts<br>aren't<br>supported for<br>Google<br>Workspace<br>data stores.|Search is called<br>using a<br>consumer<br>account<br>(@gmail.com)<br>credential, which<br>isn't supported<br>for Google<br>Workspace data<br>stores.|<br>Remove Google Workspace data stores from the<br>engine or use a managed Google Account.|

|Error code|Error message|Description|Troubleshooting|
|---|---|---|---|
|403<br>(Permission<br>Denied)|Customer ID<br>mismatch for<br>data store|Search is only<br>allowed for users<br>who belong to<br>the same<br>organization as<br>Google<br>Workspace data<br>stores.|<br>Remove Google Workspace data stores from the<br>engine or contact support if the user and Google<br>Workspace data stores are meant to be in different<br>organizations.|
|403<br>(Permission<br>Denied)|Workspace<br>access for<br>Agent Space<br>disabled by<br>organization<br>administrator.|A Google<br>Workspace<br>administrator<br>has disabled<br>access to Google<br>Workspace data<br>for Gemini<br>Enterprise.|<br>Contact your Google Workspace administrator to<br>enable access<br>(https://support.google.com/a/answer/16479199).|

### What's next

- To provide a user interface for querying your Google Chat data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Google Chat data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Configure OAuth for Google Chat

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/config

The Google Chat connector uses a Google-managed OAuth app to access your Google Chat data. You don't need to enable Google Chat APIs, create your own OAuth app, add OAuth scopes, or create OAuth client credentials. 

Depending on how your organization restricts OAuth app access, a Google Workspace administrator might need to add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the connector. For instructions, see Allowlist the Google-managed OAuth app (#allowlist-oauth-app). 

**Note:** Existing Google Chat data stores that were configured with a customer-managed OAuth app continue to function. New Google Chat data stores use the Google-managed OAuth app described on this page. 

### Allowlist the Google-managed OAuth app

If your Google Workspace organization restricts OAuth app access, a Google Workspace administrator must add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the Google Chat connector. 

To add the OAuth app to the allowlist, follow these steps: 

1. Sign in to the Google Admin console (https://admin.google.com) as a Google Workspace administrator. 

2. Go to **Security** > **Access and data control** > **API controls** . 

3. Under **App access control** , click **Manage app access** . 

4. Click **Configure new app** > **OAuth App Name Or Client ID** . 

5. In the search field, enter the following Gemini Enterprise OAuth client ID: 

```
502998392228-hpelhql0ouj9ckiu3l39lllsir24b02s.apps.googleusercontent.com
```

6. Select the app from the search results and click **Select** . 

7. For the access level, select **Trusted** . For details on other access levels, see Control which apps access Google Workspace data 

(https://support.google.com/a/answer/7281227). 

8. Click **Continue** and then **Finish** to save the change. 

For more information about OAuth app allowlisting, see Control which third-party & internal apps access Google Workspace data (https://support.google.com/a/answer/7281227) in the Google Workspace Admin Help. 

Last updated 2026-10-14 UTC. 



## Add filters to a Google Chat data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gchat/add-filters-to-gchat-data-store

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

This page explains how to add filters to your Google Chat data stores in Gemini Enterprise. Filters determine which information is retrieved or excluded from the Google Chat data store when users chat with the Assistant using the Gemini Enterprise app. 

### Filter types

The Google Chat data store supports the following filter types: 

- **Message Recency** : This filter limits search results to a specific timeframe to ensure data relevance and reduce noise. For example, setting the value to 90 days will include only messages from the last 90 days in the index, automatically excluding older data. 

- **Exclude Direct Messages** : This filter excludes all private 1:1 direct messages from the search results. When enabled, the Google Chat data store only indexes content from multi-user spaces and group chats. 

### Update filters in an existing data store

You can update filters in an existing data store using either the Google Cloud console or the API. 

To modify existing filter configurations: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Google Chat data store. 

3. Click **View/edit parameters** . 

4. In the **View/edit parameters** panel, add or update the filter types. 

5. Click **Save** . 

### Remove filters from a data store

When managing your data store configuration, you may need to clear specific filters or reset filters entirely. You can remove filters from an existing data store using either the Google Cloud console or the API. 

ConsoleREST (#rest) (#console) 

To remove existing filter configurations: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Google Chat data store. 

3. Click **View/edit parameters** . 

4. In the **View/edit parameters** panel, delete the filter types. 

5. Click **Save** . 

### What's next

- To provide a user interface for querying your Google Chat data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Google Chat data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions, see Manage actions 

- (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Google Drive connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive

The Google Drive data store for Gemini Enterprise lets you search and perform actions on your Google Drive data, including files and folders. 

**Note:** Gemini Enterprise has released new Google Workspace data connectors for Google Drive, Gmail, Google Chat, and Google Calendar. The new connectors use a Google-managed OAuth app, so you no longer create your own OAuth client or supply a client ID and client secret when you create the data store. For Google Drive setup instructions, see Set up a Google Drive data store (/gemini/enterprise/docs/connectors/gdrive/set-up-data-store). 

### Supported actions

When the Google Drive data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Copy file|Copies a file in Google Drive.|
|Create file|Creates a new file in Google Drive.|
|Download file content|Downloads the content of a Google Drive file.|
|Get cell values|Reads cell values from a Google Sheets spreadsheet.|
|Get file metadata|Fetches metadata for a Google Drive file.|
|Get file permissions|Lists the permissions on a Google Drive file.|
|Get spreadsheet|Reads the contents and metadata of a Google Sheets spreadsheet.|
|Insert dimension|Inserts rows or columns into a Google Sheets spreadsheet.|
|List recent files|Lists recent files in Google Drive.|
|List shared drives|Lists shared drives in Google Drive.|
|Read document|Reads the contents of a Google Docs document.|

|Action|Description|
|---|---|
|Read file content|Reads the contents of a Google Drive file.|
|Read presentation|Reads the contents of a Google Slides presentation.|
|Search files|Searches for Google Drive files matching a query.|
|Share file|Shares a Google Drive file with one or more users.|
|Trash file|Moves a Google Drive file to the trash.|
|Update cell values|Writes cell values to a Google Sheets spreadsheet.|
|Update file|Updates an existing Google Drive file.|
|Update formulas|Writes formulas to a Google Sheets spreadsheet.|

**Note:** The maximum file size for file uploads and downloads in Gemini Enterprise is 75 MB. 

#### Required scopes

The Google-managed OAuth app requests the following OAuth scopes. Users grant these scopes when they authorize the connector: 

|Scope|Purpose|
|---|---|
|`https://www.googleapis.`<br>`com/auth/drive.readonly`|Search and retrieve Google Drive content. Lets the data store<br>list files and folders, view metadata, list permissions, and read<br>file content.|
|`https://www.googleapis.`<br>`com/auth/drive.metadata.`<br>`readonly`|Read Google Drive file metadata.|
|`https://www.googleapis.`<br>`com/auth/drive.file`|Create and update files that the user opens or creates with the<br>connector.|
|`https://www.googleapis.`<br>`com/auth/drive.appdata`|Store application-specific data in Google Drive.|

|Scope|Purpose|
|---|---|
|`https://www.googleapis.`<br>`com/auth/drive`|Perform write actions on Google Drive files (for example, copy,<br>share, trash, and update).|

### Limitations

- The Google Drive data store is supported only in the `global` , `us` , and `eu` locations. 

- If you use security controls, be aware of their limitations related to data in Google Drive, as discussed in the following table: 

|Security control|Note the following|
|---|---|
|Data Residency (DRZ)<br>(/gemini/enterprise/docs/locations|)<br>Gemini Enterprise only guarantees data residency in<br>Google Cloud. For information about data residency an<br>Google Drive, see Google Workspace compliance<br>guidance and documentation, including<br>Data regions fo<br>Google Workspace<br>(https://support.google.com/a/answer/9223653). Also<br>review examples like<br>Choose the region where data is<br>stored(https://support.google.com/a/topic/7631290) a<br>Digital sovereignty<br>(https://workspace.google.com/intl/en_in/security/digit<br>sovereignty/)<br>.|
|Customer-managed encryption<br>keys (CMEK)<br>(/gemini/enterprise/docs/cmek)|Your keys only encrypt data within Google Cloud. Cloud<br>Key Management Service controls don't apply to data<br>stored in Google Drive.|
|Access Transparency<br>(/gemini/enterprise/docs/access-<br>transparency)|Access Transparency logs actions taken by Google<br>personnel on the Google Cloud project. You'll also need<br>to review the Access Transparency logs created by<br>Google Workspace. For more information, see<br>Access<br>Transparency log events<br>(https://support.google.com/a/answer/9230979) in the<br>Google Workspace Admin Help documentation.|

### Common search issues

If your search doesn't return the file you're looking for, it might be due to one of the following search index limitations of Google Drive: 

- Google Drive only extracts 1 MB of text and formatting data from your file to make it searchable. Keywords exceeding the 1 MB index limit aren't searchable. 

- For most file types, file size cannot exceed 10 MB. The following are exceptions: 

   - XLSX files (.xlsx) cannot exceed 20 MB. 

   - PDF files (.pdf) cannot exceed 30 MB. 

   - Text files (.txt) cannot exceed 100 MB. 

**Note:** Files exceeding the size limit are not searchable and won't appear in your search results. 

- Optical character recognition in PDF files is limited to 80 pages. Google Drive doesn't index any PDF that is larger than 50 MB or 80 pages. 

### What's next

- To create and configure a data store with Google Drive, see Set up a Google Drive data store (/gemini/enterprise/docs/connectors/gdrive/set-up-data-store). 

Last updated 2026-10-15 UTC. 



## Set up a Google Drive data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/set-up-data-store

This page describes how to create a data store and connect Google Drive to Gemini Enterprise. This connection allows Gemini Enterprise to directly retrieve information from Google Drive. Because data is not copied into the Gemini Enterprise index, you don't need to manage data storage. 

### Before you begin

- You must be signed into the Google Cloud console with the same account that you use for the Google Drive instance that you plan to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Google Drive. Personal Google Accounts (consumer accounts ending in `@gmail.com` ) don't have a customer ID and aren't supported. 

- To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider 

- (/gemini/enterprise/docs/configure-identity-provider). 

- Verify that all the documents are accessible, either by placing them in a shared drive that is owned by the domain or by assigning the ownership to a user in the domain. 

- **Enable smart features** : In your Google Workspace account, turn on both **Smart features in Google Workspace** and **Smart features in other Google products** . For details, see Turn Google Workspace smart features on or off (https://support.google.com/mail/answer/15604322). 

- **Allowlist the OAuth app (Administrators only)** : The Google Drive data store uses a Google-managed OAuth app to access your data. If your organization restricts OAuth app access, your Google Workspace administrator must add this app to your organization's allowlist. For details, see Allowlist the Google-managed OAuth app 

- (/gemini/enterprise/docs/connectors/gdrive/config#allowlist-oauth-app). 

#### Create the Google Drive data store

**Note:** When using data federation, the Google Drive connector only searches documents that are owned by the domain of the user who performs the search. Before setting up this connector, verify that all documents are accessible, either by placing them in a shared drive that is owned this domain or by setting ownership to a user in this domain. 

1. In the Google Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create (/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Google Drive** , and click **Select** . 

6. Optional: In the **Data** section, configure filters that scope which Google Drive content the data store searches. To configure filters using the Google Cloud console or REST API, select one of the following options: 

ConsoleREST API (#rest-api) 

(#console) 

- a. In the **Shared Drive IDs** field, the **Folder IDs** field, or both, enter the IDs that you want to filter on. 

- b. For each field, choose **Include** to search only the specified IDs, or **Exclude** to omit them from search. Configure either **Include** mode or **Exclude** mode for each field, but not both. 

- c. To locate a folder ID or shared drive ID, open the folder or shared drive in Google Drive and copy the ID from the URL. The URL follows this format: `https://drive.google.com/drive/folders/` _`ID`_ . For example, 

`https://drive.google.com/drive/folders/123456789012345678901` . 

**Note:** Filters scope search results only. Data stores created with the previous scoping options continue to work with their existing configuration. For more details on filter types, and to add or change filters after the data store is created, see Add filters to a Google Drive data store 

(/gemini/enterprise/docs/connectors/gdrive/add-filters-to-gdrive-data-store). 

7. In the **Actions** section, choose the actions from the list to enable them for the Google Drive connector. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

(/gemini/enterprise/docs/manage-actions). 

8. Click **Continue** . 

9. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Select **Google-managed encryption key** or **Cloud KMS key** . If you selected **Cloud KMS key** : 

In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys (/gemini/enterprise/docs/cmek). 

10. Optional: In the **Tag** field, enter a stable identifier for the data store. This identifier is used across different versions of the connector and becomes immutable after the data store is created, so choose a value that you don't need to change later. 

11. Optional: In the **Sensitive Data Protection policy** section, attach an existing Sensitive Data Protection 

   - (/sensitive-data-protection/docs/sensitive-data-protection-overview) policy to inspect and de-identify data that Gemini Enterprise retrieves through this data store. If your organization doesn't require a Sensitive Data Protection policy, you can skip this step. 

12. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

To verify the state of the data store, do the following: 

1. Navigate to the connector in the data store list and monitor its state until it changes to **Active** . 

2. When the data store state changes from **Creating** to **Active** , the Google Drive connector is ready to be used. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app) and connect it to the Google Drive data store 

(/gemini/enterprise/docs/connect-existing-data-store) before executing the query. 

### Query execution

After you authorize Google Drive, when you enter a search query: 

1. Gemini Enterprise sends your search query to the Google Drive API. 

2. Gemini Enterprise blends the results with those from other sources and displays them. 

### Error messages and troubleshooting

The following table describes error messages, including HTTP error codes and suggested troubleshooting steps, that you might encounter when working with this Google data source. 

|Error code|Error message|Description|Troubleshooting|
|---|---|---|---|
|403<br>Permission<br>Denied|Searching<br>using service<br>account<br>credentials<br>isn't supported<br>for Google<br>Workspace<br>data stores.|<br>The engine being<br>searched has<br>Google<br>Workspace data<br>stores, and the<br>credentials<br>passed are of a<br>service account.<br>Searching using<br>service account<br>credentials on<br>Google<br>Workspace data<br>stores isn't<br>supported.|<br>Call search using user credentials, or remove<br>Google Workspace data stores from the engine.|
|403<br>Permission<br>Denied|Consumer<br>accounts<br>aren't<br>supported for<br>Google<br>Workspace<br>data stores.|Search is called<br>using a<br>consumer<br>account<br>(@gmail.com)<br>credential, which<br>isn't supported<br>for Google<br>Workspace data<br>stores.|<br>Remove Google Workspace data stores from the<br>engine or use a managed Google Account.|
|403<br>Permission<br>Denied|Customer id<br>mismatch for<br>data store|Search is only<br>allowed for users<br>who belong to<br>same<br>organization as<br>Google<br>Workspace data<br>stores.|<br>Remove Google Workspace data stores from the<br>engine or contact support if the user and Google<br>Workspace data stores are meant to be in different<br>organizations.|

|Error code|Error message|Description<br>Troubleshooting|
|---|---|---|
|403<br>Permission<br>Denied|Workspace<br>access for<br>Agentspace<br>disabled by<br>organization<br>administrator.|A Google<br>Workspace<br>administrator<br>has disabled<br>access to Google<br>Workspace data<br>for Gemini<br>Enterprise.<br>Contact your Google Workspace administrator to<br>enable access<br>(https://support.google.com/a/answer/16479199).|
|400<br>Invalid<br>Argument|Request<br>contains an<br>invalid<br>argument.|This error occurs if the data connector name in the request doesn't<br>meet the naming requirements. Verify the data connector name,<br>ensuring it is 1 to 63 characters long, starts with a lowercase letter,<br>ends with a lowercase letter or digit, and contains only lowercase<br>letters, digits, hyphens, or underscores. For example, use a name<br>like`cymbal-collection-123456789`instead of`123456789-cymbal-`<br>`collection`.|

For common search issues that you encounter when querying your Google Drive data, see Common search issues 

(/gemini/enterprise/docs/connectors/gdrive#common-search-issues). 

### What's next

- To provide a user interface for querying your data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Google Drive data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To add or update folder and shared drive filters on your data store, see Add filters to a Google Drive data store 

- (/gemini/enterprise/docs/connectors/gdrive/add-filters-to-gdrive-data-store). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

- If your app wasn't initially configured to include cross-domain documents, enable the **Include cross-domain documents** feature in the **Manage web** 

**app features** settings. For more information, see Manage web app features (/gemini/enterprise/docs/manage-web-app-features). 

Last updated 2026-10-15 UTC. 



## Configure OAuth for Google Drive

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/config

The Google Drive data store uses a Google-managed OAuth app to access your Google Drive data. You don't need to enable Google Drive APIs, create your own OAuth app, add OAuth scopes, or create OAuth client credentials. 

Depending on how your organization restricts OAuth app access, a Google Workspace administrator might need to add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the connector. For instructions, see Allowlist the Google-managed OAuth app (#allowlist-oauth-app). 

**Note:** Existing Google Drive data stores that were configured with a customer-managed OAuth app continue to function. New Google Drive data stores use the Google-managed OAuth app described on this page. 

### Allowlist the Google-managed OAuth app

If your Google Workspace organization restricts OAuth app access, a Google Workspace administrator must add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the Google Drive connector. 

To add the OAuth app to the allowlist, follow these steps: 

1. Sign in to the Google Admin console (https://admin.google.com) as a Google Workspace administrator. 

2. Go to **Security** > **Access and data control** > **API controls** . 

3. Under **App access control** , click **Manage app access** . 

4. Click **Configure new app** > **OAuth App Name Or Client ID** . 

5. In the search field, enter the following Gemini Enterprise OAuth client ID: 

```
502998392228-hpelhql0ouj9ckiu3l39lllsir24b02s.apps.googleusercontent.com
```

6. Select the app from the search results and click **Select** . 

7. For the access level, select **Trusted** . For details on other access levels, see Control which apps access Google Workspace data 

(https://support.google.com/a/answer/7281227). 

8. Click **Continue** and then **Finish** to save the change. 

For more information about OAuth app allowlisting, see Control which third-party & internal apps access Google Workspace data (https://support.google.com/a/answer/7281227) in the Google Workspace Admin Help. 

Last updated 2026-10-14 UTC. 



## Add filters to a Google Drive data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gdrive/add-filters-to-gdrive-data-store

This page explains how to add filters to your Google Drive data stores in Gemini Enterprise. Filters let you control which Google Drive content is available to the Assistant by restricting search to specific locations or explicitly excluding specific locations from search. 

**Important:** Google Drive filters apply only to search results. For details, see Action behavior with filters (#tool-behavior). 

### Filter types

The Google Drive data store supports the following filter types: 

- **Folder filter** : Limits search to a specific set of Google Drive folders. You configure this filter in one of two modes: 

   - **Include** : Search is scoped to only the folders that you list. Content in any other folder isn't included. 

   - **Exclude** : The folders that you list are explicitly removed from search. Content in all other folders remains available. 

- **Shared drive filter** : Limits search to a specific set of shared drives. You configure this filter in one of two modes: 

   - **Include** : Search is scoped to only the shared drives that you list. Content in any other shared drive isn't included. 

   - **Exclude** : The shared drives that you list are explicitly removed from search. Content in all other shared drives remains available. 

For each filter type, you configure the **Include** mode or **Exclude** mode, not both at the same time. 

Filters match nested content. Both keys match recursively: a file is in scope if the specified shared drive or folder appears in its ancestor chain. 

To find a folder ID or shared drive ID, open the folder or shared drive in Google Drive and copy the ID from the URL. The URL follows this format: `https://drive.google.com/drive/folders/` _`ID`_ . For example, `https://drive.google.com/drive/folders/123456789012345678901` . 

**Note:** Data stores created before this feature was released keep working with their original folder and shared drive scoping. They aren't affected by these filters. You can't migrate an existing data store to the filter modes described on this page. To use these modes, create a Google Drive data store. 

### Action behavior with filters

While a filter is active on the connection, the connector applies it to the **Search files** action only. 

- **Search files** returns only files that match the filter. The filter is combined with the user's search terms, so a user can't widen the scope through the query. 

- **All other Google Drive actions are unaffected by filters.** An enabled action other than **Search files** can still be applied to a file outside the filter if the user has permission to that file in Google Drive. 

**Note:** Filters only take effect on a data store that has the **Search files** action enabled. You choose which actions to enable when you create the data store, or later on the **Actions** page. If you rely on filters to scope what the assistant can reach, enable only **Search files** and leave the other actions disabled. For more information, see Manage actions (/gemini/enterprise/docs/connectors/manage-actions). 

File access is always governed by the user's Google Drive permissions. Filters never grant additional access. However, filters only restrict **Search files** results. Users can still reach out-of-scope files through other enabled actions if they have permission to those files in Google Drive. 

**Note:** Don't rely on Google Drive filters as a security or data-loss-prevention boundary. Use them to focus assistant search on the content that matters. To restrict which files users can reach at all, use Google Drive sharing permissions. 

### Limitations

- **Filters apply to search only.** See Action behavior with filters (#tool-behavior). 

- **Search indexing delay** : Recent changes to folders, such as moving files or creating new folders, can take a few moments to appear in search results. Until then, filters apply the file's previous folder location. 

- **Folder depth limit** : Searches might not find files nested deeper than 10 folder levels. 

### Update filters in an existing data store

You can update filters in an existing data store using the Google Cloud console or API. 

ConsoleREST (#rest) (#console) 

To add or update filter configurations: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Google Drive data store. 

3. Click **View/edit parameters** . 

4. In the **View/edit parameters** panel, add or update the folder filter and shared drive filter. For each filter, choose **Include** or **Exclude** mode and provide the folder IDs or shared drive IDs. 

5. Click **Save** . 

### Verify that the data store includes the filters

You can get the details of the data store to confirm that the filters you added or updated are correctly applied using the Google Cloud console or the API. 

ConsoleREST (#rest) (#console) 

To view the existing filter configurations: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Google Drive data store. 

3. Click **View/edit parameters** . 

In the **View/edit parameters** panel, the existing filters applied to the data store are displayed. 

### Remove filters from a data store

When managing your data store configuration, you might need to clear specific filters or reset all filters. You can remove filters from an existing data store using the Google Cloud console or API. 

ConsoleREST (#rest) (#console) 

To remove existing filter configurations: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Google Drive data store. 

3. Click **View/edit parameters** . 

4. In the **View/edit parameters** panel, delete the folder IDs or shared drive IDs from the filters that you want to remove. 

5. Click **Save** . 

### What's next

- To provide a user interface for querying your Google Drive data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Google Drive data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-15 UTC. 



## Gmail connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail

The Gmail connector for Gemini Enterprise lets you search and perform actions on your Gmail data using natural language commands. 

**Note:** Gemini Enterprise has released new Google Workspace data connectors for Gmail, Google Drive, Google Chat, and Google Calendar. The new connectors use a Googlemanaged OAuth app, so you no longer create your own OAuth client or supply a client ID and client secret when you create the data store. For Gmail setup instructions, see Set up a Gmail data store (/gemini/enterprise/docs/connectors/gmail/set-up-data-store). 

### Supported actions

When the Gmail data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Send message|Sends a new Gmail message.|
|Reply|Replies to an existing Gmail message.|
|Forward|Forwards an existing Gmail message.|
|Create draft|Creates a new Gmail draft.|
|Update draft|Updates an existing Gmail draft.|
|List drafts|Lists Gmail drafts in the user's mailbox.|
|List threads|Lists Gmail threads in the user's mailbox.|
|Search threads|Searches for Gmail threads matching a query.|
|Get thread|Fetches the full contents of a Gmail thread.|
|Get message<br>attachment|Fetches metadata for an attachment on a Gmail message.|

|Action|Description|
|---|---|
|Create label|Creates a new label in Gmail.|
|Update label|Updates an existing Gmail label.|
|Delete label|Deletes an existing Gmail label.|
|List labels|Lists labels defined in the user's Gmail mailbox.|
|Label message|Adds one or more existing labels to a specific Gmail message.|
|Unlabel message|Removes one or more existing labels from a specific Gmail message.|
|Batch label messages|Adds one or more labels to multiple Gmail messages in a single<br>request.|
|Batch unlabel<br>messages|Removes one or more labels from multiple Gmail messages in a single<br>request.|
|Label thread|Adds one or more existing labels to a specific Gmail thread.|
|Unlabel thread|Removes one or more existing labels from a specific Gmail thread.|
|Batch label threads|Adds one or more labels to multiple Gmail threads in a single request.|
|Batch unlabel threads|Removes one or more labels from multiple Gmail threads in a single<br>request.|
|Create filter|Creates a new Gmail filter.|
|List filters|Lists Gmail filters in the user's mailbox.|
|Delete filter|Deletes an existing Gmail filter.|

**Notes** : 

The maximum file size for file uploads and downloads in Gemini Enterprise is 50 MB. 

#### Required scopes

The Google-managed OAuth app requests the following OAuth scopes. Users grant these scopes when they authorize the connector: 

|Scope|Purpose|
|---|---|
|`https://www.googleapis.com/auth/gmail.readonly`|Search and read Gmail messages,<br>threads, drafts, labels, and<br>attachments.|
|`https://www.googleapis.com/auth/gmail.send`|Send and forward Gmail messages and<br>replies.|
|`https://www.googleapis.com/auth/gmail.compose`|Create and update Gmail drafts.|
|`https://www.googleapis.com/auth/gmail.modify`|Add and remove labels on Gmail<br>messages and threads.|
|`https://www.googleapis.com/auth/gmail.labels`|Create, update, and delete Gmail<br>labels.|
|`https://www.googleapis.com/auth/gmail.`<br>`settings.basic`|Create, list, and delete Gmail filters.|

`https://www.googleapis.com/auth/userinfo.email` ,Identify the authorizing user. `https://www.googleapis.com/auth/userinfo. profile` , `openid` 

### Limitations

- The Gmail data store is supported only in the `global` , `us` , and `eu` locations. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- If you use security controls, be aware of their limitations related to data in Gmail, as discussed in the following table: 

|Security control|Note the following|
|---|---|

|Data Residency (DRZ)<br>(/gemini/enterprise/docs/locations<br>Customer-managed encryption<br>keys (CMEK)<br>(/gemini/enterprise/docs/cmek)|)<br>Gemini Enterprise only guarantees data residency in<br>Google Cloud. For information about data residency an<br>Gmail, see Google Workspace compliance guidance an<br>documentation, including<br>Data regions for Google<br>Workspace<br>(https://support.google.com/a/answer/9223653). Also<br>review examples like<br>Choose the region where data is<br>stored(https://support.google.com/a/topic/7631290) a<br>Digital sovereignty<br>(https://workspace.google.com/intl/en_in/security/digit<br>sovereignty/)<br>.<br>Your keys only encrypt data within Google Cloud. Cloud<br>Key Management Service controls don't apply to data<br>stored in Gmail.|
|---|---|
|Access Transparency<br>(/gemini/enterprise/docs/access-<br>transparency)|Access Transparency logs actions taken by Google<br>personnel on the Google Cloud project. You'll also need<br>to review the Access Transparency logs created by<br>Google Workspace. For more information, see<br>Access<br>Transparency log events<br>(https://support.google.com/a/answer/9230979) in the<br>Google Workspace Admin Help documentation.|

### What's next

To create and configure a data store with Gmail, see Set up a Gmail data store (/gemini/enterprise/docs/connectors/gmail/set-up-data-store). 

Last updated 2026-10-15 UTC.
