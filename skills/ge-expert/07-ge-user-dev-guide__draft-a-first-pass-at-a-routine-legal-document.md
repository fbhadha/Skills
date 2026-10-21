# Gemini Enterprise: user guide, Workflow Builder, developer guide / Draft a first pass at a routine legal document to Prepare for a first meeting
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 248-288, extracted 2026-10-18

Contains:
- Draft a first pass at a routine legal document (pages 248-252) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/draft-simple-legal-documents
- Summarize a legal document (pages 253-258) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/summarize-legal-documents
- Brainstorm new content (pages 259-263) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/brainstorm-new-content
- Extend and revitalize assets (pages 264-266) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/asset-extension
- Summarize a campaign (pages 267-269) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/campaign-summarization
- Tailor ad copy and messaging (pages 270-272) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/ad-messaging
- Accelerate materials discovery (pages 273-274) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/accelerate-materials-discovery
- Analyze concepts and research methodologies (pages 275-278) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/analyze-concepts-research-methodologies
- Review design standards (pages 279-281) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/review-design-standards
- Create target customer segments (pages 282-283) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/target-customer-segments
- Write a personalized outreach email (pages 284-287) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/personalized-email-outreach
- Prepare for a first meeting (pages 288-288) https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/first-meeting-preparation

## Draft a first pass at a routine legal document

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/draft-simple-legal-documents

Routine documents follow a known shape, and the slowest part of the process is assembling the facts. You can use Gemini Enterprise to produce a first draft that leaves every fact you didn't supply as a visible placeholder, so the gaps are obvious rather than filled in with something plausible. 

**Note:** Output from Gemini Enterprise is not legal advice. A qualified attorney must review and revise any document before it is sent, filed, or signed, and should review any contract before signature. Don't send output from Gemini Enterprise to a third party without attorney review. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
You are a paralegal preparing a first draft for attorney review. Draft a cease
and desist letter.
Facts I am giving you, and the only facts you may treat as established:
```

- `Our client is Cymbal Superstore.` 

- `Cymbal Superstore uses the mark "CYMBAL" in connection with retail store services.` 

- `The recipient is Cadence Retail Group, operating a store under the name "Cymbal Outlet" in the same metropolitan area.` 

- `Our client first learned of the recipient's use on \[DATE\].` 

```
Draft the letter with:
```

`1. Identification of the parties and the mark, using only the facts above.` 

`2. A description of the conduct we are objecting to.` 

`3. The demands: stop using the name, confirm in writing within a stated period,` 

```
and provide an accounting of use to date.
```

`4. A closing that reserves all rights.` 

```
Rules:
```

- `Do not assert any fact I have not given you. This includes registration status, registration numbers, the date of first use, the goods or services the recipient offers, sales figures, and whether anyone has been confused.` 

- `Do not cite any statute, case, or regulation. Insert [CITE - ATTORNEY TO SUPPLY] where authority belongs.` 

- `Do not state legal conclusions such as that infringement has occurred, that the mark is famous, or that a likelihood of confusion exists. Describe the conduct and the objection instead.` 

- `Use a bracketed placeholder in ALL CAPS for every unknown, and use the same placeholder text for the same fact throughout.` 

- `Do not assume a jurisdiction or governing law.` 

