# Gemini Enterprise: platform, security, agents, cost, monitoring / Get subscriptions and assign licenses to Security Overview
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 75-100, extracted 2026-10-18

Contains:
- Get subscriptions and assign licenses (pages 75-90) https://docs.cloud.google.com/gemini/enterprise/docs/licenses
- Frequently asked questions (pages 91-96) https://docs.cloud.google.com/gemini/enterprise/docs/licenses-faqs
- Security Overview (pages 97-100) https://docs.cloud.google.com/gemini/enterprise/docs/security-overview

## Get subscriptions and assign licenses

URL: https://docs.cloud.google.com/gemini/enterprise/docs/licenses

This page describes how to get subscriptions for Gemini Enterprise and how to manage user licenses. 

Setting up access typically involves the following stages: 

1. **Procure** : Purchase a subscription to a product edition for your billing account. 

2. **Distribute** : Allocate licenses from the subscription to specific projects and locations. 

3. **Assign** : Assign the distributed licenses to individual users. 

### About licenses

To sign in to the Gemini Enterprise app, a user must have a _license_ . Licenses can be assigned to users manually or automatically. 

- **Manually-assigned licenses:** You can add users by their email addresses. 

- **Automatically-assigned licenses:** You can configure a subscription so that Gemini Enterprise automatically assigns a license to a user the first time they access the Gemini Enterprise or the Gemini Notebook Enterprise interface. 

**Note:** Licenses are specific to a Google Cloud project and a location. For example, if users require access to a Gemini Enterprise app located in a Google Cloud project that is in both the US and global multi-regions, you need to have two separate licenses for these two separate locations within the same Google Cloud project. 

### About subscriptions

To get licenses, you must first have a _subscription_ to a Gemini Enterprise edition. Subscriptions are specific to a billing account. For information about available editions, see Compare editions of Gemini Enterprise (/gemini/enterprise/docs/editions). 

For Gemini Enterprise, you can buy a monthly subscription or a year-long subscription. These subscriptions can be set to renew automatically. 

You can purchase subscriptions for the Gemini Enterprise Standard, Gemini Enterprise Plus, and Gemini Enterprise Pay-as-you-go editions using the Google Cloud console. 

#### Subscription seat quantity limits

When you purchase or modify a seat-based subscription directly through the Google Cloud console, automatic seat quantity caps apply based on your Cloud Billing account type: 

- **Self-serve (or Online) and resold billing accounts:** Limited to a maximum of 25 seats per account when managing subscriptions using Google Cloud console. 

- **Invoiced (or Offline) account billing accounts:** Limited to a maximum of 1,000 seats per account. 

If your organization requires more seats or if you encounter the maximum seat limit error when trying to add licenses to an existing subscription, contact your Google Cloud sales representative or account manager to purchase additional licenses through an offline order or request an allowlist exemption. 

### About subscription states

A subscription can be in one of the following states: 

