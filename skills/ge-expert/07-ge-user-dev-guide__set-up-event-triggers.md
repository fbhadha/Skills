# Gemini Enterprise: user guide, Workflow Builder, developer guide / Set up event triggers to Share a workflow
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 130-168, extracted 2026-10-18

Contains:
- Set up event triggers (pages 130-134) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/configure-event-trigger
- Use flow control steps (pages 135-137) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/flow-control-steps
- Connect MCP servers (pages 138-140) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/connect-mcp-servers
- Use human-in-the-loop steps (pages 141-143) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-hitl-steps
- Add an existing agent step (pages 144-149) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/add-existing-agents
- Simulate a workflow (pages 150-152) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/simulate-workflows
- Turn a workflow on or off (pages 153-155) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/publish-workflows
- Edit a workflow (pages 156-158) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-workflows
- Share a workflow (pages 159-168) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-workflows

## Set up event triggers

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/configure-event-trigger

You can configure your workflow to run automatically when data changes in a connector. 

Event triggers use polling to detect changes such as new emails, updated calendar events, or new files in a connected data store. When a change is detected, the configured workflow runs. 

**Note:** There might be a delay of 5-10 minutes for an event to be received and trigger a workflow. The specific ordering of events is not guaranteed. 

### Before you begin

Before using this feature, complete the following steps: 

- Ensure that you have a web app with the necessary data sources connected. For more information, see Create an app (/gemini/enterprise/docs/create-app), Connect a Google data source (/gemini/enterprise/docs/create-data-store), and Connect a third-party data source 

- (/gemini/enterprise/docs/connect-third-party-data-source). 

- Ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features 

- (/gemini/enterprise/docs/manage-web-app-features). 

- Ensure that the connector you want to use as a trigger source is connected as a data store in your Gemini Enterprise app. For more information, see Connect a third-party data store 

- (/gemini/enterprise/docs/connectors/connect-third-party-data-source). 

### Supported connectors

The following connectors support event triggers: 

- Confluence 

- Gmail 

- Google Calendar 

- Google Drive 

- Jira Cloud 

- OneDrive 

- Outlook 

- ServiceNow 

- SharePoint 

- Teams 

**Note:** Some connectors require you to click **Connect** before you can select events. Connectors that are already connected to your Gemini Enterprise app display a chevron icon and can be selected immediately. 

### Configure an event trigger

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the navigation menu, click **Agents** . 

3. Click **Create agent** . 

4. Click **Start manually** . 

5. On the **What should trigger your agent?** page, click **App event** . 

6. In the details panel, under **App event - Choose an app to start with** , browse or search for the connector you want to use. Click the connector name to select it. 

7. Select the event that triggers your workflow. Events are organized by category. 

8. After selecting an event, the trigger is added to the top of your workflow in the flow builder. 

9. Click **Add step** to add workflow steps that run when the trigger fires. 

### Test an agent with event triggers

Before turning on your workflow, you can test its functionality by previewing trigger events and running simulations with sample event data. 

#### Preview event trigger results

App 

