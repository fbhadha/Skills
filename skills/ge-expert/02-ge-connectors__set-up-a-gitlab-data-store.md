# Gemini Enterprise: connectors and data stores / Set up a GitLab data store to Set up a Jira Cloud data store
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 353-379, extracted 2026-10-18

Contains:
- Set up a GitLab data store (pages 353-358) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab/set-up-data-store
- GitLab configuration (pages 359-360) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab/gitlab-configuration
- Jira Cloud connector: overview (pages 361-368) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud
- Set up a Jira Cloud data store (pages 369-379) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/set-up-data-store

## Set up a GitLab data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab/set-up-data-store

This page describes how to create a data store and connect GitLab to Gemini Enterprise. 

### Before you begin

**Public preview:** The federated search is in public preview. This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). 

Before setting up your GitLab connection, ensure you have the following in place: 

- Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   2. Locate the user account and click **Edit** . 

   3. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions (https://cloud.google.com/gemini/enterprise/docs/access-control). 

- Sign in to your GitLab account and obtain authentication credentials (/gemini/enterprise/docs/connectors/gitlab/gitlab-configuration#set-permissions-and-getcredentials%7D) . 

- Create a GitLab app to use this connector. For more information, see Creating GitLab apps (https://docs.gitlab.com/en/apps/creating-gitlab-apps). 

### Create GitLab data store

To create a GitLab data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **GitLab** , and click **Select** . 

_Select GitLab._ 

6. In the **Data** section: 

   - a. In the **Authentication settings** section, enter the following details: 

      - **Client ID** : The OAuth client ID for your application. 

      - **Client Secret** : The OAuth client secret for your application. 

_Enter the client credentials._ 

For more information about credentials, see GitLab configuration (/gemini/enterprise/docs/connectors/gitlab/gitlab-configuration#set-permissionsand-get-credentials%7D) 

- b. Click **Continue** and complete the GitLab sign-in and authorization. 

- c. In the **Destinations** section, enter the **GitLab instance URL** . 

_Enter the GitLab instance URL._ 

- d. Click **Continue** . 

- e. In the **Advanced options** section, enter the organization name in the **Owner login** field. 

- f. Click **Continue** . 

- g. In the **Entities to search** section, select **Project** . 

<!-- Start of picture text -->
Choose the entity to search.<br><!-- End of picture text -->

7. Click **Continue** . 

8. In the **Configuration** section: 

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

9. Click **Continue** . 

10. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

11. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the GitLab connector is ready to be used. 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize GitLab and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the GitLab API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (GitLab API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to GitLab. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the GitLab API. 

### What's next

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 



## GitLab configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gitlab/gitlab-configuration

This page describes how to set up and configure a third-party configuration before creating the GitLab data store. 

### Set permissions and obtain client ID and client secret

To register a GitLab app and obtain the client ID and client secret, do the following: 

1. Sign in to your GitLab account and navigate to the group for which you want to create an application. 

2. Go to the selected group. 

3. Select **Settings** > **Applications** . 

4. In the **Name** field, enter a name for your application. 

5. In the **Redirect URI** field, enter 

`https://vertexaisearch.cloud.google.com/oauth-redirect` . 

6. In the **Scopes** section, select the appropriate scope based on your needs: 

   - For search-only access, select **read_api** . 

   - For search and actions (write) access, select **api** . 

7. Select **Save application** . GitLab provides: 

   - The OAuth2 Client ID in the **Application ID** field. 

   - The OAuth2 Client Secret, accessible by selecting **Copy** in the **Secret** field. 

   - The **Renew secret** function. Use this function to generate and copy a new secret for this application. Renewing a secret prevents the existing application from functioning until the credentials are updated. 

8. Copy the **Application ID** and **Secret** values that are generated, and store them securely for later use. 

Last updated 2026-10-14 UTC. 



## Jira Cloud connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud

The Jira Cloud data store for Gemini Enterprise lets you search and perform actions on your projects, issues, and user information. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported Jira Cloud versions

The Jira Cloud data store supports version 2 of the Jira Cloud REST API. 

### Supported actions

When the Jira Cloud data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create<br>comment|Creates a new comment on a specified Jira issue to add feedback, updates, or<br>notes.|
|Update<br>comment|Edits the text of an existing comment.|
|Create issue|Creates a new issue in a Jira Cloud project. To create one, you need to provide a<br>summary, the project ID, and the issue type ID.|
|Update issue|Updates an existing issue in Jira Cloud. You need to provide the issue ID to<br>identify it, and you can modify various fields such as the summary, description,<br>and assignee.|

|Action|Description|
|---|---|
|Change issue<br>status|Change the status of an existing issue in Jira Cloud. You need to provide the<br>issue ID to identify it.|
|Upload<br>attachment|Uploads an attachment to a specified Jira issue.|
|Assign issue|Assigns an existing Jira issue to a specified user.|
|Link issues|Creates a link between two Jira issues (for example, blocks, is blocked by,<br>relates to).|
|Create project|Creates a new Jira project with a specified name, key, project type, and<br>template.|
|Update project|Updates an existing Jira project's settings, such as name, key, description, or<br>lead.|
|Create worklog|Adds a time-tracking worklog entry to a Jira issue.|
|Update<br>worklog|Updates an existing worklog entry on a Jira issue.|
|Get board|Gets a board in Jira.|
|Get issues for<br>board|Gets issues for a board in Jira.|
|List boards|Lists boards in Jira.|

**Note:** Additional read-only actions are also available. 

#### Required scopes

To enable Gemini Enterprise to perform search and actions using the Jira Cloud data store, you need the following scopes: 

Classic scopes 

|Connection<br>mode|Permission|Purpose|
|---|---|---|
|Federated<br>search and<br>|`read:jira-user`,<br>`read:jira-work`|Allows the assistant to fetch and display search results and<br>user details in real-time.|
|actions|`write:jira-`<br>`work`|Allows the assistant to modify work items (for example,<br>updating issue fields), manage comments or issues, and<br>upload attachments.|
||`manage:jira-`<br>`project`|Allows the assistant to manage Jira project settings and<br>create new project-level objects such as versions and<br>components. Required for the create and update project<br>actions.|
|Federated<br>search only|`read:jira-user`,<br>`read:jira-work`|Allows the assistant to search for and view issues, projects,<br>and user profiles.|
|Data ingestion<br>and actions|`read:jira-work`|Allows the assistant to perform broad data crawling and<br>indexing of work items.|
||`write:jira-`<br>`work`|Allows the assistant to perform write actions (creation,<br>updates, comments, and attachments) on work items within<br>the ingested environment.|
|Data ingestion|`read:jira-work`|Allows the assistant to crawl and index Jira content for<br>search availability.|

Granular scopes 

|Connection<br>mode|Permission|Purpose|
|---|---|---|
|Federated sea<br>and actions|rch<br>`write:comment:jira`|Allows the data store to post new comments<br>or replies directly from the Gemini Enterprise<br>interface.|
||`write:issue:jira`|Allows the data store to create new issues or<br>perform major edits to existing ones.|
||`write:attachment:jira`|Allows the data store to upload attachments<br>to Jira issues.|
||`write:project:jira`|Allows the data store to create and update<br>Jira projects.|
||`write:issue-worklog:jira`|Allows the data store to create and update<br>issue worklogs.|
||`write:issue-link:jira`|Allows the data store to create and update<br>links between issues.|
||`read:issue:jira`|Allows the data store to read issues.|
||`read:issue-type:jira`|Allows the data store to read issue types.|
||`read:comment:jira`|Allows the data store to read comments.|
||`read:comment.property:jira`|Allows the data store to read issue comment<br>properties.|
||`read:project:jira`|Allows the data store to read projects.|
||`read:priority:jira`|Allows the data store to read priorities.|
||`read:issue.transition:jira`|Allows the data store to read issue<br>transitions.|
||`read:issue-meta:jira`|Allows the data store to read issue metadata.|
||`read:board-scope.`<br>`admin:jira-software`|Allows the data store to read the<br>configuration, project features, filters,<br>properties, and quick filters for a board.|
||`read:board-scope:jira-`<br>`software`|Allows the data store to read boards, issues<br>on a board, issues from a backlog, reports,<br>and versions.|

|Connection<br>mode|Permission|Purpose|
|---|---|---|
||`read:issue-details:jira`|Allows the data store to read issue details.|
||`read:jql:jira`|Allows the data store to read Jira Query<br>Language (JQL) queries.|
|Federated sea<br>|rch<br>`read:issue:jira`|Allows the data store to read issues.|
|only|`read:issue-type:jira`|Allows the data store to read issue types.|
||`read:comment:jira`|Allows the data store to read comments.|
||`read:comment.property:jira`|Allows the data store to read issue comment<br>properties.|
||`read:project:jira`|Allows the data store to read projects.|
||`read:priority:jira`|Allows the data store to read priorities.|
||`read:issue.transition:jira`|Allows the data store to read issue<br>transitions.|
||`read:issue-meta:jira`|Allows the data store to read issue metadata.|
||`read:board-scope.`<br>`admin:jira-software`|Allows the data store to read the<br>configuration, project features, filters,<br>properties, and quick filters for a board.|
||`read:board-scope:jira-`<br>`software`|Allows the data store to read boards, issues<br>on a board, issues from a backlog, reports,<br>and versions.|
||`read:sprint:jira-software`|Allows the data store to read sprint details.|
||`read:issue-details:jira`|Allows the data store to read issue details.|
||`read:jql:jira`|Allows the data store to read Jira Query<br>Language (JQL) queries.|

|Connection<br>mode|Permission|Purpose|
|---|---|---|
|Data ingestion<br>and actions|`read:user:jira`,<br>`read:group:jira`,<br>`read:avatar:jira`|Allows syncing user/group metadata and<br>displaying user profiles.|
||`read:issue-security-`<br>`level:jira`,`read:issue-`<br>`security-scheme:jira`|Allows for access control, ensuring the<br>ingested data respects Jira's security<br>boundaries.|
||`read:audit-log:jira`|Allows tracking changes and performing<br>incremental syncs to keep ingested data up<br>to date.|
||`write:comment:jira`|Allows adding comments to issues using the<br>data store.|
||`write:issue:jira`|Allows the assistant to create or modify<br>issues.|
|Data ingestion|`read:user:jira`,<br>`read:group:jira`,<br>`read:avatar:jira`|Allows crawling and indexing Jira content and<br>user relationships.|
||`read:issue-security-`<br>`level:jira`,`read:issue-`<br>`security-scheme:jira`|Allows mapping permissions so only<br>authorized users can search the ingested<br>data.|
||`read:audit-log:jira`|Allows the sync engine to identify which items<br>have been updated or deleted.|
||`read:sprint:jira-software`|Allows the data store to read sprint details.|

For information on how to configure these scopes, see Configure minimum application scope 

(/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#configure-minimumapplication-permissions) 

### Rate limits for data ingestion

The Jira Cloud data store supports a default rate limit of 12 queries per second (QPS) for data ingestion. These rate limits apply exclusively to the ingestion of data from the Jira Cloud data store. 

### Limitations

This section outlines known issues and limitations that may affect your use of the Jira Cloud data store. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Jira Cloud data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Jira Cloud data store is supported only in the `global` , `us` , and `eu` locations. 

The following are the limitations for the Jira Cloud ingestion data store: 

- For unstructured data, each media type has different restrictions. For more information, see Prepare data for custom data sources 

- (/gemini/enterprise/docs/prepare-data#unstructured). 

- For structured data, each document must not exceed 500 KB in size. 

- Application roles with specific, non-empty roles cannot be granted `Browse project` or security level permissions. 

- Document permissions determined by user custom fields or group custom fields are not supported. 

- Jira Cloud doesn't allow any restrictions on worklog levels. 

- Jira Cloud doesn't index PDF attachments that exceed 2,000 pages. 

- Attachments added to private comments don't inherit the access restrictions (ACLs) on the comments. 

- Only the previous 20 comments for an issue in Jira Cloud are fetched. 

- Sprint tables can't be ingested. 

- The legacy user management model is not supported for integration with Jira Cloud. Only the centralized user management model is supported. For more information, see Atlassian Organization consolidation guide 

- (https://support.atlassian.com/atlassian-cloud/kb/atlassian-organization-consolidationguide/) 

- When querying a Jira entity (for example, an issue), related data like comments and attachments are not automatically included. This is because they are stored and indexed as separate entities. Searching based on the _content_ of an attachment to find the parent issue is not supported. 

### What's next

- To create and configure a data store with Jira Cloud, see Set up a Jira Cloud data store (/gemini/enterprise/docs/connectors/jira-cloud/set-up-data-store). 

Last updated 2026-10-15 UTC. 



## Set up a Jira Cloud data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/set-up-data-store

This page describes how to create a data store and connect Jira Cloud to Gemini Enterprise. 

### Before you begin

Ensure the following before you set up your Jira Cloud federated connection: 

- Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Locate the user account and click **Edit** . 

3. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

(https://cloud.google.com/gemini/enterprise/docs/access-control). 

- To enforce data source access control and secure data in Google Gemini Enterprise, configure your identity provider 

- (/gemini/enterprise/docs/configure-identity-provider). 

- To set up the Jira Cloud data store, you must use the new centralized Atlassian user management model. If you are using the original model, you need to migrate your user management before proceeding. For more information, see Site administrator role 

(https://support.atlassian.com/atlassian-cloud/kb/site-administrator-role-in-thecentralized-user-management-and-original-user-management-experiences/) 

Create an OAuth 2.0 app 

- (/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#create-an-oauthconfiguration) 

- , obtain the client ID and secret 

(/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#obtain-client-id-andclient-secret) 

, and configure the minimum application permissions 

(/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#configure-minimumapplication-permissions) 

with the consent of a Jira Cloud administrator. Verify that you have Jira 

_organization administrator_ access 

(/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#verify-jira-org-adminaccess) 

to the Jira instance and project. With the _organization administrator_ access, you can set up minimum permissions and provide access privileges to user groups. 

Optional: To retrieve user email addresses from Jira Cloud, even when settings restrict email visibility, install the User Identity Accessor for Jira Cloud (/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#install-identityaccessor-app) 

app with Jira _Site administrator_ privileges to install 

(/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#install-identityaccessor-app) 

and configure 

(/gemini/enterprise/docs/connectors/jira-cloud/third-party-config#configure-identityaccessor-app) 

it to securely retrieve user email addresses. You might not need to install this app if email addresses are already publicly accessible. 

**Note:** Atlassian is updating user interface elements, and some elements mentioned in this documentation are being renamed (for example, **Products** is being renamed to **Apps** ). For more information, see Atlassian Administration terminology change from "products" to "apps" (https://community.atlassian.com/forums/Atlassian-Platform-articles/AtlassianAdministration-terminology-change-from-products-to/ba-p/2967398) 

### Create Jira Cloud data store

To create a Jira Cloud data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Jira Cloud** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Connector mode** section, select **Data ingestion** or **Federated search** as the connection mode. 

   - b. Click **Continue** . 

   - c. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

      - i. Provide the following authentication details: 

         - **Client ID** : The identifier for your OAuth 2.0 app. 

         - **Client secret** : The secret key associated with your OAuth 2.0 app. 

         - **Instance URI** : The base URL of your Jira Cloud instance (For example, `https://your-domain.atlassian.net` ) . 

         - **Instance ID** : A unique identifier for your Jira Cloud instance. 

For more information about how to obtain these credentials, see Jira Cloud configuration 

      - (/gemini/enterprise/docs/connectors/jira-cloud/third-party-config). 

   - ii. If you selected **Federated search** , click **Login** and complete the Atlassian sign-in. 

   - iii. Click **Continue** . 

- d. In the **Destinations** section, enter the URL to your Jira Cloud endpoint. 

e. Click **Continue** . 

f. In the **Advanced options** section: 

- Optional: To allow a set of static IP addresses in your system, select the **Enable Static IP Addresses** checkbox. After creating the data store, you must view the registered static IP addresses on the data store details page and add them to your Jira Cloud IP allowlist rule. For more information, see Configure static IP egress 

- (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

- If you selected **Federated search** and if you have custom fields, select **Include Custom Fields** to make them searchable. Jira custom fields are user-defined data fields that store specialized information not available in default system fields. 

- If you selected **Data ingestion** : 

   - i. Optional: In the **Max QPS** field, enter the maximum queries per second to apply a rate limit on the queries that the connector sends to the Jira Cloud instance. If not set, default is 12. 

   - ii. Optional: If you have set up **User Identity Accessor for Jira Cloud** : 

      - i. In the **Jira Identity Sync Forge URL** field, enter the target URL of the Forge app generated within your instance. 

      - ii. In the **Jira Identity Sync Forge Client Secret** field, enter the API key or token generated within the Jira application's configuration. For more information about how to set up the User Identity Accessor for Jira Cloud, see Install User Identity Accessor 

(/gemini/enterprise/docs/connectors/jira-cloud/third-partyconfig#configure-identity-accessor-app) 

- g. In the **Entities to search** (if you selected **Federated search** ) or **Entities to sync** (if you selected **Data ingestion** ) section: 

   - i. Select all the required entities. 

ii. If you selected **Federated search** , proceed to the next step. 

iii. If you selected **Data ingestion** , continue with the following steps: 

- i. Optional: To sync specific projects, do the following: 

   - i. Click **Filter** . 

   - ii. To filter entities out of the index, select **Exclude from the index** , or to ensure that they are included in the index, select **Include to the index** . 

   - iii. Enter the project key. Press **Enter** after each project key. For more information about obtaining the project key, see Obtain project key 

(/gemini/enterprise/docs/connectors/jira-cloud/third-partyconfig#obtain-project-id) 

   - iv. Enter the keys. Press enter after each key. 

   - v. Click **Save** . 

- ii. To configure the sync schedule, do the following: 

   - i. In the **Sync frequency** list, select the sync frequency. 

      - To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options** . 

   - ii. In the **Incremental sync frequency** list, select the incremental sync frequency. For more information, see Sync schedules 

(https://cloud.google.com/gemini/enterprise/docs/introduction-toconnectors-and-data-stores#sync-schedules) 

7. Click **Continue** . 

8. In the **Actions** section: 

   - If you selected **Federated search** , in the **Select Jira Cloud actions to enable** section, select the actions to enable for the data store. 

If you selected **Data ingestion** : 

a. In the **Authentication settings** section: 

- i. Provide the following authentication details: 

   - **Client ID** : The identifier for your OAuth 2.0 app. 

   - **Client Secret** : The secret key associated with your OAuth 2.0 app. 

   - **Instance URI** : The base URL of your Jira Cloud instance (For example, `https://your-domain.atlassian.net` ). 

   - **Instance ID** : A unique identifier for your Jira Cloud instance. 

For more information about credentials, see Jira Cloud configuration (/gemini/enterprise/docs/connectors/jira-cloud/third-party-config). 

   - i. Click **Login** and sign-in to Jira Cloud to verify your account. 

- b. Click **Continue** . 

- c. From **Select Jira Cloud actions to enable** , select the actions from the category to enable them for the data store. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions 

(/gemini/enterprise/docs/manage-actions#add-actions). 

To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

9. Click **Continue** . 

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

On the **Data Stores** page, click your data store name to see the status. After the data store state changes from **Creating** to **Active** , the Jira Cloud data store is ready to be used. 

For an ingestion data store created with Jira Cloud, the data store state transitions from **Creating** to **Running** upon synchronization initiation. It then changes to **Active** once ingestion is complete, signifying that the data store is fully configured. Depending on data volume, ingestion may require several hours. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app), connect it to the Jira Cloud data store 

- (/gemini/enterprise/docs/connect-existing-data-store), and authorize 

(/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to access Jira Cloud before executing any queries. 

### Enable real-time sync for data ingestion

**Preview — Real-time sync** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

Real-time sync only syncs document entities and doesn't sync data related to identity entities. The following table shows which document events are supported with real-time sync. 

|Jira entities|Create|Update|Delete|Permission changes|
|---|---|---|---|---|
|Issues|||||
|Worklogs|||||
|Projects|||||
|Comments|||||
|Attachments|||||

To enable real-time sync for a Jira Cloud data store, follow these steps: 

#### Generate a webhook URL

1. Navigate to the Gemini Enterprise page, and in the navigation menu, click **Data Stores** . 

2. Select a Jira Cloud data store. 

3. Click **View/Edit** in the **Realtime sync** row. 

4. In the **View and edit realtime sync parameters** dialog, do the following: 

   - a. To turn on real-time sync, click the **Enable realtime sync** toggle. 

   - b. Enter a value in the **Client secret** field and copy it. You need this value again when creating a webhook in the Jira administration console. 

   - c. Click **Save** . 

5. After the status of **Realtime sync** changes to `Running` , click **View/Edit** . 

6. In the **View and edit realtime sync parameters** dialog, do the following: 

   - a. Copy the **Webhook URL** . 

   - b. Click **Close** . 

#### Create a webhook

1. Sign in to the Jira administration console. 

2. Click **Settings** and select **System** . 

3. In the **System settings** pane, select **Webhooks** . 

4. Click **Create a webhook** . For information about webhooks, see Webhooks (https://developer.atlassian.com/server/jira/platform/webhooks/). 

5. Enter a name for the webhook. 

6. Select the **Status** as `Enabled` . 

7. In the **URL** field, paste the URL copied from Gemini Enterprise and append `/{issue.id}` . 

8. In the **Secret** field, enter the same value you entered when generating a webhook URL in Gemini Enterprise. 

**Note:** To verify data consistency and prevent errors when configuring webhooks in Jira, only select entities that are enabled for sync in your data store. 

9. In the **Issue related events** section, select the following options: 

|Entities|Created|Updated|Deleted|
|---|---|---|---|

|Issue|Yes|Yes|Yes|
|---|---|---|---|
|Worklog|Yes|Yes|Yes|
|Comment|Yes|Yes|Yes|
|Attachment|Yes|No|Yes|

10. In the **Project related events** section, select the **created** , **updated** , and **deleted** checkboxes for the **Project** entity. 

11. Click **Create** . 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Jira Cloud and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Atlassian API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Atlassian API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Jira Cloud. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Atlassian API. 

### What's next

- To provide a user interface for querying your Jira Cloud data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Jira Cloud data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC.
