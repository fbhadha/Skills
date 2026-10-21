# Gemini Enterprise: platform, security, agents, cost, monitoring / Configure identity provider to Secure your app with VPC Service Controls
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 141-179, extracted 2026-10-18

Contains:
- Configure identity provider (pages 141-151) https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider
- Configure access controls for apps (pages 152-160) https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps
- Configure granular access controls for apps and data stores (pages 161-174) https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores
- Secure your app with VPC Service Controls (pages 175-179) https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls

## Configure identity provider

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider

To enforce data source access control and secure data in Gemini Enterprise, you must configure an identity provider. This involves setting up the identity provider and managing permissions for your data sources. Google uses your identity provider to identify the end user performing a search and determine if they have access to the documents that are returned as results. 

### Choose your identity provider type

The type of the identity provider you choose, depends on the data sources connected to your Gemini Enterprise app. Gemini Enterprise supports the following options: 

Identity provider type When to use 

Google Identity Google Identity is the recommended identity provider for Gemini Enterprise. 

Google Identity supports: 

- All first-party Google data sources that use data ingestion or data federation. You must use Google Identity (https://developers.google.com/identity) when connecting to Google Workspace (https://workspace.google.com/) data sources. 

- All third-party data sources that use data federation, where users authenticate directly with the third-party service using OAuth. 

- All third-party data sources that use data ingestion, with the exception of Microsoft 365 data sources, such as SharePoint, OneDrive, or Outlook, which require Microsoft Entra ID and Workforce Identity Federation. 

Note: To use a third-party identity provider with Google Identity, your identity provider must support OIDC or SAML 2.0. 

Before configuring Google Identity, determine the unique user attribute that your organization uses, which is typically the user's email. If users have more than one email address, you must add an email alias (https://support.google.com/a/answer/33327). 

|Third-party identity provider|When you connect Gemini Enterprise only to third-party data sources and you<br>already use a third-party identity provider that supports OIDC or SAML 2.0,<br>such as Microsoft Entra ID, Okta, or AD FS, you can use either<br>Google Identity<br>(/identity/docs/overview) or Workforce Identity Federation.|
|---|---|
||Note: Microsoft 365 data sources that connect using data ingestion require<br>Microsoft Entra ID and Workforce Identity Federation.|
||Google recommends using Google Identity for new setups. Existing customers<br>already using Workforce Identity Federation can choose to remain on<br>Workforce Identity Federation. For more information, see<br>Workforce Identity<br>Federation(/iam/docs/workforce-identity-federation).|
||Before configuring Workforce Identity Federation, determine the unique user<br>attributes that your organization uses and map them to Workforce Identity<br>Federation.|

**Caution:** If you change identity providers, users lose their existing chat history. Because chat history is tied to users' IDs from the original identity provider, switching providers gives users new IDs and effectively a fresh start. Chat history linked to their original IDs can't be retrieved. 

### Access control for Google Workspace connectors

When you use enterprise data grounding and search with Google Workspace connectors (such as **People from Google Workspace** or **Google Groups** ), Gemini Enterprise strictly respects the source system's access control lists (ACLs) and permissions. 

#### Core principle: No privilege escalation

A user interacting with Gemini Enterprise can only view and ground responses on information that they are already authorized to access directly in the source Google Workspace application. Gemini Enterprise never bypasses source system access controls or grants additional permissions. 

- **People from Google Workspace (Directory):** User visibility in search and grounding results respects your organization's Directory visibility settings. For example, if a user's visibility in the Google Workspace Directory is limited to their own department or organizational unit, they are only able to find colleagues within that department using Gemini Enterprise. They can't view profiles of employees in restricted departments. 

- **Google Groups:** Content discovery and grounding adhere to group membership and access settings. A user can only search and view content from Google Groups that they are a member of and have permission to view. Non-members can't discover or view discussions from private groups through Gemini Enterprise. 

#### Where to manage permissions

You don't configure access control and visibility settings in the Gemini Enterprise connector settings in the Google Cloud console. Instead, a Google Workspace administrator configures permission, membership, and visibility settings in the source system: 

- **User profile visibility:** The Google Workspace administrator configures user profile visibility in the Google Admin console. For more information, see Set up directory sharing (https://support.google.com/a/answer/1628008). 

- **Group access and membership:** The Google Workspace administrator configures group access and membership in Google Groups or the Google Admin console. For more information, see Set up and manage groups (https://support.google.com/a/answer/167097). 

### Workforce Identity Federation for third-party identity providers

This section describes how to configure Workforce Identity Federation for third-party identity providers. Optionally, you can verify if the Workforce Identity Federation set up works as expected. 

**Important:** The workforce identity pool admin roles give the administrators powerful permissions. For more information, see Workforce Identity Federation and pool administrators (/gemini/enterprise/docs/security-overview#pool-admins). 

#### Configure Workforce Identity Federation

For details on configuring Workforce Identity Federation with your third-party identity connector, see the following resources: 

|Identity provider|Resources|
|---|---|
|Entra ID|Note: When using data ingestion to connect to Microsoft data sources like SharePoint,<br>OneDrive, or Outlook, you must use Microsoft Entra ID groups to control document<br>access. This requires setting up Workforce Identity Federation with Microsoft Entra ID.<br>This setup is necessary even if you use a different identity provider for single sign-on<br>(SSO) with Microsoft Entra ID. However, this requirement does not apply if you are<br>connecting to a Microsoft data source using data federation.|
||Configure Workforce Identity Federation with Microsoft Entra ID and sign in users<br>(/iam/docs/workforce-sign-in-microsoft-entra-id)<br>Configure Workforce Identity Federation with Microsoft Entra ID and a large number of<br>groups(/iam/docs/workforce-sign-in-microsoft-entra-id-scalable-groups)<br>Configure SCIM in Microsoft Entra ID(/iam/docs/configure-scim-ms-entra). SCIM<br>(System for Cross-domain Identity Management) is necessary to fetch a large number<br>of groups from Entra ID for Gemini Enterprise and for autocomplete of user emails and<br>group names when users share agents and notebooks.|
|Okta|Configure Workforce Identity Federation with Okta and sign in users<br>(/iam/docs/workforce-sign-in-okta)<br>Configure SCIM in Okta(/iam/docs/configure-scim-okta). SCIM is necessary for<br>autocomplete of user emails and group names when users share agents and<br>notebooks.|
|OIDC or SAML 2.0|Configure Workforce Identity Federation with an identity provider (IdP) that supports<br>OIDC or SAML 2.0(/iam/docs/configuring-workforce-identity-federation)|

Configure attribute mapping 

Attribute mapping helps you connect your third-party identity information with Google using Workforce Identity Federation. 

When configuring attribute mapping in Workforce Identity Federation, consider the following: 

- The `google.subject` attribute is used for attribute mapping, license assignment, and sharing notebooks. We recommend mapping `google.subject` to the user's email address in lowercase, as license assignment is case sensitive. 

- If your organization has more than one unique identifier, map these unique organizational attributes using the `attribute.as_user_identifier_` _`number between 1 and 50`_ attribute. 

For example, if your organization uses both email and principal name as user identifiers across different applications, and the principal name is set as the `preferred_username` in your third-party identity provider, you can map it to Gemini Enterprise using the Workforce Identity Federation attribute mapping (for example, 

`attribute.as_user_identifier_1=assertion.preferred_username` ). 

The following examples show the required attribute mappings for common identity providers. You can add more attribute mappings to support additional unique identifiers, as described previously. 

- Entra ID with OIDC protocol (/iam/docs/workforce-sign-in-azure-ad#create-oidc-provider) This example uses the email to uniquely identify users. 

```
google.subject=assertion.email.lowerAscii()
google.groups=assertion.groups
google.display_name=assertion.given_name
```

- Entra ID with SAML protocol (/iam/docs/workforce-sign-in-azure-ad#create-saml-provider) This example uses the email to uniquely identify users. 

```
google.subject=assertion.attributes['http://schemas.xmlsoap.org/ws/2005/05/identity/claim
s/emailaddress'][0].lowerAscii()
google.groups=assertion.attributes['http://schemas.microsoft.com/ws/2008/06/identity/clai
ms/groups']
google.display_name=assertion.attributes['http://schemas.xmlsoap.org/ws/2005/05/identity/
claims/givenname'][0]
```

- Okta with OIDC protocol (/iam/docs/workforce-sign-in-okta#create-oidc-provider) This example uses the email to uniquely identify users. 

```
google.subject=assertion.email.lowerAscii()
google.groups=assertion.groups
```

- Okta with SAML protocol (/iam/docs/workforce-sign-in-okta#create-saml-provider) 

This example uses the subject assertion of the JWT to uniquely identify users. 

```
google.subject=assertion.subject.lowerAscii()
google.groups=assertion.attributes['groups']
```

#### Optional: Verify Workforce Identity Federation setup

To verify successful sign-ins and correct attribute mapping using the Workforce Identity Federation audit logging feature, do the following: 

1. Enable audit logs for the Data Access activity's Security Token Service API. 

- a. In the Google Cloud console, go to the **Audit Logs** page: 

Go to **Audit Logs** (https://console.cloud.google.com/iam-admin/audit) 

If you use the search bar to find this page, then select the result whose subheading is **IAM & Admin** . 

   - b. Select an existing Google Cloud project, folder, or organization. 

   - c. Enable the Data Access audit logs. 

      - i. See the Logging documentation for detailed steps on how to Enable audit logs (/logging/docs/audit/configure-data-access#config-console-enable). 

      - ii. For the **Security Token Service API** , select the **Admin Read** audit log type. For more information, see Example logs for Workforce Identity Federation 

      - (/iam/docs/audit-logging/examples-workforce-identity). 

2. Enable detailed logging in your workforce pool. The Workforce Identity Federation extended groups feature for Microsoft Entra ID doesn't produce detailed audit logging information. 

   - a. Go to the **Workforce Identity Pools** page: 

Go to Workforce Identity Pools (https://console.cloud.google.com/iam-admin/workforce-identity-pools) 

   - b. In the table, select the pool. 

   - c. Click the **Enable detailed audit logging** toggle to the on position. 

   - d. Click **Save Pool** . 

3. In the **Providers** section, click the **Sign in URL** for your provider, and sign in to Google Cloud console as a workforce pool user. 

4. See the audit logs that generated when you signed in. 

   - a. Go to the **Workforce Identity Pools** page: 

Go to Workforce Identity Pools (https://console.cloud.google.com/iam-admin/workforce-identity-pools) 

- b. In the table, select the pool you signed into. 

- c. Click **View** next to **Logs** . 

- d. On the audit log page clear the `protoPayload.resourceName` filter from the query. 

e. Click **Run query** . 

5. Check the audit logs for an entry with the 

   - `google.identity.sts.SecurityTokenService.WebSignIn` method that matches the sign-in timestamp. 

6. Confirm that the `metadata.mapped_attributes` field in the log matches the attribute that you used when configuring Workforce Identity Federation for third-party identity providers. 

For example: 

```
"metadata": {
  "mapped_attributes": {
    "attributes.as_user_identifier_1": "alex@admin.altostrat.com"
    "google.subject": "alex@altostrat.com"
    "google.groups": "[123abc-456d, efg-h789-ijk]"
  }
},
```

### Limitations

When connecting your data sources using a connector to create data stores, the following limitations apply: 

- 3000 readers are allowed per document. Each principal counts as a reader, where a principal can be a group or an individual user. 

You can select one identity provider type per location supported in Gemini Enterprise. 

- If the identity provider settings are updated by changing the identity provider type or the workforce pool, existing data stores won't automatically update to the new settings. You must delete and recreate these data stores to apply the new identity settings. 

- To set a data source as access-controlled, you must select this setting during data store creation. You can't turn this setting on or off for an existing data store. 

- To preview UI results for search apps that use third-party access control, you must sign in to the federated console or use the web app. See Preview your app 

- (/gemini/enterprise/docs/quickstart-gemini-enterprise#preview_your_app). 

### Connect to your identity provider

The following section describes how to connect to your identity provider using Google Cloud console. 

Before you begin 

Before connecting the identity provider, do the following: 

- Grant permissions to admins (/gemini/enterprise/docs/access-control#grant_permissions_to_admins). 

- If you are connecting a third-party identity provider using Workforce Identity Federation, configure Workforce Identity Federation. 

Connect identity provider 

To specify an identity provider for Gemini Enterprise and turn on data source access control, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/apps) 

2. Click **Settings** > **Authentication** . 

3. Click **Add identity provider** for the location you want to update. 

4. Click **Add identity provider** and select your identity provider type. If you select **3rd party identity** , you also need to select the workforce pool that applies for your data sources. 

5. Click **Save changes** . 

### Grant permissions to users

Users need the Gemini Enterprise User ( `roles/discoveryengine.agentspaceUser` ) role to access, manage, and share apps. 

|Identity provider type|Description|
|---|---|
|Google Identity|If you use Google Identity, Google recommends creating a<br>Google group<br>(https://groups.google.com) that includes all employees who use the app.<br>If you're a Google Workspace administrator, you can include all users in an<br>organization to a Google group by following the steps in<br>Add all your<br>organization's users to a group<br>(https://support.google.com/a/answer/9689259).<br>Grant the Gemini Enterprise User<br>(`roles/discoveryengine.agentspaceUser`) role to users. For more<br>information on adding the role, see<br>Grant permissions to your users<br>(/gemini/enterprise/docs/access-control#grant-role).|
|Third-party identity provider|Grant the Gemini Enterprise User<br>(`roles/discoveryengine.agentspaceUser`) role to your users and<br>workforce pool users in IAM policies<br>(/iam/docs/workforce-identity-federation#representing-workforce-users).<br>For more information on adding the role, see<br>Grant permissions to your<br>users(/gemini/enterprise/docs/access-control#grant-role).<br>Google recommends configuring group claims for your third-party identities.|

### Impact of identity provider setting changes on ingestion connectors

When you change identity settings, such as the identity provider or Workforce Identity Federation pool, existing data stores that use data ingestion are not automatically updated. To apply the new identity settings, you must delete and recreate the affected data stores. 

The following table summarizes which identity setting changes require data store recreation: 

|Change type|Requires data store<br>recreation|
|---|---|
|Switching between Google Identity and a third-Party identity provider|Yes|
|Completely changing to a new Workforce Identity Federation pool|Yes|
|Editing attribute mapping within the current identity provider|No|
|Switching to a new provider within the same Workforce Identity Federation pool. For<br>example, using Entra instead of Okta.|No|

### User identity changes

Gemini Enterprise associates a user's chat history, notebooks, and the agents that the user creates with the user's principal identifier. If you use Workforce Identity Federation, the principal identifier includes the value that your attribute mapping assigns to `google.subject` . For example: 

```
principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/
SUBJECT_ATTRIBUTE_VALUE
```

#### Impact of a subject value change

If the value that's mapped to `google.subject` changes for a user, then Gemini Enterprise treats the user as a new user. For example, this happens when the user's user principal name (UPN) or email address changes in Microsoft Entra ID and your attribute mapping uses that attribute. Principal identifiers are case-sensitive, so a change in letter case is also a change. 

After the change, the following applies: 

- The user can't access the chat history, notebooks, or agents that are associated with the previous principal identifier. 

- Gemini Enterprise doesn't migrate data from the previous principal identifier to the new principal identifier. 

- Licenses and IAM roles that are granted to the previous principal identifier don't apply to the new principal identifier. 

#### Prepare for a subject value change

To reduce the impact of a subject value change, do the following: 

- Before you change a user's UPN or email address in your identity provider, inform the user and ask them to share any private agents (/gemini/enterprise/docs/share-custom-agents) or notebooks that they want to keep. 

- Assign a Gemini Enterprise license to the new principal identifier, and grant the required roles to it. For more information, see Grant permissions to users (#grant_role). 

- Transfer ownership of the agents (/gemini/enterprise/docs/share-custom-agents#transfer-ownership) that the user shared with others to the new principal identifier. You can't transfer ownership of agents that aren't shared. 

### Troubleshoot authentication errors

If users get HTTP `401` errors that report invalid authentication credentials when they access Gemini Enterprise, check the following. 

#### Basic checks

- **Browser state** : Ask the user to clear the browser cache and cookies, or to sign in from an incognito or private browsing window. 

- **Signed-in account** : Make sure that the user signs in with the account that your identity provider configuration expects. If you use Workforce Identity Federation, the user's identity must match your attribute mapping. 

- **Device clock** : Make sure that the device clock is synchronized, for example, by using Network Time Protocol (NTP). Clock drift on the device can cause authentication to fail. 

#### Network and identity provider policies

- **Proxies and firewalls** : Proxies, firewalls, or secure web gateways that inspect TLS traffic can remove or change the `Authorization` header. Make sure that these devices don't modify requests to Google domains. 

- **Identity provider access policies** : Check whether access policies in your identity provider, such as Conditional Access policies in Microsoft Entra ID, block sign-in because of device compliance, IP address ranges, or location. 

- **Context-Aware Access** : If your organization uses Context-Aware Access with Google Cloud or Google Workspace, check whether an IP-based access level blocks the requests that Gemini Enterprise makes on the user's behalf. These requests originate from Google's servers, not from the user's network, so they don't match corporate IP ranges. Add an access level that allows the OAuth 2.0 client ID used by Gemini Enterprise, combined with the IPbased access level as an OR condition. Denied requests appear in your organization's audit logs for `contextawareaccess.googleapis.com` . 

- **DNS resolution** : Make sure that your DNS resolvers correctly resolve Google domains, including `*.google.com` and `*.googleapis.com` . 

#### Collect diagnostic information

If the error persists, capture a HAR (HTTP Archive) file and the browser console logs while you reproduce the error, and then contact Cloud Customer Care (/support/docs). HAR files can contain sensitive information, such as cookies and tokens. 

### What's next?

- If you have Cloud Storage or BigQuery data stores and you want to enforce access control on the data, then you must configure access controls for custom data sources (/gemini/enterprise/docs/identity). 

- If you connect to your own custom data source, learn how you can set up external identities (/gemini/enterprise/docs/identity-mapping). 

- Preview your app (/gemini/enterprise/docs/quickstart-gemini-enterprise#preview_your_app). 

- When you are ready to share the app with your users, you can turn on the app and share the URL with your user. Users need to sign in before they can access the app. For more information, see View the search web app 

- (/gemini/enterprise/docs/quickstart-gemini-enterprise#view_the_search_web_app). 

Last updated 2026-10-14 UTC. 



## Configure access controls for apps

URL: https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps

This page explains how a Gemini Enterprise admin can use the API to manage finegrained access control for individual Gemini Enterprise apps. 

If you need to configure granular, resource-level access controls across both apps and data stores, see Configure granular access controls for apps and data stores (/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores). 

By default, IAM permissions are often managed at the project level. App-level IAM allows for more granular control, enabling admins to: 

- Restrict user access to specific apps within the same Google Cloud project. 

- Align permissions with organizational needs and data silos for your Gemini Enterprise deployments. 

**Important:** Project-level IAM permissions take precedence over app-level policies. If a user is granted the Gemini Enterprise User ( **`roles/discoveryengine.agentspaceUser`** ) role at the project level, they can access all apps in that project, regardless of any app-level permissions. To restrict a user to specific apps, replace their project-level Gemini Enterprise User role with the Gemini Enterprise Restricted User 

( **`roles/discoveryengine.agentspaceRestrictedUser`** ) role, and then grant the Gemini Enterprise User role on each app that they need to access. 

**Note:** Users with app-level IAM permissions for a Gemini Enterprise app can access and use only that specific app. These are user-level permissions that don't include admin capabilities. 

For example, consider an organization with an HR app and a company-wide app. An HR team member with project-level permissions can access both the apps. By contrast, using an app-level IAM policy, you can grant a sales team member access to only the company-wide app, thereby preventing them from accessing the HR app. 

### Before you begin

- Confirm that you have the Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) role. 

- Confirm that all Gemini Enterprise users have a valid license and are granted the Gemini Enterprise Restricted User 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceRestrictedUser) ( `roles/discoveryengine.agentspaceRestrictedUser` ) role at the project level. For instructions, see Grant permissions to your users 

- (/gemini/enterprise/docs/access-control#grant-role). 

This role doesn't grant access to any app on its own. It provides the projectlevel access that users need, and you then grant access to individual apps. If you use a custom project-level role instead of the predefined `roles/discoveryengine.agentspaceRestrictedUser` role, ensure that your custom role includes the `discoveryengine.locations.buildAuthorizationUrl` , `discoveryengine.dataStores.get` , `discoveryengine.collections.get` , and `discoveryengine.devToolsConfigs.get` permissions. Omitting `discoveryengine.devToolsConfigs.get` causes a `403 PERMISSION_DENIED` error in Cloud Audit Logs when the web app checks `devToolsConfig` . 

### Transition from project-level to app-level access

To restrict users to specific apps, you must replace their project-level Gemini Enterprise User role with the Gemini Enterprise Restricted User role, and then grant the Gemini Enterprise User role at the individual app level. 

To transition a user from project-level access to app-level access, follow these steps. You use the Google Cloud console for the project-level changes, and the API for the app-level grant, which the Google Cloud console doesn't support. 

1. In the Google Cloud console, go to the **IAM** page. 

2. Find the user and remove the Gemini Enterprise User ( `roles/discoveryengine.agentspaceUser` ) role from their project-level permissions. 

3. If you haven't already, grant the user the Gemini Enterprise Restricted User ( `roles/discoveryengine.agentspaceRestrictedUser` ) role at the project level. 

4. Use the `setIamPolicy` method to grant the user the Gemini Enterprise User ( `roles/discoveryengine.agentspaceUser` ) role for each specific app that they need to access. For more information, see Manage IAM policies for apps (#manage-iam-policies-for-apps). 

### Manage IAM policies for apps

To manage access to your Gemini Enterprise app, you can use the `getIamPolicy` and `setIamPolicy` API methods. 

The following steps show you how to retrieve the current policy and then update it to grant or revoke user access. 

#### Get the app IAM policy

Get the current IAM policy of your app using the `getIamPolicy` 

(/gemini/enterprise/docs/reference/rpc/google.iam.v1#getiampolicyrequest) method. It's recommended to fetch the existing policy first to avoid overwriting any current permissions. 

REST 

(#rest) 

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/c
ollections/default_collection/engines/APP_ID:getIamPolicy"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

_`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

- `global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_`LOCATION`_ : the multi-region of your data store: `global` , `us` , or `eu` 

_`APP_ID`_ : the ID of the app that you want to configure. 

**Note:** Copy the **`etag`** value from the response. This value is required to update the IAM policy. The **`etag`** value changes with each policy update. 

<sup>Example command and result</sup> 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://global-discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app:getIamPolicy"
{
 "version": 1,
 "etag": "1234567890"
}
```

#### Update the app IAM policy

To grant or revoke user access to the app, update the app's IAM policy using the `setIamPolicy` (/gemini/enterprise/docs/reference/rpc/google.iam.v1#setiampolicyrequest) method. 

**Important:** The **`setIamPolicy`** method replaces the existing policy. To avoid removing existing permissions, your request must include all the policy bindings you want to retain, in addition to any new or modified bindings. 

The IAM policy uses the Gemini Enterprise User 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) ( `roles/discoveryengine.agentspaceUser` ) role to grant users direct access to the app. 

**Note:** Changes to IAM policies, such as those made using **`setIamPolicy`** , are subject to propagation delays. It can take several minutes for permissions to fully propagate. For more information, see IAM propagation delay (/iam/docs/access-change-propagation). 

REST (#rest) 

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-d '{
     "policy": {
        "etag": "ETAG",
        "bindings": [
         {
           "role": "roles/discoveryengine.agentspaceUser",
           "members": [
             "user:USER_EMAIL",
             "group:GROUP_EMAIL",
"principal://iam.googleapis.com/locations/global/workloadIdentityPools/
POOL_ID/subject/SUBJECT_ID",
"principalSet://iam.googleapis.com/locations/global/workloadIdentityPools/
POOL_ID/attribute.NAME/VALUE"
           ]
         }
       ]
     }
   }' \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/c
ollections/default_collection/engines/APP_ID:setIamPolicy"
```

Replace the following: 

- _`ETAG`_ : the `etag` value you got as the response when you used the `getIamPolicy` method. 

_`USER_EMAIL`_ , _`GROUP_EMAIL`_ : one or more user or group email addresses. In addition to `user` and `group` , `principal` and `principalSet` are valid member types for Workload Identity Federation. 

- To grant access, add principals to the `members` array. For example, `"user:cloudysanfrancisco@gmail.com"` or 

- `"group:mcymbalgroup@google.com"` . 

**Note:** Avoid extra spaces before or after the email address. 

- To revoke access, remove principals from the `members` array. 

_`POOL_ID`_ : The ID of your workload identity pool. 

_`SUBJECT_ID`_ : The subject identifier for a specific identity. 

_`NAME`_ : The name of an attribute. 

- _`VALUE`_ : The value of an attribute. 

_`PROJECT_ID`_ : the ID of your project. 

- _`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

   - `us` for the US multi-region 

   - `eu` for the EU multi-region 

   - `global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_`LOCATION`_ : the multi-region of your data store: `global` , `us` , or `eu` . 

- _`APP_ID`_ : the ID of the app that you want to configure. 

**Note:** The **`etag`** value changes with each policy update. To update the policy again, you must first get the new **`etag`** by following Get the app IAM policy (#get-app-iam-policy). 

<sup>Example command and result</sup> 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-d '{
     "policy": {
        "etag": "1234567890",
        "bindings": [
         {
           "role": "roles/discoveryengine.user",
           "members": [
             "user:cloudysanfrancisco@gmail.com",
             "group:cymbalgroup@google.com"
           ]
         }
       ]
     }
   }' \
"https://global-discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app:setIamPolicy"
{
 "version": 1,
 "etag": "2345678901",
 "bindings": [
   {
     "role": "roles/discoveryengine.user",
     "members": [
       "user:cloudysanfrancisco.com",
       "group:cymbalgroup@google.com"
     ]
   }
 ]
}
```

### What's next?

If you want to delete an app with an IAM policy, you can remove the users from the policy before deleting the app. For more information, see Best practices for deleting an app with an IAM policy 

(/gemini/enterprise/docs/delete-app#best-practices-for-deleting-an-app-with-an-iam-policy). 

Last updated 2026-10-14 UTC. 



## Configure granular access controls for apps and data stores

URL: https://docs.cloud.google.com/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores

This page explains how a Gemini Enterprise administrator can configure granular, resource-level IAM permissions to restrict access to specific Gemini Enterprise apps and data stores using either the Google Cloud console, the Google Cloud CLI, or the REST API. 

If you only need to restrict end-user access at the app level without configuring data store permissions or custom project-level roles, see Confgure access controls for appsi (/gemini/enterprise/docs/iam-policy-for-apps). 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

### Overview

By default, IAM permissions granted at the Google Cloud project level apply across all Gemini Enterprise apps and data stores in the project. If your organization needs to restrict users to specific apps or data stores within a single project, you can use resource-level access controls. 

Resource-level access controls let administrators: 

- Grant users access to specific apps and linked data stores without exposing other apps in the same project. 

- Delegate app administration or read-only monitoring for specific apps without granting broad project-wide administrative rights. 

- Enforce organizational data boundaries and compliance policies. 

**Caution:** Project-level predefined roles (/gemini/enterprise/docs/access-control#roles) override resource-level policies. If a user is assigned any of these roles at the project level, they can access all the apps and data stores in the project, regardless of resource-level bindings. To restrict access, users must not hold broad project-level roles. 

#### How access controls work

To grant resource-level access, administrators must configure two role bindings for each target user or group. Permissions are evaluated independently: to receive answers from a data store in an app, a user must be granted permissions on both the target app and the target data store. 

|Role-binding<br>level|Role type|Purpose, scope, and example roles|
|---|---|---|
|Project level|Custom role|The custom roles that you create in this guide grant permissions<br>required for the user to authenticate or load console listing pages<br>across the project without exposing specific app or data store<br>content.|
|||Example roles:|
|||`customRestrictedEndUser`<br>(#create-custom-restricted-end-user-role)<br>`customRestrictedAdmin` (#create-custom-restricted-admin-role)|
|Resource level|Predefined rol i|i eThe predefined roles that you assign on the app or data store<br>resource grant operational permissions, such as chatting, configuring<br>settings, or viewing analytics, strictly on that resource.<br>Example roles:|
|||Gemini Enterprise User<br>(/iam/docs/roles-<br>permissions/discoveryengine#discoveryengine.agentspaceUser)<br>(`roles/discoveryengine.agentspaceUser`)<br>Gemini Enterprise Admin<br>(/iam/docs/roles-<br>permissions/discoveryengine#discoveryengine.agentspaceAdmin)<br>(`roles/discoveryengine.agentspaceAdmin`)<br>Gemini Enterprise Viewer<br>(/iam/docs/roles-<br>permissions/discoveryengine#discoveryengine.agentspaceViewer)<br>(`roles/discoveryengine.agentspaceViewer`)|

#### Example scenario

Consider a Google Cloud project at Cymbal named `cymbal-ai-project` containing two apps and multiple data stores: 

Example scenario: Restricting access across apps and data stores 

Context A Google Cloud project at Cymbal named `cymbal-ai-project` contains two apps: 

- Cymbal Finance app, which is connected to two data stores: the General Finance data store and the Confidential Payroll data store. 

Cymbal HR app, which is connected to the Cymbal HR data store. 

Goal Grant Alex ( `alex@cymbal.com` ) access to use the Cymbal Finance app and query only the General Finance data store, while denying access to the Confidential Payroll data store and the Cymbal HR app. 

Required Follow these steps to configure access controls: configurations 1. Project level: Enable app and data store access control on `cymbal-ai-project` and grant Alex the `customRestrictedEndUser` 

   - (#create-custom-restricted-end-user-role) role on the project so their browser can authenticate with the service. 

2. Resource level: Grant Alex the Gemini Enterprise User 

   - (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) ( `roles/discoveryengine.agentspaceUser` ) role on only the Cymbal Finance app and the General Finance data store. 

Result When Alex signs in, they can open the Cymbal Finance app and query the General Finance data store. Even though the Confidential Payroll data store is connected to the same app, Alex can't view or query it. Attempts to access the Cymbal HR app or query the Cymbal HR data store are also denied. 

The following diagram illustrates how project-level settings and independent resourcelevel IAM permissions work together in this scenario: 

### Before you begin

- Confirm that you have the Gemini Enterprise Admin 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) role. 

- Ensure that users who need restricted access aren't assigned the project-level Discovery Engine roles. 

- Create the required custom project-level roles for your target personas in Create custom project-level roles (#create-custom-project-level-roles). 

**Warning:** If you already use app-level access controls (Configure access controls for apps (/gemini/enterprise/docs/iam-policy-for-apps)) with a custom project-level role instead of the predefined Gemini Enterprise Restricted User 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceRestrictedUser) ( **`roles/discoveryengine.agentspaceRestrictedUser`** ) role, ensure your custom project-level role includes the **`discoveryengine.dataStores.get`** , **`discoveryengine.collections.get`** , and 

**`discoveryengine.devToolsConfigs.get`** permissions before enabling app and data store access control. Granular data store access control filters data stores based on **`discoveryengine.dataStores.get`** and **`discoveryengine.collections.get`** , and omitting **`discoveryengine.devToolsConfigs.get`** generates a **`403`** 

**`PERMISSION_DENIED`** error when the web app checks **`devToolsConfig`** . No action is needed if existing users use the predefined **`roles/discoveryengine.agentspaceRestrictedUser`** role. 

### Enable app and data store access control

Before you can configure granular permissions on apps and data stores or view the **User permissions** tab in the Google Cloud console, enable app and data store access control on your project using the Google Cloud console or the REST API: 

ConsoleREST (#rest) (#console) 

To enable app and data store access control in the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** > **Settings** page. 

Go to Settings (https://console.cloud.google.com/gemini-enterprise/settings) 

2. Select the **Resource access control** tab. 

3. Turn on the **Resource access control** toggle. 

4. Click **Save** . 

5. In the **Enable resource access control?** dialog, click **Enable** . 

**Note:** After enabling this setting, wait approximately 5 minutes for the configuration change to take effect across all services and the Google Cloud console. 

### Create custom project-level roles

Custom project-level roles grant permissions without exposing all project resources. You only need to create each custom role once per Google Cloud project. 

**Note:** This guide uses predefined roles for resource-level bindings. If you create custom resourcelevel roles instead, ensure they contain all operational permissions included in the corresponding predefined role. 

#### Create a custom restricted end user role

The `customRestrictedEndUser` role grants project-level permissions required for end users to load the Gemini Enterprise authorization endpoint and developer tools configuration ( `discoveryengine.locations.buildAuthorizationUrl` and 

`discoveryengine.devToolsConfigs.get` ). It doesn't grant access to inspect or query specific apps or data stores. 

Consolegcloud (#gcloud)REST (#rest) (#console) 

To create the custom role in the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **Roles** page. 

Go to Roles (https://console.cloud.google.com/iam-admin/roles) 

2. Select your Google Cloud project. 

3. Click **+ Create custom role** . 

4. Enter the role details: 

**Title** : `Custom Gemini Enterprise Restricted End User` 

- **Description** : `Base project-level permissions to access Gemini Enterprise apps` . 

**Role ID** : `customRestrictedEndUser` 

   - **Role launch stage** : Select **General Availability** 

5. Click **+ Add permissions** . 

6. Filter and select the following permissions: 

   - `discoveryengine.devToolsConfigs.get` 

   - `discoveryengine.locations.buildAuthorizationUrl` 

7. Click **Add** . 

#### Create a custom restricted administrator role

The `customRestrictedAdmin` role grants project-level permissions required for delegated administrators and viewers to view resource listings and sidebars in the Google Cloud console without granting access to view or modify specific app or data store contents. To delegate administrative control over a specific app or data store, assign this custom role at the project level, and then assign Gemini Enterprise Admin 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) 

( `roles/discoveryengine.agentspaceAdmin` ) directly on the target resource. 

Consolegcloud (#gcloud)REST (#rest) (#console) 

To create the custom role in the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **Roles** page. 

Go to Roles (https://console.cloud.google.com/iam-admin/roles) 

2. Select your Google Cloud project. 

3. Click **+ Create role** . 

4. Enter the role details: 

**Title** : `Custom Gemini Enterprise Restricted Admin` 

   - **Description** : `Base project-level permissions to list and view Gemini Enterprise configuration pages` . 

   - **Role ID** : `customRestrictedAdmin` 

   - **Role launch stage** : Select **General Availability** . 

5. Click **+ Add permissions** . 

6. Filter and select the following permissions: 

   - `discoveryengine.aclConfigs.get` 

   - `discoveryengine.collections.list` 

   - `discoveryengine.dataStores.list` 

   - `discoveryengine.devToolsConfigs.get` 

   - `discoveryengine.engines.list` 

   - `discoveryengine.licenseConfigs.list` 

   - `discoveryengine.locations.buildAuthorizationUrl` 

   - `discoveryengine.locations.getConnectorSource` 

   - `discoveryengine.locations.listConnectorSources` 

   - `discoveryengine.projects.get` 

   - `discoveryengine.userStores.listUserLicenses` 

   - `resourcemanager.projects.get` 

7. Click **Add** . 

8. Click **Create** . 

#### Update an existing custom role

If a custom role already exists in your project and you need to add missing permissions, update the role: 

Consolegcloud (#gcloud)REST (#rest) (#console) 

To update a custom role in the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **Roles** page. 

Go to Roles (https://console.cloud.google.com/iam-admin/roles) 

2. Select the Google Cloud project in which you created the custom role. 

3. Select the **Custom** tab or filter the list to locate your custom role 

   - ( `customRestrictedEndUser` or `customRestrictedAdmin` ). 

4. Click the name of the custom role. 

5. Click **Edit role** . 

6. Click **+ Add permissions** . 

7. Search for and select the permissions you want to add, and then click **Add** . 

8. Click **Save** . 

### Assign a custom role at the project level

Assign the custom project roles to a target user or group. 

Consolegcloud (#gcloud)REST (#rest) (#console) 

To assign the custom role using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Select the Google Cloud project in which you created the custom role. 

3. Click **Grant Access** to add a new principal or edit an existing one. 

4. In **New principals** , enter the user or group email address. 

5. Select the custom role created for your persona, such as one of the following: 

   - **Custom Gemini Enterprise Restricted End User** 

**Custom Gemini Enterprise Restricted Admin** 

6. Click **Save** . 

### Configure app permissions

Grant resource-level permissions on the target app resource using the Google Cloud console or the REST API. 

If you want to assign a custom role instead of a predefined role in the app-level IAM policy, ensure that the custom role includes all permissions of the corresponding predefined role, such as Gemini Enterprise User 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) 

( `roles/discoveryengine.agentspaceUser` ) or Gemini Enterprise Admin 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) 

( `roles/discoveryengine.agentspaceAdmin` ) . 

ConsoleREST (#rest) (#console) 

To configure app permissions in the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** > **Apps** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

2. Select your target app. 

3. Click **User permissions** and click **Add user** . 

4. Select the role for the user or group: 

**User** : Assigns Gemini Enterprise User 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) ( `roles/discoveryengine.agentspaceUser` ). 

**Admin** : Assigns Gemini Enterprise Admin 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) . 

**Viewer** : Assigns Gemini Enterprise Viewer 

(/iam/docs/roles- 

permissions/discoveryengine#discoveryengine.agentspaceViewer) 

( `roles/discoveryengine.agentspaceViewer` ). 

5. Click **Save** . 

### Configure data store permissions

To configure data permissions, grant resource-level permissions on the target data store using the Google Cloud console or the REST API. End users can only connect to and query data stores to which they have been explicitly granted permissions. 

If you want to assign a custom role instead of a predefined role in the data store IAM policy, ensure that the custom role includes all permissions of the corresponding predefined role, such as Gemini Enterprise User 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) 

( `roles/discoveryengine.agentspaceUser` ) or Gemini Enterprise Admin 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) . 

For third-party connectors that enforce end-user document permissions, end user access to individual documents continues to be governed by the access control lists (ACLs) 

synced from the source system (granting IAM access doesn't bypass source ACLs). 

To find data stores, collections, and entity IDs, see Get data store and entity details (/gemini/enterprise/docs/get-datastore-details). 

ConsoleREST (#rest) (#console) 

To configure data store permissions in the Google Cloud console, follow these steps. Permissions assigned to a data store in the Google Cloud console automatically propagate to any underlying child entities: 

1. In the Google Cloud console, go to the **Gemini Enterprise** > **Data Stores** page. 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

2. Click the name of your data store. 

3. Click **User permissions** > **Add user** . 

4. Select the role for the user or group: 

**User** : Assigns Gemini Enterprise User 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) ( `roles/discoveryengine.agentspaceUser` ). 

**Admin** : Assigns Gemini Enterprise Admin 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) . 

**Viewer** : Assigns Gemini Enterprise Viewer 

- (/iam/docs/roles- 

permissions/discoveryengine#discoveryengine.agentspaceViewer) 

   - ( `roles/discoveryengine.agentspaceViewer` ). 

5. Click **Save** . 

**Note:** It can take several minutes for IAM policy changes to take effect across all services. When testing changes, sign out and sign back in, or test using a private (incognito) window to avoid active session caching. 

### Grant access to Gemini Notebook Enterprise and AI developer tools features

Restricted users who are assigned `customRestrictedEndUser` at the project level lose access to features like AI developer tools and Gemini Notebook Enterprise because their project role contains only base authorization permissions. 

Granting the full Gemini Enterprise User 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceUser) 

( `roles/discoveryengine.agentspaceUser` ) role at the project level overrides isolation and exposes all apps and data stores in the project. Instead, administrators can grant narrow, feature-specific roles at the project level. 

#### Grant access to Gemini Notebook Enterprise

Grant the Cloud NotebookLM User 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.notebookLmUser) 

( `roles/discoveryengine.notebookLmUser` ) role to allow restricted users to create and use notebooks without exposing apps or data stores: 

Consolegcloud (#gcloud)REST (#rest) (#console) 

To grant access using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Select your Google Cloud project. 

3. Locate the user or group in the permissions list, and then click **Edit principal** . Alternatively, click **Grant access** to add a new user. 

4. In the **Assign roles** section, click **Add another role** . 

5. In the **Select a role** field, search for and select **Cloud NotebookLM User** ( `roles/discoveryengine.notebookLmUser` ). 

6. Click **Save** . 

#### Grant access to AI developer tools

Grant the Gemini for Google Cloud User 

(/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) 

( `roles/cloudaicompanion.user` ) and User role for Business AI Code API 

(/iam/docs/roles-permissions/businessaicode#businessaicode.user) ( `roles/businessaicode.user` ) roles to enable AI developer tools without exposing Gemini Enterprise apps or data stores: 

Consolegcloud (#gcloud)REST (#rest) (#console) 

To grant access using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/iam-admin/iam) 

2. Select your Google Cloud project. 

3. Locate the user or group in the permissions list, and then click **Edit principal** . Alternatively, click **Grant access** to add a new user. 

4. In the **Assign roles** section, assign each of the following roles: 

**Gemini for Google Cloud User** ( `roles/cloudaicompanion.user` ) 

**User role for Business AI Code API** ( `roles/businessaicode.user` ) 

5. Click **Save** . 

### What's next?

If you want to delete an app with an IAM policy, you can remove the users from the policy before deleting the app. For more information, see Best practices for deleting an app with an IAM policy 

(/gemini/enterprise/docs/delete-app#best-practices-for-deleting-an-app-with-an-iam-policy). 

Last updated 2026-10-14 UTC. 



## Secure your app with VPC Service Controls

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-vpc-service-controls

To properly secure a Gemini Enterprise app and mitigate the risk of data exfiltration, you must configure a VPC Service Controls perimeter. Using VPC Service Controls (/vpc-service-controls/docs/overview) and Access Context Manager (/access-context-manager/docs/overview), you can protect and control access to your Gemini Enterprise app and connected enterprise data. 

**Note:** When using VPC Service Controls with Gemini Enterprise, creating new data stores is blocked until an administrator adds the required data sources and egress domains to the corresponding managed organization policy constraints. Existing data stores — including any that were previously enabled by request through a Google representative — continue to work without any further action. For more information, see Create data stores after enabling VPC Service Controls (#using-actions). 

### Set up VPC Service Controls with Gemini Enterprise

To protect your Gemini Enterprise resources using VPC Service Controls, do the following: 

1. Ensure that you have a VPC Service Controls perimeter configured. You can create a new perimeter specifically for your Gemini Enterprise app, or use an existing perimeter that houses related resources. 

   - For information about service perimeters, see Service perimeter details and configuration (/vpc-service-controls/docs/service-perimeters). 

2. Add the Google Cloud project that contains your Gemini Enterprise app to the list of protected resources within the service perimeter. 

3. Add the following APIs to the list of restricted services for the perimeter: Discovery Engine API: `discoveryengine.googleapis.com` 

**Tip:** We recommend using dry run mode (/vpc-service-controls/docs/dry-run-mode) to test your service perimeter before enforcing it. 

After the service perimeter is enabled and the Discovery Engine API is listed as a restricted service, VPC Service Controls enacts the following security measures: 

- The `discoveryengine.googleapis.com` API can no longer be accessed from the public internet. 

- Access to the Gemini Enterprise user interface is blocked, except where allowed by ingress rules. 

- Creating new data stores (which back Gemini Enterprise actions (/gemini/enterprise/docs/assistant-use-actions)) is blocked until an administrator adds the required data sources and egress domains to the corresponding managed organization policy constraints 

(/gemini/enterprise/docs/connectors/managed-policy-constraints-overview). Existing data stores — including any that were previously enabled by request through a Google representative — continue to work without any further action. For more information, see Create data stores after enabling VPC Service Controls (#using-actions). 

### Restrict public access using Access Context Manager

Gemini Enterprise applications are made publicly accessible to the public internet. By default, Gemini Enterprise requires users to authenticate and requires authorization for access. VPC Service Controls and Access Context Manager provide additional controls that you can use to gate access. 

Using Access Context Manager, you can define fine-grained, attribute-based access control for projects and resources in Google Cloud. To do this, you must define an access policy (/access-context-manager/docs/overview#access-policies), which is an organization-wide container for access levels 

- (/access-context-manager/docs/overview#access-levels) and service perimeters. 

Access levels describe the requirements that must be met in order for a request to be honored. For example, you can restrict requests based on the following: 

- Device type and operating system (requires a Chrome Enterprise Premium 

- (/chrome-enterprise-premium/docs/overview) license) 

IP address 

- User identity 

_Reference architecture using VPC Service Controls to protect Gemini Enterprise._ 

In this reference architecture, a public IP subnetwork access level is used to build the VPC Service Controls access policy. 

To gate access to Gemini Enterprise using Access Context Manager, follow the instructions in Creating a basic access level 

(/access-context-manager/docs/create-basic-access-level) to create a basic access level. Specify the following options: 

1. For **Create conditions in** , choose **Basic mode** . 

2. In the **Access level title** field, enter `corp-public-block` . 

3. In the **Conditions** section, for **When condition is met, return** , select **TRUE** . 

4. For **IP Subnetworks** , select **Public IP** . 

5. For the IP address range, specify your external IP address. 

### Apply VPC Service Controls to existing data stores

Enforcing a VPC Service Controls perimeter on a project with existing data stores is not supported. 

To enforce VPC Service Controls on an existing data store: 

1. Delete and then recreate the data store. 

This applies the service controls and lets traffic flow correctly. 

### Create data stores after enabling VPC Service Controls

VPC Service Controls primarily aims to prevent data exfiltration by creating a secure service perimeter around your projects and resources. New data stores (which back Gemini Enterprise actions, such as sending an email or creating a Jira ticket) are potential paths for data to leave this perimeter, so VPC Service Controls blocks the creation of new data stores until an administrator explicitly permits them through managed organization policy constraints. 

When you enable VPC Service Controls on a Google Cloud project containing an Gemini Enterprise app, the UI prevents you from creating new data stores. Data stores created before the perimeter was enabled — and any services that were previously enabled by request through a Google representative — continue to work; only creating new ones is gated. 

To let administrators create a new data store inside the perimeter: 

1. Add the data source to the **Restrict allowed data sources for data connectors** (/gemini/enterprise/docs/connectors/configure-allowed-data-sources) managed organization policy constraint. Adding a data source to this constraint automatically permits its well-known essential domains (for example, `graph.microsoft.com` and `api.atlassian.com` ). 

2. If the data store needs domains unique to your organization (for example, `cymbal.atlassian.net` or `cymbal.com` ), add those domains to the **Restrict** 

**egress domains for data connectors** 

(/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns) managed organization policy constraint. 

For an overview of these constraints, see Managed policy constraints (/gemini/enterprise/docs/connectors/managed-policy-constraints-overview). 

Last updated 2026-10-14 UTC.