```
After the draft, give me three lists: assumptions you deliberately did not
make,
facts still needed, and determinations that require an attorney.
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

[FIRM LETTERHEAD] 

[DATE] 

**VIA [DELIVERY METHOD - ATTORNEY TO SPECIFY]** 

Cadence Retail Group [RECIPIENT ADDRESS] 

**Re: Use of "Cymbal Outlet"** 

Dear [RECIPIENT CONTACT NAME]: 

This firm represents Cymbal Superstore. Cymbal Superstore uses the mark CYMBAL in connection with retail store services. 

It has come to our client's attention that Cadence Retail Group is operating a retail location under the name "Cymbal Outlet" at [RECIPIENT LOCATION ADDRESS], in the same metropolitan area in which our client operates. Our client first became aware of this use on [DATE CLIENT LEARNED OF USE]. 

Our client objects to this use. [BASIS FOR OBJECTION - ATTORNEY TO STATE, WITH CITE - ATTORNEY TO SUPPLY.] 

Accordingly, we request that Cadence Retail Group: 

1. Immediately cease all use of "Cymbal Outlet" and of any other name or mark incorporating "CYMBAL" in connection with retail store services, including use in signage, advertising, packaging, online listings, social media, and domain names; 

2. Confirm in writing within [NUMBER] days of the date of this letter that it has done so and will not resume such use; and 

3. Provide an accounting of its use of the name to date, including the date use began, the locations and channels in which the name has been used, and [ADDITIONAL ACCOUNTING ITEMS - ATTORNEY TO SPECIFY]. 

Nothing in this letter constitutes a waiver of any right or remedy available to our client, all of which are expressly reserved. 

Please direct your response to the undersigned. 

Sincerely, 

[ATTORNEY NAME] [FIRM NAME] 

#### Assumptions I deliberately did not make

- **Registration status.** You told me our client uses the mark. You did not tell me it is registered, where, or under what number. The letter says "uses" and nothing more. If the mark is registered, that fact and the registration number should be added, and the objection paragraph will likely change. 

- **What the recipient sells.** You gave me a store name and a location, not the goods or services offered. The letter does not claim the parties' services 

overlap. 

- **Priority.** Nothing here states who used the name first. That is typically the pivotal fact and it is not in what you gave me. 

- **Actual confusion.** No incident of confusion was described, so none is alleged. 

- **Jurisdiction and governing law.** Not stated, so no forum, statute, or body of law is referenced anywhere in the draft. 

#### Facts still needed

- Date of the client's first use of CYMBAL in this geographic area, and evidence of that use. 

- Registration status and number, if any, and the classes covered. 

- The recipient's date of first use, if known, and how you learned of it. 

- The recipient's legal entity name, registered agent, and address for service. 

- Whether the parties have had any prior contact about this name. 

- Any instances of actual confusion, and how they were documented. 

- The response deadline you want, and the delivery method. 

#### Determinations that require an attorney

- Whether to send this letter at all, given that a demand letter can precipitate a declaratory judgment action. 

- The legal basis for the objection and the authority to cite. 

- Whether the demands are proportionate, and whether the accounting request should be included in a first letter. 

- The tone: this draft is deliberately neutral. Escalating it is a judgment call. 

- Whether any of the placeholders above should remain blank as a matter of strategy rather than being filled in. 

Last updated 2026-10-14 UTC. 



## Summarize a legal document

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/summarize-legal-documents

Digest long contracts, depositions, or judicial opinions. 

**Note:** Output from Gemini Enterprise is not legal advice. A qualified attorney should review any contract before signature, and should review any summary before it is relied on operationally. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
You are a contracts analyst. Attached is the executed master services agreement
between Cymbal Superstore and Cymbal Consulting, including its exhibits.
Produce an operational summary:
1. **Our obligations** and **their obligations**, in two separate tables. For
each: what must be done, by when, the triggering event, and the section number.
2. **Dates and deadlines**, in one table: the date or period, what it governs,
what happens if it is missed, and the section. Include the effective date, the
term, renewal and notice deadlines, and any deadline measured from an event
rather than from a fixed date.
3. **Money terms**, quoting verbatim: fees, rate card, payment period, late
charges, price increase mechanism, and any cap or minimum commitment.
4. **Termination and renewal**, quoting the operative language for each route
out and the notice each requires.
5. **Defined-term traps.** Any defined term whose contract meaning differs from
its ordinary meaning in a way that changes how a clause reads.
6. **Ambiguities.** Language that could reasonably be read more than one way.
Give both readings. Do not choose between them.
7. **Not addressed.** Subjects a reader would expect this agreement to cover
that it does not.
```

`Rules:` 

- `Cite a section number for every statement. If you cannot cite one, do not make` 

```
the statement.
```

- `Quote verbatim for anything involving money, dates, notice, or termination. - If the agreement and an exhibit conflict, show both and say they conflict. Do not resolve it.` 

- `Do not give negotiation advice, opinions on whether a term is market, or predictions about enforceability.` 

- `Do not summarize any section you cannot locate in the attached file.` 

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

#### Our obligations

|Obligation|Deadline|Trigger|Section|
|---|---|---|---|
|Pay undisputed invoices|30 days|Receipt of<br>invoice|4.1|
|Provide system access and a named project<br>contact|10 business days|Effective date|3.2|
|Notify of a disputed invoice line|15 days|Receipt of<br>invoice|4.5|
|Provide written notice of non-renewal|60 days before term<br>end|Term end date|11.2|

#### Their obligations

|Obligation||Deadline|Trigger|Section|
|---|---|---|---|---|
|Deliver a written statement of w<br>work begins|ork before|Before<br>commencement|Each engageme|nt 2.1|
|Obtain written pre-approval for t<br>$2,500|ravel over|Before incurring|Travel expense|6.1|
|Provide monthly written status r|eports|Monthly|Ongoing|3.4|
|Return or destroy confidential in|i formation|30 days|Termination or<br>expiry|9.6|
#### |Dates and deadlines|||||
|Date or period|Governs|If missed||Section|
|Effective date: as stated on the<br>signature page|Start of ter|m<br>-||Preamble|
|Initial term: 3 years|Term|-||11.1|
|Auto-renewal: successive 1-year<br>terms|Renewal|Renews automa|tically|11.2|
|60 days before term end|Non-renew<br>notice|al<br>Agreement ren<br>year|ews for another|11.2|
|Net 30|Payment|Late charge ap|plies, Section 4.4|4.1|
|15 days from invoice|Invoice dis|puteSection 4.5 stat<br>"deemed accep|es the line is<br>ted"|4.5|

**The 60-day non-renewal notice is the deadline most likely to be missed.** It is measured backward from the term end date and the agreement provides no reminder mechanism. 

#### Money terms

**Section 4.1 (Payment).** 

"Customer shall pay all undisputed amounts within thirty (30) days of receipt of a valid invoice." 

**Section 4.4 (Late charges).** 

