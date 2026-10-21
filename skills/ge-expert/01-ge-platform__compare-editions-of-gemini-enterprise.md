# Gemini Enterprise: platform, security, agents, cost, monitoring / Compare editions of Gemini Enterprise to Administrator guide
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 6-47, extracted 2026-10-18

Contains:
- Compare editions of Gemini Enterprise (pages 6-9) https://docs.cloud.google.com/gemini/enterprise/docs/editions
- Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise (pages 10-26) https://docs.cloud.google.com/gemini/enterprise/docs/locations
- Quotas and overages (pages 27-44) https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages
- Administrator guide (pages 45-47) https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin

## Compare editions of Gemini Enterprise

URL: https://docs.cloud.google.com/gemini/enterprise/docs/editions

Gemini Enterprise (https://cloud.google.com/gemini-enterprise) offers a range of AIpowered solutions designed to meet diverse organizational needs. These solutions are organized into distinct editions, each providing a specific set of features and capabilities tailored to different use cases and stages of AI adoption. This page describes these editions to help you choose the right solution for driving productivity and innovation in your organization. 

### Compare features

To compare features and capabilities of different Gemini Enterprise editions, see the following table. 

**Note:** To subscribe to the Gemini Enterprise Pay-as-you-go edition, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

||Gemini|Gemini|Gemini|Gemini|Gemini|
|---|---|---|---|---|---|
|Feature|Enterprise|Enterprise|Enterprise|Enterprise|Enterprise|
||Business|Standard|Plus|Pay-as-you-go|Frontline|
|Seats|1-500|1 or more|1 or more|1 minimum|150 or more|
||users|users|users|seat|users of|
|||||requirement|Standard or|
|||||to get started|Plus editions|
|Storage and data indexing per<br>user<sup>1</sup>|25 GiB,<br>pooled|30 GiB,<br>pooled|75 GiB,<br>pooled|Pay-as-you-go|2 GiB,<br>pooled|

Access select, segment-relevant connectors 

Access the full data connector ecosystem 

||Gemini|Gemini|Gemini|Gemini|Gemini|
|---|---|---|---|---|---|
|Feature|Enterprise|Enterprise|Enterprise|Enterprise|Enterprise|
||Business|Standard|Plus|Pay-as-you-go|Frontline|

Use permission-aware enterprise search 

Ground based on enterprise data from Google data sources and third-party data sources 

Get priority access to the latest Gemini models 

Get answers incorporating blended search and text generation 

Generate media (images and videos) 

Use Ground with Google Search 

Use Web Grounding 

Use permission-aware prebuilt tasks and agent actions 

Chat with published Gemini Notebook Enterprise notebooks 

Create and publish Gemini Notebook Enterprise notebooks 

Build and publish custom nocode agents using Gemini Enterprise no-code tools (preview) 

Use custom no-code agents built using Gemini Enterprise no-code tools (preview) 

Create and upload custom skills 

||Gemini|Gemini|Gemini|Gemini|Gemini|
|---|---|---|---|---|---|
|Feature|Enterprise|Enterprise|Enterprise|Enterprise|Enterprise|
||Business|Standard|Plus|Pay-as-you-go|Frontline|
|Use Google-managed skills and|||||2|
|user-created skills shared with||||||
|you||||||

Use Deep Research (Made by Google) 

Use Data Insights (Made by Google) 

Use your own full-code agents 3 built outside of Gemini Enterprise 

Access the Agent Marketplace 

Access basic agent governance and administration Enterprise-grade security and compliance 

AI developer tools (/gemini/enterprise/docs/aideveloper-tools-overview) 4 

1 Storage and data indexing quotas are pooled across all users in a project and location, regardless of edition. Other feature quotas are pooled within each edition. 

- 2 Gemini Enterprise Frontline users can install skills themselves from **Browse skills** . They can't create or upload custom skills. For more information, see Create and manage skills (/gemini/enterprise/docs/skills#supported-editions). 

- 3 With Gemini Enterprise Frontline, users can only access previously-developed agents that have been provisioned for them by their administrator. 

- 4 To configure and use AI developer tools, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types). For more 

(/gemini/enterprise/docs/ai-developer-tools-overview). 

### Next steps

