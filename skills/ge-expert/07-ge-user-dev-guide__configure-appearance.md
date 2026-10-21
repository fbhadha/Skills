# Gemini Enterprise: user guide, Workflow Builder, developer guide / Configure appearance to Use a chat agent
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 47-88, extracted 2026-10-18

Contains:
- Configure appearance (pages 47-49) https://docs.cloud.google.com/gemini/enterprise/docs/configure-appearance
- Configure personalization and memory (pages 50-62) https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization
- Share your conversations (pages 63-65) https://docs.cloud.google.com/gemini/enterprise/docs/share-conversations
- Browse agents with Agent Gallery (pages 66-70) https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery
- Workflow Builder overview (pages 71-73) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder
- Chat agent overview (pages 74-77) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/chat-agents
- Create a chat agent (pages 78-84) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent
- Use a chat agent (pages 85-88) https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-chat-agent

## Configure appearance

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-appearance

You can customize the appearance of Gemini Enterprise in a variety of ways, including adjusting the theme, chat density, and home page elements. 

_Configure appearance settings_ 

### Set the theme

To set the theme for Gemini Enterprise, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click the icon. 

3. Click **Appearance** . 

4. Under **Theme** , select from the following options: 

**System** : Use the same theme as your operating system. 

**Light** : Use a light theme. 

**Dark** : Use a dark theme ("dark mode"). 

### Adjust the chat density

To adjust the appearance of your chats with the assistant, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click the icon. 

3. Click **Appearance** . 

4. Under **Chat density** , select from the following options: 

   - **Comfortable** : Present your chats with the assistant in a larger and more readable font. 

   - **Compact** : Present your chats with the assistant in a smaller font, using less space. 

### Select elements shown on your home page

To select the specific elements shown on your personal Gemini Enterprise home page, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click the icon. 

3. Click **Appearance** . 

4. Under **Homepage elements** , select from the following options to be displayed on your home page: 

   - **Prompts** : A selection of prompt suggestions, such as **Translate text** , **Draft email** , and **Generate image** . 

   - **Shortcuts** : Direct links to data sources that your administrator has connected to Gemini Enterprise. 