"Amounts not paid when due shall accrue interest at one and one-half percent (1.5%) per month or the maximum rate permitted by law, whichever is less." 

**Section 4.6 (Rate adjustment).** 

"Supplier may adjust the rates set forth in Exhibit B upon sixty (60) days' written notice, provided that no adjustment shall exceed five percent (5%) in any twelve (12) month period." 

**Conflict between the agreement and Exhibit B.** Section 4.6 caps annual rate adjustments at 5%. Exhibit B, note 3, states: 

"Rates are subject to annual adjustment in line with the Supplier's then current published rate card." 

These do not say the same thing and the agreement does not state which controls. Flagged for attorney review; not resolved here. 

#### Termination and renewal

**Section 11.2 (Renewal).** 

"This Agreement shall renew automatically for successive one (1) year terms unless either party provides written notice of non-renewal at least sixty (60) days prior to the end of the then-current term." 

**Section 11.3 (Termination for cause).** 

"Either party may terminate for material breach upon thirty (30) days' written notice if the breach remains uncured at the end of such period." 

**Section 11.4 (Termination for convenience).** 

"Customer may terminate any Statement of Work for convenience upon sixty (60) days' written notice, subject to payment for work performed and noncancellable commitments incurred through the effective date of termination." 

Termination for convenience applies to a **statement of work** , not to the agreement itself. There is no convenience exit from the master agreement. 

#### Defined-term traps

- **"Confidential Information" (1.4)** excludes information "independently developed without reference to the disclosing party's information." That exclusion is broader than the ordinary meaning of the phrase. 

- **"Deliverable" (1.7)** is limited to items "expressly identified as a Deliverable in a Statement of Work." Work product not named in an SOW is not a Deliverable, which affects the IP assignment in Section 8. 

- **"Business Day" (1.2)** is defined by reference to the supplier's location, not ours. Every notice period measured in business days runs on their calendar. 

#### Ambiguities

- **Section 7.1** requires support "during business hours" without stating a time zone or holiday calendar. Section 1.2 defines "Business Day" but not "business hours." Readable as the supplier's local hours or as ours. 

- **Section 4.5** says a disputed line is "deemed accepted" after 15 days. It is unclear whether this bars a later challenge to the underlying charge or only to that invoice. 

- **Section 11.4** refers to "non-cancellable commitments incurred" without defining what qualifies or requiring evidence of them. 

#### Not addressed

The agreement contains no provision covering: 

- Data deletion or return on termination, other than the confidentiality obligation in Section 9.6, which addresses confidential information only. 

Audit rights. 

Subprocessor or subcontractor notification. 

Service levels or credits. 

Insurance requirements. 

These may appear in a separate document. Nothing in the attached file references one. 

Last updated 2026-10-14 UTC. 



## Brainstorm new content

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/brainstorm-new-content

Go from a blank page to a working outline in one turn, and then ground that outline in what your organization has already published so the draft sounds like you rather than like a template. 

### Before you begin

The grounded prompt draws on your own material. Either attach your style guide and prior content, or make sure the relevant Google Drive folder or content source is connected and indexed, then reference the files by name in the prompt. 

### Example prompt

To get a first outline quickly, enter a prompt in the chat box such as the following: 

```
Give me a 5-point outline for a blog post about why inventory forecasts break
down during promotional periods. The audience is supply chain managers at
mid-size retailers who own the forecast but don't build the models themselves.
For each point, give the claim, why this audience cares, and the one example or
number that would make it land. Flag any point where I'd need data I probably
don't have.
```

To ground the outline in your own material, enter a prompt such as the following: 

```
You are a content strategist. Attached are our style guide and our ten
highest-performing posts from the last year, with their pageview and
engaged-time numbers.
I want to write about why inventory forecasts break down during promotional
periods, for supply chain managers at mid-size retailers.
```

`1. **What we've already said on this topic.** Any of our existing posts that overlap, what each one covers, and whether the new post should replace it, link to it, or be narrowed to avoid repeating it.` 

`2. **What actually performs for us.** Looking only at the attached numbers, what do our top posts have in common: length, structure, whether they lead with a claim or a story, use of data, headline pattern. Say which of these the numbers support and which is your impression.` 

`3. **Three angles** on the topic, each differentiated from what we've already published. For each: the argument, who it's aimed at, and why it's ours to make rather than anyone's.` 

`4. **An outline for the strongest angle**, following the structural pattern the data supports.` 

`5. **Voice check:** three phrases from the outline that don't match the style guide, quoted, with replacements.` 

```
Rules:
```

- `Base the performance observations on the attached numbers only. Ten posts is a small sample; say where a pattern is thin.` 

- `Don't propose an angle that requires proprietary data we haven't published. If an angle needs data, say what data and who would have it.` 

### Example output

In response to the grounded prompt, Gemini Enterprise produces output similar to the following: 

#### What we've already said

|Existing post|Overlap|Recommendation|
|---|---|---|
|"Five forecasting<br>mistakes" (Mar)|Section 3 covers promotional lift<br>in two paragraphs|Link to it; the new post is the long<br>version of that section|
|"Peak season<br>readiness checklist"|Operational, not analytical. No<br>real overlap|Cross-link|
|(Aug)|||

