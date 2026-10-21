# Gemini Enterprise: platform, security, agents, cost, monitoring / App user guide to Gemini Enterprise Quickstart Guide
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 48-74, extracted 2026-10-18

Contains:
- App user guide (pages 48-52) https://docs.cloud.google.com/gemini/enterprise/docs/get-started
- Developer guide (pages 53-54) https://docs.cloud.google.com/gemini/enterprise/docs/developer-guide
- Gemini Notebook Enterprise (pages 55-61) https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview
- AlphaEvolve (pages 62-66) https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview
- Gemini Enterprise reference (hub page) (pages 67-67) https://docs.cloud.google.com/gemini/enterprise/docs/apis
- Gemini Enterprise resources (hub page) (pages 68-69) https://docs.cloud.google.com/gemini/enterprise/docs/resources
- Gemini Enterprise Quickstart Guide (pages 70-74) https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise

## App user guide

URL: https://docs.cloud.google.com/gemini/enterprise/docs/get-started

The guides in this section help **app users, knowledge workers, and team members** use Gemini Enterprise. They describe how to navigate the app experience, search grounded company data, interact with assistants, run custom skills, and build or execute agents. 

For an in-depth walkthrough of building AI agents and automating business workflows with Gemini Enterprise, you can watch this video: 

<!-- Start of picture text -->
Gemini Enterprise use cases: Workf l o<br>Google Cloud Tech<br>Watch on<br><!-- End of picture text -->

### Choose your app experience

Gemini Enterprise is available as both a web app and a mobile app. Select an experience to get started: 

#### Use the web app

#### Use the mobile app

Access the assistant on your web browser to query company data, create documents in Canvas, and build skills or agents. 

Access company data, chat with agents, use voice and camera multimodal inputs, and manage tasks on the go from your mobile device. 

### Your product journey in the Gemini Enterprise web app

To get started with Gemini Enterprise, choose a path based on your goals: 

##### Discover

Explore the capabilities of Gemini Enterprise and customize your experience: 

Assistant 

#### Chat with the assistant

Chat with the conversational AI assistant to answer questions using connected company data, verify sources, and draft high-quality content. 

