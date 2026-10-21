# Gemini Enterprise: connectors and data stores / Best practices for Data Cloud connectors that use conversational analytics to Secure Data Cloud connectors
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 163-198, extracted 2026-10-18

Contains:
- Best practices for Data Cloud connectors that use conversational analytics (pages 163-169) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-best-practices
- Connect to BigQuery (pages 170-174) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery
- Connect to Spanner (pages 175-179) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner
- Connect to Cloud SQL (pages 180-185) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql
- Connect to AlloyDB for PostgreSQL (pages 186-190) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb
- Connect to Knowledge Catalog (pages 191-195) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog
- Secure Data Cloud connectors (pages 196-198) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security

## Best practices for Data Cloud connectors that use conversational analytics

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-best-practices

When you connect Data Cloud connectors 

(/gemini/enterprise/docs/connectors/connect-data-cloud) in federated query mode, Gemini Enterprise uses the Model Context Protocol (MCP) to query your data sources in place. While MCP tool definitions give the assistant the mechanics to execute SQL, answering natural-language business questions with high accuracy and low latency requires two additional layers of guidance: 

- **A default analytical harness** : Engine-specific procedural skills that teach the Gemini Enterprise assistant how to plan queries, resolve filter values, use advanced analytical functions, and handle errors like an expert data analyst. 

- **Organizational context** : Domain-specific skills, custom instructions, and Knowledge Catalog (/gemini/enterprise/docs/connectors/connect-knowledge-catalog) metadata that map your company's business vocabulary, KPI definitions, and governance guardrails to the right underlying tables and models. 

This document describes how Data Cloud connectors use built-in analytical skills managed by Google, and how you can use Knowledge Catalog 

(/gemini/enterprise/docs/connectors/connect-knowledge-catalog), custom skills (/gemini/enterprise/docs/skills), and assistant instructions to provide organizational context for your data. 

### Understand the default analytical harness

Out-of-the-box MCP tools expose low-level operations (such as listing tables or running a SQL string), which by themselves are often insufficient for complex multistep data analysis. First-party Data Cloud connectors bridge this gap by bundling a **default analytical harness** —a set of built-in, Google-managed skills derived from the conversational analytics agent harness. These built-in skills automatically handle core analytical tasks—such as generating read-only `SELECT` queries, recovering from SQL compiler errors, and invoking built-in BigQuery AI, ML, and 

graph functions (such as `AI.FORECAST` , `AI.DETECT_ANOMALIES` , `AI.CLASSIFY` , `AI.AGG` , `AI.GENERATE` , and `GRAPH_TABLE` ) —without requiring any configuration or action from you. 

Because Google controls these built-in connector skills, you can't modify or add context to the connectors directly. Instead, you can resolve common query execution, search latency, and metric accuracy problems by configuring connector settings, curating metadata in Knowledge Catalog 

(/gemini/enterprise/docs/connectors/connect-knowledge-catalog), or creating and using custom skills (/gemini/enterprise/docs/skills) in your Gemini Enterprise app. 

The following table describes common problems that you might encounter when using Data Cloud connectors and options to resolve them: 