|Existing post|Overlap|Recommendation|
|---|---|---|
|"What good demand<br>data looks like" (Jan)|Assumes clean baseline demand,<br>which is exactly what the new<br>post questions|Narrow the new post so it doesn't<br>contradict this one without<br>acknowledging it|

#### What performs for us

Supported by the numbers: 

- **Length.** The five highest engaged-time posts are 1,400-1,900 words. The three shortest posts in the set are also the three lowest. The pattern holds across all ten. 

- **Leading with a claim.** Seven of the ten open with an assertion rather than a scenario. Those seven average roughly double the engaged time. 

My impression, not supported by the numbers: 

- Posts with a table seem to do better, but only three of the ten have one, and one of those is the weakest post in the set. Ten posts is too small a sample to call this. 

#### Three angles

1. **"Your forecast isn't wrong during promotions; it's answering a different question."** Argues that baseline models are being asked to predict an event they were never fitted on. Aimed at managers who inherited a model they didn't build. Ours to make because our March post already established credibility on model diagnostics. 

2. **"The markdown is the forecast error."** Reframes promotional markdowns as the visible cost of a forecast the organization already knows is wrong. Aimed at managers who need to make the case upward. Strongest angle for a finance-adjacent reader. 

3. **"Stop measuring forecast accuracy in aggregate."** Argues that promotional weeks get averaged away in MAPE. Aimed at the analyst layer. Narrower audience, but nobody in our space has written it. 

#### Outline for angle 2

Following the pattern the data supports: open with the claim, 1,400-1,700 words, no scenario lead. 

1. **Open with the claim.** Markdown budgets are a forecast error line item that has been reclassified as a marketing cost. 

2. **Why the two get separated.** Different owners, different systems, different review cycles. Nobody adds them up. 

3. **What the combined number looks like.** [NEEDS DATA - a worked example with real figures. We have not published anything like this. Ask the analytics team whether an anonymized customer example can be used.] 

4. **Why more safety stock doesn't fix it.** Moves the cost, doesn't remove it. Ties back to the March post. 

5. **What to change.** Decompose promotional lift from baseline; measure accuracy on promotional weeks separately. 

6. **Close on the reframe** , not on a product mention. 

#### Voice check

|Phrase in the outline|Style guide says|Replacement|
|---|---|---|
|"reclassified as a marketing<br>cost"|Avoid nominalizations; prefer<br>verbs|"gets counted as marketing<br>spend"|
|"leverage the decomposition"|"leverage" is on the banned-<br>words list|"separate promotional lift from<br>baseline"|
|"in today's dynamic retail<br>environment"|Style guide: cut throat-clearin<br>openers|g<br>Delete; start with the claim|



## Extend and revitalize assets

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/asset-extension

Revitalize an existing asset, such as a whitepaper or a transcript from a webinar, and generate a week's worth of social media collateral in minutes, ensuring message consistency across platforms. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
I have an existing asset: [asset name or link to whitepaper, webinar
transcript, etc.]. Please generate a week's worth of social media collateral
based on this asset. Create [number] posts for [social media platform, e.g.,
LinkedIn] and [number] posts for [social media platform, e.g., X]. Ensure that
the posts are tailored to each platform's style and audience. Include relevant
hashtags for each post.
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Here are the social media posts based on the "AI in B2B Marketing" webinar transcript, tailored for LinkedIn and X, complete with relevant hashtags. 

#### LinkedIn Posts

**Post 1: AI for Personalization & Sales Cycles** 

AI is no longer just a buzzword; it's actively reshaping B2B marketing by enabling personalization at scale. Our recent webinar, "AI in B2B Marketing: From Buzzword to Bottom Line," highlighted how AI analyzes prospect behavior across touchpoints to deliver hyper-relevant content, leading to a significant reduction 

in sales cycles. This isn't just better marketing, it's a more efficient sales process. #B2BMarketing #AInMarketing #Personalization #SalesEnablement #DigitalTransformation 

**Post 2: Predictive Analytics & Lead Scoring** 

Dive deep into how AI is transforming lead qualification! In our "AI in B2B Marketing" webinar, we discussed how predictive analytics and sophisticated lead scoring models move us from guesswork to data-driven probability. AI identifies subtle patterns of high-intent prospects, helping sales teams prioritize leads and focus on building relationships with high-potential accounts. #PredictiveAnalytics #LeadScoring #B2BSales #DataDrivenMarketing #MarketingTech 

**Post 3: The Future of Generative AI & Competitive Intelligence** 

Beyond simple content drafts, generative AI is ushering in an era of dynamic content generation. Imagine custom one-pagers generated in real-time, or AIorchestrated customer journeys. Our webinar also touched on AI's role in competitive intelligence, allowing us to react to market shifts in hours, not months. The future of B2B marketing is predictive and proactive! #GenerativeAI #DynamicContent #CompetitiveIntelligence #B2BStrategy #MarketingInnovation 

#### X Posts

**Tweet 1: AI for Personalization** 