|State|Description|
|---|---|
|Not started|You purchased the subscription, but it is not yet active. You can distribute licenses from<br>this subscription to projects, but users assigned these licenses won't have access to<br>Gemini Enterprise until the subscription becomes active. For more information, see<br>Distribute licenses(#distribute-licenses).|
|Active|The subscription is active, and users who have a license in this subscription can access<br>Gemini Enterprise.|
|Deactivating|The subscription is in a deactivating state, with licenses scheduled for early termination.<br>Users with licenses in this subscription continue to have access to Gemini Enterprise for<br>a grace period of one week. After this week, the licenses transition to the Expired state.<br>For more information, see<br>Handle early termination(#handle-early-termination).|

Users with licenses in this subscription lose access to Gemini Enterprise when the Expired subscription term ends or when licenses transition from the deactivating state to the expired state after early termination. 

### Before you begin

Before starting the procedures on this page, make sure you meet the following prerequisites: 

- Complete all tasks outlined in Set up Gemini Enterprise 

- (/gemini/enterprise/docs/before-you-begin). This includes: 

   - Setting up a billing account for your project. 

   - Granting at least the Gemini Enterprise User role to any users you'll license to use Gemini Enterprise. 

- Verify that billing is enabled for your Google Cloud project. For more information, see Verify that billing is enabled for your Google Cloud project 

- (/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

**Note:** To subscribe to the Gemini Enterprise Pay-as-you-go edition, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

- Confirm that you have the required IAM roles and permissions: 

   - The Gemini Enterprise Admin 

   - (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

   - If you manage billing for your organization, you must have the following roles to manage Gemini Enterprise subscriptions and procurement orders. 

      - Billing Account Administrator (/iam/docs/roles-permissions/billing#billing.admin) ( `roles/billing.admin` ) 

      - Service Usage Consumer 

      - (/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) ( `roles/serviceusage.serviceUsageConsumer` ) 

Alternatively, for granular IAM control, you can use a custom role with the following permissions instead of the **Billing Account Administrator** role: 

|Service|Permissions|
|---|---|
|Discovery Engine|`discoveryengine.billingAccountLicenseConfigs.distribute`<br>`discoveryengine.billingAccountLicenseConfigs.get`<br>`discoveryengine.billingAccountLicenseConfigs.list`<br>`discoveryengine.billingAccountLicenseConfigs.retract`<br>`discoveryengine.licenseConfigs.create`<br>`discoveryengine.licenseConfigs.get`<br>`discoveryengine.licenseConfigs.list`<br>`discoveryengine.licenseConfigs.update`<br>`discoveryengine.projects.get`<br>`discoveryengine.projects.provision`<br>`discoveryengine.projects.reportConsentChange`<br>`discoveryengine.userStores.batchUpdateUserLicenses`<br>`discoveryengine.userStores.listUserLicenses`|
|Consumer Procureme|nt`consumerprocurement.orders.get`<br>`consumerprocurement.licensePools.assign`<br>`consumerprocurement.licensePools.unassign`<br>`consumerprocurement.licensePools.enumerateLicensedUsers`|
|Resource Manager|`resourcemanager.projects.get`<br>`resourcemanager.projects.list`|
|Service Usage|`serviceusage.services.get`<br>`serviceusage.services.list`|

### Get a subscription

To get licenses, purchase a subscription to a Gemini Enterprise edition for your billing account. The subscription provides a pool of licenses that you can use with any project connected to that billing account, distribute to projects, and assign to users. 

- Standard and PlusPay-as-you-go… (#standard-and-plus) 

To subscribe to the Gemini Enterprise Standard or Plus edition, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage subscriptions > Create subscription** . 

3. For the **Gemini Enterprise Standard** or **Gemini Enterprise Plus** edition, click **Subscribe** . 

4. Configure the **Billing details** : 

   - a. Select the **Billing account** from the drop-down. 

   - b. Enter a **Subscription name** . 

   - c. Enter the **Number of licenses** you need for the edition. 

5. Select the **Subscription period** . 

6. If you want the subscription to renew automatically, select **Auto renew subscription** . 

7. Configure the **Distribution details** : 

   - a. In the **Select a project** drop-down, select your project. 

   - b. Choose a **Location type** for your subscription. If you don't have compliance or regulatory reasons to locate your data in the US or EU multi-regions, Google recommends that you choose the global multiregion for maximum availability and low latency. 

8. Click **Create > Confirm** . 

### Manage subscriptions

This section describes how to view, update, distribute, and reclaim Gemini Enterprise subscriptions. 

#### View subscription details

To view the details of your Gemini Enterprise subscriptions, do the following: 

ConsoleREST (#rest) 

(#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage subscriptions** . 

3. Select the **Billing account** from the drop-down. 

4. In the **Gemini Subscriptions** table, click the name of your subscription. 

#### Update subscription settings

After you create a subscription, you can update the settings, such as the license count or the auto-renewal setting. 

The method for adding more licenses depends on how you originally purchased your subscription: 

- If you purchased your subscription through the Google Cloud console, add more licenses directly within the Google Cloud console using the steps in this section. 

- If you purchased using an offline order form, you must update the order form with the new license count. Contact your Google account manager to update the order form. 

**Note:** When updating your subscription seat count in the Google Cloud console, maximum seat limits apply based on your billing account type (up to **25 seats** for self-serve (or online) and resold billing accounts, and up to **1,000 seats** for invoiced (or offline) billing accounts). For more information, see Subscription seat quantity limits (#seat-limits). 

If your existing subscription exceeds these thresholds (for example, if it was initially provisioned through a sales-led offline order), attempting to add more licenses directly through the Google Cloud console might result in a seat limit error. Contact your Google Cloud sales representative or account manager to adjust your license count or request an allowlist exception. 

Follow these steps to update the license count if you purchased through the Google Cloud console: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage subscriptions** . 

3. Click the subscription you want to update from the **Gemini Subscriptions** table. 

4. Click **Edit** next to **Subscription details** . 

5. Update the license count or turn on or turn off auto renewal. 

6. Click **Submit** . 

#### Cancel a subscription

To cancel a Gemini Enterprise subscription, you must turn off automatic renewal. Your subscription remains active until the subscription term ends, and you might incur charges until that date. To learn more about your subscription, see View subscription details (#subscription-detail). 

To cancel your subscription, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage subscriptions** . 

3. In the **Gemini Subscriptions** table, click the name of your subscription to open the subscription details page. 

4. Click **Edit** . 

5. In the **Edit subscription** panel, clear the **Auto renew subscription** checkbox. 

6. Click **Submit** . 

#### Distribute licenses

If you haven't distributed the subscribed licenses to a project, which might happen when you purchase the subscription offline or when the license distribution failed previously, do the following: 

ConsoleREST (#rest) (#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage subscriptions** . 

3. Select the **Billing account** from the drop-down. 

4. In the **Gemini Subscriptions** table, click the name of your subscription. 

5. Click **Distribute License** at the top of the page. A list appears, displaying existing license distributions and statistics of remaining and total seats. 

6. To distribute licenses to a project: 

   - a. Click the project selector to select a project. The selector supports autocompletion. 

   - b. Note: If you haven't enabled the Discovery Engine API for the selected project, a dialog appears prompting you to enable it. 

   - c. Select a **Location** . 

   - d. Enter the number of licenses to allocate. 

   - e. Repeat these steps if you want to distribute licenses to multiple projects or locations. 

7. Click **Submit** . 

8. In the confirmation dialog, review the summary of changes and click **Confirm** . 

#### Reclaim unassigned licenses in a subscription

This section describes how to reclaim unassigned licenses from a project, making them available in the billing account for redistribution to other projects. 

ConsoleREST (#rest) (#console) 

**Note:** You can only perform this action once per calendar day. 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage subscriptions** . 

3. Select the **Billing account** from the drop-down. 

4. In the **Gemini Subscriptions** table, click the name of your subscription. 

5. Click **Distribute License** at the top of the page (this button opens the management form for all allocations). 

6. In the list of allocations, locate the row for the project and location you want to reclaim licenses from. 

7. Choose one of the following actions: 

   - To reduce the number of licenses: Decrease the count in the license input field. 

   - To fully reclaim licenses: Move the pointer over the row to reveal the delete button, and then click **Delete** . 

8. Click **Submit** . 

9. In the confirmation dialog, review the summary of changes (which will list any reclaimed licenses) and click **Confirm** . 

#### Handle early termination

When you migrate between different subscription types or if there's an issue with your billing account, a subscription might end earlier than planned. 

To ensure a smoother transition and prevent service interruptions, we provide a oneweek (seven days) grace period where affected licenses are in a deactivating state before they fully expire. During this grace period, you can continue to use the service while you transition to a new subscription. 

To ensure your users retain access, transfer their licenses to a new, active subscription either automatically (#auto-transfer) or manually (#manual-transfer). 

The following image shows an example of a deactivating license in the Google Cloud console: 

### Manage user licenses

This section describes how to view licenses, export user data, and assign, transfer, and remove licenses for individual users. 

#### View licenses

To view the licenses and the users assigned to them, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage users** . 

3. Select the **Multi-region** of the existing license. 

#### Export user data

The users table in the Google Cloud console does not support sorting or filtering. If you need to sort, filter, or analyze your user data, you can export up to 1,000,000 user records to a comma-separated values (CSV) file. 

The exported CSV file includes the following columns. 

|Column<br>name|Description|
|---|---|
|`user_`<br>`principal`|The email address of the user.|
|`license_`<br>`config`|The full Google Cloud resource name for the user's assigned subscription (for example,<br>`projects/PROJECT_NUMBER/locations/LOCATION/licenseConfigs/LICENSE_CONFIG_`<br>`ID`). The license config ID corresponds to the Gemini Enterprise edition (for example,<br>Standard or Plus) assigned to the user.|
|`assignment`<br>`_time`|The timestamp (in UTC) when an administrator assigned the license.|
|`last_`<br>`login_time`|The timestamp (in UTC) when the user last signed in.|
|`license_`<br>`assignment`<br>`_state`|The license assignment state. The following values are available:<br>`ASSIGNED`: The user has an assigned license.<br>`NO_LICENSE`: The user does not have a license because an administrator hasn't<br>assigned one or has removed an existing license.<br>`BLOCKED`: A policy or administrator blocks the user from receiving a license.|

To export user data to a CSV file, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** > **Manage users** page. 

Manage users (https://console.cloud.google.com/gemini-enterprise/user-license) 

2. Select the **Multi-region** of the existing license. 

3. In the **Users** section, click **Export all users** . 

Depending on the size of the users table, the export process might take up to 2.5 minutes to complete. During this time, the console displays a loading state. When the export finishes, your browser downloads the CSV file to its default download location. 

Troubleshoot export issues 

The following table lists common issues when exporting user data and their resolutions. 

|Issue|Resolution|
|---|---|
|The Export all<br>users button is<br>hidden|Make sure that there are users assigned to licenses in the selected multi-region.<br>If there are no assigned users, the Export all users button does not appear.|
|The export request<br>fails with a limit-<br>exceeded error|If your user list exceeds the export limit of 1,000,000 users, the Google Cloud<br>console rejects the export request and displays a limit-exceeded error message.|
|The export request|Make sure that your account has the<br>Gemini Enterprise Admin|
|fails with a<br>permission denied<br>error|(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin)<br>role, which includes the required`discoveryengine.userStores.listUser`<br>`Licenses`permission.|

#### Assign licenses to users

This section explains how to automatically or manually assign licenses to new users. You can assign a license to a new user at any time and, after a license is assigned, the user can access Gemini Enterprise immediately. 

Add users and assign them licenses automatically 

To assign licenses to users automatically when they sign in to the Gemini Enterprise app, do the following: 

**Note:** Ensure your subscription has enough licenses for the maximum number of users who are expected to use Gemini Enterprise. 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage users** . 

3. Select the **Multi-region** of the existing license. 

4. Select **Assign licenses automatically** and then select the subscription. 

Each time a user without a manually-assigned license signs in, Gemini Enterprise automatically assigns them a license from this subscription. If no licenses remain in the subscription, Gemini Enterprise shows users a message notifying them that they don't have access. 

- For more information about subscriptions, see the About subscriptions (#about-subscriptions) section. 

Add users and manually assign them licenses 

To give specific users access to Gemini Enterprise, you can manually assign them licenses from an active subscription. 

ConsoleREST (#rest) (#console) 

To manually assign licenses to users, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click **Manage users** . 

3. Select the **Multi-region** of the existing license. 

4. Click **Add users** . 

5. On the **Add users** page: 

   - a. Enter the email addresses of the users. Make sure to use the same email address that they'll use to sign in to the Gemini Enterprise app. 

b. Select the subscription to assign to those users. 

c. Click **Submit** . 

#### Transfer licenses from expired subscriptions

Users can't sign in to Gemini Enterprise if the subscription has expired. There are a couple of approaches to returning sign-in access to them: 

- Automatically transfer existing users with expired licenses to the default subscription (#auto-transfer). 

Manually transfer existing users to a new subscription (#manual-transfer). 

**Note:** If you previously blocked a user from accessing a license, Gemini Enterprise grants them access within 30 minutes after you assign the new license. 

Automatically transfer users to an active subscription 

To automatically transfer users to an active subscription, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Manage users** page. 

Gemini Enterprise License (https://console.cloud.google.com/gemini-enterprise/user-license) 

2. Select the **Multi-region** of the existing license. 

3. Make sure that you have an active subscription. If you don't have one, get a subscription (#get-subscription). 

4. Select **Assign licenses automatically** and choose the active subscription. 

5. Select **Automatically update expired license** . 

When a user with an expired license next signs in, Gemini Enterprise automatically grants them a license in the chosen subscription. 

Manually transfer users to an active subscription 

To manually transfer users to an active subscription, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Manage users** page. 

Gemini Enterprise License (https://console.cloud.google.com/gemini-enterprise/user-license) 

2. Select the **Multi-region** of the existing license. 

3. Make sure that you have an active subscription. If you don't have one, get a subscription (#get-subscription). 

4. Select the users and click **Assign different license** . 

5. In the **Edit Users** pane, select the subscription and click **Submit** . 

#### List the licenses

To list the licenses and the users assigned to them, run the following command: 

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

```
curl -X GET \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \` 

```
 -H "X-Goog-User-Project: PROJECT_ID" \
-
 "https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/userStores/
default_user_store/userLicenses"
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

   - `us` for the US multi-region 

   - `eu` for the EU multi-region 

   - `global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_`LOCATION`_ : the multi-region of your data store: `global` , `us` or `eu` 

#### Remove users from a license

You can remove a license from a user at any time. When a license is removed, the user immediately loses access to Gemini Enterprise. To remove users from a license, do the following: 

ConsoleREST (#rest) (#console) 

To remove users from a license using the Google Cloud console, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Manage users** page. 

Gemini Enterprise License (https://console.cloud.google.com/gemini-enterprise/user-license) 

2. Select the **Multi-region** of the existing license. 

3. In the users table, select the users. 

4. To remove users from a license, choose one of the following: 

   - To only remove the license from the selected users, click **Unassign license** . 

   - To remove the license and also delete the selected users from the project, click **Unassign and delete license** . 

5. Click **Confirm** . 

### What's next

- Learn more about the Frequently asked questions about Gemini Enterprise licenses (/gemini/enterprise/docs/licenses-faqs). 

- Learn about IAM roles and permissions (/gemini/enterprise/docs/access-control). 

Last updated 2026-10-14 UTC. 



## Frequently asked questions

URL: https://docs.cloud.google.com/gemini/enterprise/docs/licenses-faqs

This page provides answers to common questions about managing and using the Gemini Enterprise licenses. 

### Manage subscriptions

This section covers common questions related to managing your Gemini Enterprise subscriptions. 

#### Why can't I view and modify subscriptions, including reclaiming, and distributing licenses?

You must have the Billing Account Administrator 

(/iam/docs/roles-permissions/billing#billing.admin) role to manage subscriptions. You can also use a custom role with specific permissions. Verify that you have this role or the required permissions. If you don't have either, contact your billing account administrator. 

For more information, see: 

- Find a Billing Account Administrator 

(/billing/docs/how-to/find-billing-account-administrator) 

- Before you begin in Get subscriptions and assign licenses for Gemini 

Enterprise (/gemini/enterprise/docs/licenses#before-you-begin). 

#### Can I update the subscription name?

No, you can't update the subscription name after the subscription is created. 

If the subscription name is shown as `n/a` , it is a placeholder for a subscription purchased through a sales channel or an offline order form, and it doesn't mean 

#### Can I reduce the license count?

No, you can't reduce the license count during an active subscription term. License reductions are only possible when the subscription term ends or is up for renewal. 

#### Why can't I modify or manage the subscription through Google Cloud console?

If you purchased your subscription through an offline order form, you can't modify or manage it directly within the Google Cloud console. Offline order forms are handled outside of the console's self-service interface. To make any changes or updates to your subscription, such as adjusting license counts or renewing, contact your Google Account Manager. 

#### Why is Edit turned off on the Manage Users page?

In the **Gemini Enterprise licenses** section on the **Manage Users** page, the **Edit** button is turned off. 

You can't modify subscription settings directly on this page. Instead, to update settings like license counts, see Update subscription settings (/gemini/enterprise/docs/licenses#update-subscription). 

#### What does the `Subscription already exists` error mean when trying to purchase a new subscription?

This error means that you have already purchased a subscription for the same Gemini Enterprise edition and subscription period (monthly or annually) within the same billing account. 

To use a subscription for a different project or projects, you need to: 

1. Update the existing subscription 

(/gemini/enterprise/docs/licenses#update-subscription) to increase the license count. 

2. Distribute the licenses (/gemini/enterprise/docs/licenses#distribute-licenses) to the new project. 

#### Do free-trial licenses include the AI developer tools quota?

Yes. If your project uses an invoiced Cloud Billing account 

(/billing/docs/concepts#billing_account_types), a free-trial subscription for the Gemini Enterprise Standard or Plus edition includes access to AI developer tools 

(/gemini/enterprise/docs/ai-developer-tools-overview) and its base pooled credit quota. For details on credit amounts and weekly pool calculations, see Quotas for Standard and Plus editions 

(/gemini/enterprise/docs/quotas-and-overages#quotas-standard-plus). 

Free-trial seats draw from the same project-level pooled quota allocation as paid seats. However, free-trial subscriptions aren't eligible for overages 

(/gemini/enterprise/docs/quotas-and-overages#overages). 

### Distribute and assign licenses

This section covers common questions related to distributing and assigning Gemini Enterprise licenses to projects and users. 

#### Can I use one Gemini Enterprise subscription across multiple projects?

Yes, the Gemini Enterprise subscription is managed at the billing account level. This means that any project associated with that billing account can be allocated licenses from your subscription. You can distribute the licenses 

(/gemini/enterprise/docs/licenses#distribute-licenses) to multiple projects as needed, allowing flexibility in how you manage access across your different development or production environments. 

#### Can I distribute licenses to a project in a different organization?

Yes, you can distribute licenses to a project in a different organization. Gemini Enterprise subscriptions are managed at the billing account level. Since a single 

billing account can be linked to projects across different organizations, you can allocate licenses to any project associated with that billing account, regardless of its organizational affiliation. 

#### How do I move or share licenses to a different project or region?

To move, share, or correct a license allocation to a different project or region, follow these steps: 

1. Reclaim the unassigned licenses (/gemini/enterprise/docs/licenses#reclaim-licenses) from the project where they are allocated. 

2. After the licenses are reclaimed, distribute them 

(/gemini/enterprise/docs/licenses#distribute-licenses) to the new target project or the correct region. 

#### How do I check the list of projects the licenses are allocated to?

To see which projects are allocated licenses from your Gemini Enterprise subscription, use the REST API. The subscription details method 

(/gemini/enterprise/docs/licenses#subscription-detail) provides the information you need, including how you distribute licenses across projects linked to your billing account. 

#### Can I use a license assigned to me in different projects?

No, a user's license for Gemini Enterprise is only valid within the specific project where you distributed it. While you manage subscriptions at the billing account level, you allocate licenses on a per-project basis. Therefore, if you need to use Gemini Enterprise features in multiple projects, you must explicitly distribute licenses to each of those projects. 

### Troubleshoot

This section covers common issues and their solutions related to Gemini Enterprise licenses. 

#### Why am I unable to distribute licenses?

Check the following details: 

- Verify that you have enabled the Discovery Engine API in the project you are distributing the licenses to. 

- Verify you have the Billing Account Administrator 

- (/iam/docs/roles-permissions/billing#billing.admin) role ( `roles/billing.admin` ) or a custom role with the required permissions. For more information, see Before you begin in Get subscriptions and assign licenses for Gemini Enterprise 

- (/gemini/enterprise/docs/licenses#before-you-begin). 

- The Google Cloud console does not support distributing licenses to multiple projects. Therefore, use the REST API method 

- (/gemini/enterprise/docs/licenses#distribute-licenses) for this task. 

#### What does the `Not enough licenses remaining` error mean?

This error means you are trying to reclaim more licenses than what is available and unassigned. You can only reclaim licenses that are not assigned to users. To resolve this, reduce the number of licenses you are attempting to reclaim, or unassign licenses from users. 

What does the `The quantity exceeds the maximum limit of seats for this account` error mean? 

When you're purchasing or modifying licenses directly in the Google Cloud console, this error occurs if you try to buy more seats than allowed for your Cloud Billing account type. 

**Self-serve (or Online) and resold billing accounts:** Up to **25 seats** . **Invoiced (or Offline) billing accounts:** Up to **1,000 seats** . 

If you attempt to increase your seat count beyond these thresholds from the Google Cloud console, or if you attempt to add seats to an account that was previously provisioned above these limits using an offline order form, the operation fails with a maximum seat limit error. 

To request seat counts above the online limits, contact your Google Cloud sales representative or account manager to update your order or apply an allowlist exception for your billing account. 

#### What does the `404 Error: License config not found` error mean?

This error means there is a problem with the request parameter. Before reclaiming or distributing any licenses, verify the subscription information on the Subscription details page (/gemini/enterprise/docs/licenses#subscription-detail) and the region (Current location) and license config ID (Subscription ID) in the Manage Users page (/gemini/enterprise/docs/licenses#view-licenses). 

#### Why can't users access Gemini Enterprise features even though they have licenses?

Common reasons why users might not be able to access features: 

- **Subscription type:** Check if the user's license is from a subscription type that includes the specific features they are trying to access. 

- **IAM Roles:** Confirm the user has the Gemini Enterprise User role (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) 

- ( `roles/discoveryengine.agentspaceUser` ) for the Gemini Enterprise project. For more information, see IAM roles and permissions 

(/gemini/enterprise/docs/access-control). 

- **Workforce Identity Federation:** If you are using Workforce Identity Federation (/gemini/enterprise/docs/configure-identity-provider), verify that it is correctly configured, as misconfigurations can lead to access issues. 

Last updated 2026-10-14 UTC. 



## Security Overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/security-overview

Google helps organizations secure their cloud environment, protect their data, and comply with industry regulations. For general information about security across all of Google Cloud, see Google Cloud security overview (/docs/security/overview/whitepaper). 

### End user security configurations

Managing your Identity and Access Management (IAM) settings within Gemini Enterprise is crucial for security. The resources listed in this section help you understand the permissions and access controls in Gemini Enterprise: 

- Identity and permissions (/gemini/enterprise/docs/identity) 

- Set up external identities (/gemini/enterprise/docs/identity-mapping) 

- Authenticate to Gemini Enterprise API (/gemini/enterprise/docs/authentication) 

- Access control with IAM (/gemini/enterprise/docs/access-control) 

The following authentication frameworks are supported: 

Workforce Identity Federation (/iam/docs/workforce-identity-federation) 

**Note:** When you send data to Gemini Enterprise using a third-party connector, we recommend using Workforce Identity Federation (WIF). 

- Google Identity (https://developers.google.com/identity) 

- Workload Identity Federation (/iam/docs/workload-identity-federation) 

### Gemini Enterprise data security

Protecting your data from threats, breaches, and identity theft is important. Gemini Enterprise has the following security measures in place: 

- Gemini Enterprise is integrated with VPC Service Controls (/vpc-service-controls/docs/supported-products). 

- Default data encryption with Customer Managed Encryption Keys (CMEK) (/gemini/enterprise/docs/cmek). 

Gemini Enterprise also supports External key manager (EKM) or hardware security module (HSM). For information about the limitations that apply to CMEK and EKM, see Limitations of Cloud Key Management Service in Gemini Enterprise (/gemini/enterprise/docs/cmek#limitations). 

### Gemini Enterprise compliance

Data compliance involves meeting legal and regulatory requirements for handling personal and sensitive information. It governs data collection, storage, usage, and security to ensure privacy and protection. 

The resources listed in this section provide information to help you maintain data transparency and compliance: 

- Enable access transparency (/gemini/enterprise/docs/access-transparency) 

- Audit logging (/gemini/enterprise/docs/audit-logging) 

- Gemini Enterprise locations (/gemini/enterprise/docs/locations) 

- Compliance certifications and security controls 

- (/gemini/enterprise/docs/compliance-security-controls) 

- Gemini Enterprise deletes user-requested data within 60 days. For more information, see Data deletion on Google Cloud (/docs/security/deletion). 

### Workforce Identity Federation and pool administrators

If you use Workforce Identity Federation to authenticate your users, you grant the IAM Workforce Identity Pool Admin ( `roles/iam.workforcePoolAdmin` ) and IAM Workforce Pool Editor ( `roles/iam.workforcePoolEditor` ) IAM roles to some of your administrators. These roles can modify workforce pool attribute mappings. 

Incorrect changes, whether intentional or accidental, risk enabling user impersonation, which can lead to unauthorized document access and actions. 

For this reason, we recommend the following: 

- Only grant these workforce pool roles to trusted administrators who absolutely require them. 

- Use Privileged Access Manager (/iam/docs/pam-permissions-and-setup) to set up entitlements for these roles and to audit their use. 

- Integrate Workforce Identity Federation audit logs into your security monitoring solution (for example, SIEM) to quickly detect and alert on any changes to attribute mappings or unauthorized access attempts. 

### Required Google Cloud APIs

To begin using Gemini Enterprise, the following APIs must be enabled: 

- Vertex AI API 

- Gemini Enterprise (Discovery Engine) API 

- Cloud Storage API 

- Identity and Access Management API 

For more information on getting started with Gemini Enterprise, see the Before you begin (/gemini/enterprise/docs/quickstart-gemini-enterprise#before-you-begin) section. 

To disable the Gemini Enterprise (Discovery Engine) API, see Turn of Geminif Enterprise (/gemini/enterprise/docs/turn-off-gemini-enterprise). 

### Third-party connectors and public endpoints

Third-party connectors interact with public endpoints outside Google's network; for example, endpoints for a third-party's API for polling data or a webhook URL for real-time synchronization. Because VPC Service Controls are designed to govern 

Google Cloud services, they don't inherently block or secure traffic to these external, non-Google endpoints. 

To mitigate, Gemini Enterprise makes sure that your egress traffic is secured by granular VPC Firewall rules, which restrict outbound connections to only the Fully Qualified Domain Names (FQDNs) of the external service you provide. 

Last updated 2026-10-14 UTC.
