# Gemini Enterprise: user guide, Workflow Builder, developer guide / Manage workflow versions to Create and manage projects
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 169-205, extracted 2026-10-18

Contains:
- Manage workflow versions (pages 169-172) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions
- Workflow runs (pages 173-176) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs
- Delete a workflow (pages 177-178) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/delete-workflows
- Quotas and limits for Workflow Builder (pages 179-187) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits
- Known issues and limitations (pages 188-192) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues
- Get reports with Deep Research (pages 193-194) https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant
- Core Assistant agent (pages 195-197) https://docs.cloud.google.com/gemini/enterprise/docs/core-assistant
- Accelerate research and development with Co-Scientist agent (pages 198-200) https://docs.cloud.google.com/gemini/enterprise/docs/co-scientist-and-alphaevolve
- Create and manage projects (pages 201-205) https://docs.cloud.google.com/gemini/enterprise/docs/projects

## Manage workflow versions

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/manage-agent-versions

You can save, compare, delete, and restore versions of your workflow in Workflow Builder. 

Versioning lets you track changes across workflow iterations, preserve working configurations, and restore previous versions if needed. 

### Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features 

(/gemini/enterprise/docs/manage-web-app-features). 

### Save a version

To save a version of your workflow: 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing workflow in the flow builder. 

3. Click the drop-down arrow next to the **Turn on** or **Update** button. 

4. Click **Save version** . 

5. In the **Save version** dialog, do one of the following: 

Click **Save version only** to save the version without turning it on. 

- Click **Turn on** (or **Update** ) to save and make it live. 

**Note:** Turning on the workflow or updating it creates a new version of your workflow with your most recent changes and makes it live. Saving a version without making it live preserves your changes but does not update the live workflow. 

### View version history