Chat with assistant (/gemin Organize conversations (/ge 

Personalization 

#### Tailor the app to your needs

Adjust how the app looks and feels, and configure what data it can index to provide more relevant, personalized answers. 

Configure appearance (/gem Configure personalization (/ 

Assistant 

#### Access your data with assistant actions

Connect to Google Workspace and approved third-party apps like Jira or Microsoft to authorize the assistant to perform tasks on your behalf. 

Extend with actions (/gemin Connector files (/gemini/en 

Agents 

Skills 

#### Simplify complex work with agents

#### Complete activities using custom skills

Browse the Agent Gallery to find Google-made agents, tools shared by your organization, or custom multi-step agents created in Workflow Builder. 

Browse, install, and invoke domainspecific skills to standardize recurring workflows and get consistent, repeatable results in conversations. 

Agent Gallery (/gemini/ente Deep Research (/gemini/en Co-Scientist (/gemini/enterp 

Browse skills (/gemini/enter 

##### Create

Build your own customized experiences without needing to code: 

Assistant 

Assistant 

Notebooks 

#### Create documents and presentations in Canvas

Use Canvas as a dedicated side-byside workspace to draft, edit, and format documents and presentations directly alongside your conversation. 

#### Generate custom images and visual media

Bring your ideas to life by asking the assistant to generate custom images and visual media for your presentations, documents, and content. 

#### Use Gemini Notebook Enterprise

Create private notebooks to ground AI responses in your uploaded documents, Google Drive files, and web links, and generate audio overviews. 

Overview (/gemini/enterpris 

Agents Skills Build custom Build custom agents without skills for writing code reusable workflows Create, update, and edit single or multiTeach the assistant step agents in domain-specific Workflow Builder workflows and tasks using natural by defining reusable language prompts, instructions in a data connectors, and SKILL.md file with scheduled tasks. optional context files. Workflow Builder overview Create & manage skills (/ge Edit an agent (/gemini/ente Use skills in chat (/gemini/e 

##### Share and collaborate

Share your agents, skills, and conversations securely with your team or organization: 

Assistant 

Agents 

Skills 

Share Share custom Share custom conversations agents skills Export chat Share your custom Import and export transcripts and share agents securely with custom skill conversations, team members, definitions to share research responses, specific Google reusable instructions, 

|and assistant outputs|groups, or publish|rules, and domain-|
|---|---|---|
|securely with team|them to the|specific knowledge|
|members.|organization-wide<br>gallery.|across your team.|
|Share conversations (/gemi|Share an agent (/gemini/en|Share a skill (/gemini/enter|

### What's next

Example use cases (/gemini/enterprise/docs/use-cases/example-use-cases) by role, including finance, HR, legal, marketing, sales, and support. 

Last updated 2026-10-14 UTC. 



## Developer guide

URL: https://docs.cloud.google.com/gemini/enterprise/docs/developer-guide

This guide helps **developers, software engineers, and system integrators** build applications with Gemini Enterprise. Use these API references, authentication guides, and client libraries to programmatically integrate enterprise search and agent features into your software. 

#### Get search results from StreamAssist

#### Authenticate to Gemini Enterprise

How to get search results from StreamAssist programmatically 

How to authenticate to Gemini Enterprise programmatically 

(/gemini/enterprise/docs/get-answersfrom-streamassist) 

(/gemini/enterprise/docs/authentication) 

#### Client libraries

Gemini Enterprise API client libraries 

REST reference Gemini Enterprise API REST reference 

(/gemini/enterprise/docs/libraries) 

(/gemini/enterprise/docs/reference/rest) 

#### RPC reference

Gemini Enterprise API RPC reference 

(/gemini/enterprise/docs/reference/rpc) 

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 



## Gemini Notebook Enterprise

URL: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview

Gemini Notebook Enterprise is a highly compliant, enterprise-ready version of Gemini Notebook. 

Gemini Notebook is an AI-powered research and writing tool that helps you summarize and extract information across dense and complex sources. You do this by adding data sources, such as PDFs, Google Docs, Google Slides, and website URLs, to build a notebook. The AI grounds its responses in these documents. 

The base functionality lets you add these sources and interact with the content to query, chat, or generate summaries. 

While popular for personal use, the personal Gemini Notebook product lacks the compliance and administrative features necessary for enterprise environments. Gemini Notebook Enterprise shares key features with Gemini Notebook but is fortified with enterprise-grade security and compliance. 

**Note:** Gemini Notebook Enterprise is a Generative AI Service subject to the applicable terms of the agreement under which you access Google Cloud services. 

### Enterprise grade for notebooks

Gemini Notebook Enterprise runs in a Cloud-compliant environment. Your data is always within your Google Cloud project and can't be shared externally. 

Documents uploaded to a notebook within Gemini Notebook Enterprise are ingested into the Google Cloud environment and are subject to Google Cloud Terms of Service. This also applies to documents that have been uploaded to a notebook from Google Drive. 

### Limitations on Microsoft Excel Workbook documents

Microsoft Excel Workbook documents uploaded to a Gemini Notebook Enterprise notebook have the following limitations: 

- Within the general source size limits, Gemini Notebook Enterprise can process about 150,000 active cells in a single sheet. If your data is organized compactly, you might be able to upload a document with sheets containing a larger number of active cells. 

- If a document contains multiple sheets, each sheet is processed separately. 

- A single document must be less than 500 MB or 500,000 words. This is the general source size limits; see Usage limits (#usage-limits). 

- When processing XLSX files, Gemini Notebook Enterprise converts the content, including table structures and formatting, into an intermediate format to preserve the layout for analysis. This conversion process adds characters to represent the structure (for example, cell boundaries and rows). These additional characters are included in the total word count. As a result, an XLSX file with a visible word count less than 500,000 can still exceed the limit because of these added characters. For files with complex formatting or many cells, you might see a larger difference between the apparent word count and the system's calculated word count. 

### Usage limits

Limits for Gemini Notebook Enterprise are shown in the following table. 

|Feature or size|Limit|
|---|---|
|Notebooks|500 per user|
|Sources|300 per notebook|
|Source sizes|500 MB or 500,000 words per source|
|Queries|500 per user per day|
|YouTube video transcript sizes|500,000 words per transcript|
|Audio overviews|20 per user per day|

|Video overviews|20 per user per day|
|---|---|
|Mind maps|20 per user per day|
|Reports|20 per user per day|
|Slide decks|15 per user per day|
|Infographics|15 per user per day|
|Quizzes|100 per user per day|
|Flashcards|100 per user per day|

### Differences between Gemini Notebook and Gemini Notebook Enterprise

Some key differences between the personal Gemini Notebook (https://notebooklm.google) product, which is available to people with Google Accounts, and Gemini Notebook Enterprise are outlined in the following table: 

||Gemini Notebook|Gemini Notebook Ent|
|---|---|---|
||Users can't specify|Data stays in your Go|
|Data<br>residency||For more information<br>Enterprise Standard<br>regional processing c|
|||Enterprise data resid|
|||(/gemini/enterprise/d|

||Google Docs and Slides|Google Docs and S|
|---|---|---|
||Copied text|Copied text|
||Public URLs|Public URLs|
||YouTube video|YouTube video|
||PDFs|PDFs|
||TXT|TXT|
||Markdown|Markdown|
||Audio files|Audio files|
|Sources|Image files|Image files|
||When a source is uploaded or imported to Gemini<br>Notebook, a static copy of the document is created for<br>analysis. Gemini Notebook does not make changes to the<br>original file. Therefore, when you use Gemini Notebook, the<br>model relies on the static copy of the uploaded sources to<br>answer your questions and fulfill your requests.|DOCX (Microsoft W<br>PPTX (Microsoft Po<br>XLSX (Microsoft Ex<br>When a source is upl<br>Enterprise, a static c<br>analysis. Gemini Not<br>to the original file. Th<br>Enterprise, the mode<br>uploaded sources to<br>requests.|
|Usage limits|See<br>Gemini Notebook Help<br>(https://support.google.com/notebooklm/answer/16213268|)<br>The same or greater<br>Usage limits(#usage|
||Through a personal Google Account|Through one of the fo|
|||Cloud Identity(/id|
|Authentication||A third-party ident<br>Entra ID, Okta, Pin<br>SAML 2.0 identity|
||`https://notebook.google.com`|`https://notebook.`|
|Interface||`project=`_`PROJECT_NU`_|
|||Administrators config|
|||for their users throug|

|Sharing|Notebooks are private to a user. Notebooks can be shared<br>with viewer or editor permissions; either publicly or by<br>email links with other users.|Notebooks are privat<br>other users within th<br>share a notebook, th<br>always see the sourc<br>Predefined IAM roles<br>and grant viewer or e|
|---|---|---|
|||Notebooks can't be s|
||N/A|VPC-SC<br>(/vpc-service-con<br>products#table_g|
|Compliance||CMEK<br>(/gemini/enterpris|
|||Data residency(/g|
||Audio summaries can be shared through a link. Audio|When users get acce|
|Audio sharing|summaries are separate from the rest of the notebook.|the audio summaries<br>separately.|

### Separate administrator and user interfaces

There are two interfaces for Gemini Notebook Enterprise: 

- **Admin interface:** Administrators use the project's Google Cloud console UI to enable the Gemini Notebook capability and set up users authentication and authorization. Users with the Cloud NotebookLM Owner role can access the admin interface. 

- **User interface:** Your end users create and manage their notebooks through a UI that looks and behaves very much like the personal Gemini Notebook UI. The URL for the interface is unique for each project and must be distributed to users by the administrator. 

### User roles

There are five Identity and Access Management (IAM) roles predefined for Gemini Notebook Enterprise: 

Two roles are related to accessing Gemini Notebook Enterprise: 

**Cloud NotebookLM Admin (** **`roles/discoveryengine.notebookLmOwner` ):** Users with this role can configure identity settings, give users in a project access to Gemini Notebook Enterprise, and receive the URL for the user interface for sharing with end users. 

**Note:** Users with this role don't experience Guidebooks as chat-only because they have full access to all notebooks. 

**Cloud NotebookLM User** **(** **`roles/discoveryengine.notebookLmUser` ):** Users with this role can sign in to the user interface and create notebooks. Users must be granted this role in order to access Gemini Notebook Enterprise (including for free-trial subscriptions). 

The remaining three roles are the Cloud NotebookLM Notebook roles (Owner, Editor, and Viewer). Don't assign these roles through the admin interface. These roles get automatically assigned through the user interface, for example, when a user creates a notebook or shares a notebook with another user. 

### About data access, storage, and lifecycle

When your users add source data to a notebook, the data is stored in your project in the US or EU multi-region. Only Gemini Notebook Enterprise can access the data; that is, the data can't be accessed through any other Google Cloud service (such as Cloud Storage). 

When your users delete a notebook, the data is deleted along with the notebook. Similarly, when you delete the project, all the data is deleted. 

### Searching for notebooks through Gemini Enterprise

You can enable Gemini Notebook Enterprise as a data source in Gemini Enterprise. This lets your users use Gemini Enterprise to search for their notebooks by title. 

For more information about this Public Preview feature, see Enable Gemini Notebook Enterprise as a search source 

(/gemini/enterprise/docs/create-data-store#notebooklm-search). 

### Gemini Notebook Enterprise availability

You can purchase Gemini Notebook Enterprise as a standalone product or as part of Gemini Enterprise (https://cloud.google.com/gemini-enterprise). 

### About Gemini Enterprise and Gemini Notebook Enterprise

Gemini Enterprise is a parent product that includes both Gemini Notebook Enterprise and Gemini Enterprise (editions). 

- For information about Gemini Enterprise, see Gemini Enterprise overview (/gemini/enterprise/docs/overview). 

- For comparison between Gemini Notebook Enterprise and Gemini Enterprise, see Choose between Gemini Notebook Enterprise and Gemini Enterprise (/gemini/enterprise/docs/choose-product). 

Notebooks are accessible from both Gemini Notebook Enterprise and Gemini Enterprise apps if they share the same project and location. 

Last updated 2026-10-14 UTC. 



## AlphaEvolve

URL: https://docs.cloud.google.com/gemini/enterprise/docs/alphaevolve/developer-guide/overview

AlphaEvolve is a specialized AI coding agent that uses evolutionary methods to solve algorithmic discovery, mathematical search, and combinatorial optimization use cases. It is especially well-suited for use cases that fall into the category of NPcomplete or NP-hard optimization problems. 

AlphaEvolve takes as primary input blocks of code in a given programming language that define the algorithm discovery or combinatorial search use case that needs to be solved. The input code should be functionally correct but still require optimization to meet specific global (non-functional) performance criteria defined by a set of user-specified evaluation metrics. 

The agent uses a state-of-the-art evolutionary heuristic to search through the space of all possible algorithmic design choices and mathematical decision variables. This allows AlphaEvolve to identify new programs that incrementally improve performance on the target optimization objectives. 

AlphaEvolve executes this heuristic iteratively over multiple successive generations of candidate programs until it discovers a net-new solution that meets the overall performance targets required for the use case. 

### When not to use AlphaEvolve

You cannot use AlphaEvolve in the following scenarios: 

- **Basic code generation:** AlphaEvolve is not a general-purpose developer assistant (such as a Gemini CLI or coding assistant). It does not take pure natural language descriptions or incomplete, non-functional code to output baseline functional code. 

- **Linting and code style:** AlphaEvolve is not intended for basic code optimization like cleaning up code according to software engineering best practices or standard linting. 

AlphaEvolve is specifically designed for scenarios where optimizing code requires innovative new designs and execution graphs. It is built to search through a very large configuration space of possible solutions where all candidates are functionally correct, but only a subset meet the required global performance criteria. 

### Spectrum of optimization solvers and heuristics

The following table maps out where AlphaEvolve fits relative to classical optimization solvers and heuristics. 

|Solver category|Types of problems<br>typically addressed<br>by the category of<br>solver|Example<br>algorithms|AlphaEvolve<br>applicable?|AlphaEvolve<br>differentiating<br>capability|
|---|---|---|---|---|
|**Convex**<br>**optimization**<br>**methods with**<br>**continuous**<br>**variables**|Linear<br>programming<br>Quadratic<br>programming<br>Nonlinear<br>programming<br>Non-convex<br>optimization|Simplex method<br>Interior point<br>methods|Not suitable.<br>Existing<br>algorithms<br>provide exact<br>solutions and will<br>likely outperform<br>AE.||
|**Gradient based**<br>**methods**||Gradient<br>Descent<br>methods (SGD<br>and related<br>approaches)<br>Quasi-Newtonian<br>methods (BFGS,<br>L-BFGS)|||

|Solver category|Types of problems<br>typically addressed<br>by the category of<br>solver|Example<br>algorithms|AlphaEvolve<br>applicable?|AlphaEvolve<br>differentiating<br>capability|
|---|---|---|---|---|
|**Mathematical**<br>**programming**<br>**and formal**<br>**methods (i.e.**<br>**"Classic" OR**<br>**methods)**|Integer<br>programming<br>Mixed Integer<br>Linear<br>Programming<br>Constraint<br>satisfaction<br>problems|KKT based<br>methods<br>Constraint<br>relaxation (not<br>an algorithm per<br>se, but a method<br>used by multiple<br>algorithms)<br>Duality and<br>LaGrangian<br>based<br>approaches<br>Branch and<br>bound<br>Branch and cut|<br>Possibly<br>applicable.<br>Also, AE can be<br>used as a way of<br>augmenting<br>existing tools or<br>tuning them.||
|**Meta-heuristics**<br>**search methods**|Problems with<br>irregular / non-<br>differentiable<br>objective<br>functions.<br>Online<br>optimization<br>problems|Genetic<br>algorithms<br>Evolutionary<br>search<br>Simulated<br>annealing<br>Particle Swarm<br>Optimization|Possibly<br>applicable.<br>Also, AE can be<br>used as a way of<br>augmenting<br>existing tools or<br>tuning them.||
|**Bayesian**<br>**Optimization**|Problems with<br>unknown or<br>opaque-box<br>objective<br>functions.<br>Tuning ML<br>pipelines|Gaussian<br>Process based<br>Tree based (TPE,<br>SMAC)|Definitely<br>applicable.||

|Solver category|Types of problems<br>typically addressed<br>by the category of<br>solver|Example<br>algorithms|AlphaEvolve<br>applicable?|AlphaEvolve<br>differentiating<br>capability|
|---|---|---|---|---|
|**LLM + meta-**<br>**heuristics search**<br>**based agents**|Code and<br>algorithm<br>optimization use<br>cases<br>Problems with<br>unstructured /<br>semantic search<br>spaces (can't be<br>broken up into a<br>set of discrete<br>decision variables)<br>Optimize the<br>optimizer use<br>cases|AlphaEvolve<br>FunSearch<br>(legacy)|Definitely<br>applicable.<br>(either as a direct<br>optimization<br>method, or as a<br>way of improving<br>the existing<br>Bayesian<br>Optimization<br>approach)||

Last updated 2026-10-14 UTC. 



## Gemini Enterprise reference (hub page)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/apis

#### Authenticate to Gemini Enterprise

How to authenticate to Gemini Enterprise programmatically. 

#### Client libraries

Gemini Enterprise API client libraries 

(/gemini/enterprise/docs/libraries) 

(/gemini/enterprise/docs/authentication) 

#### REST reference

Gemini Enterprise API REST reference 

RPC reference Gemini Enterprise API RPC reference 

(/gemini/enterprise/docs/reference/rest) 

(/gemini/enterprise/docs/reference/rpc) 



## Gemini Enterprise resources (hub page)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/resources

#### Pricing

#### Quotas and overages

Pricing information for Gemini Enterprise. Contact sales for more details. 

Usage quotas, system limits, and overage pricing for your Gemini Enterprise resources. 

(https://cloud.google.com/geminienterprise#gemini-enterprise-appeditions-and-pricing) 

(/gemini/enterprise/docs/quotas-andoverages) 

#### Release notes

Details about updates to Gemini Enterprise. 

#### Data residency and ML regional processing commitments

(/gemini/enterprise/docs/release-notes) 

Supported geographic locations. 

(/gemini/enterprise/docs/locations) 

#### Compliance certifications and security controls

Learn about security controls and compliance certifications for Gemini Enterprise 

#### Billing questions

Learn about resources for common billing questions. 

(/gemini/enterprise/docs/billingquestions) 

(/gemini/enterprise/docs/compliancesecurity-controls) 

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 



## Gemini Enterprise Quickstart Guide

URL: https://docs.cloud.google.com/gemini/enterprise/docs/quickstart-gemini-enterprise

To see an example of how to get started with Gemini Enterprise, run the "Intro to Gemini Enterprise" notebook in one of the following environments: 

Open in Colab 

(https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/geminienterprise/intro_gemini_enterprise.ipynb) 

| View on GitHub (https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/gemini-enterprise/intro_gemini_enterprise.ipynb) 

Gemini Enterprise brings together the power of deep information retrieval, state-of-the-art natural language processing, and the latest in large language processing to understand user intent and return the most relevant results for the user. 

Before following this tutorial, make sure you have done the steps in Before you begin (/gemini/enterprise/docs/before-you-begin). 

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

Guide me (https://console.cloud.google.com/gemini-enterprise/?tutorial=gemini-enterprise--gemini-enterprise-intro) 

### Before you begin

1. Sign in to your Google Cloud account. If you're new to Google Cloud, create an account (https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project. 

<sup>**Roles required to select or create a project**</sup> 

- **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 

- **Create a project** : To create a project, you need the Project Creator role ( `roles/resourcemanager.projectCreator` ), which contains the `resourcemanager.projects.create` permission. Learn how to grant roles (/iam/docs/granting-changing-revoking-access). 

**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project. 

Go to project selector (https://console.cloud.google.com/projectselector2/home/dashboard) 

3. Verify that billing is enabled for your Google Cloud project 

   - (/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

4. Enable the Gemini Enterprise (Discovery Engine), Cloud Storage, Identity and Access Management APIs, if any are not already enabled. 

<sup>**Roles required to enable APIs**</sup> 

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role ( `roles/owner` ) . Otherwise, you can get this permission through the Service Usage Admin role ( `roles/serviceusage.serviceUsageAdmin` ) . Learn how to grant roles (/iam/docs/granting-changing-revoking-access). 

Enable the APIs (https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,discoveryengine.googleapis.com,stor 

5. Make sure that you have the following role or roles on the project: Gemini Enterprise Admin 

<sup>Check for the roles</sup> 

- a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project) 

- b. Select the project. 

- c. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

- d. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

<sup>Grant the roles</sup> 

- a. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project) 

- b. Select the project. 

- c. Click **Grant access** . 

- d. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account. 

- e. Click **Select a role** , then search for the role. 

- f. To grant additional roles, click **Add another role** and add each additional role. 

- g. Click **Save** . 

### Create a Gemini Enterprise app

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click **Create app** . 

3. Under **Your app name** , enter a name for your app. Your app ID appears under the app name. 

4. Select **global (Global)** as the location for your app. 

5. Under **External name of your company or organization** , enter the company or organization name. For this tutorial, you can use `Cymbal Bank` . 

6. Click **Create** . 

Once the app is created, you are redirected to the **Overview** page of your app. 

#### Create a data store

1. Under **Complete your setup** , click **Create Data Store** . 

2. Under **Cloud Storage** , click **Select** . 

3. Under **Unstructured Data Import (Document Search & RAG)** , make sure **Documents** is selected. 

4. Under **Synchronization frequency** , make sure **One time** is selected. 

5. Under **Select a folder or a file you want to import** , make sure **Folder** is selected. 

6. Enter the following value in the **`gs://`** field: 

```
gs://cloud-samples-data/gen-app-builder/search/cymbal-bank-employee
```

This Cloud Storage bucket contains PDF files for internal use by a fictional bank, Cymbal Bank. 

7. Click **Continue** . 

8. Under **Your data store name** , enter a name for your data store, and then click **Create** . 

The Google Cloud console redirects you to the Connected data stores page, and it shows the data store you just created. 

### Preview your app

**Note:** Because it takes a few minutes for the data stores to index and sync with the app, the preview isn't available immediately. 

1. In the navigation menu, click **Overview** to return to the overview page. 

2. Under **Your Gemini Enterprise webapp is ready** , click the link to visit the web app. 

3. To test the imported data, click **Connectors** and make sure that **Google Search** is not selected. 

4. In the search bar, ask a question about the data that we imported; for example, ask `How do I book business travel?` If the answer to this question doesn't specifically reference Cymbal Bank, wait a few more minutes and try again. 

5. Ask additional questions such as: `Who founded Cymbal Bank?` or `Where are the headquarters of Cymbal Bank?` 

### Configure the search web app

1. Return to the Google Cloud console. 

2. In the navigation menu, click **Configurations** . 

3. On the **Search UI** tab, configure settings for the search app. 

4. Under **Appearance and branding options** change the logo to this one for **Cymbal Bank** . 

```
https://storage.googleapis.com/cloud-samples-data/gen-app-builder/search/cymbal-bank-logo.png
```

5. If you change configurations on the **UI** tab, click **Save and publish** . 

6. Go to the **Autocomplete** tab to configure specific settings for autocomplete. 

Set **Enable autocomplete** to **Now** and expect to wait a day or two before you see autocomplete suggestions. 

7. Go to the **Assistant** tab to configure settings for the search assistant. 

On this page, you can set additional LLM system instructions, enable Model Armor, web grounding, and other settings related to the default assistant. 

### View the search web app

To view your Gemini Enterprise web app, do the following: 

1. In the navigation menu, click **Integration** . 

2. Make sure that **Enable the Web App** is enabled. 

3. In the **The link to your web app** section, click **Copy** and open the link in your browser. 

4. Optional: Share the search app with your users by copying the URL and sending it to them. Users can bookmark the web app URL for access. 

### Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

1. To avoid unnecessary Google Cloud charges, use the Google Cloud console (https://console.cloud.google.com/) to delete your project if you don't need it. 

2. If you created a new project to learn about Gemini Enterprise and you no longer need the project, delete the project (https://console.cloud.google.com/cloud-resource-manager). 

3. If you used an existing Google Cloud project, delete the resources you created to avoid incurring charges to your account. For more information, see Delete an app (/gemini/enterprise/docs/delete-app) and delete a data store (/gemini/enterprise/docs/delete-a-data-store). 

4. Follow the steps in Turn off Gemini Enterprise (/gemini/enterprise/docs/turn-off-gemini-enterprise). 

### What's next

Learn more about Gemini Enterprise (/gemini/enterprise/docs/overview). 

Learn more about apps and data stores (/gemini/enterprise/docs/apps-data-stores). 

(https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC.
