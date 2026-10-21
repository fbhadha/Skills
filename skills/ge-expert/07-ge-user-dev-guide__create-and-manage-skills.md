# Gemini Enterprise: user guide, Workflow Builder, developer guide / Create and manage skills to Draft legal correspondence
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 206-247, extracted 2026-10-18

Contains:
- Create and manage skills (pages 206-212) https://docs.cloud.google.com/gemini/enterprise/docs/skills
- Use the mobile app (pages 213-214) https://docs.cloud.google.com/gemini/enterprise/docs/use-the-mobile-app
- Use Gemini Notebook Enterprise within Gemini Enterprise (pages 215-217) https://docs.cloud.google.com/gemini/enterprise/docs/access-notebooklm
- Example use cases (pages 218-220) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/example-use-cases
- Get reminders and manage tasks (pages 221-221) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/reminders-and-tasks
- Analyze financial statements and calculate ratios (pages 222-223) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/analyze-financial-statements
- Detect anomalies in transaction data (pages 224-225) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/anomaly-detection-transaction-data
- Draft a financial report narrative (pages 226-227) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/financial-report-narrative
- Summarize an earnings call transcript (pages 228-232) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/earnings-call
- Create personalized onboarding materials (pages 233-234) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/personalized-onboarding
- Analyze internal salary data (pages 235-235) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/internal-salary-analysis
- Conduct legal research (pages 236-238) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/legal-research
- Prepare for a deposition (pages 239-242) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/deposition-witness-preparation
- Draft legal correspondence (pages 243-247) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/draft-legal-correspondence

## Create and manage skills

URL: https://docs.cloud.google.com/gemini/enterprise/docs/skills

Skills are reusable custom instructions that help the Gemini Enterprise assistant perform specific tasks, such as reviewing legal contracts or writing in your brand voice. 

**Note:** To create skills, your administrator must turn on the skills feature. Similarly, to share skills, your administrator must also enable skill sharing, which they can configure to require administrator review or allow immediate sharing. For more information, see Manage skills (/gemini/enterprise/docs/manage-skills). 

Each skill is a package containing a `SKILL.md` prompt file. A skill package can also include scripts, files, or background context that the assistant uses to complete a task. By default, Gemini Enterprise turns on skills that you create. 

### Supported editions

The ability to create, upload, or use skills depends on the Gemini Enterprise edition (/gemini/enterprise/docs/editions) that you subscribe to: 

- **Standard, Plus, and Pay-as-you-go** : You can create and upload custom skills, and use Google-managed skills and user-created skills shared with you. 

- **Frontline** : You can browse, install, and use Google-managed skills and usercreated skills shared with you. You can't create or upload custom skills. 

### Overview

Key aspects of skills include: 

- **Open Standard** : Built on the open skills standard, each skill is defined by a core `SKILL.md` file and can be extended with additional files or scripts. 

- **Modular extension:** Skills let you teach an agent domain-specific tasks using custom instructions and context. 

- **Dynamic access:** Gemini Enterprise accesses these specialized instructions automatically when they are relevant to your question or task. 

### Create a skill

**Note:** You can't create skills with the Gemini Enterprise Frontline edition. For more information, see Supported editions (#supported-editions). 

To create a new skill in the Gemini Enterprise web app, follow these steps: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Skills** . 

3. Click the icon and click **Create skill with Gemini** . 

4. Enter a name for your skill. 

5. Enter a description. Gemini Enterprise uses the description to determine whether the skill can help with a prompt or task. You can also add trigger instructions to the description to help guide Gemini Enterprise. 

6. Provide the skill instructions using natural language in the chat box or by manually editing the Markdown details. 

7. Click **Save** . Gemini Enterprise turns on the new skill by default. 

### Upload a skill

**Note:** You can't upload skills with the Gemini Enterprise Frontline edition. For more information, see Supported editions (#supported-editions). 

To add existing skills, upload them as Markdown or ZIP files. Gemini Enterprise automatically extracts the skill name and description from the `SKILL.md` file. In the `SKILL.md` file, make sure the description explains when to use the skill. 

If you upload a ZIP file containing multiple folders or files, you must include the `SKILL.md` file in the root directory. The ZIP archive can also include optional directories, such as a `scripts/` directory containing Python or Bash code. 

To upload a skill, follow these steps: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Skills** . 

3. Click the icon and click **Upload skill** . 

4. Drag or browse for the Markdown or ZIP file, and click **Import** . Gemini Enterprise turns on the skill by default. 

### Browse skills

You can browse and install skills by using the following sections to filter the list: 

|Section|Description|
|---|---|
|All|Both Google-managed skills and user-created skills.|
|Google|Built-in skills provided by Google.|
|Shared with me|Read-only, user-created skills that other users have shared with you.|

To browse and install a skill, follow these steps: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Skills** . 

3. Click the icon and click **Browse skills** . 

4. Find the skill you want to use and click **+ Install** . 

