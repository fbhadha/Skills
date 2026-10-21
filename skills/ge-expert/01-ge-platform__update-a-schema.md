# Gemini Enterprise: platform, security, agents, cost, monitoring / Update a schema to Gemini Enterprise
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 984-1030, extracted 2026-10-18

Contains:
- Update a schema (pages 984-990) https://docs.cloud.google.com/gemini/enterprise/docs/update-schemas
- View a schema definition (pages 991-992) https://docs.cloud.google.com/gemini/enterprise/docs/get-schema-definition
- Purge a first-party data store (pages 993-994) https://docs.cloud.google.com/gemini/enterprise/docs/delete-datastores
- Delete a schema for structured data (pages 995-995) https://docs.cloud.google.com/gemini/enterprise/docs/delete-schemas
- Delete an app (pages 996-1000) https://docs.cloud.google.com/gemini/enterprise/docs/delete-app
- Delete a data store (pages 1001-1002) https://docs.cloud.google.com/gemini/enterprise/docs/delete-a-data-store
- Evaluate search quality (pages 1003-1025) https://docs.cloud.google.com/gemini/enterprise/docs/evaluate-search-quality
- Gemini Enterprise (pages 1026-1030) https://docs.cloud.google.com/gemini/enterprise/docs/overview

## Update a schema

URL: https://docs.cloud.google.com/gemini/enterprise/docs/update-schemas

You can update the schema structured data 

(/gemini/enterprise/docs/apps-data-stores#structured-data) and unstructured data with metadata (/gemini/enterprise/docs/apps-data-stores#unstructured-data) that supports a schema. 

You can update the schema in the Google Cloud console or by using the 

`schemas.patch` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas/p atch) 

API method. 

To update the schema, you can add new fields, change indexable, searchable, and retrievable annotations for a field, or mark a field as a key property, such as `title` , `uri` and `description` . 

**Important:** Google strongly recommends that you update your schema with key property mappings, especially for **`title`** . This ensures that your results are displayed correctly and helps Gemini Enterprise identify important information that allows it to generate better results. 

### Update your schema

You can update your schema in the Google Cloud console or using the API. 

**Note:** Editing the schema indexes your data store again. For large data stores, indexing can take several hours. 