AI is here to stay in #B2BMarketing! 🚀 It's driving hyper-personalization at scale, delivering content that truly resonates with prospects. #AI #Marketing 

**Tweet 2: Shorter Sales Cycles with AI** 

Did you know AI can shorten sales cycles by up to 15%? By focusing on highintent prospects, teams become more efficient. #B2BSales #AInMarketing #Efficiency 

**Tweet 3: Dynamic Content with Generative AI** 

Generative AI is changing the game for content creation! Think custom onepagers and dynamic slide decks. #GenerativeAI #ContentMarketing #MarketingTrends 

**Tweet 4: AI for Proactive Marketing** 

Move from reactive to proactive! AI-driven competitive intelligence allows rapid responses to market shifts, making your B2B strategy sharper than ever. #AIMarketing #MarketIntelligence #FutureofMarketing 

Last updated 2026-10-14 UTC. 



## Summarize a campaign

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/campaign-summarization

Prepare for meetings by generating summaries of internal documents like campaign reports or branding guidelines. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
I have a meeting about [meeting topic]. Please summarize the document [document
name or link] by providing the top 3-5 key takeaways, any action items or next
steps mentioned, and a brief overview of the key metrics or findings.
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Here is a summary of the "Q1-Q2 2025 Campaign Performance Report" to help you prepare for your Q4 campaign planning meeting. 

### Key Takeaways

- **Video Content is Highly Effective:** Video ads, particularly on YouTube, were the top performers, driving high engagement and conversions. This format consistently outperformed static images across the board. 

- **Successful Lead Generation:** The campaign exceeded its lead generation goal by 15%, securing 11,750 qualified leads for the "Connectly Pro" platform. 

- **LinkedIn is a Double-Edged Sword:** While effective for reaching senior decision-makers, LinkedIn had the highest Cost Per Lead (CPL) of any single platform at $50.00. 

- **Audience Resonates with Productivity:** The target audience responded strongly to creative messaging that emphasized productivity and achieving a better work-life balance. 

### Action Items & Next Steps

The report recommends the following for future campaigns: 

- **Increase Video Investment:** Allocate a larger portion of the budget to video creative, specifically for YouTube and Instagram. 

- **Optimize LinkedIn Strategy:** Develop more targeted content and offers for LinkedIn to improve its Cost Per Lead. 

- **Explore New Platforms:** Test emerging social media platforms to capture a younger, tech-forward audience segment. 

- **Refine Search Keywords:** Focus on high-intent, long-tail keywords in Google Search to attract users who are closer to making a decision. 

### Overview of Key Metrics & Findings

- **Total Media Spend:** $500,000, split evenly between social ($250k) and digital ($250k) channels. 

**Overall Performance:** 

- Impressions: 50 million 

- Clicks: 1.05 million 

- Conversions: 11,750 

- Average Cost Per Lead (CPL): $42.55 

**Channel Highlights:** 

- Google Search had the best Click-Through Rate (CTR) at 6.00%. 

- Display ads were the most cost-efficient, with the lowest CPL at $33.33. 

Instagram had the highest CTR (2.00%) among social channels and a strong CPL ($38.89). 

Last updated 2026-10-14 UTC. 



## Tailor ad copy and messaging

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/ad-messaging

Launch a new ad or social campaign by generating different creative angles, headlines, and descriptions for you to test. Gemini Enterprise can map to and adopt the right tone, focusing on pain points relevant to a particular audience segment. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
We are launching a new ad campaign for [product/feature]. Our target audience
is [target audience], and we want to focus on their primary pain points:
[List of pain points]
Please generate [number] different creative angles for this campaign. For each
angle, provide 2-3 headlines and a short paragraph of ad copy that adopts a
[tone of voice, e.g. professional, witty, empathetic] tone.
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Here are three creative angles for your ad campaign, each with headlines and ad copy designed to resonate with freelance graphic designers. 

**Angle 1: Reclaim Your Creative Time** 

This angle focuses on the primary benefit of saving time, allowing designers to focus on their passion and billable work, rather than administrative tasks. 

**Headlines:** 

More Time for Design, Less for Invoicing. 

Automate Your Admin, Unleash Your Creativity. 

The 5-Minute Invoice for the 10-Hour Project. 

**Ad Copy:** 

Your creative energy is your most valuable asset. Stop letting tedious invoicing and follow-ups drain your time and interrupt your workflow. Our new automated invoicing feature handles the administrative details for you, from creation to reminders. It's time to get back to the work that you love and that truly drives your business forward. 

**Angle 2: Accelerate Your Cash Flow** 

This angle targets the critical pain point of getting paid in a timely manner, emphasizing financial stability and control. 

**Headlines:** 

Stop Chasing Payments. Start Getting Paid. 

- From Project Done to Payment Received, Faster. 

- Effortless Invoicing. Predictable Income. 

**Ad Copy:** 

As a freelancer, consistent cash flow is freedom. Our automated invoicing feature helps you get paid faster and more reliably. Send professional, branded invoices in seconds and let the app handle payment reminders automatically. Take control of your finances and eliminate the stress of waiting for your hard-earned money. 

**Angle 3: Elevate Your Professional Brand** 

