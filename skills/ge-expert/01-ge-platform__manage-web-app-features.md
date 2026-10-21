# Gemini Enterprise: platform, security, agents, cost, monitoring / Manage web app features to Configure the Gemini Enterprise app for Slack
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 654-694, extracted 2026-10-18

Contains:
- Manage web app features (pages 654-664) https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features
- Configure Canvas (pages 665-667) https://docs.cloud.google.com/gemini/enterprise/docs/configure-canvas
- Manage observability settings (pages 668-672) https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings
- Manage skills (pages 673-679) https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills
- Configure prompt chips (pages 680-683) https://docs.cloud.google.com/gemini/enterprise/docs/configure-prompt-chips
- Configure Chrome Enterprise cloud-managed browsers (pages 684-690) https://docs.cloud.google.com/gemini/enterprise/docs/configure-chrome
- Configure the Gemini Enterprise app for Slack (pages 691-694) https://docs.cloud.google.com/gemini/enterprise/docs/configure-slack-app

## Manage web app features

URL: https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features

This document describes how to configure the feature management settings for your Gemini Enterprise web app using the Google Cloud console. You can control the features that are available for your end users. 

### Before you begin

Make sure you have the following: 

- The Gemini Enterprise Admin 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role ( `roles/discoveryengine.agentspaceAdmin` ). 

- An existing Gemini Enterprise web app. For information about creating a new app, see Create an app (/gemini/enterprise/docs/create-app). 

### Configure feature controls

To configure the features available in your web app, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** and then click the **Feature Management** tab. 

4. You can turn on or turn off the following features in the web app: 

|Feature control|Description|
|---|---|
|Enable Agent Gallery|When enabled, the web app shows the Agent Gallery. For<br>more information, see<br>Browse agents with Agent Gallery|
||(/gemini/enterprise/docs/agent-gallery).|

|Feature control|Description|
|---|---|
|Enable chat agents|When enabled, users can build and use custom chat agents.<br>For more information, see<br>Chat agent overview<br>(/gemini/enterprise/docs/workflow-builder/chat-agents).|
|Enable workflows|When enabled, users can create and run custom workflows.<br>For more information, see<br>Workflows overview<br>(/gemini/enterprise/docs/workflow-builder/workflows).|
|Enable model selector|When enabled, users can select the Gemini or partner model<br>that they want to use in the web app.|
|Enable Gemini Notebook|When enabled, users can use Gemini Notebook Enterprise in<br>the web app. For more information, see<br>Use Gemini Notebook<br>Enterprise within Gemini Enterprise<br>(/gemini/enterprise/docs/access-notebooklm).|
|Enable session sharing|When enabled, users can share Gemini Enterprise<br>conversations with other users.|
|Enable memory and<br>customization|When enabled, Gemini Enterprise uses past conversations and<br>saved memory settings to generate personalized and relevant<br>responses.|
|Enable Canvas|When enabled, users can create, edit, and export files in an<br>interactive editor next to their chat conversation. For more<br>information, see<br>Create and edit documents and slides in<br>Canvas(/gemini/enterprise/docs/assistant-canvas).|
|Enable projects|When enabled, users can create and use collaborative projects<br>in the web app. For more information, see<br>Create and manage<br>projects(/gemini/enterprise/docs/projects).|