- **For you** : Quick access to data from data sources that your administrator has connected to Gemini Enterprise (for example, Google Drive files that you've recently accessed with the assistant, or upcoming events in your Google Calendar). 

- **Notebooks** : Links to your notebooks in Gemini Notebook Enterprise. 

- **Announcements** : Links to internal news shared in your organization. 

Last updated 2026-10-14 UTC. 



## Configure personalization and memory

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization

You can personalize your Gemini Enterprise experience by allowing it to securely learn from your work. Personalization enables Gemini Enterprise to anticipate your needs, help you find information, and take action more efficiently. 

This document explains how personalization works, how you remain in control of your data, and how you can provide specific details and enable data sources for personalization. 

### Overview

As you use Gemini Enterprise, it builds a personal _Memory_ by understanding your individual needs and work patterns, leading to more relevant and context-aware assistance. When you connect your work applications, such as Microsoft Outlook and Microsoft OneDrive, Gemini Enterprise can extract insights from your email, calendar, and documents to provide deep contextual assistance. 

#### Key features unlocked by personalization

Personalization transforms Gemini Enterprise into a powerful work assistant that understands you and your projects. 

|Feature|Description|Examples|
|---|---|---|
|Understand your c|lose<br>Instantly recall recent interactions|Try the following prompts:|
|collaborators|and shared work with collaborators,<br>as Gemini Enterprise scans recent<br>emails, calendar, and documents to|"What have my`COWORKERS`and I<br>discussed recently?"|
||find relevant communications and<br>files.|"Help me prepare for my 1:1 with<br>my manager."|

|Feature|Description|Examples|
|---|---|---|
|Track your projects<br>and topics|Gemini Enterprise can synthesize<br>updates from recent related activity<br>across all of your connected apps.|<br>Try the following prompts:<br>"What's the latest on Project<br>Nova?"<br>"What are my priorities for<br>today?"|
|Gain insights from<br>your information and<br>session history|Never lose track of a recent<br>decision or action item. Get<br>answers formatted to your reading<br>preferences and relevant to your<br>location. Gemini Enterprise<br>remembers your recent<br>conversations and infers stylistic<br>preferences and location.|Try the following prompts:<br>"What are some notable<br>upcoming industry events in the<br>next few months?"<br>"What's a challenging weekend<br>project that combines my<br>interests?"|

#### Data control

Gemini Enterprise is built with privacy and transparency at its core. You're always in control of your personal information. 

- **User personalization profile** : A dedicated profile section lets you explicitly define your name, role, and industry, giving you more direct control over how Gemini Enterprise communicates with you. 

- **Manage connected sources** : You can view and disconnect any connected application from a central list at any time. If a source is disconnected, Memory no longer gathers insights from it. 

**Note:** Changes to connected data sources may take up to 24 hours to take effect. 

- **Manage saved memories** : You can choose whether to allow Gemini Enterprise to reference your specifically saved memories in conversations. You can also review and remove one or all of your specifically saved memories at any time. 

- **Admin controls** : For enterprise users, administrators can manage which data sources can be connected and can disable Memory and personalization profiles for all users. By default, Memory is turned on to provide a helpful experience from the start. 

### Add information to memory

In addition to what Gemini Enterprise learns from your interactions, you can build the memory by completing your profile, connecting data sources, and saving specific information as memories. 

#### Edit your profile

To tailor how Gemini Enterprise responds to your questions, you can provide specific details about your role and preferences. This information helps Gemini Enterprise understand your context and provide more relevant and helpful answers. 

To edit your profile, follow these steps: 

1. Navigate to your Gemini Enterprise app. 

2. Navigate to the personalization settings dialog: 

   - If you are a new user, click **Authorize Now** to authorize Gemini Enterprise to connect to your apps. 

   - If you have already authorized Gemini Enterprise to connect to your apps, click **Settings > Personalization** . 

_Edit your profile details_ 

3. In the **Profile** section, enter the following information. This information helps the assistant generate more relevant answers: 

   - a. For **Preferred name** , enter the name you'd like the assistant to use when responding to your queries. 

   - b. For **Your role or job title** , enter your job title. 

   - c. For **Your industry** , select the industry you work in. 

Your settings are automatically saved. 

4. Close the **Settings** dialog. 

#### Add conversation history and data sources

You can allow Gemini Enterprise to learn from your past conversations, enabling more relevant responses. You can also choose to connect specific data sources to enhance the memory. 

To enable learning from your conversation history and connect your data sources, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click **Settings > Personalization** . 

3. Under **Memory** , enable Gemini Enterprise to learn from your past conversations by clicking the **Conversation history** toggle to the on position. 

_Enable learning from your conversation history and connected data sources_ 

4. To connect a listed data source, click the toggle for the data source to the on position. 

Your settings are automatically saved. 

5. Close the **Settings** dialog. 

**Note:** If your administrator has connected your Gemini Enterprise app to Microsoft OneDrive or Microsoft Outlook data sources, then the toggle is in the on position by default. 

#### Save information as memories

To save specific information for future reference, you can ask Gemini Enterprise to remember the information. Gemini Enterprise stores that information as a saved memory, which you can view, update, or delete. 

Enable use of saved memories 

To allow enhanced responses from the assistant using saved memories, you must configure Gemini Enterprise to reference your memories in conversations. 

To enable use of saved memories, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click **Settings > Personalization** . 

3. Under **Reference saved memories** , click the toggle to the on position. 

_Enable learning from your saved memories_ 

Save an item of information as a memory 

You can save information as a memory in conversation with the assistant. 

In the chat box, enter a prompt using the word "remember": 

```
Remember that all new proposals for Project Walby should be reviewed by
@Roberto Moreno.
```

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Got it! I'll keep that in mind for any future conversations. I created a new memory: All new proposals for Project Walby should be reviewed by rmoreno@cymbalgroup.com. I've saved those for you in your saved memories. 

View your saved memories 

You can view a list of your saved memories by asking the assistant, or in the **Settings** dialog. 

**Using the assistant** 

To view your saved memories using the assistant, do the following: 

Enter a prompt asking the assistant for your "saved memories" or "saved preferences": 

```
What are my saved memories?
```

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Here are the memories I have saved for you: 

- **Project Walby:** All new proposals for this project should be sent to rmoreno@cymbalgroup.com for review. 

- **Professional Development:** You're working on improving your public speaking skills this quarter. 

- **Writing Style:** You prefer a professional, yet approachable writing style that avoids jargon and uses active voice. 

- **Personal Preference:** You like coffee. 

Let me know if you would like me to add, change, or remove any of this information. 

**Using Settings** 

To view your saved memories in the **Settings** dialog, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click **Settings > Personalization** . 

3. Under **Managed saved memories** , click **Manage** . 

_View your saved memories_ 

Update a saved memory 

You can update a saved memory in conversation with the assistant. 

In the chat box, enter the updated memory: 

```
Remember that my favorite color is green.
```

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Got it! I'll keep that in mind for any future conversations. 

I updated an existing memory: My favorite color is green. 

### Remove information from memory

The core memory feature is enabled by default. You can't disable the memory feature, but you can opt out of providing information from connected data sources, disable use of your saved memories, or delete saved memories. 

#### Remove conversation history or data sources

You can prevent Gemini Enterprise from learning using your past conversations, or remove specific data sources, using the toggles in the **Settings** dialog. 

To turn off learning from your past conversations or remove a specific data source from the Gemini Enterprise memory, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click **Settings > Personalization** . 

3. Under **Memory** , disable learning from your past conversations by clicking the **Conversation history** toggle to the off position. 

4. To disconnect a listed data source, click the toggle for the data source to the off position. 

**Note:** It takes up to 24 hours for a change to a data source to take effect in Gemini Enterprise. 

Your settings are automatically saved. 

5. Close the **Settings** dialog. 

#### Disable use of saved memories

You can prevent Gemini Enterprise from referencing your saved memories in your conversations. 

To disable referencing of your saved memories, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click **Settings > Personalization** . 

3. Under **Reference saved memories** , click the toggle to the off position. 

#### Remove saved memories

You can remove a saved memory using the assistant, or remove one or all of your saved memories in the **Settings** dialog. 

**Important:** After you delete a saved memory, the information in that saved memory might still be retained as long as the original conversation is saved. To completely remove the saved memory, delete that conversation as well. For information about managing your conversation history, see Manage your chat history 

(/gemini/enterprise/docs/assistant-organize#manage-your-chat-history). 

**Using the assistant** 

To remove a saved memory using the assistant, ask the assistant to "Forget" or "Remove from memory". 

In the chat box, enter a prompt such as the following: 

```
Forget my memory about Project Walby proposals.
```

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Got it! I'll keep that in mind for any future conversations. I deleted an existing memory. 

**Using Settings** 

To remove one or all of your saved memories in the **Settings** dialog, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click **Settings > Personalization** . 

3. Under **Managed saved memories** , click **Manage** . 

4. In the **Saved memories** dialog, click the icon next to a memory to delete it. 

5. To delete all saved memories, click **Delete all** . 

**Note:** If you delete saved memories in the **Settings** dialog, you may need to start a new conversation with the assistant for your changes to take effect. 

### Turn off personalization and memory

If you are an administrator, you can turn off memory and personalization profiles for all users within your organization. 

To disable memory and personalization profiles for all users, do the following: 

1. In Gemini Enterprise, go to the **Gemini Enterprise** page (https://console.cloud.google.com/gemini-enterprise/). 

2. Choose your Gemini Enterprise app. 

3. Click **Configurations > Feature Management** tab. 

4. To turn off personalization and memory, click **Memory and customization** . This setting is turned on by default. 

5. Click **Save** . 

### Troubleshooting

This section addresses common issues when configuring personalization or connecting data sources for Gemini Enterprise. 

#### Resolve "Error during authorization"

When attempting to enable personalization or connect data sources, you might encounter an `"Error during authorization"` message. To resolve this error, try the following solutions: 

**Resolve Advanced Protection Program** 

(https://support.google.com/accounts/answer/7519408/) **blocks** : If you are enrolled in Google's Advanced Protection Program, third-party authentication requests might be restricted. Your Google Workspace Super Administrator must manually mark the Gemini Enterprise OAuth client as trusted in the Google Admin console under **Security > Access and data control > API controls > Manage App Access** . 

- **Disable ad blockers and browser extensions** : Ad blockers or other privacy extensions might block the dialog required for authorization. Try temporarily disabling them or attempting the authorization in an Incognito (private) browser window. 

- **Clear cache and cookies** : Browser cache issues might cause the authentication flow to fail. Clear your browser's cookies and cached files before trying again. 

Last updated 2026-10-14 UTC. 



## Share your conversations

URL: https://docs.cloud.google.com/gemini/enterprise/docs/share-conversations

You can share your previous conversations with the assistant. When you share a conversation with someone, they can see all of the existing content of the conversation, including your prompts, the assistant's responses, and any generated content such as images or videos. They won't see any new prompts, responses, or generated content. 

**Important:** If a conversation contains sensitive or confidential information (including generated content), that information is visible to anyone with whom you share the conversation. If you have a Google Workspace account, your Google Workspace administrator can restrict who you can share conversations with. If someone who isn't allowed to access a conversation tries to open the link, they see an error message. 

**Note:** To share conversations, your Gemini Enterprise administrator must turn on the **Enable session sharing** toggle in the web app feature configurations. For more information, see Manage web app features (/gemini/enterprise/docs/manage-web-app-features). 

### Share a conversation

To share a conversation with the assistant, do the following: 

1. To share your current conversation, click the icon. 

2. To share a previous conversation: 

   - a. In the sidebar of your Gemini Enterprise workspace, under **Chats,** hover over the chat you want to share. 

   - b. Click the icon. 

_Share a conversation_ 

   - a. Click **Share** . 

3. Click **Create link** . A link to the conversation is automatically copied to your system clipboard. 

### View and manage your shared conversations

To view a list of conversations you've shared, do the following: 

1. Navigate to your Gemini Enterprise app. 

2. Click the icon. 

3. Click **Shared chats** . 

_View previously shared conversations_ 

For each shared conversation, you can see the title, when the conversation was shared, and the link. You can also delete the shared conversation. 

**Note:** If you delete a shared conversation, others are no longer able to view the conversation, but it's still available in your personal chat history. 

Last updated 2026-10-14 UTC. 



## Browse agents with Agent Gallery

URL: https://docs.cloud.google.com/gemini/enterprise/docs/agent-gallery

Agent Gallery lets you discover, run, and organize prebuilt and custom agents in Gemini Enterprise. 

To open the gallery, go to your Gemini Enterprise web app and click 

**Agents** in the app navigation menu. 

|Feature|Action|Where it appears|
|---|---|---|
|Search<br>bar|Find agents by name or description keyword in real time.|Top of the gallery.|
|Filter<br>chips|Filter visible agents by category (`All`,`Pinned`,`Made by`<br>`Google`,`From your organization`,`Your agents`,<br>`Marketplace`).|Below the search bar.|
|Pinned<br>agents|Pin frequently used agents for rapid one-click access.|Pinned gallery section and<br>the left navigation menu.|
|+ New<br>agent|Open Workflow Builder to build a new custom agent.|Upper-right corner of the<br>gallery.|

The following image shows the Agent Gallery layout: 

### Find agents in the gallery

You can find agents using the search bar, category filter chips, or a combination of both. 

#### Search for agents

1. In Agent Gallery, click the search bar. 

2. Enter the name, function, or keyword for the agent you want to find. 

3. The gallery updates the visible agents in real time. Matching agents remain grouped by category. 

**Note:** When a search query is active, the filter chip row dynamically updates to display only the categories that contain matching agents. 

#### Filter agents by category

Select a filter chip below the search bar to restrict the gallery view to a single category: 

- **All** : Displays all accessible agents across all categories (default view). 

- **Pinned** : Displays only agents that you have pinned for quick access. 

- **Made by Google** : Ready-to-use first-party agents created by Google, such as Deep Research (/gemini/enterprise/docs/research-assistant), Gemini Notebook Enterprise, and Co-Scientist. 

- **From your organization** : Custom agents created by colleagues and shared with your team or workspace. 

- **Your agents** : Custom agents created by you in Workflow Builder (/gemini/enterprise/docs/workflow-builder). Cards display their current status (such as **Draft** or **Live** ). 

- **Marketplace** : Third-party partner agents available to request from your administrator. 

When viewing a specific category, click **Show more** or **Show less** to expand or collapse the section grid. 

**Note:** In the Gemini Enterprise Frontline edition, access to agents created by your organization is limited to agents provisioned by your administrator. Full access to organizational agents requires Gemini Enterprise Standard or Gemini Enterprise Plus editions. 

Made by Google agents aren't available in the Gemini Enterprise Frontline edition. 

### Pin agents for quick access

You can pin frequently used agents so they are always accessible without searching the gallery. 

- **To pin an agent:** On any agent card, click the **Pin** icon. 

- **To unpin an agent:** Click the active **Pin** icon on the card, or hover over the agent in the navigation menu and click the **unpin** icon. 

When you pin an agent: 1. The agent card appears in the **Pinned** section at the top of Agent Gallery. 2. The agent is added to the left navigation menu under the **Agents** heading, allowing you to open the agent directly from anywhere in Gemini Enterprise. 

Pin selections persist across your web sessions. 

### Create and manage custom agents

- **Run an agent:** Click any agent card to start a conversation. You can also run an agent in conversation using `@agent_name` . 

- **Create a custom agent:** Click **+ New agent** in the upper-right corner of the gallery (or in the navigation menu) to open Workflow Builder (/gemini/enterprise/docs/workflow-builder). You can build: 

   - Chat agents (/gemini/enterprise/docs/workflow-builder/create-chat-agent): Conversational agents for dialog and specialized queries. 

   - Workflows (/gemini/enterprise/docs/workflow-builder/create-workflows): Multistep automated workflows configured with triggers and connector actions. 

- **Edit or delete an agent:** On any card in **Your agents** , click the more options menu ( **⋮** ) to edit (/gemini/enterprise/docs/workflow-builder/edit-chat-agent), **share** , or delete (/gemini/enterprise/docs/workflow-builder/delete-chat-agent) the agent. 

### Request access to agents from Google Cloud Marketplace

In Agent Gallery, you can browse available agents from partner vendors listed on Google Cloud Marketplace. 

To request access to an agent: 

1. In the Gemini Enterprise web app, click 

**Agents** in the app navigation menu. 

2. Select the **Marketplace** filter chip or go to the **Marketplace** section. 

3. Click the agent card you want to access. 

4. Click **Request access** to send a request to your administrator for review. 

When your administrator approves the request: 

- You receive a notification at the bell icon in the web app. 

- The agent appears in the **From your organization** section of Agent Gallery. 

- You can run the agent by typing `@agent_name` in conversation. 

Last updated 2026-10-14 UTC. 



## Workflow Builder overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder

Workflow Builder is an interactive no-code, low-code platform for creating, managing, and turning on chat agents (/gemini/enterprise/docs/concepts#ase-agents) and workflows (/gemini/enterprise/docs/workflow-builder/workflows) in your Gemini Enterprise web app. 

With Workflow Builder, you can: 

- **Create chat agents and workflows** using natural language prompts or the interactive visual editor. 

- **Build and orchestrate** deterministic or non-deterministic workflows using triggers, steps, and actions. 

- **Connect your chat agents and workflows to various data sources** (including Google, third-party, and custom data sources) and tools. 

- **Preview and simulate** the behavior of your workflows in the integrated testing environment. 

- **Publish, turn on, and share** chat agents and workflows with specific users or groups within your organization. 

**Schedule workflow executions** to run tasks on a recurring basis. 

### Agent types

The following table lists the types of agents that you can create using Workflow Builder: 

|Agent type|Description|Best for|
|---|---|---|

|Chat agents|Designed for conversational<br>interactions to complete specific<br>tasks. Responses depend on user<br>input and are primarily non-<br>deterministic. Can be single-step or<br>multi-step agents.<br>For more information about chat<br>agents, see<br>Chat agent overview<br>(/gemini/enterprise/docs/workflow-<br>builder/chat-agents)<br>.|Open-ended conversations without<br>fixed steps. For example, a<br>brainstorming assistant for project<br>ideas.<br>Dynamic tasks where user input<br>drives the flow. For example, a<br>customer support agent where the<br>next question depends on the<br>user's issue.<br>Q&A, data lookup, or personalized<br>assistance. For example, checking<br>Jira ticket status or summarizing a<br>specific email thread.|
|---|---|---|
|Workflows|Executed as a sequence of steps or<br>actions, combining AI automation<br>with human intervention. Logic can<br>be deterministic or non-deterministic.<br>For more information about<br>workflows, see<br>Workflow overview<br>(/gemini/enterprise/docs/workflow-<br>builder/workflows)<br>.|Multi-step processes with defined<br>sequence logic. For example,<br>automating an employee<br>onboarding checklist across tools<br>like Gmail and Google Calendar.<br>Tasks with AI automation and<br>human approvals. For example,<br>drafting a report with AI that<br>requires a user sign-off before<br>publishing.<br>Complex orchestrations with<br>conditional logic. For example,<br>routing sales leads to different<br>teams based on region and<br>budget.|

### Agent controls and security

Gemini Enterprise provides centralized oversight and granular security for all AI agents and workflows within an organization. 

While Workflow Builder empowers employees and non-admin users to build and deploy chat agents and workflows, these actions remain strictly governed by administrative policies. Specifically, the actions and tools available to any agent or workflow are limited to the data connectors, tools, and permissions provisioned by 

the Gemini Enterprise administrator. This ensures that agents and workflows operated by end users can only perform tasks and access information that are explicitly authorized, maintaining enterprise-grade compliance and data integrity. 

### What's next

- Learn how to create a chat agent 

- (/gemini/enterprise/docs/workflow-builder/create-chat-agent). 

- Learn how to create a workflow 

- (/gemini/enterprise/docs/workflow-builder/create-workflows). 

Last updated 2026-10-14 UTC. 



## Chat agent overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/chat-agents

A _chat agent_ is a type of agent that you can build using Workflow Builder (/gemini/enterprise/docs/workflow-builder) in your Gemini Enterprise web app. These agents are designed to interact with users in a conversational manner to complete a specific task. Chat agent responses depend on the user's input, making them primarily non-deterministic in nature. 

Chat agents are ideal for the following use cases: 

- Open-ended conversations without fixed steps. For example, a brainstorming assistant for project ideas. 

- Dynamic tasks where user input drives the flow. For example, a customer support agent where the next question depends on the user's issue. 

- Q&A, data lookup, or personalized assistance. For example, checking Jira ticket status or summarizing a specific email thread. 

### Before you begin

Before exploring these features, do the following: 

- Ensure that a Gemini Enterprise administrator has enabled the **Enable chat agents** feature toggle in your app's feature management settings. For more information, see Manage web app features 

- (/gemini/enterprise/docs/manage-web-app-features). 

- Ensure you have a Gemini Enterprise web app with the necessary data stores connected. For more information, see About apps and data stores (/gemini/enterprise/docs/apps-data-stores). 

### Chat agent canvas

The chat agent canvas is an interactive interface that you can use to build and refine your chat agent. The canvas is divided into two main modes: 

- **Chat mode** : the chat mode provides a conversational interface to build and refine your agent using natural language prompts. It's perfect for no-code users who want to use Gemini's intelligence to quickly develop and adjust their agent's details, instructions, or behaviors. 

- **Designer mode** : the designer mode provides a visual representation of your agent and is organized into two panes: 

   - **Chat pane** : this pane is similar to the chat mode, where you can interact with your agent in a conversational manner while viewing the changes to the agent in the designer pane. 

   - **Designer pane** : this pane provides a visual representation of your agent and is further divided into the following tabs: 

      - **Flow** : presents a visual representation of your agent's workflow and control logic. Use the **Flow** tab to view the overall details of your main agent, manage the main agent and all individual sub-agents, and to design complex, multi-step agents. 

      - **Schedule** : provides configuration options to set one or more execution schedules for your agent. 

**Preview** : provides a live, interactive test environment for your agent. Use the **Preview** tab to test the agent's functionality and response as you build. 

### Chat agent components

Chat agents can be single-step or multi-step agents. Single-step chat agents consist of a single agent node, which contains the logic for the agent. Multi-step chat agents are made up of a main agent node that is connected to one or more sub-agent nodes. Each sub-agent node is an independent agent with its own logic. 

### What's next

- Learn how to create a chat agent (/gemini/enterprise/docs/workflow-builder/create-chat-agent). 

- Learn how to create a workflow (/gemini/enterprise/docs/workflow-builder/create-workflows). 

Learn how to use a chat agent 

- (/gemini/enterprise/docs/workflow-builder/use-chat-agent). 

Last updated 2026-10-14 UTC. 



## Create a chat agent

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/create-chat-agent

You can create a new chat agent using the following methods: 

- Using a prompt (#create-agent-prompt): This is the quickest way to create a chat agent. You describe the agent's purpose, and Workflow Builder generates the initial version for you within your app. This is ideal for basic agents or as a starting point for more complex ones. 

- Using the flow builder (#create-agent-flow): This method gives you direct, granular control over the agent's design from the beginning. It's ideal for designing complex, multi-step agents that require specific subagent configurations and logic flows. 

These methods are flexible, and you can combine them to suit your requirements. For example, you can start with a prompt to generate the initial chat agent and then switch to the flow builder to visually refine its logic and add complexity. 

### Before you begin

- Ensure you have a web app with the necessary data sources connected. For more information, see Create an app (/gemini/enterprise/docs/create-app), Connect a Google data source (/gemini/enterprise/docs/create-data-store), and Connect a third-party data source 

- (/gemini/enterprise/docs/connect-third-party-data-source). 

- Ensure that you have enabled the Workflow Builder feature toggle for your web app. For more information, see Manage web app features 

- (/gemini/enterprise/docs/manage-web-app-features). 

### Best practices for creating agents

To ensure your agents perform effectively and efficiently, consider the following best practices: 

- **Define clear objectives:** clearly state what you want your agent to achieve. A well-defined objective helps in designing the agent's logic and evaluating its performance. 

- **Start small, then expand:** begin with a basic agent that handles core functionalities. Once it's stable, gradually add more features and complexity. 

- **Break down complex tasks:** for multi-step agents, divide large tasks into smaller, manageable sub-tasks. Each subagent should have a specific role. 

- **Test iteratively:** regularly test your agent at each stage of development. This helps identify and fix issues early. 

- **Provide clear instructions:** when using prompts, be specific and concise. Avoid ambiguity to ensure the agent understands its purpose. See Best practices for writing prompts to create an agent (#best-practice-prompt). 

- **Use connected data stores for large document libraries:** Gemini Enterprise loads files that you upload to an agent's **Knowledge** section (or attach in a chat session) directly into the model's context window on every turn, up to a combined limit of 800,000 tokens. For large static reference libraries, policy manuals, or dense PDFs (such as documents over 100 pages), ingest the documents into a connected data store and enable it under **Manage your data** rather than uploading the files directly. Reserve direct file uploads for smaller, session-specific documents or multi-sheet spreadsheets. See Knowledge base and file upload limits 

- (/gemini/enterprise/docs/workflow-builder/quotas-and-limits#knowledge-upload-limits). 

### Create a chat agent using prompts

Use this method to quickly build a chat agent using conversational input. 

App 

(#app) 

To create a chat agent using a natural language prompt, do the following: 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click **+ Create agent > Chat agent** . 

The agent canvas opens in chat mode. 

3. Enter a prompt that describes your agent's purpose and intended behavior. 

**Note:** You can't use conversational prompts to enable or connect to data stores from the _Cloud sources_ category (for example, BigQuery, Cloud Storage, Cloud SQL). Create your agent using the designer mode for such tasks. 

**Tip:** See Best practices for writing prompts to create an agent (#best-practice-prompt). 

4. Optional: Click 

**Manage your data** and enable or disable the data sources you want your agent to use. 

5. Optional: Click **Add files** to upload any additional reference materials for your agent to use. 

6. Click **Submit** . 

The chat agent canvas appears, displaying a live preview of your agent. 

7. In the **Preview** tab, interact with your agent to test and evaluate its responses. 

8. Optional: Refine your agent's function and behaviour by providing additional instructions in the left chat pane. 

9. To view the overall details of your agent, go to the **Flow** tab and click the main agent node. 

   - Optional: In the **Knowledge** section, click **Add files** to upload any additional reference materials for your agent. 

Optional: In the **Personalization** section, add starter prompts that guide users on how to interact with the agent. You can add as many starter prompts as you like, but the system shows you a random selection of up to three prompts at a time. 

10. Optional: Click the **Schedule** tab to configure execution schedules for your agent. For more information about agent schedules, see Schedule agent executions 

(/gemini/enterprise/docs/workflow-builder/schedule-chat-agent). 

11. Click **Create** to launch and start using your agent. 

**Note:** Exiting the agent canvas without clicking **Create** puts your agent in a _Draft_ state. 

#### Best practices for writing prompts to create a chat agent

The prompt you provide helps Gemini understand your goals and generate the best possible agent. To get clear and relevant responses, follow these guidelines and best practices: 

**Provide enough context to eliminate ambiguity** 

Be specific about what you want the agent to do. For example, specify the level of detail, the types of examples to use, or the required output. This helps Gemini Enterprise to generate an agent plan that is more relevant and specific to your needs. 

<sup>**Not recommended**:</sup> `Create an agent for sales emails.` 

<sup>**Recommended**:</sup> `Create an agent that drafts follow-up emails for new sales leads from my CRM. It should search for the contact's company, summarize their business, and suggest how our product can help them.` 

**Set boundaries or limitations on the agent's output** 

Define what the agent should and shouldn't do. You can set limits on the length of its responses, the format, the tone, or specific elements to include or exclude. This helps the agent stay focused and produce more predictable results. 

<sup>**Not recommended**:</sup> `Create a sales email agent.` 

<sup>**Recommended**:</sup> `Create an agent that drafts follow-up emails for sales leads. The drafts should always use a professional tone, be no` 

```
more than three paragraphs, and never include personal information about
the client.
```

**Prompt Gemini to ask you questions** 

Instruct Gemini to ask you questions, if needed. This allows Gemini to gather details that it might have missed, and ensures that the resulting agent plan meets your expectations. 

<sup>**Not recommended**:</sup> `Create an agent to handle sales emails.` 

<sup>**Recommended**:</sup> `I need an agent that can help me draft sales emails. First, ask me what information you need to effectively qualify a lead and draft a personalized message.` 

**Examples of effective prompts** 

- **Simple example:** `Create a sales email agent that drafts concise follow-up emails to new leads. The tone should be professional, and the email should be no more than three paragraphs.` 

- **Advanced example:** `Create an agent that automatically drafts sales emails to leads. Use my Gmail and access emails with the 'leads' label. First, ask me to confirm which leads you should prioritize and what the main` 

- `selling points are for each. Once you have this information, your drafts should be no more than three paragraphs and use a professional tone. Don't` 

```
include any technical jargon or slang and never include any personal
information about the client.
```

### Create a chat agent using the flow builder

Use this method for granular control over agent design, model selection, and multistep orchestration. 

App (#app) 

To create a chat agent using the flow builder, do the following: 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click **+ Create agent > Chat agent** . The agent canvas opens in chat mode. 

3. Click **Proceed to builder** to switch to designer mode. 

   - A default agent name, **My Agent** , is created in the canvas. 

4. To view and configure the node details, click the **My Agent** node and do the following: 

      - a. **Name:** enter a name for your agent. 

      - b. **Description:** enter a summary of the agent's purpose. 

      - c. **Instructions:** provide a detailed set of instructions that define the agent's objectives, tasks, and behaviors. 

      - d. **Model:** select the Gemini LLM model for the agent to use. 

      - e. **Data and tools:** click **Add data sources & tools** to add the data sources connected to your app. 

      - f. Optional: In the **Knowledge** section, click **Add files** to upload any additional reference materials for your agent. 

      - g. Optional: In the **Personalization** section, add starter prompts that guide users on how to interact with the agent. You can add as many starter prompts as you like, but the system shows you a random selection of up to three prompts at a time. 

5. Build your subagent flow: 

      - a. In the **Flow** tab, hold the pointer over the main agent node, and then click **Add subagent** . 

      - b. Configure the subagent details. 

6. Repeat _step 5_ as needed to complete your subagent flow logic. 

7. Optional: Click the **Schedule** tab to configure execution schedules for your agent. 

8. Click the **Preview** tab to interact with your agent to test and evaluate if your agent flow logic is performing as expected. 

9. Click **Create** to publish and start using your chat agent. 

**Note:** Exiting the Workflow Builder canvas without clicking **Create** puts your agent in a _Draft_ state. 

### What's next

- Learn how to use a chat agent 

- (/gemini/enterprise/docs/workflow-builder/use-chat-agent). 

- Learn how to schedule chat agent runs 

- (/gemini/enterprise/docs/workflow-builder/schedule-chat-agent). 

- Learn how to edit a chat agent 

- (/gemini/enterprise/docs/workflow-builder/edit-chat-agent). 

- Learn how to share a chat agent 

- (/gemini/enterprise/docs/workflow-builder/share-chat-agent). 

- Learn how to delete a chat agent 

- (/gemini/enterprise/docs/workflow-builder/delete-chat-agent). 

Last updated 2026-10-14 UTC. 



## Use a chat agent

URL: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-chat-agent

A _chat agent_ is a specialized conversational assistant designed to help you accomplish specific business tasks using natural language. Chat agents combine Gemini's conversational intelligence with your organization's connected data, documents, and business tools to deliver relevant, grounded responses. 

You can use custom chat agents created and shared across your organization, agents you build yourself, or **Made by Google** prebuilt agents available in your Agent Gallery. After a chat agent is created and published, you can start using and interacting with it. 

### Start a conversation with a chat agent

App (#app) 

To find and start using a chat agent, do the following: 

1. Open your Gemini Enterprise web app in a browser. 

2. In the web app navigation menu, click 

**Agents** . 

The **Agent Gallery** page appears, displaying all available prebuilt **Made by Google** agents and custom-built agents. 

3. Click the chat agent you want to use from the **Your Agents** or **Made by Google** sections. 

This opens the conversational interface for the agent. 

4. Start interacting with the chat agent using natural language prompts. If the agent includes starter prompt suggestions, click a prompt chip to use that prompt. 

### Agent functions and capabilities

Chat agents can assist with a wide variety of everyday workplace tasks depending on how they are configured. Core capabilities include: 

- **Answering questions and knowledge lookup:** Ask questions in plain language to get clear, synthesized answers grounded in your organization's internal documentation, policies, guides, and knowledge bases. 

- **Drafting and content creation:** Generate first drafts for emails, meeting agendas, status reports, project briefs, or executive summaries tailored to your preferred style, tone, format, and audience. 

- **Summarizing documents and threads:** Quickly extract key takeaways, action items, and executive summaries from long documents, reports, or communication threads. 

- **Data analysis and insights:** Analyze tables, spreadsheets, and metrics to identify trends, compare figures, and get plain-language summaries without needing complex formulas or queries. 

- **Task automation and actions:** Perform actions across connected business systems directly from the chat, such as creating Jira tickets, scheduling Google Calendar events, updating CRM records, or triggering workflows. 

- **Brainstorming and problem solving:** Use the agent as a collaborative thought partner to explore ideas, plan project steps, brainstorm solutions, or compare different approaches. 

- **Image and visual generation:** Create images, illustrations, or visual concepts based on descriptive text prompts (when image generation tools are enabled). 

### Data options

Chat agents can connect to and retrieve information from data sources across your organization: 

- **Google Workspace data:** Ground responses in data from your Google Workspace connectors, including Google Drive files (Docs, Sheets, Slides, 

PDFs), Gmail messages, Google Calendar events, and Google Sites. 

- **Third-party business applications:** Connect to enterprise tools like Jira, Salesforce, ServiceNow, Slack, Microsoft SharePoint, OneDrive, Microsoft Outlook, Confluence, and Zendesk to access real-time records and tickets. 

- **Uploaded files and knowledge base:** Access reference documents, guides, and manuals uploaded directly to the agent's knowledge base or attached by you in the chat session. 

- **Enterprise data stores:** Retrieve structured and unstructured data from centralized enterprise repositories, including BigQuery datasets and Cloud Storage buckets. 

- **Web search:** Supplement internal enterprise knowledge with real-time public web information (when web search is turned on for the agent). 

### Tips for interacting with chat agents

To get the best results when using a chat agent, follow these tips: 

- **Use starter prompt chips:** Many agents offer clickable starter prompt chips on the chat home screen that showcase common tasks and recommended prompt formats. 

- **Be specific about your goal:** Provide clear context in your prompt, including the target audience, format (such as bullet points or a table), and length requirements. 

- **Ask follow-up questions:** You don't need to start over if a response isn't quite right. Ask the agent to adjust tone, add detail, reformat, or shorten the answer in the same chat thread. 

- **Attach files directly in chat:** Click **Add files** in the chat box to upload a document, spreadsheet, or image for the agent to review and analyze in that conversation. 

- **Review supporting sources:** When an agent references connected data, click **Sources** at the bottom of the response to review the original documents or records used to formulate the answer. 

### What's next

- Learn how to schedule chat agent runs 

- (/gemini/enterprise/docs/workflow-builder/schedule-chat-agent). 

- Learn how to create a chat agent 

- (/gemini/enterprise/docs/workflow-builder/create-chat-agent). 

- Learn how to edit a chat agent 

- (/gemini/enterprise/docs/workflow-builder/edit-chat-agent). 

- Learn how to share a chat agent 

- (/gemini/enterprise/docs/workflow-builder/share-chat-agent). 

- Learn how to delete a chat agent 

- (/gemini/enterprise/docs/workflow-builder/delete-chat-agent). 

Last updated 2026-10-14 UTC.
