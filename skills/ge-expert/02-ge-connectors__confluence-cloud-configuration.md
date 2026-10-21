# Gemini Enterprise: connectors and data stores / Confluence Cloud configuration to Dropbox connector: overview
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 279-313, extracted 2026-10-18

Contains:
- Confluence Cloud configuration (pages 279-293) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config
- Confluence Data Center connector: overview (pages 294-296) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc
- Set up a Confluence Data Center data store (pages 297-307) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/set-up-data-store
- Confluence Data Center configuration (pages 308-310) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenter-configuration
- Dropbox connector: overview (pages 311-313) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox

## Confluence Cloud configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config

This page describes how to set up and configure your Confluence Cloud instance before creating the Confluence Cloud data store. 

### Set up authentication and permissions

You need to set up authentication and permissions in the Atlassian administrator account center. This is crucial for allowing the connector to access and synchronize data. The Confluence Cloud connector supports various authentication methods, such as OAuth client credentials or API tokens. 

#### Create an OAuth 2.0 app

To create an OAuth 2.0 app for authentication, follow these steps to set up the application in your Atlassian Developer Console and obtain the necessary client ID and client secret. 

Verify Confluence organization administrator access 

To verify Confluence organization administrator access, do the following: 

1. Sign-in to Atlassian (https://id.atlassian.com/login) with your user credentials. 

2. Select the **Confluence** app. 

3. Click **Settings** . 

If you see the **System** option under **Confluence settings** , you have Confluence _organization administrator_ access. Otherwise, request your Confluence organization administrator to provide access. 

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

6. In the **Callback URL** field, enter the URL as per the connection mode of your data store. 

      - Data ingestion and actions: 

      - `https://vertexaisearch.cloud.google.com/console/oauth/confluence_oau th.html` 

      - Federated search and actions: 

      - `https://vertexaisearch.cloud.google.com/oauth-redirect` 

7. Click **Save changes** . 

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

      - iv. Select **I confirm that I've implemented the personal data reporting API** checkbox. 

   - d. Click **Save changes** . 

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

#### Grant administrator roles

To grant the Confluence _administrator_ the Discovery Engine Editor role in the Google Cloud console, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

2. Navigate to **IAM** . 

Go to IAM (https://console.cloud.google.com/iam-admin/iam?supportedpurview=project) 

3. Locate the user account that has _administrator_ access in Confluence and click the **Edit** icon . 

4. Grant the Discovery Engine Editor role to the _administrator_ . 

To grant a user an _administrator_ role in Atlassian, do the following: 

1. Sign in to Atlassian (https://atlassian.com) using an _organization administrator_ account. 

2. Click the menu icon and select your organization. Alternatively, you can go to admin.atlassian.com (https://admin.atlassian.com). 

3. On the **Admin** page, click the product and select the **Manage users** button. 

4. Click **Groups** under **User management** . 

5. On the **Groups** page: 

   - a. Click **Create group** . 

   - b. Enter a name for the group. 

This group receives permissions required by the connector. Users added to this group inherit these permissions. The connector uses this group to authenticate and fetch documents. 

1. On the **Group page** , click **Add product** . 

2. Select **User access admin** as the role for **Confluence** . 

3. Select **Product admin** as the role for **Confluence administration** . 

4. Click **Grant Access** . 

5. Click **Add group members** to add a user account or group members that the connector uses to authenticate and access the required resources. 

#### Configure minimum application scopes

To configure OAuth 2.0 and retrieve the required credentials for your Confluence connector setup, do the following: 

1. To configure scopes, do the following: 

   - a. Click **Permissions** . 

   - b. Add the necessary Confluence API scopes: 

      - i. Go to **Confluence API** . 

      - ii. Click **Add > Configure** . 

      - iii. Go to the **Granular scopes** tab and click **Edit scopes** . For federated search, some scopes might be listed under **Classic Scopes** . 

      - iv. Select the required scopes according to your connection mode. 

**Note:** The following table outlines the permissions required for each connection mode. If you enable **Actions** for either the **Federated search** or **Data ingestion** connection mode, also select the permissions listed in the **Actions** row. 

|Usage<br>reason|Permission<br>Description|
|---|---|
|Data<br>ingestion|`read:content-`<br>`details:confluenc`<br>`e`<br>Allows the data store to read content details in<br>Confluence.|
||`read:attachment:c`<br>`onfluence`<br>Allows the data store to download and read<br>attachments.|
||`read:comment:conf`<br>`luence`<br>Allows the data store to read comments.|
||`read:page:conflue`<br>`nce`<br>Allows the data store to read pages.|
||`read:whiteboard:c`<br>`onfluence`<br>Allows the data store to read whiteboards.|
||`read:space:conflu`<br>`ence`<br>Allows the data store to read spaces.|
||`read:group:conflu`<br>`ence`<br>Allows the data store to read groups.|
||`read:user:conflue`<br>`nce`<br>Allows the data store to read users.|
||`read:content.`<br>`metadata:confluen`<br>`ce`<br>Allows the data store to read content metadata.|
||`read:configuratio`<br>`n:confluence`<br>Allows the data store to read configurations.|
|Federated<br>search|`search:confluence`Allows the data store to perform search queries in<br>Confluence.|

|Usage<br>reason|Permission|Description|
|---|---|---|
|Actions|`write:page:conflu`<br>`ence`|Allows the data store to create and update pages<br>in Confluence.|
||`write:attachment:`<br>`confluence`|Allows the data store to upload attachments to<br>Confluence pages.|
||`write:blogpost:co`<br>`nfluence`|Allows the data store to create and update<br>Confluence blog posts.|
||`write:space:confl`<br>`uence`|Allows the data store to create and update<br>Confluence spaces.|
||`write:confluence-`<br>`space`|Allows the data store to manage Confluence<br>space information, including create, update, and<br>delete operations.|
||`write:confluence-`<br>`content`|Allows the data store to write content in<br>Confluence.|
||`write:confluence-`<br>`file`|Allows the data store to upload attachments to<br>Confluence.|
||`read:attachment:c`<br>`onfluence`|Allows the data store to download and read<br>attachments.|
||`read:blogpost:con`<br>`fluence`|Allows the data store to read blog posts.|
||`read:comment:conf`<br>`luence`|Allows the data store to read comments.|
||`read:configuratio`<br>`n:confluence`|Allows the data store to read configurations.|
||`read:confluence-`<br>`content.all`|Allows the data store to read all Confluence<br>content.|
||`read:confluence-`<br>`space.summary`|Allows the data store to read space summaries.|
||`read:content-`<br>`details:confluenc`<br>`e`|Allows the data store to read content details in<br>Confluence.|

Usage Permission Description reason `read:content.` Allows the data store to read content metadata. `metadata:confluen ce read:group:conflu` Allows the data store to read groups. `ence read:page:conflue` Allows the data store to read pages. `nce read:space:conflu` Allows the data store to read spaces. `ence read:space-` Allows the data store to read space details. `details:confluenc e read:task:conflue` Allows the data store to read tasks. `nce read:user:conflue` Allows the data store to read users. `nce read:whiteboard:c` Allows the data store to read whiteboards. `onfluence search:confluence` Allows the data store to perform search queries in Confluence. 

- c. Add User Identity API scopes. The `read:me` scope is required when Actions are enabled for the data store: 

   - i. Go to **User Identity API** . 

   - ii. Click **Add > Configure** . 

iii. Go to the **Granular scopes** tab and click **Edit scopes** . 

- iv. Select the `read:me` scope. 

Usage reason Permission Description 

Actions `read:me` Allows the data store to read current user information. 

d. Confirm that all the scopes are selected and save your changes. 

#### Set up an API token in Confluence

If you plan to use an API token for authentication, you must create an API token without scopes. This data store doesn't support API tokens with scopes. 

1. Sign in to Atlassian Console 

(https://id.atlassian.com/manage-profile/security/api-tokens). 

2. Click **Create API token** . 

3. Enter a name for the API token. 

4. Select an expiration date for the API token. The token expiration period ranges from 1 to 365 days. 

5. Click **Create** . 

6. Save the token for later use. 

#### Manage user visibility

To make the user's email visible to anyone in the Atlassian account, follow these steps: 

1. Sign in to the Atlassian Developer Console (https://developer.atlassian.com). 

2. Click the profile icon and select **Developer console** . 

3. Click the user profile icon and select **Manage account** . 

4. Navigate to **Profile and visibility** . 

5. Go to **Contact** and set the **Who can see this** as **Anyone** . 

To make the user's email visible to anyone in Confluence, follow these steps: 

1. Sign in to Atlassian (https://id.atlassian.com/login) with your user credentials. 

2. Select a Confluence app. 

3. Click **Settings** > **System** . 

4. Select **General Configuration** in the left pane. 

5. Click **Edit Settings** . 

6. For **User email visibility** , select **Public** . 

7. Click **Update** . 

### Install and configure User Identity Accessor for Confluence Cloud

If user email addresses aren't publicly accessible by default due to privacy settings in Confluence Cloud, you must install the **User Identity Accessor for Confluence Cloud** app to securely retrieve user email addresses. If user email addresses are already publicly visible, you might not need to install the app. For more information about restricted email visibility, see Manage user visibility and grant roles 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#manage-users). 

#### Roles and permissions

To install and configure the **User Identity Accessor for Confluence Cloud** app, you must have the appropriate administrative role and grant the required app-level permissions. 

- **Required role** : You must be a `Confluence Site administrator` to install and configure the app. 

- **App-level permissions** : You must grant the following permissions during the app installation: 

   - `Read Email Address` : Allows the app to securely retrieve user email addresses, even when profile visibility is restricted. 

   - `App Storage scope` : Enables the app to read and write to its storage device. 

#### Install User Identity Accessor for Confluence Cloud

To install the **User Identity Accessor for Confluence Cloud** app on your Confluence site, follow these steps: 

1. Navigate to Atlassian Marketplace 

(https://marketplace.atlassian.com/apps/1238254/user-identity-accessor-for-confluencecloud) 

2. Click **Get it now** . 

_Get it now_ 

3. From the **Select a site** list, select the Confluence site where you want to install the app. 

**Note:** You must have administrator privileges for the selected Confluence site to install the app. 

4. Click **Review** to authorize the required permissions and agree to the terms and conditions. 

5. Click **Get it now** to complete the app installation. 

Upon successful installation, a confirmation message appears: "Your app has been added to your instance and is ready for use." 

#### Configure User Identity Accessor for Confluence Cloud

After you've installed the **User Identity Accessor for Confluence Cloud** app, configure an API key that your external system (for example, your Confluence Cloud data store) uses to securely call the app's webtrigger to fetch emails. 

Access the configuration page 

To access the **User Identity Accessor for Confluence Cloud** app's configuration page in Confluence Cloud, follow these steps: 

1. In your Confluence Cloud instance, click the **Settings** ⚙ icon in the navigation menu. 

2. Select **Apps** from the menu. 

3. On the **Apps administration** page, locate your app, **User Identity Accessor for Confluence Cloud** , in the **Manage apps** list. 

4. Click **Configure** or the link associated with your app. The app's dedicated configuration page opens within Confluence. 

Set up the API key 

To set up the API key on the configuration page, follow these steps: 

1. In the **API Key Configuration** section, specify the secret key for authenticating requests to the app's webtrigger. You can authenticate requests using _either_ of the following methods: 

   - **Enter your own key** : Type or paste your own strong, unique API key into the API Key field. Use a key of at least 20–30 characters with a mix of uppercase letters, lowercase letters, numbers, and symbols. 

   - **Generate a key** : Click the **Generate New Key** button. The system generates and displays a strong, random key in the field. 

**Important** : Immediately copy the API key displayed in the field. For security reasons, you might be unable to view the full key again after saving or navigating away. If lost, you need to set or generate a new one. 

2. Click **Save API Key** . A success message confirms that the key is securely saved. 

**Note:** The API key generated or created in this section serves as the value for the **Confluence Identity Sync Forge Client Secret** field in the **Advanced Options** section during data store setup 

(/gemini/enterprise/docs/connectors/confluence-cloud/set-up-data-store#create-datastore) 

Test the app configuration 

Verify that the User Identity Accessor for Confluence Cloud app is configured correctly by sending a request from your external system and confirming that user email addresses are returned successfully. 

**Get the webtrigger URL** 

1. On the **Apps administration** page, locate the **Webtrigger URL** section, which displays the unique URL specific to your Confluence site and this app installation: 

   - Your external system must call this URL to request user emails. For example, `https://` _`YOUR_INSTANCE_ID`_ `.hello.atlassiandev.net/x1/` _`WEBTRIGGER_ID`_ , where _`YOUR_INSTANCE_ID`_ is your Confluence Cloud instance identifier and _`WEBTRIGGER_ID`_ is the unique identifier for the webtrigger endpoint generated for your app. 

2. Click the **Copy URL** button or copy the entire URL. 

**Configure your external system** 

- Configure your external system that needs to fetch Confluence user emails with the API key and webtrigger URL obtained in the previous steps. 

   - **Endpoint URL** : The webtrigger URL you copied. 

   - **HTTP Method** : `POST` 

   - **Required Headers** : 

**Content-Type** : `application/json` 

**X-Api-Key** : _`YOUR_API_KEY`_ 

Replace _`YOUR_API_KEY`_ with the API key you set or generated in the Set up the API key 

(/gemini/enterprise/docs/connectors/confluence-cloud/third-party-config#setup-api-key) section. 

**Example curl command** 

This example demonstrates calling the **User Identity Accessor for Confluence Cloud** webtrigger, which accepts an array of account IDs and returns the email addresses. 

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

- _`YOUR_INSTANCE_ID`_ with your Confluence Cloud instance ID 

- _`ENDPOINT_PATH`_ with the API endpoint path 

- _`YOUR_API_KEY`_ with the API key you set or generated in the Set up the API key (/gemini/enterprise/docs/confluence-cloud/third-party-config#set-up-api-key) section 

- _`ACCOUNT_ID`_ with Atlassian account IDs you want to target 

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

- Store the API key securely within your Confluence Cloud data store's configuration. 

- Verify that all communication with the webhook URL occurs over HTTPS. This is the default for **User Identity Accessor for Confluence Cloud** webtriggers. 

#### Support for User Identity Accessor for Confluence Cloud

Support offerings are available from Google for the **User Identity Accessor for Confluence Cloud** app that can include maintenance and regular updates to keep the app up to date. If you encounter any issues or have questions specific to the app functionality, contact Google Cloud Support 

(https://support.cloud.google.com/portal/). 

Last updated 2026-10-14 UTC. 



## Confluence Data Center connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc

The Confluence Data Center data store for Gemini Enterprise lets you search and perform actions on page content, attachments, and comments. 

The Confluence Data Center connector supports the following connection modes, which have different launch stages: 

- **Federated search and actions** : Generally available (GA). 

- **Data ingestion** : In Private Preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team 

- (https://cloud.google.com/contact). 

### Supported Confluence Data Center versions

The Confluence Data Center data store supports Confluence Data Center version 7.19.0 and later. 

### Supported actions

When the Confluence Data Center connector is enabled, the end user can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Upload attachment|Add an attachment to a Confluence Data Center page.|
|Download attachment|Download an attachment from a Confluence Data Center page.|

**Note** : The maximum file size for file uploads and downloads in Gemini Enterprise is 200 MB. 

### Required scopes

To enable Gemini Enterprise to perform necessary search, actions, and data ingestion, the following scopes are required: 

|Connection mode|Scope|sPurpose|
|---|---|---|
|Data ingestion|`READ`|Required to ingest Confluence page content, attachments, and<br>comments.|
|Federated search a<br>actions|nd<br>`WRITE`|Required to search Confluence page content, attachments, and<br>comments, and to upload attachments.|

For information about how to configure these scopes, see Set up OAuth 2.0 authentication and OAuth scopes 

(/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenterconfiguration#create-oauth-app-link) 

### Limitations

- Enforcing a VPC Service Controls perimeter on existing Confluence Data Center data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls 

- (/gemini/enterprise/docs/use-vpc-service-controls). 

- When creating a new application or adding a data store to an existing application, it's recommended that you add a data store with actions belonging to a single connector type. For example, don't associate two Confluence Data Center data stores with actions enabled to the same application. 

- The Confluence Data Center data store is supported only in Global, US, and EU locations. 

### What's next

- To create and configure a data store with Confluence Data Center, see Set up a Confluence Data Center data store 

- (/gemini/enterprise/docs/connectors/confluence-dc/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Confluence Data Center data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/set-up-data-store

This page describes how to create a data store and connect Confluence Data Center to Gemini Enterprise. 

### Before you begin

**Note:** To enforce data source access control and secure data in Google Gemini Enterprise, ensure that you have configured your identity provider (/gemini/enterprise/docs/configure-identity-provider). 

Before you set up your connection, do the following: 

1. Grant the Discovery Engine Editor role ( `roles/discoveryengine.editor` ). This role is required for the user to create the data store. To grant this role, do the following: 

   - a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

- b. Locate the user account and click **Edit** . 

- c. Grant the `Discovery Engine Editor` role to the user. For more information, see IAM roles and permissions 

(https://cloud.google.com/gemini/enterprise/docs/access-control). 

2. Complete the steps in Set up authentication and obtain client credentials (/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenterconfiguration#create-oauth-app-link) 

to get the client ID and client secret and set up OAuth scopes 

(/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenterconfiguration#create-oauth-app-link) 

3. If your Confluence Data Center instance uses a private IP, publish a Private Service Connect producer service 

(https://cloud.google.com/vpc/docs/configure-private-service-connect-producer). For more information about using Private Service Connect to connect Gemini Enterprise to self-hosted data sources, see Introduction to self-hosted data sources (/gemini/enterprise/docs/introduction-to-self-hosted). 

If you are using the data ingestion connection mode, you must meet these additional requirements: 

1. Verify that you have the Confluence Administrator permission (/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenterconfiguration#create-conf-user) 

to fetch the Access Control List (ACL) information. 

2. Install the Permission Accessor for Confluence Data Center plugin 

   - (https://marketplace.atlassian.com/apps/1237929/permission-accessor-for-confluencedata-center?hosting=datacenter&tab=installation) 

. This plugin provides REST endpoints to Gemini Enterprise. These endpoints enable Gemini Enterprise to retrieve space permission details, content restrictions, and email addresses of licensed users. This information is then used to ensure that the correct permissions are applied within the Gemini Enterprise search experience. 

### Create the Confluence Data Center data store

To create the Confluence Data Center data store, perform the following steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create 

(https://cloud.google.com/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** section, search for **Confluence Data Center** , and click **Select** . 

6. In the **Data** section: 

   - a. In the **Connector mode** section, select **Data ingestion** or **Federated search** . 

**Note: Data ingestion** is in Private Preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

- b. Click **Continue** . 

- c. In the **Authentication settings** section, configure authentication based on your chosen connection mode. 

   - i. Provide the authentication details: 

      - For **Federated search** , provide the following details: 

         - **Instance URI:** The base URL of your Confluence Data Center instance, for example, `https://your-confluenceinstance.com` . 

         - **Client ID:** The unique identifier for the OAuth application registered with Confluence Data Center. 

         - **Client secret:** The Secret Manager secret that contains the client secret for authenticating requests. 

To learn how to obtain these credentials, see Set up authentication and obtain client credentials 

(/gemini/enterprise/docs/connectors/confluence-dc/confluencedatacenter-configuration#create-oauth-app-link) 

For **Data ingestion** , choose between **Username** and **Password** credentials, **Personal access token** , or **API token** , and enter the authentication details accordingly. 

- ii. Click **Continue** . 

- d. From the **Destination type** list, select **Public** or **Private** . 

   - If you selected the **Public** destination type, for **Domain URL** , enter your public URL. 

   - If you selected the **Private** destination type, enter the following information: 

      - i. **Service attachment** : Enter your Private Service Connect service attachment. To obtain this, you need to publish a Private Service Connect producer service 

(https://cloud.google.com/vpc/docs/configure-private-service-connectproducer) 

for your Confluence Data Center instance. 

- ii. If the region of your Private Service Connect service attachment is different from the region of your data store, select the **Enable PSC Global Access** checkbox. 

iii. For an instance with a Domain URL: 

- Optional: **Base domain name** : Enter your base domain. Specify a unique and granular base domain name (for example, `confluence.example.com` ) rather than a shared root domain (for example, `example.com` ) . If you have multiple data connectors in the same project, such as both Jira Data Center and Confluence Data Center, ensure each uses its own full instance domain as the base domain to avoid network collisions. Two data connectors using Private Connectivity with the same base domain name cannot be created in the same project. 

- **Domain url** : Enter your domain URL. This must match the instance URI. 

Optional: **Destination port** : Enter your destination port. 

- iv. For an instance without a Domain URL: 

   - **Destination port** : Enter your destination port. 

**Note:** Private connectivity is required when connecting to private, onpremises authentication endpoints. 

e. Click **Continue** . 

f. Optional: Click **Advanced options** . 

- If you selected **Federated search** , do the following: 

   - If you enable the **SSL settings** checkbox, select a **Trust Model** from **Private** , **Public** , or **Insecure** , and then configure the required fields. For more information on trust models, see Trust models 

(https://cloud.google.com/certificate-authority-service/docs/trustmodel) 

   - **Public** : Use this option if your Confluence Data Center instance uses certificates issued by a publicly trusted CA. 

   - **Private** : Use this option if your Confluence Data Center instance uses certificates signed by a private or internal CA. 

   - **Insecure** : This option bypasses certificate validation. It is not recommended for production environments as it can expose your connection to security risks. 

- The following fields are common to all Trust Models: 

   - **Keystore Client Certificate** : The client certificate in PEM format. For example, `-----BEGIN CERTIFICATE----\n...\n-----END CERTIFICATE-----` . 

   - **Keystore Client Private Key** : The private key for the client certificate in PEM format. 

   - **Keystore Client Private Key Passphrase** : The passphrase for the client private key, if applicable. 

The following additional information is required for the **Private** Trust Model: 

                  - **Private Certificate** : The public certificate of the private CA in PEM format. 

      - If you selected **Data ingestion** , do the following: 

         - i. Select the **Enable Static IP Addresses** checkbox. After creating the connector, you must allowlist registered static IPs for sync runs to succeed. For more information, see Configure static IP egress 

            - (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

         - ii. In the **Max QPS** field, specify the maximum number of queries sent to the Confluence Data Center data store per second. 

         - iii. Select the **Enable Custom Fields** checkbox. If enabled, the connector fetches custom fields from the Confluence Data Center. 

         - iv. If required, select the **Proxy settings** and **SSL settings** checkboxes to enable them. 

- g. Click **Continue** . 

- h. In the **Entities to search** (if you selected **Federated search** ) or **Entities to sync** (if you selected **Data ingestion** ) section: 

   - i. Select all the required entities. 

   - ii. If you selected **Federated search** , proceed to the next step. 

   - iii. If you selected **Data ingestion** , continue with the following steps: 

         - i. **Optional:** To sync specific projects, do the following: 

               - i. Click **Filter** . 

               - ii. To filter entities out of the index, select the **Exclude from the index** checkbox, or to ensure that they are included in the index, select the **Include in the index** checkbox. 

               - iii. Enter the keys. Press **Enter** after each key. 

               - iv. Click **Save** . 

         - ii. To configure the sync schedule, do the following: 

- i. In the **Sync frequency** list, select a sync frequency. 

   - To schedule separate full syncs of entity and identity data, expand the menu in the **Full sync** section and then select **Custom options** . 

- ii. In the **Incremental sync frequency** list, select an incremental sync frequency. For more information, see Sync schedules 

(https://cloud.google.com/gemini/enterprise/docs/introduction-toconnectors-and-data-stores#sync-schedules) 

7. Click **Continue** . 

8. If you selected **Federated search** , in the **Actions** section, for **Select Confluence Data Center actions to enable** , choose the actions from the category to enable for the data store. 

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

Select **Google-managed encryption key** or **Cloud KMS key** . 

If you selected **Cloud KMS key** : 

In the **Key management type** list, select the appropriate type. 

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

      - c. Click the name of the Private Service Connect service corresponding to your Confluence Data Center data store. 

      - d. In the **Connected projects** section, select the checkbox next to the Gemini Enterprise tenant project for the data store, and then click **Accept project** . 

**Note:** The Gemini Enterprise tenant project ID ends in **`-tp`** . 

The data store status remains as **Creating** in the **Data Stores** page until you click **Accept project** on the service details page within Private Service Connect. After you click **Accept project** , the data store status changes to **Active** . 

To verify the state of the data store, do the following in the **Data stores** page: 

1. Navigate to the newly created data store in the data store list and monitor its state until it changes to **Active** . 

2. When the data store state changes from **Creating** to **Active** , the Confluence Data Center connector is ready to be used. 

After creating the data store: 

- Create an app (/gemini/enterprise/docs/create-app). 

- Connect it to the Confluence Data Center data store (/gemini/enterprise/docs/connect-existing-data-store). 

- Authorize (/gemini/enterprise/docs/create-app#user-authorization) Gemini Enterprise to Confluence Data Center before executing any queries. 

For information on permissions required to perform search, see Required scopes (/gemini/enterprise/docs/connectors/confluence-dc#set-up-permissions). 

### Data handling and query execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

#### Query execution

After you authorize Confluence Data Center and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Confluence Data Center API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

#### Data handling

When using third-party federated search, the following data handling rules apply: 

- Your query string is sent to the third-party search backend (Confluence Data Center API). 

- These third parties may associate queries with your identity. 

- If multiple federated search data sources are enabled, the query might be sent to all of them. 

- After the data reaches the third-party system, it is governed by that system's terms of service and privacy policies. 

**Note:** To improve accuracy, an LLM may rewrite your query before it is sent to Confluence Data Center. This rewritten query can incorporate information from your session's query history. As a result, parts of your query history might also be included in the query sent to the Confluence Data Center API. 

### What's next

- To provide a user interface for querying your Confluence Data Center data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Confluence Data Center data store 

- (/gemini/enterprise/docs/connect-existing-data-store). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## Confluence Data Center configuration

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/confluence-dc/confluence-datacenter-configuration

**Private preview:** Creating and using a data store using data ingestion is in private preview. You need to be on the allowlist to use the data ingestion data store. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

To connect Gemini Enterprise to your Confluence Data Center instance, complete the following configuration steps. 

### Create a user and grant administrator access

To create a new user and add the user to the administrator group, do the following: 

1. Sign in to your Confluence Data Center instance at the base URL with administrator credentials. The base URL is typically in the format `https://confluence.yourcompany.com` . 

2. To create a new user, follow these steps: 

   - a. Click the settings icon and select **User management** from the list. 

   - b. Enter the administrator credentials, if prompted. 

   - c. In the **Administration** page, click **Create user** . 

   - d. Enter the email address, full name, username, and password. 

   - e. Click **Create user** . 

3. To add the newly created user to the administrators group, follow these steps: 

   - a. Click **Groups** from the navigation menu. 

   - b. Search for the `confluence-administrators` group and open it. 

   - c. Click **Add/Remove Users** and add the newly created user to this group. 

### Set up OAuth 2.0 authentication and OAuth scopes

To set up an incoming external application link using OAuth 2.0 in Confluence Data Center and obtain the client ID and client secret, follow these steps. You must have administrator privilege (#create-conf-user) or the help of a Confluence Data Center administrator to complete this step. 

1. Sign in to your Confluence Data Center instance at the base URL with administrator credentials. The base URL is typically in the format `https://confluence.yourcompany.com` . 

2. Click the settings icon and select **Applications** from the list. 

3. In the navigation menu, click **Application links** . 

4. On the **Application links** page, click **Create link** . 

5. In the **Create link** modal, configure the following: 

   - **Application type** : Select **External application** . 

   - **Direction** : Select **Incoming** . 

   - Click **Continue** . 

6. Configure the OAuth 2.0 details: 

   - **Name** : Enter a name for the application link. 

   - **Redirect URL** : Enter the following redirect URI: 

      - `https://vertexaisearch.cloud.google.com/oauth-redirect` 

   - **OAuth scopes** : Select `READ` or `WRITE` based on your specific connection mode: 

|Connection mode|ScopePurpose|
|---|---|
|Data ingestion|`READ` Required to ingest Confluence page content, attachments,<br>and comments.|
|Federated search<br>and actions|`WRITE`Required to search Confluence page content, attachments,<br>and comments, and to upload attachments.|

7. Click **Continue** . The client ID and client secret are automatically generated and displayed. 

   - **Client ID (Consumer Key)** : Copy the unique ID provided. 

   - **Client Secret (Shared Secret)** : Copy the client secret and store it securely, for example, in a password manager. The secret is displayed only once. If lost, you must create a new application link to generate new credentials. 

8. Click **Save** . The newly created application link will appear in the list on the **Application links** page. 

Last updated 2026-10-14 UTC. 



## Dropbox connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/dropbox

The Dropbox data store for Gemini Enterprise lets you search and perform actions on your Dropbox data. 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Supported actions

When a Dropbox data store is configured and enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions: 

|Action|Description|
|---|---|
|Create folder|Create a folder in the user's Dropbox.|
|Copy file or folder|Copy a file or folder in the user's Dropbox.|
|Upload file|Upload a file to the user's Dropbox.|
|Download file|Download a file from the user's Dropbox.|

**Notes** : 

Additional read-only actions are also available. 

The maximum file size for file uploads and downloads in Gemini Enterprise is 50 MB. 

#### Minimum permissions for actions

To enable Gemini Enterprise to perform search and necessary actions for Dropbox, you need the following minimum permissions. 

|Scope|Description|
|---|---|
|account_info.read|Required to be registered for user-linked apps.|
|files.metadata.rea         i|idAllows the data store to read the metadata of files and folders in the user's<br>account.|
|files.content.read|Allows the data store to read file contents and download files from the<br>user's account.|
|files.content.write|Allows the data store to upload files to the user's account.|

For information about how to configure these permissions, see Dropbox configuration (/gemini/enterprise/docs/connectors/dropbox/config). 

### Limitations

The Dropbox data store for Gemini Enterprise has the following limitations: 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- Enforcing a VPC Service Controls perimeter on existing Dropbox data stores is not supported. To enforce VPC Service Controls, you must delete and recreate the data stores. For more information on VPC Service Controls and how to use actions after enabling VPC Service Controls, see Secure your app with VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

- The Dropbox data store is supported only in the `global` , `us` , and `eu` locations. 

### What's next

- To create and configure a Dropbox data store for use with Gemini Enterprise, see Set up a Dropbox data store 

(/gemini/enterprise/docs/connectors/dropbox/data-store). 

Last updated 2026-10-14 UTC.
