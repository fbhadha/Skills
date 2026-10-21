# Gemini Enterprise: connectors and data stores / Introduction to connectors and data stores to Set up a Google Calendar data store
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 6-46, extracted 2026-10-18

Contains:
- Introduction to connectors and data stores (pages 6-14) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores
- Introduction to self-hosted data sources (pages 15-20) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-self-hosted
- Prepare data for custom data sources (pages 21-29) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/prepare-data
- Create a data store: overview (pages 30-37) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store
- Google Calendar connector: overview (pages 38-41) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal
- Set up a Google Calendar data store (pages 42-46) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/set-up-data-store

## Introduction to connectors and data stores

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores

Connectors get data from Google and third-party data sources into Gemini Enterprise, storing it in dedicated data stores. This document provides an overview of these connectors. Centralizing your data in Gemini Enterprise enhances data accessibility, search functionality, and analytical capabilities. 

_Connector overview_ 

### Connector and data store concepts

Data stores 

Each data source supports a set of entity types. For example, Jira Cloud has entities such as issues, attachments, comments, and worklogs, which are unique to the data source. Gemini Enterprise creates a separate data store for each entity. Therefore, when you create a data store using the Google Cloud console, you get a collection of data stores representing these ingested data entities. 

Data federation versus ingestion (indexing) 

Data federation directly retrieves information from the specified data source. Because data isn't copied into the Gemini Enterprise index, you don't need to worry about data storage. However, because the data is not indexed, search quality might be lower. 

Data ingestion (indexing) copies data into the Gemini Enterprise index. This can result in improved search quality. However, this process consumes more storage and time. 

If the connector supports both data federation and data ingestion, select your preferred data connection method. 

Note: When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

Unstructured data 

The supported data format is specific to the data source and the entity type. If the content in an entity is stored in an unstructured format—such as PDF, HTML, DOCX, PPTX, XLSX, and XLSM—an unstructured data store is created by Gemini Enterprise. For more information and supported file types, see Unstructured search 