ConsoleREST (#rest)C# (#c)Go (#go)Java (#java)Python (#python)Ruby (#ruby) (#console) 

To update a schema in the Google Cloud console, follow these steps: 

1. Review the Requirements and limitations (#limitations) section to check that your schema update is valid. 

2. If you are updating field annotations (setting fields as indexable, retrievable, dynamic facetable, searchable, or completable), review Configure field settings (/gemini/enterprise/docs/configure-field-settings) for the limitations and requirements of each annotation type. 

3. Check that you have completed data ingestion. Otherwise, the schema might not be available to edit yet. 

4. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

5. In the navigation menu, click **Data Stores** . 

6. In the **Name** column, click the data store with the schema that you want to update. 

7. Click the **Schema** tab to view the schema for your data. 

   - This tab might be empty if this is the first time you're editing the fields. 

8. Click the **Edit** button. 

9. Update your schema: 

      - **Map key properties:** In the **Key properties** column of your schema, select a key property to map a field to. For example, if a field called `details` always contains the description of a document, map that field to the key property **Description** . 

**Update number of dimensions (Advanced)** : You can update this setting if you are using custom vector embeddings with Gemini Enterprise. See Use custom embeddings 

- (/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation. 

- **Update field annotations:** To update annotations for a field, select or deselect a field's annotation setting. Available annotations are **Retrievable** , **Indexable** , **Dynamic Facetable** , **Searchable** , and **Completable** . Some field settings have limitations. See 

Configure field settings (/gemini/enterprise/docs/configure-field-settings) for descriptions and requirements for each annotation type. 

**Add a new field:** Adding new fields to your schema before importing new documents with those fields can shorten the time it takes Gemini Enterprise to reindex your data after import. 

- a. Click **Add new fields** to expand that section. 

- b. Click **Add node** and specify settings for the new field. 

To indicate an array, set **Array** to **Yes** . For example, to add an array of strings, set **type** to `string` and **Array** to `Yes` . 

10. Click **Save** to apply your schema changes. 

Changing the schema triggers reindexing. For large data stores, reindexing can take hours. 

### Requirements and limitations

When updating a schema, be sure that the new schema is backward compatible with the schema you are updating. To update a schema with a new schema that is not backward compatible, you need to delete all the documents in the data store, delete the schema, and create a new schema. 

Updating a schema triggers re-indexing of all documents. Reindexing a large data store can take hours or days. 

Schema updates don't support the following: 

- **Changing a field type.** A schema update doesn't support changing the type of the field. For example, a field mapped to `integer` can't be changed to `string` . 

- **Removing a field.** After it's defined, a field can't be removed. You can continue adding new fields but you can't remove an existing field. 

### Limitation examples (REST only)

This section shows examples of valid and invalid types of schema updates. These examples use the following example JSON schema: 

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "type": "object",
 "properties": {
   "title": {
     "type": "string"
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
   }
 }
}
```

#### Examples of supported updates

The following updates to the example schema are supported. 

**Adding a field.** In this example, the field `properties.uri` has been added to the schema. 

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "type": "object",
 "properties": {
   "title": {
     "type": "string"
   },
   "description": {
     "type": "string",
     "keyPropertyMapping": "description"
   },
   "uri": { // Added field. This is supported.
     "type": "string",
     "keyPropertyMapping": "uri"
   },
   "categories": {
     "type": "array",
     "items": {
       "type": "string",
       "keyPropertyMapping": "category"
     }
   }
 }
}
```

**Adding or removing key property annotations for** **`title` ,** **`description` or** **`uri` .** In this example, `keyPropertyMapping` has been added to the `title` field. 

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "type": "object",
 "properties": {
   "title": {
     "type": "string",
     "keyPropertyMapping": "title" // Added "keyPropertyMapping". This is
supported.
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
   }
 }
```

#### Examples of invalid schema updates

The following updates to the example schema aren't supported. 

**Changing a field type.** In this example, the `title` field's type has been changed from string to number. This is not supported. 

```
 {
   "$schema": "https://json-schema.org/draft/2020-12/schema",
   "type": "object",
   "properties": {
     "title": {
       "type": "number" // Changed from string. Not allowed.
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
     }
   }
 }
```

**Removing a field.** In this example, the `title` field has been removed. This is not supported. 

```
 {
   "$schema": "https://json-schema.org/draft/2020-12/schema",
   "type": "object",
   "properties": {
     // "title" is removed. Not allowed.
     "description": {
       "type": "string",
       "keyPropertyMapping": "description"
     },
     "uri": {
       "type": "string",
       "keyPropertyMapping": "uri"
     },
     "categories": {
       "type": "array",
       "items": {
         "type": "string",
         "keyPropertyMapping": "category"
       }
     }
   }
 }
```

### What's next

View the schema definition for structured data (/gemini/enterprise/docs/get-schema-definition) Delete a schema for structured data (/gemini/enterprise/docs/delete-schemas) 

Preview search results (/gemini/enterprise/docs/preview-search-results) 

Last updated 2026-10-14 UTC. 



## View a schema definition

URL: https://docs.cloud.google.com/gemini/enterprise/docs/get-schema-definition

You can view the schema for any data store containing data that supports a schema, such as structured data (/gemini/enterprise/docs/prepare-data#structured) or unstructured data with structured data 

(/gemini/enterprise/docs/prepare-data#unstructured). 

You can view the schema in the Google Cloud console or by using the `dataStores.schemas.get` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.schemas/g et) 

API method. Viewing the schema for a website is supported only over the REST API. 

ConsoleREST (#rest)C# (#c)Go (#go)Java (#java)Python (#python)Ruby (#ruby) (#console) 

To view a schema in the Google Cloud console, follow these steps. 

1. If you are viewing an auto-generated schema, make sure that you have completed data ingestion. Otherwise, the schema might not be available yet. 

2. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

3. In the navigation menu, click **Data Stores** . 

4. In the **Data stores** page, select the data store. 

5. In the **Data** page, click the **Entity** tab. 

6. Select an entity with the schema that you want to view. 

7. Click the **Schema** tab to view the schema for your data. 

### What's next

Provide or auto-detect a schema (/gemini/enterprise/docs/provide-schema) 

Update a schema for structured data (/gemini/enterprise/docs/update-schemas) 

Delete a schema for structured data (/gemini/enterprise/docs/delete-schemas) 

Last updated 2026-10-14 UTC. 



## Purge a first-party data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/delete-datastores

This page describes how to purge all of the data in a structured or unstructured data store. 

You purge the data in a data store if you want to completely delete the contents of the data store before re-importing fresh data. Purging a data store deletes only the data in the data store, leaving your app, schema, and configurations intact. 

For how to delete a data store, see Delete a datastore 

(/gemini/enterprise/docs/delete-a-data-store). 

### Purge data

To purge data from a data store, do the following: 

- ConsoleREST (#rest)C# (#c)Go (#go)Java (#java)Node.js (#node.js)Python (#python)Ruby (#r (#console) 

To use the Google Cloud console to purge the data from a branch of a structured or unstructured, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/apps) 

2. In the navigation menu, click **Data Stores** . 

3. In the **Name** column, click the data store that you want to purge. 

4. In the **Documents** tab, click **Purge data** . 

5. Read the warning in the **Confirm purge data** dialog. If you want to continue, enter the name of your data store, and then click **Confirm** . Purging data is a long-running operation. For more information, see Monitor long-running operations 

(/gemini/enterprise/docs/long-running-operations). 

6. Click the **Activity** tab to monitor the progress of the purge operation. 

Last updated 2026-10-14 UTC. 



## Delete a schema for structured data

URL: https://docs.cloud.google.com/gemini/enterprise/docs/delete-schemas

You can only delete a schema if all of the documents associated with the schema are deleted. Otherwise, the attempt fails. After you delete a schema, you can call the `schemas.create` method to create a new one. 

To delete a schema for structured data, follow these steps: 

RESTC# (#c)Go (#go)Java (#java)Python (#python)Ruby (#ruby) (#rest) 

1. Find your data store ID. If you already have your data store ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page and in the navigation menu, click **Data Stores** . 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

   - b. Click the name of your data store. 

   - c. On the **Data** page for your data store, get the data store ID. 

2. Delete your schema. 

```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/gl
obal/collections/default_collection/dataStores/DATA_STORE_ID/schemas/default_sc
hema"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

_`DATA_STORE_ID`_ : the ID of the data store. 

Last updated 2026-10-14 UTC. 



## Delete an app

URL: https://docs.cloud.google.com/gemini/enterprise/docs/delete-app

This page describes best practices and instructions for safely deleting an app. 

### Steps to delete an app

The following instructions are for the Google Cloud console. 

Console 

(#console) 

To delete an app, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/apps) 

2. For the app that you want to delete, click , and then click **Delete** . 

3. In the **Delete the app?** dialog, enter your app name, and then click **Confirm** . 

### Best practices for deleting an app with an IAM policy

Deleting an app is an irreversible action. Therefore, if your app has configured access controls (/gemini/enterprise/docs/iam-policy-for-apps), you can remove all users from its IAM policy before deleting the app. Follow these steps: 

1. **Clear the IAM policy:** Before deleting the app, clear its IAM policy to remove user access. You can do this by setting an empty `bindings` array. 

   - a. Get the current IAM policy of your app using the `getIamPolicy` 

      - (/gemini/enterprise/docs/reference/rpc/google.iam.v1#getiampolicyrequest) method. 

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/
LOCATION/collections/default_collection/engines/APP_ID:getIamPol
icy"
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

   - `us` for the US multi-region 

   - `eu` for the EU multi-region 

   - `global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multiregion_for_your_data_store) 

_`LOCATION`_ : the multi-region of your data store: `global` , `us` , or `eu` 

- _`APP_ID`_ : the ID of the app that you want to configure. 

**Note:** Copy the **`etag`** value from the response. This value is required to update the IAM policy. The **`etag`** value changes with each policy update. 

<sup>Example command and result</sup> 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://global-discoveryengine.googleapis.com/v1/projects/my-
project-
123/locations/global/collections/default_collection/engines/my-
app:getIamPolicy"
{
 "version": 1,
 "etag": "1234567890"
}
```

b. To remove all existing bindings, use the `setIamPolicy` (/gemini/enterprise/docs/reference/rpc/google.iam.v1#setiampolicyrequest) method with an empty `bindings` array in the request body. 

REST 

(#rest) 

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-d '{
     "policy": {
       "etag": "ETAG",
       "bindings": []
     }
   }' \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/
LOCATION/collections/default_collection/engines/APP_ID:setIamPol
icy"
```

Replace the following: 

- _`ETAG`_ : the `etag` value you got as the response when you used the `getIamPolicy` method. 

- _`PROJECT_ID`_ : the ID of your project. 

- _`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

   - `us` for the US multi-region 

`eu` for the EU multi-region 

- `global` for the Global location 

For more information, see Specify a multi-region for your data store 

(/gemini/enterprise/docs/locations#specify_a_multiregion_for_your_data_store) 

- _`LOCATION`_ : the multi-region of your data store: `global` , `us` , or `eu` 

- _`APP_ID`_ : the ID of the app that you want to configure. 

<sup>Example command and result</sup> 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-d '{
     "policy": {
       "etag": "1234567890",
       "bindings": []
     }
   }' \
"https://global-discoveryengine.googleapis.com/v1/projects/my-
project-
123/locations/global/collections/default_collection/engines/my-
app:setIamPolicy"
{
 "version": 1,
 "etag": "3456789012"
}
```

2. **Confirm user impact:** After clearing the policy and allowing for propagation time (/iam/docs/access-change-propagation), confirm that the access revocation hasn't caused any unintended issues for users. 

3. **Delete the app:** After you've confirmed the impact, proceed with deleting the app as described in the Steps to delete an app (#delete-an-app) section. 

Last updated 2026-10-14 UTC. 



## Delete a data store

URL: https://docs.cloud.google.com/gemini/enterprise/docs/delete-a-data-store

This page describes how to delete a data store. 

Deletion is an asynchronous process that can take days. You can't reuse a data store ID until the original data store is completely deleted. To prevent this from blocking your workflow, we strongly recommend that you use a unique ID for every data store. 

### Before you begin

Before deleting a structured or unstructured data store, if your data store is connected to an app, you must do one of the following: 

- To keep the app and delete only the data store, unlink the data store from its connected app. 

- To delete both the app and the data store, first Delete the app 

- (/gemini/enterprise/docs/delete-app) that the data store is connected to. 

### Procedure

Console 

(#console) 

To delete a data store, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page, and then click **Data Stores** . 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

2. For the data store that you want to delete, click , and then click **Delete** . 

Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## Evaluate search quality

URL: https://docs.cloud.google.com/gemini/enterprise/docs/evaluate-search-quality

**Preview** 

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

As part of your search experience with Gemini Enterprise, you can evaluate the quality of your search results for custom search apps using sample query sets. 

You can evaluate the performance of custom search apps that contain structured and unstructured data. 

You can't evaluate the performance of apps with multiple data stores. 

This page explains why, when, and how to evaluate the search quality using the evaluation method. 

### Overview

This section describes why and when to perform search quality evaluation. For information on how to perform search quality evaluation, see Process for evaluating search quality (#process). 

#### Reasons to perform evaluation

Assessment of your search quality provides you metrics that help perform tasks such as the following: 

- At an aggregate-level, gauge your search engine's performance 

- At a query-level, locate patterns to understand potential biases or shortcomings in ranking algorithms 

- Compare historical evaluation results to understand the impact of changes in your search configuration 

For a list of metrics, see Understand the results (#metrics-table). 

#### When to perform evaluation

Gemini Enterprise extends several search configurations to enhance your search experience. You can perform search quality evaluation after you make the following changes: 

- Configure serving controls for search (/gemini/enterprise/docs/configure-serving-controls) 

- Filter search results (/gemini/enterprise/docs/filter-search-metadata) 

- Boost search results (/gemini/enterprise/docs/boost-search-results) 

You can also run the evaluation tests regularly because the search behavior updates periodically. 

### About sample query sets

Sample query sets are used for quality evaluation. The sample query set must adhere to its prescribed format, and it must contain query entries that have the following nested fields: 

- **Queries** : the query whose search results are used to generate the evaluation metrics and determine the search quality. Google recommends using a diverse set of queries that reflects your user's search pattern and behavior. 

- **Targets** : the URI of the document that's expected as a search result of the sample query. To understand the definition of document for structured, unstructured, see Connector and data store concepts 

- (/gemini/enterprise/docs/introduction-to-connectors-and-datastores#connector_and_data_store_concepts) 

When the target documents are compared to the documents retrieved in the search response, performance metrics are generated. Metrics are generated 

using these two techniques: 

- **Document matching** : the URIs of the target documents are compared with the URIs of the retrieved documents. This determines whether the expected documents are present in the search results. During the comparison, the evaluation API tries to extract the following fields in the following order, and use the first available value to match the target with the retrieved document: 

   - `cdoc_url` in the `structData` 

   - (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections. dataStores.branches.documents#Document.FIELDS.struct_data) field of the document definition 

   - `uri` in the `structData` 

   - (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections. dataStores.branches.documents#Document.FIELDS.struct_data) field of the document definition 

   - `link` in the `derivedStructData` 

   - (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections. dataStores.branches.documents#Document.FIELDS.derived_struct_data) field of the document definition 

   - `url` in the `derivedStructData` 

   - (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections. dataStores.branches.documents#Document.FIELDS.derived_struct_data) field of the document definition 

- **Page matching** : when you include page numbers in your sample targets, the evaluation API compares the results at a page-level. This determines whether the pages mentioned in the targets are also cited in the search response. You must enable extractive answers to enable page-level matching. The evaluation API matches the page from the first extractive answer in the search result. 

#### Purpose of sample query sets

Using the same sample query set for all your search quality evaluations for a given data store ensures a consistent and reliable way to measure the search quality results. This also establishes a fair and repeatable system. 

The results from each evaluation are compared to target results for each sample query to calculate different metrics, such as recall, precision, and normalized discounted cumulative gain (NDCG). These quantitative metrics are used to rank the results from different search configurations. 

#### Quotas and limits

The following limit applies to the sample query sets: 

Each sample query set can contain a maximum of 20,000 queries. 

The following quota applies to the sample query sets: 

- You can create a maximum of 100 sample query sets per project and 500 sample query sets per organization. For more information, see Quotas and limits (/gemini/enterprise/docs/quotas). 

#### Sample query set format

The query set must conform to the following schema when constructed in JSON format. The query set can contain multiple query entries with one query in each query entry. When presented in newline delimited JSON (NDJSON) format, each query entry must be on a new line. 

Import from BigQuery and Cloud Storage 

The following section provides the sample query set templates for importing from from BigQuery and Cloud Storage. 

Unstructured dataStructured data… (#unstructured-data) 

Use the following template to draft a sample query file in JSON format to evaluate unstructured data with metadata. 

```
{
 "queryEntry": {
   "query": "SAMPLE_QUERY",
   "targets": [
     {
       "uri": "gs://PATH/TO/CLOUD/STORAGE/LOCATION_1.docx"
     },
     {
       "uri": "gs://PATH/TO/CLOUD/STORAGE/LOCATION_2.pdf",
       "pageNumbers": [
PAGE_NUMBER_1,
PAGE_NUMBER_2
       ]
     },
     {
       "uri": "CDOC_URL"
     }
   ]
 }
}
```

Replace the following: 

- _`SAMPLE_QUERY`_ : the query used to test evaluate the search quality 

- _`PATH/TO/CLOUD/STORAGE/LOCATION`_ : the path to the Cloud Storage location where the expected result resides. This is the value of the `link` field in the `derivedStructData` 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.data Stores.branches.documents#Document.FIELDS.derived_struct_data) field of the document definition. 

- _`PAGE_NUMBER_1`_ : an optional field to indicate the page numbers in the PDF file where the expected response for the query is located. This is useful when the file has multiple pages. 

- _`CDOC_URL`_ : an optional field to indicate the custom document ID `cdoc_url` field in the document metadata in the Gemini Enterprise data store schema. 

Here's an example of a sample query set in JSON and NDJSON formats: 

JSONNDJSON (#ndjson) (#json) 

```
[
 {
   "queryEntry": {
     "query": "2018 Q4 Google revenue",
     "targets": [
       {
         "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-
investor-pdfs/2018Q4_alphabet_earnings_release.pdf"
       },
       {
         "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-
investor-pdfs/201802024_alphabet_10K.pdf"
       }
     ]
   }
 },
 {
   "queryEntry": {
     "query": "2019 Q4 Google revenue",
     "targets": [
       {
         "uri": "gs://cloud-samples-data/gen-app-builder/search/alphabet-
investor-pdfs/2019Q4_alphabet_earnings_release.pdf"
       }
     ]
   }
 }
]
```

Import from local file system 

The following section provides the sample query set templates for importing from the local file system. 

Unstructured dataStructured data… (#unstructured-data) 

Use the following template to draft a sample query file in JSON format to evaluate unstructured data with metadata. 

```
{
 "inlineSource": {
   "sampleQueries": [
     {
       "queryEntry": {
         "query": "SAMPLE_QUERY",
         "targets": [
           {
             "uri": "gs://PATH/TO/CLOUD/STORAGE/LOCATION_1.docx"
           },
           {
             "uri": "gs://PATH/TO/CLOUD/STORAGE/LOCATION_2.pdf",
             "pageNumbers": [
PAGE_NUMBER_1,
PAGE_NUMBER_2
             ]
           },
           {
             "uri": "CDOC_URL"
           }
         ]
       }
     }
   ]
 }
}
```

Replace the following: 

- _`SAMPLE_QUERY`_ : the query used to test evaluate the search quality 

- _`PATH/TO/CLOUD/STORAGE/LOCATION`_ : the path to the Cloud Storage location where the unstructured data file to be queried resides. This is the value of the `link` field in the `derivedStructData` 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.data Stores.branches.documents#Document.FIELDS.derived_struct_data) field of the document definition. 

_`PAGE_NUMBER_1`_ : an optional field to indicate the page numbers where the required response for the query can be located in the PDF file. This is useful if the file has multiple pages. 

_`CDOC_URL`_ : an optional field to indicate the custom document ID `cdoc_url` field in the document metadata in the Gemini Enterprise data store schema. 

Here's an example of a sample query set: 

JSON (#json) `{ "inlineSource": { "sampleQueries": [ { "queryEntry": { "query": "2018 Q4 Google revenue", "targets": [ { "uri": "gs://cloud-samples-data/gen-appbuilder/search/alphabet-investorpdfs/2018Q4_alphabet_earnings_release.pdf" }, { "uri": "gs://cloud-samples-data/gen-appbuilder/search/alphabet-investor-pdfs/201802024_alphabet_10K.pdf" } ] } }, { "queryEntry": { "query": "2019 Q4 Google revenue", "targets": [ { "uri": "gs://cloud-samples-data/gen-appbuilder/search/alphabet-investorpdfs/2019Q4_alphabet_earnings_release.pdf" } ] } } ] }` 

```
}
```

### Process for evaluating search quality

The process of search quality evaluation is as follows: 

1. Create a sample query set (#create-sample-query-set). 

2. Import sample query (#import-sample-query) that conforms to the prescribed JSON format. 

3. Run search quality evaluation (#run-eval). 

4. Understand the results (#interpret-results). 

The following sections give the instructions to perform these steps using REST API methods. 

#### Before you begin

- The following limit applies: 

- At a given time, you can only have a single active evaluation per project. 

- The following quota applies: 

   - You can initiate a maximum of five evaluation requests per day per project. For more information, see Quotas and limits 

   - (/gemini/enterprise/docs/quotas). 

- To get page-level metrics, you must enable extractive answers (/gemini/enterprise/docs/snippets#extractive-answers). 

#### Create a sample query set

You can create a sample query set and use it to evaluate the quality of the search responses for a given data store. To create a sample query set, do the following. 

The following sample shows how to create the sample query set using the `sampleQuerySets.create` (/gemini/enterprise/docs) method. 

1. Create the sample query set. 

```
curl -X POST \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
```

- `-H "Content-Type: application/json" \` 

```
   -H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/lo
cations/global/sampleQuerySets?sampleQuerySetId=SAMPLE_QUERY_SET_ID"
\
   -d '{
 "displayName": "SAMPLE_QUERY_SET_DISPLAY_NAME"
}'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

_`SAMPLE_QUERY_SET_ID`_ : a custom ID for your sample query set. 

- _`SAMPLE_QUERY_SET_DISPLAY_NAME`_ : a custom name for your sample query set. 

<sup>Response</sup> 

You should receive a JSON response similar to the following: 

```
{
 "name":
"projects/PROJECT_NUMBER/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID",
 "displayName": "SAMPLE_QUERY_SET_DISPLAY_NAME",
```

#### Import sample query data

After creating the sample query set, import the sample query data. To import the sample query data, you can do any of the following: 

- Import from Cloud Storage: import an NDJSON file from a Cloud Storage location. 

- Import from BigQuery: import BigQuery data from a BigQuery table. To create the BigQuery table from your NDJSON file, see Loading JSON data from Cloud Storage (/bigquery/docs/loading-data-cloud-storage-json). 

- Import from your local file system: create the sample query set in your local file system and import it. 

Cloud StorageBigQuery (#bigquery)Local file system… (#cloud-storage) 

1. Create the sample query sets that conform to the sample query set format (#sample-query-set-format). 

2. Import the JSON file containing the sample query set from a Cloud Storage location using the `sampleQueries.import` method. 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/lo
cations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/sampleQueries:impo
rt" \
-d '{
 "gcsSource": {
   "inputUris": ["INPUT_FILE_PATH"],
 },
 "errorConfig": {
   "gcsPrefix": "ERROR_DIRECTORY"
 }
}'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`SAMPLE_QUERY_SET_ID`_ : the custom ID for your sample query set that you defined during sample query set creation. 

- _`INPUT_FILE_PATH`_ : the path to the Cloud Storage location for your sample query set. 

- _`ERROR_DIRECTORY`_ : an optional field to specify the path to the Cloud Storage location where error files are logged when import errors occur. Google recommends leaving this empty or removing the `errorConfig` field so that Gemini Enterprise can automatically create a temporary location. 

<sup>Response</sup> 

You should receive a JSON response similar to the following. Note the value of _`OPERATION_ID`_ . You need this value in the next step to poll the status of this long-running operation (LRO). 

```
{
 "name":
"projects/PROJECT_NUMBER/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID/operations/OPERATION_ID",
 "metadata": {
   "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSample
QueriesMetadata"
 }
}
```

3. Get the status of the long-running operation (LRO) using the `operations.get` method. 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1beta/projects/
PROJECT_NUMBER/locations/global/sampleQuerySets/SAMPLE_QUERY_SET_ID/o
perations/OPERATION_ID"
```

<sup>Response</sup> 

You should receive a JSON response similar to the following. If there are errors and the import failed, the response shows a `failureCount` field to indicate the number of sample queries that failed to import. 

```
{
"name":
"projects/PROJECT_NUMBER/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID/operations/OPERATION_ID",
"metadata": {
  "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSample
QueriesMetadata",
  "createTime": "CREATE_TIME",
  "updateTime": "UPDATE_TIME",
  "successCount": "SUCCESS_COUNT",
  "totalCount": "TOTAL_COUNT"
},
"done": true,
"response": {
  "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1beta.ImportSample
QueriesResponse",
  "errorConfig": {
    "gcsPrefix": "gs://PROJECT_NUMBER_us_import/ERROR_CONFIG_FOLDER"
  }
}
}
```

#### Run search quality evaluation

After importing the sample query data into the sample query sets, follow these steps to run the search quality evaluation. 

REST 

(#rest) 

1. Initiate a search quality evaluation. 

**Note:** You can evaluate the search performance of an app and you can evaluate the search performance of a data store. For the following procedure, Google recommends evaluating search performance of the app. 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/lo
cations/global/evaluations" \
-d '{
"evaluationSpec": {
  "querySetSpec": {
    "sampleQuerySet":
"projects/PROJECT_ID/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID"
  },
  "searchRequest": {
    "servingConfig":
"projects/PROJECT_ID/locations/global/collections/default_collection/
engines/APP_ID/servingConfigs/default_search"
  }
}
}'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`SAMPLE_QUERY_SET_ID`_ : the custom ID for your sample query set that you defined during sample query set creation. 

- _`APP_ID`_ : the ID of the Gemini Enterprise app whose search quality you want to evaluate. 

<sup>Response</sup> 

You should receive a JSON response similar to the following. Note the value of _`EVALUATION_ID`_ . You need this value in the next step to poll the status of the evaluation, which is a long-running operation (LRO). 

```
{
"name":
"projects/PROJECT_NUMBER/locations/global/operations/OPERATION_ID",
"done": true,
"response": {
  "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.Evaluation"
,
  "name":
"projects/PROJECT_NUMBER/locations/global/evaluations/EVALUATION_ID",
  "evaluationSpec": {
    "querySetSpec": {
      "sampleQuerySet":
"projects/PROJECT_NUMBER/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID"
    },
    "searchRequest": {
      "servingConfig":
"projects/PROJECT_NUMBER/locations/global/collections/default_collect
ion/engines/APP_ID/servingConfigs/default_search"
    }
  },
  "state": "PENDING"
}
}
```

2. Monitor progress of the evaluation. 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/lo
cations/global/evaluations/EVALUATION_ID"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`EVALUATION_ID`_ : the ID for your evaluation job that was returned in the previous step when you initiated the evaluation. 

<sup>Response</sup> 

You should receive a JSON response similar to the following. The status of the evaluation is shown as `PENDING` until the evaluation is complete. 

```
{
"name":
"projects/PROJECT_NUMBER/locations/global/evaluations/EVALUATION_ID",
"evaluationSpec": {
 "querySetSpec": {
   "sampleQuerySet":
"projects/PROJECT_NUMBER/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID"
 },
 "searchRequest": {
   "servingConfig":
"projects/PROJECT_NUMBER/locations/global/collections/default_collect
ion/engines/APP_ID/servingConfigs/default_search"
 }
},
"state": "PENDING"
"createTime": "CREATION_DATETIME"
}
```

3. Retrieve the aggregate results. 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/lo
cations/global/evaluations/EVALUATION_ID"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`EVALUATION_ID`_ : the ID for your evaluation job that was returned in the previous step when you initiated the evaluation. 

<sup>Response</sup> 

You should receive a JSON response similar to the following. The status of the evaluation is shown as `PENDING` until the evaluation is complete. 

```
{
"name":
"projects/PROJECT_NUMBER/locations/global/evaluations/EVALUATION_ID",
"evaluationSpec": {
  "querySetSpec": {
    "sampleQuerySet":
"projects/PROJECT_NUMBER/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID"
  },
  "searchRequest": {
    "servingConfig":
"projects/PROJECT_NUMBER/locations/global/collections/default_collect
ion/engines/APP_ID/servingConfigs/default_search"
  }
},
"qualityMetrics": {
  "docRecall": {
    "top1": DOC_RECALL_TOP_1,
    "top3": DOC_RECALL_TOP_3,
    "top5": DOC_RECALL_TOP_5,
    "top10": DOC_RECALL_TOP_10
  },
  "docPrecision": {
    "top1": DOC_PRECISION_TOP_1,
    "top3": DOC_PRECISION_TOP_3,
    "top5": DOC_PRECISION_TOP_5,
    "top10": DOC_PRECISION_TOP_10
  },
  "docNdcg": {
    "top1": DOC_NDCG_TOP_1,
    "top3": DOC_NDCG_TOP_3,
    "top5": DOC_NDCG_TOP_5,
    "top10": DOC_NDCG_TOP_10
  },
  "pageRecall": {
    "top1": PAGE_RECALL_TOP_1,
    "top3": PAGE_RECALL_TOP_3,
    "top5": PAGE_RECALL_TOP_5,
    "top10": PAGE_RECALL_TOP_10
  },
  "pageNdcg": {
    "top1": PAGE_NDCG_TOP_1,
    "top3": PAGE_NDCG_TOP_3,
    "top5": PAGE_NDCG_TOP_5,
    "top10": PAGE_NDCG_TOP_10
   }
 },
"state": "SUCCEEDED",
"error": {},
"createTime": "CREATION_DATETIME",
"endTime": "END_DATETIME"
}
```

4. Retrieve query-level results. 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/lo
cations/global/evaluations/EVALUATION_ID:listResults"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`EVALUATION_ID`_ : the ID for your evaluation job that was returned in the previous step when you initiated the evaluation. 

<sup>Response</sup> 

You should receive a JSON response similar to the following. The status of the evaluation is shown as `PENDING` until the evaluation is complete. 

```
{
"evaluationResults": [
  {
    "sampleQuery": {
      "name":
"projects/PROJECT_NUMBER/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID/sampleQueries/QUERY_ID_1",
      "queryEntry": {
        "query": "SAMPLE_QUERY_1",
        "targets": [
          {
            "uri": "URI_1"
          }
        ]
      }
    },
    "qualityMetrics": {
      "docRecall": {
        "top1": DOC_RECALL_TOP_1,
        "top3": DOC_RECALL_TOP_3,
        "top5": DOC_RECALL_TOP_5,
        "top10": DOC_RECALL_TOP_10
      },
      "docPrecision": {
        "top1": DOC_PRECISION_TOP_1,
        "top3": DOC_PRECISION_TOP_3,
        "top5": DOC_PRECISION_TOP_5,
        "top10": DOC_PRECISION_TOP_10
      },
      "docNdcg": {
        "top1": DOC_NDCG_TOP_1,
        "top3": DOC_NDCG_TOP_3,
        "top5": DOC_NDCG_TOP_5,
        "top10": DOC_NDCG_TOP_10
      },
      "pageRecall": {
        "top1": PAGE_RECALL_TOP_1,
        "top3": PAGE_RECALL_TOP_3,
        "top5": PAGE_RECALL_TOP_5,
        "top10": PAGE_RECALL_TOP_10
      },
      "pageNdcg": {
        "top1": PAGE_NDCG_TOP_1,
        "top3": PAGE_NDCG_TOP_3,
        "top5": PAGE_NDCG_TOP_5,
        "top10": PAGE_NDCG_TOP_10
       }
     }
  },
  {
    "sampleQuery": {
      "name":
"projects/PROJECT_NUMBER/locations/global/sampleQuerySets/
SAMPLE_QUERY_SET_ID/sampleQueries/QUERY_ID_2",
      "queryEntry": {
        "query": "SAMPLE_QUERY_2",
        "targets": [
          {
            "uri": "URI_2"
          }
        ]
      }
    },
    "qualityMetrics": {
      "docRecall": {
        "top1": DOC_RECALL_TOP_1,
        "top3": DOC_RECALL_TOP_3,
        "top5": DOC_RECALL_TOP_5,
        "top10": DOC_RECALL_TOP_10
      },
      "docPrecision": {
        "top1": DOC_PRECISION_TOP_1,
        "top3": DOC_PRECISION_TOP_3,
        "top5": DOC_PRECISION_TOP_5,
        "top10": DOC_PRECISION_TOP_10
      },
      "docNdcg": {
        "top1": DOC_NDCG_TOP_1,
        "top3": DOC_NDCG_TOP_3,
        "top5": DOC_NDCG_TOP_5,
        "top10": DOC_NDCG_TOP_10
      },
      "pageRecall": {
        "top1": PAGE_RECALL_TOP_1,
        "top3": PAGE_RECALL_TOP_3,
        "top5": PAGE_RECALL_TOP_5,
        "top10": PAGE_RECALL_TOP_10
      },
      "pageNdcg": {
        "top1": PAGE_NDCG_TOP_1,
        "top3": PAGE_NDCG_TOP_3,
        "top5": PAGE_NDCG_TOP_5,
        "top10": PAGE_NDCG_TOP_10
       }
     }
  }
]
}
```

#### Understand the results

The following table describes the metrics that are returned in your evaluation results. 

|Nam|eDescription|Requiremen|
|---|---|---|
|`doc`|Recall per document, at various top-k cutoff levels.|The sample|
|`Reca`||query must|
|`ll`|Recall is the fraction of relevant documents retrieved out of all relevant<br>documents. For example,`top5`value signifies the following:|contain the<br>URI field.|
||For a single query, if 3 out of 5 relevant documents are retrieved in the to<br>the`docRecall`can be calculated as 3/5 or 0.6.|p-5,|

|`page`|Recall per page, at various top-k cutoff levels.|The|
|---|---|---|
|`Reca`||sample|
|`ll`|Recall is the fraction of relevant pages retrieved out of all relevant pages. For<br>example,`top5`value signifies the following:|query<br>must<br>|
||For a single query, if 3 out of 5 relevant pages are retrieved in the top-5, the<br>`pageRecall`can be calculated as 3/5 = 0.6|contain<br>the URI<br>and page<br>fields.|
|||Extractiv<br>answers<br>must be<br>enabled.|
|`doc`<br>`Ndcg`|Normalized discounted cumulative gain (NDCG) per document, at various<br>top-k cutoff levels.<br>NDCG measures the ranking quality, giving higher relevance to top results.<br>The NDCG value can be calculated for each query according to<br>Normalized<br>CDG<br>(https://en.wikipedia.org/wiki/Discounted_cumulative_gain#Normalized_DCG<br>.|)<br>The sample<br>query must<br>contain the<br>URI field.|
|`page`<br>`Ndcg`|Normalized discounted cumulative gain (NDCG) per page, at various top-k<br>cutoff levels.<br>NDCG measures the ranking quality, giving higher relevance to top results.<br>The NDCG value can be calculated for each query according to<br>Normalized<br>CDG<br>(https://en.wikipedia.org/wiki/Discounted_cumulative_gain#Normalized_DCG<br>.|)<br>The<br>sample<br>query<br>must<br>contain<br>the URI<br>and page<br>fields.|
|||Extractiv<br>answers<br>must be<br>enabled.|
|`doc`|Precision per document, at various top-k cutoff levels.|The sample|
|`Prec`<br>`isio`<br>`n`|Precision is the fraction of retrieved documents that are relevant. For<br>example,`top3`value signifies the following:|query must<br>contain the<br>URI field.|
||For a single query, if 4 out of 5 retrieved documents in the top-5 are relevant,<br>the`docPrecision`value can be calculated as 4/5 or 0.8.||

Based on the values of these supported metrics, you can perform the following tasks: 

- Analyze aggregated metrics: 

   - Examine overall metrics like average recall, precision, and normalized discounted cumulative gain (NDCG). 

   - These metrics provide a high-level view of your search engine's performance. 

- Review query-level results: 

   - Drill down into individual queries to identify specific areas where the search engine performs well or poorly. 

   - Look for patterns in the results to understand potential biases or shortcomings in the ranking algorithms. 

- Compare results over time: 

   - Run evaluations regularly to track changes in search quality over time. 

   - Use historical data to identify trends and assess the impact of any changes you make to your search engine. 

### What's next

- Use Cloud Scheduler to set up scheduled quality evaluation. For more information, see Use authentication with HTTP targets (/scheduler/docs/http-target-auth). 

Last updated 2026-10-14 UTC. 



## Gemini Enterprise

URL: https://docs.cloud.google.com/gemini/enterprise/docs/overview

Gemini Enterprise is an intranet search, AI assistant, and agentic platform. It empowers knowledge workers with generative AI and agentic workflows by leveraging data sources from across your organization. Gemini Enterprise includes prebuilt connectors for commonly-used third-party applications like Confluence, Jira, Microsoft SharePoint, and ServiceNow. This 

<!-- Start of picture text -->
Gemini Enterprise - Your front<br>Google Cloud<br>Watch on<br><!-- End of picture text -->

provides employees with a single, multimodal search interface offering permissions-aware access to enterprise information. Gemini Enterprise can also provide conversational assistance, answer complex questions, and host custom AI agents that apply generative AI contextually. 

### Editions and documentation

Gemini Enterprise is available in several editions: 

Business Edition 

Standard, Plus, Payas-you-go, and 

> For Business edition Frontline Editions documentation, visit the Business edition support This documentation covers center. all other editions. Compare features and capabilities across editions. Visit support center… Compare editions… 

### Explore documentation by role

Explore documentation tailored for your role: 

#### Administrators

Deploy and manage the platform, configure security policies, assign user licenses, and connect enterprise data sources from across your entire organization. 

Set up Gemini Enterpri… 

#### App users

Search enterprise data, collaborate, and interact with AI assistants and agents using the web and mobile apps. 

Get started… 

#### Developers

Authenticate programmatically, explore client libraries, and integrate REST and RPC APIs to build search and assistant features. 

Developer guide… 

### Use cases for Gemini Enterprise

You can use Gemini Enterprise to answer questions, carry out tasks, and iterate on deliverables based on connected data sources from across your organization. You can use Gemini Enterprise in the following ways: 

|Use case|Example prompts|
|---|---|
|Create images,<br>videos, and reports|Create a series of three images for a social media campaign promoting our<br>new line of artisanal coffee beans.|
||I'm attaching the latest company 10-K report. Analyze it and give me a<br>summary of the key financial highlights and risk factors.|
||Turn the attached blog post about our company's history into a short<br>documentary-style video, using archival photos and a professional<br>voiceover.|
|Handle<br>diitti tk|<br>I have a late fee in my expense report; what do I do to resolve it?|
|amnsrave as|<br>Help me book a conference room for my team meeting next Tuesday from<br>10 to 11 AM.|
|Research, ideate,<br>and plan|Summarize our best-performing campaigns from last year and give me<br>three new ideas for our upcoming holiday promotion.|
||My customer is Cymbal Insurance and I'm meeting with their Head of<br>Procurement on Thursday. Find their latest earnings report and give me a<br>list of talking points.|
||We are considering consolidating our shipping with a single logistics<br>provider. Can you research the pros and cons of a "single-provider"<br>strategy, and then identify the top three logistics partners for a company<br>of our size?|
|Learn about people<br>and projects|Find all the documentation related to our Go-To-Market strategy for the<br>new product line.|
||Who is Hao S. and what projects are they currently working on?|

For more ways to use Gemini Enterprise in your work, see Example use cases (/gemini/enterprise/docs/use-cases/example-use-cases). 

### Why use Gemini Enterprise?

Gemini Enterprise connects content across your organization to generate grounded and personalized answers using Google's premier knowledge discovery tools. 

With Gemini Enterprise, you can: 

- Process large volumes of enterprise data from multiple formats and platforms. 

- Sync and search across data from SaaS systems, such as Microsoft Sharepoint, Jira Cloud, and Confluence Cloud. 

- Enforce access-controlled search results and generative answers at scale. 

- Streamline agentic workflows and eliminate the need to switch between multiple AI assistants and agent applications. 

- Create and configure AI assistants offering generative answers from enterprise or public data. 

- Use out-of-the-box agents, available to you in the Agent Gallery (/gemini/enterprise/docs/agent-gallery). 

Gemini Enterprise offers an array of unique advantages for enterprises: 

- **Built-in trust** through SSO and user-level access. 

- **Google intelligence** that learns from user behavior and anticipates the next question. 

- **Broad connectivity** across cloud platforms, CRMs, productivity tools, and legacy systems. 

- **Enterprise-wide customization** with user-specific personalization. 

- **Customizable RAG agent** grounded on enterprise data from a wide variety of supported formats. 

- **Scalability** across geographies and languages. 

### Gemini Notebook Enterprise: AI-powered research and knowledge assistant

Gemini Notebook Enterprise is an AI-powered research and knowledge assistant that helps you to summarize information, brainstorm ideas, and write with confidence. You can use Gemini Notebook Enterprise alongside your Gemini Enterprise experience to create notebooks that contain your notes, sources, and ideas. 

### Next steps

For more information about Gemini Enterprise, see the following pages. 

- To learn about Gemini Enterprise and related products, see: 

   - Gemini Enterprise concepts (/gemini/enterprise/docs/concepts) 

   - What is Gemini Notebook Enterprise? 

   - (/gemini/enterprise/notebooklm-enterprise/docs/overview) 

   - Choose between Gemini Notebook Enterprise and Gemini Enterprise 

   - (/gemini/enterprise/docs/choose-product) 

- To learn about editions and specific features, see Compare editions of Gemini Enterprise (/gemini/enterprise/docs/editions). 

- To get started with using Gemini Enterprise, see Get started with Gemini Enterprise (/gemini/enterprise/docs/get-started). 

Last updated 2026-10-14 UTC.
