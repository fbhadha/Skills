# Gemini Enterprise: connectors and data stores / Configure allowed data sources to Troubleshoot data stores
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 654-699, extracted 2026-10-18

Contains:
- Configure allowed data sources (pages 654-656) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources
- Configure allowed egress FQDNs (pages 657-659) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns
- Custom connectors: overview (pages 660-663) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-connector
- Create a custom connector (pages 664-684) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-custom-connector
- Connect an app to an existing data store (pages 685-687) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-existing-data-store
- Manage actions (pages 688-691) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/manage-actions
- Troubleshoot data stores (pages 692-699) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/troubleshoot-data-stores

## Configure allowed data sources

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-data-sources

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

The `discoveryengine.managed.allowedDataSources` managed organization policy constraint, also known as **Restrict allowed data sources for data connectors** , lets you control which external data sources (such as Jira, Box, or Confluence) are permitted when adding a data store in Gemini Enterprise. 

### Before you begin

- Ensure you have the **Organization Policy Administrator** role ( `roles/orgpolicy.policyAdmin` ). 

**Note:** This role might only be available to project owners and is only applicable if your project is part of an organization. 

- Understand the policy enforcement dependencies and interactions. See Overview of managed policy constraints 

- (/gemini/enterprise/docs/connectors/managed-policy-constraints-overview). 

### Configure the constraint

To configure the allowed data sources, follow these steps: 

1. In the Google Cloud console, go to the **Organization Policies** page. 