### Update a skill

To update an existing skill, follow these steps: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Skills** . 

3. Click the name of the skill that you want to update. 

4. Click the icon next to the skill and click **Edit** . 

5. Make the necessary updates to the instructions, name, or description. 

6. Click **Save** . 

To return to the Skills page, click **Skills** . 

### Share a skill

If your Gemini Enterprise administrator enables skill sharing, you can share skills that you create with other users. 

**Note:** Sharing a skill doesn't send an email notification. To find the skill, recipients must go to the **Shared with me** section in Browse skills (#browse-skills). 

To share a skill, follow these steps: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Skills** . 

3. Find the skill you created and want to share. 

4. Click the icon next to the skill and click **Share** . 

5. In the **Share skill** dialog, enter the comma-separated email addresses of the users you want to share the skill with. 

6. Click **Done** . 

**Note:** If your Gemini Enterprise administrator requires approval for share requests, other users can't access the skill until your administrator approves the request. 

### Use a skill

You can use skills directly within your chat conversations in the Gemini Enterprise web app. 

#### Test a skill from the Skills page

You can test a skill directly from the **Skills** page by starting a new chat session with that skill: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Skills** . 

3. Click the icon next to the skill and click **New chat** . Gemini Enterprise opens a new chat referencing the selected skill. 

#### Invoke a skill in a conversation

You can invoke skills dynamically during a conversation to tailor the assistant's responses. 

**Note:** You can use skills and agents dynamically, but you cannot invoke both an agent and a skill in the same prompt. 

When chatting with the Gemini Enterprise assistant, you can use skills in the following ways: 

- **Manual mentions:** You can explicitly invoke a skill using the `@` or `/` mention feature in the chat box (for example, `@Brand Voice` or `/Brand Voice` ) . Typing `/` opens a menu displaying only your available skills, while typing `@` opens the general mentions menu. 

- **Direct requests:** If you need Gemini Enterprise to use a specific skill, you can ask for it directly in your prompt. For example, `Use the brand voice skill to review this` . 

- **Automatic selection:** Gemini Enterprise automatically uses a skill when it is relevant to your task based on the skill's description and trigger instructions. 

### Turn off a skill

To prevent Gemini Enterprise from using a specific skill, turn it off. When you turn off a skill, Gemini Enterprise doesn't invoke it in conversations. 

To turn off a skill, follow these steps: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Skills** . 

3. On the **Skills** page, find the skill that you want to turn off. 

4. Click the toggle next to the skill to the **Off** position. 

### Uninstall a skill

To remove an installed skill from your **Skills** page, follow these steps: 

1. Sign in to the Gemini Enterprise web app. 

2. In the navigation menu, click **Skills** . 

3. Click the icon next to the skill and click **Uninstall** . 

**Note: Turning off** a skill pauses automatic triggering but keeps it on your **Skills** page. **Uninstalling** a skill removes it from your **Skills** page, but the skill remains available in **Browse skills** for you to reinstall. 

### Skill states

In addition to turning skills on or off yourself, your administrator can change the state of a skill, which affects its availability: 

**Suspended:** Your administrator temporarily deactivates the skill. It remains visible on the **Skills** page with a suspended status, but other users cannot 

invoke it in conversations until the administrator re-enables it. Skill owners can update and test the skill. 

- **Disabled:** Your administrator temporarily hides the skill from other users, removing it from their **Skills** page. The skill remains visible to the skill owner, who can update and test it until the administrator re-enables it. 

- **Deleted:** Your administrator permanently removes the skill from the Gemini Enterprise web app, so you can no longer use it. 

### Limitations

This section lists the limitations for skills in Gemini Enterprise: 

- Skills are not available for use with agents. 

- Skills support Python and Bash execution only. 

- The web app editor lets you manually or naturally create skills that use a single `SKILL.md` file. You must upload more complex skills that require additional scripts or files as a ZIP file. 

- Natural language skill creation does not use your conversation context or connectors as inputs to create a skill. 

- Skills work best with Canvas when a skill has only one `SKILL.md` file. 

### What's next

Learn how administrators manage skills (/gemini/enterprise/docs/manage-skills). 

Last updated 2026-10-14 UTC. 



## Use the mobile app

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-the-mobile-app

This page describes the steps required before Gemini Enterprise mobile app users can access the app's suite of features to manage data, collaborate with AI agents, and complete tasks, all from a mobile device. 

### Before you begin

As an app user, you must first install the Gemini Enterprise mobile app. To install the mobile app onto your mobile device, follow these steps: 

1. Install the **Google Gemini Enterprise** app from the Apple App Store or Google Play. 

2. To connect to your organization's specific environment you can use one of the following options based on how the Gemini Enterprise administrator has configured the Gemini Enterprise app: 

   - Scan the configuration QR code in the web app 

   - Obtain a unique access link from your administrator. 

3. Tap the link on your mobile device or scan the QR code to open the app, and sign in using your company credentials. 