This angle positions the feature as a tool for business growth, helping freelancers appear more professional and organized to their clients. 

**Headlines:** 

Look as Professional as Your Portfolio. 

The Business Side of Your Craft, Perfected. 

Build Your Brand, One Perfect Invoice at a Time. 

**Ad Copy:** 

Every client interaction is an opportunity to build your brand. Our automated invoicing ensures you always present a polished, professional image. Impress your clients with clear, timely, and beautifully simple invoices that reflect the quality of your design work. It's a small step for your process, but a giant leap for your business reputation. 

Last updated 2026-10-14 UTC. 



## Accelerate materials discovery

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/accelerate-materials-discovery

Query the properties of a material or predict the properties of a hypothetical composition. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
I'm looking for a new alloy. I need it to be lightweight, have a strength of
[YIELD STRENGTH], and withstand temperatures up to [TEMPERATURE].
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Finding a lightweight alloy with strength over 1000 MPa that can withstand 800°C is a demanding task, typically leading to materials used in aerospace and other high-performance sectors. Here are the most promising candidates. 

1. Nickel-Based Superalloys 

These are the industry standard for high-temperature applications. 

- **Performance:** Alloys like Inconel and Nimonic offer excellent strength and stability at temperatures well above 700°C. 

**Trade-off:** They are dense and not considered lightweight. 

2. Titanium Aluminide (TiAl) Alloys 

These intermetallic alloys offer a superior balance of properties for your needs. 

- **Performance:** They are significantly lighter than superalloys while maintaining good strength and performance at temperatures up to 800°C. 

- **Considerations:** They can be brittle at room temperature, which makes manufacturing more complex. 

3. High-Entropy Alloys (HEAs) 

HEAs are a new frontier in materials science, created by mixing multiple elements in high concentrations. 

- **Performance:** Certain refractory HEAs show unmatched strength at extreme temperatures (even above 1000°C). 

- **Considerations:** This is an emerging field, so these materials are not yet widely available or standardized. 

Here is a summary to help you compare these options: 

|Alloy Class|Key Advantages|Key Considerations|
|---|---|---|
|Nickel-Based<br>Superalloys|Excellent high-temperature strength and<br>proven reliability.|Higher density (not lightweight).|
|Titanium<br>Aluminides (TiAl)|Good balance of low density and high-<br>temperature strength.|Can have lower ductility and be<br>more difficult to process.|
|High-Entropy<br>Alloys (HEAs)|Exceptional strength at very high<br>temperatures and cutting-edge<br>performance.|Newer material class, less<br>established supply chain.|

Last updated 2026-10-14 UTC. 



## Analyze concepts and research methodologies

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/analyze-concepts-research-methodologies

Obtain general information about research methodologies, scientific concepts, or public databases such as PubMed through a chat interface. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
My objective is to understand [specific topic, e.g., the methodology behind
clinical trials for cancer research].
Please use all available external data sources, including [list of data
sources, e.g., PubMed, Google Scholar, National Library of Medicine], to
summarize the key statistical methods used to analyze data in each phase.
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

Here is a summary of the statistical methodologies used in clinical trials for lung cancer treatments, broken down by phase. 

#### Phase I: Safety and Dosage

The primary objective of a **Phase I** trial is to determine the **safety profile** of a new treatment and to find the **Maximum Tolerated Dose (MTD)** . This is the highest dose that can be given without causing unacceptable side effects. These trials involve a small group of patients (around 15-30). 

Key statistical methods are focused on dose-escalation designs: 

- **3+3 Design** : This is a common rule-based approach. Three patients are given a dose. If none experience a dose-limiting toxicity (DLT), the next group of three gets a higher dose. If a DLT occurs, more patients are added at the current dose to better assess its safety. 

- **Continual Reassessment Method (CRM)** : A model-based design that uses data from all patients in the trial to model the dose-toxicity relationship. It allows for a more efficient and precise estimation of the MTD. 

#### Phase II: Efficacy and Side Effects

The primary objective of a **Phase II** trial is to evaluate whether the new drug has a sufficient level of **biological activity or effect** (preliminary efficacy) to warrant further testing. It also continues to monitor safety in a larger group of patients (typically under 100). 

Key statistical methods often involve single-arm studies: 

- **Simon's Two-Stage Design** : This is an efficient design that can stop the trial early if the treatment shows little promise. If a minimum number of patients respond positively in the first stage, the trial proceeds to a second stage to gather more data. 

- **Endpoint Analysis** : The primary endpoint is often the **Objective Response Rate (ORR)** , which measures the proportion of patients whose tumor shrinks by a predefined amount. The statistical analysis determines if the observed ORR is high enough to be clinically meaningful. 

#### Phase III: Comparison and Confirmation

The primary objective of a **Phase III** trial is to **confirm the efficacy** of the new treatment by comparing it to the current standard of care. These are large, pivotal trials involving hundreds or thousands of patients, and their results are used to support regulatory approval. 

Key statistical methods are the most rigorous: 