- On the subscription details page, the **Subscription tier** field displays the edition of your current subscription. For more information, see View subscription details (/gemini/enterprise/docs/licenses#subscription-detail). 

- For information about acquiring subscriptions and assigning licenses, see Get licenses for Gemini Enterprise (/gemini/enterprise/docs/licenses). 

- For detailed information about quotas and overages, including edition-based pooling, see Quotas and overages (/gemini/enterprise/docs/quotas-and-overages). 

Last updated 2026-10-16 UTC. 



## Data residency for Gemini Enterprise Standard and Plus Editions and Gemini Notebook Enterprise

URL: https://docs.cloud.google.com/gemini/enterprise/docs/locations

This page lists the locations where Gemini Enterprise and Gemini Notebook Enterprise are available, along with their data residency commitments for at-rest storage (at-rest DRZ) and artificial intelligence (AI) or machine learning processing (MLP). 

Gemini Enterprise and Gemini Notebook Enterprise support **at-rest DRZ** in the multi-regions and in-country regions listed on this page, subject to limitations (#limitations). 

If you don't have security, or regulatory reasons to locate your customer data in the `us` or `eu` multi-regions or the in-country regions with respect to at-rest DRZ or MLP, Google recommends that you choose the `global` location. This is because the `global` location provides better end-user response times, the latest model versions, and the most up-to-date features. See Limitations for multi-regions and in-country regions (#limitations). 

### Multi-regions

The following tables list the multi-regions where Gemini Enterprise and Gemini Notebook Enterprise are available. 

#### Gemini Enterprise multi-regions

The following table lists the multi-regions where Gemini Enterprise is available. 

|Multi-region description|Multi-region name|
|---|---|
|API availability in the European Union|`eu`|
|API availability in the United States|`us`|

For Gemini Enterprise, MLP, such as training, prediction, and model tuning, occurs within the `us` multi-region when requests are made to regionally-available APIs in the US, or within the `eu` multi-region when requests are made to regionallyavailable APIs in Europe, subject to the limitations outlined below. 

#### Gemini Notebook Enterprise multi-regions

The following table lists the multi-regions where Gemini Notebook Enterprise is available. 

|Multi-region description|Multi-region name|
|---|---|
|API availability in the European Union|`eu`|
|API availability in the United States|`us`|

For more information on the limitations, see Limitations for multi-regions and incountry regions (#limitations). 

### In-country regions

Using these locations is in GA with allowlist. To get access to these locations for use with Gemini Enterprise or Gemini Notebook Enterprise, contact your Google account team. 

The following table lists the in-country regions and multi-regions where Gemini Enterprise and Gemini Notebook Enterprise are available. 

|In-country description|In-country name|
|---|---|
|API availability in Canada|`ca`|
|API availability in India|`in`|
|API availability in Japan|`asia-northeast1`|
|API availability in Singapore|`sg`|
|API availability in the United Kingdom|`europe-west2`|

These locations provide at-rest DRZ within the specified location. These in-country locations may be more constrained and have limitations (#limitations) similar to the `us` and `eu` multi-regions. 

### Specify a multi-region for your data store

To confine your Customer Data to at-rest DRZ in the `us` or `eu` multi-region, follow these steps: 

1. If you create the data store through the Google Cloud console, then choose **us (multiple regions in the United States)** or **eu (multiple regions in the European Union)** when you pick your app location. 

For more information, see Create an app (/gemini/enterprise/docs/create-app). 

2. For API calls, replace `global-discoveryengine` or `discoveryengine` with `eudiscoveryengine` or `us-discoveryengine` , and replace `global` with `eu` or `us` . The following table shows examples of the API paths: 

EU multi-region 

```
https://eu-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/eu/…
```

US multi-region 

```
https://us-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/us/…
```

Global multi-region (Two equivalent endpoints) 

With the `global` endpoint prefix: 

```
https://global-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/…
```

Without the `global` endpoint prefix: 

```
https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/gl
obal/…
```

3. For Gemini Notebook Enterprise, ensure the user is licensed and is using a notebook in the selected region. 

4. Review the limitations (#limitations) associated with using a specific multiregion. 

### Limitations for multi-regions and in-country regions

The following features of Gemini Enterprise that are supported globally may have limitations for certain multi-regions and in-country regions: 

#### Gemini Enterprise limitations

|Feature|US/EU multi-<br>regions<br> <br>|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Gemini<br>Enterprise<br>base<br>functionality|At-rest DRZ and<br>MLP supported.|Status - GA with<br>allowlist.<br>At-rest DRZ and<br>MLP supported.|Includes access-controlled data, blended<br>search, Workspace search, people<br>search, core search infrastructure,<br>Assistant, answer generation, ingested<br>and federated connectors, document<br>understanding, analytics, frontend,<br>Canvas, Agent Registry, Workflow<br>Builder, custom Agents and Agent<br>Engine Platform.|

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Gemini 4<br>Argon|At-rest DRZ and<br>MLP supported.|Only available in<br>the`global`<br>region.|Gemini 4 Argon is turned off by default<br>in the Gemini Enterprise app. Beginning<br>October 27, 2026, the model toggle<br>defaults to on. For AI developer tools,<br>Gemini 4 Argon is enabled by default for<br>licensed users when default model<br>selection is active. If a custom model list<br>is configured, an administrator must<br>manually select Gemini 4 Argon.<br>To manage availability, administrators<br>can use the Gemini 4 Argon toggle in the<br>Gemini Enterprise app or configure<br>access under Antigravity authorized<br>models. For more information, see<br>Manage features on the web app<br>(/gemini/enterprise/docs/manage-web-<br>app-features)<br>and<br>Configure AI developer tools<br>settings<br>(/gemini/enterprise/docs/ai-developer-<br>tools-settings)<br>.|
||||CA, IN, JP, SG, and UK regions don't offer<br>the Gemini 4 Argon model. For<br>unsupported in-country regions, you<br>must confirm the warning dialog to route<br>traffic to the`global`endpoint.|

|Feature|US/EU multi-<br>regions<br>In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|
|Gemini 3.1<br>Pro|At-rest DRZ and<br>MLP supported<br>in:`US`.<br>At-rest DRZ not<br>supported in:<br>`EU`.<br>MLP not<br>supported in:<br>`EU`.<br>At-rest DRZ not<br>supported.<br>MLP not<br>supported.|Gemini 3.1 Pro in Gemini Enterprise is in<br>Limited Availability. For AI developer<br>tools, Gemini 3.1 Pro (Preview) is<br>enabled by default for licensed users<br>when default model selection is active. If<br>a custom model list is configured, an<br>administrator must manually select<br>Gemini 3.1 Pro.<br>To manage availability, administrators<br>can use the Gemini 3.1 Pro toggle in the<br>Gemini Enterprise app or configure<br>access under Antigravity authorized<br>models. For more information, see<br>Manage features on the web app<br>(/gemini/enterprise/docs/manage-web-<br>app-features)<br>,<br>Limited availability of Gemini 3.1 Pro<br>(/gemini/enterprise/docs/known-<br>limitations#using-gemini-3-preview)<br>, and<br>Configure AI developer tools<br>settings<br>(/gemini/enterprise/docs/ai-developer-<br>tools-settings)<br>.|

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Gemini 3.8<br>Flash|At-rest DRZ and<br>MLP supported.|SG, UK: At-rest<br>DRZ and MLP<br>supported.|Gemini 3.8 Flash is enabled by default in<br>the`global`,`us`, and`eu`regions and in<br>the SG and UK in-country regions.<br>Administrators can turn on or turn off<br>the Gemini 3.8 Flash toggle in the<br>Gemini Enterprise app. For more<br>information, see<br>Manage features on the<br>web app<br>(/gemini/enterprise/docs/manage-web-<br>app-features)<br>and<br>Configure AI developer tools<br>settings<br>(/gemini/enterprise/docs/ai-developer-<br>tools-settings)<br>.<br>CA, IN, and JP regions don't offer the 3.8<br>Flash model. For unsupported in-country<br>regions, you must confirm the warning<br>dialog to route traffic to the`global`<br>endpoint.|

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Anthropic<br>model -<br>Claude Opus<br>5.5|At-rest DRZ and<br>MLP supported.|Not available.|In the Gemini Enterprise app, Claude<br>Opus 5.5 is supported in the`global`,`us`,<br>and`eu`regions. To make Claude Opus<br>5.5 available to users in the Gemini<br>Enterprise app, administrators must turn<br>on the Claude Opus 5.5 toggle in the<br>Enable third-party models section. For<br>more information, see<br>Enable third-party<br>models<br>(/gemini/enterprise/docs/manage-web-<br>app-features#enable-third-party-models)<br>.|
||||To see the list of countries and regions<br>that the model is supported in, see<br>Supported countries and regions<br>(https://www.anthropic.com/supported-<br>countries)<br>in the Anthropic documentation.|
||||For model details, see the<br>Claude Opus<br>5.5<br>(/gemini-enterprise-agent-<br>platform/models/partner-<br>models/claude/opus-5-5)<br>model card.|

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Anthropic<br>model -<br>Claude<br>Sonnet 5.5|At-rest DRZ and<br>MLP supported.|Not available.|In the Gemini Enterprise app, Claude<br>Sonnet 5.5 is supported in the`global`,<br>`us`, and`eu`regions. To make Claude<br>Sonnet 5.5 available to users in the<br>Gemini Enterprise app, administrators<br>must turn on the Claude Sonnet 5.5<br>toggle in the Enable third-party models<br>section. For more information, see<br>Enable third-party models<br>(/gemini/enterprise/docs/manage-web-<br>app-features#enable-third-party-models)<br>.|
||||To see the list of countries and regions<br>that the model is supported in, see<br>Supported countries and regions<br>(https://www.anthropic.com/supported-<br>countries)<br>in the Anthropic documentation.<br>For model details, see the<br>Claude Sonnet<br>5.5<br>(/gemini-enterprise-agent-<br>platform/models/partner-<br>models/claude/sonnet-5-5)<br>model card.|

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Gemini 3.7<br>Flash|At-rest DRZ and<br>MLP supported.|Only available in<br>the`global`<br>region.|Gemini 3.7 Flash is turned off by default<br>in the Gemini Enterprise app. For AI<br>developer tools, Gemini 3.7 Flash is<br>enabled by default for licensed users<br>when default model selection is active. If<br>a custom model list is configured, an<br>administrator must manually select<br>Gemini 3.7 Flash.|
||||To manage availability, administrators<br>can use the Gemini 3.7 Flash toggle in<br>the Gemini Enterprise app or configure<br>access under Antigravity authorized<br>models. For more information, see<br>Manage features on the web app<br>(/gemini/enterprise/docs/manage-web-<br>app-features)<br>and<br>Configure AI developer tools<br>settings<br>(/gemini/enterprise/docs/ai-developer-<br>tools-settings)<br>.<br>For unsupported in-country regions, you<br>must confirm the warning dialog to route<br>traffic to the`global`endpoint.|

|Feature|US/EU multi-<br>regions<br>In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|
|Gemini 3.6<br>Flash|At-rest DRZ and<br>MLP supported.<br>Only available in<br>the`global`<br>region.|Gemini 3.6 Flash is turned off by default<br>in the Gemini Enterprise app. For AI<br>developer tools, Gemini 3.6 Flash is<br>enabled by default for licensed users<br>when default model selection is active. If<br>a custom model list is configured, an<br>administrator must manually select<br>Gemini 3.6 Flash.|
|||To manage availability, administrators<br>can use the Gemini 3.6 Flash toggle in<br>the Gemini Enterprise app or configure<br>access under Antigravity authorized<br>models. For more information, see<br>Manage features on the web app<br>(/gemini/enterprise/docs/manage-web-<br>app-features)<br>and<br>Configure AI developer tools<br>settings<br>(/gemini/enterprise/docs/ai-developer-<br>tools-settings)<br>.<br>For unsupported in-country regions, you<br>must confirm the warning dialog to route<br>traffic to the`global`endpoint.|
|Gemini 3.5|At-rest DRZ and<br>At-rest DRZ and||
|Flash|MLP supported.<br>MLP supported.||

|Feature|US/EU multi-<br>regions<br>I<br>(|n-country regions<br>CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Gemini 2.5<br>Pro|At-rest DRZ and<br>MLP supported.|CA, JP: At-rest<br>DRZ and MLP<br>supported until<br>October 20, 2026.<br>Gemini 2.5 Pro is<br>deprecated in the<br>CA and JP regions<br>and isn't available<br>after October 20,<br>2026.|<br> <br>IN, SG, UK regions don't offer the 2.5 Pro<br>model.<br>Gemini 2.5 Pro is turned on by default in<br>the`global`,`us`, and`eu`regions.<br>Administrators can turn off the Gemini<br>2.5 Pro toggle to make the model<br>unavailable to users in the Gemini<br>Enterprise app. For more information,<br>see<br>Manage features on the web app<br>(/gemini/enterprise/docs/manage-web-<br>app-features)<br>.|
|Model Armor|At-rest DRZ and<br>MLP supported.|At-rest DRZ<br>supported.<br>MLP supported.|Model Armor is also not available in the<br>global region. Previously created Model<br>Armor templates in CA, IN, JP, SG, and<br>UK continue to call out-of-region to avoid<br>breaking changes for customers.|
|CMEK|At-rest DRZ and<br>MLP supported.|At-rest DRZ and<br>MLP supported.|CMEK is also not available in the global<br>region. For more information, see<br>Customer-managed encryption keys<br>(CMEK)(/gemini/enterprise/docs/cmek).<br>To use this security feature, you must<br>choose either the US multi-region or the<br>EU multi-region.|
|Autocomplete|At-rest DRZ and<br>MLP supported,<br>but tail match<br>suggestions<br>and advanced<br>document data<br>mode features<br>can't be used.|At-rest DRZ and<br>MLP supported,<br>but tail match<br>suggestions and<br>advanced<br>document data<br>mode features<br>can't be used.|Tail match suggestions and advanced<br>document data mode are only available<br>in`global`. For more information, see<br>Configure autocomplete<br>(/gemini/enterprise/docs/configure-<br>autocomplete)<br>.|
|Dynamic<br>facets|Only available<br>in the`global`<br>region.|Only available in<br>the`global`<br>region.|Even if a field is set to Dynamic<br>Facetable, Gemini Enterprise doesn't<br>generate dynamic facets in these<br>locations.|

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Grounding<br>with Google<br>Search|Only available<br>in the`global`<br>region.|Only available in<br>the`global`<br>region.|The Grounding with Google Search<br>feature has several additional<br>limitations, which are described further<br>in the Grounding with Google Search<br>Service<br>Specific Terms<br>(https://cloud.google.com/terms/service-<br>terms)<br>and in the<br>Gemini Enterprise Agent<br>Platform product documentation<br>(/gemini-enterprise-agent-<br>platform/models/grounding/grounding-<br>with-google-search)<br>pages. Notably, Grounding with Google<br>Search temporarily logs certain pieces of<br>Customer Data as part of providing this<br>feature.|
|Web<br>Grounding for<br>Enterprise|At-rest DRZ<br>supported.<br>MLP supported.|At-rest DRZ not<br>supported.<br>MLP not<br>supported.|Grounding features are turned on by<br>default for US/EU.|
|Gemini 3.1<br>Flash image<br>(Nano<br>Banana 2)|At-rest DRZ and<br>MLP supported.|Only available in<br>the`global`<br>region.|To make Gemini 3.1 Flash image<br>available to users in the Gemini<br>Enterprise app, administrators must turn<br>on the Gemini 3.1 Flash image toggle.<br>For more information, see<br>Manage<br>features on the web app<br>(/gemini/enterprise/docs/manage-web-<br>app-features)<br>.|

|Feature|US/EU multi-<br>regions<br> <br>|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Gemini 3 Pro<br>image (Nano<br>Banana Pro)|Only available<br>in the`global`<br>region.|Only available in<br>the`global`<br>region.|To make Gemini 3 Pro image available to<br>users in the Gemini Enterprise app,<br>administrators must turn on the Gemini<br>3 Pro image toggle. For more<br>information, see<br>Manage features on the<br>web app<br>(/gemini/enterprise/docs/manage-web-<br>app-features)<br>.|
||||For unsupported in-country, US, and EU<br>regions, you must confirm the warning<br>dialog to route traffic to the`global`<br>endpoint.|
|Gemini 2.5<br>Flash image|At-rest DRZ and<br>MLP supported.|At-rest DRZ not<br>supported.<br>MLP not<br>supported.|The system defaults to this model if an<br>administrator doesn't select an image<br>model.|
|Video<br>generation|Only available<br>in the`global`<br>region.|Only available in<br>the`global`<br>region.||

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|AI developer<br>tools|Follows the<br>data residency<br>(at-rest DRZ)<br>and machine<br>learning<br>processing<br>(MLP)<br>commitments<br>of the selected<br>model. For<br>details, see the<br>model's entry in<br>this table.|<br>At-rest DRZ not<br>supported.<br>MLP not<br>supported.|Includes Antigravity app, Antigravity CLI,<br>Antigravity for IDEs, and Android Studio.<br>If a model isn't available in your region,<br>select a supported model or region listed<br>in this table.<br>AI developer tools also support third-<br>party models: Anthropic models - Claude<br>Opus 5.5 and Claude Sonnet 5.5.<br>Inference is available in the`global`,`us`,<br>and`eu`locations (in-country regions<br>aren't supported). Third-party models<br>are turned off by default and require<br>administrator opt-in. For more<br>information, see<br>Configure AI developer<br>tools settings<br>(/gemini/enterprise/docs/ai-developer-<br>tools-settings#enable-third-party-<br>models)<br>.|

#### Gemini Notebook Enterprise limitations

The following features of Gemini Notebook Enterprise are supported globally but may have limitations for certain multi-regions and in-country regions: 

**Note:** Machine learning processing (MLP) is supported for base functionality in the US and EU multi-regions. It is not supported for other features or in in-country regions. 

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Base|At-rest DRZ|At-rest DRZ|Includes adding sources to generate|
|functionality|supported.|supported.|embeddings and interacting with them|
||MLP supported.|MLP supported.|to query, chat, or generate summaries.|

|Feature|US/EU multi-<br>regions|In-country regions<br>(CA, IN, JP, SG, UK)|Notes|
|---|---|---|---|
|Gemini<br>Notebook<br>Content<br>Studio|At-rest DRZ<br>supported.<br>MLP not<br>supported.|Not available.<br>MLP not supported.|<br>Content Studio includes audio<br>overviews, slide decks, infographics, and<br>video overviews.|
|Discover<br>Sources|At-rest DRZ n<br>supported.<br>MLP not<br>supported.|ot<br>At-rest DRZ not<br>supported.<br>MLP not supported.|<br>Discover Sources is powered by<br>Grounding with Google Search. The<br>Grounding with Google Search feature<br>has several additional limitations, which<br>are described further in the Grounding<br>with Google Search Service<br>Specific<br>Terms<br>(https://cloud.google.com/terms/service-<br>terms)<br>and in the<br>Gemini Enterprise Agent<br>Platform product documentation<br>(/gemini-enterprise-agent-<br>platform/models/grounding/grounding-<br>with-google-search)<br>pages. Notably, Grounding with Google<br>Search temporarily logs certain pieces of<br>customer data as part of providing this<br>feature.|

#### Agent Runtime limitations

The following features of Agent Runtime are supported globally but may have limitations for certain multi-regions and in-country regions: 

|Feature|US/EU multi-regions|In-country regions (CA, IN, JP, SG,<br>UK)|
|---|---|---|
|Memory Bank and Sessions|At-rest DRZ supported.|At-rest DRZ supported.|
|Runtime|At-rest DRZ supported.|At-rest DRZ supported.|
|Code execution|At-rest DRZ supported in US.<br>At-rest DRZ not supported in<br>EU.|At-rest DRZ not supported.|

#### AlphaEvolve limitations

AlphaEvolve features are supported globally but may have limitations for certain multi-regions and in-country regions. 

|Feature|US/EU multi-regions|In-country regions (CA, IN, JP, SG,<br>UK)|
|---|---|---|
|Base functionality (with Gemini 4<br>Argon)|At-rest DRZ<br>supported.|At-rest DRZ not supported.|
||MLP supported.|MLP not supported.|
|Base functionality (with Gemini 3.8<br>Flash)|At-rest DRZ<br>supported.|At-rest DRZ not supported.|
||MLP supported.|MLP not supported.|
|Base functionality (with Gemini 3.7<br>Flash)|At-rest DRZ<br>supported.|At-rest DRZ not supported.|
||MLP supported.|MLP not supported.|
|Base functionality (with Gemini 3.5<br>Flash)|At-rest DRZ<br>supported.|At-rest DRZ not supported.|
||MLP supported.|MLP not supported.|
|Base functionality (with Gemini 3.1<br>Pro)|At-rest DRZ<br>supported.|At-rest DRZ not supported.|
||MLP not supported.|MLP not supported.|

Last updated 2026-10-15 UTC. 



## Quotas and overages

URL: https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages

**Note:** The quotas and overages on this page don't apply to users who received the email with the subject line _[Billing Update] New Gemini Enterprise overage billing controls launching August 17, 2026_ . If you received this email, see Quotas and overages (Legacy) (/gemini/enterprise/docs/overages). 

Your subscription entitles you to certain quotas across product features. If you have a pay-as-you-go subscription, there are no feature quota limits; you pay for what you use. For seat-based subscriptions, unlike other Google Cloud services, Gemini Enterprise feature quotas don't require manual increase requests; they're automatically adjusted based on the number of licenses or seats in your subscription, including free-trial subscriptions. 

**Note:** Google Cloud products that use the Discovery Engine API, including Agent Search and Gemini Enterprise, share the technical rate and allocation quotas listed on this page. However, license-based feature quotas apply only to Gemini Enterprise and aren't shared with Agent Search. 

**Note:** As a Discovery Engine administrator, you can view pooled quota usage. For more information, see View the pooled quota usage (/gemini/enterprise/docs/feature-usage#view-quota-usage). 

### Feature and edition-based quotas

Except for storage and data indexing, feature quotas are pooled across users in the same edition within a project and location. Storage and data indexing quota is pooled per project and location across all users, but it is not segmented by the edition—all editions share a single storage and data indexing pool. For all other feature quotas, users with licenses for a specific edition share a single combined limit per project and location. 

For detailed system limits, subagent depth constraints, file upload thresholds, and sharing member caps that apply to custom agents, see Workflow Builder quotas and limits (/gemini/enterprise/docs/workflow-builder/quotas-and-limits). 

Use case 1: Multiple editions in one project and location 

If you have users with different editions in the same project and location, quota pools are maintained separately for each edition except for storage and data indexing: 

- **Standard feature quotas:** Quotas are pooled separately by edition in each project and location. For example, if a project and location has 100 Standard edition licenses and 50 Plus edition licenses, your Standard edition users share a pool of 16,000 Assistant queries per day (100 licenses × 160 queries), and your Plus edition users share a separate pool of 10,000 queries per day (50 licenses × 200 queries). These feature quota pools don't combine across editions. 

- **Storage and data indexing:** Quotas are pooled per project and location across all users, regardless of edition. For example, if a project and location has 100 Standard edition licenses (30 GiB per user) and 50 Plus edition licenses (75 GiB per user), there is a single combined storage pool of 6,750 GiB ((100 × 30 GiB) + (50 × 75 GiB)) shared by all users in that project and location across all editions. 

Use case 2: Quota pooling within a single edition 

Within an edition's quota pool, the following rules apply. For example, if you have 10 Standard edition licenses, your users share a total pooled quota of 1,600 queries per day (10 licenses × 160 queries): 

- The 10 Standard edition users share a combined pool of 1,600 queries for the day. 

- One power user can use 500 queries, leaving 1,100 queries for the remaining users in that edition. 

- Individual usage isn't capped at the per-user limit; all users in the edition draw from their edition's shared pool until it is depleted. 

#### Quota reset times

Pooled quotas reset on the following schedule: 

|Feature|Reset schedule|
|---|---|
|All features except AI developer<br>tools|Daily at midnight Pacific Time (PT)|
|AI developer tools|Every seven days, starting from when a prompt or request|
|(/gemini/enterprise/docs/ai-<br>developer-tools-overview)|is first sent to an AI developer tool.<br>For example, if a user in your project sends the first<br>prompt using Antigravity on Wednesday at 2 PM Pacific<br>Time (PT), the seven-day quota cycle starts at that time,<br>and the AI developer tools quota resets the following<br>Wednesday at 2 PM PT.|

#### Quotas for Standard and Plus editions

**Note:** When your project reaches its pooled feature quota for Standard or Plus editions, you can enable overages (#overages) to allow uninterrupted usage at pay-as-you-go rates. 

For information about quotas across Gemini Enterprise Standard and Plus editions, see the following table: 

|||Gemini Enterprise<br>Standard|Gemini Enterprise Plus|
|---|---|---|---|
||Pooled or unpooled|Pooled across users|Pooled across users|
|Quotas||within the edition per|within the edition per|
|||project and location|project and location|

|||Gemini Enterprise<br>Standard|Gemini Enterprise Plus|
|---|---|---|---|
||Storage + data indexing|30 GiB|75 GiB|
||Assistant|160 queries per day|200 queries per day|
||No-code agent building<br>tools - create<sup>4</sup>|1 agent per day|10 agents per day|
|Product|No-Code agent building<br>tools - use|Based on underlying ag|ent actions<sup>4</sup>|
||Video generation|2 video generation<br>requests per day|3 video generation<br>requests per day|
||Image generation|5 images per day|10 images per day|
|Gl|Gemini Notebook - use|Gemini Notebook<br>Enterprise limits<sup>1</sup>|Gemini Notebook<br>Enterprise limits<sup>1</sup>|
|enera purpose<br>agents made by<br>Google|Gemini Notebook - create &<br>publish|Gemini Notebook<br>Enterprise limits<sup>1</sup>|Gemini Notebook<br>Enterprise limits<sup>1</sup>|
||Deep Research|3 per day|10 per day|
|AI developer<br>tools<sup>2</sup>|Included Google Antigravity,<br>Antigravity for IDEs, and<br>Android Studio credits|<br>$10 credit per user per<br>month<sup>3</sup>|$15 credit per user per<br>month<sup>3</sup>|

- 1 For information about Gemini Notebook Enterprise usage limits, see the Gemini Notebook Enterprise documentation 

- (/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits). 

- 2 AI developer tools are available only for invoiced Cloud Billing accounts (/billing/docs/concepts#billing_account_types), including accounts with a free-trial 

- subscription. 

3 Although quotas are listed as a monthly per-user amount, Gemini Enterprise enforces them on a rolling seven-day basis as a shared pool. Gemini Enterprise calculates your project's weekly quota by dividing the monthly per-user value by four and multiplying it by your project's total licensed seats, including free-trial seats. Any user in your edition can draw from this shared weekly pool. Unused quota doesn't roll over to the next week. 

4 Daily creation quotas apply to both creating custom agents in Workflow Builder and registering external or custom agents (such as A2A, ADK, or Dialogflow agents) in an app. Each registration in an engine or app consumes 1 creation quota unit. For detailed agent creation limits, registration quotas across multi-app architectures, subagent depth constraints, file upload thresholds, and sharing member caps, see Workflow Builder quotas and limits 

(/gemini/enterprise/docs/workflow-builder/quotas-and-limits#creation-quotas). 

#### Quotas and pricing for the Pay-as-you-go edition

**Note:** To subscribe to the Gemini Enterprise Pay-as-you-go edition, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

The Gemini Enterprise Pay-as-you-go edition has no feature quota limits, as you pay for what you use. To get started, you need to have an invoiced Cloud Billing account and purchase a subscription to the Pay-as-you-go edition. For more information, see Cloud Billing account types 

(/billing/docs/concepts#billing_account_types) and Get subscriptions and assign licenses (/gemini/enterprise/docs/licenses#about-subscriptions). 

The following table lists the rates and pricing for this edition: 

Pay-as-you-go charges for features 

Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs (https://cloud.google.com/skus/) apply. Charges are subject to a variable support fee depending on the support service. For more information on the support services, see Compare support services (/support/docs/overview#compare-support). 

|||Gemini Enterprise<br>Pay-as-you-go charges|
|---|---|---|
||Storage + data<br>indexing|$5 per GiB per month|
||Assistant -<br>Gemini models|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-agent-<br>platform/generative-ai/pricing#cost-of-building-and-<br>deploying-ai-models-in-agent-platform)|
||Assistant -<br>Claude models|Claude pricing(#claude-pricing-pay-as-you-go)|
||No-code agent<br>building tools -|n/a|
|Foundational|create||
|engagement layer|<br>No-code agent<br>building tools -<br>use|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-agent-<br>platform/generative-ai/pricing#cost-of-building-and-<br>deploying-ai-models-in-agent-platform)|
||Video<br>generation|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-agent-<br>platform/generative-ai/pricing#cost-of-building-and-<br>deploying-ai-models-in-agent-platform)|
||Image|Agent Platform prices|
||generation|(https://cloud.google.com/gemini-enterprise-agent-<br>platform/generative-ai/pricing#cost-of-building-and-<br>deploying-ai-models-in-agent-platform)|
|General purpose<br>agents made by<br>Google|Deep Research|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-agent-<br>platform/generative-ai/pricing#cost-of-building-and-<br>deploying-ai-models-in-agent-platform)|
||Gemini models|Agent Platform prices|
|||(https://cloud.google.com/gemini-enterprise-agent-|
|AI developer<br>tools<sup>1</sup>||platform/generative-ai/pricing#cost-of-building-and-<br>deploying-ai-models-in-agent-platform)|
||Claude models|Claude pricing(#claude-pricing-pay-as-you-go)|

1 AI developer tools are available only for invoiced Cloud Billing accounts 

(/billing/docs/concepts#billing_account_types), including accounts with a free-trial subscription. 

Claude pricing 

Pay-as-you-go charges for Claude models apply as defined in the following table: 

**Note:** Claude model pricing and discounts in the Gemini Enterprise app are distinct from pricing procured through Google Cloud Marketplace. 

GlobalUS Multi-Region (US)… EU Multi-Region (EU)… (#global) 

|Model|Type|Model price (/1M tokens)<br>=< 200K input tokens|Model price (/1M tokens)<br>> 200K input tokens|
|---|---|---|---|
||Input|$4.00|$4.00|
||Output|$20.00|$20.00|
|Claude Opus 5.5|5m Cache Write|$5.00|$5.00|
||1h Cache Write|$8.00|$8.00|
||Cache Hit|$0.20|$0.20|
||Input|$2.00|$2.00|
||Output|$10.00|$10.00|
|Claude Sonnet 5.5|5m Cache Write|$2.50|$2.50|
||1h Cache Write|$4.00|$4.00|
||Cache Hit|$0.20|$0.20|

#### Quotas for EDU and EDU Pro editions

**Note:** When your project reaches its pooled feature quota for EDU or EDU Pro editions, you can enable overages (#overages) to allow uninterrupted usage at pay-as-you-go rates. 

For information about quotas across Gemini Enterprise EDU and EDU Pro editions, see the following table: 

|||Gemini Enterprise EDU|Gemini Enterprise EDU Pro|
|---|---|---|---|
|Quotas (Pooled or|Unpooled)|Pooled across users within<br>the edition per project and<br>location|Pooled across users within<br>the edition per project and<br>location|
||Storage + data<br>indexing|5 GiB|50 GiB|
||Assistant<sup>2</sup>|40 queries per day|200 queries per day|
||No-code agent<br>building tools -|1 agent per day|10 agents per day|
|Product|Create|||
||No-Code agent<br>building tools - use|<br>Based on underlying agent|actions|
||Video generation|1 video generation<br>requests per day|3 video generation<br>requests per day|
||Image generation|2 images per day|10 images per day|
|General purpose|Gemini Notebook -<br>use|Gemini Notebook<br>Enterprise limits<sup>1</sup>|Gemini Notebook<br>Enterprise limits<sup>1</sup>|
|<br>agents made by<br>Google|Gemini Notebook -<br>create & publish|Gemini Notebook<br>Enterprise limits<sup>1</sup>|Gemini Notebook<br>Enterprise limits<sup>1</sup>|
||Deep Research|1 per day|10 per day|
|Security and|Model Armor|Same quota as the|Same quota as the|
|compliance||assistant|assistant|

1 For information about Gemini Notebook Enterprise usage limits, see the Gemini Notebook Enterprise documentation 

(/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits). 

2 This includes the usage of Google Search and Web Grounding. 

#### Quotas for Frontline editions

**Note:** When your project reaches its pooled feature quota for Frontline editions, you can enable overages (#overages) to allow uninterrupted usage at pay-as-you-go rates. 

For information about quotas across Gemini Enterprise Frontline Starter and Worker, see the following table: 

|||Gemini Enterprise Frontline<br>Starter|Gemini Enterprise<br>Frontline Worker|
|---|---|---|---|
|Quotas (Pooled or|Unpooled)|Pooled across users within<br>the edition per project and<br>location|Pooled across users within<br>the edition per project and<br>location|
||Storage + data<br>indexing|2 GiB|2 GiB|
||Search|Abuse preventative only<sup>2</sup>||
||Assistant|20 queries per day|40 queries per day|
||No-code agent|n/a|n/a|
|Product|building tools -<br>create|||
||No-Code agent<br>building tools - use|<br>Based on underlying agent|actions|
||Video generation|n/a|1 video generation request<br>per day|
||Image generation|n/a|2 images per day|
|General-purpose|Gemini Notebook -<br>use|<br>Gemini Notebook Enterprise<br>limits<sup>1</sup>|<br>Gemini Notebook<br>Enterprise limits<sup>1</sup>|
|agents made by<br>Google|Gemini Notebook -<br>create & publish|<br>n/a|n/a|
||Deep Research|n/a|1 per day|
|Security and|Model Armor|Equivalent to assistant||
|Compliance||quota||

1 For information about Gemini Notebook Enterprise usage limits, see the Gemini Notebook Enterprise documentation 

(/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits). 

2Subject to abuse-preventative usage limits only. 

#### Quotas for Emerging Market editions

**Note:** When your project reaches its pooled feature quota for Emerging Market editions, you can enable overages (#overages) to allow uninterrupted usage at pay-as-you-go rates. 

For information about quotas across Gemini Enterprise Emerging Market editions, see the following table: 

|||Gemini Enterprise|Gemini Enterprise|
|---|---|---|---|
|||Standard Emerging<br>Market|Emerging Market EDU<br>and governments|
|Quotas (Poole|d or Unpooled)|Pooled across users<br>within the edition per<br>project and location|Pooled across users<br>within the edition per<br>project and location|
||Storage + data indexing|10 GiB|3 GiB|
||Search|Abuse preventative onl|y<sup>2</sup>5 queries per day|
||Assistant|40 queries per day|5 queries per day,<br>individual only|
|Product|No-code agent building<br>tools - create|1 agent per day|1 agent per day|
||No-Code agent building<br>tools - use|Based on underlying ag|ent actions|
||Video generation|n/a|n/a|
||Image generation|n/a|1 image per day|

|||Gemini Enterprise<br>Standard Emerging<br>Market|Gemini Enterprise<br>Emerging Market EDU<br>and governments|
|---|---|---|---|
|General-urose|Gemini Notebook<br>Enterprise - use|Gemini Notebook<br>Enterprise limits<sup>1</sup>|n/a|
|pp<br>agents made by<br>Google|Gemini Notebook -<br>create & publish|Gemini Notebook<br>Enterprise limits<sup>1</sup>|n/a|
||Deep Research|1 per day|n/a|
|AI developer tools|Includes Antigravity,<br>Antigravity for IDEs, a<br>Android Studio|nd<br>Doesn't include default<br>quotas<sup>3</sup>|n/a|
|Security and<br>Compliance|Model Armor|Same quota as the<br>assistant|Same quota as the<br>assistant|

1 For information about Gemini Notebook Enterprise usage limits, see the Gemini Notebook Enterprise documentation 

(/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits). 

2Subject to abuse-preventative usage limits only. 

3AI developer tools don't include bundled quota in the Standard Emerging Market edition. 

### API and system quotas

This section lists the technical infrastructure quotas and system limits for Discovery Engine API resources used by Gemini Enterprise. System limits are fixed values that cannot be changed. 

#### Allocation quotas

The following table lists the allocation quotas for Discovery Engine API. These quotas don't reset over time. Instead, they're released when you release the resource. 

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources. 

The Cloud Quotas system does the following: 

- Monitors your consumption of Google Cloud products and services 

- Restricts your consumption of those resources 

- Provides a way to request changes to the quota value (/docs/quotas/help/request_increase) and automate quota adjustments (/docs/quotas/quota-adjuster) 

In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails. 

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the Cloud Quotas overview (/docs/quotas/overview). 

|Quota|Value|
|---|---|
|Total number of data stores per project|100<sup>1</sup>|
|Total number of engines per project|150<sup>2</sup>|
|Regional number of data stores per project per location (Global, US, EU)|100|
|Regional number of documents per project per location (Global, US, EU)|10,000,000|
|Regional number of engines per project per location (Global, US, EU)|150|

1 Due to a technical limitation, the maximum quota for data stores is 500 per project. If you need more data stores, use new projects. Each entity in a data store is counted as a data store instance and, therefore, counts toward this quota. For example, a data store with three entities counts as three data stores against your quota. 

2 Due to a technical limitation, the maximum quota for engines is 500 per project. If you need more engines, use new projects. 

**Note:** The number of data stores, documents, and engines across all locations can't exceed the total per-project quota for that resource. For example, if you already have 60 data stores in the **`eu`** multi-region and 40 in the **`us`** multi-region, you can't create another data store because the overall data store quota for the project is 100. 

#### Rate quotas

The following rate quotas apply to Discovery Engine API requests. 

There are also _system limits_ on Gemini Enterprise resources. System limits can't be changed. 

|Quota|Value|
|---|---|
|Complete query requests per minute per project|300|
|Regional search requests per minute per project per location (Global, US, EU)|300|

### Pay-as-you-go usage above quota

Feature usage is restricted when you exceed the feature quotas of your Gemini Enterprise edition. To avoid interruptions, a Gemini Enterprise administrator can turn on the **Pay-as-you-go usage above quota** setting. Pay-as-you-go usage above quota is available only if your project has an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) and at least one active, non-free-trial subscription. Free-trial subscriptions include the base pooled quotas for their edition, including AI developer tools credits, but aren't eligible for overages. To 

verify your account type, see Find out your Cloud Billing account type and charging cycle (/billing/docs/how-to/billing-cycle#view-your-charging-cycle). 

**Note:** Claude models are available only with pay-as-you-go usage. Ensure that you have turned on **Pay-as-you-go usage above quota** for all editions where you turn on Claude models for your end users. 

Pay-as-you-go charges apply as defined in the following table for all license-based editions (Standard, Plus, Frontline, EDU, and Emerging Market editions). 

If you have a Pay-as-you-go subscription, you pay for usage at the Pay-as-you-go rates listed in the following table. 

**Note:** Usage that exceeds the quota for **storage + data indexing** automatically incurs overage charges. Because storage and data indexing quota is pooled per project and location across all editions, any usage exceeding the single shared pool for the project and location incurs overage charges. You pay storage and data indexing overage charges prorated by the duration you store the data. For example, if you store 30 GiB of excess data for one day in a 30-day month, you pay $5 (30 GiB / 30 days × $5 per GiB per month). 

#### Pay-as-you-go charges for features above quota

Prices are listed in US Dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on Cloud Platform SKUs (https://cloud.google.com/skus/) apply. Charges are subject to a variable support fee depending on the support service. For more information on the support services, see Compare support services (/support/docs/overview#compare-support). 

||Gemini Enterprise<br>Quota units|Gemini Enterprise<br>Pay-as-you-go charges|
|---|---|---|
||Pooled across|Pooled across users within the edition per|
|Quotas (Pooled or Unpooled)|users within the<br>edition per project<br>and location|<br>project and location|

|||Gemini Enterprise<br>Quota units|Gemini Enterprise<br>Pay-as-you-go charges|
|---|---|---|---|
||Storage +<br>data indexing|GiB|$5 per GiB per month|
||Assistant -<br>Gemini<br>models|Queries per day|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-<br>agent-platform/generative-ai/pricing#cost-of-<br>building-and-deploying-ai-models-in-agent-<br>platform)|
||Assistant -<br>Claude<br>models|n/a - only<br>available through<br>Pay-as-you-go<br>above quota<br>charges.|Claude pricing(#claude-pricing)|
||No-code<br>agent|Agents per day|n/a|
|Foundational<br>engagement<br>|building tools<br>- create|||
|layer|No-code<br>agent<br>building tools<br>- use|Based on<br>underlying agent<br>actions|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-<br>agent-platform/generative-ai/pricing#cost-of-<br>building-and-deploying-ai-models-in-agent-<br>platform)|
||Video<br>generation|Video generation<br>requests per day|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-<br>agent-platform/generative-ai/pricing#cost-of-<br>building-and-deploying-ai-models-in-agent-<br>platform)|
||Image<br>generation|Images per day|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-<br>agent-platform/generative-ai/pricing#cost-of-<br>building-and-deploying-ai-models-in-agent-<br>platform)|

|||Gemini Enterprise<br>Quota units|Gemini Enterprise<br>Pay-as-you-go charges|
|---|---|---|---|
||Gemini<br>Notebook<br>Enterprise -<br>use|Gemini Notebook<br>Enterprise limits<sup>1</sup>|n/a|
|General<br>purpose agent<br>made by<br>Google|s<br>Gemini<br>Notebook<br>Enterprise -<br>create &<br>publish|Gemini Notebook<br>Enterprise limits<sup>1</sup>|n/a|
||Deep<br>Research|Queries per day|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-<br>agent-platform/generative-ai/pricing#cost-of-<br>building-and-deploying-ai-models-in-agent-<br>platform)|
|AI developer<br>tools<sup>2</sup>|Gemini<br>models|Dollars per<br>month<sup>3</sup>in credits<br>for Antigravity,<br>Antigravity for<br>IDEs, and Android<br>Studio|Agent Platform prices<br>(https://cloud.google.com/gemini-enterprise-<br>agent-platform/generative-ai/pricing#cost-of-<br>building-and-deploying-ai-models-in-agent-<br>platform)|
||Claude<br>models|n/a - only<br>available through<br>Pay-as-you-go<br>above quota<br>charges.|Claude pricing(#claude-pricing)|

- 1 For information about Gemini Notebook Enterprise usage limits, see the Gemini Notebook Enterprise documentation 

(/gemini/enterprise/notebooklm-enterprise/docs/overview#usage-limits). 

- 2 AI developer tools are available only for invoiced Cloud Billing accounts (/billing/docs/concepts#billing_account_types), including accounts with a free-trial 

- subscription. 

- 3 Although quotas are listed as a monthly per-user amount, Gemini Enterprise enforces them on a rolling seven-day basis as a shared pool. Gemini Enterprise calculates your project's weekly quota by dividing the monthly per-user value by 

four and multiplying it by your project's total licensed seats, including free-trial seats. Any user in your edition can draw from this shared weekly pool. Unused quota doesn't roll over to the next week. 

#### Claude pricing

Claude models are available on the Gemini Enterprise app only with pay-as-you-go usage. Ensure that you have turned on **Pay-as-you-go usage above quota** for all editions where you want to enable Claude models. 

Pay-as-you-go charges for Claude models apply as defined in the following table: 

**Note:** Claude model pricing and discounts in the Gemini Enterprise app are distinct from pricing procured through Google Cloud Marketplace. 

|Global<br> (#global)<br>US Multi-Regi|on (US)…<br>EU|Multi-Region (EU)…||
|---|---|---|---|
|Model|Type|Model price (/1M tokens)<br>=< 200K input tokens|Model price (/1M tokens)<br>> 200K input tokens|
||Input|$4.00|$4.00|
||Output|$20.00|$20.00|
|Claude Opus 5.5|5m Cache Write|$5.00|$5.00|
||1h Cache Write|$8.00|$8.00|
||Cache Hit|$0.20|$0.20|
||Input|$2.00|$2.00|
||Output|$10.00|$10.00|
|Claude Sonnet 5.5|5m Cache Write|$2.50|$2.50|
||1h Cache Write|$4.00|$4.00|
||Cache Hit|$0.20|$0.20|

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-15 UTC. 



## Administrator guide

URL: https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin

The guides in this section helps administrators and IT operators** set up and manage Gemini Enterprise. It describes the start-up tasks and prerequisites required to configure Cloud projects, manage user licensing, set up identity authentication, and deploy enterprise security controls. 

##### Project and licensing setup

Set up your Google Cloud project, enable billing, and manage user subscriptions: 

#### Create a Google Cloud project

#### Enable or verify Cloud billing

Create or select a Verify billing is active Google Cloud project on your Cloud project to host your to enable enterprise apps, data subscription tiers and stores, and thirdpay-as-you-go party data platform capabilities. connectors. 

Create project (/resource-m 

Verify billing (/billing/docs/h 

#### Purchase a product subscription

Subscribe to Gemini Enterprise edition licenses through the Google Cloud console. 

View licenses (/gemini/ente 

##### Access control and permissions

Assign platform licenses and configure Identity and Access Management (IAM) roles: 

#### Assign licenses to platform users

Distribute and assign licenses to employees manually by email or configure automatic seat assignment upon initial sign-in. 

#### Grant administrator IAM access

Grant the Gemini Enterprise Admin role to administrators managing platform settings, security policies, and data stores. 

#### Grant end-user IAM access

Grant the Gemini Enterprise User role to licensed employees accessing search, chat, and custom AI assistant features. 

##### Identity and data security

Configure single sign-on, authentication, and enterprise data source access controls: 

#### Configure your identity provider

Connect your identity provider to manage user authentication, sync group memberships, and enforce permissionsaware search access. 

Configure identity provider 

#### Connect enterprise data sources

Create Google data stores and thirdparty data stores, such as Jira, Microsoft SharePoint, and many more. 

Create Google data stores ( Connect third-party data (/g 

#### Enable Model Armor safety controls

Configure Model Armor templates to sanitize prompt inputs, redact sensitive data, and enforce enterprise safety policies. 

Enable Model Armor (/gemi 

##### Mobile app deployment

Configure access controls, device policies, and mobile app onboarding: 

Set up and configure the mobile app Enable and configure the mobile app for iOS and Android devices, including single sign-on authentication and mobile enterprise access. 

Configure the mobile app (/ 

Last updated 2026-10-14 UTC.
