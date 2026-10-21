# Gemini Enterprise: platform, security, agents, cost, monitoring / Manage resources with custom organization policies to Enable Model Armor for Gemini Notebook Enterprise
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 180-218, extracted 2026-10-18

Contains:
- Manage resources with custom organization policies (pages 180-192) https://docs.cloud.google.com/gemini/enterprise/docs/org-policy-custom-constraints
- Configure private UI access (pages 193-198) https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access
- Enable Model Armor (pages 199-207) https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor
- Enable Model Armor for Gemini Notebook Enterprise (pages 208-218) https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/enable-model-armor

## Manage resources with custom organization policies

URL: https://docs.cloud.google.com/gemini/enterprise/docs/org-policy-custom-constraints

This page shows you how to use Organization Policy Service custom constraints to restrict specific operations on the following Google Cloud resources: 

```
discoveryengine.googleapis.com/DataStore
discoveryengine.googleapis.com/Engine
```

- `discoveryengine.googleapis.com/DataConnector` 

To learn more about Organization Policy, see Custom organization policies (/organization-policy/overview#custom-organization-policies). 

### About organization policies and constraints

The Google Cloud Organization Policy Service gives you centralized, programmatic control over your organization's resources. As the organization policy administrator (/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin), you can define an organization policy, which is a set of restrictions called _constraints_ that apply to Google Cloud resources and descendants of those resources in the Google Cloud resource hierarchy (/resource-manager/docs/cloud-platform-resource-hierarchy). You can enforce organization policies at the organization, folder, or project level. 

Organization Policy provides built-in managed constraints 

(/organization-policy/reference/org-policy-constraints) for various Google Cloud services. However, if you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can also create _custom constraints_ and use those custom constraints in an organization policy. 

#### Policy inheritance

By default, organization policies are inherited by the descendants of the resources on which you enforce the policy. For example, if you enforce a policy on a folder, Google Cloud enforces the policy on all projects in the folder. To learn more about 

this behavior and how to change it, refer to Hierarchy evaluation rules (/organization-policy/hierarchy-evaluation#disallow_inheritance). 

### Before you begin

1. Sign in to your Google Cloud account. If you're new to Google Cloud, create an account (https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project. 

<sup>**Roles required to select or create a project**</sup> 

- **Select a project** : Selecting a project doesn't require a specific IAM role— you can select any project that you've been granted a role on. 

- **Create a project** : To create a project, you need the Project Creator role ( `roles/resourcemanager.projectCreator` ), which contains the `resourcemanager.projects.create` permission. Learn how to grant roles (/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project. 

Go to project selector (https://console.cloud.google.com/projectselector2/home/dashboard) 

3. Verify that billing is enabled for your Google Cloud project 

   - (/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

4. Install (/sdk/docs/install) the Google Cloud CLI. 

5. If you're using an external identity provider (IdP), you must first sign in to the gcloud CLI with your federated identity (/iam/docs/workforce-log-in-gcloud). 

6. To initialize (/sdk/docs/initializing) the gcloud CLI, run the following command: 

```
gcloud init
```

7. Ensure that you know your organization ID (/resource-manager/docs/creating-managingorganization#retrieving_your_organization_id) 

#### Required roles

To get the permissions that you need to manage custom organization policies, ask your administrator to grant you the Organization Policy Administrator 

(/iam/docs/roles-permissions/orgpolicy#orgpolicy.policyAdmin) 

( `roles/orgpolicy.policyAdmin` ) IAM role on the organization resource. For more information about granting roles, see Manage access to projects, folders, and organizations (/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through custom roles (/iam/docs/creating-custom-roles) or other predefined roles (/iam/docs/roles-overview#predefined). 

### Gemini Enterprise supported resources

The following table lists the Gemini Enterprise resources and fields that you can reference in custom constraints. 

|Resource type|Supported fields|
|---|---|
|`discoveryengine.`<br>`googleapis.com/Engine`|`resource.dataStoreIds`<br>`resource.disableAnalytics`|
||`resource.displayName`|
||`resource.industryVertical`|
||`resource.name`|
||`resource.solutionType`|

|Resource type<br>Supported fields|
|---|
|`discoveryengine.`<br>`googleapis.com/DataStore`<br>`resource.aclEnabled`<br>`resource.contentConfig`|
|`resource.displayName`|
|`resource.identityMappingStore`|
|`resource.industryVertical`|
|`resource.isInfobotFaqDataStore`|
|`resource.name`|
|`resource.servingConfigDataStore.disabledForServing`|
|`resource.solutionType`|

|Resource type|Supported fields|
|---|---|
|`discoveryengine.`<br>`googleapis.com/Data`<br>`Connector`|`resource.aclEnabled`<br>`resource.actionConfig`<br>`resource.alertPolicyConfigs`<br>`resource.autoRunDisabled`<br>`resource.bapConfig`|
||`resource.connectorModes`|
||`resource.createEuaSaas`|
||`resource.dataSource`|
||`resource.destinationConfigs`|
||`resource.egressFqdns`|
||`resource.endUserConfig`|
||`resource.entities`|
||`resource.federatedConfig`|
||`resource.hybridIngestionDisabled`|
||`resource.identityScheduleConfig`|
||`resource.incrementalRefreshInterval`<br>`resource.incrementalSyncDisabled`|
||`resource.kmsKeyName`|
||`resource.nextSyncTime`|
||`resource.realtimeSyncConfig`|
||`resource.refreshInterval`|
||`resource.removeParamKeys`|
||`resource.staticIpEnabled`|
||`resource.syncMode`|
||`resource.vpcscEnabled`|

### Set up a custom constraint

A custom constraint is defined in a YAML file by the resources, methods, conditions, and actions that are supported by the service on which you are enforcing the organization policy. Conditions for your custom constraints are defined using Common Expression Language (CEL) 

(https://github.com/google/cel-spec/blob/master/doc/intro.md). For more information about how to build conditions in custom constraints using CEL, see the CEL section of Creating and managing custom constraints 

(/organization-policy/create-custom-constraints#common_expression_language). 

Consolegcloud (#gcloud) (#console) 

To create a custom constraint, do the following: 

1. In the Google Cloud console, go to the **Organization policies** page. 

Go to Organization policies (https://console.cloud.google.com/iam-admin/orgpolicies) 

2. From the project picker, select the project that you want to set the organization policy for. 

3. Click **Custom constraint** . 

4. In the **Display name** box, enter a human-readable name for the constraint. This name is used in error messages and can be used for identification and debugging. Don't use personally identifiable information (PII) or sensitive data in display names because this name could be exposed in error messages. This field can contain up to 200 characters. 

5. In the **Constraint ID** box, enter the ID that you want for your new custom constraint. A custom constraint can only contain letters (including upper and lowercase) or numbers, for example `custom.restrictSolutionType` . This field can contain up to 70 characters, not counting the prefix ( `custom.` ), for example, `organizations/123456789/customConstraints/custom` . Don't include PII or sensitive data in your constraint ID, because it could be exposed in error messages. 

6. In the **Description** box, enter a human-readable description of the constraint. This description is used as an error message when the policy is violated. Include details about why the policy violation occurred and how to resolve the policy violation. Don't include PII or sensitive data in your description, because it could be exposed in error messages. This field can contain up to 2000 characters. 

7. In the **Resource type** box, select the name of the Google Cloud REST resource containing the object and field that you want to restrict—for example, `container.googleapis.com/NodePool` . Most resource types support up to 20 custom constraints. If you attempt to create more custom constraints, the operation fails. 

8. Under **Enforcement method** , select whether to enforce the constraint on a REST `CREATE` method or both `CREATE` and `UPDATE` methods. If you enforce the constraint with the `UPDATE` method on a resource that violates the constraint, changes to that resource are blocked by the organization policy unless the change resolves the violation. 

To see supported methods for each service, find the service in Services that support custom constraints 

(/organization-policy/reference/custom-constraint-supported-services). 

9. To define a condition, click **Edit condition** . 

   - a. In the **Add condition** panel, create a CEL condition that refers to a supported service resource, for example, `resource.management.autoUpgrade == false` . This field can contain up to 1000 characters. For details about CEL usage, see Common Expression Language 

      - (/resource-manager/docs/organization-policy/creating-managing-customconstraints#common_expression_language) 

      - . For more information about the service resources you can use in your custom constraints, see Custom constraint supported services (/resource-manager/docs/organization-policy/custom-constraint-supportedservices) 

   - b. Click **Save** . 

10. Under **Action** , select whether to allow or deny the evaluated method if the condition is met. 

The deny action means that the operation to create or update the resource is blocked if the condition evaluates to true. 

The allow action means that the operation to create or update the resource is permitted only if the condition evaluates to true. Every other case except those explicitly listed in the condition is blocked. 

11. Click **Create constraint** . 

When you have entered a value into each field, the equivalent YAML configuration for this custom constraint appears on the right. 

### Enforce a custom organization policy

You can enforce a constraint by creating an organization policy that references it, and then applying that organization policy to a Google Cloud resource. 

Consolegcloud (#gcloud) (#console) 

1. In the Google Cloud console, go to the **Organization policies** page. 

Go to Organization policies (https://console.cloud.google.com/iam-admin/orgpolicies) 

2. From the project picker, select the project that you want to set the organization policy for. 

3. From the list on the **Organization policies** page, select your constraint to view the **Policy details** page for that constraint. 

4. To configure the organization policy for this resource, click **Manage policy** . 

5. On the **Edit policy** page, select **Override parent's policy** . 

6. Click **Add a rule** . 

7. In the **Enforcement** section, select whether this organization policy is enforced or not. 

8. Optional: To make the organization policy conditional on a tag, click **Add condition** . Note that if you add a conditional rule to an organization 

policy, you must add at least one unconditional rule or the policy cannot be saved. For more information, see Scope organization policies with tags (/organization-policy/scope-policies). 

9. Click **Test changes** to simulate the effect of the organization policy. For more information, see Test organization policy changes with Policy Simulator (/policy-intelligence/docs/test-organization-policies). 

10. To enforce the organization policy in dry-run mode, click **Set dry run policy** . For more information, see Test organization policies (/organization-policy/test-policies). 

11. After you verify that the organization policy in dry-run mode works as intended, set the live policy by clicking **Set policy** . 

### Test the custom organization policy

The following example creates a custom constraint that prevents you from creating an app (engine) with `SOLUTION_TYPE_CHAT` . 

**Note:** In Gemini Enterprise, an engine is referred to as an _app_ . However, when creating a custom constraint, you must use the resource type **`discoveryengine.googleapis.com/Engine`** . 

gcloud 

(#gcloud) 

1. Create a `restrictChatEngine.yaml` constraint file with the following information. Replace _`ORGANIZATION_ID`_ with your organization ID. 

```
name:
organizations/ORGANIZATION_ID/customConstraints/custom.restrictChatApp
resourceTypes: discoveryengine.googleapis.com/Engine
condition: "resource.solutionType == 'SOLUTION_TYPE_CHAT'"
actionType: DENY
methodTypes: CREATE
displayName: Restrict creation of chat apps
description: Chat apps cannot be created.
```

2. Set the custom constraint. 

```
gcloud org-policies set-custom-constraint restrictChatEngine.yaml
```

3. Create a `restrictChatEngine-policy.yaml` policy file with the following information. In this example we enforce this constraint at the project level but you might also set this at the organization or folder level. Replace _`PROJECT_ID`_ with your project ID. 

```
name: projects/PROJECT_ID/policies/custom.restrictChatEngine
spec:
 rules:
   enforce: true
```

4. Enforce the policy. 

```
gcloud org-policies set-policy restrictChatEngine-policy.yaml
```

5. Test the constraint by trying to create an app (engine) with `SOLUTION_TYPE_CHAT` . Wait about two minutes for the policy to be enforced, and then run the following command. 

```
gcloud discovery engine engines create my-chat-app \
```

- `--project=` _`PROJECT_ID`_ `\` 

- `--location=global \` 

- `--solution-type=SOLUTION_TYPE_CHAT \` 

- `--display-name="Chat app"` 

The output is similar to the following: 

```
ERROR: (gcloud.discovery.engine.engines.create) FAILED_PRECONDITION:
Operation denied by custom org policy on resource 'projects/my-
project': ["customConstraints/custom.restrictChatApp" : "Chat app
cannot be created."]
```

### Example custom organization policies for common use cases

This table provides syntax examples for some common custom constraints. 

|Description|Constraint syntax|
|---|---|
|Require data<br>stores to have<br>`GENERIC`industry<br>vertical|`name:`<br>`organizations/`<br>`/customConstraints/custom.dataStore`<br>`GenericVertical`<br>`resourceTypes: discoveryengine.googleapis.com/DataStore`<br>`condition: "resource.industryVertical == 'GENERIC'"`<br>`actionType: ALLOW`<br>`methodTypes:`<br>`- CREATE`<br>`- UPDATE`<br>`displayName: Require GENERIC industry vertical for Data Stores`<br>`description: All data stores must use the GENERIC industry`<br>`vertical.`<br>_`ORGANIZATION_ID`_|
|Prevent data<br>stores with<br>`PUBLIC_WEBSITE`<br>content config|`name:`<br>`organizations/`<br>`/customConstraints/custom.restrictP`<br>`ublicWebsite`<br>`resourceTypes: discoveryengine.googleapis.com/DataStore`<br>`condition: "resource.contentConfig == 'PUBLIC_WEBSITE'"`<br>`actionType: DENY`<br>`methodTypes:`<br>`- CREATE`<br>`- UPDATE`<br>`displayName: Restrict PUBLIC_WEBSITE content config`<br>`description: Data stores cannot use the PUBLIC_WEBSITE content`<br>`config.`<br>_`ORGANIZATION_ID`_|

Description Constraint syntax 

Require apps to `name:` have `disable organizations/` _`ORGANIZATION_ID`_ `/customConstraints/custom.appDisabl` `Analytics` set to `eAnalytics` true `resourceTypes: discoveryengine.googleapis.com/Engine condition: "resource.disableAnalytics == true" actionType: ALLOW methodTypes: - CREATE - UPDATE displayName: Require disableAnalytics for apps description: All apps must have analytics disabled.` 

Prevent creation of `name:` custom MCP `organizations/` _`ORGANIZATION_ID`_ `/customConstraints/custom.restrictC` connectors `ustomMcpConnector resourceTypes: discoveryengine.googleapis.com/DataConnector condition: "resource.dataSource == 'custom_mcp'" actionType: DENY methodTypes: - CREATE displayName: Restrict custom MCP connectors description: Custom MCP connectors cannot be created.` 

### What's next

Learn more about Organization Policy Service (/organization-policy/overview). 

Learn more about how to create and manage organization policies 

- (/organization-policy/create-organization-policies). 

See the full list of managed organization policy constraints 

- (/organization-policy/reference/org-policy-constraints). 

Last updated 2026-10-16 UTC. 



## Configure private UI access

URL: https://docs.cloud.google.com/gemini/enterprise/docs/private-ui-access

By default, users access Gemini Enterprise interfaces for features such as agents, the assistant, and Gemini Notebook Enterprise, through the public internet. To meet organizational security requirements, you can establish private UI access using hybrid networking solutions like Cloud VPN or Cloud Interconnect. 

To configure private connectivity to Gemini Enterprise, you must route Google Cloud API traffic through a Private Service Connect (PSC) endpoint. This allows users to access Gemini Enterprise interfaces through an internal IP address within your Virtual Private Cloud (VPC), avoiding the public internet. 

_Reference architecture using VPC Service Controls to provide private access to Gemini Enterprise UIs._ 

In this reference architecture, on-premises or multi-cloud users connect to a PSC endpoint (/vpc/docs/about-accessing-google-apis-endpoints), which enables access to Google APIs through a user-defined internal IP address within your Google Cloud Virtual Private Cloud. In addition, you must configure your internal DNS to resolve Gemini Enterprise domains to the IP address of the PSC endpoint. 

### Before you begin

Before configuring private UI access, ensure that you have the following: 

- A Google Cloud Virtual Private Cloud network connected to your on-premises network through Cloud Router, using Cloud VPN 

- (/network-connectivity/docs/vpn/concepts/overview) or Cloud Interconnect 

- (/network-connectivity/docs/interconnect/concepts/overview). 

- Permissions to create Private Service Connect endpoints and manage Cloud Router custom routes. 

### Configure Private Service Connect

Private and restricted virtual IP addresses (VIPs) used for Private Google Access don't support private access to the Gemini Enterprise UI. To ensure full functionality, you must resolve the Gemini Enterprise domains to a Private Service Connect endpoint configured with the `all-apis` bundle. 

1. Create a new PSC endpoint in the same Virtual Private Cloud as the Cloud Router used for hybrid networking. 

2. Target the **All Google APIs** API bundle. This bundle provides access to most Google APIs, including `*.googleapis.com` service endpoints. The **VPC-SC** API bundle doesn't support all Gemini Enterprise domains. 

**Note:** The Google APIs DNS zone **`*.p.googleapis.com`** is automatically generated when you create a PSC endpoint. However, using this zone from an on-premises or VPC network isn't supported in Gemini Enterprise. 

### Configure network routing

The PSC endpoint uses a `/32` IP address that doesn't originate from a standard VPC subnet and won't be visible from on-premises or multi-cloud networks. You must configure your Cloud Router to advertise the IP address. For more information about IP address requirements for Private Service Connect endpoints, see IP address requirements 

(/vpc/docs/about-accessing-google-apis-endpoints#ip-address-requirements). 

1. Identify the IP address that you assigned to your PSC endpoint. 

2. In your Cloud Router configuration, create a custom route for the IP address. For more information about specifying custom advertised routes on a Cloud Router, see Advertise custom address ranges 

   - (/network-connectivity/docs/router/how-to/advertising-custom-ip). 

3. Update on-premises or multi-cloud firewalls to permit outbound traffic to the IP address. 

### Update DNS settings

Finally, update your DNS settings to resolve the Gemini Enterprise domains using the PSC endpoint. For more information, see Create DNS records by using default DNS names (/vpc/docs/configure-private-service-connect-apis#configure-dns-default). 

1. Configure internal on-premises or cloud network DNS records to resolve the following Gemini Enterprise domains to the internal IP address of the PSC endpoint: 

   - `content-discoveryengine.googleapis.com` 

   - `content-discoveryengine.mtls.googleapis.com` 

   - `content-eu-discoveryengine.googleapis.com` 

   - `content-eu-discoveryengine.mtls.googleapis.com` 

   - `content-global-discoveryengine.googleapis.com` 

   - `content-global-discoveryengine.mtls.googleapis.com` 

   - `content-us-discoveryengine.googleapis.com` 

   - `content-us-discoveryengine.mtls.googleapis.com` 

   - `content-webchannel-assistant-discoveryengine.googleapis.com` 

   - `content-us-webchannel-assistant-discoveryengine.googleapis.com` 

   - `content-eu-webchannel-assistant-discoveryengine.googleapis.com` 

   - `discoveryengine.googleapis.com` 

   - `discoveryengine.mtls.googleapis.com` 

   - `discoveryengine.clients6.google.com` 

   - `eu-discoveryengine.clients6.google.com` 

   - `us-discoveryengine.clients6.google.com` 

   - `eu-discoveryengine.googleapis.com` 

   - `eu-discoveryengine.mtls.googleapis.com` 

   - `global-discoveryengine.googleapis.com` 

   - `global-discoveryengine.mtls.googleapis.com` 

   - `us-discoveryengine.googleapis.com` 

   - `us-discoveryengine.mtls.googleapis.com` 

   - `vertexaisearch.cloud.google.com` 

   - `vertexaisearch.cloud.google` 

   - `notebooklm.cloud.google.com` 

   - `notebooklm.cloud.google` 

   - `auth.cloud.google` 

   - `payments.cloud.google` 

   - `accounts.googleapis.com` 

2. If your environment requires strict data exfiltration protection boundaries, configure the `discoveryengine.googleapis.com` domain to the VPC-SC bundle IP address. 

### Configure proxies, firewalls, and TLS inspection

If your users access Gemini Enterprise through a corporate proxy, secure web gateway, or firewall, configure these devices so that they don't block, buffer, or time out Gemini Enterprise traffic. These requirements apply whether users connect through the public internet or through a Private Service Connect endpoint. 

If you don't configure these devices correctly, users might see the following symptoms: 

- The assistant stays in the **Thinking...** state and then displays the whole answer at once, instead of streaming the answer as it's generated. 

- Requests consistently fail after a fixed duration, such as 20, 30, or 60 seconds, with errors such as `HTTP 499` or `HTTP 504` . 

- The web app works on some networks, such as a home network, but not on the corporate network. 

To avoid these issues, do the following: 

1. Allow outbound HTTPS traffic on port `443` to all of the Gemini Enterprise domains listed in Update DNS settings (#update-dns-settings). Allow the `global` , `us` , and `eu` domains even if your app uses a single location, because the web app can call more than one of these endpoints. 

2. Exclude the following streaming domains from TLS (SSL) inspection and from response buffering or content scanning. The assistant streams its answers over these connections, and devices that hold the response until it's complete cause delays and timeouts. 

   - `content-webchannel-assistant-discoveryengine.googleapis.com content-us-webchannel-assistant-discoveryengine.googleapis.com content-eu-webchannel-assistant-discoveryengine.googleapis.com` 

3. Set the idle and read timeouts on proxies, load balancers, and firewalls in the request path to at least 300 seconds. Complex requests, such as requests that use several connectors or agents, can take several minutes to complete. 

4. If you call the Gemini Enterprise API from your own applications, set the client request timeout to at least 300 seconds and use streaming methods where 

### About securing your app with VPC Service Controls

For advanced security, you can implement VPC Service Controls (VPC-SC) to prevent data exfiltration from managed services like Gemini Enterprise and BigQuery. Unlike Identity and Access Management, which controls _who_ can access data, VPC-SC controls dictate _where_ data can be accessed and moved. 

If considering this approach, keep the following in mind: 

- While optional, using VPC Service Controls is a best practice for blocking public access to Google services exposed through `googleapis.com` . 

- Among other implications, services (such as `discoveryengine.googleapis.com` ) that are added to a VPC-SC perimeter are blocked to all public access, including access through the Google Cloud console. 

- To allow access to protected services within a VPC-SC perimeter, admins must explicitly allow ingress, by using VPC-SC ingress rules 

- (/vpc-service-controls/docs/ingress-egress-rules) or defining access levels using Access Context Manager 

- (/gemini/enterprise/docs/use-vpc-service-controls#access-context-manager). 

For more information about securing your Gemini Enterprise app using VPC-SC and Access Context Manager, see Secure your app with VPC Service Controls 

(/gemini/enterprise/docs/use-vpc-service-controls). 

Last updated 2026-10-14 UTC. 



## Enable Model Armor

URL: https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor

This document describes how to enable Model Armor 

(/security-command-center/docs/model-armor-overview) for Gemini Enterprise. Model Armor is a Google Cloud service that enhances the security and safety of your AI applications by proactively screening the prompts and responses given by the Gemini Enterprise assistant. This helps protect against various risks and ensures responsible AI practices. Model Armor is supported on all Gemini Enterprise editions at no additional cost. 

Model Armor does not remove or alter personally identifiable information (PII) or mask sensitive data. However, Gemini Enterprise blocks any response from the Gemini Enterprise assistant that triggers Sensitive Data Protection detectors. 

**Note:** Enabling Model Armor in Gemini Enterprise can increase latency. 

Model Armor's response to potential issues in user queries or responses from the Gemini Enterprise assistant is governed by the template's enforcement type. For more information, see Define the enforcement type 

(/security-command-center/docs/model-armor-overview#define-enforcement-type). 

- If the enforcement type is **Inspect and block** , Gemini Enterprise blocks the request and displays an error message. This is the default enforcement type when you create a Model Armor template using the console. 

- If the enforcement type is **Inspect only** , Gemini Enterprise does not block the requests or responses. 

When the Model Armor screening service is unavailable, you can configure Gemini Enterprise to behave in one of the following ways: 

|Mode|Description|
|---|---|
|Allow user interactions|In this mode, Gemini Enterprise allows requests and responses to pass<br>through without proactive screening when the Model Armor screening<br>service is unavailable, ensuring continuous communication with the<br>end-user. However, this can occasionally expose unscreened messages<br>or provide answers to unscreened queries.|
|Block all user<br>interactions|In this mode, when the Model Armor screening service is unavailable,<br>Gemini Enterprise blocks all requests and responses, including<br>legitimate ones.|

### Before you begin

- Make sure you have the required roles assigned to you and the service account: 

   - To enable Model Armor in Gemini Enterprise, you need the Gemini Enterprise Admin 

   - (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) role. 

   - To create the Model Armor templates, you need the Model Armor Admin (/iam/docs/roles-permissions/modelarmor#modelarmor.admin) role ( `roles/modelarmor.admin` ) . 

   - To call the Model Armor APIs, you need the Model Armor User (/iam/docs/roles-permissions/modelarmor#modelarmor.user) role ( `roles/modelarmor.user` ). 

**Note:** To grant multiple IAM roles to a service account, see Grant or revoke multiple IAM roles using the Google Cloud console 

(/iam/docs/manage-access-service-accounts#multiple-roles-console). 

- If your Model Armor template is in a different project than your Gemini Enterprise app, the template's project must grant the Model Armor User (/iam/docs/roles-permissions/modelarmor#modelarmor.user) role ( `roles/modelarmor.user` ) to the Gemini Enterprise app's service account 

(/iam/docs/service-agents#discovery-engine-service-account). The service account ID is `service-` _`PROJECT_NUMBER`_ `@gcp-sa-` 

   - `discoveryengine.iam.gserviceaccount.com` , where _`PROJECT_NUMBER`_ is the project number of your Gemini Enterprise app. 

- Ensure you have created a Gemini Enterprise app. To create one, see Create an app (/gemini/enterprise/docs/create-app). 

### Create a Model Armor template

We recommend that you configure two separate Model Armor templates: one for user prompts and one for responses. User prompts and responses have different risk profiles and objectives: 

- **Template for user prompts** : Focuses on preventing malicious inputs, prompt injections, jailbreak attempts, and sensitive data from being sent or uploaded. Although harmful content is also a concern for user inputs, you can disable responsible AI filters on the user prompt template because Gemini includes built-in safety checks for user prompts. 

- **Template for response outputs** : Focuses on preventing responses from returning or leaking sensitive data, generating harmful or off-brand content, or returning malicious URLs. 

For more information about creating templates, see Create a Model Armor template (/security-command-center/docs/manage-model-armor-templates). 

#### Configuration considerations

When creating a Model Armor template for Gemini Enterprise apps, consider these configurations: 

- You can create Model Armor templates centrally in one project and reuse them across different projects. If you use a cross-project template, ensure that the cross-project permissions are configured as described in Before you begin (#before-you-begin). 

- Select **Multi-region** in the **Regions** field. The following table shows you how to map Model Armor template regions to Gemini Enterprise app regions: 

**Note:** After a Model Armor template or a Gemini Enterprise app is created, the regions can't be changed. 

|Gemini Enterprise app multi-region|Model Armor multi-region|
|---|---|
|Global|US (multiple regions in United States)|
||EU (multiple regions in the Europe Union)|
|US (multiple regions in United States)|US (multiple regions in United States)|
|EU (multiple regions in the Europe Union)|EU (multiple regions in the Europe Union)|

- Google does not recommend configuring cloud logging in the Model Armor template for Gemini Enterprise apps. This configuration can expose sensitive data to users with the Private Logs Viewer ( `roles/logging.privateLogViewer` ) IAM role. Instead, consider the following options: 

   - If you need to log the data that goes through the Model Armor template, you can reroute logs to a secure storage like BigQuery, which offers stricter access controls. For more information, see Route logs to supported destinations (/logging/docs/export/configure_export_v2). 

   - You can configure Data Access audit logs to analyze and report on the request and response screening verdicts generated by Model Armor. For more information, see Configure audit logs (#configure_audit_logs). 

- Avoid turning on the prompt injection and jailbreak detection filter for responses. Prompt injection and jailbreak attacks are more commonly used in user prompts. Enabling this filter on responses can increase false positives and add unnecessary latency. 

### Configure the Gemini Enterprise app with the Model Armor templates

The following steps describe how to add the Model Armor templates to your Gemini Enterprise app. 

ConsoleREST (#rest) 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** > **Assistant** . 

4. To turn on Model Armor, click **Enable Model Armor** . 

5. For **Model Armor template for user prompts** and **Model Armor templates for response outputs** , enter the **Resource name** of the Model Armor templates you created. 

**Note:** To get the **Resource name** , follow the steps in the View a Model Armor template (/security-command-center/docs/manage-model-armor-templates#view-matemplate) 

documentation, and copy the **Resource name** value. You can use Model Armor templates created in the same project as the Gemini Enterprise app or use Model Armor templates from a different project. If you use a template from a different project, ensure the cross-project permissions are configured as described in Before you begin (#before-you-begin). 

6. If you want to block user interactions during Model Armor processing failures, click the **Allow user interactions during Model Armor processing failure** toggle to the off position. For more information, see the two modes supported by Gemini Enterprise when Model Armor is unavailable (#modes-when-model-armor-is-unavailable). 

7. Click **Save and publish** . 

### Test if the Model Armor template is enabled

After configuring the Model Armor template, test if your Gemini Enterprise app proactively screens and blocks user prompts and responses from the Gemini 

Enterprise assistant, according to the confidence levels set in the Model Armor filters. 

When the Model Armor template is configured to **Inspect and block** requests that violate the policy, the following policy violation message is shown: 

<!-- Start of picture text -->
ConsoleREST (#rest)<br>(#console)<br>For example, you see the policy violation message:<br>Model Armor policy violation message<br><!-- End of picture text -->

### Remove the Model Armor templates from a Gemini Enterprise app

To remove the Model Armor templates from a Gemini Enterprise app, use the Google Cloud console or the REST API. 

ConsoleREST (#rest) (#console) To remove the Model Armor templates from your Gemini Enterprise app, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** > **Assistant** . 

4. To turn off Model Armor, click the **Enable Model Armor** toggle to the off position. 

5. Click **Save and publish** . 

### Configure audit logs

Model Armor can write Data Access audit logs (/logging/docs/audit#data-access), which you can use to analyze and report on the request and response screening verdicts generated by Model Armor. These logs don't contain the user queries or responses from the Gemini Enterprise assistant, so they are safe for reporting and analytics. For more information, see Audit logging for Model Armor 

(/security-command-center/docs/audit-logging-model-armor). 

To access these logs, you need to have the Private Logs Viewer 

(/iam/docs/roles-permissions/logging#logging.privateLogViewer) ( `roles/logging.privateLogViewer` ) IAM role. 

#### Enable Data Access audit logs

To enable the Data Access audit logs, follow these steps: 

1. In the Google Cloud console, go to **IAM & Admin** > **Audit Logs** . 

2. Select the **Model Armor API** . 

3. In the **Permission type** section, select the **Data read** permission type. 

4. Click **Save** . 

#### Examine Data Access audit logs

To examine the Data Access audit logs, follow these steps: 

1. In the Google Cloud console, go to **Logs Explorer** . 

2. Search the logs for the following method names: 

- `methodName:` 

- `"google.cloud.modelarmor.v1.ModelArmor.SanitizeUserPrompt"` to view the user requests that were screened. 

- `google.cloud.modelarmor.v1.ModelArmor.SanitizeModelResponse` to view the responses that were screened. 

### Considerations when using Model Armor

When using Model Armor with Gemini Enterprise, consider the following: 

|De-identification<br>and masking|When Model Armor uses a Sensitive Data Protection template for scanning<br>prompts or responses, Model Armor checks if the content matches the<br>detector criteria defined in the template. Although Sensitive Data Protection<br>supports de-identification based on the template configuration, Model<br>Armor does not pass de-identified or masked data back to Gemini<br>Enterprise. If the content triggers any detectors from Sensitive Data<br>Protection and the enforcement type is`INSPECT_AND_BLOCK`, Gemini<br>Enterprise blocks the request or response rather than de-identifying it.|
|---|---|
|Token limits and<br>quotas|There are no token limits when you use Model Armor with Gemini<br>Enterprise. However, the total throughput of your Model Armor evaluations<br>is still indirectly governed by<br>Gemini Enterprise system quotas<br>(/gemini/enterprise/docs/quotas-and-overages) and<br>Model Armor API rate<br>limits(/model-armor/quotas#quotas).|
|Service Level<br>Agreement|Gemini Enterprise provides a<br>Service Level Agreement<br>(https://cloud.google.com/terms/gemini/enterprise/sla). When Gemini<br>Enterprise is configured to use Model Armor, blocked queries don't count as<br>SLA violations, regardless of whether the fail-open or fail-closed mode is<br>used.|
|Compliance|Both Gemini Enterprise and Model Armor offer various compliance<br>certifications. When used together, the effective compliance certifications<br>are the common subset of both products. Google recommends reviewing<br>the compliance certifications for both products to ensure that they meet<br>your regulatory requirements.|

In addition to text prompts, the Model Armor integration supports documents (such as PDFs) and images. The Model Armor integration screens the following files only when you upload them to the Gemini Enterprise assistant: 

Documents (such as PDFs, CSVs, and text files). 

Document and Images that you upload directly. image screening Images contained inside other files and documents that you upload directly. 

If a file or an image inside a document violates your configured policies, the entire file or document is discarded and excluded from the request. For the list of supported document types, see Document screening (/model-armor/overview#ma-support-screening-pdfs). 

If a Model Armor template is configured to screen user requests, only interactions with the following agents are screened in Gemini Enterprise: The Gemini Enterprise assistant 

Employee-made agents Screened (/gemini/enterprise/docs/agents-overview#types-of-agents), which are interactions and created in Gemini Enterprise app using the Workflow Builder. agents Google-made agents (/gemini/enterprise/docs/agents-overview#types-of-agents) Interactions with custom agents from your organization, such as ADK, A2A, and Dialogflow, are not screened. 

### What's next

Correlate Model Armor logs with Gemini Enterprise logs (/gemini/enterprise/docs/correlate-model-armor-logs) 

Last updated 2026-10-14 UTC. 



## Enable Model Armor for Gemini Notebook Enterprise

URL: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/enable-model-armor

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

This document describes how to enable Model Armor 

(/security-command-center/docs/model-armor-overview) for Gemini Notebook Enterprise. Model Armor is a Google Cloud service that enhances the security and safety of your AI applications by proactively screening the prompts and responses given using Gemini Notebook Enterprise. This helps protect against various risks and ensures responsible AI practices. Model Armor is supported on Gemini Notebook Enterprise at no additional cost. 

Model Armor does not remove or alter personally identifiable information (PII) or mask sensitive data. However, Gemini Notebook Enterprise blocks any response that triggers Sensitive Data Protection detectors. 

**Note:** Enabling Model Armor in Gemini Notebook Enterprise can increase latency. 

Model Armor's response to potential issues in user queries or responses from Gemini Notebook Enterprise is governed by the template's enforcement type. 

- If the enforcement type is _Inspect and block_ , Gemini Notebook Enterprise blocks the request and displays an error message. This is the default enforcement type when you create a Model Armor template using the console. 

- If the enforcement type is _Inspect only_ , Gemini Notebook Enterprise does not block the requests or responses. 

For more information, see Define the enforcement type 

(/security-command-center/docs/model-armor-overview#define-enforcement-type). 

### Before you begin

Make sure you have the required roles assigned to you and the service account: 

- To enable Model Armor in Gemini Notebook Enterprise, you need the Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) role. 

- To create the Model Armor templates, you need the Model Armor Admin (/iam/docs/roles-permissions/modelarmor#modelarmor.admin) role ( `roles/modelarmor.admin` ) . 

- To call the Model Armor APIs, you need the Model Armor User (/iam/docs/roles-permissions/modelarmor#modelarmor.user) role ( `roles/modelarmor.user` ). 

- If your Model Armor template is in a different project than your notebook in Gemini Notebook Enterprise, the template's project must grant the Model Armor User (/iam/docs/roles-permissions/modelarmor#modelarmor.user) role ( `roles/modelarmor.user` ) to the notebook's service account 

- (/iam/docs/service-agents#discovery-engine-service-account). The service account ID is `service-` _`PROJECT_NUMBER`_ `@gcp-sa-discoveryengine.iam.gserviceaccount.com` , where _`PROJECT_NUMBER`_ is the project number of your Gemini Notebook Enterprise instance. 

### Create a Model Armor template

You can create and use the same Model Armor template for user prompts and responses from the assistant, or you can create two separate Model Armor templates. For more information, see Create and manage Model Armor templates (/security-command-center/docs/manage-model-armor-templates). 

When creating a Model Armor template for Gemini Notebook Enterprise, consider these configurations: 

- You can create Model Armor templates centrally in one project and reuse them across different projects. If you use a cross-project template, ensure that the cross-project permissions are configured as described in Before you begin (#before-you-begin). 

- Select **Multi-region** in the **Regions** field. The following table shows you how to map Model Armor template regions to Gemini Notebook Enterprise regions: 

**Note:** After a Model Armor template and Gemini Notebook Enterprise is created, the regions can't be changed. 

|Gemini Notebook Enterprise multi-region|Model Armor multi-region|
|---|---|
|Global|US (multiple regions in United States)|
||EU (multiple regions in the Europe Union)|
|US (multiple regions in United States)|US (multiple regions in United States)|
|EU (multiple regions in the Europe Union)|EU (multiple regions in the Europe Union)|

- Google does not recommend configuring Cloud Logging in the Model Armor template for Gemini Notebook Enterprise. This configuration can expose sensitive data to users with the Private Logs Viewer 

- ( `roles/logging.privateLogViewer` ) IAM role. Instead, consider the following options: 

   - If you need to log the data that goes through the Model Armor template, you can reroute logs to a secure storage like BigQuery, which offers stricter access controls. For more information, see Route logs to supported destinations (/logging/docs/export/configure_export_v2). 

   - You can configure Data Access audit logs to analyze and report on the request and response screening verdicts generated by Model Armor. For more information, see Configure audit logs (#configure_audit_logs). 

### Configure Gemini Notebook Enterprise with the Model Armor templates

The following steps describe how to add the Model Armor templates to Gemini Notebook Enterprise. 

REST 

(#rest) 

To add the Model Armor templates to Gemini Notebook Enterprise, run the following command : 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_NUMBER?
update_mask=customerProvidedConfig" \
-d '{
 "customerProvidedConfig": {
   "notebooklmConfig": {
     "modelArmorConfig": {
       "userPromptTemplate": "QUERY_PROMPT_TEMPLATE",
       "responseTemplate": "RESPONSE_PROMPT_TEMPLATE"
     }
   }
 }
}'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`PROJECT_NUMBER`_ : the number of your Google Cloud project. 

- _`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

   - `us` for the US multi-region 

`eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

_`QUERY_PROMPT_TEMPLATE`_ : the **Resource name** of the Model Armor templates you created. 

To get the **Resource name** , follow the steps in the View a Model Armor template 

(/security-command-center/docs/manage-model-armor-templates#view-matemplate) 

documentation, and copy the **Resource name** value. 

**Note:** You can use Model Armor templates created in the same project as the notebook in Gemini Notebook Enterprise or use Model Armor templates from a different project. If you use a template from a different project, ensure the crossproject permissions are configured as described in Before you begin (#before-you-begin). 

_`RESPONSE_PROMPT_TEMPLATE`_ : the **Resource name** of the Model Armor templates you created. You can use Model Armor templates created in the same project or from a different project. 

<sup>Example command and result</sup> 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: my-project-123" \
"https://discoveryengine.googleapis.com/v1/projects/123456?
update_mask=customerProvidedConfig" \
-d '{
 "customerProvidedConfig": {
   "notebooklmConfig": {
     "modelArmorConfig": {
       "userPromptTemplate": "projects/my-project-
123/locations/us/templates/model-armor-template",
       "responseTemplate": "projects/my-project-
123/locations/us/templates/model-armor-template"
     }
   }
 }
}'
{
 "name": "projects/123456",
 "createTime": "2025-04-18T19:38:23.299346527Z",
 "provisionCompletionTime": "2025-04-18T19:38:23.299346527Z",
 "customerProvidedConfig": {
   "notebooklmConfig": {
     "modelArmorConfig": {
       "userPromptTemplate": "projects/my-project-
123/locations/us/templates/model-armor-template",
       "responseTemplate": "projects/my-project-
123/locations/us/templates/model-armor-template"
     }
   }
 }
}
```

**Note:** The Model Armor templates takes 10 minutes or more to take effect. 

### Test if the Model Armor template is enabled

After configuring the Model Armor template, test if Gemini Notebook Enterprise proactively screens and blocks user prompts and responses according to the confidence levels set in the Model Armor filters. 

When the Model Armor template is configured to **Inspect and block** requests that violate the policy, the following policy violation message is shown: 

ConsoleREST (#rest) (#console) 

For example, you see the policy violation message: 

_Model Armor policy violation message_ 

### Remove the Model Armor templates from Gemini Notebook Enterprise

To remove the Model Armor templates from Gemini Notebook Enterprise, run the following command: 

REST (#rest) `curl -X PATCH \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json" \ -H "X-Goog-User-Project:` _`PROJECT_ID`_ `" \ - "https://` _`ENDPOINT_LOCATION`_ `discoveryengine.googleapis.com/v1alpha/projects/` _`PROJECT_NUMBER`_ `? update_mask=customerProvidedConfig" \ -d '{ "customerProvidedConfig": { "notebooklmConfig": { "modelArmorConfig": {} } } }'` 

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`PROJECT_NUMBER`_ : the number of your Google Cloud project. 

- _`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

- `eu` for the EU multi-region 

`global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store). 

<sup>Example command and result</sup> 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: my-project-123" \
"https://discoveryengine.googleapis.com/v1/projects/123456?
update_mask=customerProvidedConfig" \
-d '{
 "customerProvidedConfig": {
   "notebooklmConfig": {
   }
 }
}'
{
 "name": "projects/123456",
 "createTime": "2025-04-18T19:38:23.299346527Z",
 "provisionCompletionTime": "2025-04-18T19:38:23.299346527Z",
 "customerProvidedConfig": {
   "notebooklmConfig": {}
 }
}
```

### Considerations when using Model Armor

When using Model Armor with Gemini Notebook Enterprise, consider the following: 

|De-identification<br>and masking|When Model Armor uses a Sensitive Data Protection template for scanning<br>prompts or responses, Model Armor checks if the content matches the<br>detector criteria defined in the template. Although Sensitive Data Protection<br>supports de-identification based on the template configuration, Model<br>Armor does not pass de-identified or masked data back to Gemini Notebook<br>Enterprise. If the content triggers any detectors from Sensitive Data<br>Protection and the enforcement type is`INSPECT_AND_BLOCK`, Gemini<br>Notebook Enterprise blocks the request or response rather than de-<br>identifying it.|
|---|---|
|Token limits and<br>quotas|Although there are no direct token limits when you use Model Armor with<br>Gemini Notebook Enterprise, the total throughput of your Model Armor<br>evaluations is still indirectly governed by<br>Gemini Enterprise system quotas<br>(/gemini/enterprise/docs/quotas-and-overages) and<br>Model Armor API rate<br>limits(/model-armor/quotas#quotas).|
|Service Level<br>Agreement|Gemini Notebook Enterprise provides a<br>Service Level Agreement<br>(https://cloud.google.com/terms/gemini/enterprise/sla). When Gemini<br>Notebook Enterprise is configured to use Model Armor, blocked queries<br>don't count as SLA violations, regardless of whether the fail-open or fail-<br>closed mode is used.|
|Compliance|Both Gemini Notebook Enterprise and Model Armor offer various compliance<br>certifications. When used together, the effective compliance certifications<br>are the common subset of both products. Review the compliance<br>certifications for both products to ensure that they meet your regulatory<br>requirements.|
|Document<br>screening|If a Model Armor template is configured to screen user prompts or<br>responses, document text extracted from sources is screened when sent in<br>requests. However, images embedded within documents are not screened.<br>For the list of supported document types, see<br>Document screening<br>(/security-command-center/docs/model-armor-overview#ma-support-<br>screening-pdfs)<br>.|

### Configure audit logs

Model Armor records Data Access audit logs (/logging/docs/audit#data-access) that you can use to analyze the request and response screening verdicts. These logs don't contain the user queries or responses from Gemini Notebook Enterprise, so they are safe for reporting and analytics. For more information, see Audit logging for Model Armor (/security-command-center/docs/audit-logging-model-armor). 

To access these logs, you need to have the Private Logs Viewer 

(/iam/docs/roles-permissions/logging#logging.privateLogViewer) ( `roles/logging.privateLogViewer` ) IAM role. 

#### Enable Data Access audit logs

To enable the Data Access audit logs, follow these steps: 

1. In the Google Cloud console, go to **IAM & Admin** > **Audit Logs** . 

2. Select the **Model Armor API** . 

3. In the **Permission type** section, select the **Data read** permission type. 

4. Click **Save** . 

#### Examine Data Access audit logs

To examine the Data Access audit logs, follow these steps: 

1. In the Google Cloud console, go to **Logs Explorer** . 

2. Search the logs for the following method names: 

   - `google.cloud.modelarmor.v1.ModelArmor.SanitizeUserPrompt` to view the user requests that were screened. 

   - `google.cloud.modelarmor.v1.ModelArmor.SanitizeModelResponse` to view the responses that were screened.