App (#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing workflow in the flow builder. 

3. Click the drop-down arrow next to the **Turn on** or **Update** button. 

4. Click **View version history** . 

5. Browse the list of saved versions. Each version shows the version name and timestamp. 

6. Click a version to view its details or restore it. 

### Restore a version

To restore a version of your workflow: 

App 

- (#app) 

   1. Open your Gemini Enterprise web app in a browser. 

   2. Navigate to an existing workflow in the flow builder. 

   3. Click the drop-down arrow next to the **Turn on** or **Update** button. 

   4. Click **View version history** . 

5. Browse the list of saved versions. Each version shows the version name and timestamp. 

6. Click a version to view its details or restore it. 

7. Click **Restore this version** . The **Restore version?** dialog opens. 

8. Click **Restore** . 

The restored version details overwrite the current working draft. This includes the workflow's graph but _not_ the workflow name or description. 

### Delete a version

To delete a version of your workflow: 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing workflow in the flow builder. 

3. Click the drop-down arrow next to the **Turn on** or **Update** button. 

4. Click **View version history** . 

5. Browse the list of saved versions. Each version shows the version name and timestamp. 

6. Click the **More actions** icon and then click **Delete** . The **Delete version** dialog opens. 

   - a. Select the checkbox confirming your request to delete the version. 

   - b. Click **Delete** . 

After the version is deleted, it can't be restored and the data associated with the version is not retained. 

**Note:** Deleting a version removes the associated workflow graph for that version's runs. Use caution when deleting versions. 

### What's next

- Learn how to edit a workflow with natural language (/gemini/enterprise/docs/workflow-builder/edit-workflows). 

Learn how to view workflow runs 

- (/gemini/enterprise/docs/workflow-builder/workflow-runs). 

- Learn how to create a workflow with natural language (/gemini/enterprise/docs/workflow-builder/create-natural-language). 

Last updated 2026-10-14 UTC. 



## Workflow runs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflow-runs

A workflow run is an instance of a workflow that is executed by a trigger. The **Runs** tab in the workflow canvas lets you monitor and manage the execution logs of your workflow. Monitoring workflow runs is helpful for tracking automated tasks, debugging failed executions, and reviewing the performance of your workflow versions. 

### Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features 

(/gemini/enterprise/docs/manage-web-app-features). 

### View runs for all workflows

To view all workflow runs for your web app, do the following: 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app. 

4. Click **Runs** to view all workflow runs for your web app. 

The **Runs** tab displays a list of all workflow runs for your web app as shown in the following image. 

### View runs for a specific workflow

To view the execution logs of a workflow, do the following: 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app. 

4. Go to the **Your agents** section and click the workflow to view its execution logs. 

5. Click the **Runs** tab. 

The **Runs** tab displays a list of all executions, including simulations performed in the **Preview** tab and automated runs initiated by a trigger. Selecting an individual run from the list lets you view granular details about that specific execution, including the workflow version details. 

### Filter runs by status

App (#app) 

In the **Runs** tab, use the filter chips at the top of the run list to filter by status. Available filters include the following: 

**Running** : Runs that are in progress. 

- **Needs Review** : Runs that are paused at a human-in-the-loop step awaiting review. 

**Completed** : Runs that finished successfully. 

- **Error** : Runs that encountered an error. 

**Date** : Filter runs by date range. 

To apply a filter, click a filter chip. To remove the filter, click the chip again. 

### Understand the run details

The following table lists and describes the information that is displayed in the **Runs** tab. 

|Field|Description|
|---|---|
|Input/Trigger|The trigger that started the run.|
|Status|The current state of the run, such as`Completed`,`Running`, or`Error`.|

Field Description Started The date and time when the run started. 

**Note:** Runs that reach a human-in-the-loop step display a **Needs Review** status. For more information, see Use human-in-the-loop steps (/gemini/enterprise/docs/workflow-builder/use-hitl-steps). 

### What's next

- Learn how to use human-in-the-loop steps (/gemini/enterprise/docs/workflow-builder/use-hitl-steps). 

- Learn how to manage workfow versionsl 

- (/gemini/enterprise/docs/workflow-builder/manage-agent-versions). 

- Learn how to set up event triggers 

- (/gemini/enterprise/docs/workflow-builder/configure-event-trigger). 

Last updated 2026-10-14 UTC. 



## Delete a workflow

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/delete-workflows

**Caution:** When you delete a workflow, it is permanently removed from your Gemini Enterprise web app and can no longer be used. Even though you might see your past conversations and runs in your history, you can't continue those sessions or recover the deleted workflow. 

To delete a workflow, do the following: 

App (#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app. 

4. Go to the **Your agents** section and locate the workflow that you want to delete. 

5. Click **Actions menu** , and select **Delete** . 

6. In the confirmation dialog, click **Delete** . 

### What's next

Learn how to create a workflow 

- (/gemini/enterprise/docs/workflow-builder/create-workflows). 



## Quotas and limits for Workflow Builder

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/quotas-and-limits

A _quota_ is a configurable or allocated limit on the amount of a resource you can use, such as daily agent creations or queries. For seat-based subscriptions, quotas are automatically adjusted based on the number of licenses your organization purchases. A _limit_ is a system constraint or capacity threshold, such as subagent depth, file upload size, or the number of individuals an agent can be shared with. System limits are fixed constraints, unless explicitly noted as an adjustable administrative setting. 

For information on overall Gemini Enterprise quotas, pooling across editions, and overage pricing, see Quotas and overages 

(/gemini/enterprise/docs/quotas-and-overages). 

**Workflow Builder limits at a glance:** 

- **Creation quotas** (#creation-quotas) **:** Frontline (0), Standard (1/user/day pooled), Plus (10/user/day pooled), Pay-as-you-go (unlimited). 

- **Agent capacity** (#agent-capacity-limits) **:** 1,000 agents per user; 10,000 agents per app instance (configurable by administrators). 

- **Sharing limits** (#sharing-limits) **:** 1,500 individual accounts per agent (IAM policy cap). Use Google Groups for larger audiences. 

- **Flow complexity** (#flow-limits) **:** Single-level subagent depth (1); maximum 50 subagents routed by chat root; maximum 100 nodes per flow. 

- **Knowledge base** (#knowledge-upload-limits) **:** 20 MB max file size; 100 files max per agent; 10 files per upload batch; 800,000 combined context tokens. 

- **Schedules** (#schedule-limits) **:** Multi-region only; 14-day credential validity; up to 5- minute execution latency. 

### Feature and edition-based quotas

Creating and running agents in Workflow Builder depends on your Gemini Enterprise edition. 

#### Daily creation quotas

Creating, drafting, and registering agents consumes a daily creation quota allocated by edition 

( `discoveryengine.googleapis.com/agents_tier_enterprise_regional` ). Daily creation quotas are pooled across all users with licenses for that edition within a specific project and location, and reset daily at midnight Pacific Time (PT). 

This daily creation quota applies to both: 

- Creating and drafting custom agents in Workflow Builder. 

- Registering external, custom, or partner agents (such as A2A agents (/gemini/enterprise/docs/register-and-manage-an-a2a-agent), ADK agents (/gemini/enterprise/docs/register-and-manage-an-adk-agent), or Dialogflow agents (/gemini/enterprise/docs/register-and-manage-a-dialogflow-agent)) with an app instance or engine using the Google Cloud console or the `agents.create` (https://cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locatio ns.collections.engines.assistants.agents/create) API. 

|Edition|Daily creation<br>quota|Description|
|---|---|---|
|Frontline<br>Worker /<br>Starter|0|Cannot create or register custom agents. Frontline licenses<br>provide 0 creation quota and don't contribute to the project's<br>pooled creation quota. Users can only run agents shared with<br>them.|
|Standard|1 agent per user<br>per day (pooled)|Pooled across all Standard edition licensed seats in the project<br>and location. For example, 100 licenses provide 100 creation<br>and registration operations per day for the project.|
|Plus|10 agents per<br>user per day<br>(pooled)|Pooled across all Plus edition licensed seats in the project and<br>location. For example, 100 licenses provide 1,000 creation and<br>registration operations per day for the project.|
|Pay-as-you-<br>go|Unlimited|No daily creation limits. Usage is billed according to underlying<br>resource consumption and query volume.|

**Important: Agent registration across multiple engines or apps** 

Agent registrations are scoped to an application instance (engine). If your architecture deploys a centralized or horizontally scaled agent backend registered across multiple Gemini Enterprise engines or apps in a project, each registration API call ( **`agents.create`** ) counts as an agent creation against the project's daily quota. 

If the number of registration calls in a day exceeds the number of distributed Standard licenses in the project, subsequent calls fail with **`HTTP 429 RESOURCE_EXHAUSTED: Agent creation quota exceeded`** . 

**Deployment recommendation:** If automated deployment scripts or CI/CD pipelines need to register an agent across many apps in a single project (for example, 60+ apps), ensure that an equivalent number of Standard licenses (for example, 60+ seats) are temporarily distributed to the project before initiating the rollout. Alternatively, pace automated registrations across daily quota reset windows. 

For more information about how quotas are pooled, calculated, and billed for overages across editions, see Quotas and overages 

(/gemini/enterprise/docs/quotas-and-overages#edition-quotas). 

#### Agent capacity limits

The following limits govern the number of active agents that can exist in an application instance: 

|Resource|Default<br>limit|Scope|Description|
|---|---|---|---|
|Agents per user|1,000|Per user<br>account|The maximum number of agents that a single<br>user can create and own.|
|Agents per<br>application|10,000|Per application<br>instance|The total maximum number of agents that can<br>exist across all users within an application|
|instance|||instance.|

**Note:** App administrators can adjust the per-user and per-instance agent limits in the application's feature control configurations 

### Sharing limits

When sharing an agent with colleagues in your organization, the following limits apply: 

|Setting|Limit|Description|
|---|---|---|
|Maximum|1,500 individual|The maximum number of individual user accounts|
|individual|accounts|that can be added directly to an agent's access list.|
|members per<br>agent||Enforced by Google Cloud IAM allow policies.|
|Google Groups<br>support|Unlimited total<br>members (1 group =<br>policy member)|1<br>Sharing with a Google Group counts as a single<br>member toward the 1,500-member policy limit.|

#### Sharing limit error behavior

If you attempt to share an agent with more than 1,500 individual user accounts, the operation fails and returns the following error: 

```
The number of members in the policy (1,501) is larger than the maximum allowed
size 1,500.
```

#### Best practices for sharing at scale

To share an agent with large audiences (such as team-wide, department-wide, or organization-wide distributions) without encountering the 1,500-member IAM limit: 

1. Request that your app administrator enable group sharing 

   - (/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls) in feature controls. 

2. In the agent sharing dialog, enter the email address of a Google Group or Workspace group (for example, `support-team@example.com` ) rather than individual user accounts. 

3. Manage audience membership dynamically within the Google Group; all group members automatically inherit access without modifying the agent's IAM policy. 

For step-by-step sharing instructions and permission levels, see Share a chat agent (/gemini/enterprise/docs/workflow-builder/share-chat-agent) and Share a workflow (/gemini/enterprise/docs/workflow-builder/share-workflows). 

### Flow builder complexity limits

The flow builder canvas enforces structural and routing constraints to maintain low execution latency, ensure deterministic orchestration, and prevent circular call graphs: 

|Constraint|Limit|Description|
|---|---|---|
|Subagent depth|1 level|Single-level flow depth only. Subagents cannot call<br>additional subagents. Nested multi-level hierarchies are not<br>supported.|
|Subagents routed by<br>chat root|<br>50 subagent|s The maximum number of subagents that a single chat root<br>agent can evaluate and route requests to.|
|Nodes per flow|100 nodes|The maximum total number of nodes (including trigger,<br>condition, action, subagent, and human-in-the-loop nodes)<br>allowed in a single workflow.|
|Skills per node|20 skills|The maximum number of tool skills or actions that can be<br>attached to a single flow node.|
|Simultaneous<br>subagent execution|1 subagent<br>a time|at<br>Workflow executions evaluate and run subagents<br>sequentially; parallel branch execution across multiple<br>subagents is not supported.|

### Knowledge base and file upload limits

The following limits apply to documents uploaded directly to an agent's knowledge base: 

|Resource|Limit|Description|
|---|---|---|
|Maximum file<br>size|20 MB<br>per file|The maximum size for an individual file uploaded directly to an<br>agent's knowledge base.|
|Maximum files<br>per agent|100 files|The maximum total number of files that can be attached to a single<br>agent.|
|Maximum files<br>per upload<br>batch|10 files|The maximum number of files that can be selected and uploaded in a<br>single operation.|
|Maximum<br>combined<br>context tokens|800,000<br>tokens|The maximum total token count across all static knowledge files<br>attached to an agent, files uploaded directly within a chat session,<br>and conversation history. Exceeding this token limit returns a`FILE_`<br>`SIZE_TOO_LARGE`or`Input too long`error, even if individual files are<br>under the 20 MB size limit.|

Supported PDF, DOCX, TXT, PPTX, CSV, XLSX, HTML, and Markdown (.md). document types 

#### Best practices for large documents and multi-sheet spreadsheets

When configuring knowledge sources or analyzing complex files in your agent, follow these guidelines to avoid context token limits and processing timeouts: 

- **Use a connected data store (RAG) for large static document libraries** : Gemini Enterprise loads files that you upload to an agent's **Knowledge** section in full into the model's prompt context on every turn. If you attach many files or dense PDFs (such as manuals over 100 pages), the combined token count can exceed the 800,000-token context limit or cause generation timeouts. Instead, ingest large static reference libraries into a connected Gemini Enterprise data store, which automatically chunks and indexes documents, and reserve direct file uploads for smaller, session-specific files. 

- **Split dense PDFs for direct uploads** : Because Gemini Enterprise tokenizes each page of a PDF alongside its text and visual layout, a single multihundred-page PDF can consume a large portion of the session token budget 

and increase reasoning latency. When uploading PDFs directly to an agent or chat session, split large documents into smaller, topic-specific files. 

- **Multi-sheet Excel** **(** **`.xlsx` ) workbooks** : When you upload a multi-sheet `.xlsx` workbook to an agent's **Knowledge** section or in a chat session, Gemini Enterprise automatically converts each worksheet into an individual CSV table for Python code execution so the agent can query, join, and analyze data across all sheets in the workbook. 

#### Storage capacity

Uploaded files and indexed documents consume storage from your organization's storage capacity pool. Storage is pooled across all users in a project and location, regardless of edition: 

- **Frontline Worker / Starter:** 2 GiB per user. 

- **Standard:** 30 GiB per user. 

- **Plus:** 75 GiB per user. 

If total stored content exceeds the combined pool for your licensed seats, Google bills overages at $5 per GiB per month. For more details, see Storage and data indexing quota (/gemini/enterprise/docs/quotas-and-overages#storage-quotas). 

### Execution schedule limits

The following limits and operational constraints apply to automated agent schedules: 

|Setting|Limit or constrain|tDescription|
|---|---|---|
|Location<br>support|Multi-region only|Agent execution schedules are supported only in multi-region<br>deployments (such as`us`or`eu`).|
|Recurrence|Hourly, Daily,|Configurable intervals for automated execution triggers.|
|frequencies|Weekly, Monthly,<br>Annually||

|Setting|Limit or constraint|Description|
|---|---|---|
|Credential<br>validity window|<br>14 days|Scheduled agents execute using the author's delegated user<br>credentials. Credentials expire every 14 days and must be<br>manually refreshed in Gemini Enterprise to prevent<br>schedules from pausing.|
|Execution<br>timing latency|Up to 5 minutes<br>delay|Scheduled runs may experience a scheduling delay of up to<br>5 minutes depending on system queue load.|
|Approval<br>pausing (HITL)|Mandatory pause<br>on external<br>actions|Scheduled runs that perform actions affecting other<br>individuals (such as sending emails or scheduling meetings)<br>automatically pause for review and require user approval in<br>chat history.|

For instructions on configuring or refreshing schedules, see Schedule a chat agent run (/gemini/enterprise/docs/workflow-builder/schedule-chat-agent). 

### Connected data sources and integration limits

The following limits apply to connected data stores and third-party integrations: 

|Resource|Default<br>limit|Description|
|---|---|---|
|Data stores<br>per<br>application|100 data<br>stores|The maximum number of connected enterprise data stores per<br>application instance. Can be increased up to 500 by submitting a<br>quota increase request<br>(/docs/quotas/view-manage#requesting_higher_quota).|
|Connectors<br>per agent|100<br>connectors|The maximum number of third-party data connectors attached to a<br>single agent.|
|MCP servers<br>per agent|100 server|sThe maximum number of Model Context Protocol (MCP) servers<br>linked to an agent.|
|Skill agents<br>per agent|100 skills|The maximum number of modular skill agents referenced by an<br>agent.|

### What's next

- Create a workflow (/gemini/enterprise/docs/workflow-builder/create-workflows): Build custom workflows using the flow builder canvas. 

- Share a chat agent (/gemini/enterprise/docs/workflow-builder/share-chat-agent) and Share a workflow (/gemini/enterprise/docs/workflow-builder/share-workflows): Manage access permissions and share agents with team members or Google Groups. 

- Schedule a chat agent run 

- (/gemini/enterprise/docs/workflow-builder/schedule-chat-agent): Configure automated hourly, daily, or weekly recurrence triggers. 

- Quotas and overages (/gemini/enterprise/docs/quotas-and-overages): Review organization-wide pooled query quotas, storage indexing limits, and overage billing for Gemini Enterprise. 

Last updated 2026-10-14 UTC. 



## Known issues and limitations

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/known-issues

This page lists the known issues and limitations for Workflow Builder in this release. 

### Known issues

This section lists known issues in Workflow Builder. 

#### Natural language support

|Status|OPEN|
|---|---|
||The conversational designer does not support adding the following<br>capabilities using natural language prompts:<br>Human-in-the-loop (HITL) approvals|
|Issue|Event triggers<br>Data filtering<br>To create workflows with these capabilities, you can use the UI to add these<br>nodes to your workflow manually.|
|Workaround or<br>recommendation<br>Natural Lan|N/A<br>guage reliability|
|Status|OPEN|
|Issue|Creating a workflow from natural language may occasionally result in a<br>workflow that cannot run.|
|Workaround or<br>recommendation|Try generating the workflow again if the first attempt fails.|

#### Runs tab loading failures

|Status|OPEN|
|---|---|
|Issue|Intermittent failures may occur when loading sessions in the Runs tab.|
|Workaround or|If sessions fail to load, try refreshing the page.|
|recommendation||

#### Connectors not showing after authorization

OPEN Status A connector might not show up in the UI or work using natural language Issue immediately after being authorized. Perform a hard reload of your browser: Workaround or Windows/Linux: `Ctrl + Shift + R` or `Ctrl + F5` recommendation macOS: `Command + Shift + R` 

#### Execution timeouts under heavy load

OPEN Status Workflows may experience "Failed to build node" errors or timeouts during Issue execution when the system is under heavy load. Workaround or Ensure only necessary connectors are enabled for the agent to reduce load. recommendation 

#### Disabled actions failure

|Status|OPEN|
|---|---|
|Issue|Attempting to use actions (like sending an email) that are not enabled in your<br>environment results in execution failure.|

Workaround or Ensure required actions are enabled before running the workflow. recommendation 

#### Disable actions failure

OPEN Status Workflow failed to prompt the user to enable necessary actions for workflow Issue creation. Workaround or N/A recommendation 

#### Model recommendation

|Status|OPEN|
|---|---|
|Issue|For optimal performance and best results, we recommend using the 3.1 Pro<br>model.|
|Workaround or|N/A|
|recommendation||

#### Approval node formatting

|Status|OPEN|
|---|---|
|Issue|HTML and Markdown formatting in human-in-the-loop (HITL) approval steps<br>may display as raw text when added as a sub-step.|
|Workaround or|N/A|
|recommendation||

#### Event-triggered workflows failing with RESOURCE_EXHAUSTED

|Status<br>OPEN|
|---|

Event-triggered workflows failing with a `RESOURCE_EXHAUSTED` error (generally Issue seen when a daily quota is breached) are not retried automatically. Workaround or N/A recommendation 

#### Connector search records returned by connector type

OPEN Status Connector search tools return a specific number of records depending on the Issue connector type, such as Jira or Outlook. Workaround or N/A recommendation 

#### OAuth re-run required for A2A and ADK agents

OPEN Status If you add an A2A or ADK agent that requires user OAuth for authentication, Issue continuing the same run after the OAuth flow is complete is not supported. Workaround or The user must first authenticate, and then start a new run of the workflow. recommendation 

### Limitations

- The Gmail subject field does not support non-English characters. 

- Connector actions that list entities (for example, retrieving emails) might not return all items when the total number is very large. This is because the connector's API is limited to fetching a finite number of pages, with a default page size of 20. Items beyond the capacity of the maximum pages fetched are not retrieved. 

#### Add an existing agent step

The Add an existing agent step 

(/gemini/enterprise/docs/workflow-builder/add-existing-agents#add-existing-agent) feature has the following limitations: 

- **Clarifying questions support** : Existing agent steps support asking clarifying questions during workflow execution when using native protocol signals (such as A2A `input-required` or ADK `RequestInput` ) . Other workflow step types do not use prompt-based clarifying questions. 

- **Supported agent types** : Only agents created with the Agent Development Kit (ADK) (/gemini/enterprise/docs/register-and-manage-an-adk-agent) and Agent-toAgent (A2A) registered agents 

- (/gemini/enterprise/docs/register-and-manage-an-a2a-agent) are supported. 

Last updated 2026-10-14 UTC. 



## Get reports with Deep Research

URL: https://docs.cloud.google.com/gemini/enterprise/docs/research-assistant

Deep Research is a Made by Google agent for users who need to gather, analyze, and understand internal and external information. 

**Note:** Made by Google agents aren't available in the Gemini Enterprise Frontline edition. 

### Overview

When you enter a prompt to Deep Research, such as "Compare Example Project competitors", Deep Research assesses whether the question is research related, generates a plan outlining the steps it takes to do the research, and streams questions and answers as it progresses in its research. It then generates a report of its findings with citations as well as an audio summary. 

For research sources, Deep Research uses data that the app indexes. It can also use web results if web search is enabled for the app. 

Here are some example prompts that Deep Research generates reports for: 

- How can we improve the user experience of our existing mobile banking app to make it more intuitive and user-friendly? 

- How can we reduce customer wait times during peak hours without compromising on the quality of support? 

- Analyze the economic situation of Central European countries. 

- Compare BigQuery with its competitors, and provide the results in table format. 

### Use Deep Research

Your end users can access and use Deep Research through the app. Deep Research has access to data that the app has already indexed and, if enabled, web results. 

You can get results from Deep Research from the app or using the API (Generally available with an allowlist). 

ConsoleREST (#rest) (#console) 

To use Deep Research in the app, do the following: 

1. In the app navigation menu, go to **Deep Research** . 

2. Click **Sources** to select the sources that the agent must include to provide the most relevant data insights. 

In the sources, in addition to your Gemini Enterprise sources, you can also choose to include Google Search results. 

3. Enter a prompt to Deep Research and click **Submit** . If the prompt isn't research-related, Deep Research generates an answer. If the prompt is determined to be research-related, then Deep Research outlines the topics that the agent plans to research in a research plan. 

4. Edit the agent's prompt, if necessary, to generate a new research plan that better suits your requirements. 

5. If the research plan is acceptable to you, click **Start Research** . 

   - The agent starts researching based on the plan: 

      - Streams the topics that it's researching as it progresses 

      - Generates a report of findings with citations 

      - Creates a 1-2 minute audio summary of the report 

Last updated 2026-10-14 UTC. 



## Core Assistant agent

URL: https://docs.cloud.google.com/gemini/enterprise/docs/core-assistant

Core Assistant is the Google-provided ("Made by Google") agent that handles interactions when users talk to the Gemini Enterprise engine without specifying any other agent. 

Core Assistant includes monitoring and observability for tracing and monitoring of operations with user interactions and agent activity. It provides comprehensive observability into execution flow, performance, and usage metrics. 

The Core Assistant agent is available automatically with Gemini Enterprise. 

**Note:** Made by Google agents aren't available in the Gemini Enterprise Frontline edition. 

Key characteristics of Core Assistant: 

- **Google-managed** : Entirely maintained and managed by Google; you cannot edit its configuration or change the charts and data shown. 

- **Always available** : Automatically provisioned and runs out of the box for Gemini Enterprise agents. 

**Access** : Viewable through the Google Cloud console. 

Through Core Assistant, you can access two primary observability tabs with details of your AI operations: **Traces** and **Metrics** . 

### Prerequisites

Before you begin using Core Assistant, ensure you have the following: 

- The Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role or Google Cloud console Gemini Enterprise User role. 

An existing Gemini Enterprise app configured. 

- For **Traces** functionality, you must turn on OpenTelemetry traces and logs in your observability settings and have the Cloud Trace User role 

- ( `roles/cloudtrace.user` ). For more information, see Manage observability settings (/gemini/enterprise/docs/manage-observability-settings). *Note: The **Metrics** functionality is default ON and does not require manual configuration or trace enablement.* 

### The Traces tab

The **Traces** tab in Core Assistant provides a chronological summary of trace records showing parent-child execution span details ( `Agent to Tool` , `Invoke Agent` , and `Agent to Model` actions, including `execute_tool` and `invoke_connector` operations). These records help inspect runtime execution flows, inputs, outputs, and locate latent issues. 

Traces inside Core Assistant persist for **30 days** and require OpenTelemetry traces to be turned on. 

For a detailed breakdown of all the fields, visual workflows (graphs and timelines), and metrics logs display in the Traces tab, see Access traces for agents 

(/gemini/enterprise/docs/access-traces-and-spans#access-traces-for-agents). 

### The Metrics tab

The **Metrics** tab provides an operational overview dashboard summarizing sessions, count of agent invocations, traffic, error rates, and detailed connections of tools usage. 

Metrics inside Core Assistant persist for **6 weeks** (42 days), are default ON, require no configuration, and incur no extra billing costs. 

For a comprehensive breakdown of each metric dashboard (Overview metrics dashboard and connected Tools latency metrics), see Access metrics for agents (/gemini/enterprise/docs/access-metrics#access-metrics-for-agents). 

Last updated 2026-10-14 UTC. 



## Accelerate research and development with Co-Scientist agent

URL: https://docs.cloud.google.com/gemini/enterprise/docs/co-scientist-and-alphaevolve

**Preview** 

These features are Generative AI Preview offerings, subject to the "Pre-GA Offerings Terms" of the Google Cloud Service Specific Terms (https://cloud.google.com/terms/service-terms). For these Generative AI Preview offerings, Customers may elect to use them for production or commercial purposes, or disclose Generated Output to third-parties, and may process personal data as outlined in the Cloud Data Processing Addendum 

(https://cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. 

The AI/ML Data Location terms also apply to Co-Scientist, as an Agentic AI Service on Gemini Enterprise, subject to its restrictions and those listed in the Google Cloud Platform Services with Data Residency (https://cloud.google.com/terms/data-residency) page. 

Co-Scientist and AlphaEvolve are Google-developed agents that accelerate research and development processes. These agents leverage Gemini to automate complex scientific reasoning and algorithmic discovery. 

**Note:** Access to these agents is restricted. To request access, contact your Google account team. Your account team provides detailed product documentation once they grant access. 

### Overview of Co-Scientist agent

Co-Scientist is a multi-agent AI system built on Gemini, designed to act as a virtual scientific collaborator. The system helps researchers uncover original knowledge and formulate novel research hypotheses and experimental proposals. By combining AI reasoning with the scientific method, Co-Scientist enables scientists to navigate literature, synthesize insights across domains, and accelerate biomedical discoveries. 

#### How it works

Co-Scientist is built on a multi-agent architecture and an asynchronous task execution framework to scale test-time computation. This design allows the system to reason, debate, and improve outputs iteratively. 

When you provide a research goal in natural language, Co-Scientist coordinates the following specialized agents: 

- **Generation agent:** Explores literature using web search, synthesizes findings, and formulates initial hypotheses. 

- **Reflection agent:** Acts as a peer reviewer to examine the correctness, quality, and safety of generated hypotheses. 

- **Ranking agent:** Evaluates and prioritizes research proposals using an Elobased tournament. 

- **Evolution agent:** Refines top-ranked hypotheses by grounding them in literature and combining innovative ideas. 

- **Proximity agent:** Organizes tournament matches and deduplicates hypotheses using a proximity graph. 

- **Meta-review agent:** Synthesizes insights from all reviews and debates into a comprehensive research roadmap. 

A dedicated **Supervisor agent** orchestrates the process, allocates resources, and manages the worker queue to maintain a self-improving loop of scientific reasoning. 

#### Use cases

Co-Scientist solves complex problems across multiple scientific disciplines, specifically those requiring deep subject matter expertise and trans-disciplinary insights. Example use cases include: 

- **Drug repurposing:** Identify novel therapeutic indications for approved drugs by analyzing molecular signatures, signaling pathways, and literature-based information. 

- **Target discovery:** Propose new biological components and epigenetic targets for complex diseases and streamline hypothesis selection for experimental validation. 

- **Mechanistic explanations:** Generate hypotheses for intricate problems, such as antimicrobial resistance, by synthesizing fragmented scientific data. 

For more information and additional use cases, see the Accelerating scientific breakthroughs with an AI Co-Scientist 

(https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/) blog. 

Last updated 2026-10-14 UTC. 



## Create and manage projects

URL: https://docs.cloud.google.com/gemini/enterprise/docs/projects

In Gemini Enterprise, you can use projects to build a dedicated knowledge base for your own work or to collaborate with your team. Within a project, you can upload documents and chat privately with the assistant to get answers grounded in your project documents and web search. 

Project knowledge documents can include: 

- **Uploaded files** : Local files in the following formats are supported: PDF, Microsoft Word (DOCX), Microsoft PowerPoint (PPTX), Microsoft Excel (XLSX), CSV, HTML, and plain text (TXT). 

- **Google Drive files** : Google Docs, Google Slides, PDFs, or other supported file types linked directly from Google Drive. 

- **Notes** : Text notes pasted or typed directly into the project. 

- **External data connectors** : Files from third-party sources, such as Microsoft SharePoint, if enabled by your administrator. 

### Before you begin

- Ensure that a Gemini Enterprise administrator has turned on the **Enable projects** toggle in the web app feature management settings. For more information, see Manage web app features 

- (/gemini/enterprise/docs/manage-web-app-features). 

- If you want to link Microsoft SharePoint files to your projects, ensure that a Gemini Enterprise administrator has configured the SharePoint connector data store in the Google Cloud console. For instructions, see Connect a third-party data source (/gemini/enterprise/docs/connectors/connect-third-party-data-source). 

### Limitations

The following limitations apply when adding documents to your project's knowledge base: 

- A project can include up to 50 files and linked documents in its knowledge base. 

- Linking Google Drive files or folders, or files from data connectors to a project doesn't change their original sharing permissions. To allow other project members to use these files, you must share them in the source application (such as Google Drive or SharePoint). Project members must have at least view access to the files. 

- When viewing the **Knowledge** tab, members only see the files and documents that they have permission to access. Members cannot view the names of files they don't have access to, and Gemini Enterprise only uses accessible files when generating answers for their chats. 

- Unlike files linked from Google Drive or external connectors, all locally uploaded files are visible, downloadable, and can be deleted by all project members. 

### Create a project

- To create a project in the Gemini Enterprise web app: 

   1. Sign in to the Gemini Enterprise web app. 

   2. In the navigation menu, click **Projects** . 

   3. Click **New project** (or **Get started** if this is your first project). 

   4. Enter a name for your project and click . 

   5. In the **Welcome** tab, enter a description, and then click **Done** . 

### Manage project knowledge

The **Knowledge** tab defines the context boundary for conversations within the project. Within that boundary, theGemini Enterprise assistant answers queries using your project documents and web search for external web context, while remaining isolated from other enterprise data sources unless they are explicitly added to the project. 

To upload documents to your project: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Projects** . 

3. From the list of projects, click the project name and then select the **Knowledge** tab. 

4. To upload content, click the **Upload** icon. 

5. Choose one of the following upload options: 

   - **Upload files** : Select local files to upload. 

   - **Google Drive** : Connect with Google Drive and select the files or folders to link. 

   - **SharePoint** : Authorize the project's access to your linked SharePoint documents and folders. 

   - **Notes** : Paste your text or type it directly into the editor, and click **Add text** . 

Linked documents sync in real time. Any changes to file content or original sharing permissions sync automatically with the project. 

### Chat with assistant

You can chat with Gemini Enterprise to get answers to your project questions. These chats are private; only you can see them. Other project members can't view or join your chats. 

To chat with the assistant in a project: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Projects** . 

3. From the list of projects, click the project you want to chat in. 

4. In the **New chat** tab, enter your question or prompt in the chat box, and press **Enter** (or click ). 

When you chat in a project: 

- Responses are grounded in the project's **Knowledge** files and web search. You can create multiple different chats in the same project. 

### Invite users to a project

To invite users to your project: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Projects** . 

3. From the list of projects, click the project that you want to share. 

4. In the **Team** tab in your project, click **Add** . 

5. In the **Share project** dialog, enter the email addresses of the users you want to invite (separated by commas), and click **Done** . By default, invited members receive Editor permissions. 

You can also share using one of the following methods: 

- Click **Invite** from the **Team** , **Knowledge** , or **New chat** tabs to invite members from anywhere within your project. 

- In the **Team** tab, select users from **Suggested people** to quickly add them to your project. 

**Note:** Only the project owner can invite new members. Invited members receive Editor permissions. 

### Remove a user from a project

To remove a user from your project: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Projects** . 

3. From the list of projects, click the project you want to manage. 1 Select the **Team** tab. 

4. For the user you want to remove, in the **Role** column click the role assigned to the user and click **Remove access** . 

**Note:** Only the project owner can remove members from a project. 

### Delete a project

To delete your project: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Projects** . 

3. Next to the project that you want to delete, click and click **Delete** . 

4. When prompted, confirm the deletion. 

**Note:** Only the project owner can delete a project. 

Last updated 2026-10-14 UTC.
