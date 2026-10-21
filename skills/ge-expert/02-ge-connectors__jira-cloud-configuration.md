# Gemini Enterprise: connectors and data stores / Jira Cloud configuration to Jira Data Center configuration
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 380-414, extracted 2026-10-18

Contains:
- Jira Cloud configuration (pages 380-397) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config
- Jira Data Center connector: overview (pages 398-400) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc
- Set up a Jira Data Center data store (pages 401-411) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/set-up-data-store
- Jira Data Center configuration (pages 412-414) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration

## Jira Cloud configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-cloud/third-party-config

This page describes how to set up and configure a third-party configuration before creating the Jira Cloud data store. 

### Set up authentication and permissions

You need to set up authentication and permissions in the Atlassian administrator account center. This is crucial for allowing the connector to access and synchronize data. The Jira Cloud connector supports various authentication methods, such as OAuth client credentials or API tokens. 

#### Create an OAuth 2.0 app

To create an OAuth 2.0 app for authentication, follow these steps to set up the application in your Atlassian Developer Console and obtain the necessary client ID and client secret. 

Verify Jira organization administrator access 

To verify Jira organization administrator access, do the following: 

1. Sign-in to Atlassian (https://id.atlassian.com/login) with your user credentials. 

2. Select the **Jira** app. 

3. Click **Settings** . 

If you see the **System** option under **Jira settings** , you have Jira _organization administrator_ access. Otherwise, request your Jira organization administrator to provide access. 

Create OAuth 2.0 app 

To create an OAuth 2.0 app, do the following: 

1. Sign in to the Atlassian Developer Console (https://developer.atlassian.com). 

2. Click the profile icon and select **Developer console** . 

3. In the **Console** page, click **Create** and select **OAuth 2.0 Integration** . 

4. In the app creation page, do the following: 

   - a. Enter a name for the app. 

   - b. Select the checkbox to agree to Atlassian's developer terms. 

   - c. Click **Create** . 

5. In the app page, do the following: 

   - a. From the navigation menu, click **Authorization** . 

   - b. In the **Authorization type** table, select **Add** for **OAuth 2.0 (3LO)** . 

   - c. In the **Callback URL** field, enter the URL as per the connection mode of your data store. 

      - Federated search and actions: 

      - `https://vertexaisearch.cloud.google.com/oauth-redirect` . 

      - Data ingestion: 

      - `https://vertexaisearch.cloud.google.com/console/oauth/jira_oaut h.html` . 

**Note:** Actions always use **`https://vertexaisearch.cloud.google.com/oauthredirect`** . If you use the same OAuth 2.0 app for both data ingestion and actions, you must register both callback URLs in this app. If a required URL is missing, you'll see a **`redirect_uri is not registered for client`** error when authorizing. 

6. Click **Save changes** . 

#### Obtain client ID and client secret

To obtain the client ID and client secret, do the following: 

1. In the app page, from the navigation menu click **Distribution** . 

2. In the **Distribution** page, do the following: 

   - a. In the **Distribution controls** section, select **Edit** . 

- b. In the **Distribution status** section, select **Sharing** to enable editing other fields. 

- c. Enter information in the following mandatory fields: 

   - i. For **Vendor** , enter `Google` . 

   - ii. For **Privacy policy** , enter `https://policies.google.com` . 

   - iii. For **Does your app store personal data?** , select **Yes** . 

   - iv. Select **I confirm that I've implemented the personal data reporting API** checkbox. For more information, see Personal data reporting API 

(https://developer.atlassian.com/cloud/jira/platform/user-privacy-developerguide/) 

d. Click **Save changes** . 

3. In the app page, do the following: 

   - a. From the navigation menu, click **Settings** . 

   - b. From the settings page, copy your **Client ID** and **Client secret** . 

#### Obtain an instance ID and instance URL

1. Obtain the instance ID: 

   - a. Open a new tab, copy the instance URL, and append `/_edge/tenant_info` to the instance URL. For example, 

`https://` _`YOUR_INSTANCE`_ `.atlassian.net/_edge/tenant_info` . 

   - b. Navigate to the link to find the `cloudId` value. The `cloudId` is your instance ID. 

2. Obtain the instance URL: 

   - a. Go to atlassian.net (https://atlassian.net) and sign in with your _administrator_ account. 

   - b. Select the app you want to sync. For example, sync the first app. 

   - c. Find the instance URL (the subdomain in the address bar). 

#### Obtain project key

To obtain the project key, do the following: 

1. Sign in to your Jira Cloud account (https://www.atlassian.com/software/jira). 

2. From the navigation menu, select **Spaces** . 

3. Select the project for which you need the project ID. 

4. Open any issue within that project and click **Actions** . 

5. Click **Export XML** and download the file. 

6. Open the downloaded XML file and search for the tag containing `project id` . Copy the value associated with this tag for later use. 

#### Grant administrator roles

To grant the Jira _administrator_ the Discovery Engine Editor role in the Google Cloud console, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

2. Navigate to **IAM** . 

Go to IAM (https://console.cloud.google.com/iam-admin/iam?supportedpurview=project) 

3. Locate the user account which has _administrator_ access in Jira and click **Edit** . 

4. Grant the Discovery Engine Editor role to the _administrator_ . 

To grant a user an _administrator_ role in Atlassian, do the following: 

1. Sign in to Atlassian (https://atlassian.com) using an _organization administrator_ account. 

2. Click the menu icon and select your organization. Alternatively, you can go to admin.atlassian.com (https://admin.atlassian.com). 

3. On the **Admin** page, click the product and select the **Manage users** button. 

_Manage users_ 

4. Click **Groups** under **User management** . 

5. On the **Groups** page: 

   - a. Click **Create group** . 

   - b. Enter a name for the group. 

_Create group_ 

This group receives permissions required by the connector. Users added to this group inherit these permissions. The connector uses this group to authenticate and fetch documents. 

1. On the **Group page** , click **Add product** . 

2. Select **User access admin** as the role for **Jira** . 

3. Select **Product admin** as the role for **Jira administration** . 

_Jira user access administrator_ 

4. Click **Grant Access** . 

5. Click **Add group members** to add a user account or group members that the connector uses to authenticate and access the required resources. 

<!-- Start of picture text -->
Add group members<br><!-- End of picture text -->

#### Manage user visibility

To make the user's email visible to anyone in the Atlassian account, do the following: 

1. Sign in to the Atlassian Developer Console (https://developer.atlassian.com). 

2. Click the profile icon and select **Developer console** . 

3. Click the user profile icon and select **Manage account** . 

<!-- Start of picture text -->
Manage account<br><!-- End of picture text -->

4. Navigate to the **Profile and visibility** . 

<!-- Start of picture text -->
Profile and visibility<br><!-- End of picture text -->

5. Go to **Contact** and set the **Who can see this** as **Anyone** . 

<!-- Start of picture text -->
Contact<br><!-- End of picture text -->

To make the user's email visible to anyone in Jira, do the following: 

1. Sign in to Atlassian (https://id.atlassian.com/login) with your user credentials. 

2. Select a Jira app. 

3. Click **Settings** > **System** . 

4. Select **General Configuration** in the left pane. 

5. Click **Edit Settings** . 

6. For **User email visibility** , select **Public** . 

_Select email visibility_ 

7. Click **Update** . 

### Configure minimum application scopes

To perform the defined actions 

(/gemini/enterprise/docs/connectors/jira-cloud#supported-actions), you need to set up the following permissions for the Jira Cloud connector in the Atlassian platform. 

1. On the application page, click **Permissions** . 

2. Go to **Jira API** and click **Add** . 

**Note:** After adding the Jira API, the **Configure** button might take a moment to appear. If it doesn't show up immediately, try refreshing the page or waiting a few seconds. 

3. Click **Configure** . 

4. Go to the **Classic scopes** tab. 

5. Click **Edit scopes** and select the classic scopes as per your requirement from the following table: 

|Connection<br>mode|Permission|Purpose|
|---|---|---|
|Federated<br>search and<br>actions|`read:jira-`<br>`user`,<br>`read:jira-wor`|`k`<br>Allows the assistant to fetch and display search results<br>and user details in real-time.|
||`write:jira-`<br>`work`|Allows the assistant to modify work items (for example,<br>updating issue fields), manage comments or issues, and<br>upload attachments.|
||`manage:jira-`<br>`project`|Allows the assistant to manage Jira project settings and<br>create new project-level objects such as versions and<br>components. Required for the create and update project<br>actions.|
|Federated<br>search only|`read:jira-`<br>`user`,<br>`read:jira-wor`|`k`<br>Allows the assistant to search for and view issues,<br>projects, and user profiles.|
|Data ingestion<br>and actions|`read:jira-wor`|`k`Allows the assistant to perform broad data crawling and<br>indexing of work items.|
||`write:jira-`<br>`work`|Allows the assistant to perform write actions (creation,<br>updates, comments, and attachments) on work items<br>within the ingested environment.|
|Data ingestion|`read:jira-wor`|`k`Allows the assistant to crawl and index Jira content for<br>search availability.|

6. Confirm all the scopes are selected, and click **Save** . 

7. Go to the **Granular scopes** tab. 

8. Click **Edit scopes** and select the granular scopes as per your requirement from the following table: 

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

`read:sprint:jira-software` Allows the data store to read sprint details. 

9. Confirm all the scopes are selected, and click **Save** . 

**Note:** If you want to skip actions and use the data store for search, you can limit the permissions to just **`read`** permissions. **`write`** permissions are required only to perform the actions mentioned in Supported actions (/gemini/enterprise/docs/connectors/jira-cloud#supported-actions). 

### Install User Identity Accessor

To install the **User Identity Accessor for Jira Cloud** app on your Jira Cloud site, follow these steps: 

1. Navigate to Atlassian Marketplace 

(https://marketplace.atlassian.com/apps/1238248/user-identity-accessor-for-jira-cloud). 

2. Click **Get it now** . 

_Get it now_ 

3. From the **Select a site** list, select the Jira site where you want to install the app. 

**Note:** You must have administrator privileges for the selected Jira site to install the app. 

4. Click **Review** to authorize the required permissions and agree to the terms and conditions. 

5. Click **Get it now** to complete the app installation. 

Upon successful installation, a confirmation message appears: "Your app has been added to your instance and is ready for use." 

### Configure User Identity Accessor

After you've installed the **User Identity Accessor for Jira Cloud** app, configure an API key that your external system (for example, your Jira Cloud Connector) uses to securely call the app's web trigger to fetch emails. 

#### Access the configuration page

To access the **User Identity Accessor for Jira Cloud** app's configuration page, do the following: 

1. In your Jira Cloud instance, click the **Settings** ⚙ icon in the navigation menu. 

2. Select **Apps** from the menu. 

3. On the **Apps administration** page, locate your app, **User Identity Accessor for Jira Cloud** , in the **Manage apps** list. 

4. Click **Configure** or the link associated with your app. The app's dedicated configuration page opens within Jira Cloud. 

_Configure the User Identity Accessor for Jira Cloud app_ 

#### Set up the API key

To set up the API key on the configuration page, do the following: 

1. In the **API Key Configuration** section, specify the secret key for authenticating requests to the app's web trigger. You can authenticate requests using _either_ of the following methods: 

   - **Enter your own key** : Type or paste your own strong, unique API key into the **API Key** field. Use a key of at least 20–30 characters with a mix of uppercase letters, lowercase letters, numbers, and symbols. 

_Enter your own key_ 

**Generate a key** : Click the **Generate New Key** button. The system generates and displays a strong, random key in the field. 

_Generate a key_ 

**Important** : Immediately copy the API key displayed in the field. For security reasons, you might be unable to view the full key again after saving or navigating away. If lost, you need to set or generate a new one. 

2. Click **Save API Key** . A success message confirms that the key is securely saved. 

**Note:** The API key generated or created in this section serves as the value for the **Jira Identity Sync Forge Client Secret** field in the **Advanced Options** section during Connector setup (/gemini/enterprise/docs/connectors/jira-cloud/set-up-data-store#create-data-store). 

#### Test the app configuration

Verify if the **User Identity Accessor for Jira Cloud** app is configured correctly by sending a request from your external system and confirming that user email addresses are returned successfully. 

Get the web trigger URL 

1. On the **Apps administration** page, locate the **Webtrigger URL** section, which displays the unique URL specific to your Jira site and this app installation: 

Your external system must call this URL to request user emails. 

   - URL example: `https://` _`YOUR_INSTANCE_ID`_ `.hello.atlassiandev.net/x1/` _`WEBTRIGGER_ID`_ , where _`YOUR_INSTANCE_ID`_ is your Jira Cloud instance identifier and _`WEBTRIGGER_ID`_ is the unique identifier for the web trigger endpoint generated for your app. 

2. Click the **Copy URL** button or copy the entire URL. 

Configure your external system 

- Configure your external system that needs to fetch Jira user emails with the API key and web trigger URL obtained in the previous steps. 

- **Endpoint URL** : The web trigger URL you copied. 

- **HTTP Method** : `POST` 

**Required Headers** : 

**Content-Type** : `application/json` 

**X-Api-Key** : _`YOUR_API_KEY`_ 

Replace _`YOUR_API_KEY`_ with the API key you set or generated in the Set up the API key (#set-up-api-key) section. 

Example curl command 

This example demonstrates calling the **User Identity Accessor for Jira Cloud** web trigger, which accepts an array of account IDs and returns the email addresses. 

```
curl --location --request POST 'https://YOUR_INSTANCE_ID.hello.atlassian-
dev.net/x1/ENDPOINT_PATH' \
--header 'X-Api-Key: YOUR-API-KEY' \
--header 'Content-Type: application/json' \
--data-raw '{
  "accountIds": [
      "ACCOUNT_ID_1",
      "ACCOUNT_ID_2"
  ]
}'
```

Replace: 

- _`YOUR_INSTANCE_ID`_ with your Jira Cloud instance ID 

- _`ENDPOINT_PATH`_ with the API endpoint path 

- _`YOUR_API_KEY`_ with the API key you set or generated in the Set up the API key (#set-up-api-key) section 

- _`ACCOUNT_ID`_ with Atlassian account IDs that you want to target 

**Expected response** 

```
[{"accountId":"ACCOUNT_ID_1","emailAddress":"EMAIL_ADDRESS_1"},
{"accountId":"ACCOUNT_ID_2","emailAddress":"EMAIL_ADDRESS_2"}]
```

Replace: 

- _`ACCOUNT_ID_X`_ with actual Atlassian account IDs 

- _`USER_EMAIL_X`_ with user email addresses returned from your API call 

Implement security best practices 

To confirm the security of your API key, follow these recommendations: 

- Store the API key securely within your Jira Cloud Connector's configuration. 

- Verify that all communication with the webhook URL occurs over HTTPS. This is the default for **User Identity Accessor for Jira Cloud** web triggers. 

#### Support for User Identity Accessor for Jira Cloud

Support offerings are available from Google for the **User Identity Accessor for Jira Cloud** app that can include maintenance and regular updates to keep the app up-to-date. If you encounter any issues or have questions specific to the app functionality, contact Google Cloud Support (https://support.cloud.google.com/portal/). For more information, see Getting Cloud Customer Care (/support/docs). 

Last updated 2026-10-14 UTC. 



## Jira Data Center connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc

The Jira Data Center data store for Gemini Enterprise lets you search and perform actions on your projects, issues, and users. 

The Jira Data Center connector supports the following connection modes, which have different launch stages: 

- **Federated search and actions** : Generally available (GA). 

- **Data ingestion** : In Private Preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

### Supported Jira Data Center versions

The Jira Data Center connector supports Jira Data Center version `9.4.8` and later. 

### Supported actions

When the Jira Data Center connector is enabled, the end user can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create issue|Create a new issue or ticket.|
|Update issue|Change the details of a ticket, like updating its summary, description,<br>priority, or assignee.|
|Change Issue|Change the status of an issue.|
|Status||
|Create comment|Add a comment on an issue.|
|Update comment|Modify an existing comment on an issue.|

Action Description Download Download an attachment from an issue. attachment 

Upload attachment Add an attachment to an issue. 

**Notes** : 

- Additional read-only actions are also available. 

The maximum file size for file uploads and downloads in Gemini Enterprise is 200 MB. 

### Required scopes

To enable Gemini Enterprise to perform necessary search, actions, and data ingestion, the following scopes are required: 

|Connection mode|Scope|sPurpose|
|---|---|---|
|Data ingestion|`READ`|Required to ingest Jira Data Center projects, comments, issues,<br>attachments, and worklogs.|
|Federated search<br>and actions|`WRITE`|Required to perform search and actions like creating issues,<br>updating issues, updating comments, and uploading attachments.|

For information about how to configure these scopes, see Set up OAuth 2.0 authentication and OAuth scopes 

(/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration#create-oauth-app-link). 

### Limitations

- Enforcing a VPC Service Controls perimeter on existing Jira Data Center data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and 

how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- When adding a data store to a new or existing application, it is recommended to add a data store with actions belonging to a single connector type. For example, don't associate two Jira Data Center data stores with actions enabled to the same application. 

- The Jira Data Center data store is supported only in Global, US, and EU locations. 

### What's next

- To create and configure a data store with Jira Data Center, see Set up a Jira Data Center data store (/gemini/enterprise/docs/connectors/jira-dc/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Jira Data Center data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/set-up-data-store

This page describes how to create a data store and connect Jira Data Center to Gemini Enterprise. 

### Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have configured your identity provider 

(/gemini/enterprise/docs/configure-identity-provider). 

Before you set up your connection, do the following: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

   - b. Locate the user account and click **Edit** . 

   - c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

      - (https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Complete the steps in Set up authentication and obtain client credentials (/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration#create-oauth-app-link) to get the client ID and client secret, and set up OAuth scopes. 

3. If your Jira Data Center instance uses a private IP, publish a Private Service Connect producer service (/vpc/docs/configure-private-service-connect-producer) for your Jira Data Center instance. For more information about using Private Service Connect to connect Gemini Enterprise to self-hosted data sources, see Introduction to self-hosted data sources 

(/gemini/enterprise/docs/introduction-to-self-hosted). 

If you are using the data ingestion connection mode, you must meet these additional requirements: 

1. Verify that you have the Jira System Administrators permission (/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration#create-jira-user) to fetch Access Control List (ACL) information. 

2. If you have set up issue-level security (https://confluence.atlassian.com/adminjiraserver/configuring-issue-level-security938847117.html) 

in Jira, install the Permission Accessor for Jira Data Center plugin (https://marketplace.atlassian.com/apps/1237927/permission-accessor-for-jira-datacenter?hosting=datacenter&tab=installation) 

. This plugin provides REST endpoints to Gemini Enterprise. These endpoints enable Gemini Enterprise to retrieve space permission details, content restrictions, and email addresses of licensed users. This information is then used to ensure that the correct permissions are applied within the Gemini Enterprise search experience. 

### Create the Jira Data Center data store

To create the Jira Data Center data store, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

**Note:** To access the unified flow, your project must be on the allowlist. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Jira Data Center** , and click **Select** . 

6. In the **Data** section: 

- a. In the **Connector mode** section, select **Data ingestion** or **Federated search** . 

**Note: Data ingestion** is in Private Preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

- b. Click **Continue** . 

- c. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

   - i. Provide the authentication details. 

For **Federated search** , provide the following details: 

- **Instance URI:** The base URL of your Jira Data Center instance, for example, `https://jira.yourcompany.com` . 

**Note:** Ensure the URL includes the protocol ( **`https://`** ) and does not end with a trailing slash. 

- **Client ID:** The unique identifier for the OAuth application registered with Jira Data Center. 

- **Client secret:** The Secret Manager secret that contains the client secret for authenticating requests. 

To obtain these credentials, see Set up authentication and obtain client credentials 

(/gemini/enterprise/docs/connectors/jira-dc/jira-dcconfiguration#create-oauth-app-link) 

For **Data ingestion** , select one of the following authentication methods: **Username** and **Password** , **Personal access token** , or **API token** , and then enter the required details. 

ii. Click **Continue** . 

- d. From the **Destination type** list, select **Public** or **Private** . 

   - If you selected the **Public** destination type, for **Domain URL** , enter your public URL. This must match the instance URI. 

   - If you selected the **Private** destination type, enter the following information: 

      - i. **Service attachment** : Enter your Private Service Connect service attachment. To obtain this, you need to publish a Private Service Connect producer service (https://cloud.google.com/vpc/docs/configure-private-service-connectproducer) 

for your Jira Data Center instance. 

- ii. If the region of your Private Service Connect service attachment is different from the region of your data store, select the **Enable PSC Global Access** checkbox. 

iii. For an instance with a Domain URL: 

- Optional: **Base domain name** : Enter your base domain. Specify a unique and granular base domain name (for example, `jira.example.com` ) rather than a shared root domain (for example, `example.com` ) . If you have multiple data connectors in the same project, such as both Jira Data Center and Confluence Data Center, ensure each uses its own full instance domain as the base domain to avoid network collisions. Two data connectors using Private Connectivity with the same base domain name cannot be created in the same project. 

- **Domain URL** : Enter your domain URL. This must match the instance URI. 

Optional: **Destination port** : Enter your destination port. 

iv. For an instance without a Domain URL: 

**Destination port** : Enter your destination port. 

**Note:** Private connectivity is required when connecting to private, onpremises authentication endpoints. 

e. Click **Continue** . 

f. Optional: Click **Advanced options** . 

If you selected **Federated search** , do the following: 

- i. If you enable the **SSL settings** checkbox, select a **Trust Model** from **Private** , **Public** , or **Insecure** , and then configure the required fields. For more information on trust models, see Trust models (/certificate-authority-service/docs/trust-model). 

   - **Public** : Use this option if your Jira Data Center instance uses certificates issued by a publicly trusted CA. 

   - **Private** : Use this option if your Jira Data Center instance uses certificates signed by a private or internal CA. 

   - **Insecure** : This option bypasses certificate validation. It is not recommended for production environments as it can expose your connection to security risks. 

The following fields are common to all Trust Models: 

- **Keystore Client Certificate** : The client certificate in PEM format. For example, `-----BEGIN CERTIFICATE----\n...\n-----END CERTIFICATE-----` . 

- **Keystore Client Private Key** : The private key for the client certificate in PEM format. 

- **Keystore Client Private Key Passphrase** : The passphrase for the client private key, if applicable. 

The following additional detail is required for the **Private** Trust Model: 

**Private Certificate** : The public certificate of the private CA in PEM format. 

- ii. You can refine the scope of your searches and actions by specifying which Jira Data Center project keys to include or exclude. You can only mutate or retrieve data within the included projects. Requests for out-of-scope data either fail or return no results. 

You can add filters to the data store using the Google Cloud console or API: 

ConsoleREST (#rest) (#console) 

Note: When entering multiple project keys, separate each key with a comma. You can also copy and paste a list directly from a CSV file. 

- i. In the Project filter section: 

   - Choose the filter type: **Include in search** or **Exclude from search** . 

In the **Project filter** field, enter the exact Jira Data Center project keys to filter (for example, `ENG, HR, SUPPORT` ) . 

If you selected **Data ingestion** , do the following: 

   - i. Select the **Enable Static IP Addresses** checkbox. After creating the data store, you must allowlist the registered static IPs to ensure sync runs succeed. For more information, see Configure static IP egress 

      - (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

   - ii. In the **Max QPS** field, specify the maximum number of queries sent to the Jira Data Center data store per second. 

   - iii. Select the **Enable Custom Fields** checkbox. If enabled, the data store fetches custom fields from the Jira Data Center. 

   - iv. If required, select the **Proxy settings** and **SSL settings** checkboxes to enable them. 

- g. Click **Continue** . 

- h. In the **Entities to search** (if you selected **Federated search** ) or **Entities to sync** (if you selected **Data ingestion** ) section: 

   - i. Select all the required entities. 

   - ii. If you selected **Federated search** , proceed to the next step. 

iii. If you selected **Data ingestion** , continue with the following steps: 

- i. **Optional:** To sync specific projects, do the following: 

   - i. Click **Filter** . 

   - ii. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included in the index, select the **Include in the index** checkbox. 

   - iii. Enter the keys. Press **Enter** after each key. 

   - iv. Click **Save** . 

- ii. To configure the sync schedule, do the following: 

   - i. In the **Sync frequency** list, select a sync frequency. 

      - To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options** . 

   - ii. In the **Incremental sync frequency** list, select an incremental sync frequency. 

For more information, see Sync schedules (https://cloud.google.com/gemini/enterprise/docs/introduction-toconnectors-and-data-stores#sync-schedules) . 

7. Click **Continue** . 

8. If you selected **Federated search** , in the **Actions** section, from the **Select Jira Data Center actions to enable** list, choose the actions to enable for the data store. 

**Note:** If you skip adding actions in this step, you can add them later. For more 

information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

(/gemini/enterprise/docs/manage-actions). 

9. Click **Continue** . 

10. In the **Configuration** section: 

- a. From the **Multi-region** list, select the location for your data connector. 

- b. In the **Your data connector name** field, enter a name for your connector. 

- c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

   - Optional: If you haven't configured single-region keys, click **Go to settings page** to do so. For more information, see Register a single-region key for third-party connectors 

   - (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

Select **Google-managed encryption key** or **Cloud KMS key** . 

- If you selected **Cloud KMS key** : 

   - In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

11. Click **Continue** . 

12. In the **Billing** section, select **General pricing** or **Configurable pricing** . For more information, see Verify the billing status of your projects (https://cloud.google.com/billing/docs/how-to/verify-billing-enabled) and Licenses (/gemini/enterprise/docs/licenses). 

13. Click **Continue** . 

14. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data stores** page. 

15. If you selected the **Private** destination type and configured your Private Service Connect producer service 

   - (https://cloud.google.com/vpc/docs/configure-private-service-connect-producer) to **Accept connections for selected projects** (explicit approval), do the following: 

      - a. In the Google Cloud console, search for `Private Service Connect` and go to the **Private Service Connect** page. 

      - b. Click the **Published services** tab. 

      - c. Click the name of the Private Service Connect service corresponding to your Jira Data Center data store. 

      - d. In the **Connected projects** section, select the checkbox next to the Gemini Enterprise tenant project for the data store, and then click **Accept project** . The Gemini Enterprise tenant project ID ends in `-tp` . 

The data store status remains as **Creating** in the **Data Stores** page until you click **Accept project** on the service details page within Private Service Connect. After you click **Accept project** , the data store status changes to **Active** . 

To verify the state of the data store, do the following in the **Data stores** page: 

1. Navigate to the newly created data store in the data store list and monitor its state until it changes to **Active** . 

2. When the data store state changes from **Creating** to **Active** , the Jira Data Center connector is ready to be used. 

After creating the data store: 

- Create an app (/gemini/enterprise/docs/create-app). 

- Connect it to the Jira Data Center data store 

- (/gemini/enterprise/docs/connect-existing-data-store). 

- Add filters to the Jira Data Center data store 

- (/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store). 

- Authorize (/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to Jira Data Center before executing any queries. 

For information on permissions required to perform search, see Required scopes (/gemini/enterprise/docs/connectors/jira-dc#set-up-permissions). 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Jira Data Center and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Jira Data Center API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Jira Data Center API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Jira Data Center. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Jira Data Center API. 

### What's next

- To provide a user interface for querying your Jira Data Center data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Jira Data Center data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To add filters to the data store, see Add flters to a Jira Data Center data storei (/gemini/enterprise/docs/connectors/jira-dc/add-filters-to-jira-data-store). 

- To manage the list of actions, see View and manage actions 

- (/gemini/enterprise/docs/manage-actions). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Jira Data Center configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/jira-dc/jira-dc-configuration

**Private preview:** Creating and using a data store using data ingestion is in private preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

To successfully connect Gemini Enterprise to your Jira Data Center instance, complete the following configuration steps. 

### Create a user and grant administrator access

To create a new user and add the user to the administrator group, do the following: 

1. Sign in to your Jira Data Center instance at the base URL with administrator credentials. The base URL is typically in the format `https://jira.yourcompany.com` . 

2. To create a new user, follow these steps: 

   - a. Click the settings icon and select **User management** from the list. 

   - b. Enter the administrator credentials, if prompted. 

   - c. In the **Administration** page, click **Create user** . 

   - d. Enter the email address, full name, username, and password. 

   - e. Click **Create user** . 

3. To add the newly created user to the administrators group, follow these steps: 

   - a. Click **Groups** from the navigation menu. 

   - b. Search for the `jira-administrators` group and open it. 

   - c. Click **Add/Remove Users** and add the newly created user to this group. 

### Set up OAuth 2.0 authentication and OAuth scopes

To set up an incoming external application link using OAuth 2.0 in Jira Data Center and obtain the client ID and client secret, complete the following steps. You must have administrator privilege (#create-jira-user) or the help of a Jira Data Center administrator to complete this step. 

1. Sign in to your Jira Data Center instance at the base URL with administrator credentials. The base URL is typically in the format `https://jira.yourcompany.com` . 

2. Click the settings icon and select **Jira Administration** from **Applications** . 

3. In the navigation menu, click **Application links** from **Integrations** . 

4. On the **Application links** page, click **Create link** . 

5. In the **Create link** modal, configure the following: 

   - **Application type** : Select **External application** . 

   - **Direction** : Select **Incoming** . 

   - Click **Continue** . 

6. Configure the OAuth 2.0 details: 

   - **Name** : Enter a descriptive name for the application link. 

   - **Redirect URL** : Enter the following redirect URI: 

      - `https://vertexaisearch.cloud.google.com/oauth-redirect` 

   - **OAuth scopes** : Select the `READ` or `WRITE` scope for the OAuth App, based on your connection mode: 

|Connection mode|ScopePurpose|
|---|---|
|Data ingestion|`READ` Required to ingest Jira Data Center projects, comments, issues,<br>attachments, and worklogs.|
|Federated search<br>and actions|`WRITE`Required to perform search and actions like creating issues,<br>updating issues, updating comments, and uploading<br>attachments.|

7. Click **Continue** . The client ID and client secret are automatically generated and displayed. 

   - **Client ID (Consumer Key)** : Copy the unique ID provided. 

   - **Client Secret (Shared Secret)** : Copy the client secret and store it securely, for example, in a password manager. The secret is displayed only once. If lost, you must create a new application link to generate new credentials. 

8. Click **Save** . The newly created application link will appear in the list on the **Application links** page. 

Last updated 2026-10-14 UTC.
