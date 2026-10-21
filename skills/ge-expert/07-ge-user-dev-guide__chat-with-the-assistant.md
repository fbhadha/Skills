# Gemini Enterprise: user guide, Workflow Builder, developer guide / Chat with the assistant to Extend the assistant with actions
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 5-46, extracted 2026-10-18

Contains:
- Chat with the assistant (pages 5-21) https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat
- Find and organize chats and files (pages 22-27) https://docs.cloud.google.com/gemini/enterprise/docs/assistant-organize
- Create and edit documents and slides in Canvas (pages 28-31) https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas
- Analyze data and create images and videos (pages 32-39) https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze
- Extend the assistant with actions (pages 40-46) https://docs.cloud.google.com/gemini/enterprise/docs/assistant-use-actions

## Chat with the assistant

URL: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-chat

In your app, you can chat about search results and uploaded content with the assistant. The assistant can provide summaries and answer questions through natural language conversations, and you can export the assistant's answers in common formats to share with others. 

## _Chat with the assistant_

When you ask a question, the assistant provides a summary based on the information it can find. You can then ask follow-up questions to refine the answer and get details based on the data that your app searches across. You can also provide your own context by uploading files for the assistant to analyze, or by mentioning specific people and documents in your prompt. 

**Important:** Older chats are automatically deleted after the retention period set by your administrator. The retention period is based on the **creation date** . For example, if the retention period is 60 days, the chat you started 60 days ago is deleted, even if you interacted with it yesterday. 

### Ask questions and view sources

To engage in a conversation with the assistant and view supporting sources: 