**Randomized Controlled Trials (RCTs)** : Patients are randomly assigned to an **experimental group** (new treatment) or a **control group** (standard treatment). This randomization minimizes bias. These trials are often "double-blinded," meaning neither the patients nor the investigators know who is receiving which treatment. 

- **Survival Analysis** : This is crucial in cancer research. 

   - **Kaplan-Meier Curves** are used to estimate and graph survival probabilities over time. 

   - The **Log-Rank Test** is used to statistically compare the survival curves between the treatment groups. 

The **Cox Proportional Hazards Model** is a regression model used to assess the effect of the treatment while adjusting for other variables like age or disease stage. It calculates a **hazard ratio (HR)** , which quantifies how much more likely an event (like death or disease progression) is in one group compared to the other. 

#### Phase IV: Post-Marketing Surveillance

The primary objective of a **Phase IV** trial is to monitor the **long-term safety and effectiveness** of the drug after it has been approved and is available to the public. This phase can detect rare or long-term side effects that were not apparent in earlier, smaller studies. 

Key statistical methods include: 

- **Observational Studies** : Researchers analyze data from large patient populations in real-world settings to see how the drug performs outside the controlled environment of a clinical trial. 

- **Real-World Data (RWD) Analysis** : Data from electronic health records, insurance claims, and patient registries are used to monitor safety signals and and understand long-term outcomes. This process is often part of **pharmacovigilance** , the science of drug safety monitoring. 

Last updated 2026-10-14 UTC. 



## Review design standards

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/review-design-standards

Verify design standards or existing product specifications, drawing on integrated enterprise data. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
What is the acceptable tolerance for the diameter of [COMPONENT]?
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

The acceptable tolerance for a 25 mm steel drive shaft depends entirely on its application and the type of "fit" required with its mating components, such as bearings or gears. There is no single universal tolerance. Instead, engineers use a standardized system, ISO 286, to define these tolerances. 

This system specifies different "fits," which are categorized into three main types: 

- **Clearance Fits:** The shaft is always smaller than the hole, allowing for rotation or sliding. 

- **Transition Fits:** There can be either a small clearance or a slight interference, used for precise location where disassembly might be needed. 

- **Interference Fits:** The shaft is intentionally larger than the hole, creating a solid, press-fit assembly that transmits torque. 

#### Factors That Determine the Right Tolerance

Several key factors must be considered to select the appropriate tolerance for a drive shaft: 

- **Mating Components:** The primary factor is what the shaft connects to. For instance, the fit for a ball bearing will be different from that for a gear or a pulley. 

- **Operating Conditions:** High speeds, heavy loads, and significant temperature variations all demand tighter and more specific tolerances to prevent failure. 

- **Rotational Component:** As a general rule, the part that rotates (usually the shaft) requires a tighter, interference fit with its mating component to prevent slipping or "creep." 

- **Material:** The material of both the shaft and the housing is important. For example, an aluminum housing expands more with heat than a steel one and may require a tighter initial fit. 

#### Common ISO Tolerances for a 25 mm Shaft

For a nominal 25 mm diameter shaft, here are some common ISO tolerance "classes" and their corresponding dimensions. These classes are designated by a letter (which sets the tolerance position relative to the nominal size) and a number (which indicates the tolerance magnitude). 

|Fit Type|ISO<br>Class|Upper Lim<br>(mm)|it<br>Lower Lim<br>(mm)|it<br>Application Examples|
|---|---|---|---|---|
|Clearance|h11|25.000|24.870|Used where high accuracy is not needed,|
|(Loose)||||suitable for large temperature variations.|
|Clearance|g6|24.993|24.980|For sliding parts and guiding shafts that need|
|(Running)||||to move and turn freely with high accuracy.|
|Clearance|...||||
|(Sliding)|||||

Last updated 2026-10-14 UTC. 



## Create target customer segments

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/target-customer-segments