Go to Organization Policies (https://console.cloud.google.com/iam-admin/orgpolicies) 

2. In the project selector, choose the organization or project where you want to change policy enforcement. 

3. In the **Filter** field, enter `discoveryengine.managed.allowedDataSources` or `Restrict allowed data sources for data connectors` . 

4. Click the policy name to open its details. 

5. Click **Manage Policy** . 

6. Select **Override parent's policy** . 

7. Set **Enforcement** to **On** . 

8. Edit the `allowedDataSources` parameter: 

   - a. Click edit next to `allowedDataSources` . 

   - b. Set **Value Type** to **User-defined** . 

   - c. Add values, such as `jira` , `box` , or `custom_mcp` . For a complete list, see Supported Data Sources (#supported-data-sources). 

9. **Optional** : To enforce this policy on specific projects not in VPCSC, update the `enforcedProjects` parameter and add the project names in the format `projects/<project_name>/` . 

10. Click **Set Policy** . 

#### Supported data sources

For the canonical list of supported `dataSource` values that you can add to the `allowedDataSources` parameter, see the tables in Connect a third-party data source (/gemini/enterprise/docs/connectors/connect-third-party-data-source#sources-by-launchstage) 

. Use the values from the **Value for** **`allowedDataSources`** column exactly as they appear. 

### Verify the policy change

Verify the policy by attempting to create a data store. If the configuration is correct, you can create the data store without an `Operation denied by org policy` error related to `discoveryengine.managed.allowedDataSources` . 

### What's next

- To connect your data sources, see Connect a Google data source (/gemini/enterprise/docs/create-data-store) and Connect a third-party data source (/gemini/enterprise/docs/connect-third-party-data-source). 

- To create custom organization policies with fine-grained rules for your data connectors or data stores, see Manage resources with custom organization policies (/gemini/enterprise/docs/org-policy-custom-constraints). 

Last updated 2026-10-14 UTC. 



## Configure allowed egress FQDNs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-allowed-egress-fqdns

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

The **Restrict egress domains for data connectors** managed organization policy constraint lets you specify which fully qualified domain names (FQDNs) are permitted when adding a data store in Gemini Enterprise. The domains you need to add typically include the domain names extracted from the instance URL, authorization URL, and token URL provided when provisioning a data store. For example, if the authorization URL is `https://api.cymbal.com/oauth/authorize` , you only need to allowlist `api.cymbal.com` . 

### Before you begin

Ensure you have the **Organization Policy Administrator** role ( `roles/orgpolicy.policyAdmin` ). 

**Note:** This role might only be available to project owners and is only applicable if your project is part of an organization. 

Understand the policy enforcement dependencies and interactions. See Overview of managed policy constraints 

(/gemini/enterprise/docs/connectors/managed-policy-constraints-overview). 

### Configure the constraint

To configure the allowed egress FQDNs, follow these steps: 

1. In the Google Cloud console, go to the **Organization Policies** page. 

Go to Organization Policies (https://console.cloud.google.com/iam-admin/orgpolicies) 

2. In the project selector, choose the organization or project where you want to change policy enforcement. 

3. In the **Filter** field, enter `discoveryengine.managed.allowedEgressFqdns` or `Restrict egress domains for data connectors` . 

4. To open the policy details page, click the policy name. 

5. Click **Manage Policy** . 

6. Select **Override parent's policy** . 

7. Set **Enforcement** to **On** . 

8. Next to the `allowedEgressFqdns` parameter, click **Edit** . 

9. Change the **Value Type** to **User-defined** . 

10. Click **Add item** , and then enter each required fully qualified domain name (FQDN). Add only the domain (such as `api.cymbal.com` ), not the full URL. Repeat this step to add all required domains based on your data store type: 

**Note:** If your endpoints are hosted on different domains, add every domain to the list of permitted domains. Omitting required domains blocks outbound requests during OAuth sign-in, token exchange, and data syncs, causing connection and authentication checks to fail. 

|Data store type|Required domains|
|---|---|
|Custom MCP data stores|Add the domain of the MCP server URL, authorization URL, and<br>token URL.|
||For example, for an MCP server URL of`https://api.cymbal.`|
||`com/mcp`with authorization and token URLs on`auth.cymbal.`<br>`com`, add both`api.cymbal.com`and`auth.cymbal.com`.|

|Data store type|Required domains|
|---|---|
|All other data stores|Add the domain of the instance URL, authorization URL, and<br>token URL.|
||For example, if your authorization URL is`https://auth.`<br>`cymbal.com/oauth/authorize`, add`auth.cymbal.com`.|

11. Optional. To enforce the managed constraint on projects where VPCSC isn't enabled, click **Edit** next to the `enforcedProjects` parameter and add the project numbers. 

12. Click **Set Policy** . 

### Verify the policy change

After you apply the new configuration, verify that the policy status is updated. 

Verify the policy by attempting to create a data store. If the configuration is correct, you can create the data store without an `Operation denied by org policy` error related to `discoveryengine.managed.allowedEgressFqdns` . 

### What's next

- To connect your data sources, see Connect a Google data source (/gemini/enterprise/docs/create-data-store) and Connect a third-party data source (/gemini/enterprise/docs/connect-third-party-data-source). 

Last updated 2026-10-14 UTC. 



## Custom connectors: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/custom-connector

Custom connectors let you integrate external data sources that fall outside the Gemini Enterprise standard connector library, making your organization's unique data searchable and accessible using natural language, powered by Gemini and Google's advanced search intelligence. The custom connector interacts directly with the Discovery Engine API (/generative-ai-app-builder/docs/reference/rest), which enables robust data storage, indexing, and intelligent search capabilities. The connector converts the source information into the standardized JSON-based Document format 

(/generative-ai-app- 

builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents) (structuring the content, metadata, and Access Control Lists (ACLs)) and ensures this data is organized into Data stores 

(/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores). These stores act as logical repositories, ideally representing a single document format, each with its own dedicated search index and configurations. 

### How custom connectors work

Custom connectors work by using an automated data pipeline to perform three key actions: Fetch, Transform, and Sync. This process ensures external data is correctly prepared and uploaded to Gemini Enterprise. 

- Fetch: The connector pulls data, including documents, metadata, and permissions, from external system using its APIs, databases, or file formats. 

- Transform: The connector converts raw data into the document format of the Discovery Engine, structures the content and metadata, and assigns a globally unique ID to each document. For access controls, you can use either Google-recognized identities directly or identity mapping for external users or custom groups. 

- Sync: The connector uploads the documents to Gemini Enterprise data stores and keeps them updated through scheduled jobs. The data sync is performed using a data store created for an entity. For more information about creating data store, see Data store creation process (#data-store-creation-process). 

Choose a sync mode based on your needs: _Incremental_ adds and updates data, while _Full_ replaces the entire dataset. 

### ACLs and Identity mapping

To manage document-level access, choose between two methods — Pure ACLs or Identity Mapping, depending on the identity format used by the data. 

- Pure ACLs (AclInfo) 

- (/generative-ai-app- 

- builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.docume nts#Document.AclInfo) 

- : This method is used when the data source uses email-based identities recognized by (Google Cloud). This approach is ideal for directly defining who has access. 

- Identity mapping: This method is used when the data source uses usernames, legacy IDs, or other external identity systems: 

   - It establishes a clear and one-to-one association between external identity groups (e.g., EXT1) and internal Identity Provider (IDP) users or groups (e.g., `IDPUser1@example.com` ) . 

   - It allows the system to understand and apply group-based access controls from the source system, which is useful when an API returns group labels without full user memberships or for efficiently scaling ACLs without listing thousands of users per document. 

The identity mapping process requires resolving all nested or hierarchical identity structures into a flat list of direct mappings, typically in a specified JSON format. 

Use unique external identity group IDs (e.g., EXT1) for external identities to maintain system integrity. For more information and examples, see Map external identities (/gemini/enterprise/docs/identity-mapping). 

### Data store creation process

1. **Create the identity store:** This store acts as the parent resource for all identity mappings. Upon creation, project-level Identity Provider (IDP) settings are automatically fetched. For more information, see Retrieve or create identity store (/gemini/enterprise/docs/create-custom-connector#retrieve-initialize-is). 

2. **Load external identity mappings into identity store:** After creating the identity store, load the external identity data into it. For more information, see Ingest identity mapping into identity store 

   - (/gemini/enterprise/docs/create-custom-connector#ingest-im-into-is). 

3. **Create and bind the entity data store:** The entity data store can only be created _after_ the identity store is successfully created and the identity mappings are loaded. You must bind the identity store to the entity data store during its creation. For more information about creating entity data store, see Create data store (/gemini/enterprise/docs/create-custom-connector#create-ds). 

_Data store creation process._ 

#### Data sync

There are two different architecture models for syncing data: 

- **Architecture Model 1: Incremental upsert:** The incremental upsert approach is best suited for scenarios where data is streaming and requires real-time updates. The connector leverages the Discovery Engine API to perform efficient, incremental upserts (inserting or updating data) by calling the appropriate functions with small changes as they occur. This focus on minimal change sizes and minimal delay keeps the document store highly current, even with fast-changing data. 

**Architecture Model 2: Comprehensive sync with Google Cloud** 

**Storage:** This recommended approach offers a comprehensive set of data management features and high flexibility. It supports full syncs, which allow for data insertion, updating, and deletion across the entire dataset, and incremental syncs, which handle only inserts and updates by sending changes. This makes the approach robust for a wide range of data needs, 

particularly for managing larger or more complex data operations. This model utilizes a staging process (step 1 in the diagram) where the connector first writes the data to Google Cloud Storage (GCS), then leverages the Discovery Engine API to update the document store by calling the necessary import functions from the staged GCS location. 

Custom connectors are flexible enough to support a hybrid architecture, allowing you to implement incremental upsert for fast-changing data and comprehensive sync for scheduled full data updates or deletions. 

_Data sync options._ 

Last updated 2026-10-14 UTC. 



## Create a custom connector

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-custom-connector

This page describes how to create a custom connector. 

### Before you begin

Before you start, make sure you have the following: 

- Check whether billing is enabled on your Google Cloud project (/billing/docs/how-to/verify-billing-enabled). 

- Install (/sdk/docs/install) and initialize (/sdk/docs/initialize) the gcloud CLI. Ensure it is authenticated for your project. 

- Install the required Python libraries: 

```
pip install google-cloud-discoveryengine requests
```

- Obtain Discovery Engine administrator access for your Google Cloud project. 

- Obtain access credentials for your third-party data source (such as API keys or database authentication). 

- Create a clear data mapping plan. This must include which fields to index and how to represent access control including third-party identities. 

**Note:** Custom connectors can be configured for APIs that are available in seven different languages. This documentation uses Python for all code examples, but the underlying API calls and logic are consistent across every supported language. For more information about supported languages and client libraries, see Gemini Enterprise client libraries (/gemini/enterprise/docs/libraries). 

### Create basic connector

This section demonstrates creating a custom connector in your chosen language. The principles and patterns shown here apply to any external system. Simply adapt the API calls and data transformations for your specific source in your chosen language to create a basic connector. 

#### Fetch data

To get started, retrieve data from your third-party data source. In this example, we demonstrate how to fetch posts using pagination. For production environments, we recommend using a streaming approach for large datasets. This prevents memory issues that can occur when loading all the data at once. 

Python (#python) `from typing import List import requests def fetch_posts(base_url: str, per_page: int = 15) -> List[dict]: #Fetch all posts from the given site.# url = base_url.rstrip("/") + "/wp-json/wp/v2/posts" posts: List[dict] = [] page = 1 while True: resp = requests.get( url, params={"page": page, "per_page": per_page}, # headers={"Authorization": "Bearer YOUR_API_KEY"}, # Add auth if needed ) resp.raise_for_status() batch = resp.json() posts.extend(batch) if len(batch) < per_page: break page += 1 return posts` 

#### Transform data

To convert your source data into the Discovery Engine document format, structure it as shown in the following example payload. You can include as many key-value pairs as needed. For example, you can include the full content for a comprehensive search. Alternatively, you can include structured fields for a faceted search, or a combination of both. 

Python (#python) `from typing import List import json from google.cloud import discoveryengine_v1 as discoveryengine def convert_posts_to_documents(posts: List[dict]) -> List[discoveryengine.Document]: # Convert WP posts into Discovery Engine Document messages. docs: List[discoveryengine.Document] = [] for post in posts: payload = { "title": post.get("title", {}).get("rendered"), "body": post.get("content", {}).get("rendered"), "url": post.get("link"), "author": post.get("author"), "categories": post.get("categories"), "tags": post.get("tags"), "date": post.get("date"), } doc = discoveryengine.Document( id=str(post["id"]), json_data=json.dumps(payload), ) docs.append(doc) return docs` 

#### Retrieve or create identity store

To manage user identities and groups for access control, you must retrieve or create an identity store. This function gets an existing identity store by its ID, 

project, and location. If the identity store doesn't exist, it creates and returns a new, empty identity store. 

Python (#python) 

```
   from google.cloud import discoveryengine_v1 as discoveryengine
   def get_or_create_ims_data_store(
       project_id: str,
       location: str,
       identity_mapping_store_id: str,
   ) -> discoveryengine.DataStore:
     """Get or create a DataStore."""
     # Initialize the client
     client_ims = discoveryengine.IdentityMappingStoreServiceClient()
     # Construct the parent resource name
     parent_ims = client_ims.location_path(project=project_id,
location=location)
     try:
       # Create the request object
       name =
f"projects/{project_id}/locations/{location}/identityMappingStores/{identi
ty_mapping_store_id}"
       request = discoveryengine.GetIdentityMappingStoreRequest(
           name=name,
       )
       return client_ims.get_identity_mapping_store(request=request)
     except:
       # Create the IdentityMappingStore object (it can be empty for
basic creation)
       identity_mapping_store = discoveryengine.IdentityMappingStore()
       # Create the request object
       request = discoveryengine.CreateIdentityMappingStoreRequest(
           parent=parent_ims,
           identity_mapping_store=identity_mapping_store,
           identity_mapping_store_id=identity_mapping_store_id,
       )
       return client_ims.create_identity_mapping_store(request=request)
```

The get_or_create_ims_data_store function uses the following key variables: 

- `project_id` : The ID of your Google Cloud project. 

- `location` : The Google Cloud location for the identity mapping store. 

- `identity_mapping_store_id` : A unique identifier for the identity store. 

- `client_ims` : An instance of discoveryengine.IdentityMappingStoreServiceClient used to interact with the identity store API. 

- `parent_ims` : The resource name of the parent location, constructed using client_ims.location_path. 

- `name` : The full resource name of the identity mapping store, used for GetIdentityMappingStoreRequest. 

#### Ingest identity mapping into identity store

To load identity mapping entries into the specified identity store, use this function. It takes a list of identity mapping entries and initiates an inline import operation. This is crucial for establishing the user, group, and external identity relationships needed for access control and personalization. 

PythonPython  (#python) (#python) 

The load_ims_data function uses the following key variables: 

- `ims_store` : The discoveryengine.DataStore object representing the identity mapping store where data will be loaded. 

- `id_mapping_data` : A list of discoveryengine.IdentityMappingEntry objects, each containing an external identity and its corresponding user or group ID. 

- `result` : Return value of type discoveryengine.DataStore. 

#### Create data store

To use a custom connector, you must initialize a data store for your content. Use the `default_collection` for custom connectors. The `IndustryVertical` 

(/gemini/enterprise/docs/reference/rest/v1/IndustryVertical) parameter customizes the data store's behavior for specific use cases. `GENERIC` is suitable for most scenarios. However, you can choose a different value for a particular industry, such as `MEDIA` 

or `HEALTHCARE_FHIR` . Configure the display name and other properties to align with your project's naming conventions and requirements. 

Python (#python) 

```
from google.cloud import discoveryengine_v1 as discoveryengine
def get_or_create_data_store(
   project_id: str,
   location: str,
   display_name: str,
   data_store_id: str,
   identity_mapping_store: str,
) -> discoveryengine.DataStore:
 """Get or create a DataStore."""
 client = discoveryengine.DataStoreServiceClient()
 ds_name = client.data_store_path(project_id, location, data_store_id)
 try:
   result = client.get_data_store(request={"name": ds_name})
   return result
 except:
   parent = client.collection_path(project_id, location,
"default_collection")
   operation = client.create_data_store(
       request={
           "parent": parent,
           "data_store": discoveryengine.DataStore(
               display_name=display_name,
               acl_enabled=True,
industry_vertical=discoveryengine.IndustryVertical.GENERIC,
               identity_mapping_store=identity_mapping_store,
           ),
           "data_store_id": data_store_id,
       }
   )
   result = operation.result()
   return result
```

The get_or_create_data_store function uses the following key variables: 

- `project_id` : The ID of your Google Cloud project. 

- `location` : The Google Cloud location for the data store. 

- `display_name` : The human-readable display name for the data store. 

- `data_store_id` : A unique identifier for the data store. 

- `identity_mapping_store` : The resource name of the identity mapping store to bind. 

`result` : Return value of type discoveryengine.DataStore. 

#### Upload documents inline

To directly send documents to Discovery Engine, use inline upload. This method uses incremental reconciliation mode by default and doesn't support full reconciliation mode. In incremental mode, new documents are added and existing ones are updated, but documents no longer in the source are not deleted. Full reconciliation mode synchronizes the data store with your source data, including deleting documents that are no longer present in the source. 

Incremental reconciliation is ideal for systems like a CRM that handle frequent, small changes to data. Instead of syncing the entire database, only send specific changes, making the process faster and more efficient. 

As a best practice, perform an initial full synchronization, followed by more frequent incremental synchronizations. 

Python 

(#python) 

```
   from typing import List
   from google.cloud import discoveryengine_v1 as discoveryengine
   def upload_documents_inline(
       project_id: str,
       location: str,
       data_store_id: str,
       branch_id: str,
       documents: List[discoveryengine.Document],
   ) -> discoveryengine.ImportDocumentsMetadata:
       """Inline import of Document messages."""
       client = discoveryengine.DocumentServiceClient()
       parent = client.branch_path(
           project=project_id,
           location=location,
           data_store=data_store_id,
           branch=branch_id,
       )
       request = discoveryengine.ImportDocumentsRequest(
           parent=parent,
inline_source=discoveryengine.ImportDocumentsRequest.InlineSource(
               documents=documents,
           ),
       )
       operation = client.import_documents(request=request)
       operation.result()
       result = operation.metadata
       return result
```

The `upload_documents_inline` function uses the following key variables: 

- `project_id` : The ID of your Google Cloud project. 

- `location` : The Google Cloud location for the data store. 

- `data_store_id` : The ID of the data store. 

- `branch_id` : The ID of the branch within the data store (typically "0"). 

- `documents` : A list of discoveryengine.Document objects to be uploaded. 

- `result` : Return value of type discoveryengine.ImportDocumentsMetadata. 

The `uri` field within the `discoveryengine.Document` object is used to point to the ingested content source itself, either as raw bytes or a URI in Google Cloud Storage. This is different from the URI of the third-party source content. The URI of the third-party source content should be defined as a field within the document's `json_data` payload. For example, in the `convert_posts_to_documents` function, the `url` field in the payload serves this purpose. 

#### Validate your connector

To validate that your connector is working as expected, perform a test run to ensure proper data flow from the source to Discovery Engine. 

Python (#python) 

```
   from google.cloud import discoveryengine_v1 as discoveryengine
   from google.api_core import exceptions as gcp_exceptions
   SITE = "https://altostrat.com"
   PROJECT_ID = "ucs-3p-connectors-testing"
   LOCATION = "global"
   IDENTITY_MAPPING_STORE_ID = "your-unique-ims-id17" # A unique ID for
your new store
   DATA_STORE_ID = "my-acl-ds-id1"
   BRANCH_ID = "0"
   posts = fetch_posts(SITE)
   docs = convert_posts_to_documents(posts)
   print(f"Fetched {len(posts)} posts and converted to {len(docs)}
documents.")
   try:
     # Step #1: Retrieve an existing identity mapping store or create a
new identity mapping store
     ims_store = get_or_create_ims_data_store(PROJECT_ID, LOCATION,
IDENTITY_MAPPING_STORE_ID)
     print(f"STEP #1: IMS Store Retrieval/Creation: {ims_store}")
     RAW_IDENTITY_MAPPING_DATA = [
         discoveryengine.IdentityMappingEntry(
             external_identity="external_id_1",
             user_id="testuser1@example.com",
         ),
         discoveryengine.IdentityMappingEntry(
             external_identity="external_id_2",
             user_id="testuser2@example.com",
         ),
         discoveryengine.IdentityMappingEntry(
             external_identity="external_id_2",
             group_id="testgroup1@example.com",
         )
     ]
     # Step #2: Load IMS Data
     response = load_ims_data(ims_store, RAW_IDENTITY_MAPPING_DATA)
     print(
         "\nStep #2: Load Data in IMS Store successful.", response
     )
     # Step #3: Create Entity Data Store & Bind IMS Data Store
     data_store =  get_or_create_data_store(PROJECT_ID, LOCATION, "my-
acl-datastore", DATA_STORE_ID, ims_store.name)
     print("\nStep #3: Entity Data Store Create Result: ", data_store)
     metadata = upload_documents_inline(
         PROJECT_ID, LOCATION, DATA_STORE_ID, BRANCH_ID, docs
     )
     print(f"Uploaded {metadata.success_count} documents inline.")
   except gcp_exceptions.GoogleAPICallError as e:
     print(f"\n--- API Call Failed ---")
     print(f"Server Error Message: {e.message}")
     print(f"Status Code: {e.code}")
   except Exception as e:
     print(f"An error occurred: {e}")
```

Validate your connector code uses the following key variables: 

- `SITE` : The base URL of the third-party data source. 

- `PROJECT_ID` : Your Google Cloud project ID. 

- `LOCATION` : The Google Cloud location for the resources. 

- `IDENTITY_MAPPING_STORE_ID` : A unique ID for your Identity Mapping Store. 

- `DATA_STORE_ID` : A unique ID for your data store. 

- `BRANCH_ID` : The ID of the branch within the data store. 

- `posts` : Stores the fetched posts from the third-party source. 

- `docs` : Stores the converted documents in discoveryengine.Document format. 

- `ims_store` : The retrieved or created discoveryengine.DataStore object for identity mapping. 

`RAW_IDENTITY_MAPPING_DATA` : A list of discoveryengine.IdentityMappingEntry objects. 

Expected output: 

Shell (#shell) 

```
 Fetched 20 posts and converted to 20 documents.
 STEP #1: IMS Store Retrieval/Creation: "projects/ <Project
Number>/locations/global/identityMappingStores/your-unique-ims-id17"
 Step #2: Load Data in IMS Store successful.
 Step #3: Entity Data Store Create Result: "projects/ <Project
Number>/locations/global/collections/default_collection/dataStores/my-acl-
ds-id1"
 display_name: "my-acl-datastore"
 industry_vertical: GENERIC
 create_time {
   seconds: 1760906997
   nanos: 192641000
 }
 default_schema_id: "default_schema"
 acl_enabled: true
 identity_mapping_store: "projects/ <Project
Number>/locations/global/identityMappingStores/your-unique-ims-id17".
 Uploaded 20 documents inline.
```

You can also see your data store in the Google Google Cloud console at this point: 

_Custom connector data store._ 

When a search is performed, fields from the payload are used for the search, and the payload's URI field is used for citations. The three key property fields that Gemini Enterprise identifies are `title` , `description` , and `uri` . The corresponding 

document fields can have different names, and their mapping can be done by using the Schema -> Edit option in the Google Cloud console. 

### Create connector with Google Cloud Storage upload

While inline import works well for development, production connectors should use Google Cloud Storage for better scalability and to enable full reconciliation mode. This approach handles large datasets efficiently and supports automatic deletion of documents no longer present in the third-party data source. 

#### Convert documents to JSONL

To prepare documents for bulk import into Discovery Engine, convert them to JSON Lines format. 

Python (#python) 

```
   from typing import List
   from google.cloud import discoveryengine_v1 as discoveryengine
   def convert_documents_to_jsonl(
       documents: List[discoveryengine.Document],
   ) -> str:
       """Serialize Document messages to JSONL."""
       return "\n".join(
           discoveryengine.Document.to_json(doc, indent=None)
           for doc in documents
       ) + "\n"
```

The convert_documents_to_jsonl function uses the following variable: 

`documents` : A list of discoveryengine.Document objects to be converted. 

#### Upload to Google Cloud Storage

To enable efficient bulk import, stage your data in Google Cloud Storage. 

Python (#python) 

`from google.cloud import storage` (https://docs.cloud.google.com/python/docs/reference/storage/latest) 

`def upload_jsonl_to_gcs(jsonl: str, bucket_name: str, blob_name: str) -> str: """Upload JSONL content to Google Cloud Storage.""" client = storage` (https://docs.cloud.google.com/python/docs/reference/storage/latest) `.Client` (https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.stora ge.client.Client.html) `() bucket = client.bucket` (https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.stora ge.client.Client.html#google_cloud_storage_client_Client_bucket) `(bucket_name) blob = bucket.blob(blob_name) blob.upload_from_string` (https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.stora ge.blob.Blob.html#google_cloud_storage_blob_Blob_upload_from_string) `(jsonl, content_type="application/json") return f"gs://{bucket_name}/{blob_name}"` 

The upload_jsonl_to_gcs function uses the following key variables: 

`jsonl` : The JSONL formatted string content to be uploaded. 

`bucket_name` : The name of the Google Cloud Storage bucket. 

`blob_name` : The name of the blob (object) within the specified bucket. 

#### Import from Google Cloud Storage with full reconciliation

To perform a complete data synchronization using full reconciliation mode, use this method. This ensures your data store mirrors the third-party data source exactly, automatically removing any documents that no longer exist. 

**Note:** To allow Discovery Engine to read from your Google Cloud Storage bucket, you must grant the Discovery Engine service agent the **Storage Object Viewer** ( **`roles/storage.objectViewer`** ) role on the bucket. The service agent typically has the format **`service-{PROJECT_NUMBER}@gcp-sa-discoveryengine.iam.gserviceaccount.com`** . 

When importing from Google Cloud Storage, be aware of the following limitations: 

A single import request can contain at most 100 files, or 100,000 files if the `dataSchema` parameter is set to `content` . 

Each file can be up to 2 GB, or 100 MB if the `dataSchema` parameter is set to `content` . 

Python (#python) 

```
   from google.cloud import discoveryengine_v1 as discoveryengine
   def import_documents_from_gcs(
       project_id: str,
       location: str,
       data_store_id: str,
       branch_id: str,
       gcs_uri: str,
   ) -> discoveryengine.ImportDocumentsMetadata:
       """Bulk-import documents from Google Cloud Storage with FULL
reconciliation mode."""
       client = discoveryengine.DocumentServiceClient()
       parent = client.branch_path(
           project=project_id,
           location=location,
           data_store=data_store_id,
           branch=branch_id,
       )
       gcs_source = discoveryengine.GcsSource(input_uris=[gcs_uri])
       request = discoveryengine.ImportDocumentsRequest(
           parent=parent,
           gcs_source=gcs_source,
           reconciliation_mode=
               discoveryengine.ImportDocumentsRequest
               .ReconciliationMode.FULL,
       )
       operation = client.import_documents(request=request)
       operation.result()
       return operation.metadata
```

The import_documents_from_gcs function uses the following key variables: 

- `project_id` : The ID of your Google Cloud project. 

- `location` : The Google Cloud location for the data store. 

- `data_store_id` : The ID of the data store. 

- `branch_id` : The ID of the branch within the data store (typically "0"). 

- `gcs_uri` : The Google Cloud Storage URI pointing to the JSONL file. 

#### Test Google Cloud Storage upload

To verify the Google Cloud Storage-based import workflow, execute the following: 

Python 

(#python) 

```
 BUCKET = "your-existing-bucket"
 BLOB = "path-to-any-blob/wp/posts.jsonl"
 SITE = "https://altostrat.com"
 PROJECT_ID = "ucs-3p-connectors-testing"
 LOCATION = "global"
 IDENTITY_MAPPING_STORE_ID = "your-unique-ims-id17" # A unique ID for
your new store
 DATA_STORE_ID = "your-data-store-id"
 BRANCH_ID = "0"
 posts = fetch_posts(SITE)
 docs = convert_posts_to_documents(posts)
 print(f"Fetched {len(posts)} posts and converted to {len(docs)}
documents.")
 jsonl_payload = convert_documents_to_jsonl(docs)
 gcs_uri = upload_jsonl_to_gcs(jsonl_payload, BUCKET, BLOB)
 print("Uploaded to:", gcs_uri)
 metadata = import_documents_from_gcs(
     PROJECT_ID, LOCATION, DATA_STORE_ID, BRANCH_ID, gcs_uri
 )
 print(f"Imported: {metadata.success_count} documents")
```

The following key variables are used in testing the Google Cloud Storage upload: 

- `BUCKET` : The name of the Google Cloud Storage bucket. 

- `BLOB` : The path to the blob within the bucket. 

- `SITE` : The base URL of the third-party data source. 

- `PROJECT_ID` : Your Google Cloud project ID. 

- `LOCATION` : The Google Cloud location for the resources (e.g., "global"). 

- `IDENTITY_MAPPING_STORE_ID` : A unique ID for your Identity Mapping Store. 

- `DATA_STORE_ID` : A unique ID for your data store. 

- `BRANCH_ID` : The ID of the branch within the data store (typically "0"). 

- `jsonl_payload` : The documents converted to JSONL format. 

- `gcs_uri` : The Google Cloud Storage URI of the uploaded JSONL file. 

Expected output: 

Shell 

(#shell) 

```
   Fetched 20 posts and converted to 20 documents.
   Uploaded to: gs://alex-de-bucket/wp/posts.jsonl
   Imported: 20 documents
```

### Manage permissions

To manage document-level access in enterprise environments, Gemini Enterprise supports Access Control Lists (ACLs) and identity mapping, which help to limit what content users can see. 

#### Enable ACLs in data store

To enable ACLs when creating your data store, execute the following: 

Python (#python) `# get_or_create_data_store() "data_store": discoveryengine.DataStore( display_name=data_store_id, industry_vertical=discoveryengine.IndustryVertical.GENERIC, acl_enabled=True, # ADDED )` 

#### Add ACLs to documents

To compute and include AclInfo when transforming the documents, execute the following: 

Python 

(#python) 

```
 # convert_posts_to_documents()
 doc = discoveryengine.Document(
     id=str(post["id"]),
     json_data=json.dumps(payload),
     acl_info=discoveryengine.Document.AclInfo(
         readers=[{
             "principals": [
                 {"user_id": "baklavainthebalkans@gmail.com"},
                 {"user_id": "cloudysanfrancisco@gmail.com"}
             ]
         }]
     ),
 )
```

#### Make content public

To make a document publicly accessible, set the `readers` field as follows: 

Python (#python) 

```
 readers=[{"idp_wide": True}]
```

#### Validate ACLs

To validate that your ACL configurations are working as expected, consider the following: 

Search as a user who doesn't have access to the document. 

Inspect the uploaded document structure in Cloud Storage and compare it to a reference. 

<!-- Start of picture text -->
JSON<br>(#json)<br> {<br>   "id": "108",<br>   "jsonData": "{...}",<br>   "aclInfo": {<br>     "readers": [<br>       {<br>         "principals": [<br>           { "userId": "baklavainthebalkans@gmail.com" },<br>           { "userId": "cloudysanfrancisco@gmail.com" }<br>         ],<br>         "idpWide": false<br>       }<br>     ]<br>   }<br> }<br><!-- End of picture text -->

#### Use identity mapping

Use identity mapping for the following scenarios: 

- Your third-party data source uses non-Google identities 

- You want to reference custom groups (e.g., wp-admins) instead of individual users 

- Your API returns only group names 

- You need to manually group users for scale or consistency 

- Your third-party system implements ACLs using non-IDP based groups, and you want to honor those ACLs using the custom data store in Gemini Enterprise. 

To map identities (/gemini/enterprise/docs/identity-mapping), follow these steps: 

1. Create and link the identity data store. 

2. Import external identities (for example, `external_group:wp-admins` ) . Don't include the `external_group: prefix` when importing, for example: 

JSON (#json) `{ "externalIdentity": "wp-admins", "userId": "user@example.com" }` 

3. In the ACL info 

(/generative-ai-app- 

builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.docume nts#aclinfo) 

of your document 

(/generative-ai-app- 

builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.docume nts#resource:-document) 

, define the external entity ID in the `principal identifier` 

(/generative-ai-appbuilder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.docume nts#principal) 

. When referencing custom groups, use the `external_group:` prefix in the `groupId` field. 

4. The `external_group:` prefix is required for group IDs within the document's ACL info during import, but it is not used when importing identities to the mapping store. Example document with identity mapping: 

JSON (#json) `{ "id": "108", "aclInfo": { "readers": [ { "principals": [ { "userId": "cloudysanfrancisco@gmail.com" }, { "groupId": "external_group:wp-admins" } ] } ] }, "structData": { "id": 108, "date": "2025-04-24T18:16:04", ... } }` 

### What's next

To provide a user interface for querying your data, create an app (/gemini/enterprise/docs/create-app) in Gemini Enterprise and connect it to the existing _Custom connector_ data store 

- (/gemini/enterprise/docs/connect-existing-data-store). 

Last updated 2026-10-14 UTC. 



## Connect an app to an existing data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-existing-data-store

This page describes how to connect a data store to an app and authorize Gemini Enterprise for an existing data store. 

### Connect a data store to an app

**Note:** If you don't have an existing app, create one by following the steps in Create an app (/gemini/enterprise/docs/create-app). 

Console 

(#console) 

Follow these steps to connect an existing data store to your app: 

1. In the Google Cloud console, go to the **Gemini Enterprise page** (https://console.cloud.google.com/gemini-enterprise/start). 

2. From the navigation menu, click **Apps** . 

3. Select the Gemini Enterprise app where you want to connect your data store. 

4. From the navigation menu of the app, click **Connected data sources** . 

5. Click **Add existing data stores** and select your data store. 

6. Click **Connect** . 

### User authorization

To successfully connect and use data stores with your Gemini Enterprise app, ensure that you have authorized Gemini Enterprise to access data from your data store. 

Console 

(#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise page** (https://console.cloud.google.com/gemini-enterprise/start). 

2. From the navigation menu, click **Apps** . 

3. Select the Gemini Enterprise app that you have connected your data store to. 

4. Click the web app URL or copy it to open it in a new tab. 5. Select **Manage your data** . _Manage data_ 

<!-- Start of picture text -->
6. Authorize your data store:<br>For data stores with actions configured, click  Enable actions  and<br>then sign in to authorize your data store.<br>For search-only data stores, click  Authorize  and then sign in to<br>authorize your data store.<br>User authorization<br><!-- End of picture text -->

Last updated 2026-10-14 UTC. 



## Manage actions

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/manage-actions

You can add actions either during data store creation or later. This page provides steps to add new actions after data store creation, and manage the list of actions. 

**Note:** Users with data store configuration permissions can view its associated actions, provided that the data source includes default search or read-only actions, or that Gemini Enterprise has prebuilt actions for it. 

For more information, see the following: 

- Prebuilt actions supported for Google data stores: Google data store actions (/gemini/enterprise/docs/connectors/create-data-store#supported_actions) 

- Prebuilt actions supported for third-party data stores: Third-party data store actions (/gemini/enterprise/docs/connectors/connect-third-party-datasource#supported_actions) 

### Add actions

Console 

(#console) 

To add new actions to the data store, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Select a data store of your choice. 

4. From the navigation menu, select **Actions** . 

5. On the **Actions** page: 

- a. If actions were not added during data store creation, click **Enable actions** . Then, on the **Enable actions** page, to add new actions, do the following: 

For a federated data store: 

- i. Select the actions from the list. 

- ii. Click **Enable actions** . 

For an ingestion data store: 

- i. Expand the **Authentication settings** section and provide the authentication details. 

   - i. Click **Login** and sign in to the data store to verify your account. 

   - ii. Click **Continue** . 

- ii. Optional: Expand the **Advanced settings** and provide the necessary details. 

iii. Select the actions to enable. 

   - iv. Click **Enable actions** . 

- b. To add additional actions to the existing list, do the following: 

i. Select the actions from the list. 

      - ii. Click **Enable actions** . 

6. To reauthenticate using different credentials than those used for creating the data store, do the following: 

   - a. Click **Re-authenticate** on the **Actions** page. 

   - b. Provide the authentication details. 

   - c. Click **Login** to authorize Gemini Enterprise to access the data store. 

   - d. Click **Update** to update the new authentication details. 

7. To view or edit the data store parameters for actions, do the following: 

- a. Click **View/Edit parameters** to edit connector-specific details. For example, for Microsoft Outlook, SharePoint, OneDrive, provide the Tenant ID. 

- b. Click **Save** to update the parameter details. 

### View actions

Console (#console) 

To view the list of actions for a data store, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Select the data store of your choice. 

4. From the navigation menu, select **Actions** . The actions you enabled during data store creation appear as a table on the **Actions** page. 

### Disable actions

Console 

(#console) 

To disable actions, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Select the data store of your choice. 

4. Select **Actions** from the navigation menu. 

5. Select the actions to disable from the table. 

6. Click **Disable actions** . 

Last updated 2026-10-14 UTC. 



## Troubleshoot data stores

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/troubleshoot-data-stores

Use this page to diagnose and resolve any issues with Gemini Enterprise data stores. When a data store fails to retrieve information, you can independently debug the issue by moving through a cohesive, step-by-step observability journey. 

To get a complete picture of an error, understand how Google Cloud's observability tools work together: 

- **Cloud Monitoring** (/monitoring/docs) **:** Detects **when** there is a problem. Use it to view high-level trends, error rates, and set up alerts for your data stores. 

- **Cloud Trace** (/trace/docs/overview) **:** Discovers **where** the problem is occurring. Use it to view the lifecycle of a request, analyze spans, and identify exactly which step caused high latency or failure. 

- **Cloud Logging** (/logging/docs/overview) **:** Explains **why** the problem is occurring. Use it to read the exact error messages and payloads associated with a failed request. 

- **Cloud Audit Logs** (/logging/docs/audit) **:** Identifies **who** or what policy blocked the action. Use it to track security compliance, permission changes, and administrative actions that might be causing access denials. 

### Debugging workflow

When investigating a data store issue, follow this sequential workflow to isolate and resolve the root cause: 

1. Check error rate trends (#check-error-rate-trends) 

2. Find the specific failing request (#find-the-specific-failing-request) 

3. View the error payload (#view-the-error-payload) 

4. Cross-reference usage audit logs (#cross-reference-usage-audit-logs) 

#### Check error rate trends

1. In the Google Cloud console, go to the **Metrics Explorer** page. 

Go to Metrics Explorer (https://console.cloud.google.com/monitoring/metrics-explorer) 

2. Check your dashboards and review your data store request counts and filter by **Tool ID** and **Engine ID** . You can determine if the issue is a one-off error or a widespread systemic spike that requires immediate attention. 

#### Find the specific failing request

1. In the Google Cloud console, go to the **Trace explorer** page: 

Go to **Trace explorer** (https://console.cloud.google.com/traces/explorer) 

You can also find this page by using the search bar. 

2. Examine the scatter plot for traces with an error icon (a red exclamation mark) or unusually high latency. 

3. Click a trace to view its Gantt chart. 

4. Check the `invoke_connector` span to see where the process stalled or failed. 

5. Additionally, you can find the unique assist token associated with a specific request. If you need to escalate a complex issue to Google Cloud Support, share this assist token to expedite the investigation. 

#### View the error payload

1. Click the failing span in **Trace Explorer** . 

2. In the details pane, click **Show logs** . 

3. This automatically pivots you into Cloud Logging, filtered to that exact request. Here, you can read the raw log payload to identify the exact error signature (such as `RESOURCE_EXHAUSTED` or `PERMISSION_DENIED` ). 

#### Cross-reference usage audit logs

If the log payload indicates an IAM issue, a missing scope, or a permission denial, cross-reference your Cloud Audit Logs: 

1. In the Google Cloud console, go to the **Logs Explorer** page. 

Go to Logs Explorer (https://console.cloud.google.com/logs/query) 

2. Review the administrative history. Verify if your administrator recently modified an action filter or revoked a required permission. 

### Example: Trace a failed data store request

Imagine a user prompts your Gemini Enterprise agent to get the status of a Jira issue, but the agent returns a generic failure message. Here is how you would use the observability workflow to find the root cause: 

1. **Check error trends:** Before looking for individual errors, you want to know how widespread the issue is. Open the **Metrics Explorer** in Cloud Monitoring and filter your data store request metrics by the `tool_id: get_issue` . You may see a massive, sudden spike in `RESOURCE_EXHAUSTED` errors. This confirms it is a systemic issue, not just a one-off user typo. 

2. **Find the failed request:** Open the **Trace Explorer** and set the time filter to the last one hour. In the scatter plot, you notice a cluster of traces with a red error icon indicating failures. Click one of these recent traces to investigate. 

3. **Examine the Gantt chart:** The Gantt chart visualizes the request's journey. You see a successful parent span for the initial agent routing, but nested underneath it is a failing `invoke_connector` span specifically targeting the Jira Cloud data store. 

4. **Pivot to logs:** Click the failing `invoke_connector` span. In the Trace details pane, click **Show logs** . 

5. **Identify the root cause:** The **Logs Explorer** opens, pre-filtered to the exact trace ID. You can now examine the log payload generated by the data store to identify the exact error: 

```
"message": "Connector Error: Cause: Failed to execute spec-based tool
'get_issue': Request failed: HTTP error 403: {\"errorMessages\":
[\"permission denied: [User] does not have access to
[Resource]"],\"errors\":{}}"
```

In this payload error message, you can see the specific tool ( `get_issue` ) that failed and the explicit message indicating that the user executing the request lacks access to the specific resource in the target system. 

6. **Resolve:** Using the Common errors (#common-errors) section, you can identify this as a Missing end-user resource access (#missing-end-user-resource-access) error. The Gemini Enterprise agent successfully connected to Jira Cloud, but Jira Cloud rejected the query because the user lacks permissions. To resolve this, ask your Jira Cloud administrator to grant the user access to the specific resource. 

### Common errors

When reviewing your error payloads in Cloud Logging, focus on the broad error signatures. Most data store errors are fully self-resolvable. Find the error you encountered in the following list to determine the root cause and fix. 

#### Authentication & access errors

These errors occur when there are issues with credentials, scopes, or administrative policies preventing access to the required resources. If you encounter these errors, Cloud Audit Logs is useful for debugging recent IAM changes, action filter updates, or revoked permissions. 

Expired or invalid OAuth token 

**Error Signature:** `HTTP request failed with status code 401 / 401 Unauthorized` 

- **Root Cause:** The OAuth token has expired or is invalid. 

- **Resolution:** Re-authorize the data store in your Gemini Enterprise settings to generate a fresh token. 

Tool blocked by an action filter 

- **Error Signature:** `Permission "connectors.tool.execute" denied ... rejected by admin filter configuration` 

- **Root Cause:** The administrator has blocked the tool using an action filter. 

- **Resolution:** The administrator must update the action or tool allowlist. 

Missing OAuth scopes 

- **Error Signatures:** `Access to [Resource] in [Third-Party API] requires [Scope] ... only [Scope] granted` OR `Cause: Insufficient Permission` 

- **Root Cause:** The application registration in the third-party platform is missing the required scopes. 

- **Resolution:** An administrator must grant the exact scopes named in the log and re-authorize the app. 

Missing IAM project permissions 

- **Error Signature:** `Access Denied: User does not have [permission] / mcp.tools.call permission` 

- **Root Cause:** The caller or service account is missing required Google Cloud IAM permissions in the target project. 

- **Resolution:** Grant the named IAM permission to the caller. 

#### Performance & throttling errors

These errors are triggered when request volumes exceed the limits set by the target API or service. Cloud Trace helps identify exactly how long these throttled requests are hanging before they fail. 

Third-party API 429 throttling 

   - **Error Signature:** `Cause: Request has been rate limited` 

   - **Root Cause:** You are making requests faster than the third-party API allows. 

   - **Resolution:** Reduce your request rate, implement backoff strategies, or request a quota increase from the third-party provider. 

- "Enable actions" button is not visible 

   - **Error Signature: Enable actions** button is not visible or disabled in the console after creating a data store. 

   - **Root Cause:** The data store has limited functionality (such as federated search only, ingestion only, or search only) and doesn't support actions. 

   - **Resolution:** Actions can't be enabled on these data store types. 

#### Visibility and resource errors

These errors indicate that while authentication might be successful, the user or application does not have the specific rights to view or interact with the requested data. 

Third-party visibility restriction 

- **Error Signature:** `422 ... you do not have permission to view [Resource/Users]` 

- **Root Cause:** A visibility restriction or organization policy in the third-party platform is preventing data retrieval. 

- **Resolution:** Adjust your third-party organization membership, or reduce the limit of your query scope. 

Missing end-user resource access 

- **Error Signature:** `permission denied: [user] does not have access to [Resource]` 

- **Root Cause:** The end-user executing the request lacks access to the specific component or resource in the target system. 

- **Resolution:** Grant the user access to the resource directly within the target system. 

#### System and server-side errors

These errors result from infrastructure issues, timeouts, or backend misconfigurations and are typically not self-resolvable. 

Slow or overloaded third-party endpoint 

- **Error Signature:** `context deadline exceeded` 

- **Root Cause:** The third-party endpoint is slow or overloaded, causing the Google-side request to time out. 

- **Resolution:** Retry the request. If the error is persistent, contact Google Cloud Support for timeout tuning. 

MCP server credential binding misconfiguration 

- **Error Signature:** `CredsPermissionException: auth.creds.useNormalUserEUC not granted / EUC_PRESENTER` 

- **Root Cause:** There is a server-side policy issue where the MCP server credential binding is misconfigured. This is not customer-actionable. 

- **Resolution:** Contact Google Cloud Support. 

### Get support

If you encounter a persistent `context deadline exceeded` or a `CredsPermissionException` error, you may need to file a support ticket with Google Cloud Support. 

To expedite resolution, please gather the following artifacts from your observability tools before opening a ticket: 

- **From Cloud Logging:** The full JSON log payload of the error. 

- **From Cloud Trace:** The assist token and specific span details (including trace ID) associated with the failed request. 

- **From Usage Audit Logs:** Any relevant IAM modification timestamps or policy changes that might have triggered the issue. 

Last updated 2026-10-14 UTC.