### Mobile features

The Gemini Enterprise mobile app includes the following key features: 

- **Agent Gallery:** After signing in, the home screen serves as a central hub (Agent Gallery) where you can browse and launch available agents. 

- **Multimodal input:** You can use your device's camera to provide photos as direct context for your query, such as, "Summarize the text on this whiteboard", or upload files from your device. 

- **Interactive Actions:** Agents can suggest actions, such as sending emails, which appear as interactive cards that you can review and confirm directly in 

the chat. 

- **Chat management:** You can organize your history by starring important conversations, renaming sessions, or deleting them. 

- **Voice:** You can input your query through voice and listen to the response in audio format. 

- **Speech to Text** : You can use the microphone to input your query in audio format. The audio gets transcribed to text which shows in the input box. The audio is ephemeral and not stored. 

- **Text to Speech** : The generated answer can be read in audio format by pressing the speaker button next to the answer. 

Last updated 2026-10-14 UTC. 



## Use Gemini Notebook Enterprise within Gemini Enterprise

URL: https://docs.cloud.google.com/gemini/enterprise/docs/access-notebooklm

Gemini Notebook Enterprise is integrated with Gemini Enterprise. This page describes how end users access Gemini Notebook Enterprise from within the Gemini Enterprise search web app UI and how they can add documents found in searches to a notebook. 

**Note:** In the Gemini Enterprise Frontline edition, Gemini Notebook Enterprise support is limited to interacting with published notebooks. Creating new notebooks requires the Gemini Enterprise Standard or Gemini Enterprise Plus editions. 

### Access Gemini Notebook Enterprise from the web app

To access Gemini Notebook Enterprise, do the following: 

1. Open the Gemini Enterprise web app. 

2. In the app navigation menu, go to **Agents** . 

3. In the **Made by Google** section, click **Gemini Notebook** . 

The Gemini Notebook Enterprise interface opens in the web app. 

The notebooks that you created in a particular project and location through the Gemini Notebook Enterprise site are accessible from within Gemini Enterprise web apps. Similarly, notebooks created from within a Gemini Enterprise app are accessible from the Gemini Notebook Enterprise site. 

### Add a source to a notebook from Gemini Enterprise (Private preview)

**Preview:** To use this feature, your project must be on the allowlist. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

When Gemini Enterprise returns search results, you might want to add those search results to a notebook. For many document types, you can do this from the search web app with a single click. 

Not all document types can be added to notebooks as sources. For example, you can add Google slides but not emails. If a document type can't be added, then the **Add content to…** button isn't available. 

#### Notebook source limitations and security

Here are a couple of security considerations related to sources in notebooks: 

- Sources as instances: When you add a document as a source to a notebook, a _copy_ of the document is added to the notebook. This means that there are now two copies of the document, one that belongs to original owner and one that belongs to the owner of the notebook. Changes to the original document aren't reflected in the copy. This has security implications: if you want to change who can access the information, you need to make the change on both documents, the original and the copy. 

Shared notebooks: 

- Sources in shared notebooks: If a notebook is shared with others, you can't add more sources to it. This restriction is to maintain access control. See Notebooks that can't be shared 

