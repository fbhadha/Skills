# Gemini Enterprise: platform, security, agents, cost, monitoring / AI developer tools: overview to Turn off AI developer tools
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 401-439, extracted 2026-10-18

Contains:
- AI developer tools: overview (pages 401-406) https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview
- Configure settings (pages 407-421) https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings
- View metrics (pages 422-428) https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics
- Track third-party model token usage (pages 429-436) https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-track-token-usage
- Create a custom role to restrict access (pages 437-438) https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles
- Turn off AI developer tools (pages 439-439) https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-turn-off

## AI developer tools: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview

**Note:** To use this feature, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

Gemini Enterprise provides AI-powered developer tools designed to accelerate software development and delivery through autonomous agents. With a subscription to the Gemini Enterprise Standard, Plus, or Pay-as-you-go edition and an invoiced Cloud Billing account, users can access the AI developer tools. 

### AI developer tools on Gemini Enterprise

|AI developer tool|Description|
|---|---|
|Google Antigravity|An AI-powered development environment designed to help<br>developers build applications using autonomous AI agents.|
||Supported tools: Antigravity app and Antigravity CLI.|
||To get started, see<br>Get started with Antigravity<br>(https://antigravity.google/docs/enterprise).|
|Antigravity for IDEs|An AI-powered extension for integrated development<br>environments (IDEs) that brings autonomous AI agent capabilities<br>into your developer workflow.|
||Supported IDEs: Visual Studio Code, Visual Studio, JetBrains IDEs<br>(such as IntelliJ IDEA, PyCharm, WebStorm, and GoLand), Zed, and<br>Xcode.|
||To get started, see<br>Antigravity IDE extensions<br>(https://antigravity.google/docs/ide/extensions).|

|AI developer tool|Description|
|---|---|
|Android Studio|The recommended IDE for professional Android development.<br>Provides AI capabilities that help you build, debug, and scale your<br>Android apps faster.|
||Supported tools: the latest<br>stable version of Android Studio<br>(https://developer.android.com/studio).|
||To get started, see<br>Use Android Studio with Gemini Enterprise<br>(https://developer.android.com/studio/gemini/enterprise).|

### Key benefits and use cases

AI developer tools help engineering teams accelerate software delivery and improve code quality through autonomous, multi-step agentic workflows: 

|Use case|Description|
|---|---|
|Automated code reviews<br>and quality checks|Autonomous agents analyze code changes and pull requests to<br>detect bugs, security vulnerabilities, and style violations, offering<br>actionable suggestions and automated fixes before code is<br>merged.|
|Accelerated debugging and<br>root-cause analysis|Agents investigate test failures, build breakages, and runtime<br>errors across large codebases by inspecting logs, tracing stack<br>traces, and proposing validated code corrections.|
|End-to-end feature<br>development and<br>refactoring|Developers can delegate multi-step software engineering tasks—<br>such as implementing new features, refactoring legacy modules,<br>migrating APIs, and generating comprehensive test suites—<br>directly to autonomous AI agents.|
|Seamless CLI and IDE<br>integration|With support for the Antigravity app, the Antigravity CLI,<br>Antigravity for IDEs, and Android Studio, developers can<br>incorporate AI agents into their daily IDE development, terminal<br>workflows, and automated pipelines.|

### Before you begin

Before you use AI developer tools, ensure that your organization meets the following requirements: 

|Requirement|Description|
|---|---|
||You must have a paid or free-trial subscription to the Gemini<br>Enterprise Standard or Plus edition, or a paid subscription to the<br>Standard Emerging Market or Pay-as-you-go edition.|
|Supported editions|Gemini Enterprise Standard Emerging Market edition is available<br>only to eligible customers. Contact your Google account team to<br>assess the requirements and determine your eligibility.|
|Supported regions|For more information about regional availability and feature<br>limitations, see<br>Data residency for Gemini Enterprise Standard and<br>Plus Editions and Gemini Notebook<br>(/gemini/enterprise/docs/locations).|
|Invoiced billing account|Your project must have Cloud Billing enabled and use an invoiced<br>account. For more information, see<br>Cloud Billing account types<br>(/billing/docs/concepts#billing_account_types).|
|Overages|To check usage limits and how overage charges apply, see<br>Quotas<br>and overages(/gemini/enterprise/docs/quotas-and-overages). To<br>enable and configure pay-as-you-go overages when usage<br>exceeds your standard quota, see<br>Configure overages<br>(/gemini/enterprise/docs/configure-overages).|

|Requirement|Description|
|---|---|
||To access or configure AI developer tools, users must have the<br>appropriate role:<br>Gemini Enterprise Admin<br>(/gemini/enterprise/docs/access-<br>control#discoveryengine.agentspaceAdmin)<br>(`roles/discoveryengine.agentspaceAdmin`): Required to<br>configure AI developer tools settings and view metrics.<br>Gemini Enterprise User<br>(/gemini/enterprise/docs/access-<br>control#discoveryengine.agentspaceUser)<br>(`roles/discoveryengine.agentspaceUser`): Required to<br>access and use AI developer tools.|
|Required roles|Note: The Gemini Enterprise Admin role doesn't grant<br>permissions to access AI developer tools. You must explicitly<br>grant the Gemini Enterprise User role to users who need to<br>access AI developer tools, even if they already have the Gemini<br>Enterprise Admin role.|
||To prevent users from accessing AI developer tools, you can create<br>a custom role that doesn't include the AI developer tools<br>permissions and assign that custom role instead of the default<br>Gemini Enterprise User role. For more information, see<br>Create<br>custom roles for AI developer tools<br>(/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles)<br>.|

### Known limitations

The following are known issues and limitations when configuring and using AI developer tools: 

|Limitation|Description|
|---|---|
||If you purchase new Gemini Enterprise subscriptions before you<br>enable the required APIs, the purchase or provisioning might fail.|
|API enablement before<br>license purchases|To resolve this, enable the required APIs as described in<br>Before<br>you begin(/gemini/enterprise/docs/licenses#before-you-begin),<br>and then wait approximately five minutes for the change to<br>propagate before you complete your purchase.|
|Default policy for accessing<br>files outside working folders|When you configure AI developer tools for the first time, the<br>Outside of file access policy defaults to Deny instead of the<br>expected default of Always ask. To prompt users before AI agents<br>access files outside their designated working folders, you must<br>explicitly change this policy to Always ask.|
|Access to Android Studio<br>using a third-party identity<br>provider|Android Studio doesn't support third-party identity providers. If a<br>third-party identity provider is configured for a specific location in<br>your Gemini Enterprise Google Cloud project, users whose licenses<br>are in that location can't access AI developer tools features in<br>Android Studio.|

### Compliance limitations

Antigravity in Gemini Enterprise doesn't support the following compliance certifications and security controls: 

- Access Transparency (AXT) 

- FedRAMP (Moderate and High) 

- Impact Level 4 (IL4) and Impact Level 5 (IL5) 

- International Organization for Standardization (ISO) certifications, including ISO 27001 and ISO 42001 

- International Traffic in Arms Regulations (ITAR) 

- Service Organization Control (SOC) 1, SOC 2, and SOC 3 

### What's next

- Learn how to enable AI developer tools and configure security, compliance, and model availability controls. For more information, see Configure AI developer tools settings (/gemini/enterprise/docs/ai-developer-tools-settings). 

- Learn how to view metrics, adoption telemetry, and third-party model token consumption: 

   - View AI developer tools metrics 

   - (/gemini/enterprise/docs/ai-developer-tools-metrics) 

   - Track third-party model token usage 

   - (/gemini/enterprise/docs/ai-developer-tools-track-token-usage) 

- Learn how to create custom IAM roles to restrict access to AI developer tools. For more information, see Create custom roles for AI developer tools 

- (/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles). 

- Learn how to turn off AI developer tools for your organization. For more information, see Turn off AI developer tools 

- (/gemini/enterprise/docs/ai-developer-tools-turn-off). 

Last updated 2026-10-14 UTC. 



## Configure settings

URL: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings

**Note:** To use this feature, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

Use the AI developer tools settings page in Gemini Enterprise to configure developer tools, enforce security and compliance controls, turn Google Antigravity features on or off, and manage model availability for your organization. 

### Before you begin

Make sure you have the following: 

- **Invoiced Cloud Billing account** : To use AI developer tools, your project must have Cloud Billing enabled. AI developer tools are available for invoiced accounts only. For more information, see Cloud Billing account types (/billing/docs/concepts#billing_account_types). 

- **Supported editions** : To access AI developer tools, users must have a subscription to the Gemini Enterprise Standard, Plus, Standard Emerging Market, or Pay-as-you-go edition. 

**Note:** Gemini Enterprise Standard Emerging Market edition is available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility. 

- **Supported regions** : For more information about regional availability and feature limitations, see Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook (/gemini/enterprise/docs/locations). 

- **Required roles** : You must have the **Gemini Enterprise Admin** ( `roles/discoveryengine.agentspaceAdmin` ) role to configure AI developer tools settings. 

**Note** : The Gemini Enterprise Admin role doesn't grant permissions to access AI developer tools. Administrators must explicitly grant users the Gemini Enterprise User role, even if they already have the Gemini Enterprise Admin role. 

**Required APIs** : Your project must have the following APIs enabled: 

**Discovery Engine API** ( `discoveryengine.googleapis.com` ): Provides core platform services, security and compliance controls, and settings management for Gemini Enterprise. 

**Business AI Code API** ( `businessaicode.googleapis.com` ) : Provides AIpowered code generation for Antigravity in Gemini Enterprise. You must enable this API on your project to let authorized principals reach the service from your project. 

**Note:** Enabling the API is required, but it doesn't automatically grant user access on its own. Users still need both an appropriate IAM role and a Gemini Enterprise license to use the service. 

When you turn on the **AI developer tools** toggle in the Google Cloud console, the system checks your project configuration and automatically enables these required APIs if you haven't already enabled them. 

### Turn on AI developer tools

The availability of AI developer tools depends on your Gemini Enterprise subscription type: 

- **New Standard, Plus, or Pay-as-you-go subscriptions** : AI developer tools is enabled by default in the location where you purchased the subscription if it is supported for that location or region. 

- **Existing subscriptions** : An administrator must manually enable AI developer tools in the Google Cloud console for each location to activate the tools for licensed users. 

To manually enable AI developer tools for an existing Gemini Enterprise subscription, follow these steps: 

1. In the Google Cloud console, go to **Gemini Enterprise** . 

Go to Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click **Settings** , and select the **AI developer tools** tab. 

3. Turn on the **AI developer tools** toggle. 

4. Configure the settings in the **Security** (#configure-security-settings), **Compliance** (#configure-compliance-settings), **Features** 

   - (#configure-feature-settings), and **Model availability** 

   - (#configure-model-availability) sections. 

### Configure security settings

As an administrator, you can prevent unauthorized data exposure across developer interfaces. Use the settings in this section to restrict access to external sources and manage automated execution permissions. For example, you can enforce mandatory security policies to prevent users from overriding safety rules, and require approval before AI agents run terminal commands or select links. 

#### Manage security policies

You can configure security policies to control how AI agents access local files outside their working folders and execute terminal commands in developer workspaces. 

|Setting|Description|Default<br>status|
|---|---|---|
|Outside of file<br>access policy|Specify the agent's permission level for accessing files outside of<br>its designated working folders. The following options are<br>available:<br>Deny: Prevents the agent from accessing files outside its<br>working folders.<br>Always ask: Prompts the user for permission before the agent<br>accesses files outside its working folders.<br>Allow: Permits the agent to access files outside its working<br>folders without prompting.|Deny|
|Terminal auto-<br>execution mode|Enable this setting to let agents run terminal commands<br>automatically to streamline multi-step workflows. The following<br>options are available:<br>Require review: Prompts the user for approval before running<br>any terminal command.<br>Proceed in sandbox: Automatically runs commands in a secure<br>isolated environment.<br>Always proceed: Automatically runs commands in the current<br>environment without prompting.|,<br>Always<br>proceed|
|Sandbox mode|Enable this setting to restrict agent tools to a secure, isolated<br>local sandbox.|Disabled|

#### Manage external web access

If your security policy requires controlling agent access to external websites to prevent data exfiltration, these settings let you limit browser access or restrict it to a list of allowed URLs. 

|Setting|Description|Default status|
|---|---|---|
||Enable this setting to control external web access. This|Disabled|
|Browser access|prevents data exfiltration and defines organizational<br>boundaries.||

|Setting|Description<br>Default status|
|---|---|
|Allowed URLs|Specify a list of allowed URLs that the agent can access in<br>the browser. When configured, the system blocks all other<br>URLs.<br>This setting applies only to the Antigravity browser agent.<br>You can run the browser agent in Antigravity by typing the<br>`/browser`command in the chat field.<br>None. By default,<br>no URLs are<br>blocked.|
|Browser JavaScript<br>auto-execution<br>mode|Enable this setting to let agents run JavaScript to support<br>advanced web-based coding and testing tasks. The<br>following options are available:<br>Disabled: Prevents the agent from running JavaScript.<br>Request review: Prompts the user for approval before<br>the agent runs JavaScript.<br>Allowed: Permits the agent to run JavaScript<br>automatically.<br>Disabled|

#### Manage Model Context Protocol (MCP)

You can configure access to Model Context Protocol (MCP) servers, which lets AI agents securely access additional data sources and tools. 

|Setting|Description|Default<br>status|
|---|---|---|
||Enable this setting to manage access to Model Context Protocol<br>(MCP) servers to securely extend the AI's data context.<br>MCP is required to use IDEs that support the Agent Client Protocol|Disabled|
|MCP servers|(ACP), such as Android Studio and JetBrains IDEs. In these<br>environments, administrator controls operate on a best-effort basis<br>because the IDEs can inject their own MCP tools that aren't subject<br>to enforcement.||

Default Setting Description status Allowed server This setting lets administrators define specific server configurations Not configuration for MCP server access. Administrators define the allowlist as a JSON configured object with configurations for local and remote MCP servers. The UI provides real-time validation for the following fields: Local MCP servers ( `local_servers` ): `id` (string): The unique identifier of the MCP server. `command` (string, optional): The command to run the local MCP server. If specified, this overrides the user's local configuration. `args` (array of strings, optional): The arguments passed to the command. If specified, these override the user's local configuration. Remote MCP servers ( `remote_servers` ): `id` (string): The unique identifier of the MCP server. `url` (string, optional): The endpoint URL of the remote MCP server. Required for custom remote servers and optional for pre-configured remote servers. 

<sup>Example configuration</sup> 

```
{
  "mcpServers": {
    "local_servers": [
      {
        "id": "gopls-mcp-server",
        "command": "go",
        "args": [
          "run",
          "golang.org/x/tools/gopls@latest",
          "mcp"
        ]
      }
    ],
    "remote_servers": [
      {
```

<!-- Start of picture text -->
Default<br>Setting Description<br>status<br>        "id": "bigquery"<br>      },<br>      {<br>        "id": "custom-remote-server",<br>        "url": "https://mcp.example.com/mcp"<br>      }<br>    ]<br>  }<br>}<br><!-- End of picture text -->

### Configure compliance settings

If your organization operates in a regulated industry or has specific internal policies, you might need to maintain audit logs of AI interactions for compliance. This section's settings let you configure logging and data retention policies to meet your legal and regulatory requirements. 

<!-- Start of picture text -->
Default<br>Setting Description<br>status<br>Enable this setting to record interactions between developers and the AI Disabled<br>Prompts and to compute usage metrics and maintain an audit trail for security<br>responses reviews. The system stores logs securely within your organization's<br>logging project, and Google never accesses the logs for model training or human<br>review.<br>Enable this setting to record product metadata to help you track usage Disabled<br>and analytics across your organization, including third-party model token<br>Metadata consumption<br>logging  (/gemini/enterprise/docs/ai-developer-tools-track-token-usage). The<br>system stores logs securely within your organization's project, and<br>Google never accesses the logs for model training or human review.<br><!-- End of picture text -->

### Configure feature settings

Some Antigravity features offer advanced multi-agent capabilities to help developers tackle complex tasks. Because these features can increase token usage and costs, use the settings in this section to control access for users in your organization. To access enabled features, users must use Antigravity app version 2.18.0 or later, or Antigravity CLI version 1.2.10 or later. 

To turn a feature on or off, follow these steps: 

1. In the Google Cloud console, go to **Gemini Enterprise** . 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click **Settings** and select the **AI developer tools** tab. 

3. In the **Features** section, click **Edit** . 

4. For each feature, turn the toggle on or off. 

Default Setting Description status Enable this setting to let users run a tiered multi-agent hierarchy to Enabled `/boost` solve complex algorithmic challenges and deep debugging tasks. command For more information, see Boost deep reasoning (https://antigravity.google/docs/boost). Enable this setting to let users deploy a coordinated framework of Enabled `/teamwork-` autonomous subagents to execute large-scale, long-horizon projects `preview` (Preview). For more information, see Teamwork agent teams command (https://antigravity.google/docs/teamwork). 

5. Click **Save** . 

### Configure model availability

Use the settings in this section to authorize specific AI models and manage access levels. This ensures developers only use AI models that comply with your organization's safety and usage policies. For example, you can give developers access to preview models for experiments, or restrict tools to use only authorized models. 

#### Key considerations before configuring models

Before you configure models, consider the following: 

- **Policy alignment:** Enabling a model in Gemini Enterprise doesn't override Gemini Enterprise Agent Platform organization policies. To prevent pay-asyou-go requests that exceed your standard quota from failing, ensure that the allowed models match across both platforms. 

- **Data residency:** Preview models and the Gemini 3 Pro Image model are available only in the `global` region. Therefore, they don't support data residency (DRZ) or machine learning (ML) regional processing commitments in the US or EU multi-regions. 

- **Third-party model inference and data handling:** Third-party models are available only after an administrator enables them and accepts the provider's terms. When a developer selects an enabled third-party model, Gemini Enterprise sends the prompt and the code context needed for that request to the model, with the same processing and protections as Gemini models. Prompts and responses aren't used to train models. Third-party model inference is available in the `global` , `us` , and `eu` locations. In-country regions aren't supported. To see the list of countries and regions that can access the model, see Anthropic's Supported countries and regions 

- (https://www.anthropic.com/supported-countries). For more information on data residency, see Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook (/gemini/enterprise/docs/locations). 

- **Hybrid execution and billing disclosures:** Gemini models draw from your organization's pooled edition seat credits, while administrator-enabled thirdparty models are billed as pay-as-you-go usage on your Cloud Billing account. When a developer selects an enabled third-party model (such as **Anthropic Claude Opus 5.5** or **Anthropic Claude Sonnet 5.5** ) for primary reasoning, planning, tool orchestration, and code generation tasks, Antigravity continues to use lightweight Gemini models in the background for client-side coordination—such as context management and summaries—and Gemini 3 Pro Image for image generation. Using these models can incur charges. For more information, see Quotas and overages 

- (/gemini/enterprise/docs/quotas-and-overages) and Track third-party model token usage (/gemini/enterprise/docs/ai-developer-tools-track-token-usage). 

#### Configure authorized models

You can configure authorized models to control which AI models are available to your AI developer tools. 

The **Antigravity authorized models** setting operates as an allowlist: 

- **Default selection (empty)** : When the field is empty, all supported Gemini models are permitted. Newly released Google models become available automatically to licensed users. 

- **Custom model list** : When you select one or more specific models, only the selected models are permitted. Unselected models and newly released models aren't available to developers until an administrator manually selects them. 

To configure authorized models: 

1. In the Google Cloud console, go to **Gemini Enterprise** . 

Go to Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click **Settings** , and then select the **AI developer tools** tab. 

3. In the **Model availability** section, click **Edit** . 

4. In the **Antigravity authorized models** field, select the models that you want to permit. To permit all supported models, leave the field empty. 

5. Click **Save** . 

|Setting|Description|Default status|
|---|---|---|
|Antigravity<br>authorized<br>models|Specify which AI models the Antigravity tool is authorized to use<br>within the project. Leave the field empty to allow all supported<br>Gemini models. If you specify a custom list of models, the<br>setting acts as an allowlist, and newly released or unselected<br>models must be manually added to become available. In<br>addition to Gemini models made by Google, administrators can<br>opt in to enable third-party models, including Anthropic Claude<br>Opus 5.5 and Anthropic Claude Sonnet 5.5. For information<br>about each model's capabilities, limitations, and safety<br>evaluations, see the model cards for<br>Anthropic Claude Opus 5.5<br>(/gemini-enterprise-agent-platform/models/partner-<br>models/claude/opus-5-5)<br>and<br>Anthropic Claude Sonnet 5.5<br>(/gemini-enterprise-agent-platform/models/partner-<br>models/claude/sonnet-5-5)<br>.|<br>Empty (all Gemini<br>models<br>permitted). Third-<br>party models are<br>turned off by<br>default and<br>require<br>administrator<br>consent.|

#### Supported models

AI developer tools ( **Antigravity app** , the **Antigravity CLI** , and **Antigravity for IDEs** ) support the following Gemini models and partner models. A _licensed user_ is a developer assigned an active Gemini Enterprise seat license (Standard, Plus, or Pay-as-you-go). For more information, see Manage licenses (/gemini/enterprise/docs/licenses). 

|Model display<br>name|Provider|Availability in Gemini Enterprise|
|---|---|---|
|Gemini 4 Argon|Google|Enabled by default for licensed users when default model selection is<br>active (empty list). If a custom model list is configured, the model<br>must be manually selected.|
|Gemini 3.8<br>Flash|Google|Enabled by default for licensed users when default model selection is<br>active. If a custom model list is configured, the model must be<br>manually selected.|
|Gemini 3.7<br>Flash|Google|Enabled by default for licensed users when default model selection is<br>active. If a custom model list is configured, the model must be<br>manually selected.|

|Model display<br>name|Provider|Availability in Gemini Enterprise|
|---|---|---|
|Gemini 3.6<br>Flash|Google|Enabled by default for licensed users when default model selection is<br>active. If a custom model list is configured, the model must be<br>manually selected.|
|Gemini 3.1 Pro<br>(Preview)|Google|Enabled by default for licensed users when default model selection is<br>active. If a custom model list is configured, the model must be<br>manually selected.|
|Anthropic<br>Claude Opus 5.5|<br>Anthropi f|cTurned off by default. Requires administrator opt-in (see<br>Enable or<br>turn offthird-party models(#enable-third-party-models)).|
|Anthropic<br>Claude Sonnet<br>5.5|Anthropi f|cTurned off by default. Requires administrator opt-in (see<br>Enable or<br>turn offthird-party models(#enable-third-party-models)).|

For information about quotas and pooled edition credits, see Quotas and overages (/gemini/enterprise/docs/quotas-and-overages) and Configure overages (/gemini/enterprise/docs/configure-overages). For third-party model pricing, see the Cloud Billing SKUs for Anthropic Claude Opus 5.5 (https://cloud.google.com/skus?filter=opus&currency=USD&e=48754805) and Anthropic Claude Sonnet 5.5 

(https://cloud.google.com/skus?filter=sonnet&currency=USD&e=48754805). 

#### Thinking level for third-party models

Developers can use **Anthropic Claude Opus 5.5** and **Anthropic Claude Sonnet 5.5** at a thinking level of Low, Medium, High, or Max. Each level appears as a separate entry in the model picker, for example **Anthropic Claude Opus 5.5 (High)** . Medium is the default. When you enable a third-party model, all of its thinking levels are available to developers. You can't restrict individual thinking levels. 

#### Enable or turn off third-party models

Third-party models are billed as pay-as-you-go usage and require overages. Before you enable a third-party model, turn on overages (/gemini/enterprise/docs/configure-overages). If overages are turned off later, 

developers can't use third-party models until overages are turned back on. To control costs, you can set a monthly spend limit 

(/gemini/enterprise/docs/configure-overages#set-spend-limit) for your project. The limit applies to all models, including third-party models. 

To enable or manage third-party models (such as **Anthropic Claude Opus 5.5** and **Anthropic Claude Sonnet 5.5** ) in the Google Cloud console: 

1. In the Google Cloud console, go to **Gemini Enterprise** . 

Go to Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click **Settings** , and then select the **AI developer tools** tab. 

3. In the **Antigravity authorized models** setting, turn on the toggle for the third-party model that you want to enable. 

4. In the embedded Terms of Service dialog that appears, review and accept the third-party terms. 

If you turn off a third-party model, developers lose access to it shortly afterwards. If the model provider restricts access to a third-party model for your organization, developers can't use that model. To resolve the issue, contact Google Cloud Support (/support/docs). 

For developer instructions on signing in to Antigravity and selecting models, see the Antigravity enterprise documentation (https://antigravity.google/docs/enterprise/). 

#### Security considerations for third-party models

AI models, including third-party models, can follow instructions hidden in content they process, such as files, web pages, or tool output. This is known as _prompt injection_ . Antigravity provides the following protections when developers use thirdparty models: 

- **Administrator opt-in:** Third-party models are off by default. Developers can use a third-party model only after an administrator enables it. 

- **Provider safety protections:** Third-party models include the provider's built-in safety protections. For more information, see Claude safety 

- (/gemini-enterprise-agent-platform/models/partner-models/claude/safety). 

- **Your security policies:** The security policies (#manage-security-policies) and external web access (#manage-external-web-access) settings that you configure apply to agents regardless of the model that a developer selects. 

**Best practices** 

- Enable only the third-party models that your developers need. 

- Set **Terminal auto-execution mode** to **Require review** or **Proceed in sandbox** , so that developers approve commands before they run. 

- Keep **Outside of file access policy** set to **Deny** . 

- Turn on **Browser access** and limit agents to a list of **Allowed URLs** . 

- Turn on **Sandbox mode** for projects that work with untrusted code, dependencies, or web content. 

- Encourage developers to review the commands and code changes that agents propose before approving them. 

- Set a monthly spend limit 

- (/gemini/enterprise/docs/configure-overages#set-spend-limit) for your project. 

### What's next

- Track third-party model token usage 

- (/gemini/enterprise/docs/ai-developer-tools-track-token-usage) 

- View AI developer tools metrics (/gemini/enterprise/docs/ai-developer-tools-metrics) 

- Create custom roles for AI developer tools 

- (/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles) 

- Turn off AI developer tools (/gemini/enterprise/docs/ai-developer-tools-turn-off) 

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## View metrics

URL: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-metrics

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

**Note:** To use this feature, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

This document describes how to view usage metrics and telemetry for AI developer tools (/gemini/enterprise/docs/ai-developer-tools-overview) in your organization, such as Google Antigravity and the Antigravity CLI. These metrics show user adoption, token consumption, API calls, and tool execution. 

### Before you begin

Before you view AI developer tools metrics, make sure you meet the following prerequisites: 

- **Turn on AI developer tools** : To view AI developer tools metrics, your organization must turn on AI developer tools for the project. See Turn on AI developer tools 

- (/gemini/enterprise/docs/ai-developer-tools-settings#enable-ai-developer-tools). 

- **Invoiced Cloud Billing account** : Your project needs Cloud Billing enabled and an invoiced account. See Cloud Billing account types 

- (/billing/docs/concepts#billing_account_types). 

- **Supported editions** : Users need a subscription to the Gemini Enterprise Standard, Plus, Standard Emerging Market, or Pay-as-you-go edition. 

**Note:** Gemini Enterprise Standard Emerging Market edition is available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility. 

- **Required roles** : To access the **Developer tools metrics** page in the Google Cloud console, you need the Gemini Enterprise Admin 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) 

- ( `roles/discoveryengine.agentspaceAdmin` ) role. 

### Access the metrics dashboard

To view AI developer tools metrics in the Google Cloud console, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise) 

2. Select the Google Cloud project where you enabled AI developer tools. 

3. In the navigation menu, click **Developer tools metrics** . 

4. Use the time-range controls in the top-right corner of the dashboard to adjust the reporting timeframe: 

|Control|Description|
|---|---|
|Time-range selector menu|By default, the dashboard displays data for Last 1 day with<br>automatic live refreshing enabled. Click the menu to do any of<br>the following:<br>Type a custom duration directly into the Relative time filter<br>field (for example,`15m`,`1h`,`1d`, or`1w`).<br>Select a preset relative timeframe: Today, Yesterday, Last<br>15 minutes, Last 30 minutes, Last 1 hour, Last 3 hours, Last<br>6 hours, Last 12 hours, Last 1 day, Last 2 days, Last 7 days,<br>or Last 14 days.<br>Click Start and end times to specify a custom start and end<br>date and time for the reporting window.<br>Click Around a time to specify a date and time and display<br>metrics centered around that timestamp.<br>Click Time zone to select a different display timezone for<br>the charts (for example, PDT (UTC-7)).|
|Left and right arrows|Shift the reporting timeframe backward () or forward () in time<br>by the duration selected in the menu. For example, if Last 1<br>day is selected, clicking shifts the charts backward by one day.|
|Zoom out of time range|Click to zoom out of a specific time range. All charts update to<br>show data for the zoomed-out time range. To zoom in and<br>reset the view, select a duration from the Time-range selector<br>menu.|
|Auto-refresh|Toggle automatic live refreshing of dashboard data on or off<br>when viewing a relative timeframe. When an absolute time<br>range is selected (such as custom start and end times or a<br>historical window), auto-refresh is disabled because auto-<br>refresh isn't supported for absolute time ranges.|

### Explore chart data

Each chart on the **Developer tools metrics** dashboard provides interactive controls to help you inspect time series, correlate metrics with logs, and analyze underlying data: 

|Control|Description|
|---|---|
|Information|Next to the chart title, click Information to view details about the<br>filters, groupings, and aggregation properties applied to the<br>chart's metric query.|
|Create alert policy|On metric line charts, click Create alert policy in the chart toolbar<br>to open the<br>alerting workflow(/monitoring/alerts/using-alerting-ui)<br>in Cloud Monitoring pre-populated with the chart's time-series<br>query. You can then configure threshold conditions and notification<br>channels for the metric.|
|Explore data|In the chart toolbar, click Explore data to open the metric query in<br>Metrics Explorer(/monitoring/charts/metrics-explorer). In Metrics<br>Explorer, you can inspect, filter, group, and modify the underlying<br>time-series query across different dimensions, or save customized<br>views to a custom dashboard.|
|View in full screen|In the chart toolbar, click More chart options, and then select View<br>in full screen to expand the chart to fill your screen for detailed<br>inspection of time series and legend data.|
|Inspect related logs|You can correlate metric data with log entries written around the<br>same timeframe to troubleshoot activity and errors:<br>Dashboard view: In the chart toolbar, click More chart options,<br>and then select Inspect related logs to open a split-view panel<br>displaying the chart alongside correlated log entries.<br>Data-point tooltip: On any chart time series, hold your pointer<br>over a specific data point, and then select Inspect related logs<br>from the tooltip. In this mode, the split-view panel filters log<br>entries to a window five minutes before and after the selected<br>timestamp.|

### Available metrics

The following table lists all metrics available on the dashboard. 

**Note:** Metrics typically appear on the dashboard within 5 to 15 minutes of user activity. 

|Section|Metric name|Description|
|---|---|---|
||An active user is a unique us<br>action (such as an API reque<br>reporting timeframe.|er who initiated at least one AI developer tool<br>st, prompt, or tool execution) during the|
||Hourly active users<br>(average)|Displays the average number of unique active<br>users per hour over the selected timeframe.|
||Daily active users (average)|Displays the average number of unique active<br>users per day over the selected timeframe.|
||Weekly active users<br>(average)|Displays the average number of unique active<br>users per week over the selected timeframe.|
||Monthly active users<br>(average)|Displays the average number of unique active<br>users per month (28-day active users) over the|
|Active Users<br>||selected timeframe.|
|(Adoption)|Hourly Active Users|A trend line chart that shows the number of<br>unique active users by hour over the selected<br>timeframe.|
||Daily Active Users|A trend line chart that shows the number of<br>unique active users by day over the selected<br>timeframe.|
||Weekly Active Users|A trend line chart that shows the number of<br>unique active users by week over the selected<br>timeframe.|
||Monthly Active Users|A trend line chart that shows the number of<br>unique active users by month (28-day active<br>users) over the selected timeframe.|

|Section|Metric name|Description|
|---|---|---|
||Total Tokens|The total number of combined input and output<br>tokens consumed by AI developer tools over<br>the selected timeframe.|
||Daily Token Usage|A line chart showing daily token consumption<br>over time.|
|Tools & API calls|Daily API Calls|A line chart showing the daily count of API calls<br>made by AI developer tools, including an error<br>breakdown by`error_type`label (for example,<br>quota limits, authentication errors, or client<br>errors).|
||Daily Tool Calls|A line chart showing the daily count of tool<br>calls initiated by AI developer tools.|
||Daily Tool Calls Accepted|A line chart showing the daily count of agent-<br>proposed tool call suggestions that users<br>accepted and executed.|

### What's next

- Learn more about available tools and capabilities in the AI developer tools overview (/gemini/enterprise/docs/ai-developer-tools-overview). 

- Learn how to configure developer tools settings. For more information, see Configure AI developer tools settings 

- (/gemini/enterprise/docs/ai-developer-tools-settings). 

- Learn how to manage access with custom roles. For more information, see Create custom roles for AI developer tools 

- (/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles). 



## Track third-party model token usage

URL: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-track-token-usage

**Note:** To use this feature, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

You can calculate token consumption by model, day, and user for third-party models in AI developer tools (/gemini/enterprise/docs/ai-developer-tools-overview), such as **Anthropic Claude Opus 5.5** and **Anthropic Claude Sonnet 5.5** , using Cloud Logging and **Observability Analytics** . 

### Quickstart

If your project's `_Default` log bucket is already upgraded for **Observability Analytics** , run the following query in **Logging > Observability Analytics** (replacing `[PROJECT_ID]` with your Google Cloud project ID) to get 30-day token usage across third-party Anthropic models: 

```
SELECT
 JSON_VALUE(labels.model) AS model,
 COUNT(*) AS requests,
 SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.promptTokenCount) AS INT64))
AS input_tokens,
 SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.candidatesTokenCount) AS
INT64)) AS output_tokens,
IFNULL(SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.cachedContentTokenCount)
AS INT64)), 0) AS cached_tokens,
 IFNULL(SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.thoughtsTokenCount) AS
INT64)), 0) AS thoughts_tokens,
 SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS INT64)) AS
total_tokens
FROM
 `[PROJECT_ID].global._Default._Default`
WHERE
 log_id = "businessaicode.googleapis.com/inference_response"
 AND JSON_VALUE(labels.model_provider) = "Anthropic"
 AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
```

`GROUP BY` 

```
 model
ORDER BY
 total_tokens DESC
```

### Before you begin

Make sure that your project meets the following requirements before running the tutorial steps: 

**Metadata logging is enabled.** Your AI developer tools administrator controls must have **Metadata logging** 

(/gemini/enterprise/docs/ai-developer-tools-settings#configure-compliance-settings) enabled so that `inference_response` records include the `jsonPayload.metadata` token block. 

- **You hold at least the Logs Viewer role (** **`roles/logging.viewer` ) .** The standard `roles/logging.viewer` role grants SQL access to the `_Default._Default` log view used throughout this guide. Querying the `_Default._AllLogs` view requires `roles/logging.privateLogViewer` or `roles/logging.viewAccessor` . 

**Your** **`_Default` log bucket is upgraded for Observability Analytics.** 

1. In the Google Cloud console, go to **Logging > Logs Storage** , find the `_Default` bucket, and check the **Observability Analytics** column. 

2. If it isn't enabled, click **More** > **Upgrade to use Observability Analytics** . Upgrading modifies `_Default` in place and can't be undone. 

3. **Allow for initial propagation:** After upgrading a bucket, Cloud Logging takes 30 to 60 minutes to refresh routing caches for new log entries, and several hours to backfill historical logs (backfill begins 1 hour after the upgrade completes). 

### How the log record is structured

Every inference call emits a single `InferenceResponseLog` entry to the `businessaicode.googleapis.com%2Finference_response` log. Model identity is recorded in `labels` , and token counts are recorded in `jsonPayload.metadata` : 

```
{
 "logName":
"projects/[PROJECT_ID]/logs/businessaicode.googleapis.com%2Finference_response"
,
 "timestamp": "2026-10-07T17:23:03.495323480Z",
 "labels": {
   "model": "claude-sonnet-5-5",
   "model_provider": "Anthropic",
   "client_name": "antigravity_cli",
   "user_id": "user:user@example.com",
   "trajectory_id": "25cd0b58-58ea-4beb-b2d7-42e0d3fdd96d",
   "request_id": "25cd0b58-58ea-4beb-b2d7-42e0d3fdd96d-19"
 },
 "jsonPayload": {
   "@type":
"type.googleapis.com/google.cloud.businessaicode.logging.v1.InferenceResponseLo
g",
   "metadata": {
     "promptTokenCount": "70825",
     "cachedContentTokenCount": "69079",
     "candidatesTokenCount": "14215",
     "totalTokenCount": "85040"
   }
 }
}
```

#### Field reference and counting rules

|LogEntry field<br>(Logs Explorer and<br>Log-based metrics)|<br>SQL expression (Observability<br>Analytics)|Description|
|---|---|---|
|`labels.model`|`JSON_VALUE(labels.model)`|Model identifier (for example,`claude-`<br>`sonnet-5-5`for Anthropic Claude Sonnet<br>5.5 or`claude-opus-5-5`for Anthropic|
|||Claude Opus 5.5).|

|LogEntry field<br>(Logs Explorer and<br>Log-based metrics)|<br>SQL expression (Observability<br>Analytics)|Description|
|---|---|---|
|`labels.model_`<br>`provider`|`JSON_VALUE(labels.model_`<br>`provider)`|Provider name (for example,`Anthropic`or<br>`Google`).|
|`labels.user_id`|`JSON_VALUE(labels.user_id)`|Authenticated principal (for example,<br>`user:user@example.com`).|
|`labels.`<br>`trajectory_id`|`JSON_VALUE(labels.`<br>`trajectory_id)`|Conversation or agent trajectory ID. One<br>user turn typically spans multiple<br>`request_id`calls under a single<br>`trajectory_id`.|
|`jsonPayload.`<br>`metadata.prompt`<br>`TokenCount`|`SAFE_CAST(JSON_VALUE(json_`<br>`payload.metadata.prompt`<br>`TokenCount) AS INT64)`|Total input tokens for the call (includes<br>cached tokens).|
|`jsonPayload.`<br>`metadata.cached`<br>`ContentToken`<br>`Count`|`SAFE_CAST(JSON_VALUE(json_`<br>`payload.metadata.cached`<br>`ContentTokenCount) AS`<br>`INT64)`|Subset of`promptTokenCount`served from<br>prompt cache. Omitted when zero. Don't<br>add to`promptTokenCount`or`totalToken`<br>`Count`.|
|`jsonPayload.`<br>`metadata.`<br>`candidatesToken`<br>`Count`|`SAFE_CAST(JSON_VALUE(json_`<br>`payload.metadata.candidates`<br>`TokenCount) AS INT64)`|Output tokens generated by the model.|
|`jsonPayload.`<br>`metadata.`<br>`thoughtsToken`<br>`Count`|`SAFE_CAST(JSON_VALUE(json_`<br>`payload.metadata.thoughts`<br>`TokenCount) AS INT64)`|Reasoning tokens, when applicable.<br>Omitted for Anthropic models.|
|`jsonPayload.`<br>`metadata.total`<br>`TokenCount`|`SAFE_CAST(JSON_VALUE(json_`<br>`payload.metadata.totalToken`<br>`Count) AS INT64)`|Authoritative total for the call. Equals<br>`promptTokenCount + candidatesToken`<br>`Count`(+`thoughtsTokenCount`when<br>present).|

### Step 1: Verify incoming logs in Logs Explorer

Before running SQL queries, confirm that `inference_response` records with token metadata are arriving in your project: 

1. In the Google Cloud console, open **Logging > Logs Explorer** . 

2. Paste the following query into the query editor, replacing `[PROJECT_ID]` with your project ID: 

```
logName="projects/[PROJECT_ID]/logs/businessaicode.googleapis.com%2Finfere
nce_response"
labels.model_provider="Anthropic"
```

3. Click **Run query** . 

4. In the **Log fields** pane, click **model** to view the request distribution across Anthropic models. This view counts requests, not tokens. 

### Step 2: Sum tokens by model in Observability Analytics

1. In the Google Cloud console, open **Logging > Observability Analytics** . 

2. Set the **Time-range selector** to **Last 30 days** (the time-range selector bounds your query results in addition to your SQL `WHERE` clause). 

3. Paste and run the following query, replacing `[PROJECT_ID]` with your project ID: 

`SELECT` 

```
 JSON_VALUE(labels.model) AS model,
 COUNT(*) AS requests,
 SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.promptTokenCount) AS
INT64)) AS input_tokens,
 SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.candidatesTokenCount) AS
INT64)) AS output_tokens,
IFNULL(SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.cachedContentTokenCo
unt) AS INT64)), 0) AS cached_tokens,
IFNULL(SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.thoughtsTokenCount)
AS INT64)), 0) AS thoughts_tokens,
 SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS
INT64)) AS total_tokens
FROM
 `[PROJECT_ID].global._Default._Default`
WHERE
 log_id = "businessaicode.googleapis.com/inference_response"
 AND JSON_VALUE(labels.model_provider) = "Anthropic"
 AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY
 model
ORDER BY
 total_tokens DESC
```

### Step 3: Common SQL recipes

Use the following SQL queries in **Logging > Observability Analytics** to analyze daily token trends and per-user token attribution. 

#### Daily token trend by model

```
SELECT
 TIMESTAMP_TRUNC(timestamp, DAY) AS day,
 JSON_VALUE(labels.model) AS model,
 COUNT(*) AS requests,
 SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS INT64)) AS
total_tokens
FROM
 `[PROJECT_ID].global._Default._Default`
WHERE
 log_id = "businessaicode.googleapis.com/inference_response"
 AND JSON_VALUE(labels.model_provider) = "Anthropic"
 AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY
 day, model
ORDER BY
 day DESC, total_tokens DESC
```

#### Per-user, per-model attribution

```
SELECT
 JSON_VALUE(labels.user_id) AS user_id,
 JSON_VALUE(labels.model) AS model,
 COUNT(*) AS requests,
 SUM(SAFE_CAST(JSON_VALUE(json_payload.metadata.totalTokenCount) AS INT64)) AS
total_tokens
FROM
 `[PROJECT_ID].global._Default._Default`
WHERE
 log_id = "businessaicode.googleapis.com/inference_response"
 AND JSON_VALUE(labels.model_provider) = "Anthropic"
 AND JSON_VALUE(labels.user_id) IS NOT NULL
 AND timestamp >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY
 user_id, model
ORDER BY
 total_tokens DESC
```

### Step 4: Pin to a Cloud Monitoring dashboard

You have two options for dashboarding, depending on whether you need historical or ad hoc SQL breakdowns, or a lightweight continuous metric: 

|Approach|Best for|Retains history<br>beyond 30 days?|Supports<br>`user_id`<br>grouping?|
|---|---|---|---|
|Option A: Save SQL|Per-model, daily, and per-|Bounded by log|Yes (no cardinality|
|chart from Observabili|ty<br>user tables and charts with|bucket retention|limit)|
|Analytics|zero metric setup|(default 30 days)||
|Option B: Log-based<br>distribution metric|Continuous Monitoring time<br>series and alerting on low-<br>cardinality labels|Yes (stored in<br>Monitoring)|No (high cardinality<br>exhausts metric<br>quota)|

#### Option A: Save directly from Observability Analytics

1. Run the query from Step 2 (#sum-tokens-by-model) or the Daily token trend by model (#daily-token-trend-by-model) query in **Observability Analytics** . 

2. Switch the results pane from **Table** to **Chart** if you want a visual time series or bar chart. 

3. In the results pane toolbar, click **Save to dashboard** , and then choose an existing Monitoring dashboard or create a new one. 

#### Option B: Create a log-based distribution metric

1. In the Google Cloud console, go to **Logging > Log-based metrics** , and then click **Create metric** . 

2. Select **Distribution** as the metric type. 

3. Paste the query from Step 1 (#verify-incoming-logs) into the **Filter** field, and set **Field name** to `jsonPayload.metadata.totalTokenCount` . 

4. Add two labels: 

   - `model` mapped to `labels.model` 

   - `model_provider` mapped to `labels.model_provider` 

### What's next

- View AI developer tools metrics (/gemini/enterprise/docs/ai-developer-tools-metrics) 

- Configure AI developer tools model availability 

- (/gemini/enterprise/docs/ai-developer-tools-settings#configure-model-availability) 

- Configure AI developer tools compliance settings 

- (/gemini/enterprise/docs/ai-developer-tools-settings#configure-compliance-settings) 

Last updated 2026-10-14 UTC. 



## Create a custom role to restrict access

URL: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-creating-custom-roles

**Note:** To use this feature, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

Default roles often provide broad access. To restrict access to AI developer tools and better align permissions with your organization's security policies, create custom roles. This guide shows you how to create and assign a custom IAM role for Gemini Enterprise's AI developer tools in the Google Cloud console. 

When AI developer tools are enabled, users with a Gemini Enterprise license can access these tools if you grant them the Gemini Enterprise User (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) ( `roles/discoveryengine.agentspaceUser` ) role. 

### Create a custom IAM role

To create a custom IAM role that restricts access to AI developer tools, follow these instructions: 

1. In the Google Cloud console, go to **IAM & Admin > Roles** . 

2. Click **Create role** . 

3. Enter the role details: 

   - **Title:** Give your role a name. For example, Custom Gemini Enterprise User. 

   - **ID:** The Google Cloud console automatically generates the ID, but you can edit it. 

   - **Role launch stage:** Set this to "General Availability". 

4. Click **Add permissions** . 

5. In the panel, search for and select the Gemini Enterprise User (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) ( `roles/discoveryengine.agentspaceUser` ) role. 

6. Remove all permissions starting with `businessaicode.` from the Gemini Enterprise User role to ensure users assigned this custom role can't access the AI developer tools feature. 

7. Click **Create** . 

### Add users to the custom role

To add users to the custom role you created, follow these steps: 

1. In the Google Cloud console, go to **IAM & Admin > IAM** . 

2. Click the **Grant access** button at the top of the page. 

3. In the **New principals** field, enter the email addresses of the users or groups you want to add. 

4. Assign the role: 

   - Click **Assign roles** and search for the **Title** of the custom role you created in the previous section. 

   - Select the role. 

5. Click **Save** . 

Last updated 2026-10-14 UTC. 



## Turn off AI developer tools

URL: https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-turn-off

**Note:** To use this feature, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

This page describes how to turn off AI developer tools for your organization in the Google Cloud console. When you turn off AI developer tools, users in your project can no longer access these features. 

## Turn off AI developer tools

To turn off AI developer tools, follow these steps: 

1. In the Google Cloud console, go to **Gemini Enterprise** . 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click **Settings** , and select the **AI developer tools** tab. 

3. Turn off the **AI developer tools** toggle. 

The setting is automatically saved. 

Last updated 2026-10-14 UTC.
