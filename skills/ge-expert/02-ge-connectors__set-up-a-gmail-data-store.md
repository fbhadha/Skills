# Gemini Enterprise: connectors and data stores / Set up a Gmail data store to Sync people data
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 85-121, extracted 2026-10-18

Contains:
- Set up a Gmail data store (pages 85-89) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail/set-up-data-store
- Configure OAuth for Gmail (pages 90-91) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail/config
- Import from Cloud Storage (pages 92-97) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage
- Sync from Google Groups (pages 98-100) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-groups
- Connect to Google Sites (pages 101-103) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-sites
- Add filters to a Google Sites data store (pages 104-107) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gsites/add-filters-to-gsites-data-store
- Sync people data (pages 108-121) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people

## Set up a Gmail data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail/set-up-data-store

This page describes how to create a data store and connect Gmail to Gemini Enterprise. 

### Before you begin

- Sign in to the Google Cloud console with the same account that you use for the Google Workspace instance that you plan to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Gmail. Personal Google Accounts (consumer accounts ending in `@gmail.com` ) don't have a customer ID and aren't supported. 

- To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider 

- (/gemini/enterprise/docs/configure-identity-provider). 

- **Enable smart features** : In your Google Workspace account, turn on both **Smart features in Google Workspace** and **Smart features in other Google products** . For details, see Turn Google Workspace smart features on or off (https://support.google.com/mail/answer/15604322). 

- **Allowlist the OAuth app (Administrators only)** : The Gmail data store uses a Google-managed OAuth app to access your data. If your organization restricts OAuth app access, your Google Workspace administrator must add this app to your organization's allowlist. For details, see Allowlist the Googlemanaged OAuth app 

- (/gemini/enterprise/docs/connectors/gmail/config#allowlist-oauth-app). 

### Create the Gmail data store

To create the Gmail data store, perform the following steps: 

1. In the Google Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create (/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click + **Create data store** . 

5. In the **Source** , search for **Google Mail** , and click **Select** . 

6. In the **Actions** section, choose the actions from the list to enable them for the Gmail connector. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To manage the list of actions, see Manage actions 

(/gemini/enterprise/docs/manage-actions). 

7. Click **Continue** . 

8. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Select **Google-managed encryption key** or **Cloud KMS key** . If you selected **Cloud KMS key** : 

         - In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

9. Optional: In the **Tag** field, enter a stable identifier for the data store. This identifier is used across different versions of the connector and becomes 

immutable after the data store is created, so choose a value that you don't need to change later. 

10. Optional: In the **Sensitive Data Protection policy** section, attach an existing Sensitive Data Protection 

   - (/sensitive-data-protection/docs/sensitive-data-protection-overview) policy to inspect and de-identify data that Gemini Enterprise retrieves through this data store. If your organization doesn't require a Sensitive Data Protection policy, you can skip this step. 

11. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. When the data store state changes from **Creating** to **Active** , the Gmail connector is ready to be used. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app) and connect it to the Gmail data store (/gemini/enterprise/docs/connect-existing-data-store) before executing the query. 

### Query Execution

This section describes how Gemini Enterprise manages your query and the privacy implications of using the federated data store. 

After you authorize Gmail and send a search query to Gemini Enterprise: 

- Gemini Enterprise sends your search query directly to the Gmail API. 

- Gemini Enterprise blends the results with those from other connected data sources and displays a comprehensive search result. 

### Error messages and troubleshooting

The following table describes common error messages that you might encounter when you work with the Gmail connector, which includes possible HTTP error codes and suggested troubleshooting steps. 

|Error code|Error message|Description|Troubleshooting|
|---|---|---|---|
|403<br>(Permission<br>Denied)|Search by<br>using service<br>account<br>credentials<br>isn't supported<br>for Google<br>Workspace<br>data stores.|<br>The engine<br>being searched<br>has Google<br>Workspace data<br>stores, and the<br>credentials<br>passed are of a<br>service account.<br>Search by using<br>service account<br>credentials on<br>Google<br>Workspace data<br>stores isn't<br>supported.|Call search using user credentials, or remove<br>Google Workspace data stores from the engine.|
|403<br>(Permission<br>Denied)|Consumer<br>accounts<br>aren't<br>supported for<br>Google<br>Workspace<br>data stores.|Search is called<br>using a<br>consumer<br>account<br>(@gmail.com)<br>credential, which<br>isn't supported<br>for Google<br>Workspace data<br>stores.|<br>Remove Google Workspace data stores from the<br>engine or use a managed Google Account.|
|403<br>(Permission<br>Denied)|Customer ID<br>mismatch for<br>data store|Search is only<br>allowed for users<br>who belong to<br>the same<br>organization as<br>Google<br>Workspace data<br>stores.|<br>Remove Google Workspace data stores from the<br>engine or contact support if the user and Google<br>Workspace data stores are meant to be in different<br>organizations.|

|Error code|Error message|Description|Troubleshooting|
|---|---|---|---|
|403|Workspace|A Google|Contact your Google Workspace administrator to|
|(Permission|access for|Workspace|enable access|
|Denied)|Agent Space<br>disabled by<br>organization<br>administrator.|administrator<br>has disabled<br>access to Google<br>Workspace data<br>for Gemini<br>Enterprise.|<br>(https://support.google.com/a/answer/16479199).|

### What's next

- To provide a user interface for querying your Gmail data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Gmail data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions, see Manage actions (/gemini/enterprise/docs/manage-actions). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Configure OAuth for Gmail

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gmail/config

The Gmail connector uses a Google-managed OAuth app to access your Gmail data. You don't need to enable Gmail APIs, create your own OAuth app, add OAuth scopes, or create OAuth client credentials. 

Depending on how your organization restricts OAuth app access, a Google Workspace administrator might need to add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the connector. For instructions, see Allowlist the Google-managed OAuth app (#allowlist-oauth-app). 

**Note:** Existing Gmail data stores that were configured with a customer-managed OAuth app continue to function. New Gmail data stores use the Google-managed OAuth app described on this page. 

### Allowlist the Google-managed OAuth app

If your Google Workspace organization restricts OAuth app access, a Google Workspace administrator must add the Google-managed OAuth app to your organization's OAuth app allowlist before users can authorize the Gmail connector. 

- To add the OAuth app to the allowlist, follow these steps: 

   1. Sign in to the Google Admin console (https://admin.google.com) as a Google Workspace administrator. 

   2. Go to **Security** > **Access and data control** > **API controls** . 

   3. Under **App access control** , click **Manage app access** . 

   4. Click **Configure new app** > **OAuth App Name Or Client ID** . 

   5. In the search field, enter the following Gemini Enterprise OAuth client ID: 

```
502998392228-hpelhql0ouj9ckiu3l39lllsir24b02s.apps.googleusercontent.com
```

6. Select the app from the search results and click **Select** . 

7. For the access level, select **Trusted** . For details on other access levels, see Control which apps access Google Workspace data 

(https://support.google.com/a/answer/7281227). 

8. Click **Continue** and then **Finish** to save the change. 

For more information about OAuth app allowlisting, see Control which third-party & internal apps access Google Workspace data 

(https://support.google.com/a/answer/7281227) in the Google Workspace Admin Help. 

Last updated 2026-10-14 UTC. 



## Import from Cloud Storage

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage

You can create data stores from Cloud Storage tables in two ways: 

- **One-time ingestion** : You import data from a Cloud Storage folder or file into a data store. The data in the data store doesn't change unless you manually refresh the data (/gemini/enterprise/docs/refresh-data). 

- **Periodic ingestion** : You import data from a Cloud Storage folder or file, and you set a sync frequency that determines how often the data store is updated with the most recent data from that Cloud Storage location. 

The following table compares the two ways that you can import Cloud Storage data into Gemini Enterprise data stores. 

|One-time ingestion|Periodic ingestion|
|---|---|
|Generally available (GA).|Public preview.|
|Data must be refreshed manually.|Data updates automatically every one, three,<br>or five days. Data cannot be manually<br>refreshed.|
|Gemini Enterprise creates a single data store<br>from one folder or file in Cloud Storage.|Gemini Enterprise creates a_data connector_,<br>and associates a data store (called an_entity_<br>data store) with it for the file or folder that is<br>specified. Each Cloud Storage data connector<br>can have a single entity data store.|
|Data from multiple files, folders, and buckets<br>can be combined in one data store by first<br>ingesting data from one Cloud Storage location<br>and then more data from another location.|<br>Because manual data import is not supported,<br>the data in an entity data store can only be<br>sourced from one Cloud Storage file or folder.|
|Data source access control is supported. For<br>more information, see<br>Data source access<br>control(/gemini/enterprise/docs/identity).|Data source access control is not supported.<br>The imported data can contain access controls<br>but these controls won't be respected.|
|You can create a data store using either the<br>Google Cloud console or the API.|You must use the console to create data<br>connectors and their entity data stores.|
|CMEK-compliant.|CMEK-compliant.|

### Before you begin

To import data from a source Google Cloud project that's different from the Google Cloud project with the Gemini Enterprise data store, grant the following Identity and Access Management (IAM) roles to the `service-` _`PROJECT_NUMBER`_ `@gcp-sadiscoveryengine.iam.gserviceaccount.com` service account in the project that contains the Gemini Enterprise data store: 

Storage Object Admin ( `roles/storage.objectAdmin` ) 

- (/storage/docs/access-control/iam-roles) 

Storage Object Viewer ( `roles/storage.objectViewer` ) 

(/storage/docs/access-control/iam-roles) 

**Caution:** When you import data from Cloud Storage into a Gemini Enterprise data store, Cloud Storage permissions aren't imported with the data. After import, any user with sufficient Gemini Enterprise permissions (/gemini/enterprise/docs/access-control#roles) can view the data, even if they don't have permission to view the data in Cloud Storage. 

### Import once from Cloud Storage

To ingest data from Cloud Storage, use the following steps to create a data store and ingest data using either the Google Cloud console or the API. 

Before importing your data, review Prepare data for ingesting (/gemini/enterprise/docs/prepare-data#unstructured). 

**Note:** Data import is recursive. That is, if there are folders within the bucket or folder that you specify, files within those folders are imported. 

ConsoleREST (#rest) (#console) 

To use the console to ingest data from a Cloud Storage bucket, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page. 

3. Click **Create Data Store** . 

4. On the **Select a data source** page, select **Cloud Storage** . 

5. In the **Select a folder or file you want to import** section, select **Folder** or **File** . 

6. Click **Browse** and choose the data you have prepared for ingesting (/gemini/enterprise/docs/prepare-data), and then click **Select** . Alternatively, enter the location directly in the **`gs://`** field. 

7. Select what kind of data you are importing. 

8. Click **Continue** . 

9. If you are doing one-time import of structured data: 

   - a. Map fields to key properties. 

   - b. If there are important fields missing from the schema, use **Add new field** to add them. 

For more information, see About auto-detect and edit 

(/gemini/enterprise/docs/provide-schema#about-auto-and-edit). 

      - c. Click **Continue** . 

10. Choose a region for your data store. 

11. Enter a name for your data store. 

12. Optional: If you selected unstructured documents, you can select parsing and chunking options for your documents. To compare parsers, see Parse documents 

   - (/gemini/enterprise/docs/parse-chunk-documents#parsing). For information about chunking see Chunk documents for RAG 

   - (/gemini/enterprise/docs/parse-chunk-documents#parse-chunk-rag). 

The OCR parser (/gemini/enterprise/docs/parse-chunk-documents#parsing-pdfs) and layout parser 

(/gemini/enterprise/docs/parse-chunk-documents#layout-parsing) can incur additional costs. See Document AI feature pricing 

(/generative-ai-app-builder/pricing#document_ai_feature_pricing). 

To select a parser, expand **Document processing options** and specify the parser options that you want to use. 

13. Click **Create** . 

14. To check the status of your ingestion, go to the **Data Stores** page and click your data store name to see details about it on its **Data** page. When the status column on the **Activity** tab changes from **In progress** to **Import completed** , the ingestion is complete. 

Depending on the size of your data, ingestion can take several minutes or several hours. 

### Connect to Cloud Storage with periodic syncing

Before importing your data, review Prepare data for ingesting 

(/gemini/enterprise/docs/prepare-data). 

The following procedure describes how to create a data connector that associates a Cloud Storage location with a Gemini Enterprise data connector and how to specify a folder or file in that location for the data store that you want to create. Data stores that are children of data connectors are called _entity_ data stores. 

Data is synced periodically to the entity data store. You can specify synchronization daily, every three days, or every five days. 

Console 

(#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page. 

3. Click **Create Data Store** . 

4. On the **Source** page, select **Cloud Storage** . 

5. Select what kind of data you are importing. 

6. Click **Periodic** . 

7. Select the **Synchronization frequency** , how often you want the Gemini Enterprise connector to sync with the Cloud Storage location. You can change the frequency later. 

8. In the **Select a folder or file you want to import** section, select **Folder** or **File** . 

9. Click **Browse** and choose the data you have prepared for ingesting (/gemini/enterprise/docs/prepare-data), and then click **Select** . Alternatively, enter the location directly in the **`gs://`** field. 

10. Click **Continue** . 

11. Choose a region for your data connector. 

12. Enter a name for your data connector. 

13. Optional: If you selected unstructured documents, you can select parsing and chunking options for your documents. To compare parsers, see Parse documents 

   - (/gemini/enterprise/docs/parse-chunk-documents#parsing). For information about chunking see Chunk documents for RAG 

(/gemini/enterprise/docs/parse-chunk-documents#parse-chunk-rag). 

The OCR parser and layout parser can incur additional costs. 

To select a parser, expand **Document processing options** and specify the parser options that you want to use. 

14. Click **Create** . 

You have now created a data connector, which will periodically sync data with the Cloud Storage location. You have also created an entity data store, which is named `gcs_store` . 

15. To check the status of your ingestion, go to the **Data Stores** page and click your data connector name to see details about it on its **Data** page 

**Data ingestion activity** tab. When the status column on the **Data ingestion activity** tab changes from **In progress** to **succeeded** , the first ingestion is complete. 

Depending on the size of your data, ingestion can take several minutes to several hours. 

After you set up your data source and import data the first time, data is synced from that source at a frequency that you select during setup. About an hour after the data connector is created, the first sync occurs. The next sync then occurs around 24 hours, 72 hours, or 120 hours later. 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps in Create a search app (/gemini/enterprise/docs/create-app). 

- To preview how your search results appear after your app and data store are set up, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Sync from Google Groups

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-groups

**Preview:** You need to be on the allowlist to use this connector. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

**Note:** You must enable Google Workspace smart features in other Google products to connect Google Groups data to Gemini Enterprise. For information, see Turn Google Workspace smart features on or off (https://support.google.com/mail/answer/15604322). 

To search data from Google Groups, use the following steps to create a connector using the Google Cloud console. 

### Before you begin

- You must be signed into the Google Cloud console with the same account that you use for the Google Workspace instance that you plan to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Google Groups. 

- To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider 

- (/gemini/enterprise/docs/configure-identity-provider). Gemini Enterprise strictly respects the source system's permissions and group access settings. Users can only search and view content from groups that they are a member of and authorized to view (no privilege escalation). 

- If you use security controls, be aware of their limitations related to data in Google Groups, as discussed in the following table: 

Security control 

Note the following 

|Data Residency (DRZ)<br>(/gemini/enterprise/docs/locations|)<br>Gemini Enterprise only guarantees data residency in<br>Google Cloud. For information about data residency an<br>Google Groups, see Google Workspace compliance<br>guidance and documentation, including<br>Data regions fo<br>Google Workspace<br>(https://support.google.com/a/answer/9223653). Also<br>review examples like<br>Choose the region where data is<br>stored(https://support.google.com/a/topic/7631290) a<br>Digital sovereignty<br>(https://workspace.google.com/intl/en_in/security/digit<br>sovereignty/)<br>.|
|---|---|
|Customer-managed encryption<br>keys (CMEK)<br>(/gemini/enterprise/docs/cmek)|Your keys only encrypt data within Google Cloud. Cloud<br>Key Management Service controls don't apply to data<br>stored in Google Groups.|
|Access Transparency<br>(/gemini/enterprise/docs/access-<br>transparency)|Access Transparency logs actions taken by Google<br>personnel on the Google Cloud project. You'll also need<br>to review the Access Transparency logs created by<br>Google Workspace. For more information, see<br>Access<br>Transparency log events<br>(https://support.google.com/a/answer/9230979) in the<br>Google Workspace Admin Help documentation.|

Console 

(#console) 

To use the console to make Google Groups data searchable, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page. 

3. Click **Create Data Store** . 

4. On the **Select a data source** page, select **Google Groups** . 

5. Choose a region for your data store. 

6. Enter a name for your data store. 

7. Click **Create** . Depending on the size of your data, ingestion can take several minutes to several hours. Wait at least an hour before using your data store for searching. 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps in Create a search app (/gemini/enterprise/docs/create-app). 

- To preview how your search results appear after your app and data store are set up, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Connect to Google Sites

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-sites

**Note:** You must enable Google Workspace smart features in other Google products to connect Google Sites data to Gemini Enterprise. For information, see Turn Google Workspace smart features on or off (https://support.google.com/mail/answer/15604322). 

To search data from Google Sites, use the following steps to create a connector using the Google Cloud console. 

### Before you begin

- You must be signed into the Google Cloud console with the same account that you use for the Google Workspace instance that you plan to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Google Sites. 

- To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider 

- (/gemini/enterprise/docs/configure-identity-provider). 

- If you use security controls, be aware of their limitations related to data in Google Sites, as discussed in the following table: 

|Security control|Note the following|
|---|---|
|Data Residency (DRZ)<br>(/gemini/enterprise/docs/loc|ations)<br>Gemini Enterprise only guarantees data residency in<br>Google Cloud. For information about data residency an<br>Google Sites, see Google Workspace compliance<br>guidance and documentation, including<br>Data regions fo<br>Google Workspace<br>(https://support.google.com/a/answer/9223653). Also<br>review examples like<br>Choose the region where data is<br>stored(https://support.google.com/a/topic/7631290) a<br>Digital sovereignty<br>(https://workspace.google.com/intl/en_in/security/digit<br>sovereignty/)<br>.|

|Customer-managed encryption<br>keys (CMEK)<br>(/gemini/enterprise/docs/cmek)|Your keys only encrypt data within Google Cloud. Cloud<br>Key Management Service controls don't apply to data<br>stored in Google Sites.|
|---|---|
|Access Transparency|Access Transparency logs actions taken by Google|
|(/gemini/enterprise/docs/access-<br>transparency)|personnel on the Google Cloud project. You'll also need<br>to review the Access Transparency logs created by<br>Google Workspace. For more information, see<br>Access<br>Transparency log events<br>(https://support.google.com/a/answer/9230979) in the<br>Google Workspace Admin Help documentation.|

Console 

(#console) 

To use the console to make Google Sites data searchable, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page. 

3. Click **Create Data Store** . 

4. On the **Select a data source** page, select **Google Sites** . 

5. Choose a region for your data connector. 

6. Enter a name for your data connector. 

7. Click **Create** . 

### Next steps

- To attach your data store to an app, create an app and select your data store following the steps in Create a search app (/gemini/enterprise/docs/create-app). 

- To preview how your search results appear after your app and data store are set up, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

- To restrict retrieval to specific Site URLs or exclude them, see Add filters to a Google Sites data store 

(/gemini/enterprise/docs/connectors/gsites/add-filters-to-gsites-data-store). 

Last updated 2026-10-14 UTC. 



## Add filters to a Google Sites data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gsites/add-filters-to-gsites-data-store

This page explains how to add filters to your Google Sites data stores in Gemini Enterprise. Use filters to narrow search results by including or excluding specific Site URLs or URL prefixes. 

### Filter types

The Google Sites data store supports the following filter: 

- **Site Path Prefix** : A list of exact Site URLs or URL prefixes. You can apply this filter in one of two modes for each data store: 

   - **Include in search** : Only sites whose URLs start with one of the listed prefixes are retrieved. This mode maps to the `admin_filter.SitePathPrefix` parameter in the API. 

   - **Exclude from search** : Sites whose URLs start with one of the listed prefixes are removed from search results. This mode maps to the `admin_exclusion_filter.SitePathPrefix` parameter in the API. 

**Note:** The **Site Path Prefix** filter for each data store can be configured to either include or exclude specified URL prefixes. You cannot apply both inclusion and exclusion filters simultaneously for the same data store. Set **`admin_filter.SitePathPrefix`** to only include matching prefixes, or set **`admin_exclusion_filter.SitePathPrefix`** to exclude matching prefixes. 

### Add filters to a new data store

You can add a filter when you create a Google Sites data store using either the Google Cloud console or the API. 

C l REST (# t) 

To add a filter when you create a Google Sites data store: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data stores** . 

3. Click **+ Create data store** . 

4. On the **Select a data source** page, select **Google Sites** . 

5. On the **Specify the Google Sites source for your data store** step, under **Filters** , configure the **Site Path Prefix** filter: 

   - a. Select **Include in search** to retrieve only the listed sites, or **Exclude from search** to remove the listed sites from search results. 

   - b. In the **Site Path Prefix** field, enter one or more exact Site URLs or URL prefixes. For example, 

`https://sites.google.com/a/example.com/site-name` . 

6. Click **Continue** . 

7. Complete the remaining configuration steps and click **Create** . 

If you select **Include in search** , the filter is saved as `admin_filter.SitePathPrefix` in the data connector parameters. If you select **Exclude from search** , it is saved as 

`admin_exclusion_filter.SitePathPrefix` . 

### Update filters in an existing data store

You can update the **Site Path Prefix** filter in an existing data store using either the Google Cloud console or the API. 

ConsoleREST (#rest) (#console) 

To modify the existing filter configuration: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Google Sites data store. 

3. Click **View/edit parameters** . 

4. In the **View/edit parameters** panel, under **Filters** : 

   - a. Switch the radio selection between **Include in search** and **Exclude from search** , or keep the current selection. 

   - b. Add, edit, or remove **Site Path Prefix** entries. 

5. Click **Save** . 

### Remove filters from a data store

You can remove the **Site Path Prefix** filter from an existing data store using either the Google Cloud console or the API. 

ConsoleREST (#rest) (#console) 

To remove the existing filter configuration: 

1. In the Google Cloud console navigation menu, click **Data stores** . 

2. Select your Google Sites data store. 

3. Click **View/edit parameters** . 

4. In the **View/edit parameters** panel, under **Filters** , clear all entries in the **Site Path Prefix** field. 

5. Click **Save** . 

### Parameter reference

The following table describes the API parameters that the **Site Path Prefix** filter maps to. 

|Parameter|Type|Description|
|---|---|---|
|`params.admin_filter.`|Repeated|Site URLs or URL prefixes to include in retrieval. Set when|
|`SitePathPrefix`|string|the Console filter mode is Include in search. Mutually<br>exclusive with`admin_exclusion_filter`.|
|`params.admin_`|Repeated|Site URLs or URL prefixes to exclude from retrieval. Set|
|`exclusion_filter.`|string|when the Console filter mode is Exclude from search.|
|`SitePathPrefix`||Mutually exclusive with`admin_filter`.|

### What's next

- To provide a user interface for querying your Google Sites data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Google Sites data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC. 



## Sync people data

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people

You can set up people search for your work teams by syncing people data from Google Workspace. After the people search data store is set up and the data is ingested into the Gemini Enterprise index, it enables features such as Knowledge Graph and Natural Language Processing (/gemini/enterprise/docs/use-knowledge-graph-search). This improves search quality, letting you find people in your Google Workspace Directory through the web app. 

For information about Google Workspace Directory, see the Google Workspace documentation: 

- Overview: Set up and manage the Directory (https://support.google.com/a/answer/1628009) 

- Add information to a user's Directory profile (https://support.google.com/a/answer/6191788) 

**Note:** If your people data is not in Google Workspace, you can import it from Cloud Storage or BigQuery. For information, see Import people data from a custom source (/gemini/enterprise/docs/connectors/connect-people-custom). 

#### Before you begin

Before you can set up a people search data store, you must do the following: 

- To enforce data source access control and secure data in Gemini Enterprise, make sure that you have configured your identity provider (/gemini/enterprise/docs/configure-identity-provider). Gemini Enterprise strictly respects the source system's permissions and directory visibility settings. Users can only view directory profiles that they are authorized to access in Google Workspace Directory (no privilege escalation). 

- A Google Workspace administrator must enable people search on Google Workspace data: 

   1. Sign in to the Google Admin console (https://admin.google.com/) with an administrator account. 

   2. Go to **Directory** > **Directory settings** . 

   3. Turn on **Contact sharing** . 

- Sign in to the Google Cloud console with the same account that you use for Google Workspace. 

- If you use security controls, be aware of their limitations related to data in Google Workspace, as discussed in the following table: 

|Security control|Note the following|
|---|---|
|Data Residency (DRZ)<br>(/gemini/enterprise/docs/locations|)<br>Gemini Enterprise only guarantees data residency in<br>Google Cloud. For information about data residency an<br>Google Workspace, see Google Workspace compliance<br>guidance and documentation, including<br>Data regions fo<br>Google Workspace<br>(https://support.google.com/a/answer/9223653). Also<br>review examples like<br>Choose the region where data is<br>stored(https://support.google.com/a/topic/7631290) a<br>Digital sovereignty<br>(https://workspace.google.com/intl/en_in/security/digit<br>sovereignty/)<br>.|
|Customer-managed encryption<br>keys (CMEK)<br>(/gemini/enterprise/docs/cmek)|Your keys only encrypt data within Google Cloud. Cloud<br>Key Management Service controls don't apply to data<br>stored in Google Workspace.|
|Access Transparency<br>(/gemini/enterprise/docs/access-<br>transparency)|Access Transparency logs actions taken by Google<br>personnel on the Google Cloud project. You'll also need<br>to review the Access Transparency logs created by<br>Google Workspace. For more information, see<br>Access<br>Transparency log events<br>(https://support.google.com/a/answer/9230979) in the<br>Google Workspace Admin Help documentation.|

Before creating the people data store, you need to set up a service account and domain-wide delegation. 

#### Set up the service account

1. Verify that you have the permissions you need to create a service account. See Required roles (/iam/docs/service-accounts-create#permissions). 

2. Create a service account (/iam/docs/service-accounts-create) in a Google Cloud project within the organization. 

3. Optional: Skip the **Grant this service account access to project (optional)** step. 

_Skip the Grant this service account access to project (optional) step._ 

4. Grant the Discovery Engine service account ( `service-` _`PROJECT_NUMBER`_ `@gcp-sadiscoveryengine.iam.gserviceaccount.com` ) access as a **Service account token creator** ( `roles/iam.serviceAccountTokenCreator` ), and click **Save** . 

_Grant the Discovery Engine service account access._ 

5. After the service account is created, click the **Details** tab of the service account, and click **Advanced settings** . 

6. Copy the client ID for domain-wide delegation. 

_Copy the client ID._ 

#### Set up domain-wide delegation

1. Sign in to the Google Workspace Admin console (https://admin.google.com). 

2. Navigate to **Security** > **Access and data control** > **API controls** . 

3. Click **Manage domain wide delegation** . 

<!-- Start of picture text -->
Click Manage domain wide delegation.<br><!-- End of picture text -->

4. Click **Add new** . 

<!-- Start of picture text -->
Click Add new.<br><!-- End of picture text -->

5. In the **Add a new client ID** dialog, do the following: 

- a. **Client ID** : Enter the client ID. 

- b. **OAuth scopes** : Enter 

`https://www.googleapis.com/auth/directory.readonly` . 

- c. Click **Authorize** . 

_Configure the domain-wide delegation settings._ 

#### Configure custom attributes

If you have custom people data (also known as custom attributes) and want the custom attribute data to appear in search results, do the following: 

1. Sign in to the Google Workspace Admin console (https://admin.google.com). 

2. Click **Directory > Users > More options > Manage custom attributes** . 

_Click Manage custom attributes._ 

3. To make the custom attribute searchable, set **Visibility** for the attribute to **Visible to organization** . 

_Set the visibility of the custom attribute to Visible to organization to make it searchable._ 

#### Connect using OAuth

Connecting with OAuth offers an alternative to domain-wide delegation for authenticating your people search connector. This method requires you to create an OAuth client to authorize the connector to access your organization's directory 

data. The following steps guide you through creating the client, setting up the connector, and updating the credentials. 

1. Create an OAuth client 

   - a. Navigate to the Google Cloud console and search for `Credentials` . 

b. Click **Create Credentials** . 

_Create credentials._ 

c. Select **OAuth client ID** from the drop-down menu. 

_Select the OAuth client ID._ 

d. Select **Web application** from the **Application type** drop-down menu. 

_Select the web application option._ 

- e. Add a name for the OAuth client ID and enter the authorized redirect URI as `https://vertexaisearch.cloud.google.com/oauth-redirect` . 

- f. Click **Create** and save the credentials. 

#### Create a people search data store

To connect your people data to Gemini Enterprise, follow these steps: 

Console 

(#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page. 

3. Click **Create Data Store** . 

4. On the **Select a data source** page, click **People search** . 

_Select the People Search data store._ 

5. Configure the authentication details: 

You can authenticate using either an OAuth 2.0 refresh token or domainwide delegation. 

Using an OAuth 2.0 refresh token: 

- a. Select **OAuth 2.0 refresh token** and add the client ID and client secret you created in the previous steps. 

- b. Click the **Authenticate** button to give consent for the scope `https://www.googleapis.com/auth/directory.readonly` . 

- c. Provide a name for the connector and click **Create** . 

Using domain-wide delegation: 

   - a. Select **Domain-wide delegation** . 

   - b. Enter the service account email and the private key that you generated. 

   - c. Click **Continue** . 

6. Update the connector credentials: 

You must update your client credentials if your OAuth refresh token has expired, or if you want to switch credential flows for ingesting documents. This process is necessary when you switch from domainwide delegation to OAuth, or from OAuth back to domain-wide delegation. 

- a. Navigate to the People Search connector. 

- b. Click **Re-authenticate** . 

_Click the Re-authenticate button._ 

- c. Choose the credential flow that you want to use. 

_Click the credential flow._ 

- d. Add the new credentials and click **Authenticate** . 

- e. Enter the email address of the account that fetches the people data. If you prefer not to use an administrator account, you can use an alternate account that has access to the organization's directory data. 

- f. Enter the service account email you created previously. 

- g. Click **Continue** . 

_Configure the authentication details._ 

7. Choose a region for your data store. 

8. In the **Your data store name** field, enter a name for your data store. 

9. Click **Create** . 

Syncing might take several minutes to hours, depending on data size. 

### Error messages

The following table describes error messages that you might encounter when syncing people data by using data indexing. This table includes gRPC error codes and suggested troubleshooting steps. 

|Error Code<br>(gRPC)|Error Message|Description|Troubleshooting|
|---|---|---|---|
|9 (Failed<br>precondition|)<br>Authentication<br>failed: Service<br>account<br>misconfigured.<br>Ensure that the<br>Discovery Engine<br>service account<br>has the service<br>account token<br>creator role and<br>that the domain<br>wide delegation<br>(DWD) service<br>account auth<br>scope is set up<br>correctly on<br>Google Cloud<br>Admin. All<br>documents have<br>been deleted<br>from Gemini<br>Enterprise.|This error<br>occurs when<br>the<br>Discovery<br>Engine<br>service<br>account<br>lacks the<br>service<br>account<br>token<br>creator role,<br>or the<br>domain-wide<br>delegation<br>(DWD)<br>service<br>account<br>lacks the<br>correct auth<br>scope.|Verify that the Discovery Engine service account<br>has the service account token creator role as<br>described in the<br>Set up the service account<br>(/gemini/enterprise/docs/connectors/connect-<br>people#service-account)<br>section and verify that the DWD service account<br>auth scope is set up correctly on Google Cloud<br>Admin as described in the<br>Set up domain-wide<br>delegation<br>(/gemini/enterprise/docs/connectors/connect-<br>people#domain-delegation)<br>section. Regrant the missing service account<br>permissions.|

|Error Code<br>(gRPC)|Error Message|Description|Troubleshooting|
|---|---|---|---|
|9 (Failed<br>precondition|)<br>Zero results<br>fetched after full<br>sync. All<br>documents have<br>been deleted<br>from Gemini<br>Enterprise.|This error<br>occurs when<br>contact<br>sharing is<br>disabled in<br>directory<br>settings of<br>the Admin<br>console.|Verify that you turned on contact sharing to<br>enable people search on Google Workspace data<br>as described in the<br>Before you begin<br>(/gemini/enterprise/docs/connectors/connect-<br>people#before-you-begin)<br>section.|
|3 (Invalid<br>argument)|Failed to<br>exchange signed<br>JWT for access<br>token. Google<br>Workspace<br>account has been<br>deleted. All<br>documents have<br>been deleted<br>from Gemini<br>Enterprise.|<br>This error<br>occurs when<br>the Google<br>Workspace<br>account is<br>deleted.|Create a new connector with an active Google<br>Workspace account.|
|3 (Invalid<br>argument)|GAIA id not<br>found.<br>Authentication<br>failed.|This error<br>occurs when<br>the user<br>account is<br>incorrect.|Verify that the user account exists and enter the<br>correct credentials.|
|8 (Resource<br>exhausted)|The quota for the<br>project exceeded.<br>Increase the<br>document quota<br>for the project.|<br>This error<br>occurs when<br>the project<br>quota is<br>exceeded.|Increase the document quota for the project. For<br>more information, see<br>Quotas<br>(/gemini/enterprise/docs/quotas).|
|13 (Internal<br>error)|Internal error<br>encountered.|This error<br>occurs when<br>there is an<br>internal<br>error.|Contact the support team.|

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC.