1. Type your question into the chat box. The assistant automatically provides a summary based on your search results. If you prefer to speak your question, see Use your voice to chat (#voice-chat) below. 

2. Ask follow-up questions to refine the answers. 

3. Review the assistant's real-time reasoning and actions using **transparent thinking** : 

   - **Plan explanation:** The assistant explains its plan and rationale before calling a tool or data source. 

   - **Tool activity:** An expandable section displays tool execution details between the thinking phase and the final answer. 

   - **Faster response:** This transparency delivers a faster time to first token (TTFT) and improves perceived latency without increasing total response time. 

**Note:** If you use the assistant in a language other than English, the transparent thinking text might initially appear in English. Once the response finishes, expand the section to view the steps and tool details in your language. 

4. To see the data sources the assistant used, click **Sources** at the end of the response. 

5. Hover over a listed source to highlight the portion of the result supported by that source. 

_View supporting sources for the response_ 

**Note:** The **Sources** button and side panel behave as follows during multi-turn chats: 

      - The **Sources** button is dynamic and is only displayed under the most recent response containing grounding metadata. 

      - When you submit a subsequent prompt or message, the **Sources** button is removed from all previous chat entries. Inline citation chips in older responses remain visible. 

      - If the right-hand **Sources** side panel is left open when a subsequent query is submitted, the panel stays open but its contents are cleared (displaying as empty) while the assistant is in a **Thinking...** state. 

- To get ideas about what to ask, do the following: 

   1. Click one of the prompt suggestions below the chat box, such as **Help me write** . A list of specific prompts appears. 

   2. Click one of these specific prompts, such as **Help me write a blog post. Ask me about the topic and purpose** , to start a new conversation using that prompt. 

### Use your voice to chat

As an alternative to typing, you can use your voice to enter questions in the chat box. Hands-free dictation can be especially helpful when drafting longer queries or prompts. 

**Note:** Before you can use your voice to chat, your administrator must turn on the **speechto-text** feature. For more information, see Manage web app features 

(/gemini/enterprise/docs/manage-web-app-features). 

To use your voice to enter a query or prompt, do the following: 

1. In the chat box, click the icon to start recording. 

If your browser prompts you for permission, click **Allow** to enable recording. 

2. Speak clearly into your device's microphone. 

3. Click the icon to stop recording. 

The recording is transcribed but not stored. 

4. Review the transcribed text in the chat box, and edit it if necessary. 

5. Click **Submit** . 

If your voice isn't being recorded or transcribed, check the following: 

|Issue|Root cause|Recommended action|
|---|---|---|
|No transcription<br>appears|Microphone permission<br>might be blocked in your<br>browser.|Give the microphone permission to record.|
|Inaccurate<br>transcriptions|Background noise or low<br>input volume.|Speak directly into your microphone, or adjust<br>your system's microphone input volume in your<br>OS settings.|

### Chat with files in connectors

Gemini Enterprise can analyze content and generate answers from the following connectors: 

**Note:** A Gemini Enterprise admin must enable the required actions for the Gemini Enterprise assistant to access the content, allowing you to chat with the files. 

|Connectors|Supported files|Required connector actions|
|---|---|---|
||CSV|Download document|
|Google Drive|PDF<br>PPTX<br>XLSX|For more information, see the<br>Google Drive supported<br>actions<br>(/gemini/enterprise/docs/connectors/gdrive#supported-<br>actions)<br>.|
||CSV|Download document|
|Microsoft<br>SharePoint|PDF<br>PPTX<br>XLSX|For more information, see the<br>Microsoft SharePoint<br>supported actions<br>(/gemini/enterprise/docs/connectors/ms-<br>sharepoint#supported_actions)<br>.|
|Microsoft Outlook|Email<br>attachments|Download attachment<br>For more information, see the<br>Microsoft Outlook<br>supported actions<br>(/gemini/enterprise/docs/connectors/ms-<br>outlook#supported-actions)<br>.|
||CSV|Download file|
|Box|PDF<br>PPTX<br>XLSX|For more information, see the<br>Box supported actions<br>(/gemini/enterprise/docs/connectors/box#supported-<br>actions)<br>.|

To chat with files, do the following: 

1. Ensure that you have authorized Gemini Enterprise to access the data in the connector. For more information, see User authorization 

   - (/gemini/enterprise/docs/connect-existing-data-store#user_authorization). 

2. In the chat box: 

      - a. Click **Connectors** and make sure that the connector you want to chat with is turned on. 

      - b. Turn off the other connectors and Google Search when using this feature. For example, to chat with files in the Microsoft SharePoint connector, only enable the Microsoft SharePoint connector. 

_Turn on the Microsoft SharePoint connector_ 

3. Enter a prompt or query in the chat box. If you know the filename, include it in your prompt to help narrow the search. For example: "Summarize the key points in the file 'Q3-Marketing-Budget.xlsx'." 

#### Best practices

When chatting with files in connectors, follow these best practices: 

- Avoid ambiguous or overly broad questions to prevent the model from overthinking. Be ready to ask follow-up questions to narrow the scope. 

- If the model suggests an action, such as removing duplicate rows, ask followup questions to confirm that the action is necessary for your task. 

- The assistant displays executed code for XLSX and CSV files. Review this code to understand your data was processed. 

### Upload and chat about files

The assistant can analyze files that you upload, such as PDFs, images, and videos. You can also add files from your connected Google Drive or Microsoft OneDrive Business accounts. 

**Note:** The first time someone in your organization adds a file from Microsoft OneDrive Business, your tenant might require administrator approval. If it does, users see a **Need admin approval** screen when they sign in to Microsoft Entra ID: "Please ask an admin to grant permission to this app before you can use it." To resolve this, a Microsoft Entra ID Global Administrator or Application Administrator for your tenant must complete the first authorization: 

1. In the Gemini Enterprise web app, click the icon in the chat box, and then click **Add from OneDrive Business** . 

2. Sign in with the administrator account. If the **Need admin approval** screen appears, click **Have an admin account? Sign in with that account** . 

3. On the permissions screen, select **Consent on behalf of your organization** , and then click **Accept** . 

This step is required only once for your tenant. After the administrator completes the authorization, other users can add files from OneDrive without the approval screen. For more information, see the Microsoft Entra ID documentation 

(https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent). 

To chat about uploaded content, do the following: 

1. In the chat box, click the icon. 

<!-- Start of picture text -->
Upload files to the assistant<br><!-- End of picture text -->

2. Upload one or more files to the assistant. 

3. Enter a prompt or query in the chat box. 

#### File formats and size limitations

The following table lists the file formats and size limitations for files that you can upload to the assistant: 

|File type|Description|
|---|---|
|Images|Maximum image size: 30 MB|
||Supported file extensions:`.png`,`.jpeg`|

File type Description 

Documents Maximum document size: 

PDF: 100 MB 

XLSX: 50 MB<sup>1</sup> The XLSX limit applies to the size of the file after it's decompressed. Gemini Enterprise automatically converts each worksheet in a multi-sheet XLSX workbook into a separate table so the assistant can analyze data across all sheets. 

CSV: 7 MB<sup>1</sup> 

DOCX: 3 MB 

PPTX: 100 MB 

Text: 7 MB 

Markdown: 2 MB 

JSON: 1 MB 

JavaScript: 1 MB 

HTML: 0.5 MB 

CSS: 1 MB 

Java: 1 MB 

Python: 2 MB 

Supported file extensions: `.pdf` , `.xlsx` , `.csv` , `.docx` , `.pptx` , `.txt` , `.md` , `.json` , `.js` , `.html` , `.css` , `.java` , `.py` 

Video Maximum document size: 200 MB 

Supported file extensions: `.mp4` 

Audio Maximum document size: 200 MB 

Supported file extensions: `.mp3` 

1 The size limits for XLSX and CSV files aren't row limits. For large spreadsheets, the assistant analyzes the data by running code instead of reading the entire file directly, so responses can take longer. For tips on getting faster responses with large spreadsheets, see Best practices for faster responses (#faster-responses). 

**Note:** In addition to per-file byte limits, the combined content of all files uploaded in a chat session (including any static knowledge files attached to a custom chat agent) and the conversation history can't exceed **800,000 tokens** . Even if a file is within the byte size limit, exceeding the 800,000-token budget returns a **`FILE_SIZE_TOO_LARGE`** or **`Input too long`** error. To avoid this limit, start a new chat session, split large PDFs (such as manuals over 100 pages) into smaller topical files, or ask your administrator to index large document collections in a connected data store. 

### Add context with mentions

You can mention an agent, person, or uploaded file in your chat with the assistant by typing `@` in the chat box. You can launch a workflow agent by entering `@` and the workflow agent name in your chat prompt. 

To add an agent, person, or file to the chat, including launching a workflow agent, do the following: 

1. Type `@` . Gemini Enterprise opens a list of suggested agents, people, and files that you can select from. 

_Mention agents, people, or files in the chat_ 

2. Continue typing to filter the suggestions, or select one from the list. 

### Best practices for faster responses

The time that the assistant takes to respond depends on how much information it needs to search, retrieve, and process. To get faster responses, follow these best practices: 

- **Turn on only the connectors that you need.** In the chat box, click **Connectors** and turn off the connectors, custom MCP servers, and Google Search that aren't relevant to your question. Each additional source adds searches and tool calls before the assistant can start answering. 

- **Start a new chat when you change topics.** The assistant considers the earlier messages and files in a conversation when it answers. Long conversations with many turns or attached files take longer to process. 

- **Attach only the files that you need.** Large or numerous uploaded files increase processing time. To get faster responses with large spreadsheets (XLSX and CSV files), do the following: 

   - Keep only the sheets, columns, and rows that you need for your question. 

   - Split large workbooks into smaller files, and ask focused questions about specific columns or values. 

   - For large tables or tables that you query often, store the data in BigQuery and connect a BigQuery data store 

   - (/gemini/enterprise/docs/connectors/connect-bigquery) instead of uploading the file. 

- **Ask specific questions.** Include names, dates, filenames, or other details that narrow the scope. Broad questions can cause the assistant to search more sources and take more steps. 

- **Use data stores for large or frequently used data.** Data that is ingested into a Gemini Enterprise data store is typically faster to search than data that the assistant retrieves live from a third-party system through a federated 

connector. For more information, see Introduction to connectors and data stores (/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores). 

If responses are consistently slow or time out for all users on your corporate network, ask your administrator to review Configure proxies, frewalls, and TLSi inspection (/gemini/enterprise/docs/private-ui-access#configure-proxies). 

### Limitations

The following limitations apply when using the assistant with the listed data sources: 

Data source 

Limitation 

Admin restrictions 

If you use both Gemini Enterprise and Google Workspace, your Google Workspace administrator can restrict your access to Gemini Enterprise and its features. An administrator can use security settings to restrict the following: 

   - Your access to Gemini Enterprise in Google Workspace entirely. In this case, you can't invoke Gemini Enterprise agents in Google Workspace. 

   - Access to some or all Google Workspace data by Gemini Enterprise. In this case, you can use all Gemini Enterprise features, including agents, but they can't use any or only some of the Google Workspace data your account can access, including Google Drive files and Gmail messages. 

- Google Sharing Gemini Enterprise conversations (Gemini Enterprise - Business edition Workspace only). In this case, any one who has the link to your chat will see an error message when they try to open it. 

If you think you should have access, you can reach out to your Google Workspace administrator for help. If you're not sure who that is, see Who is my administrator? (https://support.google.com/a/answer/6208960) 

Content owner restrictions 

Gemini has the same access to Google Workspace data as you do, so it can only access files in Drive that have been shared with you. Additionally, if a file's owner doesn't allow you to download, copy, and print the file, Gemini can't access it even if it's shared with you. Learn more about sharing settings (https://support.google.com/drive/answer/2494893#prevent_download_print_copy) 

All data Images from data sources aren't rendered in the chat. sources 

Data Limitation source The following search queries are not supported: Searching for most recent or oldest emails. For example, `first` , `earliest` , `latest` , and `most recent` . Fetching email threads to generate answers. Microsoft Gathering information from multiple emails. Outlook Using words based on their intent or semantics, rather than their literal meaning (Microsoft Outlook search does not support this). Getting information from email attachments, unless they are explicitly mentioned in the email's subject or body. Microsoft Queries that request to list the items in a directory are not supported. OneDrive 

Microsoft Queries that request to list the items in a directory are not supported. SharePoint 

### Export to Google Docs and Google Sheets

You can export the assistant's responses to Google Docs and export tabular and CSV data to Google Sheets. 

To export results, do the following: 

To export a response to Google Docs, click the icon at the bottom of the response, then click **Export to Docs** . 

To export a table to Google Sheets, click **Export to Sheets** . 

To export CSV data to Google Sheets, click **Export to Sheets** . 

The exported file uses the same name as the chat session. 

### Provide diagnostic information for support

If you encounter a problem with the assistant's responses, you can help Support to resolve the problem by providing diagnostic information for troubleshooting. 

To obtain this information: 

1. Go to the end of the problematic conversation and click the icon. 

2. Click **Show diagnostic info** . The **Diagnostic info** dialog appears. 

3. Click **Copy token** . The information is copied to your system clipboard. 

Provide the copied information when you contact Support for help with the conversation. 

### Usage limits

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

- Your project reached its monthly spend cap. 

- Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 

This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

Last updated 2026-10-14 UTC. 



## Find and organize chats and files

URL: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-organize

Gemini Enterprise provides tools to search your content, star items for quick retrieval, pin agents for quick access, and manage your chat history. 

### Search your Gemini Enterprise content

You can use the main search bar to find your chats, generated images and videos, and other personal content within your Gemini Enterprise workspace. 

To search your content within Gemini Enterprise: 

1. Click the icon in the upper left to reveal the search window. 

2. Enter your search terms. 

You can search for the following: 

- A chat title 

- A phrase from a chat 

- A filename 

- A description of an image or video 

- An agent 

### Star items for quick retrieval

You can **star** important items, such as chats, files, or images, to help you find them later. 

To star an item: 

1. Open a chat, file, or image in your Gemini Enterprise workspace. 

2. Click the icon and click **Add to starred** . 

To see all of your starred content collected in one place: 

1. Click the **Search** and then the icon. 

### Pin agents for quick access

To keep frequently used agents readily available, you can pin them to the top of the list in the sidebar. 

To pin an agent: 

1. Go to **Agents** . 

2. Locate the agent you want to pin, and click the icon. 

### Manage your chat history

You can view and manage the recent and pinned chats that you have had with the assistant. 

To manage a chat: 

1. In the sidebar of your Gemini Enterprise workspace, under **Chats,** hover over the chat you want to manage. 

2. Click the icon. 

3. Choose an option: 

- **Share:** Share a previous chat with someone else in your organization. For more information, see Share your conversations (/gemini/enterprise/docs/share-conversations). 

**Note:** A Gemini Enterprise administrator must turn on the **Enable session sharing** setting for the share feature to show on the Gemini Enterprise web app. 

- **Add to starred:** Keep frequently used chats at the top of your list in the sidebar. 

- **Rename:** Customize chat names to make them easier to identify. 

- **Delete:** Remove chats from your pinned and recent lists after they're no longer needed. 

**Important:** Older chats are automatically deleted after the retention period set by your administrator. The retention period is based on the **creation date** . For example, if the retention period is 60 days, the chat you started 60 days ago is deleted, even if you interacted with it yesterday. 



## Create and edit documents and slides in Canvas

URL: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-canvas

Canvas is a dedicated, interactive tool within Gemini Enterprise that helps you create AI-generated documents and slide presentations from your conversations. You can work on your documents and slides side-by-side with your chat, without needing to switch between applications. 

### Before you begin

Before you can use Canvas in Gemini Enterprise, an administrator must enable the feature toggle and configure any necessary permissions. For more information, see Configure Canvas (/gemini/enterprise/docs/configure-canvas). 

### Create a document or a slide in Canvas

To create a document or a slide in Canvas: 

1. Sign in to the Gemini Enterprise web app. 

2. Start a new chat. 

3. Click **Tools** in the chat box. A list of shortcuts appears. 

4. Select **Canvas** , or enter a prompt that implies creating a document or slide. 

5. Enter a prompt. 

**Note:** Your chat conversation history, content from enabled connectors, and explicitly added sources are used as input. 

6. (Optional) To upload files or an image with your prompt, click **+ Add files** . 

7. Click **Submit** . The document or the slide presentation opens in the Canvas editor on the right. 

#### Source citations

To view the references and search results used to generate documents, click **Sources** directly under the AI's response. 

For slides, a final **Image Sources** slide is automatically included, containing all the metadata for the images used in your deck. 

### Edit a document in Canvas

You can edit a document in the following ways: 

- **Direct edits** : In the Canvas space, you can manually add, edit, or delete text, change formatting like headings, bold, and italics, and create bulleted and numbered lists. Changes are auto-saved. 

- **AI-powered edits** : At the bottom right of the Canvas panel, use the **Change length** and **Change tone** sliders for global adjustments to tone and length, or provide detailed chat feedback for more specific edits. 

- **Highlight to edit** : To refine a specific section of text, highlight it and enter your instructions in one of two ways. You can type directly into the **Ask Gemini** box that appears next to your selection, or use the main prompt box to tell Gemini Enterprise how you want that section rewritten. 

You can also use the undo and redo options on the toolbar to navigate between different saved versions of your document. 

**Note:** Canvas supports editing content generated during your active session. To edit further, export (#export_documents_and_slides_from_canvas) your content to another application. 

### Edit a slide in Canvas

To open and edit a slide presentation in Canvas: 

1. Go to the chat where you generated the slides. 

2. Click **Open** . 

3. In the chat box, enter your suggestions to update the slides. 

4. Click **Submit** . 

**Note:** Each update generates a completely new Canvas artifact. The existing artifact is not modified or versioned. 

### Export documents and slides from Canvas

You can export documents and slides from Canvas to download and edit it in your preferred application. 

<sup>Export a document</sup> 

To export a document from Canvas: 

1. Open the chat with the Canvas document that you want to export. 

2. At the top right of the Canvas panel, click **Export** . You can export to Google Docs, DOCX, or PDF. 

3. You can also copy all text to your clipboard. To copy all text, at the top right of the Canvas panel, click **Copy** . 

<sup>Export a slide presentation</sup> 

- To export a slide presentation from Canvas: 

   1. Open the chat with the Canvas slides that you want to export. 

   2. At the top right of the Canvas panel, click **Export** . You can export to Google Slides, Microsoft PowerPoint, or PDF. 

### Limitations

Canvas isn't supported on the mobile app. It is only available on the web app. 

### Best practices

When generating content in Canvas, follow these best practices: 

- For complex documents and presentations, provide clear and detailed prompts, with other Gemini Enterprise knowledge artifacts as sources and template references. 

- Always review and edit the AI-generated content to ensure that it meets your requirements. 

Last updated 2026-10-14 UTC. 



## Analyze data and create images and videos

URL: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-analyze

Beyond simple conversations, the assistant offers advanced tools that let you perform complex actions, from analyzing data and generating reports to creating custom images and videos. 

### Access actions with the Tools menu

To access tools within a chat: 

1. Click the **Tools** button in the chat box. A list of shortcuts appears. 

_Open the Tools menu_ 

2. Select a tool from the list. Some of the tools that might be available to you let you perform the following tasks: 

   - **Search internal sources** to limit Gemini Enterprise to searching your enterprise data when responding to prompts. 

   - **Search Google** to limit Gemini Enterprise to searching the web when responding to prompts. 

   - **Run Deep Research** , a Made by Google agent, to research a topic in depth. 

- **Generate images** to generate an image based on your description using Gemini Enterprise. 

- **Create videos** to generate a video based on your description using Gemini Enterprise. 

**Note:** Made by Google agents aren't available in the Gemini Enterprise Frontline edition. 

### Analyze data and create reports

The assistant can analyze data you provide by uploading files, pasting data, or referring to search results. You can ask the assistant to perform calculations and create tables or reports from your data. 

To analyze data, do the following: 

1. (Optional) Upload a file. 

**Note:** The first time someone in your organization adds a file from Microsoft OneDrive Business, your tenant might require administrator approval. If it does, users see a **Need admin approval** screen when they sign in to Microsoft Entra ID: "Please ask an admin to grant permission to this app before you can use it." To resolve this, a Microsoft Entra ID Global Administrator or Application Administrator for your tenant must complete the first authorization: 

- a. In the Gemini Enterprise web app, click the icon in the chat box, and then click **Add from OneDrive Business** . 

- b. Sign in with the administrator account. If the **Need admin approval** screen appears, click **Have an admin account? Sign in with that account** . 

- c. On the permissions screen, select **Consent on behalf of your organization** , and then click **Accept** . 

This step is required only once for your tenant. After the administrator completes the authorization, other users can add files from OneDrive without the approval screen. For more information, see the Microsoft Entra ID documentation 

(https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent) . 

2. Enter a prompt. Example prompts for data analysis include the following: 

   - "Can you tell me what the total revenue for December is?" 

   - "Which product had the highest sales?" 

   - "Generate a sales report for the last quarter, including a breakdown by product category and a comparison to the previous year." 

### Generate an image

If your admin has enabled image generation, you can use the assistant to generate custom visuals like artwork, UI mockups, and charts from a text prompt. 

To create an image: 

1. In the chat box, click **Tools > Generate an image** . 

2. Describe the image that you want Gemini Enterprise to create and submit the prompt. Example prompts for image and chart generation include the following: 

   - "Generate a high-fidelity mockup of a mobile banking app with a clean, minimalist design, displaying a user's account balance and recent transactions." 

   - "I need a visualization of our customer demographics. Can you create a chart showing the distribution of age, gender, and location?" 

_Generate a custom image_ 

3. After generating the initial image, upload existing images or enter follow-up text prompts to refine the generated image. 

4. You can export any finished image or chart in PNG format. 

### Generate a video

If your admin has enabled video generation, you can use the assistant to create a short video based on your description. 

To create a video: 

1. In the chat box, click **Tools > Generate a video** . 

2. Describe the video that you want Gemini Enterprise to create and submit the prompt. 

_Generate a custom video_ 

3. After you receive the assistant's response, you can send follow-up prompts to refine the result. 

### View, download, and search generated images and videos

If your admin has enabled image or video generation, you can view and download generated images and videos from your previous chats. You can also search your generated content using natural language. 

To view, search, and interact with your generated content: 

1. Click **Library** . Your generated images and videos are shown. 

_View all of your generated content_ 

To filter results by type, click **Images** or **Videos** . 

2. Click a generated visual to view it. 

_Interact with your generated content_ 

Choose an option: 

- To open the chat where you generated an image or video, click the icon. 

- To copy an image, click the icon. 

To download an image or video, click the icon. 

3. Click the icon to search your generated images and videos. Type a description of what you're looking for. 

**Note:** The search results show up to 10 matching images and videos. 

_Search your generated content_ 

### Usage limits and overages

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

Your project reached its monthly spend cap. 

- Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 

This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

Last updated 2026-10-14 UTC. 



## Extend the assistant with actions

URL: https://docs.cloud.google.com/gemini/enterprise/docs/assistant-use-actions

With assistant actions, you can ask the assistant to perform tasks for you in other applications, like scheduling a meeting in Google Calendar or sending an email in Gmail. This lets you handle relatively low-effort tasks efficiently, freeing you up for other work that requires more involvement. 

See the following sections for information about available actions. 

**Note:** The actions available to you depend on which services your administrator has configured. If you don't see an option you expect, contact your organization's administrator. 

### Authorize your connected services

Before you can use actions in the assistant, you must authorize the specific connected service to act using your account. 

To authorize actions for a service: 

1. In the chat box, click the **Manage your data** icon. 

2. Find the service you want to authorize, and click **Enable actions** . 

3. Sign in to the service if necessary, and follow the prompts to authorize it. 

_Authorize a connected service_ 

After you authorize the connected service, you can ask the assistant to perform actions using that service on your behalf. 

### Schedule an event in Google Calendar

If your administrator has configured Google Calendar actions, you can ask the assistant to create Google Calendar events for you. 

To create an event, do the following: 

1. Ask the assistant to schedule the event, providing some basic information. For example, you can say, "Schedule a meeting with Amal, Charlie, and Kim at 3 PM tomorrow." 

2. Edit the draft event created by the assistant. 

_Provide event details to the assistant_ 

Enter any of the following for your event: 

|Field|Description|
|---|---|
|Attendees|A list of email addresses for everyone who should be invited. You're<br>automatically included.|
|Title|The name of the event.|
|Start time|When the event begins.|
|Duration|How long the event lasts. The default is 30 minutes.|

Field Description 

Time zone The time zone for the event. If you don't specify one, your own time zone is used. 

DescriptionAny additional information about the event. 

3. If you have not previously used the assistant to manage Google Calendar, click **Authorize** to grant the necessary permissions. 

**Note:** The first time that you use the assistant to manage your Google Calendar, you might be asked to grant permissions for both Google Calendar and Gmail. Gemini Enterprise uses a single connection for both tools, so you only have to grant permission once. Approving this request allows the assistant to help you with both your calendar and email seamlessly. 

4. Click **Send** . The assistant creates the event in Google Calendar and sends an email to your selected attendees. 

### Send an email in Gmail

If your administrator has configured Gmail actions, you can ask the assistant to send emails for you. 

To create and send an email, do the following: 

1. Ask the assistant to send the email, providing some basic information. For example, you can say, "Send an email to Ariel and ask about the status of the design revisions. CC Izumi and Tristan." 

2. Edit the draft email created by the assistant. 

_Provide email details to the assistant_ 

Enter any of the following for your email: 

|Field|Description|
|---|---|
|To|A list of everyone who should receive the email.|
|Subject|The subject line of the email.|
|Content|The body of the email, which can be in Markdown format.|
|CC|A list of anyone who should be CC'd on the email.|
|BCC|A list of anyone who should be BCC'd on the email.|

3. If you have not previously used the assistant to manage Gmail, click **Authorize** to grant the necessary permissions. 

**Note:** The first time that you use the assistant to manage your Gmail, you might be asked to grant permissions for both Gmail and Google Calendar. Gemini Enterprise uses a single connection for both tools, so you only have to grant permission once. Approving this request allows the assistant to help you with both your email and calendar seamlessly. 

4. Click **Send** . The assistant sends the email to your selected recipients. 

### Usage limits

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

Your project reached its monthly spend cap. 

- Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 

This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC.