|Problem|Options to resolve|
|---|---|
|Ensuring that<br>all BigQuery<br>queries run in<br>a single<br>project|Configure the Billing Project ID (under Advanced options) when you<br>create the<br>BigQuery data store<br>(/gemini/enterprise/docs/connectors/connect-bigquery#create-data-store).<br>Setting a billing project ensures that all BigQuery query jobs executed through<br>the connector run and are billed in that designated Google Cloud project.|
|Reducing<br>search<br>latency or<br>prioritizing<br>specific data|Use one or both of the following options to narrow where the agent searches and<br>queries data:<br>Create a custom skill:<br>Create and share a skill(/gemini/enterprise/docs/skills)<br>in your Gemini Enterprise app that guides the agent to only search for or<br>query data in specific Google Cloud projects, datasets, or tables. For example,<br>include the following instructions in your skill:<br>_"When answering questions about sales, revenue, or customer activity, only_<br>_search for metadata and run SQL queries against tables in the_`analytics-`<br>`prod.sales_mart`_dataset. Don't scan staging, sandbox, or archive datasets."_<br>Create a Knowledge Catalog data product: Curate high-priority tables into a<br>Knowledge Catalog data product<br>(/knowledge-catalog/docs/data-products-overview) (see<br>Create data products<br>(/knowledge-catalog/docs/create-data-products)) so the agent can discover<br>authoritative assets directly.|

|Problem<br>|Options to resolve|
|---|---|
|Agent using<br>the wrong<br>i|Use one or more of the following options to standardize definitions and join logic:<br>Create custom skills:<br>Create and share custom skills<br>(/gemini/enterprise/docs/skills) (and<br>manage shared skills<br>(/gemini/enterprise/docs/manage-skills)) in your Gemini Enterprise app that<br>tell the agent how to define and calculate your metrics (see<br>Choose where to<br>define business metrics: Custom skills versus Knowledge Catalog<br>(#organization-wide-skills) for an example).|
|definition of a<br>metric or<br>joining on<br>incorrect keys|Curate glossaries and golden queries in Knowledge Catalog: Ensure that<br>metric definitions, business glossaries, and pre-verified sample queries<br>(golden queries) are curated and surfaced in Knowledge Catalog. Golden<br>queries provide certified SQL join syntax that helps prevent the agent from<br>hallucinating table joins on complex schemas. For best practices on<br>structuring metadata for AI agents, see<br>Establish foundational data context<br>with Knowledge Catalog<br>(/knowledge-catalog/docs/establish-foundational-data-context) and<br>Manage<br>glossaries on Knowledge Catalog<br>(/knowledge-catalog/docs/manage-glossaries).|

To compare the advantages of using Knowledge Catalog versus custom skills, see Choose where to define business metrics: Custom skills versus Knowledge Catalog (#organization-wide-skills). For step-by-step instructions on creating and enabling skills in your app, see Create and manage skills (/gemini/enterprise/docs/skills) and Manage skills (/gemini/enterprise/docs/manage-skills). 

### Provide organizational context with skills and Knowledge Catalog

Because Data Cloud connectors are not restricted to a single dataset or table— they can access all resources in the connected data source that the authenticated user has permission to query—the assistant needs organizational context to know which assets are authoritative and how your business calculates key metrics. 

Use a layered approach that combines **Knowledge Catalog** , **organization-wide custom skills** , and **user personalization** : 

1. Ground data discovery with Knowledge Catalog 

When you connect a BigQuery or database connector in federated query mode, Knowledge Catalog (/gemini/enterprise/docs/connectors/connect-knowledge-catalog) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app. Rather than making sequential exploratory calls across raw database schemas, the agent uses Knowledge Catalog tools to search for data that the user has access to and look up rich metadata context in a single workflow. 

If your organization curates metadata in third-party catalogs (such as DataHub) or internal documentation wikis, sync those descriptions into Knowledge Catalog or capture essential business rules in organization-wide custom skills so the agent can discover them. 

2. Choose where to define business metrics: Custom skills versus Knowledge Catalog 

To codify organization-specific analytical rules and standardize business metric definitions and SQL formulas across conversations, you can either: 

- Create, upload, and share custom skills (/gemini/enterprise/docs/skills) (and manage shared skills (/gemini/enterprise/docs/manage-skills)) directly in Gemini Enterprise. 

- Work with your data stewards to curate enterprise metric definitions, business glossaries, and pre-verified example queries in Knowledge Catalog (/knowledge-catalog/docs/establish-foundational-data-context) (see Manage glossaries on Knowledge Catalog (/knowledge-catalog/docs/manage-glossaries) and Data products overview (/knowledge-catalog/docs/data-products-overview)). 

Defining exact calculation logic and filter rules for company KPIs ensures that the assistant doesn't have to guess. For example, you can define that **"Active Customer"** strictly means an account in `analytics_prod.crm.user_events_log` with more than 10 platform logins in the past 30 days ( `event_type = 'LOGIN'` and `is_test_account = FALSE` ), or that **"Net Contribution Margin"** must exclude promotional giveaways ( `order_type != 'PROMO'` ) and inventory shrinkage ( `status != 'SHRINKAGE'` ). 

When choosing whether to implement metric definitions in custom skills within Gemini Enterprise or in Knowledge Catalog, consider the following trade-offs: 

**Knowledge Catalog** : 

**Advantages** : 

- Enforces Identity and Access Management (IAM) access controls so users and agents only discover metadata and definitions that they have permission to view. 

- Can be reused across other agent harnesses, tools, and platforms outside of Gemini Enterprise (such as BigQuery Studio and MCP clients). 

- Centrally maintained by data governance teams without requiring individual app users to enable a skill. 

**Disadvantages** : 

- Provides descriptive metadata context and sample queries rather than strict procedural instructions, so the agent might need additional prompting for complex, multi-step calculation flows. 

**Organization-wide custom skills in Gemini Enterprise** : 

- **Advantages** : 

- Provides specific, prescriptive procedural instructions and exact SQL formulas that the agent adheres to deterministically within the app. 

- Can be rapidly created and updated by Gemini Enterprise app administrators without modifying corporate catalog resources. 

**Disadvantages** : 

- Must be shared with users (/gemini/enterprise/docs/manage-skills) and enabled in Gemini Enterprise, and applies only within Gemini Enterprise rather than across other harnesses or platforms. 

3. Tailor analysis with user skills and personalization 

Individual analysts and business users can layer personal context on top of organization-wide skills: 

**User-created skills** : End users can create personal skills (/gemini/enterprise/docs/skills) for recurring analytical tasks or team-specific defaults—for example, a skill stating that whenever the user asks for "weekly product performance," the assistant should automatically filter for their product line, exclude QA traffic, and group results by fiscal week. 

**Gemini Enterprise memory and personalization** : When personalization (/gemini/enterprise/docs/configure-personalization) is enabled, the assistant can retain user-specific preferences and clarifications across sessions, reducing repeated disambiguation prompts over time. 

### Choose where to configure each type of context

Because Google controls the built-in skills attached to Data Cloud connectors, you can't add custom context directly to a connector. Instead, use the following table to decide where to configure your analytical rules and business context: 

|Context layer|Managed by|Best used for|Example|
|---|---|---|---|
|Knowledge Catalog<br>(/gemini/enterprise/docs/connectors/connect-<br>knowledge-catalog)<br>metadata|Data stewards<br>and catalog<br>administrators|Dynamic asset<br>discovery across<br>large data<br>estates, table<br>and column<br>descriptions,<br>data quality<br>signals, dataset<br>glossaries, and<br>verified sample<br>SQL queries.|<br>Curating<br>certified Data<br>Products and<br>business<br>glossary terms<br>in`analytics_`<br>`prod`so the<br>agent can<br>discover<br>authoritative<br>tables and<br>metric<br>definitions.|

|Context layer|Managed by|Best used for|Example|
|---|---|---|---|
||Gemini<br>Enterprise<br>administrators|Deterministic<br>project and<br>dataset scoping,|Restricting<br>queries to<br>specific|
|Organization-wide custom skills<br>(/gemini/enterprise/docs/skills) and<br>assistant<br>instructions<br>(/gemini/enterprise/docs/configure-assistant)|and data<br>operators|company-wide<br>KPI definitions,<br>disambiguation<br>rules, and<br>response<br>conventions.|production<br>datasets;<br>defining the<br>exact SQL<br>calculation for<br>"Weighted Net<br>ARR".|
||Individual end<br>users and<br>analysts|Role-specific<br>default filters,<br>preferred metric|Automatically<br>applying EMEA<br>region and|
|User skills and<br>personalization<br>(/gemini/enterprise/docs/configure-<br>personalization)||layouts, and<br>recurring team<br>workflows.|active QA<br>filters when a<br>user asks for<br>"monthly<br>pipeline<br>metrics".|

### What's next

- Learn how to create and manage skills (/gemini/enterprise/docs/skills) and manage shared skills (/gemini/enterprise/docs/manage-skills) in Gemini Enterprise. 

- Review Data Cloud connectors overview 

- (/gemini/enterprise/docs/connectors/connect-data-cloud) and Secure Data Cloud connectors (/gemini/enterprise/docs/connectors/data-cloud-security). 

Last updated 2026-10-14 UTC. 



## Connect to BigQuery

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-bigquery

This document describes how to create a data store (/gemini/enterprise/docs/concepts) that connects to BigQuery data. You can link this data store to a Gemini Enterprise app to allow the agents to analyze your data. 

To connect to BigQuery data using a Gemini Enterprise data store, you can use one of the following modes: 

**Federated query (recommended)** [Preview 

(https://cloud.google.com/products#product-launch-stages)]: Connect to BigQuery data in place without incurring egress costs for copying and moving the data. Federated query sends your query directly to BigQuery across all datasets and tables that your identity has Identity and Access Management (IAM) permission to access, which is more efficient for analytical queries. Because queries run using your credentials, BigQuery IAM permissions, including rowlevel security (/bigquery/docs/row-level-security-intro), remain intact. When you use federated query mode, Knowledge Catalog 

(/gemini/enterprise/docs/connectors/connect-knowledge-catalog) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app to give the agent tools to search for data that the user has access to and look up context. 

- **Data ingestion** : Copy data from a specific BigQuery table to the Gemini Enterprise data store. Data must be refreshed to reflect changes in the BigQuery table. This mode incurs egress costs for moving data to a new location, and existing IAM permissions aren't replicated into the data store. 

### Before you begin

To create a BigQuery data store in Gemini Enterprise, you must have the Gemini Enterprise Admin 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) or Discovery Engine Admin (/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) 

( `roles/discoveryengine.admin` ) role. For more information, see Grant permissions to admins (/gemini/enterprise/docs/access-control#grant-permissions-to-admins). 

If your project is protected by a VPC Service Controls perimeter or has organization policy enforcement enabled, ensure that your organization policy allows the connector: 

Add `bigquery_mcp` to the `allowedDataSources` parameter in the `discoveryengine.managed.allowedDataSources` managed constraint ( **Restrict allowed data sources for data connectors** ). For more information, see Overview of managed policy constraints 

(/gemini/enterprise/docs/connectors/managed-policy-constraints-overview) and Configure allowed data sources 

(/gemini/enterprise/docs/connectors/configure-allowed-data-sources). 

In addition, configure the required BigQuery IAM permissions for the connector mode (#connector-mode) that you plan to use: 

Federated queryData ingestion… (#federated-query) 

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions 

(https://cloud.google.com/products/#product-launch-stages). 

Federated query (#federated-query) mode uses the BigQuery MCP server (/bigquery/docs/use-bigquery-mcp). Because different MCP tools (/bigquery/docs/reference/mcp) (actions (#actions)) require different permissions, the required IAM permissions depend on which tools you use. For more information, see Required roles (/bigquery/docs/use-bigquery-mcp#required-roles) in the BigQuery MCP documentation. 

The following are the most commonly applied IAM roles for users who query or perform actions through the connector: 

BigQuery Job User ( `roles/bigquery.jobUser` ) 

(/bigquery/docs/access-control#bigquery.jobUser) on the BigQuery Google 

Cloud project where the query executes (compute or billing project), to give users the ability to run query jobs. 

BigQuery Data Viewer ( `roles/bigquery.dataViewer` ) 

(/bigquery/docs/access-control#bigquery.dataViewer) on the BigQuery Google Cloud project where the data is stored (storage project), to give users the ability to access data in a query or through BigQuery metadata tools such as `get_table_info` (/bigquery/docs/reference/mcp/tools_list/get_table_info) . If write actions (#actions) are enabled, grant BigQuery Data Editor 

( `roles/bigquery.dataEditor` ) 

(/bigquery/docs/access-control#bigquery.dataEditor) instead. 

MCP Tool User ( `roles/mcp.toolUser` ) 

(/iam/docs/roles-permissions/mcp#mcp.toolUser) on both the BigQuery storage Google Cloud project and compute Google Cloud project. 

### Create a BigQuery data store

To create a data store that connects data from BigQuery to Gemini Enterprise, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data stores** page. 

3. Click **Create data store** . 

4. On the **Source** page, choose a data source for your data store. Search for "BigQuery" in the **Select a data source** search field, or find BigQuery in the list of **First-party data sources** . Select **Add data source** . 

5. On the **Data** page, select the connector mode for how to connect to your data. Select from the following tabs for further instructions based on the mode that you have chosen. 

Federated queryData ingestion… (#federated-query) 

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

   - a. Select **Federated query (recommended)** . 

   - b. Optionally, under **Advanced options** , specify the Google Cloud billing project for your data store's query execution by typing the project ID into the **Billing Project ID** field. If you leave this field empty, queries will prompt the user for a billing project or rely on custom instructions. 

   - c. Click **Continue** . 

   - d. On the **Actions** page, select the BigQuery actions that you want to enable for your data store. You can edit these settings later. Click **Continue** . 

6. On the **Configuration** page, configure your data store settings. 

   - **Location of your data connector** : Choose a region for where to store the metadata of your data store. You cannot change the location after the data store is created. For important information about multi-regions, see Gemini Enterprise locations (/gemini/enterprise/docs/locations). 

   - **Your data connector name** : In the **Data connector name** field, enter a name for your data connector. You cannot change the name after the data connector is created. Entering a name generates a unique ID for your data connector. Optionally, in the **Tag (optional)** field, enter a tag for your data connector, which serves as a stable identifier for the connector across all versions. 

   - **Sensitive data protection policy** : Select a sensitive data protection policy (/gemini/enterprise/docs/protect-sensitive-data) for your data store. The format should follow: 

`projects/{project}/locations/{location}/contentPolicies/{policy}` . You can edit this setting later. 

7. Click **Create** . 

Now you're ready to attach your data store to a Gemini Enterprise app. In federated query mode, queries incur BigQuery compute costs when users run queries through the attached app; in data ingestion mode, importing data incurs BigQuery and Gemini Enterprise indexing costs even before the data store is attached to an app. To learn more about these charges, see Gemini Enterprise pricing (https://cloud.google.com/generative-ai-app-builder/pricing). 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps on Create a Gemini Enterprise app 

- (/gemini/enterprise/docs/create-app). 

- Learn how Knowledge Catalog works with Data Cloud connectors (/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (automatically enabled when you use federated query mode) to help the agent search for data that the user has access to and look up organizational context. 

- To build a scoped agent with verified queries in BigQuery, see Publish a BigQuery data agent to Gemini Enterprise 

- (/bigquery/docs/create-data-agents#publish-agent-gemini-enterprise). 

Last updated 2026-10-14 UTC. 



## Connect to Spanner

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-spanner

This document describes how to create a data store (/gemini/enterprise/docs/concepts) that connects to Spanner data. You can link this data store to a Gemini Enterprise app to allow the agents to analyze your data. 

To connect to Spanner data using a Gemini Enterprise data store, you can use one of the following modes: 

**Federated query (recommended)** [Preview 

(https://cloud.google.com/products#product-launch-stages)]: Connect to Spanner data in place without incurring egress costs for copying and moving the data. Federated query sends your query directly to Spanner across all databases and tables that your identity has Identity and Access Management (IAM) permission to access, which is more efficient for analytical queries. When you use federated query mode, Knowledge Catalog 

(/gemini/enterprise/docs/connectors/connect-knowledge-catalog) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app to give the agent tools to search for data that the user has access to and look up context. 

**Caution: High-accuracy database queries:** Federated query mode provides broad access across all databases and tables accessible by the user, but query accuracy can vary on complex transactional schemas. For workloads requiring high accuracy, deterministic table scoping, and verified queries (golden SQL), create a scoped data agent in Spanner 

(/gemini/data-agents/conversational-analytics/spanner/create-data-agents#publishagent-gemini-enterprise) and publish it to Gemini Enterprise. 

**Data ingestion** : Copy data from a specific Spanner table to the Gemini Enterprise data store. Data must be manually refreshed to reflect changes in the Spanner table. This mode incurs egress costs for moving data to a new location, and existing IAM permissions aren't replicated into the data store. 

### Before you begin

To create a Spanner data store in Gemini Enterprise, you must have the Gemini Enterprise Admin 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) or Discovery Engine Admin 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) 

( `roles/discoveryengine.admin` ) role. For more information, see Grant permissions to admins (/gemini/enterprise/docs/access-control#grant-permissions-to-admins). 

If your project is protected by a VPC Service Controls perimeter or has organization policy enforcement enabled, ensure that your organization policy allows the connector: 

Add `spanner` to the `allowedDataSources` parameter in the `discoveryengine.managed.allowedDataSources` managed constraint ( **Restrict allowed data sources for data connectors** ). For more information, see Overview of managed policy constraints 

(/gemini/enterprise/docs/connectors/managed-policy-constraints-overview) and Configure allowed data sources 

(/gemini/enterprise/docs/connectors/configure-allowed-data-sources). 

In addition, configure the required Spanner IAM permissions for the connector mode (#connector-mode) that you plan to use: 

Federated queryData ingestion… (#federated-query) 

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

To connect to Spanner using federated query (#federated-query) mode, grant the following IAM roles to users who query or perform actions through the connector in the Google Cloud project that contains your Spanner database: 

**Database access** : 

- Cloud Spanner Database Reader ( `roles/spanner.databaseReader` ) 

(/spanner/docs/iam#roles) for read-only queries and tools. 

Cloud Spanner Database User ( `roles/spanner.databaseUser` ) 

(/spanner/docs/iam#roles) or Cloud Spanner Database Admin 

- ( `roles/spanner.databaseAdmin` ) (/spanner/docs/iam#roles) if write or DDL actions (#actions) are enabled. 

**MCP tool access** : 

MCP Tool User ( `roles/mcp.toolUser` ) 

(/iam/docs/roles-permissions/mcp#mcp.toolUser) in the project where the Spanner database lives to invoke Spanner MCP tools. 

### Create a Spanner data store

To create a data store that connects data from Spanner to Gemini Enterprise, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data stores** page. 

3. Click **Create data store** . 

4. On the **Source** page, choose a data source for your data store. Search for "Spanner" in the **Select a data source** search field, or find Spanner in the list of **First-party data sources** . Select **Add data source** . 

5. On the **Data** page, select the connector mode for how to connect to your data. Select from the following tabs for further instructions based on the mode that you have chosen. 

Federated queryData ingestion… (#federated-query) 

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

   - a. Select **Federated query (recommended)** . Click **Continue** . 

   - b. On the **Actions** page, select the Spanner actions that you want to enable for your data store. You can edit these settings later. Click **Continue** . 

6. On the **Configuration** page, configure your data store settings. 

   - **Location of your data connector** : Choose a region for where to store the metadata of your data store. You cannot change the location after the data store is created. For important information about multi-regions, see Gemini Enterprise locations (/gemini/enterprise/docs/locations). 

   - **Your data connector name** : In the **Data connector name** field, enter a name for your data connector. You cannot change the name after the data connector is created. Entering a name generates a unique ID for your data connector. Optionally, in the **Tag (optional)** field, enter a tag for your data connector, which serves as a stable identifier for the connector across all versions. 

   - **Sensitive data protection policy** : Select a sensitive data protection policy (/gemini/enterprise/docs/protect-sensitive-data) for your data store. The format should follow: 

`projects/{project}/locations/{location}/contentPolicies/{policy}` . You can edit this setting later. 

7. Click **Create** . 

Now you're ready to attach your data store to a Gemini Enterprise app. In federated query mode, queries incur Spanner usage costs when users run queries through the attached app; in data ingestion mode, importing data incurs Spanner and Gemini Enterprise indexing costs even before the data store is attached to an app. To learn more about these charges, see Gemini Enterprise pricing (https://cloud.google.com/generative-ai-app-builder/pricing). 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps on Create a Gemini Enterprise app 

- (/gemini/enterprise/docs/create-app). 

- Learn how Knowledge Catalog works with Data Cloud connectors (/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (automatically enabled when you use federated query mode) to help the agent search for data that the user has access to and look up organizational context. 

- To build a high-accuracy, scoped agent with verified queries, see Publish a Spanner data agent 

- (/gemini/data-agents/conversational-analytics/spanner/create-data-agents#publishagent-gemini-enterprise) 

to Gemini Enterprise. 

Last updated 2026-10-14 UTC. 



## Connect to Cloud SQL

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-sql

This document describes how to create a data store (/gemini/enterprise/docs/concepts) that connects to Cloud SQL data. You can link this data store to a Gemini Enterprise app to allow the agents to analyze your data. 

To connect to Cloud SQL data using a Gemini Enterprise data store, you can use one of the following modes: 

**Federated query (recommended)** [Preview 

(https://cloud.google.com/products#product-launch-stages)]: Connect to Cloud SQL data in place without incurring egress costs for copying and moving the data. Federated query sends your query directly to Cloud SQL across all instances, databases, and tables that your identity has Identity and Access Management (IAM) permission to access, which is more efficient for analytical queries. When you use federated query mode, Knowledge Catalog 

(/gemini/enterprise/docs/connectors/connect-knowledge-catalog) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app to give the agent tools to search for data that the user has access to and look up context. 

**Caution: High-accuracy database queries:** Federated query mode provides broad access across all instances and databases accessible by the user, but query accuracy can vary on complex transactional schemas. For workloads requiring high accuracy, deterministic table scoping, and verified queries (golden SQL), create a scoped data agent in Cloud SQL for MySQL 

(/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents#publishagent-gemini-enterprise) or Cloud SQL for PostgreSQL 

(/gemini/data-agents/conversational-analytics/sql-postgres/create-dataagents#publish-agent-gemini-enterprise) and publish it to Gemini Enterprise. 

**Data ingestion** : Copy data from a specific Cloud SQL table to the Gemini Enterprise data store. Data must be manually refreshed to reflect changes in the Cloud SQL table. This mode incurs egress costs for moving data to a new location, and existing IAM permissions aren't replicated into the data store. 

### Before you begin

To create a Cloud SQL data store in Gemini Enterprise, you must have the Gemini Enterprise Admin 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) ( `roles/discoveryengine.agentspaceAdmin` ) or Discovery Engine Admin 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) 

( `roles/discoveryengine.admin` ) role. For more information, see Grant permissions to admins (/gemini/enterprise/docs/access-control#grant-permissions-to-admins). 

If your project is protected by a VPC Service Controls perimeter or has organization policy enforcement enabled, ensure that your organization policy allows the connector: 

Add `cloudsql` to the `allowedDataSources` parameter in the `discoveryengine.managed.allowedDataSources` managed constraint ( **Restrict allowed data sources for data connectors** ). For more information, see Overview of managed policy constraints 

(/gemini/enterprise/docs/connectors/managed-policy-constraints-overview) and Configure allowed data sources 

(/gemini/enterprise/docs/connectors/configure-allowed-data-sources). 

In addition, complete the prerequisites and configure the required Cloud SQL IAM permissions for the connector mode (#connector-mode) that you plan to use: 

Federated queryData ingestion… (#federated-query) 

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

To connect to Cloud SQL using federated query (#federated-query) mode, complete the following prerequisites in the Google Cloud project that 

contains your Cloud SQL instance: 

1. **Enable the Data API on your Cloud SQL instance** : 

```
gcloud sql instances patch <var>INSTANCE_NAME</var> \
```

- `--project=<var>PROJECT_ID</var> \` 

```
   --data-api-access=ALLOW_DATA_API
```

2. **Grant IAM permissions** : Grant the following IAM roles in the Google Cloud project that contains your Cloud SQL instance to users who query or perform actions through the connector: 

**Instance and database access** : 

Cloud SQL Viewer ( `roles/cloudsql.viewer` ) 

- (/sql/docs/postgres/iam-roles#roles) and Cloud SQL Client 

- ( `roles/cloudsql.client` ) (/sql/docs/postgres/iam-roles#roles) (or Cloud SQL Instance User ( `roles/cloudsql.instanceUser` ) 

- (/sql/docs/postgres/iam-roles#roles) with IAM database authentication) for read-only queries and tools. 

Cloud SQL Editor ( `roles/cloudsql.editor` ) 

- (/sql/docs/postgres/iam-roles#roles) or Cloud SQL Admin 

- ( `roles/cloudsql.admin` ) (/sql/docs/postgres/iam-roles#roles) if write or administrative actions (#actions) are enabled. 

**MCP tool access** : 

MCP Tool User ( `roles/mcp.toolUser` ) 

(/iam/docs/roles-permissions/mcp#mcp.toolUser) permission in the project where the Cloud SQL instance lives to invoke MCP tools. 

### Create a Cloud SQL data store

To create a data store that connects data from Cloud SQL to Gemini Enterprise, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data stores** page. 

3. Click **Create data store** . 

4. On the **Source** page, choose a data source for your data store. Search for "Cloud SQL" in the **Select a data source** search field, or find Cloud SQL in the list of **First-party data sources** . Select **Add data source** . 

5. On the **Data** page, select the connector mode for how to connect to your data. Select from the following tabs for further instructions based on the mode that you have chosen. 

Federated queryData ingestion… (#federated-query) 

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

   - a. Select **Federated query (recommended)** . Click **Continue** . 

   - b. On the **Actions** page, select the Cloud SQL actions that you want to enable for your data store. You can edit these settings later. Click **Continue** . 

6. On the **Configuration** page, configure your data store settings. 

**Location of your data connector** : Choose a region for where to store the metadata of your data store. You cannot change the location after the data store is created. For important information about multi-regions, see Gemini Enterprise locations (/gemini/enterprise/docs/locations). 

- **Your data connector name** : In the **Data connector name** field, enter a name for your data connector. You cannot change the name after the data connector is created. Entering a name generates a unique ID for your data connector. Optionally, in the **Tag (optional)** field, enter a tag for your data connector, which serves as a stable identifier for the connector across all versions. 

- **Sensitive data protection policy** : Select a sensitive data protection policy (/gemini/enterprise/docs/protect-sensitive-data) for your data store. The format should follow: 

`projects/{project}/locations/{location}/contentPolicies/{policy}` . You can edit this setting later. 

7. Click **Create** . 

Now you're ready to attach your data store to a Gemini Enterprise app. In federated query mode, queries incur Cloud SQL usage costs when users run queries through the attached app; in data ingestion mode, importing data incurs Cloud SQL, Cloud Storage, and Gemini Enterprise indexing costs even before the data store is attached to an app. To learn more about these charges, see Gemini Enterprise pricing (https://cloud.google.com/generative-ai-app-builder/pricing). 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps on Create a Gemini Enterprise app 

- (/gemini/enterprise/docs/create-app). 

- Learn how Knowledge Catalog works with Data Cloud connectors (/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (automatically enabled when you use federated query mode) to help the agent search for data that the user has access to and look up organizational context. 

- To build a high-accuracy, scoped agent with verified queries, see Publish a Cloud SQL for MySQL data agent 

- (/gemini/data-agents/conversational-analytics/sql-mysql/create-data-agents#publishagent-gemini-enterprise) 

or Cloud SQL for PostgreSQL data agent 

(/gemini/data-agents/conversational-analytics/sql-postgres/create-data-agents#publishagent-gemini-enterprise) 

to Gemini Enterprise. 

Last updated 2026-10-14 UTC. 



## Connect to AlloyDB for PostgreSQL

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-alloydb

This document describes how to create a data store (/gemini/enterprise/docs/concepts) that connects to AlloyDB for PostgreSQL data. You can link this data store to a Gemini Enterprise app to allow the agents to analyze your data. 

To connect to AlloyDB for PostgreSQL data using a Gemini Enterprise data store, you can use one of the following modes: 

**Federated query (recommended)** [Preview 

(https://cloud.google.com/products#product-launch-stages)]: Connect to AlloyDB for PostgreSQL data in place without incurring egress costs for copying and moving the data. Federated query sends your query directly to AlloyDB for PostgreSQL across all clusters, databases, and tables that your identity has Identity and Access Management (IAM) permission to access, which is more efficient for analytical queries. When you use federated query mode, Knowledge Catalog (/gemini/enterprise/docs/connectors/connect-knowledge-catalog) is automatically enabled on the **Assistant** tab of your Gemini Enterprise app to give the agent tools to search for data that the user has access to and look up context. 

**Caution: High-accuracy database queries:** Federated query mode provides broad access across all clusters and databases accessible by the user, but query accuracy can vary on complex transactional schemas. For workloads requiring high accuracy, deterministic table scoping, and verified queries (golden SQL), create a scoped data agent in AlloyDB for PostgreSQL 

(/gemini/data-agents/conversational-analytics/alloydb/create-data-agents#publishagent-gemini-enterprise) 

and publish it to Gemini Enterprise. 

**Data ingestion** : Copy data from a specific AlloyDB for PostgreSQL table to the Gemini Enterprise data store. Data must be manually refreshed to reflect changes in the AlloyDB for PostgreSQL table. This mode incurs egress costs for moving data to a new location, and existing IAM permissions aren't replicated into the data store. 

### Before you begin

To create an AlloyDB for PostgreSQL data store in Gemini Enterprise, you must have the Gemini Enterprise Admin 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) 

( `roles/discoveryengine.agentspaceAdmin` ) or Discovery Engine Admin 

(/iam/docs/roles-permissions/discoveryengine#discoveryengine.admin) 

( `roles/discoveryengine.admin` ) role. For more information, see Grant permissions to admins (/gemini/enterprise/docs/access-control#grant-permissions-to-admins). 

If your project is protected by a VPC Service Controls perimeter or has organization policy enforcement enabled, ensure that your organization policy allows the connector: 

Add `alloydb` to the `allowedDataSources` parameter in the `discoveryengine.managed.allowedDataSources` managed constraint ( **Restrict allowed data sources for data connectors** ). For more information, see Overview of managed policy constraints 

(/gemini/enterprise/docs/connectors/managed-policy-constraints-overview) and Configure allowed data sources 

(/gemini/enterprise/docs/connectors/configure-allowed-data-sources). 

In addition, configure the required AlloyDB for PostgreSQL IAM permissions for the connector mode (#connector-mode) that you plan to use: 

Federated queryData ingestion… (#federated-query) 

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

To connect to AlloyDB for PostgreSQL using federated query (#federated-query) mode, grant the following IAM roles in the Google Cloud project that contains 

your AlloyDB for PostgreSQL cluster to users who query or perform actions through the connector: 

**Cluster and database access** : 

Cloud AlloyDB Viewer ( `roles/alloydb.viewer` ) 

- (/alloydb/docs/reference/iam-roles-permissions#roles) and Cloud AlloyDB Client ( `roles/alloydb.client` ) 

- (/alloydb/docs/reference/iam-roles-permissions#roles) (or Cloud AlloyDB Database User ( `roles/alloydb.databaseUser` ) 

(/alloydb/docs/reference/iam-roles-permissions#roles) with IAM database authentication) for read-only queries and tools. 

Cloud AlloyDB Admin ( `roles/alloydb.admin` ) 

- (/alloydb/docs/reference/iam-roles-permissions#roles) if write or cluster management actions (#actions) (such as creating clusters, 

instances, or backups, or executing SQL writes) are enabled. 

**MCP tool access** : 

MCP Tool User ( `roles/mcp.toolUser` ) 

(/iam/docs/roles-permissions/mcp#mcp.toolUser) permission in the Google Cloud project where the AlloyDB for PostgreSQL cluster lives to invoke MCP tools. 

### Create a AlloyDB for PostgreSQL data store

To create a data store that connects data from AlloyDB for PostgreSQL to Gemini Enterprise, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data stores** page. 

3. Click **Create data store** . 

4. On the **Source** page, choose a data source for your data store. Search for "AlloyDB for PostgreSQL" in the **Select a data source** search field, or find 

AlloyDB for PostgreSQL in the list of **First-party data sources** . Select **Add data source** . 

5. On the **Data** page, select the connector mode for how to connect to your data. Select from the following tabs for further instructions based on the mode that you have chosen. 

Federated queryData ingestion… (#federated-query) 

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

   - a. Select **Federated query (recommended)** . Click **Continue** . 

   - b. On the **Actions** page, select the AlloyDB for PostgreSQL actions that you want to enable for your data store. You can edit these settings later. Click **Continue** . 

6. On the **Configuration** page, configure your data store settings. 

   - **Location of your data connector** : Choose a region for where to store the metadata of your data store. You cannot change the location after the data store is created. For important information about multi-regions, see Gemini Enterprise locations (/gemini/enterprise/docs/locations). 

   - **Your data connector name** : In the **Data connector name** field, enter a name for your data connector. You cannot change the name after the data connector is created. Entering a name generates a unique ID for your data connector. Optionally, in the **Tag (optional)** field, enter a tag for your data connector, which serves as a stable identifier for the connector across all versions. 

   - **Sensitive data protection policy** : Select a sensitive data protection policy (/gemini/enterprise/docs/protect-sensitive-data) for your data store. The 

format should follow: 

`projects/{project}/locations/{location}/contentPolicies/{policy}` . You can edit this setting later. 

7. Click **Create** . 

Now you're ready to attach your data store to a Gemini Enterprise app. In federated query mode, queries incur AlloyDB for PostgreSQL usage costs when users run queries through the attached app; in data ingestion mode, importing data incurs AlloyDB for PostgreSQL and Gemini Enterprise indexing costs even before the data store is attached to an app. To learn more about these charges, see Gemini Enterprise pricing (https://cloud.google.com/generative-ai-app-builder/pricing). 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps on Create a Gemini Enterprise app 

- (/gemini/enterprise/docs/create-app). 

- Learn how Knowledge Catalog works with Data Cloud connectors (/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (automatically enabled when you use federated query mode) to help the agent search for data that the user has access to and look up organizational context. 

- To build a high-accuracy, scoped agent with verified queries, see Publish an AlloyDB for PostgreSQL data agent 

- (/gemini/data-agents/conversational-analytics/alloydb/create-data-agents#publishagent-gemini-enterprise) 

to Gemini Enterprise. 

Last updated 2026-10-14 UTC. 



## Connect to Knowledge Catalog

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-knowledge-catalog

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

This document describes how Gemini Enterprise integrates with Knowledge Catalog to give agents read-only tools to search for data that a user has access to and look up technical and business context. 

You don't need to create a separate data store (/gemini/enterprise/docs/concepts) to connect to Knowledge Catalog. Instead, the Knowledge Catalog integration is **automatically enabled** when you connect a BigQuery 

(/gemini/enterprise/docs/connectors/connect-bigquery#federated-query), Spanner (/gemini/enterprise/docs/connectors/connect-spanner#federated-query), Cloud SQL (/gemini/enterprise/docs/connectors/connect-cloud-sql#federated-query), or AlloyDB for PostgreSQL (/gemini/enterprise/docs/connectors/connect-alloydb#federated-query) data store in **federated query mode** to your Gemini Enterprise app. Rather than appearing as a data store, Knowledge Catalog is a configuration option on the **Assistant** tab of your Gemini Enterprise app. You can also manually turn the integration on or off (#configure-knowledge-catalog) at any time, even outside of the companion Data Cloud connectors. 

### How Knowledge Catalog and Data Cloud connectors work together

In Knowledge Catalog, every cataloged data asset across your Google Cloud environment is stored as a metadata record called an _entry_ . Because Data Cloud connectors in federated query mode have broad access to all resources that an authenticated user can view—rather than being restricted to a single dataset or table—the agent doesn't initially know where the relevant data resides. 

When Knowledge Catalog is enabled for your Gemini Enterprise app—either automatically when you attach a federated Data Cloud connector, or manually on the **Assistant** tab—the integration provides the agent with built-in skills and readonly tools to do the following: 

- **Search for accessible data** : Search across cataloged data assets in Knowledge Catalog that the authenticated user has permission to access. 

- **Look up technical and business context** : Retrieve enriched metadata— including table schemas, column descriptions, business glossary terms, and pre-verified sample queries (golden queries). When paired with a companion Data Cloud connector, the agent uses these golden queries to prevent join hallucinations on complex schemas and passes this context to the connector to generate and run an accurate query. 

#### Example workflow

The following diagram illustrates how Knowledge Catalog and a federated Data Cloud connector work together to answer a user's question: 

In this workflow, Gemini Enterprise completes the following steps: 

1. **User question** : A user asks a natural-language question in Gemini Enterprise: 

```
"How many sales did we have this month for all cold weather products?"
```

2. **Semantic search discovery** : The Gemini Enterprise root agent searches Knowledge Catalog using search terms extracted from the user's question: 

```
["cold weather", "products", "orders", "sales"]
```

3. **Context retrieval** : For the matching entries that the user has access to, the agent looks up enriched context in Knowledge Catalog (derived from technical metadata, usage patterns, business glossaries, and LLM inference): 

```
simpleName: my-project.ecomm.products
type: BigQuery Table
terms: "Cold Weather Products; category IN ('Sweaters', 'Coats &
Jackets')"
```

4. **Query execution** : Using the retrieved table metadata and business definition, the agent formulates and executes a read-only SQL query through the federated BigQuery connector: 

```
-- Execute BigQuery read-only SQL
SELECT COUNT(order_id) FROM `my-project.ecomm.orders`
WHERE product_id IN (
 SELECT id FROM `my-project.ecomm.products`
 WHERE category IN ('Sweaters', 'Coats & Jackets')
);
```

### Before you begin

The Knowledge Catalog integration is **read-only** and uses internal APIs, so you don't need to enable the Dataplex API or grant MCP tool permissions, and users don't need permissions to create or modify resources in Knowledge Catalog. 

Because the integration authenticates requests using **end-user credentials** , the agent can only find and discover data assets that the authenticated user has Identity and Access Management (IAM) permission to view: 

**Separation of metadata and data access with search result trimming** : Knowledge Catalog enforces search result trimming based on the authenticated user's permissions in the underlying data source. If a user lacks read permissions (such as `roles/bigquery.dataViewer` or `roles/bigquery.metadataViewer` ) on a dataset or table, that asset is automatically filtered out of catalog search results and cannot be discovered by the assistant. 

**First-party Google Cloud data sources** : Permissions for first-party data sources—such as BigQuery 

(/gemini/enterprise/docs/connectors/connect-bigquery#bq-prereqs), AlloyDB for PostgreSQL (/gemini/enterprise/docs/connectors/connect-alloydb#alloydb-prereqs), Spanner (/gemini/enterprise/docs/connectors/connect-spanner#spanner-prereqs), and Cloud SQL (/gemini/enterprise/docs/connectors/connect-cloud-sql#cloud-sql-prereqs)— are inherited automatically. For example, granting a user the BigQuery Data Viewer ( `roles/bigquery.dataViewer` ) role gives them access to search and discover the corresponding table and dataset metadata in Knowledge Catalog. 

- **Additional metadata and third-party data sources** : For custom metadata, business glossaries, or third-party data assets added to Knowledge Catalog, ensure that users have the required view permissions in Knowledge Catalog (such as `roles/dataplex.dataDomainEntryReader` or `roles/dataplex.catalogViewer` ) so the agent can discover that data. For more information, see Manage access with IAM 

- (/knowledge-catalog/docs/iam-and-access-control) in the Knowledge Catalog documentation. 

### Enable or disable Knowledge Catalog in your app

When you attach a BigQuery, Spanner, Cloud SQL, or AlloyDB for PostgreSQL data store in **federated query mode** to a Gemini Enterprise app, Knowledge Catalog and its built-in agent skills are automatically enabled for the app. 

You can also manually turn the Knowledge Catalog integration on or off at any time —even outside of the companion Data Cloud connectors (for example, to enable Knowledge Catalog without attaching a Data Cloud connector, or to turn it off while keeping a Data Cloud connector active)—on the **Assistant** tab of your app's **Configurations** page: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** , and then select the **Assistant** tab. 

4. In the **Enable Knowledge Catalog** section, use the toggle to turn the Knowledge Catalog integration on or off. 

5. Click **Save and publish** . 

For more information about assistant settings, see Configure the assistant (/gemini/enterprise/docs/configure-assistant). 

### Next steps

- Connect a Data Cloud data source in federated query mode: 

   - Connect to BigQuery (/gemini/enterprise/docs/connectors/connect-bigquery) 

   - Connect to Spanner (/gemini/enterprise/docs/connectors/connect-spanner) 

   - Connect to Cloud SQL (/gemini/enterprise/docs/connectors/connect-cloud-sql) 

   - Connect to AlloyDB for PostgreSQL 

   - (/gemini/enterprise/docs/connectors/connect-alloydb) 

- Learn about Best practices for Data Cloud connectors that use conversational analytics (/gemini/enterprise/docs/connectors/data-cloud-best-practices). 

Last updated 2026-10-14 UTC. 



## Secure Data Cloud connectors

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/data-cloud-security

This page describes the security and compliance controls supported by Data Cloud connectors (/gemini/enterprise/docs/connectors/connect-data-cloud) in Gemini Enterprise and explains how to configure organization policies when your project is protected by a VPC Service Controls perimeter. 

### Supported security and compliance controls

Data Cloud connectors support the following enterprise security and compliance controls in Gemini Enterprise: 

**Data residency (DRZ)** : When you use federated query mode, your customer data remains where it's already stored and isn't moved. The connector queries your data in place and returns the results to the agent in the location of your Gemini Enterprise app. If write actions are enabled, the agent can also modify data in place within the underlying data source, subject to the user's Identity and Access Management permissions. Gemini Enterprise supports data residency in the `us` and `eu` multi-regions. For more information, see Gemini Enterprise locations (/gemini/enterprise/docs/locations). 

**Customer-managed encryption keys (CMEK)** : When you use federated query mode, your underlying data remains in the connected data source, where you can configure CMEK directly in that service. In Gemini Enterprise, you can use encryption keys managed in Cloud Key Management Service to protect data at rest, including query results returned to the agent and stored in conversations, connector configurations, and end-user credentials. For more information, see Customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

**VPC Service Controls** : You can protect your Gemini Enterprise apps and Data Cloud connectors within a VPC Service Controls service perimeter to help mitigate data exfiltration risks. When VPC Service Controls is enabled, you must also allow the Data Cloud connector IDs in your organization policies as described in Allow Data Cloud connectors in organization policies (#allow-connectors-org-policies). For general perimeter setup instructions, see Use VPC Service Controls (/gemini/enterprise/docs/use-vpc-service-controls). 

### Allow Data Cloud connectors in organization policies

If your project is protected by a VPC Service Controls perimeter, or is explicitly included in the `enforcedProjects` parameter of an organization policy, Gemini Enterprise enforces the Google-managed `constraints/discoveryengine.managed.allowedDataSources` organization policy constraint. This constraint blocks data store creation unless the connector's internal identifier is explicitly listed in the policy's `allowedDataSources` parameter. 

To allow Data Cloud connectors, add the corresponding connector identifier to the `allowedDataSources` parameter: 

- `bigquery_mcp` : Allows the BigQuery federated data connector. 

- `spanner` : Allows the Spanner federated data connector. 

- `cloudsql` : Allows the Cloud SQL federated data connector. 

`alloydb` : Allows the AlloyDB for PostgreSQL federated data connector. 

**Note:** First-party API connectors communicate directly over internal Google APIs, so their endpoints are automatically permitted when the connector is allowed in **`allowedDataSources`** . You don't need to add domain names to the **`discoveryengine.managed.allowedEgressFqdns`** constraint. 

For more information about managed constraints and step-by-step instructions for configuring organization policies in the Google Cloud console, see the following resources: 

- Overview of managed policy constraints 

- (/gemini/enterprise/docs/connectors/managed-policy-constraints-overview) 

- Configure allowed data sources 

- (/gemini/enterprise/docs/connectors/configure-allowed-data-sources) 

- Configure allowed egress FQDNs 

- (/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns) 

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC.
