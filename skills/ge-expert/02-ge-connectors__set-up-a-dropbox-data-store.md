# Gemini Enterprise: connectors and data stores / Set up a Dropbox data store to GitLab connector: overview
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 314-352, extracted 2026-10-18

Contains:
- Set up a Dropbox data store (pages 314-321) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/data-store
- Dropbox configuration (pages 322-325) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/config
- Microsoft Dynamics 365 connector: overview (pages 326-327) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365
- Set up a Dynamics 365 data store (pages 328-332) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365/set-up-data-store
- Dynamics 365 configuration (pages 333-336) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365/third-party-config
- GitHub connector: overview (pages 337-341) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github
- Set up a GitHub data store (pages 342-346) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/set-up-data-store
- GitHub configuration (pages 347-350) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/github-configuration
- GitLab connector: overview (pages 351-352) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab

## Set up a Dropbox data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/data-store

This page describes how to create a data store, and connect Dropbox to Gemini Enterprise. 

**Note:** To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider 

(/gemini/enterprise/docs/configure-identity-provider). 

### Before you begin

Before you set up your Dropbox data store, do the following: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   - b. Locate the user account and click **Edit** . 

   - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

      - (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Create an app in the Dropbox App Console, obtain the authentication credentials, and set the required scopes. For more information, see Dropbox configuration (/gemini/enterprise/docs/connectors/dropbox/config). 

### Create the Dropbox data store

To create a Dropbox data store, do the following: 

1. In the Google Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. On the **Select a data source** page, enter _Dropbox_ into the search field. The Dropbox card displays. 

6. Click Select. 

7. In the **Data** section, fill in the following fields: 

   - a. For the **Connector mode** field, select **Federated search** and click **Continue** . 

   - b. Under **Authentication settings** , enter the values you copied when you created an app in the Dropbox App Console: 

      - For **Client ID** , enter the Dropbox app's **App key** . 

      - For **Client Secret** , enter the Dropbox app's **App secret** . 

For more information about creating an app in the Dropbox App Console, see Dropbox configuration (/gemini/enterprise/docs/connectors/dropbox/config). 

Click **Login** . 

- c. Click **Continue** . 

- d. In the **Entities to search** section, select the entity types that you want Gemini Enterprise to search. 

Click **Continue** . 

8. In the **Actions** section, select the actions that you want users to be able to perform in their Dropbox accounts using the Gemini Enterprise assistant. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

   - To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

9. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see Configure static IP egress (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

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

- For more information, see Customer-managed encryption keys (/gemini/enterprise/docs/cmek). 

Click **Continue** . 

11. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects 

   - (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses 

   - (/gemini/enterprise/docs/licenses). 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Dropbox data store is ready to be used. 

After creating the data store, do the following before running any queries: 

1. Create an app (/gemini/enterprise/docs/create-app). 

2. Connect the app (/gemini/enterprise/docs/connect-existing-data-store) to the Dropbox data store. 

3. Authorize (/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to connect to Dropbox. 

For information about the permissions required to perform a search, see Minimum permissions (/gemini/enterprise/docs/connectors/dropbox#minimum-permissions-actions). 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Dropbox and send a search query to Gemini Enterprise: 

Gemini Enterprise sends your search query directly to the Dropbox API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

- When using third-party federated search, the following data handling rules apply: 

   - Your query string is sent to the third-party search backend (Dropbox API). 

   - These third parties may associate queries with your identity. 

   - If multiple federated search data sources are enabled, the query might be sent to all of them. 

   - After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Dropbox. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Dropbox API. 

### What's next

- To provide a user interface for querying your data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Dropbox data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## Dropbox configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox/config

This page describes how to set up authentication and permissions before creating a Dropbox data store for use with Gemini Enterprise. 

### Set up authentication and permissions

To connect Dropbox to Gemini Enterprise, you must create an app in the Dropbox DBX Platform. 

#### Create and configure a Dropbox app

1. Navigate to the Dropbox App Console (https://www.dropbox.com/developers/apps). 

2. Click **Create app** . Fill in the following fields: 

   - a. For **Choose an API** , select **Scoped access** . 

   - b. For **Choose the type of access you need** , select **Full Dropbox** . 

   - c. In the **Name your app** field, enter a name for your Dropbox app. 

   - d. Select the **I agree to Dropbox API Terms and Conditions** checkbox. 

   - e. Click **Create app** . 

3. In the details page for your new app, click the **Settings** tab. Configure the following settings: 

   - a. For the **Development users** status, click **Enable additional users** . A **Limit raised to 500 users** dialog opens and displays a message that your app can link to up to 500 users. 

   - b. Click **Okay** . 

   - c. Copy the **App key** and **App secret** . 

   - d. For the **OAuth 2** field, add 

`https://vertexaisearch.cloud.google.com/console/oauth/default_oauth. html` in the **Redirect URIs** field. 

- e. Click **Add** . 

- f. Enter `https://vertexaisearch.cloud.google.com/oauth-redirect` in the **Redirect URIs** field. 

- g. Click **Add** . 

   - `https://vertexaisearch.cloud.google.com/console/oauth/default_o auth.html` 

   - `https://vertexaisearch.cloud.google.com/oauth-redirect` 

4. Click the **Permissions** tab. In the **Individual Scopes** section, select the following scopes: 

   - In the **Account Info** section, select the **account_info.read** checkbox. 

   - In the **Files and folders** section, select the **files.metadata.read** checkbox and the **files.content.read** checkbox. 

5. Click **Submit** . 

Last updated 2026-10-14 UTC. 



## Microsoft Dynamics 365 connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

The Dynamics 365 connector for Gemini Enterprise lets you search your Dynamics 365 data. 

### Limitations

This section outlines known issues and limitations that may affect your use of the Dynamics 365 data store. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Dynamics 365 data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Dynamics 365 data store is supported only in the `global` , `us` , and `eu` locations. 

### What's next

- To create and configure a connector with Dynamics 365, see Set up a Dynamics 365 data store 

- (/gemini/enterprise/docs/connectors/dynamics365/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Dynamics 365 data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365/set-up-data-store

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

This page describes how to create a data store and connect Dynamics 365 to Gemini Enterprise. 

### Before you begin

Before setting up your Dynamics 365 connection, ensure you have the following in place: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

      - b. Locate the user account and click **Edit** . 

      - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Register Gemini Enterprise as an OAuth 2.0 application in Microsoft Entra ID (/gemini/enterprise/docs/connectors/dynamics365/third-party-config) and obtain the following credentials 

   - (/gemini/enterprise/docs/connectors/dynamics365/third-party-config#obtain-details): 

         - Client ID 

         - Tenant ID 

### Create Dynamics 365 data store

To create a Dynamics 365 data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create (/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Dynamics 365** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Authentication settings** section, enter the following authentication details: 

      - **Instance URI** : The instance URL of your Dynamics 365 instance. For example, `https://myorg.crm.dynamics.com` . 

      - **Tenant ID** : The tenant ID of your Dynamics 365 instance. 

      - **Subject identifier** : The unique ID of the service account. Copy this value and use it to add a federated credential in Microsoft Entra ID (/gemini/enterprise/docs/connectors/dynamics365/third-party-config#addfed-credentials) 

      - **Client ID** : The Client ID of your registered application. 

For more information about credentials, see Dynamics 365 configuration (/gemini/enterprise/docs/connectors/dynamics365/third-party-config). 

   - b. Click **Continue** . 

   - c. In the **Entities to search** section, select the entities that you want Gemini Enterprise to search. For Dynamics 365, these are **Invoice** , **Sales Order** , and **Quote** . 

7. Click **Continue** . 

8. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see Configure static IP egress (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

9. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Your data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a single-region key for third-party connectors 

      - (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

      - Select **Google-managed encryption key** or **Cloud KMS key** . If you selected **Cloud KMS key** : 

         - In the **Key management type** list, select the appropriate type. 

         - In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys (/gemini/enterprise/docs/cmek). 

10. Click **Continue** . 

11. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

12. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Dynamics 365 connector is ready to be used. 

After creating the data store, connect the data store you just created to an existing app or create a new app (/gemini/enterprise/docs/create-app) and connect (/gemini/enterprise/docs/connect-existing-data-store) it to the new app. 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Dynamics 365 and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Dynamics 365 API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Dynamics 365 API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Dynamics 365. This rewritten query can incorporate information from your session's query history. As a 

result, parts of your query history might also be included in the query sent to the Dynamics 365 API. 

### What's next

- To provide a user interface for querying your Dynamics 365 data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Dynamics 365 data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Dynamics 365 configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dynamics365/third-party-config

**Public preview:** The federated search and actions features are in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

This page describes how to set up and configure a third-party application before creating the Dynamics 365 data store. 

### Register Microsoft Entra app for Dynamics 365 connector

You must set up an Entra application registration to enable secure access to Dynamics 365 before you can create the connector in Gemini Enterprise. 

To register Gemini Enterprise as an OAuth 2.0 application in Entra, do the following: 

1. Navigate to Microsoft Entra admin center (https://entra.microsoft.com). 

2. In the navigation menu, expand **Identity** and select **App registrations** . 

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

      - `https://vertexaisearch.cloud.google.com/oauth-redirect` . 

   - c. Click **Configure** . 

### Add federated credential

To enable access to your Dynamics 365 instance using federated credentials, do the following: 

1. In the app navigation menu, click **Certificates & secrets** . 

2. Select the **Federated credentials** tab. 

3. Click **Add credential** . 

4. Select **Other issuer** from the **Federated credential scenario** list. 

5. In the **Issuer** field, enter `https://accounts.google.com` . 

6. In the **Subject identifier** field, enter the value that you get from the Google Cloud console. This value is generated during the Dynamics 365 datastore creation 

   - (/gemini/enterprise/docs/connectors/dynamics365/set-up-data-store#create-data-store) in the data section. 

7. In the **Name** field, enter a unique label for the federated credential. 

8. Click **Add** to grant access. 

### Obtain client credentials

To connect the Dynamics 365 data store, obtain the application's Client ID and your Tenant ID: 

#### Obtain client ID

1. In the app navigation menu, select **Overview** . 

2. Copy the **Application (client) ID** . 

#### Obtain Tenant ID

Your tenant ID can be found in the **Tenant ID** box on the overview page (https://entra.microsoft.com/#view/Microsoft_AAD_IAM/TenantOverview.ReactView) in the Microsoft Entra admin center. 

### Configure Microsoft API permissions

To configure the required API permissions for the app, do the following: 

1. Navigate to the app page. 

2. In the app navigation menu, select **API permissions** . 

3. Click **Add permissions** . 

4. In the **Request API permissions** pane, select **Dynamics CRM** . 

5. Search for and select the following delegated permission: 

**user_impersonation** (Access Dynamics 365 as organization users) 

6. Click **Add Permissions** . 

Last updated 2026-10-14 UTC. 



## GitHub connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github

The GitHub connector for Gemini Enterprise lets you perform create, update, and read operations on GitHub data. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported actions

When the GitHub data store is enabled, you can use natural language commands in Gemini Enterprise to perform GitHub actions. 

The following GitHub actions that modify data are supported by the data store. Additional read-only actions are also available for tasks like searching and fetching context. 

|Action|Description|
|---|---|
|Add comment to pending review|Add a review comment to your latest pending pull request<br>review.|
|Add issue comment|Add a comment to a specific issue or pull request.|
|Create branch|Create a new branch in a repository.|
|Create gist|Create a new GitHub Gist.|
|Create or update file|Create or update a single file in a repository.|
|Dismiss notification|Mark a GitHub notification as read or done.|
|Fork repository|Fork a repository to your account or a specified organization.|

|Action|Description|
|---|---|
|Manage notification subscription|Ignore, watch, or delete a notification thread subscription.|
|Manage repository notification<br>subscription|Ignore, watch, or delete a repository's notification<br>subscription.|
|Mark all notifications read|Mark all notifications as read, optionally scoped to a<br>repository.|
|Merge pull request|Merge a pull request.|
|Push files|Push multiple files to a repository in a single commit.|
|Reply to pull request comment|Add a reply to an existing pull request comment.|
|Star repository|Star a repository on behalf of the authenticated user.|
|Trigger Actions workflow|Trigger a GitHub Actions workflow (run, cancel, or rerun<br>jobs).|
|Unstar repository|Unstar a repository on behalf of the authenticated user.|
|Update gist|Update an existing GitHub Gist.|
|Update pull request|Update an existing pull request.|
|Write discussion comment|Add, reply to, update, delete, or mark/unmark as answer a<br>discussion comment.|
|Write GitHub project|Create or update GitHub Projects (project, items, fields,<br>status updates).|
|Write issue|Create or update an issue in a repository.|
|Write repository label|Create, update, or delete a label on a repository.|

### Required permissions

To enable Gemini Enterprise to perform search using the GitHub data store, you need the following permissions: 

Permission Name Permission Type Reason for Access 

|Repository: Actions|Read and write|Trigger, list, cancel, and rerun workflow runs; access job<br>logs|
|---|---|---|
|Repository:<br>Administration|Read-only|List repository collaborators|
|Repository: Contents|Read and write|Read files, commits, branches, tags, and releases;<br>create branches, write files, push commits, and fork<br>repositories|
|Repository:<br>Discussions|Read and write|Read GitHub Discussions and discussion categories;<br>add, update, or delete discussion comments|
|Repository: Issues|Read and write|Read issues, labels, comments, and search issues;<br>create or update issues, post comments, and manage<br>labels|
|Repository: Metadata|Read-only<br>(Mandatory)|Search for repositories and users|
|Repository: Pull<br>requests|Read and write|Read pull requests, diffs, and PR comments; merge,<br>update, and add review comments and replies|
|Repository: Code<br>scanning alerts|Read-only|Read code scanning alerts|
|Repository:<br>Dependabot alerts|Read-only|Read Dependabot security alerts|
|Repository: Secret<br>scanning alerts|Read-only|Read secret scanning alerts|
|Organization:<br>Members|Read-only|View organization teams and their members|
|Organization: Issue<br>Types|Read-only|View organization issue types|
|Organization: Projects|Read and write|Read and manage organization-level Projects v2<br>(projects, items, fields, and status updates)|
|Account: Starring|Read and write|Star and unstar repositories|
|Account: Profile|Read and write|Access user profile information|

**Note:** You need to create a GitHub App to use this connector. For more information, see Creating GitHub apps (https://docs.github.com/en/apps/creating-github-apps) 

For information on how to configure these permissions, see Set permissions and obtain client ID and client secret 

(/gemini/enterprise/docs/connectors/github/github-configuration#set-permissions-and-getcredentials) 

### Limitations

This section outlines known issues and limitations that may affect your use of the GitHub data store. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing GitHub data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

The GitHub data store is supported only in the `global` , `us` , and `eu` locations. 

### What's next

- To create and configure a connector with GitHub, see Set up a GitHub data store (/gemini/enterprise/docs/connectors/github/set-up-data-store). 



## Set up a GitHub data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/set-up-data-store

This page describes how to create a data store and connect GitHub to Gemini Enterprise. 

### Before you begin

Before setting up your GitHub connection, ensure you have the following in place: 

- Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Locate the user account and click **Edit** . 

3. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

(https://cloud.google.com/gemini/enterprise/docs/access-control). 

- Sign in to your GitHub account and obtain authentication credentials (/gemini/enterprise/docs/connectors/github/github-configuration#set-permissions-andget-credentials%7D) 

- Create a GitHub app to use this connector. For more information, see Creating GitHub apps (https://docs.github.com/en/apps/creating-github-apps). 

### Create GitHub data store

To create a GitHub data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **GitHub** , then select it. 

6. In the **Data** > **Authentication settings** section: 

   - a. Enter the client credential details: 

      - **Client ID** : The OAuth client ID for your application. 

      - **Client Secret** : The OAuth client secret for your application. 

For more information about credentials, see GitHub configuration (/gemini/enterprise/docs/connectors/github/github-configuration#set-permissionsand-get-credentials%7D) 

- b. If your users sign in through an identity provider (IdP), such as with GitHub Enterprise Managed Users (EMU) 

(https://docs.github.com/en/enterprise-cloud@latest/admin/managingiam/understanding-iam-for-enterprises/about-enterprise-managed-users) 

, then enter the GitHub SSO sign-in details. Otherwise, leave these fields blank. 

      - **GitHub SSO Scope** : The GitHub namespace that gates sign-in. If your IdP is configured at the enterprise level, select **enterprises** . If your IdP is configured at the organization level, select **orgs** . 

      - **GitHub SSO Slug** : The slug of your GitHub enterprise or organization, for example `octocorp` for the enterprise URL `https://github.com/enterprises/octocorp` . Enter the slug only, not a full URL. 

   - c. Click **Verify Auth** and complete verifying the GitHub authorization. 

7. In the **Data** > **Advanced options** section: 

   - a. Enter your GitHub organization name in the **Organization Name** field. This is required to scope search and actions. 

   - b. Click **Continue** . 

8. In the **Data** > **Entities to search** section: 

   - a. Select the required entities. 

   - b. Click **Continue** . 

9. In the **Actions** section: 

   - a. For **Select GitHub actions to enable** , choose the actions from the category to enable them for the data store. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions 

(/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

(/gemini/enterprise/docs/manage-actions). 

b. Click **Continue** . 

10. If the create data store flow shows an **Advanced options** section, you can select the **Enable Static IP Addresses** checkbox within it. This ensures the data store uses a fixed set of IP addresses for outbound traffic, suitable for allowlisting on the source system. For more information, see Configure static IP egress (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

11. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Your data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a 

single-region key for third-party connectors 

(/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

Select **Google-managed encryption key** or **Cloud KMS key** . 

If you selected **Cloud KMS key** : 

In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys (/gemini/enterprise/docs/cmek). 

12. Click **Continue** . 

13. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

14. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the GitHub connector is ready to be used. 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize GitHub and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the GitHub API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (GitHub API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to GitHub. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the GitHub API. 

### What's next

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## GitHub configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/github/github-configuration

This page describes how to set up and configure a third-party configuration before creating the GitHub data store. 

### Set permissions and obtain client ID and client secret

To register a GitHub app and obtain the client ID and client secret, do the following: 

1. Sign in to your GitHub account. 

2. Go to **Settings** > **Developer Settings** . 

3. In the **Developer Settings** page, click **GitHub apps** . 

4. Click **New GitHub app** . 

_GitHub app_ 

5. In the app registration page, do the following: 

   - a. In the **GitHub app name** field, enter a label to identify the app. 

   - b. In the **Homepage URL** field, enter the full URL to your application homepage. 

   - c. In the **Callback URL** field, enter 

      - `https://vertexaisearch.cloud.google.com/oauth-redirect` . 

   - d. To ensure tokens expire regularly and to receive a `refresh_token` that can be used to request a new access token, select the **Expire user authorization tokens** checkbox. 

- e. To prompt users to authorize your app when they install it, select the **Request user authorization (OAuth) during installation** checkbox. 

- f. In the **Permissions** section, enable the following permissions: 

|Permission Name|Permission<br>Type|Reason for Access|
|---|---|---|
|Repository: Actions|Read and write      l|Trigger, list, cancel, and rerun workflow runs;<br>access job logs|
|Repository:<br>Administration|Read-only|List repository collaborators|
|Repository:<br>Contents|Read and write  i|Read files, commits, branches, tags, and<br>releases; create branches, write files, push<br>commits, and fork repositories|
|Repository:<br>Discussions|Read and write|Read GitHub Discussions and discussion<br>categories; add, update, or delete discussion<br>comments|
|Repository: Issues|Read and write|Read issues, labels, comments, and search<br>issues; create or update issues, post<br>comments, triage issues, and manage labels|
|Repository:<br>Metadata|Read-only<br>(Mandatory)|Search for repositories and users|
|Repository: Pull<br>requests|Read and write    f|Read pull requests, diffs, and PR comments;<br>merge, update, and add review comments and<br>replies|
|Repository: Code<br>scanning alerts|Read-only|Read code scanning alerts|
|Repository:<br>Dependabot alerts|Read-only|Read Dependabot security alerts|
|Repository: Secret<br>scanning alerts|Read-only|Read secret scanning alerts|
|Organization:<br>Members|Read-only|View organization teams and their members|
|Organization: Issue<br>Types|Read-only|View organization issue types|

Organization: Read and write Read and manage organization-level Projects Projects v2 (projects, items, fields, and status updates) Account: Starring Read and write Star and unstar repositories Account: Profile Read and write Access user profile information 

- g. In the section asking where to install the app, select **Only on this account** . 

h. Click **Create GitHub app** . 

6. In the navigation menu, select **Install app** . 

7. Select an account to install the newly created app and click **Install** . 

8. Select **All repositories** and click **Install & authorize** . 

9. In the navigation menu, select **General** . 

10. Click **Generate a new client secret** . Copy the **Client ID** and the generated **Client secret** values, and store them securely for later use. 

_GitHub app General tab_ 



## GitLab connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

The GitLab connector for Gemini Enterprise lets you search across your GitLab data. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Required permissions

To enable Gemini Enterprise to use the GitLab data store, you need to select scopes when configuring OAuth 2.0 for GitLab. 

To allow search in the GitLab data store, select the following scope: 

`read_api` : Grants read access to the API. 

**Note:** You need to create a GitLab App to use this connector. For more information, see Creating GitLab apps (https://docs.gitlab.com/en/apps/creating-gitlab-apps) 

For information on how to configure these permissions, see Set permissions and obtain client ID and client secret 

(/gemini/enterprise/docs/connectors/gitlab/gitlab-configuration#set-permissions-and-getcredentials) 

### Limitations

This section outlines known issues and limitations that may affect your use of the GitLab data store. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing GitLab data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The GitLab data store is supported only in the `global` , `us` , and `eu` locations. 

### What's next

- To create and configure a connector with GitLab, see Set up a GitLab data store (/gemini/enterprise/docs/connectors/gitlab/set-up-data-store). 

Last updated 2026-10-14 UTC.