(/gemini/enterprise/docs/connectors/prepare-data#unstructured). 

Structured data 

The supported data format is specific to the data source and the entity type. If the content in an entity is stored in a structured format, a structured data store is created by Gemini Enterprise. For more information, see Structured search 

(/gemini/enterprise/docs/connectors/prepare-data#structured). 

Data schemas 

The data schema defines the data structure. When you import structured data using Gemini Enterprise, the system auto-detects the schema. You can use the auto-detected schema or define the schema using the API. For more information, see Provide or auto-detect a schema (/gemini/enterprise/docs/provide-schema). 

Data store regions 

When ingesting data, you need to select the region where you want to store the data, such as global, the US, or the EU. For more information, see Data residency and ML regional processing commitments (/gemini/enterprise/docs/locations). Data stored in the US or EU regions require data encryption. The default encryption is with Google-owned and Google-managed encryption keys, but alternatively, you can use customer-managed encryption keys 

(/gemini/enterprise/docs/cmek). 

Data syncs 

A data sync pulls and updates identity data (such as roles, permissions, and users) and entity data (such as data related to a specific data source) from the original data source. For more information, see Data sync types and schedules (#sync-types-schedules). 

### Data sync types and schedules

A data sync captures entity data, identity data, or both, and updates the contents of the data store in Gemini Enterprise. 

#### Sync types

Data stores in Gemini Enterprise use two essential types of data sync: 

- A _full sync_ captures the entire state of the third-party app or service. This includes additions, updates, and deletions. A full sync replaces the existing contents of the data store. 

- An _incremental sync_ periodically captures entity data that has been added or updated since the last sync. It does not sync identity data or deletions of entity data. 

You can schedule a full sync separately for the following data types: 

- An _entity sync_ captures data specific to the third-party data source. For example, a data store for a system like Jira can sync issues, worklogs, comments, and attachments. Entity syncs don't include identity information. 

- An _identity sync_ captures data about user accounts associated with an ACL group. 

Interaction between identity sync and full sync 

To understand how an individual identity sync run works with a full sync run, consider an example scenario including two pages: `page_1` , linked to an ACL group `group_1` ; and `page_2` , linked to an ACL group `group_2` . 

1. An initial identity sync runs, and retrieves information about groups `group_1` and `group_2` . 

      - Assume that `group_1` contains user `user_1` . 

      - Assume that `group_2` contains user `user_2` . 

   - This identity sync establishes the following mapping: 

      - `user_1` maps to `group_1` . 

      - `user_2` maps to `group_2` . 

2. Alongside the identity sync, a full sync runs, fetching both `page_1` and `page_2` . This full sync establishes the following mapping: 

      - `user_1` has access to `page_1` (via `group_1` ). 

      - `user_2` has access to `page_2` (via `group_2` ). 

#### Sync schedules

For each data store, you can select a frequency for different sync types: 

- Full syncs of all identity data and entity data can be scheduled simultaneously for every 3 hours, 6 hours, 12 hours, 1 day, or 3 days. 

- Independent full syncs of all identity data, and independent full syncs of all entity data, can be scheduled separately using any of the following custom sync frequencies: 

   - Entity data: Every 3 hours, 6 hours, 12 hours, 1 day, 3 days, 5 days, and every 7 days. 

- Identity data: Every 30 minutes, 1 hour, 3 hours, 6 hours, 12 hours, 1 day, 3 days, 5 days, and every 7 days. 

Incremental syncs of updated or added entity data can be scheduled for every 3 hours, 6 hours, 12 hours, 1 day, 3 days, 5 days, or every 7 days. By default, an incremental sync is performed every 3 hours. 

**Note:** Incremental syncs must be scheduled to occur more frequently than full sync. For example, if you have scheduled full syncs for every 12 hours, you can only schedule incremental syncs for every 3 hours or every 6 hours. 

If you schedule incremental sync and full sync for the same frequency, incremental sync will be automatically paused and require manual intervention to resume. 

Frequency recommendations 

Choose a data sync frequency that aligns with the volume of records fetched and the recommended queries per second (QPS). 

The following table shows the typical number of records retrieved for one, three, five, and seven-day syncs. The actual number of records may vary depending on the data source and its configuration. 

|QPS|<sup>Record volume for 1-</sup><br>day sync|Record volume for 3-<br>day sync|Record volume for 5-<br>day sync|Record volume for 7-<br>day sync|
|---|---|---|---|---|
|5|432k|1.296M|2.16M|3M|
|10|864k|2.592M|4.32M|6M|
|20|1.7M|5.1M|8.5M|11.9M|
|50|4.3M|12.9M|21.5M|30.1M|
|100|8.6M|25.8M|43M|60.2M|

#### Pausing and resuming syncs

You can pause, and resume, both full syncs and incremental syncs: 

- When you pause a sync type, the data store cancels ongoing syncs of that type and stops scheduling new syncs of that type. 

- When you resume a sync type, the data store schedules the new sync based on the last scheduled sync time, but does not continue the previously interrupted sync. 

For example, if you pause full sync while a full sync is occurring, the data store cancels that sync. If you later resume full sync, the data store automatically schedules a new full sync according to the full sync schedule. 

### Google data sources

You can connect to Google data sources, such as BigQuery, Spanner, and Google Drive. 

#### Checklist for Google data sources

Before sending data to Gemini Enterprise, go through the following checklist: 

- Set up access control for your data source. For more information see, Identity and permissions (/gemini/enterprise/docs/identity). 

- Decide whether data should be federated or ingested (indexed) (#data_federation_versus_ingestion_indexing). 

- Decide how often the data should be synced. 

- If you are using customer-managed encryption keys (CMEK), create multiregion keys. For more information, see Register single-region keys for third- party data sources 

- (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

- If you have personally identifiable information (PII) and intend to use autocomplete for query suggestions, see protect against PII leaks (/gemini/enterprise/docs/configure-autocomplete#pii). 

#### Supported Google data sources

**Note:** For more information on the Google data sources, see Connect a Google data source (/gemini/enterprise/docs/create-data-store). 

Google Drive Gmail Google Calendar People search (/gemini/enterprise/do (/gemini/enterprise/do (/gemini/enterprise/do (/gemini/enterprise/do cs/connectors/gdrive) cs/connectors/gmail) cs/connectors/gcal) cs/connectors/connectpeople) 

### Third party data sources

Third-party data stores ingest third-party application data into Gemini Enterprise. 

#### Checklist for third-party data sources

Before connecting a third-party data source to Gemini Enterprise, go through the following checklist: 

- Specific scopes and permissions must be configured for certain data sources. An administrator of the third-party application must review the required credentials to connect a data source and set up authentication and permissions. For information about the specific scopes and permissions, see the respective third-party data source documentation. 

- Set up access control for your data store. For more information, see Identity and permissions (/gemini/enterprise/docs/identity) 

- Decide whether data should be federated or ingested (indexed) (#data_federation_versus_ingestion_indexing). 

- If data is ingested, make sure that resources aren't restricted for the user credential that you use to ingest data into the data source. 

- Decide how often the data should be synced. 

- If you are using customer-managed encryption keys (CMEK), create multiregion and single-region keys. For more information, see Register single- region keys for third-party data stores 

- (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

- If you have personally identifiable information (PII) and intend to use autocomplete for query suggestions, see protect against PII leaks (/gemini/enterprise/docs/configure-autocomplete#pii). 

- If you want outbound traffic from the data store to originate from a fixed set of IP addresses (for example, to allowlist them on the source system), and if the data store supports it, see Configure static IP egress 

- (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

#### Supported third-party data sources

<!-- Start of picture text -->
Note:  For the complete list of supported third-party data sources, see Connect a third-party<br>data source (/gemini/enterprise/docs/connect-third-party-data-source).<br>Microsoft Entra ID Microsoft OneDrive Microsoft Outlook Microsoft SharePoint<br> (/gemini/enterprise/do  (/gemini/enterprise/do  (/gemini/enterprise/do  (/gemini/enterprise/do<br>cs/connectors/entra- cs/connectors/ms- cs/connectors/ms- cs/connectors/ms-<br>id/connect-entra-id) onedrive) outlook) sharepoint)<br>Jira Cloud Confluence Cloud ServiceNow<br> (/gemini/enterprise/do  (/gemini/enterprise/do  (/gemini/enterprise/do<br>cs/connectors/jira- cs/connectors/confluen cs/connectors/servicen<br>cloud) ce-cloud) ow)<br><!-- End of picture text -->

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## Introduction to self-hosted data sources

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/introduction-to-self-hosted

Gemini Enterprise can securely connect to customer-managed, self-hosted, thirdparty data sources. These connections are established through Private Service Connect producer services. 

This connectivity model ensures that sensitive data remains in your control and network boundaries, while allowing Gemini Enterprise to access and use the information contained within these data sources. Using Private Service Connect lets you establish a secure and scalable communication channel, bypassing the public internet and minimizing potential security risks associated with traditional network configurations. 

_Access patterns for self-hosted data sources_ 

Gemini Enterprise supports the following self-hosted data source patterns: 

**On-premises or multi-cloud:** Data sources deployed in your data center or in another cloud provider (for example, Amazon Web Services EC2 or EKS, or Microsoft Azure virtual machines), using hybrid network connectivity. 

**Google Kubernetes Engine:** Data sources hosted within GKE clusters. 

- **Google Cloud Compute Engine:** Data sources deployed on Google Compute Engine VMs. 

### Using Private Service Connect with self-hosted services

Private Service Connect is a Google Cloud networking feature that enables private access from a consumer's Virtual Private Cloud network to managed services. It creates a secure, explicit connection between a service consumer and a service producer, eliminating the need for Virtual Private Cloud peering, complex routing, or public IP addresses. 

You can set up a Gemini Enterprise Private Service Connect deployment with the following: 

- Gemini Enterprise as the service consumer 

- Your network, containing load balancers that reference on-premises, multicloud, or Google Cloud compute resources, as the service producer 

For information about specific aspects of using Private Service Connect to connect your self-hosted service to Gemini Enterprise, see the following sections. 

#### VPC network and subnet configuration

Keep the following in mind: 

- Proxy allocation is at the VPC level, not at the load balancer level. You must create one proxy-only subnet 

- (https://cloud.google.com/load-balancing/docs/proxy-only-subnets) in each region of a virtual network (VPC) in which you use Envoy-based load balancers. If you deploy multiple load balancers in the same region and same VPC network, they share the same proxy-only subnet for load balancing. 

Health check probes 

- (https://cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-healthchecks) 

originate from the Envoy proxies located in the proxy-only subnet (https://cloud.google.com/load-balancing/docs/proxy-only-subnets) within the region. For the health check probes to function correctly, you must create firewall 

rules in the external environment that allow traffic from the proxy-only subnet to reach your external backends. 

- The proxy-only subnet is the source subnet targeting the cross cloud database. Ensure that this subnet is advertised by a Cloud Router. For more information, see Advertise specifc VPC subnetsi 

- (https://cloud.google.com/network-connectivity/docs/router/how-to/advertising-subnets). 

- The proxy-only subnet must be on the allowlist for the on-premises or CrossCloud firewall. 

- You must create proxy-only subnets regardless of whether your VPC network is auto mode or custom. A proxy-only subnet must provide 64 or more IP addresses. This corresponds to a prefix length of /26 or shorter. The recommended subnet size is /23 (512 proxy-only addresses). 

Private Service Connect NAT subnet 

Packets from the consumer VPC network are translated using source NAT (SNAT), so that their original source IP addresses are converted to source IP addresses from the NAT subnet in the producer's VPC network. Private Service Connect for NAT subnets cannot host workloads. 

The minimum subnet size for a Private Service Connect NAT is /29. You can add additional NAT subnets to a service attachment at any time, without interrupting traffic. 

You can monitor published services 

(https://cloud.google.com/vpc/docs/monitor-private-service-connect-connections) using either predefined dashboards or Google Cloud metrics for Private Service Connect NAT consumption. 

#### Load balancer configuration

A service producer places its application or service behind a Google Cloud Internal Load Balancer 

(https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#lb-types). We recommend that you use an Internal TCP Proxy Load Balancer. If using Google Kubernetes Engine, you can use an internal passthrough Network Load Balancer. 

**Note:** Each load balancer's forwarding rule can be associated with a single service attachment. You can't associate multiple service attachments with the same forwarding rule. 

Because Gemini Enterprise is not available in all locations 

(https://cloud.google.com/gemini/enterprise/docs/locations), you must enable global access when creating the internal load balancer forwarding rule. If you don't enable global access, then endpoint creation for Gemini Enterprise (the service consumer) can fail. Ensure that you have enabled global access before you create the Private Service Connect service attachment. For more information about client access for internal load balancers, see Client access 

(https://cloud.google.com/load-balancing/docs/internal#client-access). 

#### Service attachment configuration

To publish a service using Private Service Connect, a service producer creates a service attachment 

(https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#publishservice) . This attachment enables service consumers, such as Gemini Enterprise, to connect to the producer's service. For information about publishing a service and creating a service attachment, see Publish a service 

(https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#publishservice) 

The service producer has two primary options for controlling consumer connections, managed using the following connection preferences: 

- **Automatically accept all connections** : This allows any consumer to connect, without explicit approval. 

- **Accept connections for selected projects** (explicit approval): This requires you to manually approve each project that requests a connection. With this option, you can choose to accept or reject a project. 

If you use explicit project approval, then in order to establish a connection to your service attachment, you must do the following: 

1. Create a data store (for example, a Jira Data Center (/gemini/enterprise/docs/connectors/jira-dc) data store). 

2. In the **Private Service Connect** page of the Google Cloud console, accept the pending connection from the Gemini Enterprise tenant project for your new data store. You can identify the tenant project by its project ID, which ends in `-tp` . For more information, see Manage requests for access to a published service 

(https://cloud.google.com/vpc/docs/manage-private-service-connectservices#access) 

3. In the **Gemini Enterprise** page of the Google Cloud console, in **Data stores** , click the name of your new data store to see its status. The data store status is shown on its **Data** page. 

You can't see the Gemini Enterprise tenant project ID until you create a data store. The data store status remains as **Creating** until you accept the project connection in Private Service Connect. 

**Note:** Gemini Enterprise doesn't support the **Accept connections for selected networks** connection preference. 

When creating a service attachment, don't select the proxy protocol (https://cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol) unless it's supported by the self-hosted service. Doing so results in a SSL/TLS error. You can deselect the proxy protocol by editing the service attachment. 

#### Firewall configuration

Configure ingress firewall rules 

(https://cloud.google.com/vpc/docs/configure-private-service-connect-producer#firewall-rules) to allow traffic between the Private Service Connect NAT subnet and the backend VMs in the producer service load balancer. If you're using a hybrid or internet NEG as the backend, firewall rules are not required. 

### What's next

- For more information about how Gemini Enterprise integrates with Private Service Connect, see the following codelabs on Google Developer Codelabs: 

   - Gemini Enterprise to Zonal NEG self-hosted database 

(https://codelabs.developers.google.com/agentspace-psc-zonal-neg) 

- Gemini Enterprise Hybrid NEG to Cross Cloud self-hosted database (https://codelabs.developers.google.com/agentspace-psc-hybrid-neg-crosscloud) 

- Gemini Enterprise Custom Domain 

(https://codelabs.developers.google.com/agentspace-networking-customdomain) 

   - Gemini Enterprise Custom Domain, WIF Support 

   - (https://codelabs.developers.google.com/agentspace-networking-customdomainwif) 

- For more information on using an internal load balancer across VPC networks on Google Kubernetes Engine, see Create an internal load balancer across VPC networks 

(https://cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-acrossvpc-net) 

Last updated 2026-10-14 UTC. 



## Prepare data for custom data sources

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/prepare-data

Enterprises often have custom applications that are built in-house. If you want Gemini Enterprise to connect to the data sources in these custom applications, first you need to prepare the data. How you prepare data depends on the kind of data that you're importing from your custom data source and the way you choose to import it. Start with what kind of data you plan to import: 

Unstructured data (#unstructured) 

Structured data (#structured) 

For limitations for blended search, where multiple data stores can be connected to a single app, see About connecting multiple data stores 

(/gemini/enterprise/docs/apps-data-stores#blended). 

### Unstructured data

Gemini Enterprise supports search over documents that are in TXT, PDF, HTML, DOCX, PPTX, XLSX, and XLSM formats. 

The following table lists the file size limits of each file type with different configurations (for more information, see Parse and chunk documents 

(/gemini/enterprise/docs/parse-chunk-documents)). You can import up to 100,000 files at a time. 

|File type|Default import|
|---|---|
|Text-based files such as HTML, TXT, JSON, XHTML, and XML|< 200 MB|
|PPTX, DOCX, XLSX, and XLSM|< 200 MB|
|PDF|< 200 MB|

If you plan to include embeddings in your unstructured data, see Use custom embeddings (/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search 

documentation. 

If you have non-searchable PDFs (scanned PDFs or PDFs with text inside images, such as infographics), we recommend turning on the layout parser during data store creation. This allows Gemini Enterprise to extract elements such as text blocks and tables. If you have searchable PDFs that are mostly composed of machine-readable text and contain many tables, you can consider turning on OCR processing with the option for machine-readable text enabled in order to improve detection and parsing. For more information, see Parse and chunk documents 

(/gemini/enterprise/docs/parse-chunk-documents). 

If you want to use Gemini Enterprise for retrieval-augmented generation (RAG), turn on document chunking when you create your data store. For more information, see Parse and chunk documents 

(/gemini/enterprise/docs/parse-chunk-documents). 

You can import unstructured data from the following sources: 

- Cloud Storage (#storage-unstructured) 

- BigQuery (#bigquery-unstructured) 

- Google Drive (#drive) 

#### Cloud Storage

You can import data from Cloud Storage with or without metadata using Google Cloud console (/gemini/enterprise/docs/connectors/connect-cloud-storage), by the `ImportDocuments` method, or by streaming ingestion through CRUD methods. For API reference information, see `DocumentService` 

(/gemini/enterprise/docs/reference/rpc/google.cloud.discoveryengine.v1#documentservice) and `documents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.d ocuments) 

Data import is recursive. That is, if there are folders within the bucket or folder that you specify, files within those folders are imported. 

If you plan to import documents from Cloud Storage without metadata, put your documents directly into a Cloud Storage bucket. The document ID is an example of 

metadata. 

For testing, you can use the following publicly available Cloud Storage folders, which contain PDFs: 

- `gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs` 

- `gs://cloud-samples-data/gen-app-builder/search/CUAD_v1` 

- `gs://cloud-samples-data/gen-app-builder/search/kaiser-health-surveys` 

- `gs://cloud-samples-data/gen-app-builder/search/stanford-cs-224` 

If you plan to import data from Cloud Storage with metadata, put a JSON file that contains the metadata into a Cloud Storage bucket whose location you provide during import. 

Your unstructured documents can be in the same Cloud Storage bucket as your metadata or a different one. 

The metadata file must be a JSON Lines (https://jsonlines.org/) or an NDJSON file. The document ID is an example of metadata. Each row of the metadata file must follow one of the following JSON formats: 

Using `jsonData` : 

```
{ "id": "<your-id>", "jsonData": "<JSON string>", "content": { "mimeType":
"<application/pdf or text/html>", "uri": "gs://<your-gcs-
bucket>/directory/filename.pdf" } }
```

Using `structData` : 

```
{ "id": "<your-id>", "structData": { <JSON object> }, "content": {
"mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-
bucket>/directory/filename.pdf" } }
```

Use the `uri` field in each row to point to the Cloud Storage location of the document. 

Here is an example of an NDJSON metadata file for an unstructured document. In this example, each line of the metadata file points to a PDF document and contains the metadata for that document. The first two lines use `jsonData` and the second two lines use `structData` . With `structData` you don't need to escape quotation marks that appear within quotation marks. 

```
{"id":"doc-0","jsonData":"
{\"title\":\"test_doc_0\",\"uri\":\"https://test_doc_0.html\",\"description\":\
"This document uses a blue color theme\",\"color_theme\":\"blue\"}","content":
{"mimeType":"application/pdf","uri":"gs://test-bucket-
12345678/test_doc_0.pdf"}}
{"id":"doc-1","jsonData":"
{\"title\":\"test_doc_1\",\"uri\":\"https://test_doc_1.html\",\"description\":\
"This document uses a green color
theme\",\"color_theme\":\"green\"}","content":
{"mimeType":"application/pdf","uri":"gs://test-bucket-
12345678/test_doc_1.pdf"}}
{"id":"doc-2","structData":
{"title":"test_doc_2","uri":"https://test_doc_2.html","description":"This
document uses a red color theme","color_theme":"red"},"content":
{"mimeType":"application/pdf","uri":"gs://test-bucket-
12345678/test_doc_3.pdf"}}
{"id":"doc-3","structData":
{"title":"test_doc_3","uri":"https://test_doc_3.html","description":"This is
document uses a yellow color theme","color_theme":"yellow"},"content":
{"mimeType":"application/pdf","uri":"gs://test-bucket-
12345678/test_doc_4.pdf"}}
```

To create your data store, see Connect a Google data source 

(/gemini/enterprise/docs/create-data-store). 

#### BigQuery

If you plan to import metadata from BigQuery, follow these steps: 

1. Create a BigQuery table that contains metadata. The document ID is an example of metadata. 

2. Put your unstructured documents into a Cloud Storage bucket. 

You can import using Google Cloud console 

(/gemini/enterprise/docs/connectors/connect-cloud-storage), by the `ImportDocuments` method, or by streaming ingestion through CRUD methods. For API reference information, see `DocumentService` 

(/gemini/enterprise/docs/reference/rpc/google.cloud.discoveryengine.v1#documentservi ce) 

and `documents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.bran ches.documents) 

Use the following BigQuery schema. Use the `uri` field in each record to point to the Cloud Storage location of the document. 

```
[
 {
   "name": "id",
   "mode": "REQUIRED",
   "type": "STRING",
   "fields": []
 },
 {
   "name": "jsonData",
   "mode": "NULLABLE",
   "type": "STRING",
   "fields": []
 },
 {
   "name": "content",
   "type": "RECORD",
   "mode": "NULLABLE",
   "fields": [
     {
       "name": "mimeType",
       "type": "STRING",
       "mode": "NULLABLE"
     },
     {
       "name": "uri",
       "type": "STRING",
       "mode": "NULLABLE"
     }
   ]
 }
]
```

For more information, see Create and use tables (/bigquery/docs/tables) in the BigQuery documentation. 

To create your data store, see Connect a Google data source (/gemini/enterprise/docs/create-data-store). 

#### Google Drive

Syncing data from Google Drive is supported for search. 

If you plan to import data from Google Drive, you must set up Google Identity as your identity provider in Gemini Enterprise. For information about setting up access control, see Identity and permissions (/gemini/enterprise/docs/identity). 

To create your data store, see Connect a Google data source 

(/gemini/enterprise/docs/create-data-store). 

### Structured data

Prepare your data according to the import method that you plan to use. 

You can import structured data from the following sources: 

- BigQuery (#bigquery-structured) 

- Cloud Storage (#storage-structured) 

- Local JSON data (#json-data-api) 

When you import structured data from BigQuery or from Cloud Storage, you are given the option to import the data with metadata. (Structured with metadata is also referred to as _enhanced structured data_ .) 

#### BigQuery

You can import structured data from BigQuery datasets. 

Your schema is auto-detected. After importing, Google recommends that you edit the auto-detected schema to map key properties, such as titles. If you import using the API instead of the Google Cloud console, you have the option to provide your own schema as a JSON object. For more information, see Provide or auto-detect a schema (/gemini/enterprise/docs/provide-schema). 

For examples of publicly available structured data, see the BigQuery public datasets (/bigquery/public-data). 

If you plan to include embeddings in your structured data, see Use custom embeddings (/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation. 

If you select to import structured data with metadata, you include two fields in your BigQuery tables: 

- An `id` field to identify the document. If you import structured data without metadata, then the `id` is generated for you. Including metadata lets you specify the value of `id` . 

- A `jsonData` field that contains the data. For examples of `jsonData` strings, see the preceding section Cloud Storage (#storage-unstructured). 

Use the following BigQuery schema for structured data with metadata imports: 

```
[
 {
   "name": "id",
   "mode": "REQUIRED",
   "type": "STRING",
   "fields": []
 },
 {
   "name": "jsonData",
   "mode": "NULLABLE",
   "type": "STRING",
   "fields": []
 }
]
```

To create your data store, see Connect a Google data source (/gemini/enterprise/docs/create-data-store). 

**Notes** : 

- You can't import from BigQuery tables that have external data sources. For information about external data sources in BigQuery, see Introduction to external tables 

- (/bigquery/docs/external-tables) in the _BigQuery documentation_ . 

- If your BigQuery tables contain columns with flexible column names, those columns aren't imported. For information about flexible column names, see Flexible column names (/bigquery/docs/schemas#flexible-column-names) in the _BigQuery documentation_ . 

#### Cloud Storage

Structured data in Cloud Storage must be in either JSON Lines (https://jsonlines.org/) or NDJSON format. Each file must be less than 2 GB, and each row of the file less than 1 MB. You can import up to 1,000 files in a single import request. 

For examples of publicly available structured data, refer to the following folders in Cloud Storage, which contain NDJSON files: 

- `gs://cloud-samples-data/gen-app-builder/search/kaggle_movies` 

- `gs://cloud-samples-data/gen-app-builder/search/austin_311` 

If you plan to include embeddings in your structured data, see Use custom embeddings (/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation. 

Here is an example of an NDJSON metadata file of structured data. Each line of the file represents a document and is made up of a set of fields. 

```
{"id": 10001, "title": "Hotel 1", "location": {"address": "1600 Amphitheatre
Parkway, Mountain View, CA 94043"}, "available_date": "2024-02-10",
"non_smoking": true, "rating": 3.7, "room_types": ["Deluxe", "Single",
"Suite"]}
{"id": 10002, "title": "Hotel 2", "location": {"address": "Manhattan, New York,
NY 10001"}, "available_date": "2023-07-10", "non_smoking": false, "rating":
5.0, "room_types": ["Deluxe", "Double", "Suite"]}
{"id": 10003, "title": "Hotel 3", "location": {"address": "Moffett Park,
Sunnyvale, CA 94089"}, "available_date": "2023-06-24", "non_smoking": true,
"rating": 2.5, "room_types": ["Double", "Penthouse", "Suite"]}
```

To create your data store, see Connect a Google data source (/gemini/enterprise/docs/create-data-store). 

#### Local JSON data

You can directly upload a JSON document or object using the API. 

Google recommends providing your own schema as a JSON object for better results. If you don't provide your own schema, the schema is auto-detected. After importing, we recommend that you edit the auto-detected schema to map key properties, such as titles. For more information, see Provide or auto-detect a schema (/gemini/enterprise/docs/provide-schema). 

If you plan to include embeddings in your structured data, see Use custom embeddings (/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation. 

To create your data store, see Connect a Google data source (/gemini/enterprise/docs/create-data-store). 

Last updated 2026-10-14 UTC. 



## Create a data store: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store

This page describes how to create a data store for Google data sources, such as Cloud Storage or Google Drive. 

**Note:** Google Workspace data sources, such as Google Drive, Gmail, Google Calendar, and Google Chat, require a Google Workspace organization account and a Customer ID. Personal Google Accounts (consumer accounts ending in **`@gmail.com`** ) don't have a customer ID and aren't supported for data connectors. 

To import data from a third-party data source, see Connect a third-party data source (/gemini/enterprise/docs/connect-third-party-data-source). 

#### Generally Available

- Connect to BigQuery (/gemini/enterprise/docs/connectors/connect-bigquery) (ingestion mode) 

- Import from Cloud Storage 

- (/gemini/enterprise/docs/connectors/connect-cloud-storage) 

- Sync from Google Drive (/gemini/enterprise/docs/connectors/gdrive) 

- Sync from Gmail (/gemini/enterprise/docs/connectors/gmail) 

- Sync from Google Calendar (/gemini/enterprise/docs/connectors/gcal) 

- Connect to Google Sites (/gemini/enterprise/docs/connectors/connect-sites) 

- Sync people data (/gemini/enterprise/docs/connectors/connect-people) 

- Connect to Cloud SQL (/gemini/enterprise/docs/connectors/connect-cloud-sql) (ingestion mode) 

- Connect to Spanner (/gemini/enterprise/docs/connectors/connect-spanner) (ingestion mode) 

- Import from Firestore (/gemini/enterprise/docs/connectors/connect-firestore) 

- Import from Bigtable (/gemini/enterprise/docs/connectors/connect-bigtable) 

- Connect toAlloyDB for PostgreSQL 

- (/gemini/enterprise/docs/connectors/connect-alloydb) (ingestion mode) 

- Create a data store using Terraform 

- (/gemini/enterprise/docs/connectors/connect-terraform) 

#### Public Preview

- Sync from Google Chat (/gemini/enterprise/docs/connectors/gchat) (Preview) 

- Import from Compute Engine 

- (/gemini/enterprise/docs/connectors/google-compute-engine) (Preview) 

- Connect Google Stitch with data federation 

- (/gemini/enterprise/docs/connectors/googlestitch) (Preview) 

- Sync from Google Groups (/gemini/enterprise/docs/connectors/connect-groups) (Preview) 

- Import people data from a custom source 

- (/gemini/enterprise/docs/connectors/connect-people-custom) (Preview) 

- Enable Gemini Notebook Enterprise as a search source 

- (/gemini/enterprise/docs/connectors/connect-notebooklm) (Preview) 

- Connect to data from AlloyDB for PostgreSQL 

- (/gemini/enterprise/docs/connectors/connect-alloydb-data) (Preview) 

- Connect to data from BigQuery using federated query 

- (/gemini/enterprise/docs/connectors/connect-bigquery) (Preview) 

- Connect to data from Spanner using federated query 

- (/gemini/enterprise/docs/connectors/connect-spanner) (Preview) 

- Connect to data from Cloud SQL using federated query 

- (/gemini/enterprise/docs/connectors/connect-cloud-sql) (Preview) 

- Connect to data from AlloyDB for PostgreSQL using federated query 

- (/gemini/enterprise/docs/connectors/connect-alloydb) (Preview) 

- Use Knowledge Catalog with federated query connectors 

- (/gemini/enterprise/docs/connectors/connect-knowledge-catalog) (Preview) 

### Supported actions

Expand the data store name in the following list to reveal the available actions for each. 

**Note:** Not all Google data stores support actions (for example, Google Sites is ingestion-only and doesn't support actions). 

Google Calendar 

|Launch<br>date|Action|Description|
|---|---|---|
|9/1/26|Create event|Creates a new Google Calendar event.|
||Delete event|Deletes an existing Google Calendar event.|
||Get event|Fetches a Google Calendar event by ID.|
||List calendars|Lists calendars in the user's Google Calendar account.|
||List events|Lists events from a Google Calendar.|
||Respond to<br>event|Responds to a Google Calendar event invitation.|
||Search events|Searches for Google Calendar events matching a query.|
||Suggest time|Suggests a meeting time based on attendees' free/busy<br>data.|
||Update event|Updates an existing Google Calendar event.|

Google Chat 

|Launch<br>date|Action|Description|
|---|---|---|

|9/1/26|Add membership|Adds a member to a Google Chat conversation.|
|---|---|---|
||Add reaction|Adds a reaction to a Google Chat message.|
||Create<br>conversation|Creates a Google Chat conversation (named space, direct<br>message, or group direct message).|
||List memberships|Lists memberships in a Google Chat conversation.|
||List messages|Retrieves messages from a specified Google Chat<br>conversation (space, direct message, or group direct<br>message).|
||List messages<br>(Markdown)|Retrieves messages from a specified Google Chat<br>conversation in Markdown format.|
||Remove<br>membership|Removes a user membership from a Google Chat<br>conversation.|
||Remove reaction|Removes a reaction from a Google Chat message.|
||Search<br>conversations|Searches for Google Chat conversations by display name.|
||Search messages|Searches for Google Chat messages using keywords and<br>filters. Works across all spaces the user has access to, or<br>can be scoped to a specific conversation.|
||Send message|Sends a Google Chat message to a conversation.|
||Send message<br>(Markdown)|Sends a Google Chat message to a conversation with<br>Markdown formatting.|
|Gmai|Update<br>membership<br>l|Updates a user membership in a Google Chat<br>conversation.|
|Launch<br>date|Action|Description|

|9/1/26|Batch label<br>messages|Adds one or more labels to multiple Gmail messages<br>in a single request.|
|---|---|---|
||Batch label threads|Adds one or more labels to multiple Gmail threads in a<br>single request.|
||Batch unlabel<br>messages|Removes one or more labels from multiple Gmail<br>messages in a single request.|
||Batch unlabel<br>threads|Removes one or more labels from multiple Gmail<br>threads in a single request.|
||Create draft|Creates a new Gmail draft.|
||Create filter|Creates a new Gmail filter.|
||Create label|Creates a new label in Gmail.|
||Delete filter|Deletes an existing Gmail filter.|
||Delete label|Deletes an existing Gmail label.|
||Forward|Forwards an existing Gmail message.|
||Get message<br>attachment|Fetches metadata for an attachment on a Gmail<br>message.|
||Get thread|Fetches the full contents of a Gmail thread.|
||Label message|Adds one or more existing labels to a specific Gmail<br>message.|
||Label thread|Adds one or more existing labels to a specific Gmail<br>thread.|
||List drafts|Lists Gmail drafts in the user's mailbox.|
||List filters|Lists Gmail filters in the user's mailbox.|
||List labels|Lists labels defined in the user's Gmail mailbox.|
||List threads|Lists Gmail threads in the user's mailbox.|
||Reply|Replies to an existing Gmail message.|
||Search threads|Searches for Gmail threads matching a query.|
||Send message|Sends a new Gmail message.|

|Unlabel message|Removes one or more existing labels from a specific<br>Gmail message.|
|---|---|
|Unlabel thread|Removes one or more existing labels from a specific<br>Gmail thread.|
|Update draft|Updates an existing Gmail draft.|
|Update label|Updates an existing Gmail label.|

Google Drive 

|Launch<br>date|Action|Description|
|---|---|---|
|9/1/26|Copy file|Copies a file in Google Drive.|
||Create file|Creates a new file in Google Drive.|
||Download file<br>content|Downloads the content of a Google Drive file.|
||Get file metadata|Fetches metadata for a Google Drive file.|
||Get file<br>permissions|Lists the permissions on a Google Drive file.|
||List recent files|Lists recent files in Google Drive.|
||List shared drives|Lists shared drives in Google Drive.|
||Read file content|Reads the contents of a Google Drive file.|
||Search files|Searches for Google Drive files matching a query.|
||Share file|Shares a Google Drive file with one or more users.|
||Trash file|Moves a Google Drive file to the trash.|
||Update file|Updates an existing Google Drive file.|

|10/12/26|Get cell values|Reads cell values from a Google Sheets spreadsheet.|
|---|---|---|
||Get spreadsheet|Reads the contents and metadata of a Google Sheets<br>spreadsheet.|
||Insert dimension|Inserts rows or columns into a Google Sheets<br>spreadsheet.|
||Read document|Reads the contents of a Google Docs document.|
||Read presentation|Reads the contents of a Google Slides presentation.|
||Update cell values|Writes cell values to a Google Sheets spreadsheet.|
||Update formulas|Writes formulas to a Google Sheets spreadsheet.|

Google Stitch 

|Launch date|Action|Description|
|---|---|---|
|6/5/26|Create project|Creates a new Stitch project.|
||Update design system|Updates a design system.|
|6/23/26|Apply design system|Applies a design system to a project.|
||Create design system|Creates a new design system.|
|7/29/26|Edit screens|Edits screens.|

### Troubleshoot data ingestion

If you're using customer-managed encryption keys (/gemini/enterprise/docs/cmek) and data import fails (with error message `The caller does not have permission` ), then make sure that the CryptoKey Encrypter/Decrypter IAM role ( `roles/cloudkms.cryptoKeyEncrypterDecrypter` ) on the key has been granted to the Cloud Storage service agent. For more information, see Before you begin 

(/gemini/enterprise/docs/cmek#before-you-begin) in "Customer-managed encryption keys". 

Last updated 2026-10-15 UTC. 



## Google Calendar connector: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal

The Google Calendar connector for Gemini Enterprise lets you search and perform actions on your events and calendars. 

**Note:** Gemini Enterprise has released new Google Workspace data connectors for Google Calendar, Google Drive, Gmail, and Google Chat. The new connectors use a Google-managed OAuth app, so you no longer create your own OAuth client or supply a client ID and client secret when you create the data store. For Google Calendar setup instructions, see Set up a Google Calendar connector (/gemini/enterprise/docs/connectors/gcal/set-up-data-store). 

### Supported Google Calendar versions

The Google Calendar data store supports Google Calendar version v3 and later. 

### Supported actions

When the Google Calendar data store is enabled, end users can use natural language commands in Gemini Enterprise to perform the following actions. 

|Action|Description|
|---|---|
|Create event|Creates a new Google Calendar event.|
|Update event|Updates an existing Google Calendar event.|
|Delete event|Deletes an existing Google Calendar event.|
|Get event|Fetches a Google Calendar event by ID.|
|Respond to event|Responds to a Google Calendar event invitation.|
|List events|Lists events from a Google Calendar.|
|Search events|Searches for Google Calendar events matching a query.|

|Action|Description|
|---|---|
|List calendars|Lists calendars in the user's Google Calendar account.|
|Suggest time|Suggests a meeting time based on attendees' free/busy data.|
|**Notes**:||
|Google Ca   i|lendar doesn't support file uploads and downloads.|

#### Required scopes

The Google-managed OAuth app requests the following OAuth scopes. Users grant these scopes when they authorize the connector: 

|Scope|Purpose|
|---|---|
|`https://www.googleapis.com/auth/calendar.`<br>`calendarlist.readonly`|List calendars in the user's Google Calendar<br>account.|
|`https://www.googleapis.com/auth/calendar.`<br>`events.readonly`|Read and search Google Calendar events.|
|`https://www.googleapis.com/auth/calendar.`<br>`readonly`|Read Google Calendar metadata and event<br>attachments.|
|`https://www.googleapis.com/auth/calendar.`<br>`events`|Create, update, delete, and respond to<br>Google Calendar events.|
|`https://www.googleapis.com/auth/calendar.`<br>`events.freebusy`|Query attendees' free/busy data to suggest<br>meeting times.|
|`https://www.googleapis.com/auth/calendar.`<br>`freebusy`|Query free/busy information for a calendar.|
|`https://www.googleapis.com/auth/calendar`|Perform write operations on Google Calendar<br>data.|

### Limitations

- The Google Calendar data store is supported only in the `global` , `us` , and `eu` locations. 

- When creating a new app or adding a data store to an existing one, it's recommended to associate only one data store with actions belonging to a single connector type. 

- If you use security controls, be aware of their limitations related to data in Google Calendar, as discussed in the following table: 

|Security control|Note the following|
|---|---|
|Data Residency (DRZ)<br>(/gemini/enterprise/docs/locations|)<br>Gemini Enterprise only guarantees data residency in<br>Google Cloud. For information about data residency an<br>Google Calendar, see Google Workspace compliance<br>guidance and documentation, including<br>Data regions fo<br>Google Workspace<br>(https://support.google.com/a/answer/9223653). Also<br>review examples like<br>Choose the region where data is<br>stored(https://support.google.com/a/topic/7631290) a<br>Digital sovereignty<br>(https://workspace.google.com/intl/en_in/security/digit<br>sovereignty/)<br>.|
|Customer-managed encryption<br>keys (CMEK)<br>(/gemini/enterprise/docs/cmek)|Your keys only encrypt data within Google Cloud. Cloud<br>Key Management Service controls don't apply to data<br>stored in Google Calendar.|
|Access Transparency<br>(/gemini/enterprise/docs/access-<br>transparency)|Access Transparency logs actions taken by Google<br>personnel on the Google Cloud project. You'll also need<br>to review the Access Transparency logs created by<br>Google Workspace. For more information, see<br>Access<br>Transparency log events<br>(https://support.google.com/a/answer/9230979) in the<br>Google Workspace Admin Help documentation.|

### What's next

- To create and configure a connector with Google Calendar, see Set up a Google Calendar connector 

(/gemini/enterprise/docs/connectors/gcal/set-up-data-store). 

Last updated 2026-10-14 UTC. 



## Set up a Google Calendar data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/gcal/set-up-data-store

This page describes how to create a data store and connect Google Calendar to Gemini Enterprise. 

### Before you begin

- Sign in to the Google Cloud console with the same account that you use for the Google Workspace instance that you plan to connect. Gemini Enterprise uses your Google Workspace customer ID to connect to Google Calendar. Personal Google Accounts (consumer accounts ending in `@gmail.com` ) don't have a customer ID and aren't supported. 

- To enforce data source access control and secure data in Gemini Enterprise, ensure that you have configured your identity provider 

- (/gemini/enterprise/docs/configure-identity-provider). 

- **Enable smart features** : In your Google Workspace account, turn on both **Smart features in Google Workspace** and **Smart features in other Google products** . For details, see Turn Google Workspace smart features on or off (https://support.google.com/mail/answer/15604322). 

- **Allowlist the OAuth app (Administrators only)** : The Google Calendar data store uses a Google-managed OAuth app to access your data. If your organization restricts OAuth app access, your Google Workspace administrator must add this app to your organization's allowlist. For details, see Allowlist the Google-managed OAuth app 

- (/gemini/enterprise/docs/connectors/gcal/config#allowlist-oauth-app). 

#### Create the Google Calendar data store

To create the Google Calendar data store, perform the following steps: 

1. In the Google Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select or create (/resource-manager/docs/creating-managing-projects) a Google Cloud project. 

3. In the navigation menu, click **Data stores** . 

4. Click **Create data store** . 

5. In the **Source** , search for **Google Calendar** , and click **Select** . 

6. In the **Actions** section, choose the actions from the list to enable them for Google Calendar connector. 

**Note:** If you skip adding actions in this step, you can add them later. For more information, see Add actions (/gemini/enterprise/docs/manage-actions#add-actions). 

To view and manage the list of actions, see View and manage actions (/gemini/enterprise/docs/manage-actions). 

7. Click **Continue** . 

8. In the **Configuration** section: 

   - a. From the **Multi-region** list, select the location for your data connector. 

   - b. In the **Data connector name** field, enter a name for your connector. 

   - c. If you selected `us` or `eu` as the location, configure the **Encryption settings** : 

      - Select **Google-managed encryption key** or **Cloud KMS key** . If you selected **Cloud KMS key** : 

         - In the **Key management type** list, select the appropriate type. 

In the **Cloud KMS key** list, select the key. 

For more information, see Customer-managed encryption keys (/gemini/enterprise/docs/cmek). 

9. Optional: In the **Tag** field, enter a stable identifier for the data store. This identifier is used across different versions of the connector and becomes 

immutable after the data store is created, so choose a value that you don't need to change later. 

10. Optional: In the **Sensitive Data Protection policy** section, attach an existing Sensitive Data Protection 

   - (/sensitive-data-protection/docs/sensitive-data-protection-overview) policy to inspect and de-identify data that Gemini Enterprise retrieves through this data store. If your organization doesn't require a Sensitive Data Protection policy, you can skip this step. 

11. Click **Create** . Gemini Enterprise creates your data store and displays your data stores on the **Data Stores** page. 

On the **Data Stores** page, click your data store name to see the status. When the data store state changes from **Creating** to **Active** , the Google Calendar connector is ready to be used. 

After creating the data store, create an app (/gemini/enterprise/docs/create-app) and connect it to the Google Calendar data store 

(/gemini/enterprise/docs/connect-existing-data-store) before executing the query. 

### Query execution

After you authorize Google Calendar, when you enter a search query: 

1. Gemini Enterprise sends your search query to the Google Calendar API. 

2. Gemini Enterprise blends the results with those from other sources and displays them. 

### Error messages and troubleshooting

The following table describes error messages, including HTTP error codes and suggested troubleshooting steps, that you might encounter when working with this Google data source. 

|Error code|Error message|Description|Troubleshooting|
|---|---|---|---|
|403<br>Permission<br>Denied|Searching<br>using service<br>account<br>credentials<br>isn't supported<br>for Google<br>Workspace<br>data stores.|<br>The engine being<br>searched has<br>Google<br>Workspace data<br>stores, and the<br>credentials<br>passed are of a<br>service account.<br>Searching using<br>service account<br>credentials on<br>Google<br>Workspace data<br>stores isn't<br>supported.|<br>Call search using user credentials, or remove<br>Google Workspace data stores from the engine.|
|403<br>Permission<br>Denied|Consumer<br>accounts<br>aren't<br>supported for<br>Google<br>Workspace<br>data stores.|Search is called<br>using a<br>consumer<br>account<br>(@gmail.com)<br>credential, which<br>isn't supported<br>for Google<br>Workspace data<br>stores.|<br>Remove Google Workspace data stores from the<br>engine or use a managed Google Account.|
|403<br>Permission<br>Denied|Customer id<br>mismatch for<br>data store|Search is only<br>allowed for users<br>who belong to<br>same<br>organization as<br>Google<br>Workspace data<br>stores.|<br>Remove Google Workspace data stores from the<br>engine or contact support if the user and Google<br>Workspace data stores are meant to be in different<br>organizations.|

|Error cod|e Error message|Description|Troubleshooting|
|---|---|---|---|
|403|Workspace|A Google|Contact your Google Workspace administrator to|
|Permissio|n<br>access for|Workspace|[enable access]|
|Denied|Agentspace<br>disabled by<br>organization<br>administrator.|administrator<br>has disabled<br>access to Google<br>Workspace data<br>for Gemini|<br>(https://support.google.com/a/answer/16479199).|
|||Enterprise.||

### What's next

- To provide a user interface for querying your Google Calendar data, create an app (/gemini/enterprise/docs/create-app) and connect it to the Google Calendar data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To view and manage the list of actions you enabled for the Google Calendar data store, see View and manage actions (/gemini/enterprise/docs/manage-actions) 

- To preview how your search results appear after your app is set up, see Get search results (/gemini/enterprise/docs/preview-search-results). 

- To enable alerts for the data store, see Configure alerts for third-party data stores (/gemini/enterprise/docs/configure-periodic-data-alerts). 

Last updated 2026-10-14 UTC.