(#app) 

1. In the workflow canvas, click the event trigger node at the top of your workflow. 

2. In the right-side configuration panel, click **Preview results** . 

3. Gemini Enterprise fetches recent events from the connector. Each item displays the event title and timestamp. Google Calendar preview results are based on recently updated events and might not reflect recent events. 

4. You can click a preview result to see the details of the event. 

#### Test your agent workflow

App 

(#app) 

1. Switch to the **Test** tab in the workflow canvas. 

2. In the trigger input section, select a sample event from the list of previewed events using the **Select input** selector. 

3. Click **Start manually** to run the workflow simulation using the sample event data. 

4. When the run finishes, expand the simulation summary to inspect the outputs and verify that each step processed the trigger payload correctly. 

### Manage event triggers

You can manage event triggers by editing their configuration, turning workflows on or off, or deleting triggers. 

NOTE: Events can take up to 10 minutes to appear. 

- **Edit an event trigger:** Open the agent in edit mode, click the trigger node on the canvas, and update its settings or filter criteria in the configuration panel. 

- **Turn on an event trigger:** To activate the trigger and begin polling for events, turn on the workflows. For more information, see Turn a workflow on or off (/gemini/enterprise/docs/workflow-builder/publish-workflows). 

- **Turn off an event trigger:** To pause or deactivate event polling, turn off the workflow. 

### Known issues and limitations

These are known issues and limitations when working with event triggers. 

- **Connector unlinking:** When an administrator unlinks a connector from the engine or app, the event trigger is paused automatically. However, no notification is sent to the user, and users cannot view paused agents in their gallery. 

- **Failed session retries:** If an agent execution fails due to errors fetching data from an associated connector in an event trigger, a session is created with a failed status. Manual retries on failed sessions are not currently supported. 

- **Filters:** Always add filters to your event triggers to ensure timely agent execution on most important events. 

**Gmail triggers:** 

   - Agent initiation might be slower for users with a high volume of emails. 

   - Gmail supports two triggers: **When an email is sent** and **When an email is received** . If you want to trigger an agent by sending yourself an email, use **When an email is sent** . If you use **When an email is received** , that will not trigger the agent. 

- For a full list of system constraints, see Workflow Builder quotas and limits (/gemini/enterprise/docs/workflow-builder/quotas-and-limits). 

### What's next

- Learn how to configure Agent node connectors and actions 

- (/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions). 

- Learn how to search with filters 

- (/gemini/enterprise/docs/workflow-builder/search-with-filters). 

- Learn how to view agent execution logs 

- (/gemini/enterprise/docs/workflow-builder/workflow-runs). 

- Learn how to turn a workflow on or of 

- (/gemini/enterprise/docs/workflow-builder/publish-workflows). 

Last updated 2026-10-14 UTC. 



## Use flow control steps

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/flow-control-steps

You can add flow control steps to your agent workflow to direct execution based on conditions, filter data, or loop over lists of items. 

Flow control steps let you build complex workflows with branching logic, scoped data processing, and iterative operations. 

### Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features 

(/gemini/enterprise/docs/manage-web-app-features). 

### Flow control step types

Workflow Builder provides three flow control step types: 

- **Condition** : Branch your workflow into different paths based on criteria you define. Use conditions to route execution to different steps depending on data values or step outputs. 

- **Filter** : Filter a list of data to process only items that match your criteria. Use filters to narrow results from a search or previous step before passing data to downstream steps. 

- **Loop** : Iterate over a list of items and run one or more steps for each item. Use loops to process multiple records, such as each email in a search result or each ticket in a project. 

### Add a condition step

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing agent or create a new agent. 

3. In the flow builder, click **Add step** . 

4. In the **Add step** panel, click **Flow control** to expand the section. 

5. Click **Condition** . 

6. The condition step is added to your workflow and its configuration panel opens on the right. 

7. Configure the condition criteria that determines which branch the workflow follows. 

8. Add steps to each branch of the condition. 

### Add a filter step

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing agent or create a new agent. 

3. In the flow builder, click **Add step** . 

4. In the **Add step** panel, click **Flow control** to expand the section. 

5. Click **Filter** . 

6. The filter step is added to your workflow and its configuration panel opens on the right. 

7. Configure the filter criteria to specify which items should pass through to downstream steps. 

### Add a loop step

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing agent or create a new agent. 

3. In the flow builder, click **Add step** . 

4. In the **Add step** panel, click **Flow control** to expand the section. 

5. Click **Loop** . 

6. The loop step is added to your workflow and its configuration panel opens on the right. 

7. Configure the list of items to iterate over. 

8. Add one or more steps inside the loop that run for each item in the list. 

### What's next

- Learn how to configure Agent node connectors and actions 

- (/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions). 

- Learn how to search with filters 

- (/gemini/enterprise/docs/workflow-builder/search-with-filters). 

- Learn how to use human-in-the-loop steps 

- (/gemini/enterprise/docs/workflow-builder/use-hitl-steps). 

Last updated 2026-10-14 UTC. 



## Connect MCP servers

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/connect-mcp-servers

You can connect Model Context Protocol (MCP) servers to your agent workflow to extend your agent's capabilities with custom tools, resources, and APIs. 

Workflow Builder provides dedicated MCP step types that let you call tools, list resources, and query servers hosted on any MCP-compatible endpoint. You can also add MCP tools to Gemini agent steps so the model can invoke them dynamically during reasoning. 

### Before you begin

Before using this feature, complete the following steps: 

- Ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features 

- (/gemini/enterprise/docs/manage-web-app-features). 

- Ensure that your Gemini Enterprise organization has access to at least one MCP-compatible server endpoint. For more information, see Set up a custom MCP server data store 

- (/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server). 

### Add an MCP step to your workflow

App (#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing agent or create a new agent. 

3. In the flow builder, click **Add step** . 

4. In the **Add step** panel, click **MCP servers** to expand the section. 

5. Click the MCP step you want to add. 

6. The MCP step is added to your workflow, and its configuration panel opens. 

7. Configure any additional parameters required by the selected step type. 

8. (Optional) Click **Preview** to preview the workflow and the operation of the MCP step. 

### Add MCP tools to a Gemini agent step

You can add MCP tools to a Gemini agent step so the model can discover and invoke them dynamically based on context. Unlike dedicated MCP steps that run deterministically in your workflow based on an event or trigger, MCP tools added to a Gemini agent step are available for the model to call as needed during its reasoning process. 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing agent or create a new agent. 

3. In the flow builder, click the Gemini agent step you want to configure. The agent configuration panel opens. 

4. Click **Tools & Integrations** to view available tools, including any MCP connectors available in your organization. 

5. To enable access to the tool for your agent, click the **Authorize** toggle. The Gemini agent step can discover and invoke the authorized MCP connectors at runtime, if required. 

### What's next

- Learn how to use flow control steps 

- (/gemini/enterprise/docs/workflow-builder/flow-control-steps). 

- Learn how to set up event triggers 

- (/gemini/enterprise/docs/workflow-builder/configure-event-trigger). 

- Learn how to search with filters 

- (/gemini/enterprise/docs/workflow-builder/search-with-filters). 

Last updated 2026-10-14 UTC. 



## Use human-in-the-loop steps

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-hitl-steps

You can add human-in-the-loop steps to your workflow to pause execution and require human input before proceeding. 

Workflow Builder provides two step types: requesting information from a user and requiring approval before the agent takes further action. 

### Before you begin

Before using this feature, ensure that a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features (/gemini/enterprise/docs/manage-web-app-features). 

### Human-in-the-loop step types

Workflow Builder provides two human-in-the-loop step types: 

- **Request info** : Pause the workflow and ask the user one or more questions. Use this step when the workflow needs additional information or clarification to proceed. 

- **Approval** : Pause the workflow and present outputs for human review and approval. Use this step when the workflow produces outputs that require human sign-off before downstream steps execute. 

### Add a request info step

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing workflow or create a new workflow. 

3. In the flow builder, click **Add step** . 

4. In the **Add step** panel, click **Human in the loop** to expand the section. 

5. Click **Request info** . 

6. The request info step appears in your workflow, and its configuration panel opens on the right. 

7. In the **Message** field, enter the message to display to the user when the workflow pauses. This message provides context about why input is needed. 

8. In the **Info to request** section, configure the questions to ask the user. For each question, do the following: 

   - a. Enter the question text in the question field. 

   - b. Select the input type from the list (for example, **Short answer** ). 

9. To add more questions, click **Add question** . 

10. To configure additional settings, click **More** . 

### Add an approval step

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing workflow or create a new workflow. 

3. In the flow builder, click **Add step** . 

4. In the **Add step** panel, click **Human in the loop** to expand the section. 

5. Click **Approval** . 

6. The approval step appears in your workflow, and its configuration panel opens on the right. 

7. Configure the approval settings, including what information is presented to the reviewer. 

When a workflow run reaches a human-in-the-loop step, the run pauses and appears with a **Needs Review** status in the **Runs** tab. For more information, see View workflow runs (/gemini/enterprise/docs/workflow-builder/workflow-runs). 

### What's next

- Learn how to view workflow runs 

- (/gemini/enterprise/docs/workflow-builder/workflow-runs). 

- Learn how to use flow control steps 

- (/gemini/enterprise/docs/workflow-builder/flow-control-steps). 

- Learn how to manage workfow versionsl 

- (/gemini/enterprise/docs/workflow-builder/manage-agent-versions). 

Last updated 2026-10-14 UTC. 



## Add an existing agent step

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/add-existing-agents

You can add existing AI agents as steps in your workflow to transfer tasks to specialized agents. This lets you compose multi-agent workflows that orchestrate among different agents, each handling a specific part of a larger process. 

**At a glance:** 

- **Purpose:** Reuse specialized ADK and A2A agents as steps within Workflow Builder workflows. 

- **Clarifying questions:** Allows referenced agents to pause execution and ask the user for missing details instead of failing or guessing. 

- **Integration options:** Supported natively for custom A2A agents ( **`input-required`** ) and ADK agents ( **`RequestInput`** ). 

### Before you begin

Before using this feature, complete the following steps: 

- Make sure a Gemini Enterprise administrator has enabled the Workflow Builder feature toggle in your app's feature management settings. For more information, see Manage web app features 

- (/gemini/enterprise/docs/manage-web-app-features). 

- Make sure the agents you want to add are available in your organization. This feature supports the addition of the following agents: 

   - ADK agents (/gemini/enterprise/docs/register-and-manage-an-adk-agent) 

   - A2A agents (/gemini/enterprise/docs/register-and-manage-an-a2a-agent) 

## Add an existing agent step

App 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing agent or create a new agent 

   - (/gemini/enterprise/docs/workflow-builder/create-chat-agent). 

3. In the flow builder, click **Add step** . 

4. In the **Add step** panel, click **Existing agents** to expand the section. 

5. Browse the list of available agents. 

**Note:** The agent picker displays published ADK and A2A agents that your organization has shared with you. Cross-project agents are not displayed. 

6. Click the agent you want to add. 

The system adds the existing agent step to your workflow. The selected agent runs as part of your workflow, receiving input from earlier steps and passing output to later steps. 

**Note:** If you add an A2A or ADK agent that requires user OAuth for authentication, you must first authenticate and then start a new run of the workflow. 

7. In the canvas, click the existing agent step to open its configuration panel, and configure the following: 

   - **Prompt** : Enter the prompt or instructions used to trigger the agent. You can include static text or reference outputs from previous steps (for example, `${step_name.output}` ) . 

The agent step is a dynamic reference to the selected agent. If the source agent is updated or a new version is made live, your workflow automatically uses the most recent version. 

For more information on the limitations of this feature, see Known issues and limitations 

(/gemini/enterprise/docs/workflow-builder/known-issues#add_an_existing_agent_step). 

### How clarifying questions work

When an existing agent runs in a workflow, it can pause execution to ask the user a clarifying question if it needs missing information to complete its task. Clarifying questions are supported natively when the referenced agent emits an `inputrequired` signal (A2A) or a `RequestInput` event (ADK). 

When an existing agent step runs and requires additional information: 

1. **Execution pauses** : The workflow pauses execution at the existing agent step and initiates a human-in-the-loop (HITL) prompt. 

2. **User answers the prompt** : The Gemini Enterprise web app displays the agent's clarifying question to the user along with a text field to enter their response. 

3. **Execution resumes** : When the user submits their answer, the workflow resumes the existing agent, passing the user's answer back to the agent. 

4. **Multi-turn support** : The agent can ask multiple clarifying questions in succession across multiple turns until it gathers all required information and produces its final output. 

#### Context isolation

During a clarifying question exchange, the referenced agent only receives its own interaction history with the user and the initial prompt configured for the node. Outputs and variables from other steps in the workflow are not automatically passed to the referenced agent unless explicitly referenced in the step's prompt. 

### Implement clarifying questions in your agent

To support clarifying questions, configure your custom agent to emit a protocollevel request-input signal when it needs additional information. 

#### A2A agents (native)

For agents that implement the Agent-to-Agent (A2A) protocol directly, return the task in the `input-required` state with `TaskUpdater` , providing the clarifying question in the message payload: 

```
from a2a.server.tasks import TaskUpdater
from a2a.types import Message, Part, Role, TextPart
Inside your custom agent's task executor class:
async def execute(self, context, event_queue):
   updater = TaskUpdater(event_queue, context.task_id, context.context_id)
   if context.current_task is None:
       await updater.submit()
   await updater.start_work()
   user_input = context.get_user_input()
   if "weather" in user_input and "tokyo" not in user_input.lower():
       await updater.requires_input(
           Message(
               message_id=f"q-{context.task_id}",
               role=Role.agent,
               parts=[Part(root=TextPart(
                   text="Which city would you like the weather for?"))],
               task_id=context.task_id,
               context_id=context.context_id,
           )
       )
       return
   await updater.complete(
       Message(
           message_id=f"a-{context.task_id}",
           role=Role.agent,
           parts=[Part(root=TextPart(
               text="It is sunny and 72°F in Tokyo."))],
           task_id=context.task_id,
           context_id=context.context_id,
       )
   )
```

The user's response is sent back to your agent as a `message/send` request with the same `taskId` . 

#### A2A agents (built with ADK)

If your agent is built with the Agent Development Kit (ADK) and exposed through A2A (using `to_a2a()` ), wrap your question-asking function in `LongRunningFunctionTool` : 

```
from google.adk.agents import Agent
from google.adk.tools.long_running_tool import LongRunningFunctionTool
from google.adk.a2a.utils.agent_to_a2a import to_a2a
def get_weather(city: str) -> str:
   """Returns weather information for a city."""
   return f"It is sunny and 72°F in {city}."
def ask_clarifying_question(question: str) -> None:
   """Asks the user a question and waits for their reply."""
   return None
root_agent = Agent(
   model="gemini-2.5-flash",
   name="weather_agent",
   instruction=(
       "If the user asks for weather without specifying a city, call "
       "`ask_clarifying_question` and wait. Do not guess."
   ),
   tools=[get_weather, LongRunningFunctionTool(ask_clarifying_question)],
)
a2a_app = to_a2a(root_agent, port=8000)
```

**Note:** The function passed to **`LongRunningFunctionTool`** must return **`None`** . If it returns a value, the step completes instead of pausing. 

#### ADK agents on Agent Engine

For reasoning-engine-hosted ADK agents on Agent Engine, emit a `RequestInput` event within a generator tool or custom agent step: 

```
from google.adk.events import RequestInput
Inside a generator tool or custom agent step
def ask_for_details():
   """Requests user input during tool or step execution."""
   yield RequestInput(
       interrupt_id="weather_city",
       message="Which city would you like the weather for?",
   )
```

### What's next

- Learn how to configure Agent node connectors and actions 

- (/gemini/enterprise/docs/workflow-builder/workflows#configure-agent-actions). 

- Learn how to connect MCP servers 

- (/gemini/enterprise/docs/workflow-builder/connect-mcp-servers). 

- Learn how to use flow control steps 

- (/gemini/enterprise/docs/workflow-builder/flow-control-steps). 

Last updated 2026-10-14 UTC. 



## Simulate a workflow

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/simulate-workflows

This page provides information about workflow simulations and how to run them. Running simulations can help you identify and resolve issues with your workflow before making it live. Simulations can also help you understand how your workflow will behave in different situations. 

### Run a simulation

App 

- (#app) 

To run a simulation of your workflow, do the following: 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app. 

4. Go to the **Your agents** section and click the workflow that you want to simulate. 

The workflow canvas appears. 

5. Go to the **Preview** tab and click **Start simulation** . 

6. A simulation of the workflow begins. You can interact with the simulation in the same way that you would interact with the live workflow (for example, by providing inputs or answering questions). 

7. When the simulation ends, a summary of the simulation results appears. Expand the summary to see details about the simulation, such as the individual steps that the workflow took, the actions and reasoning that the workflow performed at each step, and the outputs of each step. 

### What's next

- Learn how to turn on your workflow 

- (/gemini/enterprise/docs/workflow-builder/publish-workflows). 

Last updated 2026-10-14 UTC. 



## Turn a workflow on or off

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/publish-workflows

Turning on a workflow triggers the workflow logic and executes the sequence of steps that you have configured. After you create and test a workflow or a new version of a workflow, you can turn it on. 

### Workflow versions

When you create a workflow, you can save it as a draft or turn it on. After the workflow is live, you can create additional versions of the workflow. Having multiple versions of a workflow can be useful in the following scenarios: 

- You can save a draft of the workflow if it is not yet ready to be turned on. 

- You can test a new version of the workflow without disrupting the current live version. 

You can revert to an earlier version of the workflow if necessary. 

### Turn on a workflow version

To turn on a workflow version, do the following: 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app. 

4. Go to the **Your agents** section and click the workflow that contains the version that you want to turn on. 

The workflow canvas appears with the last saved draft version of the workflow. 

5. Optional: To select another workflow version, click the **Turn on** or **Update** drop-down and select **Version history** . In the **Version history** pane, select the version that you want to turn on. 

6. Click **Turn on** (or **Update** ). 

7. In the confirmation dialog, click **Turn on** (or **Update** ). You can also choose to click **Save version only** to save the version but not turn it on. 

After you make the workflow live, a new draft version of the workflow is created and the status of the existing one changes to **Live** . Open the **Version history** pane to view the live version of your workflow. 

### Turn off a workflow version

To turn off a workflow version, do the following: 

**Caution:** Turning off a workflow version terminates all associated schedules and active runs. Ensure no critical processes are active before proceeding. Also, the workflow stops running for everyone you shared the workflow with. 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

3. The **Agent Gallery** page appears displaying all the prebuilt available agents and workflows in your web app. 

4. Go to the **Your agents** section and click the workflow that contains the workflow version that you want to turn off. 

5. In the editor canvas, click the **Turn on** or **Update** drop-down and select **Version history** . 

6. In the **Version history** pane, locate the live version that you want to turn off. 

7. Click **Actions menu** , and select **Turn off** . 

8. In the confirmation dialog, click **Turn off** . 

   - The status of the workflow version changes to **Draft** . 

### What's next

Learn how to view workflow runs 

- (/gemini/enterprise/docs/workflow-builder/workflow-runs). 

Last updated 2026-10-14 UTC. 



## Edit a workflow

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-workflows

This page describes how to edit an existing workflow using natural language prompts or the visual editor. You can refine your workflow's logic, add or remove steps, update instructions for Gemini agents, or adjust integrations with tools and data sources. 

### Before you begin

Before using this feature, create a workflow. For information about creating a workflow, see Create a workflow 

(/gemini/enterprise/docs/workflow-builder/create-workflows). 

### Edit a workflow using natural language

App 

(#app) 

To edit a workflow using natural language prompts, do the following: 

1. Open your Gemini Enterprise web app in a browser. 

2. Navigate to an existing workflow in the flow builder. 

3. In the prompt bar in the flow builder, click **What would you like to change?** 

4. Enter a description of the change you want to make. For example: 

   - "Add a condition step that checks if the email has attachments." 

   - "Change the Gemini agent step's model to Gemini-2.5-flash." 

   - "Update the instructions to be more direct." 

   - "Add a loop that processes each search result." 

**Note:** If you select a specific node in the flow builder before entering a prompt, any changes requested are limited to that node. Edits will only be made to other parts of the workflow if the requested changes don't make sense for the node, or changes to other parts of the workflow are required to produce a valid configuration. 

5. Click **Submit** or press **Enter** . 

Gemini Enterprise applies the requested changes to your workflow. 

6. Review the updated workflow. Optionally, use the **Diff** and **Undo** options to view or revert changes as needed. 

7. To preview and test your workflow, switch to the **Preview** tab and click **Start simulation** . 

8. To make your updated workflow live, click **Turn on** (or click **Update** if the workflow is already live). 

**Note:** Natural language editing does not support all node types. If you request a change to an unsupported node, Gemini Enterprise provides an informative message and the node can be configured manually instead. 

### Edit using the visual editor

App 

(#app) 

To edit a workflow using the visual editor, do the following: 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** and go to the **Your agents** section. 

3. Locate the workflow that you want to edit. 

4. Click **Actions menu** , and select **Edit** . 

The workflow canvas appears with the last saved draft version of the workflow. 

5. Optional: To select another workflow version, click the **Turn on** or **Update** drop-down and select **Version history** . In the **Version history** pane, select the version that you want to modify. 

6. Click the component (trigger or step) in the canvas that you want to modify. 

The configuration pane for the component opens. 

7. Update the fields for the selected component, such as changing the schedule frequency or updating instructions for a Gemini Agent node. 

8. To add new steps, click **+ Add step** and select the required node type. 

9. To preview and test your workflow, switch to the **Preview** tab and click **Start simulation** . 

10. To make your updated workflow live, click **Turn on** (or click **Update** if the workflow is already live). 

### What's next

- Learn how to run test simulations for your workflow (/gemini/enterprise/docs/workflow-builder/simulate-workflows). 

- Learn about workflow versions 

- (/gemini/enterprise/docs/workflow-builder/publish-workflows#versions). 

Last updated 2026-10-14 UTC. 



## Share a workflow

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-workflows

Share workflows that you've created and launched using Workflow Builder with other users within your organization. 

With workflow sharing, you can: 

- Share live workflows with users and groups in your organization. 

- Set up custom run schedules or event-based triggers. 

- Track preview executions and automated runs. 

- Duplicate shared workflows to customize their steps. 

Depending on your app's feature control confgurationsi 

(/gemini/enterprise/docs/manage-web-app-features#configure-feature-controls), you might need an administrator to review and approve (#review-request) your request before you can share a workflow. 

If you share a workflow, the people you shared the workflow with will see and use the live version. 

**Caution:** When you share an agent, consider the following data access behaviors: 

- **Knowledge files:** Any user with access to the shared agent can query and view information from files uploaded to the agent's **Knowledge** section, even if they don't have direct access or permissions to the source files. For example, if you upload a confidential file to the **Knowledge** section, all users with access to the shared agent can ask questions about that file's content. 

- **Connectors and data stores:** When an agent accesses data through connectors, user access control lists (ACLs) and permissions are preserved. Users can only query and retrieve data from data stores and connectors that their individual user accounts are authorized to access. 

## Share a workflow

To share a workflow, do the following: 

App 

(#app) 

1. Open your Gemini Enterprise app and go to the **Agent Gallery** page. The **Agent Gallery** page appears displaying all the prebuilt agents and custom-built agents. 

2. In the **Your agents** section, find the workflow you want to share. 

**Note:** You can share a workflow that is in a **`draft`** state, but other users can't run it until it's turned on. 

3. In the upper right header of the Workflow Builder canvas, click **Share** . 

4. Enter the email addresses of the users or Google Groups that you want to share the workflow with. 

**Note:** You can share your workflow with individual user email addresses. Sharing with Google Groups isn't enabled for end users. A Gemini Enterprise app administrator or any user with the Discovery Engine Admin (discoveryengine.admin) (/iam/docs/roles-permissions/discoveryengine) role can enable group sharing at the Gemini Enterprise app level. 

5. Click **Done** . 

**Note:** If your app administrator has enabled administrator review for workflow sharing, a share request is sent to the app administrator for review and approval (#review-request). After the app administrator approves the request, the workflow is shared with those in the access list. You can, at any time, edit the share request to add or remove users, or cancel the request. 

### Administrator review control

By default, workflow owners can share their workflows with any user within their organization without approval from an app administrator. However, app administrators can change the app feature control confgurationsi (/gemini/enterprise/docs/manage-web-app-features#configure-feature-controls) to require administrator review and approval for sharing workflows in the app. 

By default, workflow owners can't share their workflows with groups. However, the Gemini Enterprise app administrator can choose to make workflows shareable with Google Groups— with or without administrator approval. 

#### The sharing process

Only the initial sharing of a workflow requires administrator review and approval. Subsequent workflow revisions don't need re-approval. 

Workflow sharing follows a two-step process when administrator review is enabled: 

1. The workflow owner shares the workflow with one or more users or Google Groups. 

2. The app administrator reviews the sharing request (#review-request) and approves or denies it. 

#### Review a share request

App administrators are responsible for reviewing and managing workflow sharing requests. 

**Notes:** 

- This section only applies if the Enable workflow sharing without administrator approval (/gemini/enterprise/docs/manage-web-app-features) feature is disabled in the app's feature controls. 

Only app administrators with the Gemini Enterprise Admin 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) IAM role 

can review and approve share requests. 

Console (#console) 

To review a share request as an app administrator, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Apps** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app containing the workflow. 

3. In the app navigation menu, click **Agents** . 

4. Find the workflow with a **Review share request** action in the **User permissions** column. 

5. Click **Review share request** . 

6. In the **Share request** pane: 

   - Review the access list under **Requested to share with the following users** . 

   - Optional: Modify the access list to add or remove user accounts, Google Groups, or WIF identity pools. 

7. To approve the request and grant access, click **Approve and enable** . 

8. To reject the request, click **Deny** . 

### Use a shared workflow

When a workflow owner shares a workflow with you, you can access and preview its graph configuration. While the workflow graph is read-only for shared users, you can run a preview manually, confgure your own trigger settingsi (#set-up-triggers), view your own run history (#view-runs), or make a copy of the workflow (#copy-workflow). 

App (#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

3. Go to the **Shared with me > From your org** section. 

4. Click the shared workflow you want to view. The workflow launches in a read-only designer layout, displaying the live node graph. Note: If the shared workflow is suspended or turned off, the Workflow Builder canvas doesn't render and you can't run it, but you can still view its previous runs. 

5. Optional: To perform a manual test run of the workflow: 

   - Click **Preview** in the upper right header of the Workflow Builder canvas. 

Run the preview. If the preview run fails because a connector used by the workflow is not authorized, click **Enable Connectors** below the error message to complete the OAuth flow. 

#### Set up your own triggers

Triggers on a shared workflow are user-specific. You can configure a custom run schedule or event filters to run a shared workflow automatically. 

To set up your own triggers, do the following: 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** > **Gallery** . 

3. Go to the **Shared with me > From your org** section and click the shared workflow you want to set up a trigger for. 

4. Access the trigger configuration: 

   - Select the **Actions** menu > **Set up triggers** . 

   - Alternatively, open the workflow in the Workflow Builder editor canvas, click the workflow name, and select **Set up triggers** . 

5. You can configure a trigger using either of the following modes: 

   - **Schedule:** Select **Run on a schedule** and configure when the workflow runs for you (such as the frequency and time zone). 

   - **Event:** Select **Run on app events** and configure the event filters to specify when the workflow runs for you. For example, for a Google Drive event trigger, you can filter by fields such as **Owners** (such as a Google ID like `janedoe` ) , **Name** , **MIME type** , **Modified time** , or **Parent folder** . You select an operator (such as **contains** or **equals** ), enter a value, and combine multiple rules using **AND** or **OR** conditions. 

6. If the workflow uses connectors that require authentication (for example, connectors used in a workflow step rather than the trigger itself), enable and authorize the connectors in the Workflow Builder canvas editor when prompted. 

7. Click **Save** . The trigger is saved and it runs the workflow automatically. You can manually trigger the workflow (/gemini/enterprise/docs/workflow-builder/simulate-workflows) to preview what will happen when the schedule or event trigger runs this workflow. If 

you want your workflow to stop running, select **Don't run on app events** or **Don't run on a schedule** from the **Set up triggers** dialog. 

#### View your runs

To view your runs, do the following: 

App 

- (#app) 1. In the web app navigation menu, click 

**Agents** . 

2. Go to the **Shared with me > From your org** section and click the shared workflow. 

3. In the Workflow Builder canvas, click the **Runs** tab. 

4. Click a specific run to view its execution logs and step-by-step trace. 

For more information, see workflow runs 

(/gemini/enterprise/docs/workflow-builder/workflow-runs#view-runs-workflow). 

#### Make a copy of a shared workflow

Shared workflows are read-only for shared users, except for their trigger configurations. If you want to edit and customize a shared workflow's steps, you can create a copy in your own workspace. 

To create an editable duplicate of the shared workflow, do the following: 

App 

(#app) 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** > **Gallery** . 

3. Go to the **Shared with me > From your org** section and click the shared workflow you want to copy. 

4. In the Workflow Builder editor canvas, click the workflow title, and select **Make a copy** . The copy is added to your **Your agents** list. 

### Shared workflow dependencies

If your workflow imports and references other workflows (sub-workflows) in its workflow steps, keep the following in mind: 

- **Access requirements** : When you share a parent workflow, or when you import a workflow into your workflow, ensure that all users in your access list also have access to all imported sub-workflows. 

- **Run failures** : If a user runs a workflow without access to an imported subworkflow, the run fails with a message asking them to request access from the owner. 

### Sharing limits

When sharing a workflow, the following limits apply: 

- **Maximum 1,500 individual accounts:** Workflow Builder manages agent access using underlying Google Cloud IAM allow policies, which enforce a hard cap of 1,500 members per policy. Sharing an agent with more than 1,500 individual user accounts causes the operation to fail with the following error: 

```
The number of members in the policy (1,501) is larger than the maximum
allowed size 1,500.
```

- **Use groups to share at scale:** Each Google Groups or Workspace group counts as a single member toward the 1,500-member policy limit. If you need to share an agent with hundreds or thousands of colleagues across an organization, ask your app administrator to enable group sharing 

(/gemini/enterprise/docs/manage-web-app-features#configure_feature_controls) and enter group email addresses (for example, `support-team@example.com` ) instead of individual user accounts. 

For a full list of system constraints, see Workflow Builder quotas and limits (/gemini/enterprise/docs/workflow-builder/quotas-and-limits). 

### Considerations

- If the workflow owner turns on a new version or updates the live version of the workflow, all shared users automatically run the new live version on subsequent executions. 

- If a workflow is turned off or suspended, the Workflow Builder canvas doesn't render and shared users cannot run the workflow, but they can still view their past run histories and session logs in the **Runs** gallery. If the workflow is unshared, disabled, or deleted, shared users lose all access, including to their past run histories and session logs. 

- Actions that modify external data require human-in-the-loop (HITL) approval, except for emails or calendar events you send to yourself. 

- App administrators can transfer ownership of a shared workflow to another user or to themselves in the Google Cloud console. If the workflow has a schedule trigger or event trigger, the transfer operation marks them as disabled schedules or events, and the new owner should enable them before using the agent. For more information, see Transfer agent ownership 

- (/gemini/enterprise/docs/share-custom-agents#transfer-ownership). 

### What's next

- Learn how to create a workflow 

- (/gemini/enterprise/docs/workflow-builder/create-workflows). 

- Learn how to edit a workflow 

- (/gemini/enterprise/docs/workflow-builder/edit-workflows). 

- Learn how to manage workfow versionsl 

- (/gemini/enterprise/docs/workflow-builder/manage-agent-versions). 

- Learn how to monitor workflow runs 

- (/gemini/enterprise/docs/workflow-builder/workflow-runs). 

View Workflow Builder quotas and limits 

- (/gemini/enterprise/docs/workflow-builder/quotas-and-limits). 

Last updated 2026-10-14 UTC.