Categorize a list of accounts into target segments. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
I'm attaching a CSV file containing a list of [COMPANIES]. For each company,
can you categorize them into [SEGMENT 1], [SEGMENT 2], [SEGMENT 3], and
[SEGMENT 4]? If one company falls into multiple categories, put it in the
category that best fits. If you encounter any ambiguity, prompt me to clarify
via chat.
```

### Example output

In response to this prompt, Gemini Enterprise produces output similar to the following: 

I have categorized all the companies from your file. I used a combination of automated searching and manual refinement to ensure accuracy. For companies where the category was ambiguous or for which I couldn't find enough information, I have marked them as "Uncategorized". 

Here is the complete list of companies and their assigned categories: 

|Company|Category|
|---|---|
|[COMPANY ONE]|Agencies & Consultancies|
|[COMPANY TWO]|Uncategorized|
|[COMPANY THREE]|Agencies & Consultancies|

Category 

Last updated 2026-10-14 UTC. 



## Write a personalized outreach email

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/personalized-email-outreach

Personalizing an outreach email can fail in two ways: an email can say nothing specific about the prospect, or the email can say something specific and wrong. You can use Gemini Enterprise to research an account, draft outreach grounded in the research, and separate the claims you can source from the ones you can't. 

The research and the drafting are two different jobs. Run the research first with the Deep Research agent, which produces a cited report, then bring that report into the Gemini Enterprise chat to draft from. 

### Before you begin

- To research a public company, select the **Deep Research** agent rather than asking the assistant to "do deep research" in a normal chat turn. 

- Attach your own product collateral to give the assistant specific product knowledge. 

- Personal profile pages on social networks are usually not retrievable. If a person's background matters, paste the relevant text into the prompt instead of linking to it. 

   - Researching a named individual may be subject to your organization's privacy and data-handling policies. 

### Example prompt

Select the Deep Research agent, and enter a prompt such as the following: 

```
Research Cymbal Retail Group, a public specialty retailer, for a sales
conversation. I want:
```

`1. Their stated strategic priorities for this fiscal year, in their own words, with a source for each.` 

`2. Operational problems they have publicly acknowledged, from earnings calls, annual reports, or press coverage. Quote them.` 

`3. Recent changes in leadership, structure, or technology spending.` 

`4. Anything that would make this a bad time to reach out.` 

```
Cite a source for every claim. If something is widely repeated but you cannot
find a primary source, say so.
```

Then, in the Gemini Enterprise chat box, enter a prompt such as the following: 

```
Using the research report above and the attached product one-pager for our
inventory forecasting platform, draft a first outreach email to the VP of
Supply Chain at Cymbal Retail Group.
Requirements:
1. **Under 150 words.** No greeting paragraph about how much I admire their
company.
```

`2. **One specific observation about their business**, drawn from the research and traceable to a source. Not a generic industry statement.` 

`3. **One connection to what we do**, using only capabilities stated in the attached one-pager.` 

```
4. **A low-commitment ask.** Not a demo request.
Then, separately from the email:
```

`5. **A source table:** every factual claim in the email, and where it came from.` 

```
6. **Claims I should verify before sending**, including anything sourced from a
secondary report rather than the company itself.
Rules:
```

- `Do not state anything about our product that is not in the attached one-pager. If the natural thing to say isn't in there, write [NOT IN COLLATERAL] and tell me what claim you wanted to make.` 

```
- Do not attribute a quote or a priority to an individual unless the source
attributes it to that individual by name.
```

- `Do not describe their current tools or vendors unless a source states them.` 

### Example output

In response to the drafting prompt, Gemini Enterprise produces output similar to the following: 

**Subject: Your Q3 comment on peak-season stockouts** 

Hi [NAME], 

On the Q3 call, your CFO said stockouts during peak "cost us more in lost sales than the markdowns did." That's a hard problem to fix with more safety stock, since it usually just moves the cost to the other side of the ledger. 

We build inventory forecasting that models promotional lift separately from baseline demand, which is typically where peak forecasts break down. Two of our customers are specialty retailers of roughly your store count. 

Worth 20 minutes to compare notes on how you're handling peak forecasting today? Happy to share what we've seen work even if we're not a fit. 

[YOUR NAME] 

#### Source table

|Claim in the email|Source|
|---|---|
|CFO comment on peak stockouts|Q3 earnings call transcript, prepared remarks —<br>quoted verbatim|
|They are a specialty retailer with a<br>comparable store count|Annual report, store count disclosure|

|Claim in the email|Source|
|---|---|
|We model promotional lift separately from|Attached one-pager, "Demand decomposition"|
|baseline demand|section|
|Two customers of similar profile|Attached one-pager, customer summary page|

#### Claims to verify before sending

- **The CFO quote is verbatim and attributed correctly** , but confirm it was the CFO and not the COO. The transcript attribution is clear; the secondary coverage I found attributed it to "management." 

- **"Two of our customers are specialty retailers of roughly your store count"** comes from the one-pager. Confirm you're allowed to reference them, even unnamed, in outbound email. 

- **[NOT IN COLLATERAL]** I wanted to say our forecasts improve peak accuracy by a specific percentage, because that would be the strongest line in the email. The one-pager contains no accuracy figure. If a defensible number exists, add it and I'll rewrite around it. 

#### What I deliberately left out

- A trade-press article claimed they are replacing their planning system this year. No company source confirms it, and being wrong about a prospect's stack in a first email is expensive. Omitted. 

- The VP's background. Their profile page could not be retrieved, so nothing in this email refers to them personally. 

Last updated 2026-10-14 UTC. 



## Prepare for a first meeting

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/first-meeting-preparation

When preparing to meet with a customer for the first time, use Gemini Enterprise to help you arrive with talking points that resonate. 

### Example prompt

In the chat box, enter a prompt such as the following: 

```
I have a crucial meeting tomorrow morning with [KEY STAKEHOLDER NAME], [TITLE]
at [COMPANY NAME]. Please use your Deep Research capabilities to prepare a
comprehensive meeting brief.
I need insights on:
```

- `[COMPANY NAME]'s recent market performance and strategic shifts.` 

- `[KEY STAKEHOLDER NAME]'s professional background, interests, and any recent public statements or articles.` 

- `Suggestions for personalized talking points that resonate with their specific role and the company's current situation.` 

```
Present this information in an easily digestible format, and be ready for
follow-up questions.
```

Last updated 2026-10-14 UTC.
