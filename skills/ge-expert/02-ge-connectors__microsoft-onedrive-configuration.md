# Gemini Enterprise: connectors and data stores / Microsoft OneDrive configuration to SharePoint connector: overview
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 455-494, extracted 2026-10-18

Contains:
- Microsoft OneDrive configuration (pages 455-460) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config
- Outlook connector: overview (pages 461-468) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook
- Set up a Microsoft Outlook data store (pages 469-478) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/set-up-data-store
- Microsoft Outlook configuration (pages 479-486) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/third-party-config
- SharePoint connector: overview (pages 487-494) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint

## Microsoft OneDrive configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-onedrive/third-party-config

This page describes how to set up and configure a third-party configuration before creating the OneDrive data store. 

### Set up authentication and permissions

You must set up authentication and permissions in Microsoft 365. This is crucial for allowing the connector to access and synchronize data. The OneDrive connector supports various authentication methods, such as OAuth client credentials or API tokens. 

#### Register Microsoft Entra app for Microsoft OneDrive connector

You must set up an Entra application registration to enable secure access to Microsoft OneDrive before you can create the connector in Gemini Enterprise. 

To register Gemini Enterprise as an OAuth 2.0 application in Entra, do the following: 

1. Navigate to Microsoft Entra admin center (https://entra.microsoft.com). 

2. In the navigation menu, expand the **Entra ID** and select **App registrations** . 

3. On the **App registrations** page, click **New registration** . 

4. On the **Register an application** page, do the following: 

   - a. In the **Name** field, enter a name for your app. 

   - b. In the **Supported account types** section, select **Accounts in this organizational directory only** . 

   - c. In the **Redirect URI** section, do the following: 

      - i. In the platform list, select `Web` . 

      - ii. In the redirect URI field, enter 

         - `https://vertexaisearch.cloud.google.com/console/oauth/default_o auth.html` . 

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

6. In the **Subject identifier** field, enter the value that you get from the Google Cloud console. This value is generated during the Microsoft OneDrive data store creation 

(/gemini/enterprise/docs/connectors/ms-onedrive/set-up-data-store#create-data-store) in the data section. 

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

Obtain Tenant ID 

Your tenant ID can be found in the **Tenant ID** box on the overview page (https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView) in the Microsoft Entra admin center. 

#### Configure Microsoft API permissions

To configure the required API permissions for the app, do the following: 

1. Navigate to the app page. 

2. In the app navigation menu, select **API permissions** . 

3. Click **Add permissions** . 

4. In the **Request API permissions** pane, select **Microsoft Graph** . 

5. Search for and select the following permissions based on your connection mode: 

|Connection<br>mode|Type|Scope|Purpose|
|---|---|---|---|
|Federated<br>search|Delegated|`Files.`<br>`Read.All`|Allows the data store to read all files that the user can<br>access.|
||Delegated|`Sites.`<br>`Read.All`|Allows the data store to read documents and list items in<br>all site collections that the user can access.|
||Delegated|`User.`<br>`Read.All`|Allows the data store to resolve user drive locations for<br>content discovery.|
|Data<br>ingestion|Application|`Files.`<br>`Read.All`|Allows the data store to read and synchronize files across<br>the organization without a signed-in user.|
||Application|`Group.`<br>`Read.All`|Allows the data store to read properties and memberships<br>of all groups.|
||Application|`Group`<br>`Member.`<br>`Read.All`|Allows the data store to read memberships for all groups<br>to manage access control (ACL) syncing.|
||Delegated|`User.`<br>`Read`|Allows the data store to read the profile and basic<br>company information of signed-in users.|
||Application|`Sites.`<br>`Full`<br>`Control.`<br>`All`|Allows full control of all site collections.|
||Application|`Sites.`<br>`Selected`|Allows access to a specific subset of site collections.|
||Federated<br>credentials<br>only|`User.`<br>`Read.All`|Allows the data store to read user profiles.|
||Delegated|`User.`<br>`Read`<br>`Basic.`<br>`All`|Allows reading a basic set of profile properties for users in<br>the organization.|

|Connection<br>mode|Type|Scope|Purpose|
|---|---|---|---|
|Actions|Delegated|`Files.`<br>`Read`<br>`Write.`<br>`App`<br>`Folder`|Allows the data store to read, create, update and delete<br>files in the Microsoft OneDrive folder.|
||Delegated|`Files.`<br>`Read`<br>`Write`|Allows the data store to read, download, create, upload,<br>update, and delete the files that the user can access.|
||Delegated|`Files.`<br>`Read`<br>`Write.`<br>`All`|Allows the data store to read and update files across all<br>drives the user has access to. Required for the file and<br>folder mutation actions (copy, move, rename, share,<br>update properties) that operate on files stored in drives<br>beyond the user's own Microsoft OneDrive.|

6. Click **Add Permissions** . 

7. Grant administrator consent. For information about how to grant consent, see Grant tenant-wide administrator consent to an application 

   - (https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent? pivots=portal) 

in the Microsoft Entra documentation. 

### Troubleshooting

This section describes how to resolve common issues with the Microsoft OneDrive connector. 

#### Users see "Need admin approval" when they connect

When users connect to Microsoft OneDrive from the Gemini Enterprise web app for the first time, Microsoft might show a **Need admin approval** screen. This happens if Gemini Enterprise requests administrator-level permissions, or if your Microsoft Entra tenant prohibits users from authorizing third-party apps without prior tenant-wide administrator consent. 

To resolve this issue, an administrator must complete the first authorization. After that, other users in your tenant can connect without the approval screen. 

1. Ask a Microsoft Entra ID administrator who can grant tenant-wide consent to sign in to the Gemini Enterprise web app and connect to Microsoft OneDrive. 

2. On the permissions screen, have the administrator select **Consent on behalf of your organization** , and then click **Accept** . 

3. Ask users to connect again. 

For more information, see Grant tenant-wide admin consent (https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent? pivots=portal) 

in the Microsoft Entra documentation. 

**Note:** Deleting and re-creating the data store doesn't resolve this issue, because consent is granted in your Microsoft Entra tenant, not to the data store. 

Last updated 2026-10-14 UTC. 



## Outlook connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook

The Microsoft Outlook data store for Gemini Enterprise lets you search and perform actions on your emails, calendars, contacts, and Microsoft 365 files (Excel workbooks, Word documents, and PowerPoint presentations) stored in OneDrive and SharePoint. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported Microsoft Outlook versions

The Microsoft Outlook data store supports Microsoft Graph API v1.0 with IDP integration. 

### Supported actions

When the Microsoft Outlook data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create contact|Creates a new contact in Microsoft Outlook.|
|Create event|Creates a new event.|
|Download|Downloads an attachment from a Microsoft Outlook email message.|
|attachments||
|Send mail|Sends an email message. This includes sending email with attachments.|

|Action|Description|
|---|---|
|Add attachments|Adds one or more attachments to an existing draft email message.|
|Create message|Creates a new draft email message in the signed-in user's mailbox.|
|Forward mail|Forwards an existing email message to one or more recipients.|
|Move mail|Moves an email message to a different mail folder in the signed-in user's<br>mailbox.|
|Reply to message|Sends a reply to an existing email message in the signed-in user's<br>mailbox.|
|Update message|Updates an existing draft email message in the signed-in user's mailbox.|
|Update contact|Updates an existing contact in Microsoft Outlook.|
|Update event|Updates an existing event.|
|Read Excel data|Lists workbooks, reads worksheets, tables, and rows from Excel (.xlsx)<br>files stored in OneDrive or SharePoint.|
|Edit Excel data|Adds and updates rows, creates worksheets and tables, and adds key<br>columns in Excel (.xlsx) files stored in OneDrive or SharePoint.|
|Create Word<br>document|Creates a new Word (.docx) document in the user's OneDrive.|
|Convert Word<br>document to PDF|Converts a Word (.docx) document stored in OneDrive or SharePoint to<br>PDF.|
|Create PowerPoint<br>presentation|Creates a new PowerPoint (.pptx) presentation in the user's OneDrive.|
|Convert PowerPoint<br>PDF|to<br>Converts a PowerPoint (.pptx) presentation stored in OneDrive or<br>SharePoint to PDF.|
|Create calendar|Creates a new calendar for the signed-in user.|
|Update calendar|Updates an existing calendar for the signed-in user.|
|RSVP to event|Responds (accept, decline, or tentatively accept) to a calendar event<br>invitation.|
|**Notes**:||

- Additional read-only actions are also available. 

- The maximum file size for file uploads and downloads in Gemini Enterprise is 25 MB. 

- Excel, Word, and PowerPoint actions require additional Microsoft Graph API permissions on the OneDrive or SharePoint files that the user is working with. For details, see [Required permissions](#required-permissions). 

#### Required permissions

The following table outlines the permissions required for Microsoft Outlook search and actions. 

|Connection<br>mode|Permission Purpose|
|---|---|
|Federated<br>search|`Mail.Read`<br>`Mail.`<br>`Read.`<br>(Delegated) Allows the data store to read the signed-in user's<br>mailbox, email from shared mailboxes, calendar events, and<br>contacts.|
||`Shared`|
||`Calendars`|
||`.Read`|
||`Contacts.`|
||`Read`|

|Connection<br>mode|Permission Purpose|
|---|---|
|Data<br>ingestion|`Calendars`<br>`.Read`<br>(Application) Allows the data store to read events of all calendars.|
||`Calendars`<br>`.Read`<br>`Basic.All`<br>(Application) Allows the data store to read events of all calendars,<br>except for properties such as body, attachments, and extensions.|
||`Contacts.`<br>`Read`<br>(Application) Allows the data store to read all contacts in all<br>mailboxes.|
||`Mail.Read`(Application) Allows the data store to read mail in all mailboxes.|
||`Mail.Read`<br>`Basic`<br>(Application) Allows the data store to read basic mail properties in all<br>mailboxes. Includes all properties except body, previewBody,<br>attachments and any extended properties.|
||`Mail.Read`<br>`Basic.All`<br>(Application) Allows the data store to read basic mail properties in all<br>mailboxes. Includes all properties except body, previewBody,<br>attachments and any extended properties.|
||`User.Read`(Delegated) Allows the data store to read the profile of signed-in<br>users.|
||`User.`<br>`Read.All`<br>(Application) Allows the data store to read the full set of profile<br>properties, reports, and managers of other users in your organization.|
||`User.Read`<br>`Basic.All`<br>(Application) Allows the data store to read a basic set of profile<br>properties of other users in your organization.|

|Connection<br>mode|Permission|Purpose|
|---|---|---|
|Actions|`Mail.Send`<br>`Mail.Read`<br>`Write`<br>`Calendars`<br>`.Read`<br>`Write`<br>`Contacts.`<br>`ReadWrite`<br>`User.Read`|(Delegated) Allows the data store to send mail as users in the<br>organization.<br><br>(Delegated) Allows the data store to create, read, update, move, and<br>delete messages, and add attachments to messages. Required for<br>the **Add attachments**, **Create message**, **Update message**,<br>and **Move mail** actions.<br><br>(Delegated) Allows the data store to create, read, update, and delete<br>events in user calendars.<br><br><br>(Delegated) Allows the data store to create, read, update, and delete<br>user contacts.<br>(Delegated) Allows the data store to read the profile of signed-in<br>users.|
|File<br>productivity<br>(Excel, Word,<br>PowerPoint)|`Files.`<br>`Read.All`|(Delegated) Sufficient only for tools that read file metadata or<br>download file content: listing Excel workbooks, reading Excel<br>workbook metadata, and converting Word (.docx) or PowerPoint<br>(.pptx) documents to PDF. Reads all files the user can access,<br>including files stored in SharePoint sites the user has access to. Not<br>sufficient for Excel workbook content operations (see next row).|
||`Files.`<br>`Read`<br>`Write.All`<br>`User.Read`|(Delegated) Required for all Excel workbook content operations (read<br>and write), including get worksheets, get tables, get rows, get row,<br>create worksheets and tables, add and update rows, and add key<br>columns. Per the Microsoft Graph API reference for these endpoints<br>(for example,<br>worksheet-list<br>(https://learn.microsoft.com/graph/api/worksheet-list),<br>table-list<br>(https://learn.microsoft.com/graph/api/table-list),<br>tablerow-list<br>(https://learn.microsoft.com/graph/api/tablerow-list)), the accepted<br>delegated permission is`Files.ReadWrite`.`Files.ReadWrite.All`<br>grants the same capability across all drives the user can access<br>(personal OneDrive and any SharePoint document library the user<br>has access to). Also required for creating Word and PowerPoint<br>documents in the user's OneDrive.<br>(Delegated) Required to resolve the signed-in user's OneDrive<br>location for file operations.|

|Connection<br>mode|Permissio|n Purpose|
|---|---|---|
|Tasks|`Tasks.`|(Delegated) Required for read operations on the signed-in user's|
|(Outlook to-<br>do lists and<br>tasks)|`Read`<br>`Tasks.`<br>`ReadWri`|Outlook task lists and tasks (list task lists, list tasks, get task).<br>`te`<br>(Delegated) Required for write operations: creating, updating, and<br>deleting tasks in the signed-in user's Outlook task lists.|
|Users and|`User.Re`|`ad`<br>(Delegated) Required for tools that enumerate or look up profiles of|
|directory|`Basic.A`|`ll`<br>other users in the organization (Get User, List Users, and tools that|
|(delegated<br>enumeration)||operate on other users' mailboxes or calendars).|

**Note:** The file-productivity actions above require the user's tenant admin to grant the corresponding Microsoft Graph API permissions on the OAuth app registration. If these permissions are not granted, requests to Excel, Word, and PowerPoint tools fail with an HTTP 403 **`accessDenied`** error. **Recommended:** grant **`Files.ReadWrite.All`** , which covers every fileproductivity tool. If you only need Word or PowerPoint PDF conversion and Excel workbook listing/metadata (no worksheet, table, or row access), **`Files.Read.All`** alone is sufficient. For the driveItem-based operations (Word/PowerPoint PDF conversion, listing Excel workbooks, reading Excel workbook metadata), Microsoft Graph also documents **`Sites.Read.All`** or **`Sites.ReadWrite.All`** as accepted alternatives (see driveItem-get (https://learn.microsoft.com/graph/api/driveitem-get) and driveItem-get-content-format (https://learn.microsoft.com/graph/api/driveitem-get-content-format)). See Configure Microsoft Outlook and set the necessary permissions (/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#configure-apipermissions) 

for the setup steps. 

**Note:** Missing **`Tasks.Read`** or **`Tasks.ReadWrite`** causes Outlook task tools to fail with HTTP 403 **`notAllowed`** . Missing **`User.ReadBasic.All`** (delegated) causes user-lookup tools to fail with HTTP 403 **`Authorization_RequestDenied`** . Tenants that need higher-privileged user access can substitute **`User.Read.All`** or **`Directory.Read.All`** for **`User.ReadBasic.All`** . 

For information on how to add the permissions for Microsoft Outlook, see Configure Microsoft Outlook and set the necessary permissions 

(/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#configure-api-permissions). 

### Rate limits for data ingestion

The request volume limit is 10,000 API requests per 10-minute period. These rate limits apply exclusively to the Microsoft Outlook data store when you choose to use ingestion as the connection mode. 

### Limitations

This section outlines known issues and limitations that may affect your use of the Microsoft Outlook data store. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Microsoft Outlook data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Microsoft Outlook data store is supported only in the `global` , `us` , and `eu` locations. 

- The Microsoft Outlook data store can process one transaction per second, per node, and throttles any transactions beyond this limit. 

- The Microsoft Outlook data store's ability to retry on rate-limit exceeded errors depends on receiving a _retry-after_ value from the Microsoft Graph API, which is only provided for the Outlook data store. The default number of retry attempts is three. 

- The Microsoft Outlook data store's throughput is limited by API call restrictions imposed by Microsoft Graph. Limits apply to each app ID and mailbox combination—that is, a specific app accessing a specific user or group mailbox. Exceeding the limit for one mailbox doesn't affect the ability of the application to access another mailbox. 

- The Microsoft Outlook data store maps one-to-one with a single Azure Tenant ID. It can't span multiple, isolated Microsoft 365 tenants within a Multi-Tenant Organization (MTO). You must create a dedicated data store for each distinct tenant. 

- Mailboxes must be fully migrated to Exchange Online. Mailboxes hosted onpremise in a Hybrid Exchange environment aren't accessible through the Microsoft Graph API. Attempts to query these or cross-tenant mailboxes can result in a `MailboxNotEnabledForRESTAPI` error. 

- The Microsoft Outlook data store can process one transaction per second per node and throttles any transactions beyond this limit. 

### What's next

- To create and configure a data store with Microsoft Outlook, see Set up a Microsoft Outlook data store 

- (/gemini/enterprise/docs/connectors/ms-outlook/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Microsoft Outlook data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/set-up-data-store

This page describes how to create a data store and connect Microsoft Outlook to Gemini Enterprise. 

### Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have configured your identity provider 

(/gemini/enterprise/docs/configure-identity-provider). 

Ensure the following before you set up your Microsoft Outlook federated connection. 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   - b. Locate the user account and click **Edit** . 

   - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

      - (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Plan your multi-tenant architecture (if applicable): If your organization spans multiple isolated Microsoft 365 tenants (a Multi-Tenant Organization (https://learn.microsoft.com/en-us/entra/identity/multi-tenant-organizations/overview)), you need to create a dedicated data store for each distinct Azure Tenant ID. 

To prevent browser session conflicts across tenants during the data store creation process, you must plan to use **Federated credentials** for authentication. For configuration details, see Add federated credential for data 

ingestion 

(/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#add-fed-credentials). 

3. Register Gemini Enterprise as an OAuth 2.0 application in Microsoft Entra ID (/gemini/enterprise/docs/connectors/ms-outlook/third-party-config) and obtain the following credentials 

(/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#obtain-client-id-andclient-secret) 

: 

      - Client ID 

      - Client secret 

      - Tenant ID 

4. Configure the Microsoft API permissions 

   - (/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#configure-apipermissions) 

with the consent of a Microsoft Outlook administrator. 

### Create the Microsoft Outlook data store

To create the Microsoft Outlook data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Microsoft Outlook** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Connector mode** section, select **Data ingestion** or **Federated search** as the connection mode. 

- b. Click **Continue** . 

- c. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

   - i. Provide the following authentication details as necessary: 

      - **Client ID:** The unique identifier of the application registered in your organization's Microsoft Entra ID. 

      - **Client secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID. 

      - **Tenant ID:** The unique identifier for your organization in Microsoft Entra admin center. For more information, see Obtain client credentials 

(/gemini/enterprise/docs/connectors/ms-outlook/third-partyconfig#obtain-client-id-and-client-secret) 

- **Microsoft Outlook Environment Type:** Select the environment that hosts your Microsoft 365 tenant: 

   - Select **Standard** (the default) if you connect to standard commercial Microsoft 365 or Government Community Cloud (GCC). 

   - Select **US Government** if you connect to a Microsoft 365 US Government sovereign cloud (GCC High or DoD). 

**Note:** These settings apply only to Microsoft 365 US Government (sovereign cloud) customers. If you connect to a US Government cloud, use the matching combination; otherwise keep the defaults ( **Standard** and **Global** ): 

- **GCC** : Environment Type **Standard** , Cloud Environment **GCC** . 

- **GCC High** : Environment Type **US Government** , Cloud Environment **GCC High** . 

**DoD** : Environment Type **US Government** , Cloud Environment **DoD** . 

      - If you selected **Data ingestion** with **Federated credentials** authentication method, copy the **Subject identifier** and use it to add federated credential for data ingestion 

      - (/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#add-fedcredentials) 

            - **Subject identifier:** The unique ID of the service account you plan to use. 

      - If you selected **Federated Search** , click **Login** and complete the Microsoft sign-in. 

- d. Click **Continue** . 

- e. In the **Advanced options** section: 

      - Select your **Microsoft 365 Cloud Environment** : 

            - If you connect to a Microsoft 365 US Government instance, select the option that matches it: **GCC** , **GCC High** , or **DoD** . 

            - Otherwise, keep the default, **Global** . 

      - If you selected **Federated search** , in the **Azure Tenant** field, enter the tenant ID that you obtained when you created the Entra application. 

      - If you selected **Data ingestion** : 

         - i. Optional: To allow a set of static IP addresses in your system, select the **Enable Static IP Addresses** checkbox. For more information, see Configure static IP egress 

            - (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

         - ii. Optional: In the **Max QPS** field, enter the maximum queries per second to apply a rate limit on the queries that the connector sends to the Outlook instance. 

- f. In the **Entities to search** (if you selected **Federated search** ) or **Entities to sync** (if you selected **Data ingestion** ) section: 

   - i. Select all the required entities. 

   - ii. If you selected **Federated search** , proceed to the next step. 

iii. If you selected **Data ingestion** , continue with the following steps: 

- i. Optional: To sync specific projects, do the following: 

   - i. Click **Filter** . 

   - ii. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included in the index, select the **Include to the index** checkbox. 

   - iii. Enter the keys. Press enter after each key. 

   - iv. Click **Save** . 

- ii. To configure the sync schedule, do the following: 

   - i. In the **Sync frequency** list, select the sync frequency. 

      - To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options** . 

ii. In the **Incremental sync frequency** list, select the incremental sync frequency. For more information, see Sync schedules 

(https://cloud.google.com/gemini/enterprise/docs/introduction-toconnectors-and-data-stores#sync-schedules) 

7. Click **Continue** . 

8. In the **Actions** section: 

   - If you selected **Federated search** : 

      - a. From **Select Microsoft Outlook actions to enable** , select the actions from the category to enable them for the connector. 

If you selected **Data ingestion** : 

- a. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

- b. Provide the following authentication details as necessary: 

- **Client ID:** The unique identifier of the application registered in your organization's Microsoft Entra ID. 

- **Client Secret:** The secret key generated during the OAuth 2.0 application registration process in Microsoft Entra ID. 

- **Tenant ID:** The unique identifier for your organization in Microsoft Entra admin center. 

For information on how to obtain authentication credentials, see Obtain client credentials 

(/gemini/enterprise/docs/connectors/ms-outlook/third-party-config#obtainclient-id-and-client-secret) 

   - . For information on the required scopes, see Required permissions 

   - (/gemini/enterprise/docs/connectors/ms-outlook#required-permissions). 

- c. Click **Login** and sign-in to Microsoft Outlook to verify your account. 

- d. Click **Continue** . 

- e. In the **Advanced options** section: 

      - i. Enter **Azure Tenant** , the tenant ID that you obtained when you created the Entra application. 

- f. From **Select Microsoft Outlook actions to enable** , select the actions from the category to enable them for the connector. 

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

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Microsoft Outlook connector is ready to be used. 

For an ingestion connector created with Microsoft Outlook, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Microsoft Outlook data store 

(/gemini/enterprise/docs/connect-existing-data-store), and authorize 

(/gemini/enterprise/docs/connect-existing-data-store#user_authorization) Gemini Enterprise to access Microsoft Outlook before executing any queries. 

### Enable real-time sync

**Preview — Real-time sync** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

**Note:** Real-time sync is only available for the **Data ingestion** connection mode. 

Real-time sync only syncs document entities and doesn't sync data related to identity entities. The following table shows which document events are supported with real-time sync. 

<!-- Start of picture text -->
Outlook entities Create Update Delete Permission change<br>Email<br>Email attachments<br>Calendar<br>Contacts<br><!-- End of picture text -->

To enable real-time sync for your data store, follow these steps. 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Click the name of the Microsoft Outlook data store for which you want to enable real-time sync. 

4. On the data store **Data** page, wait until the **Connector state** changes to **Active** . 

5. In the **Real-time sync** field, click **View/edit** . 

6. To enable real-time sync, click the **Enable real-time sync** toggle. 

7. In the **Client secret** field, enter a value. This value is used to verify Microsoft Outlook webhook events. We recommend using a string of 20 characters. 

8. Click **Save** . 

Wait for the **Real-time sync** field to change to **Running** . 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Microsoft Outlook and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Microsoft API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

Your query string is sent to the third-party search backend (Microsoft API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Microsoft Outlook. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Microsoft API. 

### What's next

- To provide a user interface for querying your Microsoft Outlook data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Microsoft Outlook data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Microsoft Outlook configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-outlook/third-party-config

This page describes how to set up and configure a third-party configuration before creating the Outlook data store. 

### Set up authentication and permissions

You need to set up authentication and permissions in Microsoft Entra admin center. This is crucial for allowing the connector to access and synchronize data. 

#### Register Entra app for Microsoft Outlook connector

Before creating the Microsoft Outlook connector in Gemini Enterprise, register a Microsoft Entra application to enable secure access. 

To register Gemini Enterprise as an OAuth 2.0 application in Entra, do the following: 

1. Navigate to Microsoft Entra admin center (https://entra.microsoft.com). 

2. In the navigation menu, expand the **Entra ID** and select **App registrations** . 

3. On the **App registrations** page, click **New registration** . 

4. On the **Register an application** page, do the following: 

   - a. In the **Name** field, enter a name for your app. 

   - b. In the **Supported account types** section, select **Accounts in this organizational directory only** . 

   - c. In the **Redirect URI** section, do the following: 

      - i. In the platform list, select `Web` . 

      - ii. In the redirect URI field, enter 

         - `https://vertexaisearch.cloud.google.com/console/oauth/default_o auth.html` . 

            - i. Click **Register** . Microsoft Entra creates your app and displays the overview page of your app. 

5. In the app navigation menu, click **Authentication** . 

6. Click **Add redirect URI** . 

7. In the platform selection pane, do the following: 

   - a. Select **Web** . 

   - b. In the **Redirect URI** field, enter 

      - `https://vertexaisearch.cloud.google.com/oauth-redirect` . 

   - c. Click **Configure** . 

Add federated credential for data ingestion 

If you are using **Data ingestion** as the connection mode and **Federated credentials** as authentication method, then do the following: 

1. In the app navigation menu, click **Certificates & secrets** . 

2. Select the **Federated credentials** tab. 

3. Click **Add credential** . 

4. Select **Other issuer** from the **Federated credential scenario** list. 

5. In the **Issuer** field, enter `https://accounts.google.com` . 

6. In the **Subject identifier** field, enter the value that you get from the Google Cloud console. This value is generated during the Microsoft Outlook data store creation 

(/gemini/enterprise/docs/connectors/ms-outlook/set-up-data-store#create-data-store) in the data section. 

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

Obtain Tenant ID 

Your tenant ID can be found in the **Tenant ID** box on the overview page (https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView) in the Microsoft Entra admin center. 

#### Configure Microsoft API permissions

To configure the required API permissions for the app, do the following: 

1. On the app page, select **API permissions** . 

2. Click **Add permissions** . 

3. In the **Request API permissions** page, select **Microsoft Graph** . 

4. Search for and select the following permissions based on your connection mode: 

|Connection<br>mode|Permission Purpose|
|---|---|
|Federated<br>search|`Mail.Read`<br>`Mail.`<br>`Read.`<br>`Shared`<br>`Calendars`<br>`.Read`<br>`Contacts.`<br>`Read`<br>(Delegated) Allows the data store to read the signed-in user's<br>mailbox, mail from shared mailboxes, calendar events, and<br>contacts.|
|Data<br>ingestion|`Calendars`<br>`.Read`<br>(Application) Allows the data store to read events of all<br>calendars.|
||`Calendars`<br>`.Read`<br>`Basic.All`<br>(Application) Allows the data store to read events of all<br>calendars, except for properties such as body, attachments, and<br>extensions.|
||`Contacts.`<br>`Read`<br>(Application) Allows the data store to read all contacts in all<br>mailboxes.|
||`Mail.Read`(Application) Allows the data store to read mail in all mailboxes.<br>`Mail.Read`<br>`Basic`<br>(Application) Allows the data store to read basic mail properties<br>in all mailboxes. Includes all properties except body,<br>previewBody, attachments and any extended properties.|
||`Mail.Read`<br>`Basic.All`<br>(Application) Allows the data store to read basic mail properties<br>in all mailboxes. Includes all properties except body,<br>previewBody, attachments and any extended properties.|
||`User.Read`(Delegated) Allows the data store to read the profile of signed-in<br>users.|
||`User.`<br>`Read.All`<br>(Application) Allows the data store to read the full set of profile<br>properties, reports, and managers of other users in your<br>organization.|
||`User.Read`<br>`Basic.All`<br>(Application) Allows the data store to read a basic set of profile<br>properties of other users in your organization.|

Connection Permission Purpose mode 

Actions `Mail.Send` (Delegated) Allows the data store to send mail as users in the organization. `Mail.Read` (Delegated) Required for the **Add attachments**, **Create `Write` message**, **Update message**, and **Move mail** actions. `Calendars` (Delegated) Allows the data store to create, read, update, and `.Read` delete events in user calendars. `Write` 

`Contacts.` (Delegated) Allows the data store to create, read, update, and `ReadWrite` delete user contacts. 

`User.Read` (Delegated) Allows the data store to read the profile of signed-in users. File `Files.` (Delegated) Sufficient only for tools that read file metadata or productivity `Read.All` download file content: listing Excel workbooks, reading Excel (Excel, Word, workbook metadata, and converting Word (.docx) or PowerPoint PowerPoint) (.pptx) documents to PDF. Not sufficient for Excel workbook content operations (see next row). `Files.` (Delegated) Required for all Excel workbook content operations `Read` (read and write), including get worksheets, get tables, get rows, `Write.All` get row, create worksheets and tables, add and update rows, and add key columns. Per the Microsoft Graph API reference for these endpoints (for example, worksheet-list (https://learn.microsoft.com/graph/api/worksheet-list), table-list (https://learn.microsoft.com/graph/api/table-list), tablerow-list (https://learn.microsoft.com/graph/api/tablerow-list)), the accepted delegated permission is `Files.ReadWrite` . `Files. ReadWrite.All` grants the same capability across all drives the user can access. Also required for creating Word and PowerPoint documents in the user's OneDrive. 

`User.Read` (Delegated) Required to resolve the signed-in user's OneDrive location for file operations. 

|Tasks|`Tasks.`|(Delegated) Required for read operations on the signed-in user's|
|---|---|---|
|(Outlook to-|`Read`|Outlook task lists and tasks (list task lists, list tasks, get task).|
|do lists and|||
|tasks)|`Tasks.`|(Delegated) Required for write operations: creating, updating,|
||`ReadWri`|`te`<br>and deleting tasks in the signed-in user's Outlook task lists.|

Connection Permission Purpose mode Users and `User.Read` (Delegated) Required for tools that enumerate or look up directory `Basic.All` profiles of other users in the organization (Get User, List Users, (delegated and tools that operate on other users' mailboxes or calendars). enumeration) 

5. Click **Add Permissions** . 

**Note:** If you only intend to use the data store for search and not perform any actions, you can limit the scopes to just **`Mail.Read`** , **`Calendars.Read`** , and **`Contacts.Read`** . The other scopes are required to perform the actions mentioned in Supported actions (/gemini/enterprise/docs/connectors/ms-outlook#supported-actions). 

**Note:** For the file-productivity actions on Excel, Word, and PowerPoint, **grant** **`Files.ReadWrite.All` if you plan to use any Excel workbook content operations** (worksheets, tables, rows) — per the worksheet-list (https://learn.microsoft.com/graph/api/worksheet-list), table-list (https://learn.microsoft.com/graph/api/table-list), and tablerow-list (https://learn.microsoft.com/graph/api/tablerow-list) Microsoft Graph API references, the accepted delegated permission for those endpoints is **`Files.ReadWrite`** , so **`Files.Read.All`** alone is not sufficient. **`Files.Read.All`** is sufficient only for listing Excel workbooks, reading Excel workbook metadata, and Word or PowerPoint PDF conversion. Tenants that skip the required scope will see HTTP 403 **`accessDenied`** errors. For the driveItem-based operations (Word/PowerPoint PDF conversion, listing Excel workbooks, reading Excel workbook metadata), Microsoft Graph also documents **`Sites.Read.All`** or **`Sites.ReadWrite.All`** as accepted alternatives (see driveItem-get (https://learn.microsoft.com/graph/api/driveitem-get) and driveItem-get-content-format (https://learn.microsoft.com/graph/api/driveitem-get-content-format)). 

**Note:** The Outlook task tools require **`Tasks.Read`** (read task lists and tasks) or **`Tasks.ReadWrite`** (create, update, delete tasks). The user-lookup tools (Get User, List Users, and tools that operate on other users' mailboxes or calendars) require **`User.ReadBasic.All`** at minimum. Tenants that skip these scopes will see HTTP 403 **`notAllowed`** on task tools and 

HTTP 403 **`Authorization_RequestDenied`** on user-lookup tools. Tenants that need higherprivileged user access can substitute **`User.Read.All`** or **`Directory.Read.All`** . 

**Note:** After adding application permissions, you need to grant admin consent for your tenant. For more information, see Grant tenant-wide admin consent (https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent? pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps-pane) 

### Troubleshooting

This section describes how to resolve common issues with the Microsoft Outlook connector. 

#### Troubleshoot REST API and message search issues

If the Gemini Enterprise assistant reports that message search isn't working, or that the REST API isn't enabled for a user's mailbox (corresponding to a `MailboxNotEnabledForRESTAPI` error from Microsoft Graph), you can troubleshoot the issue in your Microsoft environment. 

This error occurs for the following reasons: 

- The mailbox is hosted on-premises (in a hybrid Exchange deployment) and hasn't been enabled for REST API access. 

- The mailbox is inactive or soft-deleted. 

- There is a tenant or directory mismatch. 

To resolve this issue, ensure that the mailbox is hosted in Exchange Online or configure REST API access for hybrid mailboxes. For more information, see How to fix MailboxNotEnabledForRESTAPI 

(https://learn.microsoft.com/en-us/answers/questions/1657546/how-to-fixmailboxnotenabledforrestapi) 

in the Microsoft documentation. 

#### Users see "Need admin approval" when they connect

When users connect to Microsoft Outlook from the Gemini Enterprise web app for the first time, Microsoft might show a **Need admin approval** screen. This happens if Gemini Enterprise requests administrator-level permissions, or if your Microsoft Entra tenant prohibits users from authorizing third-party apps without prior tenant-wide administrator consent. 

To resolve this issue, an administrator must complete the first authorization. After that, other users in your tenant can connect without the approval screen. 

1. Ask a Microsoft Entra ID administrator who can grant tenant-wide consent to sign in to the Gemini Enterprise web app and connect to Microsoft Outlook. 

2. On the permissions screen, have the administrator select **Consent on behalf of your organization** , and then click **Accept** . 

3. Ask users to connect again. 

For more information, see Grant tenant-wide admin consent (https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent? pivots=portal) 

in the Microsoft Entra documentation. 

**Note:** Deleting and re-creating the data store doesn't resolve this issue, because consent is granted in your Microsoft Entra tenant, not to the data store. 

Last updated 2026-10-14 UTC. 



## SharePoint connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/ms-sharepoint

The Microsoft SharePoint data store for Gemini Enterprise lets you search and perform actions on your _Microsoft SharePoint Online_ data, including documents, lists, and sites. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported Microsoft SharePoint versions

The Microsoft SharePoint data store supports the latest cloud version of Microsoft SharePoint Online. 

### Supported actions

When the Microsoft SharePoint data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create folder|Creates a new folder in a specified path.|
|Add list|Creates a new structured data list (for example, tasks, contacts) on<br>the Microsoft SharePoint site.|
|Upload document|Uploads a document to a Microsoft SharePoint site or library.|
|Download document|Downloads a document from a Microsoft SharePoint site or library.|
|Add page|Creates a new page on the Microsoft SharePoint site.|

|Action|Description|
|---|---|
|Check out document|Check out a document from a Microsoft SharePoint library.|
|Check in document|Check a document into a Microsoft SharePoint library.|
|Rename attachment or<br>document|Rename an attachment or document in a Microsoft SharePoint library.|
|Move attachment or<br>document|Move a document from a Microsoft SharePoint library to a destination<br>library, folder, or another SharePoint site.|
|Discard check out<br>document|Discards a check-out on a document, reverting it without saving<br>changes.|
|Share resource|Shares a document, folder, or resource with specified recipients or<br>generates a share link.|
|Update file properties|Updates metadata properties of a document in a Microsoft SharePoint<br>library.|
|Update page|Updates an existing page on the Microsoft SharePoint site.|
|Update list|Updates settings of an existing structured data list on the Microsoft<br>SharePoint site.|
|Create list item|Creates a new item in a specified list on the Microsoft SharePoint site.|
|Update list item|Updates fields of an existing item in a specified list.|
|List lists|Retrieves all lists and document libraries in a specified Microsoft<br>SharePoint site.|
|Get list item|Returns a single list item, including all of its column values.|
|Get list fields|Returns the schema of a specified list, including all of its fields and<br>their properties.|

**Notes** : 

Additional read-only actions are also available. 

The maximum file size for file uploads and downloads in Gemini Enterprise is 50 MB. 

#### Required permissions

To enable Gemini Enterprise to perform search and data ingestion using the Microsoft SharePoint data store, you need the following permissions: 

Microsoft Graph API permissions 

The table below outlines the permissions required for each connection mode. 

**Note:** The following table outlines the permissions required for each connection mode. If you enable **Actions** for either the **Federated search** or **Data ingestion** connection mode, also select the permissions listed in the **Actions** row. 

Connection Scope Purpose mode Federated N/A No Graph API permissions are required. search 

|Connection<br>mode|Scope|Purpose|
|---|---|---|
|Data<br>ingestion|`Group`<br>`Member.`<br>`Read.All`|(Federated credentials & OAuth 2.0 refresh token) Allows the data<br>store to read memberships and basic group properties for all groups<br>without a signed-in user.|
||`User.Read`<br>`User.Read.`<br>`All`|(Federated credentials & OAuth 2.0 refresh token) Allows the data<br>store to read the profile of signed-in users. It also allows the data<br>store to read basic company information of signed-in users.<br>(OAuth 2.0 refresh token only) Allows the data store to read user<br>profiles.|
||`Sites.Full`<br>`Control.All`<br>(Option 1)<br>`Sites.`<br>`Selected`<br>(Option 2)|(Federated credentials & OAuth 2.0 refresh token) Option 1 allows<br>the data store to have full control of all site collections. Option 2<br>allows the data store to access a subset of site collections. The<br>specific site collections and the permissions granted can be<br>configured in SharePoint Online.|
||`User.Read.`<br>`All`(Option<br>1)<br>`User.Read`<br>`Basic.All`<br>(Option 2)|(Federated credentials only) Option 1 allows the data store to read<br>user profiles. Option 2 allows the data store to read a basic set of<br>profile properties of other users in the organization.|
|Actions|`Sites.Read`<br>`Write.All`|(Federated search & Data ingestion) Allows the data store to edit or<br>delete documents and list items in all site collections on behalf of the<br>signed-in user.|
||`Sites.Read.`<br>`All`|(Federated search & Data ingestion) Allows the data store to read<br>lists, list items, and list schemas in all site collections on behalf of the<br>signed-in user. Required for the list lists, get list item, and get list<br>fields actions.|
||`Files.Read`<br>`Write`|Allows the data store to read, create, update and delete the signed-in<br>user's files.|
||`Files.Read`<br>`Write.All`|Allows the data store to read, create, update, delete, upload, and<br>download all files the signed-in user can access.|
||`Sites.`<br>`Manage.All`|Allows the data store to create or delete document libraries and lists<br>in all site collections on behalf of the user.|

Microsoft SharePoint API permissions 

The table below outlines the permissions required for each connection mode. 

|Connection mode|Scope|Purpose|
|---|---|---|
|Federated search|`Sites.Search.All`<br>(Delegated)|Allows the data store to run search queries and to read<br>basic site info on behalf of the current signed-in user.<br>Search results are based on the user's permissions<br>instead of the app's permissions.|
||`AllSites.Read`<br>(Option 1,<br>Delegated)|Allows the data store to read documents and list items<br>in all site collections on behalf of the signed-in user.|
||`Sites.Selected`<br>(Option 2,<br>Delegated)|Allows the data store to access a subset of site<br>collections with a signed-in user. The specific site<br>collections and the permissions granted can be<br>configured in SharePoint Online.|
|Data ingestion<br>(Federated<br>credentials)|`Sites.Full`<br>`Control.All`<br>(Option 1,<br>Application)|Allows the data store to have full control of all site<br>collections.|
||`Sites.Selected`<br>(Option 2,<br>Application)|Allows the data store to access a subset of site<br>collections with a signed-in user. The specific site<br>collections and the permissions granted can be<br>configured in SharePoint Online.|
|Data ingestion<br>(OAuth 2.0 refresh<br>token)|<br>`AllSites.Full`<br>`Control`(Option 1,<br>Delegated)|Allows the data store to have full control of all site<br>collections on behalf of the signed-in user.|
||`Sites.Selected`<br>(Option 2,<br>Delegated)|Allows the data store to access a subset of site<br>collections with a signed-in user. The specific site<br>collections and the permissions granted can be<br>configured in SharePoint Online.|
|Actions|`AllSites.Write`<br>(Delegated)|Allows the data store to create, read, update, delete,<br>upload, and download documents and list items in all<br>site collections on behalf of the signed-in user.|

For information on how to add the permissions for Microsoft SharePoint, see Configure Microsoft SharePoint and set the necessary permissions 

(/gemini/enterprise/docs/connectors/ms-sharepoint/third-party-config#configure-apipermissions) 

### Limitations

This section outlines known issues and limitations that may affect your use of the Microsoft SharePoint data store. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Microsoft SharePoint data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Microsoft SharePoint data store is supported only in the `global` , `us` , and `eu` locations. 

- **Search quality prerequisite:** To achieve optimal search results and fully leverage Knowledge Graph features, we recommend configuring and syncing the People search data store (/gemini/enterprise/docs/connectors/connect-people) in addition to the Microsoft SharePoint data store. 

The following are the limitations for the Microsoft SharePoint federated data store: 

- **Search limitations** : Search results may vary and are not always comprehensive for all file types. Content in archived or encrypted folders may not be accessible for search. Federated search does not support searching within attachments. 

- **Delegated access:** Access to shared sites or libraries may require specific permissions not covered by standard user authorization. 

- **Layout parser in federated search mode:** While the layout parser is standard, its effectiveness on complex PDFs (with tables, multi-column layouts, or needing OCR) is limited in federated search mode. This mode's 

real-time API calls might not provide the complete data or time required for the deep analysis the layout parser performs during data ingestion. 

- **Unsupported PDF Features:** Consequently, complex PDF structures might not be fully analyzed or searchable. This includes: 

   - Multi-column text layouts 

   - Data within embedded tables and charts 

   - Text in scanned documents requiring Optical Character Recognition (OCR) 

   - Documents with non-linear reading orders or intricate formatting. 

#### Recommendation

For Microsoft Sharepoint data containing PDFs with complex features (like tables, multi-column layouts, or OCR-dependent content), we recommend using standard ingestion mode for effective search. This mode allows the layout parser to deeply process and index the entire document content. 

### Troubleshooting SharePoint connector search results

If you are experiencing issues with missing documents, incorrect results, or poor search relevance, check the following diagnostic areas: 

- **Check the People data store:** Ensure the People search data store (/gemini/enterprise/docs/connectors/connect-people) is set up and syncing if you face relevance or entity-matching issues. 

- **Authentication errors:** Persistent authentication errors, such as "Error when retrieving Graph API access token," will prevent searches from functioning. To resolve this, check the Microsoft Entra ID logs for details and then reauthenticate the connection. 

- **Identity mismatch:** If using Google Identity, verify that the user's Google email exactly matches their Microsoft SharePoint email. Mismatches prevent results from returning. 

- **Targeted folder searches (.aspx URLs):** Searching with full browser URLs that end in `/Forms/AllItems.aspx` executes a search across the whole site, not just the specific folder. Always use absolute folder paths for targeted searches. 

- **Result limits:** Be aware that federated searches may have limits on the number of documents returned per query (typically capping around 20 results). 

- **Citation issues:** Intermittent incorrect citations can occur. If persistent, report the issue to support and include your diagnostic tokens. 

- **Connector-model compatibility:** Ensure you are using the latest Gemini model versions. Some older models (for example, 3.x) have known issues resolving tools for SharePoint actions, such as `download_document` within Agent Builder. 

### What's next

- To create and configure a data store with Microsoft SharePoint, see Set up a Microsoft SharePoint data store 

- (/gemini/enterprise/docs/connectors/ms-sharepoint/set-up-data-store). 

Last updated 2026-10-14 UTC.