- (/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks#no-sharing). 

- Shared notebooks as search sources: If a notebook is shared with you, but you aren't the owner, Gemini Enterprise doesn't use it as a data source for search results. This restriction is to maintain access control and aligns with the security behavior of other data connectors. 

#### Procedure

To add a document returned by search as a source to a notebook, do the following: 

1. Click book_4_spark **Add content to…** . 

2. Choose to add the content to one of the following: 

   - A new notebook 

An existing notebook 

Last updated 2026-10-14 UTC. 



## Example use cases

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/example-use-cases

The following pages provide examples of how to use Gemini Enterprise to accomplish a variety of goals or tasks in various contexts. 

For an in-depth walkthrough of building AI agents and automating business workflows with Gemini Enterprise, you can watch this video: 

<!-- Start of picture text -->
Gemini Enterprise use cases: Workf l o<br>Google Cloud Tech<br>Watch on<br><!-- End of picture text -->

FILTER BY 

<!-- Start of picture text -->
Use Case Category<br> General<br> Finance<br> HR<br> Legal<br> Marketing<br> R&D<br> Sales<br> Software<br> Support<br><!-- End of picture text -->

Filter results Accelera Analyze Analyze te concepts fnanciali material and stateme s research nts and discover methodo calculate y logies ratios 

(https://docs .cloud.googl e.com/gemin i/enterprise/ docs/usecases/accele ratematerialsdiscovery? hl=en) 

(https://docs (https://docs .cloud.googl .cloud.googl e.com/gemin e.com/gemin i/enterprise/ i/enterprise/ docs/usedocs/usecases/analyz cases/analyz e-conceptse-financialresearchstatements? methodologi hl=en) es?hl=en) 

Query the properties of a material or predict the… 

#### Analyze internal salary data

(https://docs .cloud.googl e.com/gemin i/enterprise/ docs/usecases/intern al-salaryanalysis? hl=en) 

Ensure internal pay equity and competitiv… 

#### Create personali zed onboardi ng material s

Obtain Analyze raw general financial information statements, about… calculate k… 

#### Brainstor m new content

#### Conduct legal research

(https://docs .cloud.googl e.com/gemin i/enterprise/ docs/usecases/brains torm-newcontent? hl=en) 

(https://docs .cloud.googl e.com/gemin i/enterprise/ docs/usecases/legalresearch? hl=en) 

Jumpstart legal research to understan… 

Go from a blank page to a working outline in… 

#### Debug and troubles hoot code

#### Create target custome r segment

s 

|(https://docs<br>.cloud.googl|(https://docs<br>.cloud.googl|(https://docs<br>.cloud.googl|
|---|---|---|
|e.com/gemin|e.com/gemin|e.com/gemin|
|i/enterprise/|i/enterprise/|i/enterprise/|
|docs/use-|docs/use-|docs/use-|
|cases/person|cases/target-|cases/debug|
|alized-|customer-|-|
|onboarding?|segments?|troubleshoot|
|hl=en)|hl=en)|-code?<br>hl=en)|
|Provide new|Categorize a|R<br>l<br>d|

1 (#) 2 (#) 3 (#) 4 (#) 

Last updated 2026-10-14 UTC. 



## Get reminders and manage tasks

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/reminders-and-tasks

Manage tasks and remind you about upcoming meetings, events, or deadlines. 

### Before you begin

To successfully manage tasks and reminders using these prompts, you must have a compatible to-do list tool (such as Google Tasks) enabled and configured in your Google Workspace environment and the corresponding Google Workspace extension enabled in Gemini Enterprise. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
Add 'follow up with finance on the expense report' to my to-do list for
tomorrow morning at 10 a.m. Can you also remind me to prepare for the customer
meeting on Friday?
```

Last updated 2026-10-14 UTC. 



## Analyze financial statements and calculate ratios

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/analyze-financial-statements

Analyze raw financial statements, calculate key performance indicators (KPIs), and generate an initial interpretation. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
You are a senior financial analyst. Based on the following financial data for
Cymbal Superstore for Q3 2025, perform the following tasks:
```

`1. Calculate the following financial ratios:` 

- `Gross Profit Margin` 

- `Operating Profit Margin` 

- `Net Profit Margin` 

- `Current Ratio` 

`2. Present the results in a table.` 

`3. In the table, include a column with a brief, one-sentence interpretation of each ratio.` 

```
[Paste financial data here.]
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

|Ratio|Calculation|ResultInterpretation|
|---|---|---|
|Gross Profit<br>Margin|($5M - $2M) / $5M|60.0%For every dollar of sales, the company keeps 60<br>cents after accounting for the direct costs of goods<br>sold.|
|Operating<br>Profit Margin|($5M - $2M -<br>$1.5M) / $5M|30.0%After paying for both direct production costs and<br>core operational expenses, the company earns 30<br>cents per dollar of revenue.|
|Net Profit<br>Margin|($5M - $2M -<br>$1.5M - $0.5M) /<br>$5M|20.0%The company's final profitability is 20%, meaning it<br>keeps 20 cents of profit for every dollar of revenue<br>generated.|
|Current Ratio|$4M / $2M|2.0x<br>The company has $2.00 of current assets available<br>to cover every $1.00 of its short-term liabilities,<br>indicating strong liquidity.|

Last updated 2026-10-14 UTC. 



## Detect anomalies in transaction data

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/anomaly-detection-transaction-data

Review monthly corporate credit card expense reports for unusual or noncompliant spending. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
You are an internal auditor. Review the following list of employee expense
transactions. Identify and list any items that meet the following criteria:
```

- `Are potential duplicates (same vendor and amount on consecutive days).` 

- `Occur on a weekend (Saturday or Sunday).` 

- `Are for an unusually high amount (over $1,000).` 

```
For each flagged item, provide a brief reason for flagging it.
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

The following transactions have been flagged for review based on your criteria: 

**Transaction 1 (Charlie S., Cymbal Superstore, $1,250):** 

**Reason:** Flagged for high value (exceeds the $1,000 threshold). 

**Transactions 3 & 4 (Luka D., Cymbal Direct, $45):** 

**Reason:** Flagged as a potential duplicate transaction (same employee, vendor, and amount on the same day). 

**Transaction 5 (Tristan J., Cymbal Shops, $250):** 

**Reason:** Flagged for occurring on a weekend (Saturday), which may be outside of company policy for this vendor type. 

Last updated 2026-10-14 UTC. 



## Draft a financial report narrative

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/financial-report-narrative

Draft report narratives, such as a Management Discussion & Analysis (MD&A), quickly by generating well-structured drafts. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
You are a financial reporting manager. Using the data below, write a draft of
the 'Results of Operations' section for our Q3 2025 report. The tone should be
formal and professional. Compare the current quarter to the same quarter in the
prior year and explain the key drivers for the changes.
[Paste data here]
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

#### Results of Operations

Revenue for the third quarter ended September 30, 2025, was $8.2 million, an increase of $1.2 million, or 17.1%, compared to $7.0 million in the same period of the prior year. The increase in revenue was primarily driven by strong demand for our new Product X, which launched in the first quarter of 2025, as well as expanded sales in international markets. 

Gross profit for the third quarter of 2025 was $4.1 million, compared to $3.85 million in the third quarter of 2024. As a percentage of revenue, the gross margin decreased from 55.0% to 50.0%. This margin compression was primarily due to higher raw material costs and increased shipping logistics expenses. 

Operating expenses in the third quarter of 2025 were $2.5 million, an increase of 13.6% from $2.2 million in the prior year's third quarter. The increase was mainly attributable to higher sales and marketing expenses related to the launch of Product X and an increase in headcount in our research and development department. 

Last updated 2026-10-14 UTC. 



## Summarize an earnings call transcript

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/earnings-call

Stay on top of competitor and industry trends without spending hours reading dense transcripts. Paste in the text of an earnings call, and get the key takeaways in seconds. 

**Note:** Verify every figure against the company's filed results release before using it. A transcript is a secondary source, and transcription errors in numbers are common. 

### Before you begin

- Attach the transcript rather than pasting it. A full call runs 10,000 words or more, and attaching keeps the whole document available to the model. 

- To compare earning calls across quarters, attach the prior quarter transcript in the same turn. 

- For a competitor's call that you don't have on file, use the second example prompt with the Deep Research agent, which cites its sources. 

### Example prompt

To summarize an attached transcript, enter a prompt in the chat box such as the following: 

```
You are an equity analyst. Attached are the Q3 and Q2 earnings call transcripts
for Cymbal Retail Group.
Summarize the Q3 call:
1. **Reported numbers**, quoted verbatim with the speaker named. Revenue,
margin, EPS, and any segment figure management called out. Do not calculate
anything that was not stated on the call.
```

`2. **Guidance**, quoted verbatim: what was given, and how it differs from what was given in Q2. If guidance was withdrawn, narrowed, or moved from a range to a` 

```
point, say so explicitly.
3. **Prepared remarks vs. Q&A.** Anything management raised in Q&A that did not
appear in prepared remarks, and anything from prepared remarks that no analyst
followed up on.
4. **Analyst questions**, grouped by theme. For each: who asked, what they were
getting at, and whether it was answered. Mark any question that was deflected,
answered with a different metric than the one asked about, or promised as a
follow-up.
5. **Language shifts from Q2.** Phrases used in Q2 that are gone in Q3, and new
hedging language. Quote both quarters side by side.
6. **Not addressed:** subjects an analyst would expect on this call that nobody
raised.
Rules:
```

- `Quote verbatim for every number and every guidance statement, and name the speaker.` 

- `Do not derive ratios, growth rates, or margins that were not stated aloud.` 

- `Distinguish what management said from what an analyst asserted in a question.` 

- `If the transcript marks a passage as inaudible or uncertain, flag it rather than filling it in.` 

To summarize a competitor's call you don't have on file, select the Deep Research agent and enter a prompt such as the following: 

```
Find the most recent quarterly earnings call for Cymbal Retail Group and
summarize it using the structure above. Link the transcript or webcast you
used,
and note the publisher. If you can only find secondary coverage rather than a
transcript, say so and do not quote as though from the transcript itself.
```

### Example output

In response to the first prompt, Gemini Enterprise produces output similar to the following: 

#### Reported numbers

|Metric|Quote|Speaker|
|---|---|---|
|Revenue|"Total revenue for the third quarter was $1.24 billion, up<br>6% year over year."|CFO, prepared<br>remarks|
|Gross marg|in "Gross margin came in at 38.1%, down 120 basis points<br>from a year ago."|CFO, prepared<br>remarks|
|EPS|"Adjusted earnings per share of $1.50."|CFO, prepared<br>remarks|
|Digital<br>segment|"Digital grew 14%, and now represents just under a quart<br>of total revenue."|er<br>CEO, prepared<br>remarks|

"Just under a quarter" was not given as a precise figure on the call and is not calculated here. 

#### Guidance

**Q3 call, CFO:** 

"We now expect full-year revenue growth of 4% to 5%." 

**Q2 call, CFO:** 

"We continue to expect full-year revenue growth of 5% to 7%." 

The range was lowered and narrowed. The CFO characterized this as "recalibrating for a promotional environment," not as a reduction. 

#### Prepared remarks vs. Q&A

- **Raised only in Q&A:** the delayed distribution center opening. It appeared in no part of prepared remarks and came up when an analyst asked about capacity. 

- **In prepared remarks, never followed up:** the new loyalty program. The CEO spent roughly two minutes on it and no analyst asked a single question about it. 

#### Analyst questions by theme

|Theme|Who aske|dGetting at|Answered?|
|---|---|---|---|
|Promotional<br>intensity and<br>margin|Analyst 1,<br>Analyst 4|Whether the margin<br>decline is structural o<br>cyclical|r<br>Deflected. Asked about margin<br>trajectory; answered with full-year<br>revenue guidance|
|Inventory positi|onAnalyst 2|Whether excess<br>inventory is driving<br>the promotions|Answered. Gave units on hand and<br>weeks of supply|
|Distribution<br>center delay|Analyst 3|Timing and cost<br>impact|Partially. Timing given; cost impact<br>promised as a follow-up|
|Digital<br>profitability|Analyst 5|Whether digital growt<br>is margin-dilutive|h<br>Answered with a different metric. Asked<br>about digital contribution margin;<br>answered with digital revenue growth|

#### Language shifts from Q2

|Q2|Q3|
|---|---|
|"We are confident in our full-year<br>outlook."|"We feel good about our positioning as we head into the<br>fourth quarter."|
|"Promotional activity has<br>normalized."|"The promotional environment remains dynamic."|
|(not used in Q2)|"assuming the consumer environment holds" - used three<br>times in Q3|

The Q2 phrase "normalized" is gone. The new conditional on the consumer environment appears only in Q3 and always attached to a forward-looking statement. 

#### Not addressed

- No question about the CFO transition announced two weeks before the call. 

- Nobody asked about the buyback, despite the release stating the authorization was materially drawn down this quarter. 

- Nobody asked what "dynamic" means for Q4 margin, which is the obvious follow-up to the deflection in the first theme above. 

#### Verification

Confirm the four figures in the first table against the filed results release. One passage in the Q&A is marked "[inaudible]" in the transcript where the CFO appears to give a store-count figure; that number is not reported here. 

Last updated 2026-10-14 UTC. 



## Create personalized onboarding materials

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/personalized-onboarding

Provide new hires with immediate, personalized access to necessary information, policies, and tasks. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
Generate a personalized onboarding checklist for a new [Job Title], starting on
[Start Date].
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Of course! Here is a personalized onboarding checklist for a new Sales Representative starting on October 21st. This checklist is designed to provide a structured and comprehensive onboarding experience, blending general sales best practices with specific insights into Cymbal Superstore's sales culture and processes. 

#### Onboarding Plan for a new Sales Representative

Welcome to the team! We are thrilled to have you on board. This 90-day plan is designed to help you ramp up smoothly and set you up for success. 

#### Phase 1: The First 30 Days - Foundation and Learning

Last updated 2026-10-14 UTC. 



## Analyze internal salary data

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/internal-salary-analysis

Ensure internal pay equity and competitiveness by analyzing internal salary data against market benchmarks. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
Generate a comprehensive report on compensation for all [Job Title] in the
company. Compare each employee's salary and bonus against market data for their
role and level.
```

Last updated 2026-10-14 UTC. 



## Conduct legal research

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/legal-research

Jumpstart legal research to understand a legal concept, find landmark cases, or generate an outline for a memo. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
Act as a law clerk. I need to write a research memorandum on the legal standard
for the business judgment rule as it applies to corporate directors in the
state
of California.
Please provide the following:
```

`1. A clear and concise definition of the business judgment rule in California.` 

`2. A list of the key elements a director must satisfy to be protected by the rule.` 

`3. The names of 2-3 seminal California court cases that established or clarified` 

```
  this doctrine. Provide a one-sentence summary for each case.
```

`4. An outline for a legal memo on this topic.` 

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

1. **Definition of the Business Judgment Rule in California:** 

The business judgment rule is a legal presumption that corporate directors, in making business decisions, acted on an informed basis, in good faith, and in the honest belief that the action taken was in the best interests of the company. The rule shields directors from personal liability for their decisions, even if they result in losses, provided the decision was made with due care and loyalty. 

2. **Key Elements for Protection:** 

- The director must not have a personal financial interest in the decision (disinterested). 

- The director must have been reasonably informed about the matter before making a decision (due care). 

- The director must have rationally believed their decision was in the best interests of the corporation (good faith). 

3. **Seminal California Cases:** 

- **_Lamden v. La Jolla Shores Clubdominium Homeowners Assn. (1999) 21 Cal.4th 249:_** The California Supreme Court affirmed the strong presumption of the rule, applying it to decisions made by homeowners' association boards. 

- **_Katz v. Chevron Corp. (1994) 22 Cal.App.4th 1352:_** This case helped clarify that the burden is on the plaintiff to prove that a director's decision was not made in good faith or with due care. 

4. **Legal Memo Outline:** 

- a. Introduction: Statement of the issue regarding the applicability of the business judgment rule. 

- b. Statement of Facts: [To be filled in with case-specific facts] 

- c. Discussion: 

   - i. The Business Judgment Rule in California: Definition and Purpose. 

   - ii. Elements Required for the Rule's Protection. 

      - i. Disinterestedness and Independence. 

      - ii. Due Care and Being Reasonably Informed. 

iii. Good Faith and Rational Belief. 

iii. Analysis of Seminal Case Law (Lamden, Katz). 

iv. Application of the Rule to the Present Facts. 

d. Conclusion: Summary of whether the directors' actions are likely protected by the business judgment rule. 

Last updated 2026-10-14 UTC. 



## Prepare for a deposition

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/deposition-witness-preparation

Prepare for a deposition by building a witness's documentary footprint from the case file and turning it into an outline where every line of questioning is tied to an exhibit. 

**Note:** Output from Gemini Enterprise is not legal advice. A qualified attorney must review and verify any deposition outline, and confirm every document reference against the record. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
You are a litigation associate preparing to depose the opposing party's
operations manager. Attached are the complaint, the answer, the parties'
agreement, the produced email set, and the transcript of the plant supervisor's
deposition.
Build a preparation packet:
1. **Witness footprint.** Every document in the attached record that this
witness authored, received, or is named in. Give the date, the document, the
Bates or exhibit number as it appears in the file, and one line on why it
matters. Order by date.
2. **Contradictions.** Any place this witness's documents conflict with the
plant supervisor's testimony, with the other party's pleadings, or with each
other. Quote both sides verbatim and cite each.
3. **Outline by topic.** For each topic, give the fact you are trying to
establish, the document you would use to establish it, and three to five
questions building to it. Every question must be answerable from a document in
the attached record.
4. **Anticipated problems.** Areas where the record is favorable to the
witness,
and what they are likely to say.
```

`5. **Not in the record.** Facts the pleadings assume that no attached document supports. These are the questions where you have no exhibit to fall back on.` 

```
Rules:
```

- `Use only the attached documents. Do not invent exhibit numbers, Bates numbers,` 

- `dates, names, or quotes.` 

- `Quote verbatim when you say a document says something, and cite it.` 

- `If you cannot support a line of questioning from the record, put it under "Not` 

- `in the record" rather than writing the question as though you can.` 

- `Use bracketed placeholders such as [DATE NOT IN RECORD] rather than filling in a plausible value.` 

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

#### Witness footprint

|Date|Document|Cite|Why it matters|
|---|---|---|---|
|Mar|4Email, witness to plant<br>supervisor|CYM-<br>000412|Directs a change to the inspection interval<br>three weeks before the failure|
|Mar|Weekly operations report,|CYM-|Reports "no open maintenance items" for the|
|19|authored by witness|000871|affected line|
|Apr 2|Email chain, witness copied|CYM-<br>001033|Supervisor raises a vibration complaint;<br>witness does not reply on the chain|
|Apr|Incident summary, authored|CYM-|States the failure was "sudden and without|
|11|by witness|001190|prior indication"|

#### Contradictions

**The Apr 11 incident summary against the Apr 2 email.** 

The witness wrote on April 11 (CYM-001190): 

"The failure was sudden and without prior indication." 

The witness was copied on April 2 (CYM-001033), where the supervisor wrote: 

"Line 3 is vibrating again, worse than last month. We should look at it before the next run." 

**The Mar 19 report against the supervisor's testimony.** 

The witness's March 19 report states "no open maintenance items." The supervisor testified (Dep. 84:6-14): 

"I told him the bearing needed replacing. I told him more than once." 

#### Outline by topic

**Topic 1: The witness received notice of the vibration.** Fact to establish: the witness saw the April 2 email. Document: CYM-001033. 

1. You use the email address shown at the top of this document? 

2. Reading the recipient line, you were copied on this message? 

3. Do you have any reason to believe you did not receive it? 

4. You did not reply to this message, correct? 

5. Did you take any action in response to it? 

**Topic 2: The inspection interval changed before the failure.** Fact to establish: the witness directed the change. Document: CYM-000412. 

1. This is an email you sent on March 4? 

2. Please read the second sentence aloud. 

3. Who decided to make that change? 

4. What was the interval before this email? 

5. Was anyone consulted before the change? 

#### Anticipated problems

- **The March 19 report may not be the witness's own work.** The document carries no signature block and the record does not establish who compiled it. Expect "that report is assembled by the shift leads." Establish authorship before using it. 

- **"Without prior indication" is arguably about the mechanical failure rather than the complaint history.** Expect the witness to draw that distinction. Pin down what they understood the phrase to mean at the time. 

#### Not in the record

- Nothing in the attached documents shows what the inspection interval was changed **to** , or who approved the change. The complaint asserts it doubled; no attached document states that. [NOT IN RECORD - confirm before asking a question that assumes it.] 

- No maintenance log, work order, or bearing replacement record appears in the production. If one exists, it is the central document for Topic 2 and is missing. 

- The supervisor's testimony refers to telling the witness "more than once." Only one written instance appears in the record. [DATES OF OTHER INSTANCES NOT IN RECORD.] 

Last updated 2026-10-14 UTC. 



## Draft legal correspondence

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/draft-legal-correspondence

Explaining a contract clause to a business client means translating what the text actually says, what it means in practice, and where it is genuinely unclear. You can use Gemini Enterprise to draft that explanation from the operative language, with the quoted text attached to every claim you make about it. 

**Note:** Output from Gemini Enterprise is not legal advice. A qualified attorney should review any correspondence before it is sent, and should review any contract before signature. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
You are a commercial attorney. Attached is our client's supply agreement with
Cymbal Manufacturing. The client asked whether they can walk away if Cymbal
misses another delivery date.
Draft an email to the client that:
1. **Quotes the operative language verbatim**, with the section number, before
explaining anything. Include every section that bears on the answer, including
cure periods, notice requirements, and any limitation on remedies.
2. **Explains what the text says** in plain language, section by section. State
only what the words support.
3. **Separates three things explicitly:** what the contract says, what is
ambiguous, and what I am recommending. Label them.
4. **Identifies the steps that have conditions attached**, such as written
notice, a cure window, or a deadline measured from a triggering event, and what
happens if a step is missed.
5. **Lists what you need from the client** to answer the question fully.
Rules:
- Use only the attached agreement. Do not assume standard terms that aren't in
this document.
- Do not predict how a court would rule, characterize the other side's likely
behavior, or state what remedies are available in law beyond what the contract
provides.
- Where language could reasonably be read two ways, say so and give both
readings. Do not pick one silently.
- Leave bracketed placeholders for facts I have not given you, such as dates of
prior missed deliveries. Do not supply plausible values.
- End with a short list of what I need to confirm before this email goes out.
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Subject: Your options on the Cymbal delivery delays 

Hi [CLIENT NAME], 

Short answer: the agreement does give you a way out for repeated late delivery, but it is conditional, and the clock on it is shorter than it looks. Here is the language and what it means. 

**What the contract says** 

**Section 5.2 (Delivery).** 

"Supplier shall deliver each Order by the delivery date specified in the applicable Purchase Order. Time is of the essence with respect to delivery." 

"Time is of the essence" matters. It means a late delivery is a breach of the agreement on its own, not merely a scheduling problem. 

**Section 12.1 (Termination for cause).** 

"Either party may terminate this Agreement upon thirty (30) days' written notice if the other party commits a material breach and fails to cure such 

breach within the notice period." 

Termination is not automatic. It requires written notice, and Cymbal gets thirty days to fix the problem after they receive it. 

**Section 12.2 (Repeated failure).** 

"Notwithstanding Section 12.1, Customer may terminate immediately upon written notice if Supplier fails to meet the delivery date for three (3) or more Orders in any rolling six (6) month period." 

This is the provision you are asking about. Three late orders in a rolling six-month window lets you terminate immediately, with no cure period. 

**Section 15.4 (Notices).** 

"All notices shall be in writing and delivered by certified mail or nationally recognized overnight courier to the address set forth in Exhibit A. Notice by email shall not be effective." 

Email does not count. A termination notice sent by email is not valid notice under this agreement. 

**What is ambiguous** 

- **Section 12.2 does not say when the six-month window is measured from.** It can be read as the six months preceding the third missed delivery, or as the six months preceding the notice. If the earlier misses are close to the edge of that window, the two readings give different answers. 

- **"Fails to meet the delivery date" is not defined.** The agreement does not say whether a partial shipment on time, or a delivery accepted late without objection, counts as a failure. Section 5.2 does not resolve this. 

- **Section 12.2 does not address whether prior missed deliveries you waived still count.** If your team accepted late deliveries in writing without reserving rights, Cymbal may argue those don't count toward the three. 

**What I recommend** 

1. Before anything else, send written notice by certified mail for the most recent missed delivery, reserving all rights. This preserves your position regardless of which route you take. 

2. Don't rely on email for anything you may later need to prove as notice. 

3. Let me confirm the count under Section 12.2 before we act on it. If we are at two rather than three, the immediate-termination route isn't available yet and we should use the Section 12.1 path instead. 

**What I need from you** 

- The dates of each missed delivery in the last six months, and the purchase order number for each. [DATES NOT PROVIDED] 

- Any written communication where your team accepted a late delivery, agreed to a revised date, or said the delay was acceptable. 

- Confirmation of the notice address currently in Exhibit A, and whether it has been updated since signing. 

- Whether you want to preserve the relationship or exit. That changes which of the two termination routes we use. 

Best, [YOUR NAME] 

#### Before you send this

- Confirm the attached agreement is the executed version and that no amendment or side letter changes Sections 5.2, 12.1, 12.2, or 15.4. 

- Verify the delivery dates and the count under Section 12.2 yourself; the draft leaves them blank on purpose. 

- Decide whether to include the recommendation section at all, or to deliver it by phone. 

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC.
