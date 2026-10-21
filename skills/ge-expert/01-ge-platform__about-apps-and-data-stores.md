# Gemini Enterprise: platform, security, agents, cost, monitoring / About apps and data stores to Provide or auto-detect a schema
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 312-331, extracted 2026-10-18

Contains:
- About apps and data stores (pages 312-318) https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores
- Get data store and entity details (pages 319-321) https://docs.cloud.google.com/gemini/enterprise/docs/get-datastore-details
- Provide or auto-detect a schema (pages 322-331) https://docs.cloud.google.com/gemini/enterprise/docs/provide-schema

## About apps and data stores

URL: https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores

This page describes Gemini Enterprise apps and data stores. 

With Gemini Enterprise, you create an app and connect it to a data store. A given Google Cloud project can contain multiple apps. 

Key terms: 

- **App** : A Gemini Enterprise app provides search results, actions, and agents to your end users. The term _app_ can be used interchangeably with the term _engine_ in the context of APIs. 

- **Data store** : A data store is an entity that contains the data ingested from a first-party data source such as Cloud Storage or third-party applications such as Jira or Salesforce. Data stores that contain data from third-party applications are also called _data connectors_ . 

### Relationship between apps and data stores

An app must be connected to a data store in order to use the data from it to serve search results, answers, or actions. 

