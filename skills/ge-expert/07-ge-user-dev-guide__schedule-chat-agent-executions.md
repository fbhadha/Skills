# Gemini Enterprise: user guide, Workflow Builder, developer guide / Schedule chat agent executions to Use workflow templates
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 89-129, extracted 2026-10-18

Contains:
- Schedule chat agent executions (pages 89-94) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent
- Edit a chat agent (pages 95-97) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent
- Share a chat agent (pages 98-103) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent
- Delete a chat agent (pages 104-105) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/delete-chat-agent
- Workflows overview (pages 106-121) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows
- Create a workflow (pages 122-124) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows
- Create a workflow with natural language (pages 125-127) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-natural-language
- Use workflow templates (pages 128-129) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-agent-templates

## Schedule chat agent executions

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent

You can configure your chat agent to execute tasks automatically on a recurring basis. A schedule serves as an automated trigger for the agent's predefined instructions or prompts. 

**Note:** Execution schedules are only supported for non-workflow chat agents. 

**Note:** Scheduled chat agents run automatically for personal tasks, such as creating your own calendar invites or emailing yourself. However, scheduling agents is not supported for actions involving other people. 

### Add an execution schedule

App 

(#app) 

To add an execution schedule for your chat agent, do the following: 

1. Open your agent in edit mode 

   - (/gemini/enterprise/docs/workflow-builder/edit-chat-agent#open-edit-mode). 

2. In the chat agent builder canvas, click the **Schedule** tab. 

3. Click **+ Add schedule** and configure the recurrence and execution time: 

      - a. **Repeat frequency:** select how often the agent should run to execute the provided prompt. The following options are available: 

         - **Hourly:** runs the task every specified number of hours and at a specific minute within that hour. 

         - **Daily:** runs the task once per day at the specified time. 

         - **Weekly:** runs the task once per week on the specified day and time. 

      - **Monthly:** runs the task once per month on the specified day of the month and time. If a month doesn't have this day, the agent won't trigger. For example, if you enter `30` here, the agent won't trigger in February. 

      - **Annually:** runs the task once per year on the specified month, day, and time. 

   - b. **Execution time and timezone:** define the specific interval settings based on your selected frequency and select the execution timezone. 

   - c. **Execution time and time zone:** define the specific interval settings based on your selected frequency and select the execution time zone. 

   - d. **Prompt:** enter the specific prompt (or instruction) the agent will receive at the scheduled time. This defines the task the chat agent will execute. 

4. Click **Save** to create the schedule and add it to your agent in a **Draft** state. 

5. Optional: Test your schedule (#test-schedule) to verify if it functions as expected. 

6. To activate your schedule and relaunch your chat agent with the updated changes, click **Update** . 

### Test the execution schedule

After configuring a schedule, you can immediately test the chat agent's execution to ensure it performs the task as expected without waiting for the next scheduled interval. 

App 

(#app) 

To test the execution schedule, do the following: 

1. In the chat agent builder canvas, click the **Schedule** tab. 

2. Find the schedule card that you want to test and click **Run in preview** . 

This triggers the chat agent using the saved prompt and configuration. 

### Edit an execution schedule

Edit an execution schedule to make changes to the frequency, time, time zone, or prompt. 

App 

(#app) 

To edit an existing execution schedule, do the following: 

1. In the chat agent builder canvas, click the **Schedule** tab. 

2. Find the schedule card that you want to test and click **Edit** . 

3. Modify the **Repeat Frequency** , **Run Time** , **Time Zone** , and the **Prompt** as selected. 

4. Click **Save** . 

5. Click **Update** to ensure all changes, including the new schedule, are saved and applied to the chat agent. 

### Delete an execution schedule

If a recurring task is no longer needed, you can delete and remove it from the **Agent Schedules** list. 

App 

(#app) 

To delete an execution schedule, do the following: 

1. In the chat agent builder canvas, click the **Schedule** tab. 

2. Find the schedule card that you want to test and click **Delete** . 

3. Confirm the deletion to permanently remove the execution schedule for your chat agent. 

### Refresh chat agent schedules

Chat agent schedules operate using your user credentials. To ensure data privacy and security, these credentials expire every **14 days** . You must manually refresh your chat agent schedules to ensure they continue to run automatically without interruption. 

App 

(#app) 

To refresh schedules for all your chat agents, do the following: 

1. Open your Gemini Enterprise web app and go to the **Agent Gallery** page. 

2. Perform one of the following actions to refresh your schedules: 

   - Go to the **Your agents** section and click ( **Refresh the existing schedules** ). 

Open the chat agent in edit mode 

(/gemini/enterprise/docs/workflow-builder/edit-chat-agent#open-edit-mode) and do the following: 

- a. In the chat agent builder canvas, click the **Schedule** tab. 

- b. Click **Refresh schedules** . 

Your user credentials are refreshed, and all scheduled chat agents will continue to run for another 14-day period. 

### View and approve scheduled runs

All scheduled runs, including those waiting for approval, are listed in your chat history. 

App (#app) 

To view and approve scheduled runs, do the following: 

1. Open your Gemini Enterprise web app and go to the **Chats** section in the navigation menu. 

2. Find and open the conversation thread corresponding to your scheduled chat agent. 

3. If the scheduled run is paused, review the proposed action and click **Approve** to complete the task. 

### Limitations

- You must manually refresh your schedules every 14 days to prevent your scheduled chat agents from failing. 

- A maximum delay of 5 minutes is expected when executing a chat agent schedule. 

Schedules are only supported in multi-region locations. 

### What's next

- Learn how to use a chat agent 

- (/gemini/enterprise/docs/workflow-builder/use-chat-agent). 

- Learn how to edit a chat agent 

- (/gemini/enterprise/docs/workflow-builder/edit-chat-agent). 

- Learn how to share a chat agent 

- (/gemini/enterprise/docs/workflow-builder/share-chat-agent). 

- Learn how to delete a chat agent 

- (/gemini/enterprise/docs/workflow-builder/delete-chat-agent). 

Last updated 2026-10-14 UTC. 



## Edit a chat agent

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent

You can update or modify your chat agent using the conversational chat interface or the visual flow builder. 

### Open chat agent in edit view

To begin editing any part of your chat agent, you must first open it in edit view: 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

The **Agent Gallery** page appears displaying all the prebuilt agents and custom-built agents. 

3. Go to the **Your agents** section, find the chat agent you want to edit. 

4. Click **Actions menu** and select **Edit** . 

The chat agent opens in edit view. 

### Edit agent details and subagent logic

You can edit your chat agent's logic, instructions, and configuration in two ways: 

Use the chat pane for conversational, no-code updates (#edit-using-chat) Use the flow builder for manual control (#edit-using-flow) 

**Important:** The main agent node stores the overall details of your chat agent. Editing the main node details (name, description, instructions) will also update the overall details for 

#### Edit using conversational chat

Use the chat pane of the canvas to use Gemini AI and update your chat agent's instructions or behaviors. 

App 

(#app) 

1. In the left chat pane, enter a prompt detailing the changes you want to make to the agent's function or behavior. 

Example prompt: `Change the main agent's model to Gemini-2.5-flash and` 

```
update its instructions to be more direct.
```

Gemini updates the agent logic and instructions based on your prompt. 

2. Click the **Preview** tab and interact with the agent to verify and evaluate the changes. 

3. Click **Update** to save and relaunch the chat agent. 

#### Edit using the flow builder

Use the **Flow** tab to visually edit the chat agent flow, Gemini model, data sources, and instructions for the main agent node or any subagents nodes. 

App 

(#app) 

To edit the main agent node, do the following: 

1. In the Workflow Builder canvas, click the **Flow** tab. 

2. Click the main agent node to open its details pane. 

3. Edit the agent's **Name** , **Gemini model** , **Description** , **Instructions** , and **Data sources** . 

4. You can also add or remove subagents from this pane. 

**Warning:** Removing a subagent may disrupt your agent's flow and control logic. 

5. Click **Update** to save and relaunch the agent. 

To edit a subagent node, do the following: 

1. In the Workflow Builder canvas, click the **Flow** tab. 

2. Click the subagent node that you want to edit. 

3. Edit the subagent **Name** , **Gemini model** , **Description** , **Instructions** , and **Data sources** . 

4. Click **Update** to save and relaunch the chat agent. 

### What's next

- Learn how to use a chat agent 

- (/gemini/enterprise/docs/workflow-builder/use-chat-agent). 

- Learn how to schedule chat agent runs 

- (/gemini/enterprise/docs/workflow-builder/schedule-chat-agent). 

- Learn how to share a chat agent 

- (/gemini/enterprise/docs/workflow-builder/share-chat-agent). 

- Learn how to delete a chat agent 

- (/gemini/enterprise/docs/workflow-builder/delete-chat-agent). 

Last updated 2026-10-14 UTC. 



## Share a chat agent

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent

Share the chat agents that you've created and launched using Workflow Builder with other users within your organization. Depending on your web app's feature control configurations 

(/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls), you might need an Gemini Enterprise app administrator to review and approve 

(#review-request) to share a chat agent. 

**Caution:** When you share an agent, consider the following data access behaviors: 

- **Knowledge files:** Any user with access to the shared agent can query and view information from files uploaded to the agent's **Knowledge** section, even if they don't have direct access or permissions to the source files. For example, if you upload a confidential file to the **Knowledge** section, all users with access to the shared agent can ask questions about that file's content. 

- **Connectors and data stores:** When an agent accesses data through connectors, user access control lists (ACLs) and permissions are preserved. Users can only query and retrieve data from data stores and connectors that their individual user accounts are authorized to access. 

## Share a chat agent

To share a chat agent, do the following: 

App 

(#app) 

1. Open your Gemini Enterprise app and go to the **Agent Gallery** page. The **Agent Gallery** page appears displaying all the prebuilt agents and custom-built agents. 

2. In the **Your Agents section** , find the chat agent that you want to share. 

**Note:** You can't share a chat agent that is in a **`draft`** state. 

3. Click **Actions menu** , and select **Share** . 

4. In the share dialog, enter the email addresses of the users you want to share the agent with. You can also click **Copy link** to generate a shareable link. 

**Notes:** 

You can share your chat agent with individual user email addresses. Sharing with Google Groups isn't supported. 

If your web app is connected to a People Search data store (/gemini/enterprise/docs/connectors/connect-people#create) with autocomplete (/gemini/enterprise/docs/configure-autocomplete) configured for user data, the share dialog provides autofill suggestions as you enter user email addresses. 

5. Click **Done** . 

The chat agent is shared with the users in your access list. 

**Note:** If your web app administrator has enabled administrator review for agent sharing, a share request is sent to the app administrator for review and approval. After the app administrator approves the request, the chat agent is shared with the users in the access list. You can, at any time, edit the share request to add or remove users, or cancel the request. 

### Administrator review control

By default, agent owners can share their agents with any user within their organization without approval from an app administrator. However, app administrators can change the app feature control confgurationsi 

(/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls) to require administrator review and approval for sharing agents in the app. 

Agent sharing follows a two-step process when administrator review is enabled: 

1. The agent owner shares the agent (#share-agent) with one or more users. 

2. The app administrator reviews the sharing request (#review-request) and approves or denies it. 

#### Review a share request

App administrators are responsible for reviewing and managing agent sharing requests. 

**Notes:** 

- This section only applies if the **Enable agent sharing without admin approval** feature is disabled in the app's feature controls. 

- Only app administrators with the Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) IAM role can review and approve share requests. 

Console 

(#console) 

To review a share request as an app administrator, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Apps** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app containing the agent. 

3. In the app navigation menu, click **Agents** . 

4. Find the agent with a **Review share request** action in the **User permissions** column. 

5. Click **Review share request** . 

6. In the **Share request** pane: 

   - Review the access list under **Requested to share with the following users** . 

   - Optional: Modify the access list to add or remove user accounts, Google groups or Workforce Identity Federation (WIF) identity pools. 

7. To approve the request and grant access, click **Approve and enable** . 

8. To reject the request, click **Deny** . 

### Sharing limits

When sharing a chat agent, the following limits apply: 

- **Maximum 1,500 individual accounts:** Gemini Enterprise manages agent access using underlying Google Cloud IAM allow policies, which enforce a hard cap of 1,500 members per policy. Sharing an agent with more than 1,500 individual user accounts causes the operation to fail with the following error: 

```
The number of members in the policy (1,501) is larger than the maximum
allowed size 1,500.
```

For a full list of system constraints, see Workflow Builder quotas and limits 

(/gemini/enterprise/docs/workflow-builder/quotas-and-limits). 

### Considerations

- When you share a chat agent, users can query the content of files uploaded to the **Knowledge** section regardless of direct file access, while data accessed through connectors continues to respect individual user permissions and Access Control Lists (ACLs). 

- App administrators can add and remove users from the access list at any time. 

- Only app administrators can share the agent with Google groups and Workforce Identity Federation (WIF) identity pools in your organization. 

- Agent owners can remove any user from the access list at any time (including those added by the app admin). 

- App administrators can transfer ownership of a shared chat agent to another user or to themselves in the Google Cloud console. For more information, see Transfer agent ownership 

- (/gemini/enterprise/docs/share-custom-agents#transfer-ownership). 

You can also share a chat agent from the chat agent builder canvas. 

### What's next

- Learn how to use a chat agent 

- (/gemini/enterprise/docs/workflow-builder/use-chat-agent). 

- Learn how to schedule chat agent runs 

- (/gemini/enterprise/docs/workflow-builder/schedule-chat-agent). 

- Learn how to edit a chat agent 

- (/gemini/enterprise/docs/workflow-builder/edit-chat-agent). 

- Learn how to delete a chat agent 

- (/gemini/enterprise/docs/workflow-builder/delete-chat-agent). 

- View Workflow Builder quotas and limits 

- (/gemini/enterprise/docs/workflow-builder/quotas-and-limits). 

Last updated 2026-10-14 UTC. 



## Delete a chat agent

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/delete-chat-agent

You can delete the entire chat agent or remove individual main or subagent nodes from within the Workflow Builder. 

### Delete the entire chat agent

**Warning:** When you delete a chat agent, it is permanently removed from your Gemini Enterprise web app and can no longer be used. Even though you might see your past conversations in your history, you can't continue those sessions or recover the deleted chat agent. 

App 

(#app) 

To delete the entire chat agent, do the following: 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

The **Agent Gallery** page appears displaying all the prebuilt agents and custom-built agents. 

3. For the chat agent you want to delete, click **Actions menu** and select **Delete** . 

4. Confirm your decision to permanently delete the chat agent. 

Your chat agent is deleted and removed from your Gemini Enterprise web app. 

### Delete a main agent node or a subagent node

You can remove a main agent node or a subagent node from your chat agent's flow using the Workflow Builder **Flow** tab. 

**Note:** Deleting the main agent node will automatically delete all connected subagent nodes. 

App 

(#app) 

To delete a main agent or a subagent node, do the following: 

1. Open your Gemini Enterprise web app and go to the **Agent Gallery** page. 

2. For the chat agent that contains the main agent or the subagent nodes that you want to delete, click **Actions menu** and select **Edit** . 

3. In the Workflow Builder canvas, click the **Flow** tab. 

4. Click the main agent or the subagent node that you want to delete. 

5. In the main agent or subagent node details pane, click **Delete** . 

6. Confirm your decision to permanently delete the main agent or subagent node. 

7. Click **Update** to save and relaunch the chat agent. 

### What's next

Learn how to create a chat agent 

- (/gemini/enterprise/docs/workflow-builder/create-chat-agent). 

Last updated 2026-10-14 UTC. 



## Workflows overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/workflows

**Workflows** are agents that you can build using Workflow Builder 

(/gemini/enterprise/docs/workflow-builder) in your Gemini Enterprise web app. These agents are designed to execute a sequence of steps or actions, which can include a mix of AI automation and human intervention, based on a configured trigger. Workflow responses can be deterministic or non-deterministic based on the overall orchestration logic of the agent. 

Workflows are ideal for the following use cases: 

- **Multi-step processes** with defined sequence logic. For example, automating an employee onboarding checklist across tools like Gmail and Calendar. 

- Tasks with AI automation and human approvals. For example, drafting a report with AI that requires a user **sign-off** before publishing. 

- Complex orchestrations with conditional logic. For example, routing sales leads to different teams based on region and budget. 

The following features are available in Workflow Builder: 

- **Create a workflow with natural language** : Describe your workflow in plain language and generate a workflow scaffold automatically. 

- **Use workflow templates** : Browse and start from prebuilt templates for common business use cases. 

- **Set up workflow triggers** : Run workflows automatically when data changes in connectors. 

- **Connect connectors to agent steps** : Enable read and write-back tools (such as Gmail, Jira, and Google Drive) within your Gemini Agent steps to search data, send messages, and manage records. 

- **Use flow control steps** : Add conditional branching, data filtering, and loops to your workflow. 

- **Connect MCP servers** : Connect MCP servers as workflow steps or as tools for Gemini Agent steps. 

- **Use human-in-the-loop steps** : Add human review, approval, and information request steps to your workflow. 

- **Add existing agents to your workflow** : Hand off tasks to other specialized AI agents within your workflow. 

- **Manage workflow versions** : Save, share, compare, and restore workflow versions. 

- **Edit a workflow with natural language** : Edit existing workflows by describing changes in natural language. 

- **View workflow execution logs** : Monitor workflow runs with **step-by-step** execution traces. 

- **Share a workflow** : Share live workflows with other users in your organization. 

### Supported connectors

Workflows support these connectors: 

- Gmail 

- Google Calendar 

- Google Chat 

- Google Drive 

- Confluence 

- Confluence Data Center 

- Jira 

- Jira Data Center 

- Microsoft Teams 

- Notion 

- OneDrive 

- Outlook 

- Salesforce 

- SharePoint 

- ServiceNow 

- Slack 

### Before you begin

Before exploring these new features, do the following: 

- Ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features 

- (/gemini/enterprise/docs/manage-web-app-features). 

- Ensure you have a Gemini Enterprise web app with the necessary data stores connected. For more information, see About apps and data stores (/gemini/enterprise/docs/apps-data-stores). 

### Workflow canvas

Workflow Builder offers a hybrid canvas that combines the ease of natural language prompts with the control of a visual editor. 

- **Conversational designer** : The conversational designer, accessible at the start of workflow creation and within the visual editor, provides a conversational interface to build and refine your workflow using natural language prompts. This is ideal for users who prefer a **no-code** development experience and want to use natural language to build their workflows. 

 

 

**Editor canvas** : The editor canvas provides a visual representation of the workflow. It provides a logical flow of nodes that represent the steps and connections between them. The visual editor is ideal for users who want to refine the workflow logic, add conditional logic, and integrate with various tools and applications. 

**Preview** : The preview tab provides a live preview of the workflow, letting you run simulations to test the workflow's flow and make any necessary adjustments. 

- **Runs** : The runs tab provides a list of all the workflow runs, including the date and time of each run, the trigger that started the run, and the current status of the run. 

### Workflow components

A workflow consists of the following components: 

- **Triggers** 

- **Steps** 

**Variables** 

#### Triggers

_Triggers_ are events that start the execution of a workflow. The following table lists the supported triggers for workflows: 

|Trigger|Description<br>i i|Configuration fields|
|---|---|---|
|Manual|Triggers the execution of the workflow|Input fields: Optional or required input|
|trigger|on demand. Users can launch the<br>workflow by entering`@`and the workflow<br>name from a Gemini Enterprise app chat<br>prompt.|fields that users can provide when<br>launching the workflow.|

|Trigger|Description|Configuration fields|
|---|---|---|
|Schedule<br>trigger|Triggers the execution of the workflow a<br>a specified frequency.|l t<br>Frequency: The frequency at which the<br>workflow is triggered. You can specify<br>the frequency in minutes, hours, days,<br>weeks, months, or use a custom cron<br>expression.|
|||Time zone: The time zone for the<br>frequency.|
|Event<br>trigger|Triggers the execution of the workflow<br>when data changes in a connector.|Connector: The connected application<br>that generates the event.|
|||Filter: The criteria that must be met for<br>the event to trigger the workflow.|

**Note:** Event triggers define the starting condition for a workflow based on external connector activity (such as receiving an email). They are configured as workflow triggers and don't appear as intermediate step nodes in the canvas flow. 

#### Steps

_Steps_ are individual tasks that the workflow performs. Each step is executed in sequence, and the outcome of each step can influence the next step. 

The following table lists the supported steps, categorized by the type of action that they perform: 

|Category|Step|Description|Configuration fields|
|---|---|---|---|
|Agent nodes|Gemini Agent|An AI-powered agent that<br>you can configure to read,<br>reason, and respond based<br>on predefined instructions.|Input fields:<br>Instructions: The instructions for<br>the Gemini Agent.<br>Knowledge: The additional files or<br>resources that the Gemini Agent<br>can access to generate responses.<br>When a Google Drive or OneDrive<br>data store is configured, Add from<br>Drive and Add from OneDrive<br>options are available. These<br>options let you select specific files<br>or folders, restricting the agent's<br>search to only those resources.<br>The search is performed live on<br>each agent run, so any changes to<br>the source files are immediately<br>reflected.|
||||Important: If the full Drive or<br>OneDrive tool is enabled on the<br>same agent node, it takes<br>precedence and grants the agent<br>unrestricted search access. The<br>recommended workaround is to<br>use two distinct<br>**`Gemini Agent`**<br>nodes. The first node should use<br>the restricted knowledge for<br>searching, and the second node<br>can use the full tool for other<br>functionalities like writing<br>updates.|
||||Connected apps: Select which<br>connectors and actions the agent<br>can access at runtime. You can<br>granularly select search actions<br>and enable or disable data<br>modification actions. For more<br>information, see<br>Configure Agent|

|Category|Step|Description|Configuration fields|
|---|---|---|---|
||||node connectors and actions<br>(#configure-agent-actions).<br>Model: The Gemini model that the<br>Gemini Agent uses.|
||||Note: Only Gemini 3.0 and later<br>models are supported.|
||||Output fields:|
||||The response from the Gemini Agent<br>is captured as a variable that can be<br>passed as input to subsequent steps<br>in the workflow.|
||||Output format: You can specify the<br>output as plain text or in a<br>structured JSON format.|
||||JSON schema: When using<br>structured output, you can define a<br>manual JSON schema to specify<br>the format and data types of the<br>output variables, ensuring<br>consistent data handling|
||||throughout the orchestration.|

|Category|Step|Description|Configuration fields|
|---|---|---|---|
|Flow control|Condition|Conditions are logical<br>statements that determine<br>how the workflow executes<br>the steps. They define the<br>criteria that must be met for<br>a step to execute, and can<br>be based on the outcome of<br>previous steps or external<br>data sources.|<br>Input fields:<br>Branch name: The name of the<br>branch to execute if the condition<br>is true.<br>Variable: The variable to evaluate.<br>You can select a variable from the<br>output of previous steps.<br>Operator: The operator (such as<br>`contains`, `equals`, `greater<br>than`) to use for the evaluation.<br>Value: The value to compare with<br>the variable. You can specify a<br>static value, or select a variable<br>from the output of previous steps.<br>+ Condition: You can add<br>additional conditions using logical<br>operators such as `AND` and `OR`.|
|Human in the<br>loop|<br>Request info|Lets you request<br>information from a human<br>user.|Input fields:<br>Message: The message to display<br>to the user. You can specify a static<br>message, or select a variable from<br>the output of previous steps.<br>Questions: The questions to ask<br>the user. You can specify the type<br>of answer you are requesting (such<br>as short answer, paragraph, date,<br>email, single-select, or yes or no).<br>Output fields:<br>The questions that the user<br>answered.|

#### Configure Agent node connectors and actions

When you configure a **Gemini Agent** node, you can control which connectors and actions the agent can access at runtime. You can restrict the agent to read-only search operations or enable mutative write-back actions. 

At a glance: Agent node action capabilities 

|Capability|Action category|Selection granularity|Example use case|
|---|---|---|---|
|Search & query|`Search For Data`|Per-action (toggle<br>individual actions on or<br>off)|<br>Broad queries, looking<br>up tickets, searching<br>across knowledge<br>bases.|
|Data modification|`Add Or Update Data`|Connector-level (all-or-<br>nothing toggle)|Creating tickets,<br>updating issue status,<br>sending emails.|

Attach and authorize a connector 

App (#app) 

To attach a connector to an agent node, do the following: 

1. In the workflow canvas, click the **Gemini Agent** node to open its configuration pane. 

2. Under **Connected apps** , locate the connector you want to attach (such as **Jira** , **Gmail** , or **Google Drive** ). 

3. Toggle the connector switch to **On** . 

   - If this is the first time you or your organization is using the connector, complete the prompted OAuth authorization flow to grant the required permissions. 

4. Click the expand arrow () next to the connector name to turn on the actions supported by the connector. 

Select action categories 

Each connector organizes its actions into two distinct categories: 

- **Search For Data** : Actions that search, query, list, or retrieve records from the connected service. 

   - **Granular action selection** : Click the **Configure** icon () next to **Search For Data** to view all available search actions (such as `Search Events` , `List Events` , or `List Calendars` ). You can enable or disable individual actions independently. 

   - **Deterministic search filters** : Limit search scopes by configuring filters using structured drop-downs or native query expressions, such as Jira Query Language (JQL), Confluence Query Language (CQL), Drive search queries, or Gmail search operators. 

   - **In-line query testing** : Validate your queries directly within the configuration pane to verify that your filters return the expected results before running the workflow. 

- **Add Or Update Data** : Actions that create, modify, send, or delete records in the target application (for example, creating a Jira issue or sending an email). 

   - **Connector-level toggle** : The mutative action toggle operates at the connector level. Toggling this on grants the agent access to all supported mutative operations for that connector. 

**Note:** Adding or updating data through connectors requires human review. If you toggle a connector on but disable all underlying actions in both the **Search For Data** and **Add Or Update Data** categories, the agent cannot interact with the connector at runtime. 

Action dependency requirement 

**Caution: Mutative actions depend on read-only and search actions to resolve entity identifiers at runtime.** 

Mutative actions typically require the agent to first look up a record identifier (such as an issue ID, contact email, or folder ID) before performing an update, create, or delete operation. 

For example, an **Update Jira issue** action requires the agent to first query Jira to obtain the internal **`issue_id`** . If mutative actions are enabled without their supporting search actions, the agent cannot look up the required target records, which causes runtime action execution errors (such as **`ENTITY_NOT_FOUND`** or missing parameter errors). When enabling mutative actions, always enable the supporting search and retrieval actions. 

Example: Restrict an agent to read-only Jira search 

App (#app) 

The following example shows how to configure a **Gemini Agent** node to search Jira issues without allowing the agent to create or modify issues: 

1. In the workflow canvas, click the **Gemini Agent** node to open its configuration pane. 

2. Under **Connected apps** , toggle **Jira** to **On** (complete OAuth authorization if prompted). 

3. Click the expand arrow () next to **Jira** . 

4. Ensure the **Search For Data** toggle is **On** , and toggle **Add Or Update Data** to **Off** . 

5. Click the **Configure** icon () next to **Search For Data** , and verify that only the desired read-only search actions (such as **Search Jira** ) are enabled. 

Action resolution and runtime precedence 

When the workflow executes, Gemini Agent selects and invokes actions based on the following precedence rules: 

|Configuration state|Runtime action execution|
|---|---|
|Search enabled|Exposes standard list and retrieve actions for all enabled<br>search operations.|

|Configuration state|Runtime action execution|
|---|---|
|Individual search action disabled|The specific search action is omitted from the agent's<br>action catalog.|
|Add / Update data enabled|Exposes mutative actions alongside any enabled search<br>actions.|
|Add / Update data disabled|All data creation, update, and deletion actions are<br>blocked for that connector.|

#### Variables

_Variables_ are values that can be passed between steps in a workflow. These values are generated as the output of steps, and can be used as input for subsequent steps. 

### Workflow versions

When you create a workflow, you can save it as a draft or turn it on. After you make the workflow live, you can create additional versions of the workflow, and save, compare, and restore them. Having multiple versions of a workflow can be useful in the following scenarios: 

You want to test a new version of the workflow without disrupting the existing version. 

You want to revert to an earlier version of the workflow. 

For more information, see Manage workfow versionsl (/gemini/enterprise/docs/workflow-builder/manage-agent-versions). 

### Known issues

The following are the known issues and limitations for workflows in this release: 

- Natural language support (/gemini/enterprise/docs/workflow-builder/known-issues#KI28) Email template display issues (/gemini/enterprise/docs/workflow-builder/known-issues#KI29) Natural Language reliability (/gemini/enterprise/docs/workflow-builder/known-issues#KI30) Runs tab loading failures (/gemini/enterprise/docs/workflow-builder/known-issues#KI31) 

- Connectors not showing after authorization (/gemini/enterprise/docs/workflow-builder/known-issues#KI32) 

- Execution timeouts under heavy load (/gemini/enterprise/docs/workflow-builder/known-issues#KI33) 

- Disabled actions failure 

- (/gemini/enterprise/docs/workflow-builder/known-issues#KI34) 

- Model recommendation 

- (/gemini/enterprise/docs/workflow-builder/known-issues#KI35) 

- Approval node formatting 

- (/gemini/enterprise/docs/workflow-builder/known-issues#KI36) 

### What's next

- Learn how to create a workflow with natural language 

- (/gemini/enterprise/docs/workflow-builder/create-natural-language). 

- Learn how to use workflow templates (/gemini/enterprise/docs/workflow-builder/use-agent-templates). 

- Learn how to set up event triggers (/gemini/enterprise/docs/workflow-builder/configure-event-trigger). 

- Learn how to share a workfowl (/gemini/enterprise/docs/workflow-builder/share-workflows). 

Learn how to manage workfow versionsl 

(/gemini/enterprise/docs/workflow-builder/manage-agent-versions). 

Last updated 2026-10-16 UTC. 



## Create a workflow

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-workflows

This document describes how to use the workflow canvas to create a workflow using either natural prompts or the visual editor. 

### Before you begin

Before using this feature, complete the following steps: 

- Ensure that you have a web app with the necessary data sources connected. For more information, see Create an app (/gemini/enterprise/docs/create-app), Connect a Google data source (/gemini/enterprise/docs/connectors/create-data-store) , and Connect a third-party data source 

- (/gemini/enterprise/docs/connectors/connect-third-party-data-source). 

- Ensure that you have enabled the Workflow Builder feature toggle for your web app. For more information, see Manage web app features 

- (/gemini/enterprise/docs/manage-web-app-features). 

### Create a workflow using natural prompts

App (#app) 

To create a workflow using natural language prompts, you describe the task you want the agent to perform, and Workflow Builder generates a workflow scaffold for you. For more information, see Create a workflow using natural language (/gemini/enterprise/docs/workflow-builder/create-natural-language). 

### Create a workflow using the visual editor

App (#app) 

To create a workflow using the visual editor, do the following: 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click **+ New agent > Workflow** . 

3. Click **Build manually** to open the visual editor. 

4. A default manual trigger is added to the canvas. Click **Input fields** to enter a required or optional input field that the user can provide when running the workflow. 

To change the trigger to another trigger type, click the manual trigger in the canvas and then select another trigger type in the configuration pane. 

5. Click **+ Add step** to add additional steps to the workflow. For the list of supported steps and their configurations, see Steps 

   - (/gemini/enterprise/docs/workflow-builder/workflows#steps). 

6. To preview and test your workflow, switch to the **Test** tab and start a test run. 

7. To turn on your workflow and make it live, click **Turn on** . 

The workflow is live and starts to execute according to the configured schedule or events, or manually by the user. 

### What's next

Learn how to run test simulations for your workflow (/gemini/enterprise/docs/workflow-builder/simulate-workflows). 

Last updated 2026-10-14 UTC. 



## Create a workflow with natural language

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-natural-language

You can create an agent in Workflow Builder by describing your agent's function in plain language. 

Gemini Enterprise generates a workflow scaffold based on your description, including steps, conditions, and actions. You can then refine the generated workflow in the visual flow builder. 

### Before you begin

Before using this feature, make sure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features 

(/gemini/enterprise/docs/manage-web-app-features). 

### Create an agent using a natural language prompt

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the sidebar, click **Agents** . 

3. Click **Create agent** . 

4. In the **Describe your agent** field, enter a description of your agent's function. For example: "Prioritize messages and draft professional replies" or "Summarize my emails from yesterday." 

**Tip:** Provide enough context about the workflow's purpose, boundaries, and expected behavior. You can prompt Gemini to ask clarifying questions to refine the 

workflow. 

5. Click **Submit** or press **Enter** . 

Gemini Enterprise generates a workflow scaffold in the flow builder. The generated workflow is a starting point. You can add, remove, or reconfigure steps to match your requirements. For more information, see Edit an agent with natural language prompts 

(/gemini/enterprise/docs/workflow-builder/edit-workflows#natural-language). 

6. Click any step in the flow builder to view and edit its configuration in the configuration panel. 

7. To test your workflow, click the **Preview** tab. 

8. When the workflow is ready, click **Turn on** to make it live. 

Turning on a scheduled workflow starts it on the configured schedule. Turning on an event-triggered workflow begins listening for the configured events. Note: Not all node types can be added or edited with natural language prompts. If editing with natural language is not supported for nodes in your workflow, you can continue to edit those nodes manually. 

### What's next

Learn how to use agent templates 

- (/gemini/enterprise/docs/workflow-builder/use-agent-templates). 

Learn how to edit an agent with natural language 

- (/gemini/enterprise/docs/workflow-builder/edit-workflows). 

Learn how to configure Agent node connectors and actions 

- (/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions). 



## Use workflow templates

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-agent-templates

You can create a workflow from a prebuilt template in Workflow Builder. 

Templates provide pre-configured workflow scaffolds for common business use cases, so you can start without building a workflow from scratch. 

**Note:** Only Google-provided templates are available in this release. 

### Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features (/gemini/enterprise/docs/manage-web-app-features). 

### Browse and use a template

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the sidebar, click **Agents** . 

3. Click **Create agent** . 

4. Click **Browse all templates** . 

5. In the templates gallery, browse templates by category. 

6. Click a template card to view its details. Each template card shows the connectors used, a description, and the template author. 

7. Click **Use template** to create a workflow based on the selected template. 

The template opens in the flow builder with pre-configured steps. Review and customize the workflow as needed. 1. To test your workflow, click the **Preview** tab. 1. When you are satisfied with your workflow, click **Turn on** to make it live. 

**Note:** Turning on a scheduled workflow starts it on the configured schedule. Turning on an event-triggered workflow begins listening for the configured events. 

### What's next

Learn how to create a workflow with natural language 

- (/gemini/enterprise/docs/workflow-builder/create-natural-language). 

Learn how to set up event triggers 

- (/gemini/enterprise/docs/workflow-builder/configure-event-trigger). 

- Learn how to configure Agent node connectors and actions (/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions). 

Last updated 2026-10-14 UTC.