|Feature control|Description|
|---|---|
|Enable image generation|When enabled, users can generate images in the web app. You<br>can also choose the image model you want your users to use.<br>Available models include:<br>Gemini 3 Pro image (Nano Banana Pro): This model is<br>generally available (GA) and is turned off by default. It is<br>only available in the Global region.|
||A warning is displayed if an end user attempts to use the<br>Gemini 3 Pro image model in a region other than Global.<br>The user can accept the terms and proceed.|
||Gemini 3.1 Flash image (Nano Banana 2): This model is<br>generally available (GA) and is turned off by default. If an<br>administrator turned on this model during the Public<br>Preview, it remains turned on in GA too.<br>Gemini 2.5 Flash image: The system defaults to this model<br>if you don't make any selection.|
|Enable video generation|When enabled, users can generate videos in the web app.|
|Enable OneDrive upload|When enabled, users can upload files to the assistant from<br>Microsoft OneDrive as a data source.|
|Enable talk to content|When enabled, users can navigate to the Sources referenced<br>in an answer, add documents to the conversation by clicking<br>the icon next to a source, and then ask questions about the<br>content of the documents.|
|Enable speech-to-text|When enabled, users can dictate their prompts into the web<br>app, using the icon in the chat box. For more information, see<br>Use your voice to chat<br>(/gemini/enterprise/docs/assistant-chat#voice-chat).|
|Enable Google Drive<br>upload|When enabled, users can upload files to the assistant from<br>Google Drive as a data source.|

|Feature control|Description|
|---|---|
|Include cross-domain<br>documents|You can enable the Include cross-domain documents feature<br>for an existing app, even if you didn't enable it during app<br>creation. When enabled, users can search and access<br>documents from outside your organization using the<br>Google<br>Drive data store<br>(/gemini/enterprise/docs/connectors/gdrive/set-up-data-store)<br>.|
||Enabling this feature increases exposure to security risks,<br>such as prompt injection from external documents and<br>potential manipulation of search results.|
|Enable welcome emails|When enabled, users receive a welcome email the first time<br>they sign in to the web app.|
|Enable skills|When enabled, users can create and use skills in the web app.<br>For more information, see<br>Create and manage skills<br>(/gemini/enterprise/docs/skills).|
|Enable skill sharing|When enabled, users can share custom skills with other users<br>using the Gemini Enterprise app. To enable this, you must turn<br>on Enable skills. If you don't also turn on the Enable skill<br>sharing without admin approval setting, administrators must<br>review and approve pending skill share requests. For more<br>information, see<br>Create and manage skills<br>(/gemini/enterprise/docs/skills).|
|Enable skill sharing<br>without admin approval|When enabled, users on your team can share and use custom<br>skills without administrator approval when using the Gemini<br>Enterprise app. To enable this setting, you must turn on<br>Enable skills and Enable skill sharing.|
||Review and approve pending sharing requests before<br>turning on this feature to prevent users from having to<br>resubmit the sharing requests.|
||For more information, see<br>Create and manage skills<br>(/gemini/enterprise/docs/skills).|

|Feature control|Description|
|---|---|
|Enable agent sharing|When enabled, users can share agents created using Workflow<br>Builder with other users using the Gemini Enterprise app. For<br>more information, see<br>Share an agent<br>(/gemini/enterprise/docs/workflow-builder/share-chat-agent).<br>If you use Okta or Microsoft Entra ID as a third-party identity<br>provider with Workforce Identity Federation,<br>configure SCIM<br>(/gemini/enterprise/docs/configure-identity-<br>provider#configure_workforce_id_federation)<br>to enable autocomplete of email addresses (and group names)<br>when users share agents.|
|Enable agent sharing<br>without admin approval|When enabled, users on your team can share and use agents<br>created using Workflow Builder without administrator approval<br>when using the Gemini Enterprise app.<br>Note: Review and approve pending sharing requests before<br>turning on this feature to prevent users from having to<br>resubmit the sharing requests.<br>For more information, see<br>Share an agent<br>(/gemini/enterprise/docs/workflow-builder/share-chat-agent).|
|Enable End Users to share<br>with Groups|When enabled, users can share custom agents with groups in<br>the organization. Whether the administrator must approve<br>sharing depends on the Enable agent sharing without admin<br>approval setting. For more information, see<br>Share an agent<br>(/gemini/enterprise/docs/workflow-builder/share-chat-agent).<br>If you use Okta or Microsoft Entra ID as a third-party identity<br>provider with Workforce Identity Federation,<br>configure SCIM<br>(/gemini/enterprise/docs/configure-identity-<br>provider#configure_workforce_id_federation)<br>to enable autocomplete of group names (and email addresses)<br>when users share agents.|

- Feature control Description Model availability You can select the models that users can use in the web app. To enable model selection, you must turn on the Enable model selector toggle. The following Gemini and partner models are available: Gemini models: Gemini 4 Argon, Gemini 3.8 Flash, Gemini 3.7 Flash, Gemini 3.6 Flash, Gemini 3.5 Flash, Gemini 3.1 Pro, and Gemini 2.5 Pro. For more information, see Enable Gemini models (#enable-gemini-models). Partner models: Anthropic models—Claude Opus 5.5 and Claude Sonnet 5.5. For more information, see Enable third- party models (#enable-third-party-models). 

### Enable Gemini models

You can control which Gemini models users can select in the Gemini Enterprise web app. To let users choose a model in the web app, make sure that the **Enable model selector** toggle is turned on in the **Feature Management** tab. 

#### Available Gemini models

The following Gemini models are available in the web app: 

|Model|Default state|Supported locations and notes|
|---|---|---|
|Gemini 4 Argon|Turned off in`global`,`us`,<br>and`eu`(defaults to on<br>beginning October 27,<br>2026)|To make Gemini 4 Argon available to users, click<br>the Gemini 4 Argon toggle to the on position. For<br>unsupported in-country regions, confirm the<br>warning dialog to route traffic to the`global`<br>endpoint. For more information, see<br>Data<br>residency for Gemini Enterprise<br>(/gemini/enterprise/docs/locations).|

|Model|Default state|Supported locations and notes|
|---|---|---|
|Gemini 3.8 Flash|Turned on in`global`,`us`,<br>and`eu`, and in`sg`and<br>`europe-west2`|If you don't want users to use Gemini 3.8 Flash,<br>click the Gemini 3.8 Flash toggle to the off<br>position. For unsupported in-country regions,<br>click the Gemini 3.8 Flash toggle to the on<br>position and confirm the warning dialog to route<br>traffic to the`global`endpoint.|
|Gemini 3.7 Flash|Turned off|To let users use Gemini 3.7 Flash, click the<br>Gemini 3.7 Flash toggle to the on position. For<br>unsupported in-country regions, you must also<br>confirm a warning dialog to route traffic to the<br>`global`endpoint.|
|Gemini 3.6 Flash|Turned off|To let users use Gemini 3.6 Flash, click the<br>Gemini 3.6 Flash toggle to the on position. For<br>unsupported in-country regions, you must also<br>confirm a warning dialog to route traffic to the<br>`global`endpoint.|
|Gemini 3.5 Flash|Turned on|For some models in General Availability (GA) in<br>the Gemini Enterprise app, such as Gemini 3.5<br>Flash, you can't turn the toggle off.|
|Gemini 3.1 Pro|Turned off|Available in Limited Availability if supported in<br>your region. To let users use Gemini 3.1 Pro, click<br>the Gemini 3.1 Pro toggle to the on position. For<br>more information about known limitations, see<br>Using Gemini 3.1 Pro in Limited Availability<br>(/gemini/enterprise/docs/known-<br>limitations#using-gemini-3-preview)<br>.|
|Gemini 2.5 Pro|Turned on in`global`,`us`,<br>and`eu`|If you don't want users to use Gemini 2.5 Pro,<br>click the Gemini 2.5 Pro toggle to the off position.<br>Gemini 2.5 Pro is deprecated in the`ca`and`asia-`<br>`northeast1`regions and isn't available in those<br>regions after October 20, 2026. For more<br>information, see<br>Data residency for Gemini<br>Enterprise(/gemini/enterprise/docs/locations).|

#### Turn on or turn off a Gemini model

To turn on or turn off a Gemini model in the web app, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** and then click the **Feature Management** tab. 

4. Go to the **Gemini model availability** section. 

5. Click the toggle for the Gemini model that you want to turn on or turn off. 

   - If you turn on a model in an unsupported in-country region, confirm the warning dialog to route traffic to the `global` endpoint. 

6. Click **Save** . 

The changes take effect after a few minutes. 

### Enable third-party models

In addition to Gemini models, you can let users chat with third-party models, such as Anthropic models—Claude Opus 5.5 and Claude Sonnet 5.5—in the Gemini Enterprise web app. You pay for third-party model usage per token, on a pay-asyou-go basis. 

#### Available third-party models

The following third-party models are available in the web app: 

|Model|Publisher<sup>Supported</sup><br>locations|
|---|---|
|Claude Opus 5.5|Anthropic`global`,`us`, and|
|(/gemini-enterprise-agent-platform/models/partner-<br>models/claude/opus-5-5)|`eu`|

Model Publisher<sup>Supported</sup> locations Claude Sonnet 5.5 Anthropic `global` , `us` , and (/gemini-enterprise-agent-platform/models/partner- `eu` models/claude/sonnet-5-5) 

Anthropic models—Claude Opus 5.5 and Claude Sonnet 5.5—are turned off by default in the `global` , `us` , and `eu` regions. To make them available to end users, turn them on by enabling billing and accepting the terms of service. For more information about regional support, see Data residency for Gemini Enterprise (/gemini/enterprise/docs/locations). 

Third-party models aren't available in the Gemini Enterprise Starter edition. They also aren't available for in-country regions. 

#### Before you begin

Before you turn on a third-party model, make sure that the following requirements are met: 

- You have the Gemini Enterprise Admin 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role ( `roles/discoveryengine.agentspaceAdmin` ). 

- If you have a subscription, **Pay-as-you-go usage above quota** is turned on for your project. You must turn it on separately for each edition, such as Gemini Enterprise Standard and Gemini Enterprise Plus. For more information, see Configure overages (/gemini/enterprise/docs/configure-overages). 

- The **Enable model selector** toggle is turned on in the **Feature Management** tab, so that users can select the model in the web app. 

We recommend that you set a monthly spend limit 

(/gemini/enterprise/docs/configure-overages#set-spend-limit) and budgets in Cloud Billing (/billing/docs/how-to/budgets) to control costs. For pricing information, see Claude pricing (/gemini/enterprise/docs/quotas-and-overages#claude-pricing). 

**Note:** If you have negotiated pricing or a custom contract, the prices might differ from the 

published prices. Refer to your agreement for exact pricing. 

#### Turn on a third-party model

To make a third-party model available to users in the web app, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** and then click the **Feature Management** tab. 

4. Go to the **Enable third-party models** section. 

5. In the section for the publisher, click the toggle for the model that you want to turn on. 

The **_Model_ pricing** dialog appears. The dialog describes how the model is charged and checks whether **Pay-as-you-go usage above quota** is turned on for your project. 

6. In the **_Model_ pricing** dialog, do one of the following: 

   - If pay-as-you-go usage is available for your project, click **Enable** . 

   - If **Pay-as-you-go usage above quota** isn't turned on, click **Go to Usage & spend** to turn it on, and then return to this procedure. The model toggle is turned off. 

   - If your project's billing account isn't eligible for **Pay-as-you-go usage above quota** , you can't turn on the model. Click **Cancel** and contact your billing administrator. 

7. If the **Terms of service** dialog appears, read the terms for the model. Go to the end of the terms, and then click **Agree** . 

You accept the terms of service once for each project and model family. For example, after you accept the terms for Claude Opus 5.5 in a project, the **Terms of service** dialog doesn't appear again when you turn on that model in other apps in the same project. 

If you click **Cancel** , the model toggle is turned off. 

8. Click **Save** . 

9. In the **Important billing info** dialog, review the billing information, and then click **I understand** . 

**Note:** When you enable a Claude model for the first time, allow up to 15 minutes for the change to take effect. After the model is available, users can select it from the **Model** selector. 

#### Turn off a third-party model

To stop users from using a third-party model, follow these steps: 

1. In the **Feature Management** tab, go to the **Enable third-party models** section. 

2. Click the toggle for the model to the off position. 

3. Click **Save** . 

The model is removed from the model selector in the web app after a few minutes. 

Last updated 2026-10-15 UTC. 



## Configure Canvas

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-canvas

This page describes how administrators can set up and configure Canvas in Gemini Enterprise for their users. 

Canvas is generally available in the global, US, and EU regions. It is available for users of Gemini Enterprise Business edition, Standard and Plus editions. 

### Before you begin

Canvas is disabled by default. You can review and test Canvas before you choose to enable it for users. 

To enable Canvas for your users, complete the following setup: 

- Turn on the feature toggle (#turn-on-canvas) 

- Add Canvas permissions to a custom IAM role (#add-canvas-permissions) 

#### Turn on Canvas on the Gemini Enterprise app

For users to access the Canvas feature, a Gemini Enterprise administrator must turn on the **Enable canvas** toggle in the web app feature management settings. For more information, see Manage web app features 

(/gemini/enterprise/docs/manage-web-app-features). 

#### Add Canvas permissions to a custom IAM role

Ensure users have the required permissions for Canvas: 

- **Predefined roles** : Users accessing Gemini Enterprise with standard roles like `roles/discoveryengine.user` don't need to make any changes, as the necessary permissions are included in the predefined roles. 

- **Custom roles** : For users accessing Gemini Enterprise using custom IAM roles, you must add the `immersiveArtifacts` permissions to the custom role. Without 

these permissions, users can't use Canvas. Canvas requires the following permissions: 

- `discoveryengine.immersiveArtifacts.create` 

- `discoveryengine.immersiveArtifacts.delete` 

- `discoveryengine.immersiveArtifacts.export` 

- `discoveryengine.immersiveArtifacts.get` 

- `discoveryengine.immersiveArtifacts.list` 

- `discoveryengine.immersiveArtifacts.navigate` 

```
discoveryengine.immersiveArtifacts.update
```

Because the permissions required for Canvas are in preview, you can't add them using the Google Cloud console. Instead, use the gcloud CLI. For example, to add these permissions to an existing project-level custom role, run the following command: 

```
gcloud iam roles update ROLE_ID \
 --project=PROJECT_ID \
 --add-
permissions=discoveryengine.immersiveArtifacts.create,discoveryengine.imme
rsiveArtifacts.delete,discoveryengine.immersiveArtifacts.export,discoverye
ngine.immersiveArtifacts.get,discoveryengine.immersiveArtifacts.list,disco
veryengine.immersiveArtifacts.navigate,discoveryengine.immersiveArtifacts.
update
```

**Note:** Because these permissions are in preview, you see an expected warning from gcloud CLI stating that these permissions are in the **`alpha`** launch stage and might be unstable for use in custom roles. This warning is expected and doesn't prevent the permissions from being applied. 

For more information about managing Gemini Enterprise IAM roles, see Access control with IAM (/gemini/enterprise/docs/access-control). 

### Limitations

Canvas isn't supported on the mobile app. It is only available on the web app. 

### Quota consumption

Canvas queries and regular Gemini Enterprise app chat queries are counted in the same way and share the same quota. 

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

- Your project reached its monthly spend cap. 

- Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 

This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

Last updated 2026-10-14 UTC. 



## Manage observability settings

URL: https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings

This document describes how to configure the observability settings for your Gemini Enterprise app or individual agents using the Google Cloud console or the REST API. 

The enablement logic depends on the agent type: 

- **Core Assistant agent** : Use the application-level (engine-level) toggle in configurations. 

- **Other agents** : (Limited to Workflow Builder employee-made agents and Deep Research agents at this time): Use the agent-level toggle inside the individual agent's settings. 

After you enable the settings, you can view the following data from your interactions with the assistant or agents in your Gemini Enterprise web app: 

- View metrics in Metrics Explorer. View traces and spans in Trace Explorer. 

### Key concepts

This section introduces key concepts related to observability in Gemini Enterprise. 

|Concept|Description|
|---|---|
||A trace is a collection of spans that represents a single request or<br>transaction as it flows through different services and components.|
|Trace|For example, a trace represents the entire lifecycle of a request. This<br>includes a user asking a question from the Gemini Enterprise assistant, the<br>Gemini Enterprise assistant responding, and any subsequent actions<br>triggered by the answer, such as sending an email.|

|Concept|Description|
|---|---|
|Span|A span is a single, timed unit of work within a trace. It represents a specific<br>operation, such as a function call, an API request, or a database query. Each<br>span includes details like its start and end times, a unique ID, and its<br>relationship to other spans. These relationships together form a trace.|
|Span logs|Span logs are timestamped, free-form messages or events associated with<br>a specific span. They provide detailed, contextual information about a<br>span's execution, helping users debug issues and understand the flow of a<br>request.|
|Metrics|Metrics are numerical measurements that systems collect over time. These<br>measurements represent the performance, resource utilization, or behavior<br>of a system. Engineers use metrics to monitor system health, identify<br>trends, and trigger alerts.|
|Usage audit logs|Usage audit logs are records of administrative activities and accesses within<br>your Google Cloud resources. They provide detailed information about who<br>performed what action, when, and from where. These logs are essential for<br>security auditing, compliance, and understanding how your resources are<br>being used.|
|Gemini Enterprise<br>connector error<br>logs|Gemini Enterprise connector error logs capture errors and failures<br>encountered when integrating Gemini Enterprise with third-party data<br>sources like Jira and Microsoft OneDrive. These logs include connection<br>problems, data transformation issues, and API errors.|

### Before you begin

Make sure you have the following: 

- The Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

- An existing Gemini Enterprise web app. For information about creating a new app, see Create an app (/gemini/enterprise/docs/create-app). 

### Turn on observability settings

To turn on observability for your Gemini Enterprise app or individual agents, you can use either the Google Cloud console or the REST API. 

ConsoleREST (#rest) (#console) 

To turn on the observability settings using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Depending on the agent type you are configuring, do one of the following: 

**Core Assistant agent** : Click **Configurations** , and then click the **Observability** tab. 

**Other agents (Workflow Builder employee-made agents and Deep Research agents)** : Click **Agents** , click the name of the agent you want to configure, and then click the **Configuration** tab. 

4. You can turn on or turn off the following settings: 

|Observability setting|Description|
|---|---|
|Enable instrumentation of<br>OpenTelemetry traces and logs|When enabled, you can view traces, spans, span<br>logs, and metrics associated with your logs in<br>Cloud Logging.|

|Observability setting|Description|
|---|---|
|Enable logging of prompt inputs<br>and response outputs|When enabled, Cloud Logging logs the full<br>content of user prompts and responses. This<br>includes sensitive data or Personally Identifiable<br>Information (PII). To enable this setting, you must<br>first enable Enable instrumentation of<br>OpenTelemetry traces and logs.|
||Caution: Enabling this setting logs potentially<br>sensitive data, including PII. Restrict log access<br>to authorized personnel only.|

### Turn off observability settings

To turn off the observability settings for your Gemini Enterprise app or individual agents, use either the Google Cloud console or the REST API. 

ConsoleREST (#rest) (#console) 

To turn off the observability settings using the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app for which you want to turn off the observability settings. 

3. Depending on the agent type you are configuring, do one of the following: 

**Core Assistant agent** : Click **Configurations** , and then click the **Observability** tab. 

**Other agents (including Workflow Builder employee-made agents and Deep Research agents)** : Click **Agents** , click the 

name of the agent you want to configure, and then click the **Configuration** tab. 

4. You can turn off the following settings: 

|Observability setting|Description|
|---|---|
|Enable instrumentation of<br>OpenTelemetry traces and logs|When turned off, this setting stops the collection<br>of traces, spans, span logs, and metrics. It also<br>turns off the Enable logging of prompt inputs and<br>response outputs setting, which means no logs<br>are sent to Cloud Logging.|
|Enable logging of prompt inputs<br>and response outputs|When turned off, Cloud Logging does not log<br>prompt inputs and response outputs.|

### What's next

- To learn more about how to access the Gemini Enterprise logs, see Access usage audit logs (/gemini/enterprise/docs/set-up-usage-audit-logs). 

- To learn more about how to access the Gemini Enterprise trace and span data, see Access traces and spans in Trace Explorer (/gemini/enterprise/docs/access-traces-and-spans). 

- To learn more about how to access the Gemini Enterprise metrics, see Access metrics in Metrics Explorer (/gemini/enterprise/docs/access-metrics). 

Last updated 2026-10-14 UTC. 



## Manage skills

URL: https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills

User-created skills are reusable instructions that help the Gemini Enterprise assistant perform specific tasks. 

By default, Gemini Enterprise turns off the skills feature. As a Gemini Enterprise administrator, you can turn on skills, manage skill sharing, and require administrator approval for shared skills. 

**Note:** Skills don't have specific location restrictions. Their availability depends on the model selected in the chat conversation. For more information, see Gemini Enterprise limitations (/gemini/enterprise/docs/locations#product-limitations). 

### Supported editions

Whether users can create, upload, or use skills depends on their Gemini Enterprise edition (/gemini/enterprise/docs/editions): 

- **Standard, Plus, and Pay-as-you-go** : Users can create and upload custom skills, and use Google-managed skills and user-created skills shared with them. 

- **Frontline** : Users can browse, install, and use Google-managed skills and usercreated skills shared with them. They can't create or upload custom skills. 

### Before you begin

- To perform administrative tasks related to skills, you must have the Gemini Enterprise Admin 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role ( `roles/discoveryengine.agentspaceAdmin` ). 

### Turn on skills and configure sharing

To allow users to create, use, and share skills, you must turn on the feature in the **Feature Management** settings. 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** and then click the **Feature Management** tab. 

4. Turn on the following toggles based on your use case: 

|Toggle|Description|
|---|---|
|Enable skills|Allow users to create and use skills. Users with a Frontline license can<br>use Google-managed skills and user-created skills shared with them,<br>but can't create or upload skills.|
|Enable skill<br>sharing|Allow users to share skills with other users. To enable this setting, you<br>must turn on Enable skills. If you don't also turn on the Enable skill<br>sharing without admin approval, administrators must review and<br>approve pending skill share requests.|
|Enable skill<br>sharing without<br>admin approval|Allow users to share and use skills immediately without requiring<br>administrator review. To enable this setting, you must turn on Enable<br>skills and Enable skill sharing.|

For more information about feature management, see Manage web app features (/gemini/enterprise/docs/manage-web-app-features). 

### View skills

To view the skills created by users, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that has the skill. 

3. Click **Skills** . The **Skills** page appears, listing all skills created by users. 

### Review share requests

If you have configured skill sharing to require administrator approval, you can review pending share requests on the **Skills** page. Follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that has the skill. 

3. Click **Skills** . 

4. On the **Skills** page, look for skills with a pending sharing status. 

5. Click **Review share request** . 

6. Select the users you want to share the skill with. 

7. Click **Approve** to allow the skill to be shared, or **Deny** to deny the request. 

### Suspend a skill

To temporarily suspend a skill created by a user and make it unavailable for use, follow these steps: 

**Note:** You can't use administrator controls to suspend Google-managed skills for all end users. But, end users can turn off Google-managed skills they installed if they don't want to use them. 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that has the skill. 

3. Click **Skills** . 

4. On the **Skills** page, click next to the skill you want to suspend. 

5. Enter the reason for suspending the skill. 

6. Click **Suspend** . 

The skill status changes to **Suspended** . The skill remains visible in the end-user skill gallery with a **Suspended** label next to its name, but users can no longer invoke it in conversations. The skill owner can update and test the skill. 

### Disable a skill

To hide a skill that is shared with users and prevent its use, follow these steps: 

**Note:** You can't use administrator controls to disable Google-managed skills for all users. End users can turn off Google-managed skills they installed if they don't want to use them. 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that has the skill. 

3. Click **Skills** . 

4. On the **Skills** page, click next to the skill you want to disable. 

5. Click **Disable** . 

Gemini Enterprise hides the skill from the end-user skill gallery. 

### Enable a skill

To re-enable a suspended or disabled skill, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that has the skill. 

3. Click **Skills** . 

4. On the **Skills** page, click next to the suspended or disabled skill. 

5. Click **Enable** . The skill becomes available for use. 

### Reject a skill

When you reject a skill that is in the **Disabled** state, Gemini Enterprise returns it to the **Private** state and makes it available only to the skill owner. You must enter a reason for the rejection. 

To reject a skill, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that has the skill. 

3. Click **Skills** . 

4. On the **Skills** page, click next to the disabled skill you want to reject. 

5. Click **Reject** . 

6. Enter a reason for the rejection. 

7. Click **Confirm** . 

### Delete a skill

To permanently delete a user-created skill, follow these steps: 

**Note:** You can't delete Google-managed skills. 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that has the skill. 

3. Click **Skills** . 

4. On the **Skills** page, click next to the skill you want to delete. 

5. Click **Delete** . 

### Skill states

The following table describes each state that a skill might be in: 

|State|Description|
|---|---|
|Private|The skill isn't shared with other users and is only available to the skill<br>owner.|
|Suspended|The skill is temporarily deactivated. The skill remains visible in the end-user<br>gallery with a Suspended label next to its name, but users can no longer<br>invoke it in conversations. Skill owners can update and test the skill.|
|Enabled|The skill is active and available for use on the web app.|
|Disabled|The skill is inactive and hidden completely from the end user's Skills page.<br>Users can't interact with the skill until you re-enable it. Skill owners can<br>update and test the skill.|

### What's next

- Learn how users create and manage skills (/gemini/enterprise/docs/skills). 

- Learn more about how to manage web app features (/gemini/enterprise/docs/manage-web-app-features). 

Last updated 2026-10-14 UTC. 



## Configure prompt chips

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-prompt-chips

This page shows you how to configure your prompt chips for your web app using the Google Cloud console. 

### Overview

A _prompt chip_ is a predefined category that's accessible from the Gemini Enterprise web app. When you click a prompt chip, suggested prompts display that you can immediately send to the model. 

### Before you begin

You must have an existing Gemini Enterprise web app. To create a new app, see Create an app (/gemini/enterprise/docs/create-app). 

### Configure your prompt chips

To configure your prompt chips, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to **Gemini Enterprise** (https://console.cloud.google.com/gemini-enterprise/products) 

2. Select your project. 

3. Select your app from the **Name** column. The navigation menu updates. 

4. Click **Prompt chips** . The **Prompt chips** page displays all of the prompts created by Google and by you. 

5. If you want all of the prompt chips to display on your **Gemini Enterprise** web app, then select the **Automatically enable new prompts from Google** checkbox. 

If you want to control which prompt chips display, then clear the checkbox. 

### Create a prompt chip

1. Click **+ New prompt** , and the **Create prompt** page displays. 

2. Enter a prompt-chip name in the **Name** field, which can't be changed after it's saved and must follow this format: 

      - The name's length must be from 1 to 63 characters long. 

      - The name only contains lowercase letters, numbers, or hyphens. 

      - The name must begin and end with a letter or a number. 

3. Enter the name for your prompt chip in the **Display name** field. This name appears in the **Display name** column of the **Prompt chips** table. 

4. Enter a title in the **Title** field for your prompt chip. When the prompt chip is clicked, all prompts defined for this title display. 

5. Enter a brief description that explains what the user should enter as a prompt on the **Gemini Enterprise** web app in the **Prefix** field. 

6. To provide prompts that your user can choose from for a specific title, enter the text in the **Suggested prompt** field. 

   - a. Click **+ Add suggested prompt** . 

   - b. To make the prompt chip available on the **Gemini Enterprise** web app, click the **Enabled** toggle. 

   - c. Optional: Continue to enter suggested prompts. 

7. Click **Create** . All of your prompts are stored in the **Our prompts** category. Delete unused suggested prompt fields. 

### Edit or delete a prompt chip

To edit a prompt chip, do the following: 

1. Click the pencil icon for the prompt chip that you want to change. An **Edit Prompt** pane displays. 

2. Change the field(s). You can't change the prompt chip name. 

3. Click **Update** . 

To delete a prompt chip, do the following: 

1. Click the trashcan icon, and a confirmation dialog displays. 

2. Click **Delete** . 

### Filter prompt chips

To find a prompt chip from a list of prompt chips, you can filter two different ways: 

- You can select a prompt chips category, which include the following: 

   - **All** : Displays both **Google-made** and **Our prompts** prompt chips. 

   - **Google-made** : Displays the prompt chips provided by Google. 

   - **Our prompts** : Displays the prompt chips that you create. 

- To find your prompt chip quickly, enter a few characters in the **Filter** field. 

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## Configure Chrome Enterprise cloud-managed browsers

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-chrome

Gemini Enterprise seamlessly integrates with Chrome Enterprise to deliver AIpowered custom content suggestions to the address bar of your users' cloudmanaged Chrome browsers. This page describes the steps to enable and configure cloud-managed Chrome browsers (https://support.google.com/chrome/a/answer/9116814) to show these suggestions in the Chrome address bar (omnibox (https://www.chromium.org/user-experience/omnibox/)). 

**Note:** To complete these steps, you need the necessary permissions to manage Chrome browsers for your organization. 

### Before you begin

#### Set up Gemini Enterprise

Before setting up the Gemini Enterprise x Chrome Enterprise integration, set up Gemini Enterprise. Learn more about how to get started with Gemini Enterprise (/gemini/enterprise/docs/quickstart-gemini-enterprise). 

#### Sign up for Chrome Enterprise Core

Chrome Enterprise Core lets you use the Google Admin console to set up the Gemini Enterprise Chrome policy. Learn more about how to set up Chrome Enterprise Core (https://support.google.com/chrome/a/answer/9116814). 

#### Enroll users and browsers

There are two options to manage Chrome browsers from the Google Admin console using Chrome Enterprise Core: Device-level browser enrollment and User profilelevel browser enrollment. Learn more about these options in _Cloud-managed Chrome browser_ (https://support.google.com/chrome/a/topic/9025410). 

**Note:** Changes may take up to 24 hours to apply for all cloud-managed browsers. 

1. Login to Google Workspace Admin Console (http://admin.google.com) using your credentials. 

2. Navigate to Menu > Chrome Browser > **Settings** to reveal the _User & browser settings_ view. 

3. Choose the specific **Group** or **Organizational Unit** from the respective list, or retain the default setting. Note: Learn more about applying settings to certain users of Google Chrome (https://support.google.com/a/answer/13815697). 

4. In the _Omnibox search provider_ category, select **Enterprise search aggregator.** 

5. Add a name, shortcut, search URL, and suggest URL, then select **Save** . 

|Properties||
|---|---|
|Name|The name that is shown to the user in their address bar.|
|Shortcut|The keyword that the user enters to trigger the search.<br>The shortcut can include plain words and characters, but<br>cannot include spaces or start with the @ symbol.<br>Shortcuts must be unique.|

|Properties||
|---|---|
|Search URL|The URL on which to search. Enter the web address for<br>the search engine's results page (for example, 1234),<br>and append the search terms inside a bracketed query<br>string.|
||Example copied value:<br>https://vertexaisearch.cloud.google.com/home/cid/123<br>4<br>Formatted value:<br>https://vertexaisearch.cloud.google.com/home/cid/123<br>4?q={searchTerms}|
||Note: To find the ID for your Gemini Enterprise<br>agent, navigate to your<br>Google Cloud Console's AI<br>Applications<br>(https://console.cloud.google.com/gen-app-<br>builder/start)<br>page, select the appropriate Gemini Enterprise<br>application, then select Integration > Web App.|

|Properties||
|---|---|
|Suggest URL|The URL that provides search suggestions.<br>Example copied value:<br>https://discoveryengine.googleapis.com/v1alpha/proje<br>cts/1234/locations/global/collections/default_collection<br>/engines/enterprisesearch/servingConfigs/default_sear<br>ch:search<br>Formatted value:<br>https://discoveryengine.googleapis.com/v1alpha/proje<br>cts/1234/locations/global/collections/default_collection<br>/engines/enterprisesearch/completionConfig:complete<br>Query|
||Note: To find the ID for your Gemini Enterprise agent,<br>navigate to your<br>Google Cloud Console's AI<br>Applications<br>(https://console.cloud.google.com/gen-app-<br>builder/start)<br>page, select the appropriate Gemini Enterprise<br>application, then select Integration > Web App.|
|Icon URL_(optional)_|Company branded icon that will be shown when user<br>types @ or starts the scoped search.<br>Recommended format: favicon<br>Supported file formats: JPEG, PNG, and ICO.|
|Require address bar shortcut to<br>see search recommendations|Specifies whether the address bar shortcut is required to<br>see search recommendations from this provider.|

### Enable autocomplete in your Gemini Enterprise project

To enable Autocomplete in your Gemini Enterprise project, go to your Google Cloud Console Gemini Enterprise page 

(https://console.cloud.google.com/gemini-enterprise/start), select your app, then select **Configurations > Autocomplete** . Autocomplete by default won't 

start making suggestions until it has sufficient quality data (typically a few days). To start generating autocomplete suggestions in Chrome sooner, select **Now** . 

Last updated 2026-10-14 UTC. 



## Configure the Gemini Enterprise app for Slack

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-slack-app

Gemini Enterprise can integrate with Slack to deliver AI-powered answers and search to your Slack users, directly in their Slack workspace. After you configure the Gemini Enterprise app for Slack, your users can send prompts to Gemini Enterprise and receive answers that incorporate data from all connected Gemini Enterprise data stores. 

**Note:** The Gemini Enterprise app for Slack is configured separately from the Slack data connector (/gemini/enterprise/docs/connectors/slack), which allows Gemini Enterprise to search data from a Slack workspace. 

### Supported regions

The Gemini Enterprise app for Slack is supported in the global, US, and EU multi-regions. 

### Limitations

The Gemini Enterprise app for Slack has the following limitations: 

- **Supports only Gemini Enterprise search.** Data store actions are not supported. 

- **Does not support Workforce Identity Federation.** An administrator must set up the Gemini Enterprise app for Slack using Google Identity. For more information, see Before you begin (#before-you-begin). 

- **Supports one-to-one workspace mapping:** You can link each Gemini Enterprise app to only one Slack workspace. For Slack Enterprise Grid, link each workspace to a separate Gemini Enterprise app. 

### Before you begin

Ensure that you have the following before configuring the Gemini Enterprise app for Slack: 

- Access to the Slack AI add-on. For information about Slack AI, see the Slack website (https://slack.com/features/ai). 

- A Gemini Enterprise app. If you haven't created an app yet, see Create an app (/gemini/enterprise/docs/create-app). 

- A configured Gemini Enterprise app that uses Google Identity as the identity provider. For information about setting up Google Identity, see Configure identity provider (/gemini/enterprise/docs/configure-identity-provider). 

- Configured data stores for any services that you want users to be able to search. For information about connecting Google and third-party data sources with Gemini Enterprise, see Introduction to connectors and data stores (/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores). 

- The Project IAM Admin (/resource-manager/docs/access-control-proj#resourcemanager.projectIamAdmin) role ( `roles/resourcemanager.projectIamAdmin` ) for your Google Cloud project. 

- Google Cloud OAuth 2.0 credentials for your Slack instance. To get the credentials, do the following: 

1. In the Google Cloud console, navigate to **APIs & Services > Credentials** . 

Go to Credentials (https://console.cloud.google.com/apis/credentials) 

2. Click **Create credentials** , then select **OAuth client ID** . 

3. In the **Application type** drop-down, select **Web application** . 

4. For **Name** , enter a name for the OAuth 2.0 client. 

5. In the **Authorized redirect URIs** section, click **Add URI** . 

6. Enter the URL `https://vertexaisearch.cloud.google.com/slack/oauth_callback` . 

7. Click **Create** . 

8. When the **OAuth client created** dialog appears, copy the values of **Client ID** and **Client secret** . 

The ID of your Slack workspace. For more information, see Find your Slack workspace ID (#find-your-slack-workspace-id). 

#### Find your Slack workspace ID

You need your Slack workspace ID to connect your workspace to your Gemini Enterprise app. 

**Note:** If your organization uses Slack Enterprise Grid, don't use your Organization Grid ID (which begins with **`E`** ). If you use the Grid ID, the integration fails and the app doesn't respond to user messages. Use the individual workspace ID (which begins with **`T`** ). 

Standard Slack workspaces 

To find the workspace ID for a standard Slack workspace: 

1. Open your Slack workspace in a web browser. 

2. In the URL, your workspace ID is the string beginning with T. For example, in the URL `https://app.slack.com/client/T0123456789/...` , the workspace ID is `T0123456789` . 

3. Copy and store the workspace ID. 

Slack Enterprise Grid 

To find the workspace ID for a specific workspace in your Enterprise Grid: 

1. Open the Slack Admin Center (https://admin.slack.com/). 

2. In the sidebar, click **Workspaces** . 

3. Select the workspace you want to integrate. 

4. In the URL, your workspace ID is the string beginning with `T` . For example, in the URL `https://admin.slack.com/workspaces/T0123456789` , the workspace ID is `T0123456789` . 

5. Copy and store the workspace ID. 

### Connect your Slack workspace with Gemini Enterprise

Register your Slack workspace in the settings of your Gemini Enterprise app. 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the **Apps** list, select the Gemini Enterprise app to which you want to connect Slack. 

3. Click **Integration > Slack** . 

4. Fill out the required fields: 

Enter your Slack workspace ID. 

Enter your Google Cloud OAuth 2.0 client ID. 

Enter your Google Cloud OAuth 2.0 client secret. 

5. Click **Save** . 

### Install the Gemini Enterprise app for Slack in your Slack workspace

After registering your workspace, install the Gemini Enterprise app for Slack in your Slack workspace. 

1. Click the following link: 

Install Gemini Enterprise app for Slack (https://slack.com/oauth/v2/authorize?client_id=8599736726022.9330833439668&scope=app_me 

2. Click **Allow** . 

3. In your Slack workspace settings, verify that the app installed successfully. If you have a Workspace Owner or Workspace Admin role, you can check to see if the Gemini Enterprise app for Slack has been successfully installed by clicking **Manage > Installed Apps** . 

After installing the app, each user must grant one-time access to the Gemini Enterprise app for Slack if they want Gemini Enterprise to search their data. This authorization is done separately by each user. For instructions, see User authorization (/gemini/enterprise/docs/connectors/connect-existing-data-store#user_authorization). 

### Use the app in Slack

**Note:** To enable the channel mentions (#channel-mentions) and multi-turn support (#multi-turn-support) features, your Slack administrator must reinstall the Gemini Enterprise app. For more information, see Install the Gemini Enterprise app for Slack in your Slack workspace (#install-app). After the administrator reinstalls the app, end users must authorize the Slack connector. For more information, see User authorization (/gemini/enterprise/docs/connectors/connect-existing-data-store#user_authorization). 

After you authorize the Gemini Enterprise app for Slack, you can interact with it in the following ways: 

#### Direct messages with multi-turn support

You can message the Gemini Enterprise app for Slack directly to ask questions. These direct messages support multi-turn conversations. The Gemini Enterprise app remembers the context of your current session. You can ask follow-up questions or refine previous responses. To clear the current context and start a new session, click **New chat** . 

#### Channel mentions

You can collaborate with the Gemini Enterprise app directly in your Slack channels and threads. Mention the app in a channel or thread with a prompt. For example: `@Gemini Enterprise summarize this thread` . The app adds an 👀 (eyes) reaction to your message to confirm receipt of the prompt. The app returns the response privately, and the message is marked as **Only visible to you** . You can review the response before sharing it in the channel or thread. 

**Note:** Chat history is platform-specific. Conversations in the Gemini Enterprise app for Slack remain in Slack, and conversations in the Gemini Enterprise web app remain in the web app. Chat histories are not synced across platforms. 

### What's next

To connect your data sources to Gemini Enterprise, see Connect a Google data source (/gemini/enterprise/docs/create-data-store) and Connect a third-party data source (/gemini/enterprise/docs/connect-third-party-data-source). 

To integrate Gemini Enterprise with Chrome Enterprise cloud-managed browsers, see Configure Chrome Enterprise cloud-managed browsers (/gemini/enterprise/docs/configure-chrome). 

Last updated 2026-10-14 UTC.