Apps have a many-to-many relationship with data stores. When multiple data stores are connected to a single app, this is referred to as _blended search_ . For information about limitations of connecting a search app to more than one data store, see About blended search (#blended). 

**Note:** You can't connect website data stores to your Gemini Enterprise search and assistant apps. 

### Method of app creation and data ingestion

How you create an app and ingest data depends on the type of data you have: 

- For third-party data, you use the Google Cloud console, not the API, to create your app and ingest data. 

- For other data, you can use either the Google Cloud console or the API. 

### Documents

Each data store has one or more data records, called _documents_ . What a document represents varies depending on the type of data in the data store: 

- **Data for third-party data sources** . A document is an entity specific to the third-party data source, such as a Jira issue or Confluence space. 

- **Structured data** . A document is a row in a table or a JSON record that follows a particular schema. You can provide this schema yourself or you can let Gemini Enterprise derive the schema from the ingested data. 

- **Unstructured data** . A document is a file in HTML, PDF with embedded text, or TXT format. PPTX and DOCX formats are available in Preview. 

### Data stores and apps

In Gemini Enterprise, there are various kinds of data stores. A data store can contain only one type of data. 

- Third-party data (#structured-third-party) 

- Structured data (#structured-data) 

- Unstructured data (#unstructured-data) 

#### Structured data for third-party data stores

The following third-party data source connectors are available in Preview with allowlist: 

- Confluence 

- Jira 

- Salesforce 

- Sharepoint Online 

Slack 

Data from these third parties is considered structured data. 

When you set up a new connector, you select a synchronization frequency. You also select which entities to sync. Entities vary depending on the source, such as issues for Jira and content and spaces for Confluence. A unique data store is created for each entity. Entity data stores are grouped by connector instance. 

What's next 

- Connect a third-party data source 

- (/gemini/enterprise/docs/connect-third-party-data-source). 

Create an app (/gemini/enterprise/docs/create-app). 

#### Structured data

A data store with structured data enables semantic search or recommendations over structured data. You can import data from BigQuery or Cloud Storage. You can also manually upload structured JSON data through the API. 

For example, you can enable search or recommendations over a product catalog for your ecommerce experience or a directory of doctors for provider search or recommendations. 

Gemini Enterprise auto-detects the schema from the data that you import. Optionally, you can provide a schema for your data. Providing a schema for your data typically improves the quality of results. 

What's next 

Prepare structured data for ingestion 

- (/gemini/enterprise/docs/prepare-data#structured). 

Create a search data store using one of these methods: 

Import from BigQuery (/gemini/enterprise/docs/connectors/connect-bigquery). 

- Import from Cloud Storage 

- (/gemini/enterprise/docs/connectors/connect-cloud-storage). 

Create an app (/gemini/enterprise/docs/create-app). 

#### Unstructured data

An unstructured data store enables semantic search or recommendations over data such as documents and images. 

Unstructured data stores support documents in HTML, PDF with embedded text, and TXT format. PPTX and DOCX formats are available in Preview. 

Search provides results in the form of 10 URLs and summarized answers for natural language queries. Documents must be uploaded to a Cloud Storage bucket with appropriate access permissions. For example, a financial institution can enable search or recommendations over their private corpus of financial research publications, or a biotech company can enable search or recommendations over their private repository of medical research. 

What's next 

- Prepare unstructured data for ingestion 

- (/gemini/enterprise/docs/prepare-data#unstructured). 

- Create a search data store using one of these methods: 

   - Import from BigQuery (/gemini/enterprise/docs/connectors/connect-bigquery). 

   - Import from Cloud Storage 

   - (/gemini/enterprise/docs/connectors/connect-cloud-storage). 

   - Sync from Google Drive (/gemini/enterprise/docs/connectors/gdrive). 

- Create a first-party datastore (/gemini/enterprise/docs/create-data-store) for your unstructured data. 

- Create an app (/gemini/enterprise/docs/create-app). 

### About blended search

With blended search, multiple data stores can be connected to a single app. This lets the app search across multiple sources and types of data. 

**Note:** Blended search is rate-limited in the Gemini Enterprise Standard and Gemini Enterprise Frontline editions. Unlimited and enhanced blended search requires the Gemini Enterprise Plus edition. 

To make a blended search app, you connect one or more data stores to an app after it has been created. 

When getting search results, you can either search across all data stores, or filter for results from a single data store. 

Blended search has the following limitations: 

- Data stores that contain unstructured data imported using BigQuery are not supported. 

- Blended search allows the following fields in search requests 

- (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.serving Configs/search) 

: 

- `boostSpec` 

- `contentSearchSpec` 

- `dataStoreSpecs` 

- `facetSpecs` 

- `filter` 

- `languageCode` 

- `offset` 

- `oneBoxPageSize` 

- `orderBy` 

   - `query` 

   - `pageSize` 

   - `pageToken` 

   - `relevanceScoreSpec` 

   - `relevanceThreshold` 

   - `session` 

   - `sessionSpec` 

   - `spellCorrectionSpec` 

   - `userInfo` 

   - `userPseudoId` 

- Blended search allows the following fields in `dataStoreSpecs` : 

   - `dataStore` 

   - `boostSpec` : If there are boost specs specified for both `SearchRequest` and `dataStoreSpecs` , both boost specs are applied to search results 

   - `filter` : If there are filters specified for both `SearchRequest` and `dataStoreSpecs` , both filters are applied to search results 

- Create, Read, Update, and Delete (CRUD) operations on serving configs are supported for blended apps. Only the following fields can be added or updated in a serving config: 

   - `boostControlIds` 

   - `displayName` 

   - `filterControlIds` 

   - `genericConfig` : 

      - `contentSearchSpec` 

   - `name` 

   - `solutionType` 

   - `synonymsControlIds` 

- CRUD operations on the following controls are supported for blended search apps: 

   - `boostAction` 

   - `synonymAction` 

   - `filterAction` 

- There is a limit of 50 data stores per search app. 

- If one data store uses a CMEK configuration, all other data stores must also use the same CMEK configuration. 

Last updated 2026-10-14 UTC. 



## Get data store and entity details

URL: https://docs.cloud.google.com/gemini/enterprise/docs/get-datastore-details

This page explains how to retrieve resource details for Gemini Enterprise data stores and their underlying entities using either the Google Cloud console or the Discovery Engine REST API. 

When you interact with data stores using APIs—such as configuring resource-level IAM access controls (/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores), querying search endpoints, or automating ingestion pipelines—you need the unique resource IDs of target data stores and their underlying entities. 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

### Data store concepts

To understand how data store resources are structured in the Discovery Engine API, consider the following concepts: 

Concept Description 

Data storeA container for data ingested from Google or third-party data sources. Standalone data stores belong to the default collection ( `default_collection` ). For more information, see Gemini Enterprise concepts (/gemini/enterprise/docs/concepts#ase-data-stores) and About apps and data stores (/gemini/enterprise/docs/apps-data-stores). 

Data A logical grouping resource within a Google Cloud project and location ( `projects/` collection `{project}/locations/{location}/collections/{collection}` ). 

Multi-entity third-party data stores (such as Jira, Salesforce, or SharePoint Online) create a dedicated collection representing the data store instance. 

Concept Description 

Data storeWhen you connect a third-party data source that contains multiple entity types (such as entity Jira issues, Jira projects, or SharePoint files), Gemini Enterprise automatically creates a separate child data store for each entity type. 

These entity data stores reside as child resources under `collections/default_collection/dataStores/{DATA_STORE_ENTITY_ID}` . 

For more information, see Structured data for third-party data stores 

(/gemini/enterprise/docs/apps-data-stores#structured-third-party) and Introduction to connectors and data stores (/gemini/enterprise/docs/connectors/introduction-to-connectors-and-data-stores). 

### Retrieve data store and entity details

Select one of the following options: 

ConsoleREST (#rest) (#console) 

To retrieve data store and entity details in the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** > **Data Stores** page. 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

2. Click the name of your target data store. 

3. On the data store details page, view the **Data store ID** displayed in the header. 

4. If the data store contains entities, click the **Entities** tab to view the list of configured entities, display names, and their corresponding entity data store IDs (for example, `DataConnector3_entityA` and `DataConnector3_entityB` ). 

### What's next

Configure granular access controls for apps and data stores 

- (/gemini/enterprise/docs/iam-policy-for-apps-and-data-stores#configure-data-storepermissions) 

Discovery Engine REST API reference (/gemini/enterprise/docs/reference/rest) 

Last updated 2026-10-14 UTC. 



## Provide or auto-detect a schema

URL: https://docs.cloud.google.com/gemini/enterprise/docs/provide-schema

When you import structured data using the Google Cloud console, Gemini Enterprise auto-detects the schema. You can either use this auto-detected schema in your engine or use the API to provide a schema to indicate the structure of the data. 

If you provide a schema and later update it with a new schema, the new schema must be backward compatible with the original. Otherwise the schema update fails. 

**Important:** If you don't provide a schema, the auto-detect feature can update your schema by incorporating any newly detected fields when you import new data. If any documents in your imported data contain new fields that are not backward compatible with your original schema, those documents fail to import. 

For reference information about the schema, see `dataStores.schemas` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas). 

**Key Terms:** In the context of schema, the terms _field_ and _property_ are used interchangeably. 

### Approaches to providing the schema for your data store

There are various approaches to determining the schema for structured data. 

- **Auto-detect and edit.** Let Gemini Enterprise auto-detect and suggest an initial schema. Then, you refine the schema through the console interface. Google highly recommends that, after your fields are auto-detected, you map key properties to all the important fields. 

This is the approach that you'll use when following the Google Cloud console instructions for structured data in Create a first-party data store (/gemini/enterprise/docs/connectors/create-data-store). 

**Provide the schema as a JSON object.** Provide the schema to Gemini Enterprise as a JSON object. You need to have prepared a correct JSON object. For an example of a JSON object, see Example schema as a JSON object (#example-schema). After creating the schema, you upload your data according to that schema. 

This is the approach that you can use when creating a data store through the API using a curl command (or program). For example, see Import once from BigQuery (/gemini/enterprise/docs/connectors/connect-bigquery#bq-import-once). Also see the following instructions, Provide your own schema (#provide-your-own). 

### About auto-detect and edit

When you begin importing data, Gemini Enterprise samples the first few documents that are imported. Based on these documents, it proposes a schema for the data, which you can then review or edit. 

If fields that you want to map to key properties aren't present in the sampled documents, then you can manually add these fields when you review the schema. 

**Tip:** Make sure that the documents at the beginning of your dataset are good quality—that all the key fields are represented. That way, you don't have to add or edit fields later. 

If Gemini Enterprise encounters additional fields later in the data import, it still imports these fields and adds them to the schema. If you want to edit the schema after all the data has been imported, see Update your schema (/gemini/enterprise/docs/update- 

schemas#discoveryengine_v1_generated_SchemaService_UpdateSchema_sync-console) . 

### Example schema as a JSON object

You can define your own schema using the JSON Schema (https://json-schema.org/) format, which is an open source, declarative language to define, annotate, and validate JSON documents. For example, this is a valid JSON schema annotation: 

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "type": "object",
 "dynamic": "true",
 "datetime_detection": true,
 "geolocation_detection": true,
 "properties": {
   "title": {
     "type": "string",
     "keyPropertyMapping": "title",
     "retrievable": true,
     "completable": true
   },
   "description": {
     "type": "string",
     "keyPropertyMapping": "description"
   },
   "categories": {
     "type": "array",
     "items": {
       "type": "string",
       "keyPropertyMapping": "category"
     }
   },
   "uri": {
     "type": "string",
     "keyPropertyMapping": "uri"
   },
   "brand": {
     "type": "string",
     "indexable": true,
     "dynamicFacetable": true
   },
   "location": {
     "type": "geolocation",
     "indexable": true,
     "retrievable": true
   },
   "creationDate": {
     "type": "datetime",
     "indexable": true,
     "retrievable": true
   },
```

- `"isCurrent": {` 

- `"type": "boolean",` 

- `"indexable": true,` 

```
     "retrievable": true
   }
 }
}
```

Here are some of the fields in this schema example: 

- **`dynamic`** . If `dynamic` is set to the string value `"true"` , then any new properties found in the imported data is added to the schema. If `dynamic` is set to `"false"` , new properties found in imported data are ignored; the properties are not added to the schema nor are the values are imported. 

For example, a schema has two properties: `title` and `description` , and you upload a data that contains properties for `title` , `description` , and `rating` . If `dynamic` is `"true"` , then the ratings property and data are imported. If `dynamic` is `"false"` , then `rating` properties are not imported, although `title` and `description` are. 

The default is `"true"` . 

- **`datetime_detection`** . If `datetime_detection` is set to the boolean `true` , then, when data in datetime format are imported, the schema type is set to `datetime` . The supported formats are RFC 3339 (https://www.rfc-editor.org/rfc/rfc3339) and ISO 8601 

- (https://en.wikipedia.org/wiki/ISO_8601). 

For example: 

```
2024-08-05 08:30:00 UTC
2024-08-05T08:30:00Z
2024-08-05T01:30:00-07:00
```

- `2024-08-05` 

```
2024-08-05T08:30:00+00:00
```

If `datatime_detection` is set to the boolean `false` , then, when data in datetime format are imported, the schema type is set to `string` . 

The default is `true` . 

- **`geolocation_detection`** . If `geolocation_detection` is set to the boolean `true` , then, when data in geolocation format are imported, the schema type is set to `geolocation` . Data is detected as geolocation if it is an object containing a latitude number and a longitude number or an object containing an address string. 

For example: 

- `"myLocation": {"latitude":37.42, "longitude":-122.08}` 

- `"myLocation": {"address": "1600 Amphitheatre Pkwy, Mountain View, CA 94043"}` 

If `geolocation_detection` is set to the boolean `false` , then, when data in geolocation format are imported, the schema type is set to `object` . 

The default is `true` . 

- **`keyPropertyMapping`** . A field that maps predefined keywords to critical fields in your documents, helping to clarify their semantic meaning. Values include `title` , `description` , `uri` , and `category` . Note that your field name doesn't need to match the `keyPropertyValues` value. For example, for a field that you named `my_title` , you can include a `keyPropertyValues` field with a value of `title` . 

Fields marked with `keyPropertyMapping` are by default indexable and searchable, but not retrievable, completable, or dynamicFacetable. This means that you don't need to include the `indexable` or `searchable` fields with a `keyPropertyValues` field to get the expected default behavior. 

**Note:** Key properties can improve the quality of search results and search autocomplete accuracy. If you use auto-schema detection, key properties are not automatically added. We highly recommend using the **`schemas.patch`** method to mark data fields as key properties, especially **`title`** , **`uri`** , and **`description`** . 

- **`type`** . The type of the field. This is a string value that is `datetime` , `geolocation` or one of the primitive types ( `integer` , `boolean` , `object` , `array` , `number` , or `string` ) . 

- **`retrievable`** . Indicates whether this field can be returned in a search response. This can be set for fields of type `number` , `string` , `boolean` , `integer` , `datetime` , and `geolocation` . A maximum of 50 fields can be set as retrievable. Userdefined fields and `keyPropertyValues` fields are not retrievable by default. To make a field retrievable, include `"retrievable": true` with the field. 

- **`indexable`** . Indicates whether this field can be filtered, faceted, boosted, or sorted in the `servingConfigs.search` 

- (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.s ervingConfigs/search) 

method. This can be set for fields of type `number` , `string` , `boolean` , `integer` , `datetime` , and `geolocation` . A maximum of 50 fields can be set as indexable. User-defined fields are not indexable by default, except for fields containing the `keyPropertyMapping` field. To make a field indexable, include `"indexable": true` with the field. 

- **`dynamicFacetable`** . Indicates that the field can be used as a dynamic facet. This can be set for fields of type `number` , `string` , `boolean` , and `integer` . To make a field dynamically facetable, it must also be indexable: include `"dynamicFacetable": true` and `"indexable": true` with the field. 

- **`searchable`** . Indicates whether this field can be reverse indexed to match unstructured text queries. This can only be set for fields of type `string` . A maximum of 50 fields can be set as searchable. User-defined fields are not searchable by default, except for fields containing the `keyPropertyMapping` field. To make a field searchable, include `"searchable": true` with the field. 

- **`completable`** . Indicates whether this field can be returned as an autocomplete suggestion. This can only be set for fields of type `string` . To make a field completable, include `"completable": true` with the field. 

**Note:** For auto-detected schemas, newly detected fields are automatically indexable, searchable, and retrievable, as long as they follow the type requirements and stay within the maximum limits. 

### Provide your own schema as a JSON object

To provide your own schema, you create a data store that contains an empty schema and then you update the schema, supplying your schema as a JSON object. Follow these steps: 

1. Prepare the schema as a JSON object, using the Example schema as a JSON object (#example-schema) as a guide. 

2. Create a data store. 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/g
lobal/collections/default_collection/dataStores?dataStoreId=DATA_STORE_ID"
\
-d '{
 "displayName": "DATA_STORE_DISPLAY_NAME",
 "industryVertical": "INDUSTRY_VERTICAL"
}'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

   - _`DATA_STORE_ID`_ : the ID of the data store that you want to create. This ID can contain only lowercase letters, digits, underscores, and hyphens. 

   - _`DATA_STORE_DISPLAY_NAME`_ : the display name of the data store that you want to create. 

   - _`INDUSTRY_VERTICAL`_ : `GENERIC` 

3. Use the schemas.patch 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.sche mas/patch) 

API method to provide your new JSON schema as a JSON object. 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locatio
ns/global/collections/default_collection/dataStores/DATA_STORE_ID/schemas/
default_schema" \
-d '{
 "structSchema": JSON_SCHEMA_OBJECT
}'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`DATA_STORE_ID`_ : the ID of the data store. 

- _`JSON_SCHEMA_OBJECT`_ : your new JSON schema as a JSON object. For example: 

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "type": "object",
 "properties": {
   "title": {
     "type": "string",
     "keyPropertyMapping": "title"
   },
   "categories": {
     "type": "array",
     "items": {
       "type": "string",
       "keyPropertyMapping": "category"
     }
   },
   "uri": {
     "type": "string",
     "keyPropertyMapping": "uri"
   }
 }
}
```

<sup>Example command and result</sup> 

```
curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-
token)" -H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/dataStores/my-
data-store/schemas/default_schema" -d '{
"structSchema": {
"$schema": "https://json-schema.org/draft/2020-12/schema",
"type": "object",
"properties": {
"title": {
"type": "string",
"keyPropertyMapping": "title"
},
"categories": {
"type": "array",
"items": {
"type": "string",
"keyPropertyMapping": "category"
}
},
"uri": {
"type": "string",
"keyPropertyMapping": "uri"
}
}
}
}'
{
"name":
"projects/123456/locations/global/collections/default_collection/dataS
tores/my-data-store/schemas/default_schema/operations/update-schema-
10569824819404198922",
"metadata": {
"@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.UpdateSchemaMetad
ata"
}
}
```

4. Optional: Review the schema by following the procedure View a schema definition (/gemini/enterprise/docs/get-schema-definition). 

### What's next

- Create a search app (/gemini/enterprise/docs/create-app) 

- Get the schema definition for structured data (/gemini/enterprise/docs/get-schema-definition) 

Update a schema for structured data (/gemini/enterprise/docs/update-schemas) 

Last updated 2026-10-14 UTC.
