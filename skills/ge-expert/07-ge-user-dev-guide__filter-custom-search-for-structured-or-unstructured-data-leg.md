# Gemini Enterprise: user guide, Workflow Builder, developer guide / Filter custom search for structured or unstructured data (Legacy) to Get snippets and extracted content (Legacy)
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 487-527, extracted 2026-10-18

Contains:
- Filter custom search for structured or unstructured data (Legacy) (pages 487-494) https://docs.cloud.google.com/gemini/enterprise/docs/filter-search-metadata
- Filter searches by document-level relevance (Legacy) (pages 495-500) https://docs.cloud.google.com/gemini/enterprise/docs/filter-by-relevance
- Boost search results (Legacy) (pages 501-511) https://docs.cloud.google.com/gemini/enterprise/docs/boost-search-results
- Order results from structured data stores (Legacy) (pages 512-518) https://docs.cloud.google.com/gemini/enterprise/docs/order-structured-results
- Get snippets and extracted content (Legacy) (pages 519-527) https://docs.cloud.google.com/gemini/enterprise/docs/snippets

## Filter custom search for structured or unstructured data (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/filter-search-metadata

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

If you have a search app that uses structured data, or unstructured data with metadata, you can use the metadata to filter your search queries. This page explains how to use metadata fields to restrict your search to a specific set of documents. 

**Note:** Another approach to filters for structured data is to use document-level relevance filtering to reduce the number of results returned. For information about this Preview feature, see Filter searches by document-level relevance (/gemini/enterprise/docs/filter-by-relevance). 

### Before you begin

Make sure you have created an app and ingested structured data, or unstructured data with metadata. For more information, see Create a search app 

(/gemini/enterprise/docs/create-app). 

#### Metadata example

Review this example of metadata for four PDF files ( `document_1.pdf` , `document_2.pdf` , `document_3.pdf` , and `document_4.pdf` ) . This metadata would be in a JSON file in a Cloud Storage bucket, along with the PDF files. You can refer back to this example as you read through this page. 

```
{"id": "1", "structData": {"title": "Policy on accepting corrected claims",
"category": ["persona_A"]}, "content": {"mimeType": "application/pdf", "uri":
"gs://bucketname_87654321/data/document_1.pdf"}}
{"id": "2", "structData": {"title": "Claims documentation and reporting guidelines for
commercial members", "category": ["persona_A", "persona_B"]}, "content": {"mimeType":
"application/pdf", "uri": "gs://bucketname_87654321/data/document_2.pdf"}}
{"id": "3", "structData": {"title": "Claims guidelines for bundled services and
supplies for commercial members", "category": ["persona_B", "persona_C"]}, "content":
{"mimeType": "application/pdf", "uri":
"gs://bucketname_87654321/data/document_3.pdf"}}
{"id": "4", "structData": {"title": "Advantage claims submission guidelines",
"category": ["persona_A", "persona_C"]}, "content": {"mimeType": "application/pdf",
"uri": "gs://bucketname_87654321/data/document_4.pdf"}}
```

#### Filter expression syntax

Make sure you understand the syntax of the filter expression that you'll use to define your search filter. The filter expression syntax can be summarized by the following Extended Backus–Naur form 

(https://en.wikipedia.org/wiki/Extended_Backus%E2%80%93Naur_form#:%7E:text=In%20compute): 

- `# A single expression or multiple expressions that are joined by "AND" or "OR".` **`filter`** `=` **`expression`** `, { " AND " | "OR",` **`expression`** `};` 

- `# Expressions can be prefixed with "-" or "NOT" to express a negation.` **`expression`** `= [ "-" | "NOT " ],` 

- `# A parenthetical expression.` 

- `| "(", expression, ")"` 

- `# A simple expression applying to a text field.` 

- `# Function "ANY" returns true if the field exactly matches any of the literals.` 

- `(` **`text_field`** `, ":", "ANY", "(",` **`literal`** `, { ",",` **`literal`** `}, ")"` 

- `# A simple expression applying to a numerical field. Function "IN" returns true` 

- `# if a field value is within the range. By default, lower_bound is inclusive and` 

- `# upper_bound is exclusive.` 

- `|` **`numerical_field`** `, ":", "IN", "(",` **`lower_bound`** `, ",",` **`upper_bound`** `, ")"` 

- `# A simple expression that applies to a numerical field and compares with a double` 

- `value.` 

- `|` **`numerical_field`** `,` **`comparison`** `, double` 

- `# An expression that applies to a geolocation field with text/street/postal` 

- `address.` 

- `|` **`geolocation_field`** `, ":", "GEO_DISTANCE(", literal, ",", distance_in_meters, ")"` 

- `# An expression that applies to a geolocation field with latitude and longitude.` 

- `|` **`geolocation_field`** `, ":", "GEO_DISTANCE(", latitude_double, ",", longitude_double,` 

- `",", distance_in_meters, ")"` 

- `# Datetime field` 

- `|` **`datetime_field`** `,` **`comparison`** `, literal_iso_8601_datetime_format);` 

- `# A lower_bound is either a double or "*", which represents negative infinity.` 

- `# Explicitly specify inclusive bound with the character 'i' or exclusive bound` 

- `# with the character 'e'.` 

```
lower_bound = ( double, [ "e" | "i" ] ) | "*";
```

- `# An upper_bound is either a double or "*", which represents infinity.` 

- `# Explicitly specify inclusive bound with the character 'i' or exclusive bound` 

- `# with the character 'e'.` 

```
upper_bound = ( double, [ "e" | "i" ] ) | "*";
 # Supported comparison operators.
comparison = "<=" | "<" | ">=" | ">" | "=";
 # A literal is any double quoted string. You must escape backslash (\) and
 # quote (") characters.
literal = double quoted string;
text_field = text field - for example, category;
numerical_field = numerical field - for example, score;
geolocation_field = field of geolocation data type - for example home_address,
location;
datetime_field = field of datetime data type - for example creation_date,
expires_on;
literal_iso_8601_datetime_format = either a double quoted string representing ISO
8601 datetime or a numerical field representing microseconds from unix epoch.
```

### Search using a metadata filter

To search using a metadata filter, follow these steps: 

1. Determine the metadata field to use for filtering your search queries. For example, for the metadata in Before you begin (#before-you-begin), you could use the `category` field as a search filter. Your users could filter on `persona_A` , `persona_B` , or `persona_C` , so their search is restricted to the documents associated with the persona that they're interested in. 

2. Make the metadata field indexable: 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page and in the navigation menu, click **Apps** . 

Go to the Apps page (https://console.cloud.google.com/gemini-enterprise/apps) 

- b. Click your search app. 

- c. In the navigation menu, click **Data** . 

- d. Click the **Schema** tab. This tab shows current field settings. 

**Note:** The **Schema** tab appears only for data stores that contain structured data or unstructured data with metadata. 

- e. Click **Edit** . 

- f. Select the **Indexable** checkbox for the field that you want to make indexable. 

   - g. Click **Save** . For more information, see Configure field settings (/gemini/enterprise/docs/configure-field-settings). 

3. Find your data store ID. If you already have your data store ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page and in the navigation menu, click **Data Stores** . 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

   - b. Click the name of your data store. 

   - c. On the **Data** page for your data store, get the data store ID. 

4. Preview search results. 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/locations/globa
l/collections/default_collection/dataStores/DATA_STORE_ID/servingConfigs/default_s
earch:search" \
-d '{
"query": "QUERY",
"filter": "FILTER"
}'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`DATA_STORE_ID`_ : the ID your data store. 

- _`QUERY`_ : the query text to search. 

- _`FILTER`_ : optional. A text field that lets you to filter on a specified set of fields, using filter expression syntax (#filter-expression-syntax). The default value is an empty string, which means no filter is applied. 

For example, say that you imported the four PDF files with metadata from Before you begin (#before-you-begin). You want to search for documents that contain the word "claims", and only query documents with a `category` value of `persona_A` . You would do that by including the following statements with your call: 

```
"query": "claims",
"filter": "category: ANY(\"persona_A\")"
```

For more information, see the REST tab at Preview search results for an app with structured or unstructured data 

(/gemini/enterprise/docs/preview-search-results#structured-unstructured). 

<sup>Click for an example response.</sup> 

If you perform a search like the one in the preceding procedure, you can expect to get a response similar to the following. Notice that the response includes the three documents that have a `category` value of `persona_A` . 

```
{
"results": [
{
  "id": "2",
  "document": {
    "name":
"projects/abcdefg/locations/global/collections/default_collection/dataStores/searc
h_store_id/branches/0/documents/2",
    "id": "2",
    "structData": {
      "title": "Claims documentation and reporting guidelines for commercial
members",
      "category": [
        "persona_A",
        "persona_B"
      ]
    },
    "derivedStructData": {
      "link": "gs://bucketname_87654321/data/document_2.pdf",
      "extractive_answers": [
        {
          "pageNumber": "1",
          "content": "lorem ipsum"
        }
      ]
    }
  }
},
{
  "id": "1",
  "document": {
    "name":
"projects/abcdefg/locations/global/collections/default_collection/dataStores/searc
h_store_id/branches/0/documents/1",
    "id": "1",
    "structData": {
      "title": "Policy on accepting corrected claims",
      "category": [
        "persona_A"
      ]
    },
    "derivedStructData": {
      "extractive_answers": [
        {
          "pageNumber": "2",
          "content": "lorem ipsum"
        }
      ],
      "link": "gs://bucketname_87654321/data/document_1.pdf"
    }
  }
},
{
  "id": "4",
  "document": {
    "name":
"projects/abcdefg/locations/global/collections/default_collection/dataStores/searc
h_store_id/branches/0/documents/4",
    "id": "4",
    "structData": {
      "title": "Advantage claims submission guidelines",
      "category": [
        "persona_A",
        "persona_C"
      ]
    },
    "derivedStructData": {
      "extractive_answers": [
        {
          "pageNumber": "47",
          "content": "lorem ipsum"
        }
      ],
      "link": "gs://bucketname_87654321/data/document_4.pdf"
    }
  }
}
],
"totalSize": 330,
"attributionToken":
"UvBRCgsI26PxpQYQs7vQZRIkNjRiYWY1MTItMDAwMC0yZWIwLTg3MTAtMTQyMjNiYzYzMWEyIgdHRU5FU
klDKhSOvp0VpovvF8XL8xfC8J4V1LKdFQ",
"guidedSearchResult": {},
"summary": {}
}
```

### Examples of filter expressions

The following table provides examples of filter expressions. 

|Filter|Only returns results for documents where:|
|---|---|
|`category: ANY(\"persona_A\")`|the text field`category`is`persona_A`|
|`score: IN(*, 100.0e)`|the numerical field`score`is greater than<br>negative infinity and less than 100.0|
|`non-smoking = \"true\"`|the boolean`non-smoking`is true|
|`pet-friendly = \"false\"`|the boolean`pet-friendly`is false|
|`manufactured_date = \"2023\"`|the`manufactured date`is any time in 2023|
|`manufactured_date >= \"2024-04-16\"`|the`manufactured_date`is on or after April 16,<br>2024|
|`manufactured_date < \"2024-04-16T12:00:00-`<br>`07:00\"`|the`manufactured_date`is before noon Pacific<br>Daylight Time on April 16, 2024|
|`office.location:GEO_DISTANCE(\"1600`<br>`Amphitheater Pkwy, Mountain View, CA,`<br>`94043\", 500)`|the geolocation field`office.location`is within<br>a 500 m distance of 1600 Amphitheater Pkwy|
|`NOT office.location:GEO_DISTANCE(\"Palo Alto,`<br>`CA\", 1000)`|<br>the geolocation field`office.location`is not<br>within a 1 km radius of Palo Alto, California.|
|`office.location:GEO_DISTANCE(34.1829, -121.`<br>`293, 500)`|the geolocation field`office.location`is within<br>a 500 m radius of latitude 34.1829 and longitude<br>-121.293|
|`category: ANY(\"persona_A\") AND score: IN(*,`<br>`100.0e)`|<br>`category`is`persona_A`and`score`is less than<br>100|
|`office.location:GEO_DISTANCE(\"Mountain View,`<br>`CA\", 500) OR office.location:GEO_DISTANCE(`<br>`\"Palo Alto, CA\", 500)`|<br>`office.location`is within a 500 m distance of<br>either Mountain View or Palo Alto.|

Filter 

Only returns results for documents where: 

```
(price<175 AND pet-friendly = \"true\") OR
(price<125 AND pet-friendly = \"false\")
```

`price` is less than 175 and I can bring my pet, or `price` is less than 125 and I can't bring my pet 

### What's next

- To understand the impact of filters on the search quality, evaluate the search quality. For more information, see Evaluate search quality 

- (/gemini/enterprise/docs/evaluate-search-quality). 

Last updated 2026-10-14 UTC. 



## Filter searches by document-level relevance (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/filter-by-relevance

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the GCP Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the Generative AI Preview terms and conditions (https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the Cloud Data Processing Addendum (https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

When searching in your Gemini Enterprise app, you can apply a relevance threshold so that only the documents that meet this threshold are returned as results. This page explains how to specify a relevance threshold in order to reduce the number of documents returned in queries. 

### About filtering by document-level relevance

Each document returned by a search query is given a relevance level, which indicates the relevance of the returned document to the query. When you make a query through an API call, you can set a relevance threshold. Setting a high relevance threshold can reduce the number of documents returned by a query. 

For example, if you find that search is returning too many documents of insufficient relevance to your users, set the relevance threshold to high to narrow the results to only those few that are most relevant. If the high setting is too restrictive, try the medium setting. 

**Note:** This document-level relevance filtering feature is different from and less precise than the document-relevance score 

(/gemini/enterprise/docs/preview-search-results#relevance-scores) that can be returned for search results. 

### Data types and apps supported for document-level relevance filter

The document-level relevance filter can be applied to data stores with following kinds of data: 

Website data with advanced website indexing 

- Custom unstructured data 

- Custom structured data 

The document-level relevance filter doesn't work for data stores with basic website indexing, media data, or healthcare data. 

Furthermore, the document-level relevance filter can't be used with blended search apps. Blended search apps are apps that are connected to multiple data stores. 

### Other kinds of filters

The document-level relevance filter is not the only way you can filter data returned by queries. You can also use filter expressions to filter results based on metadata (in unstructured data with metadata data stores) and field values (in structured data stores). 

For information, see Filter search with metadata 

(/gemini/enterprise/docs/filter-search-metadata). 

If you use both a filter expression and the document-level relevance filter, the filter expression is applied first to the results and then the document-level relevance filter is applied. 

### Before you begin

Make sure you have created an app and data store and have ingested data into your data store. For more information, see Create a first-party app 

(/gemini/enterprise/docs/create-app). See also Data types and apps supported for document-level relevance filter (#supported). 

### Search and filter results by document-level relevance

To filter by relevance, follow these steps: 

**Note:** You can search over an app using the **`engines.servingConfigs.search`** (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConf igs/search) 

method and you can search over a data store using the **`dataStores.servingConfigs.search`** (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.servingC onfigs/search) 

method. For the following procedure, Google recommends searching using the **`engines.servingConfigs.search`** method. 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

- b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. To filter search by document-level relevance, use the `relevanceThreshold` field with the `engines.servingConfigs.search` 

(/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.se rvingConfigs/search) 

method. 

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth application-default
print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfigs/de
fault_search:search" \
-d '{
"servingConfig":
"projects/PROJECT_ID/locations/global/collections/default_collection/engin
es/APP_ID/servingConfigs/default_search",
"query": "QUERY",
"relevanceThreshold": "RELEVANCE_THRESHOLD"
}'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : the query text to search. 

- _`RELEVANCE_THRESHOLD`_ : one of the following: `HIGH` , `MEDIUM` , `LOW` , `LOWEST` . 

<sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-search-
app/servingConfigs/default_search:search" \
-d '{
"servingConfig": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-search-
app/servingConfigs/default_search",
"query": "What is the check grounding API",
"relevanceThreshold": "HIGH"
}'
{
"results": [
{
 "id": "a082e70352c073a4443502477255bd2a",
 "document": {
   "name":
"projects/123456/locations/global/collections/default_collection/dataStore
s/my-data-store/branches/0/documents/a082e70352c073a4443502477255bd2a",
   "id": "a082e70352c073a4443502477255bd2a",
   "derivedStructData": {
     "displayLink": "cloud.google.com",
     "link": "https://cloud.google.com/example/docs/check-grounding",
     "htmlTitle": "Check grounding | Example | Google Cloud",
     "title": "Check grounding | Example | Google Cloud"
   }
 }
}
],
"totalSize": 1,
"attributionToken": "f_B-
CgwIidzwswYQyue15gESJDY2N2M1NmJkLTAwMDAtMjk3Ni1iMGI4LTg4M2QyNGZmNTZhOCIHR0
VORVJJQypAjr6dFavEii3b7Ygt3o-aIoCymiLC8J4Vo4CXIra3jC3Usp0V24-
aIt7tiC3n7YgtrsSKLeTtiC2DspoixsvzFw",
"guidedSearchResult": {},
"summary": {}
}
```

Here, the relevance threshold is set to high, so only the most relevant results are returned. In this example, only one document was determined to be highly relevant. 

3. Test multiple queries with different thresholds to determine the best threshold settings for your data and application. 

Last updated 2026-10-14 UTC. 



## Boost search results (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/boost-search-results

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

You can specify boost conditions in your search request to promote or demote certain documents in your search results. When a document fulfills the specified conditions, boost values are applied to it and the results are ordered accordingly. You can also specify custom numerical values and timestamp values that let you order the results based on parameters such as popularity and freshness. 

The boost specification in a search request is different from a boost control that's attached to a serving config. For more information about boost controls, see About boost controls (/gemini/enterprise/docs/configure-serving-controls#boost). 

This page describes the following types of boost specifications: 

- Boost with a fixed condition (#fixed-boost) Boost using custom numerical attributes (#custom-numerical-attr-boost) Boost according to freshness (#freshness-boost) 

### Boost with a fixed condition

To boost results by a fixed amount based on whether they satisfy a condition, do the following: 

1. Specify the boost specification in the `boostSpec` (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.evaluations#BoostSpec ) field when you send a `servingConfigs.search` (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines.ser vingConfigs/search) request. 

```
{
 "boostSpec": {
   "conditionBoostSpecs": {
     "condition": "BOOST_CONDITION",
     "boost":BOOST_VALUE
   }
 }
}
```

The specification contains the following parameters: 

- _`BOOST_CONDITION`_ : a text filter expression 

- (/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax) to select the documents to which boost is applied. The filter must evaluate to a boolean value. 

- _`BOOST_VALUE`_ : a floating point number in the range [-1,1]. When the value is negative, results are demoted (they appear lower down in the results). When the value is positive, results are promoted (they appear higher up in the results). 

#### Example use case

Suppose your data store contains data about hotels and their star ratings. You want to boost hotels with star ratings greater than or equal to three. The star rating is available in the `star_rating` numerical field. You can specify the `condition` in the `boostSpec` as `star_rating >= 3.0` and a boost value of 0.7 to boost all hotels with `star_rating` of 3.0 or higher by an equal amount. 

```
{
 "boostSpec": {
   "conditionBoostSpecs": {
     "condition": "star_rating>=3.0",
     "boost": 0.7
   }
 }
```

### Boost using custom numerical attributes

You can boost results based on custom numerical attributes in a piecewise linear (https://en.wikipedia.org/wiki/Piecewise_linear_function) manner by specifying control points and their corresponding boost values. 

To specify a boost specification using custom numerical attributes, do the following: 

1. Specify the boost specification in the `boostSpec` 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.evaluations#BoostSpec ) field when you send a `servingConfigs.search` 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines.ser vingConfigs/search) 

request. 

```
{
 "boostSpec": {
   "conditionBoostSpecs": {
       "condition": "BOOST_CONDITION",
       "boostControlSpec": {
         "attributeType": "NUMERICAL",
         "interpolationType": "LINEAR",
         "fieldName": "CUSTOM_ATTRIBUTE_FIELD_NAME",
         "controlPoints": [
           {
             "attributeValue": "CUSTOM_ATTRIBUTE_VALUE_1",
             "boostAmount": BOOST_AMOUNT_1
           },
           {
             "attributeValue": "CUSTOM_ATTRIBUTE_VALUE_2",
             "boostAmount":BOOST_AMOUNT_2
           }
         ]
       }
   }
 }
}
```

The specification contains the following parameters: 

- _`BOOST_CONDITION`_ : a text filter expression 

- (/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax) to select the documents to which boost is applied. The filter must evaluate to a boolean value. 

- _`CUSTOM_ATTRIBUTE_FIELD_NAME`_ : the field name of the custom numerical attribute whose value decides the boost amount. 

- _`CUSTOM_ATTRIBUTE_VALUE`_ : the numerical value of the custom attribute for a given control point with a string data type. For example, `"3.3"` or `"12"` . For more information, see ControlPoint 

- (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.evaluations#cont rolpoint) 

- _`BOOST_AMOUNT`_ : a floating point number in the range [-1,1]. When the value is negative, results are demoted (they appear lower down in the results). When the value is positive, results are promoted (they appear higher up in the results). Indicates the boost amount mapped to the custom attribute for a given control point. 

When a document in the search result meets the specified condition, a boost amount is applied as follows: 

|Attribute value|Boost amount|
|---|---|
|Less than the first<br>control point|Is equal to the boost amount of the first control point|
|Equal to control point|Is equal to the mapped boost amount|
|Between control points|Is calculated by<br>linear interpolation<br>(https://en.wikipedia.org/wiki/Linear_interpolation)|
|Greater than the last<br>control point|Is equal to the boost amount of the last control point|

#### Example use case

Suppose your data store contains data about hotels and their star ratings. You want to boost the hotel search results in proportion to their star ratings. You can define the boost specification as follows: 

```
{
 "boostSpec": {
   "conditionBoostSpecs": {
       "condition": "star_rating >= 3.0",
       "boostControlSpec": {
         "attributeType": "NUMERICAL",
         "interpolationType": "LINEAR",
         "fieldName": "star_rating",
         "controlPoints": [
           {
             "attributeValue": "3.5",
             "boostAmount": 0.25
           },
           {
             "attributeValue": "4.0",
             "boostAmount": 0.30
           },
           {
             "attributeValue": "4.5",
             "boostAmount": 0.32
           }
         ]
       }
   }
 }
}
```

For this scenario, the search results are boosted as follows: 

|Star rating|Boost amount|
|---|---|
|less than or equal to 3.5|0.25|
|between 3.5 and 4.0|between 0.25 and 0.30, calculated using linear interpolation|

|Star rating|Boost amount|
|---|---|
|equal to 4.0|0.30|
|between 4.0 and 4.5|between 0.30 and 0.32, calculated using linear interpolation|
|greater than or equal to 4.5|0.32|

### Boost according to freshness

You can boost results based on datetime attributes in a piecewise linear (https://en.wikipedia.org/wiki/Piecewise_linear_function) manner by specifying control points and their corresponding boost values. 

To specify a boost specification using custom datetime attributes, do the following: 

1. Specify the boost specification in the `boostSpec` 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.evaluations#BoostSpec ) field when you send a `servingConfigs.search` 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines.ser vingConfigs/search) request. 

```
{
 "boostSpec": {
   "conditionBoostSpecs": {
       "condition": "BOOST_CONDITION",
       "boostControlSpec": {
         "fieldName": "DATETIME_FIELD_NAME",
         "attributeType": "FRESHNESS",
         "interpolationType": "LINEAR",
         "controlPoints": [
           {
             "attributeValue": "DURATION_VALUE_1",
             "boostAmount":BOOST_AMOUNT_1
           },
           {
             "attributeValue": "DURATION_VALUE_2",
             "boostAmount":BOOST_AMOUNT_2
           }
         ]
       }
   }
 }
}
```

The specification contains the following parameters: 

- _`BOOST_CONDITION`_ : a text filter expression 

- (/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax) to select the documents to which boost is applied. The filter must evaluate to a boolean value. 

- _`DATETIME_FIELD_NAME`_ : the field name of a custom `DATETIME` attribute, such as date of publication or date of last update, or a predefined Googleinferred attribute, such as `datePublished` . 

- _`DURATION_VALUE`_ : the duration value in `dayTimeDuration` data type (https://www.w3.org/TR/xmlschema11-2/#dayTimeDuration) that decides the freshness of a document. This is calculated as the duration between the datetime when the search is performed and the datetime of the custom datetime attribute of a document. The duration value must be specified according to the ISO 8601 format in the pattern `[nD][T[nH][nM][nS]]` . For example, the duration between January 1, 2024 and March 1, 2024 can be expressed as `59D` . Similarly, the duration of two and a half days can be expressed as `2DT12H` . For more information, see ControlPoint 

- (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.evaluations#cont rolpoint) 

- _`BOOST_AMOUNT`_ : a floating point number in the range [-1,1]. When the value is negative, results are demoted (they appear lower down in the results). When the value is positive, results are promoted (they appear higher up in the results). Indicates the boost amount mapped to the custom datetime attribute for a given control point. 

When a document in the search result meets the specified condition, a boost amount is applied as follows: 

|Duration value|Boost amount|
|---|---|
|Less than the first control point|Is equal to the boost amount of the first control point|
|Equal to a given control point|Is equal to the mapped boost amount|
|Between control points|Is calculated by linear interpolation|
|Greater than the last control point|Is equal to the boost amount of the last control point|

#### Example use case using a custom datetime attribute

Suppose your data store contains structured data where each document has a publication date. You want to boost the search results in proportion to their freshness. You can define the boost specification as follows: 

```
{
 "boostSpec": {
   "conditionBoostSpecs": {
       "condition": true,
       "boostControlSpec": {
         "fieldName": "publication_date",
         "attributeType": "FRESHNESS",
         "interpolationType": "LINEAR",
         "controlPoints": [
           {
             "attributeValue": "7D",
             "boostAmount": 0.40
           },
           {
             "attributeValue": "30D",
             "boostAmount": 0.37
           },
           {
             "attributeValue": "60D",
             "boostAmount": 0.32
           },
           {
             "attributeValue": "90D",
             "boostAmount": 0
           }
```

<!-- Start of picture text -->
         ]<br>       }<br>   }<br> }<br>}<br><!-- End of picture text -->

For this scenario, the search results are boosted as follows: 

|Freshness|Boost amount|
|---|---|
|less than or equal to 7 days|0.40|
|between 7 and 30 days|between 0.40 and 0.37, calculated using linear interpolation|
|equal to 30 days|0.37|
|between 30 and 60 days|between 0.37 and 0.32, calculated using linear interpolation|
|equal to 60 days|0.32|
|between 60 and 90 days|between 0.32 and 0.0, calculated using linear interpolation|
|greater than or equal to 90 days|0.0|

### Regulate boost amount with relevance filter

In addition to factors that influence the ranking of a result, such as keyword matching, context matching, and relevance, the boost condition impacts the ranking of a result significantly. Therefore, you must carefully calibrate the boost amount especially when using the `boostSpec` field with relevance filter. For more information on relevance filter, see Filter searches by document-level relevance (/gemini/enterprise/docs/filter-by-relevance). 

Suppose you have different documents with different published dates. For a particular query, the following table represents the absolute ranking without implementing any boost amount or relevance filters and indicates the relevance of the documents to query. 

|Document|Published date|Relevance|Ranking|
|---|---|---|---|
|A|Feb 1, 2024|High|#1|
|B|Mar 1, 2024|High|#2|
|C|Apr 1, 2024|Lowest|#3|
|D|May 1, 2024|Medium|#4|
|E|Jun 1, 2024|Low|#5|

On Jun 6, 2024 you add the following search conditions in your search request: Relevance filter set to `LOW` . 

- Boost value such that documents published during the last 31 days are boosted by a value of 0.7 and documents older than a week but fresher than 60 days are boosted by value of 0.6. 

In your search output, the results are first filtered by relevance and then the boost amount is applied. Therefore, the applied conditions alter the ranking of the pages in the results in the following manner: 

|Document|Published date|Relevance|Ranking|
|---|---|---|---|
|E|Jun 1, 2024|Low|#1|
|D|May 1, 2024|Medium|#2|
|A|Feb 1, 2024|High|#3|
|B|Mar 1, 2024|High|#4|

The result with the lowest relevance is filtered out because of the relevance filter. The documents that are less relevant to a query are ranked as top results because they are boosted by a large boost amount. The more relevant results are ranked lower. 

Therefore, Google recommends that you start the boost amount from a low, precise value and adjust the value depending on the search output. In this example, 

starting with boost amounts of 0.1 or less might fetch more relevant results on the top. 

### What's next

- Make a search request (/gemini/enterprise/docs/preview-search-results) with the boost specification in the `boostSpec` field. 

- To understand the impact of boost on the search quality of a custom search app, evaluate the search quality. For more information, see Evaluate search quality (/gemini/enterprise/docs/evaluate-search-quality). 

Last updated 2026-10-14 UTC. 



## Order results from structured data stores (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/order-structured-results

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

**Note:** This feature is a Preview offering, subject to the "Pre-GA Offerings Terms" of the GCP Service Specific Terms (https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the launch stage descriptions (https://cloud.google.com/products#product-launch-stages). Further, by using this feature, you agree to the Generative AI Preview terms and conditions 

(https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). For this feature, you can process personal data as outlined in the Cloud Data Processing Addendum (https://cloud.google.com/terms/data-processing-addendum), subject to applicable restrictions and obligations in the Agreement (as defined in the Preview Terms). 

This page explains how to order the results of a search query made on structured data stores and on unstructured data stores with metadata. 

### Supported data types for ordering the results

These are the field types that you can have your search results ordered by: 

```
string
number
```

- `datetime` 

- `geolocation` 

### Before you begin

Make sure that you have an app with a data store that contains structured data or unstructured data with metadata. 

### Order your search results

To order the search results for a structured data store or for an unstructured data store with metadata, follow these steps: 

REST 

(#rest) 

To use the API to order your search results for an app with structured data or unstructured data with metadata, use the `engines.servingConfigs.search` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.serving Configs/search) 

method: 

**Note:** You can search over an app using the **`engines.servingConfigs.search`** (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servi ngConfigs/search) 

method and you can search over a data store using the 

**`dataStores.servingConfigs.search`** 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.se rvingConfigs/search) 

method. For the following procedure, Google recommends searching using the **`engines.servingConfigs.search`** method. 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

- b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. Make a search query and include the `orderBy` field. 

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/l
ocations/global/collections/default_collection/engines/APP_ID/serving
Configs/default_search:search" \
-d '{
"servingConfig":
"projects/PROJECT_ID/locations/global/collections/default_collection/
engines/APP_ID/servingConfigs/default_search",
"query": "QUERY",
"orderBy": "ORDER_BY"
}'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project.. 

- _`APP_ID`_ : the ID of the app.. 

- _`QUERY`_ : the query text to search. 

- _`ORDER_BY`_ : the order in which the results are arranged. The default sort order is ascending. For example, specifying `date` returns results from the oldest to the newest. To get descending sort order, append `desc` to the `date` value—for example, `date desc` . For more examples, see `orderBy` examples (#examples). 

<sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
 "https://discoveryengine.googleapis.com/v1alpha/projects/my-
project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:search" \
-d '{
   "query": "hotel",
   "orderBy": "rating desc"
  }'
{
"results": [
{
 "id": "10d480b19c256bb1",
 "document": {
   "name":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-store/branches/0/documents/10d480b19c256bb1",
   "id": "10d480b19c256bb1",
   "structData": {
     "available_date": "2023-11-05",
     "amenities": [
       "Lake Views",
       "Private Beach",
       "Spa",
       "Water Activities"
     ],
     "room_types": [
       "Lakefront Suite",
       "Deluxe Room",
       "Cottage"
     ],
     "location": {
       "address": "988 Serenity Circle, Tranquil Town, NV 89501,
USA"
     },
     "rating": 4.6,
     "id": 11,
     "price_per_night": 220.5,
     "title": "Serenity Springs Hotel"
   }
 }
},
{
 "id": "9ffae8af37cc8b63",
 "document": {
   "name":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-store/branches/0/documents/9ffae8af37cc8b63",
   "id": "9ffae8af37cc8b63",
   "structData": {
     "title": "Riverfront Plaza Hotel",
     "rating": 4.2,
     "location": {
       "address": "101 Main St, Anytown, CA 94501, USA"
     },
     "price_per_night": 145.8,
     "amenities": [
       "Fitness Center",
       "Conference Rooms",
       "Restaurant",
       "Valet Parking"
     ],
     "id": 3,
     "room_types": [
       "Executive Suite",
       "King Room",
       "Double Queen"
     ],
     "available_date": "2023-11-15"
   }
 }
},
{
 "id": "3be9e854d8f3a47f",
 "document": {
   "name":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-store/branches/0/documents/3be9e854d8f3a47f",
   "id": "3be9e854d8f3a47f",
   "structData": {
     "amenities": [
       "Oceanfront Views",
       "Pool",
       "Spa",
       "Beachside Dining"
     ],
     "available_date": "2023-09-18",
     "location": {
       "address": "449 Oceanfront Drive, Seaside Resort, CA 92007,
USA"
     },
     "id": 13,
     "title": "Ocean Breeze Hotel",
     "room_types": [
       "Ocean View Suite",
       "Deluxe Room",
       "Family Suite"
     ],
     "rating": 4.1,
     "price_per_night": 180
   }
 }
}
],
"totalSize": 3,
"attributionToken":
"wAHwvwoMCNDYz7UGEMCklrsCEiQ2NmIzYmU5My0wMDAwLTIxMDUtYmUyNy01ODI0Mjlj
MzdlZTQiB0dFTkVSSUMqgAHd1akt3e2ILebtiC2CspoigLKaIpjeqC-q-
LMtjr6dFeqCsS2W3qgvwvCeFaz4sy2jgJcinta3LeiCsS3b7Ygt5O2ILa3Eii3Usp0Vpp
-VLZzWty359rMt-_azLaCJsy3dj5oixcvzF6vEii2iibMttreMLd_VqS3bj5oipJ-
VLQ",
"guidedSearchResult": {},
"summary": {}
}
```

In this example, the documents that contain the word "hotel" are ordered by rating, from the Serenity Springs Hotel with a 4.6 rating to the Ocean Breeze Hotel with a 4.1 rating. 

`orderBy` examples 

To order on a string field called `title` : 

- `"orderBy": "title"` to return the documents in ascending alphabetic order according to title. 

- `"orderBy": "title desc"` to return the documents sorted in reverse alphabetic order (from Z to A) according to the title. 

To order on a number field called `rating` : 

   - `"orderBy": "rating"` to order from the lowest to the highest rated documents. 

   - `"orderBy": "rating desc"` to order from the highest to the lowest rated documents. 

- To order on a datetime field called `available_date` : 

   - `"orderBy": "available_date"` to order from the soonest available document to the farthest out. 

   - `"orderBy": "available_date desc"` to order from the document with the farthest out available date to the one soonest available. 

To order according to geolocation on a field called `location` : 

- `"orderBy": "GEO_DISTANCE(location, \"Mountain View, CA\")"` sorts the documents in order from those nearest to Mountain View to those farthest from Mountain View. 

- `"orderBy": "GEO_DISTANCE(location, 37.38, -122.08) desc"` sorts the documents in order from farthest to nearest to the location 37.38°N and 122.08°W. 

Last updated 2026-10-14 UTC. 



## Get snippets and extracted content (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/snippets

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

Gemini Enterprise can provide search snippets, extractive answers, and extractive segments with each search response to enhance your results. 

- **Snippets** (#snippets): A snippet is a brief extract of text from the search result document that provides a preview of a search result's content. It includes hit highlighting that you can render in your UI. Snippets are typically displayed under each search result to help end users assess the relevance and usefulness of that result. Snippets are available for data stores with unstructured data. 

- **Extractive answers** (#extractive-answers): An extractive answer is verbatim text that is returned with each search result. It is extracted directly from the original document. Extractive answers are typically displayed near the top of web pages to provide an end user with a brief answer that is contextually relevant to their query. Extractive answers are available for data stores with unstructured data. 

- **Extractive segments** (#extractive-segments): An extractive segment is verbatim text that is returned with each search result. An extractive segment is usually more verbose than an extractive answer. Extractive segments can be displayed as an answer to a query, and can be used to perform postprocessing tasks and as input for large language models to generate answers or new text. Extractive segments are available for data stores with unstructured data. 

### Examples

The following examples help illustrate the differences between snippets, extractive answers, and extractive segments. 

**Query:** "what is example product?" 

Snippet: 

To enable this, we are announcing our new **Example Google Product** , the fastest way for developers to jumpstart the creation of apps such as bots, ... 

Extractive answer: 

Example Google Product allows developers to quickly ship new experiences including bots, chat interfaces, custom search engines, digital assistants, and more. Developers have API access to Google's foundation models and can use out-of-the-box templates to jumpstart the creation of gen apps in minutes or hours. 

Extractive segment: 

Businesses and governments also want to make customer, partner, and employee interactions more effective and helpful with this new AI technology. To enable this, we are announcing our new Example Google Product. 

Example Google Product allows developers to quickly ship new experiences including bots, chat interfaces, custom search engines, digital assistants, and more. Developers have API access to Google's foundation models and can use out-of-the-box templates to jumpstart the creation of gen apps in minutes or hours. With Example Google Product, developers will also: 

Combine organizational data and information retrieval techniques to provide relevant answers. 

Search and respond with more than just text. 

Combine natural conversations with structured flows. 

Don't just inform — transact. 

### Snippets

Snippets are short pieces of extracted verbatim from each search result document. They include hit highlighting in bold HTML tags for rendering previews of search results in a UI. Typically, snippets are rendered as preview text underneath a search result to help end users decide if clicking that search result will be useful. 

Snippets are available for unstructured data. 

#### Get snippets

To get snippets: 

1. Send a search request that includes `ContentSearchSpec.SnippetSpec` (/gemini/enterprise/docs/reference/rest/v1/ContentSearchSpec#snippetspec) and sets `returnSnippet` to true. 

The following example of `SnippetSpec` specifies that a snippet can be returned for each search result. 

```
"contentSearchSpec":
{
 "snippetSpec":
 {
   "returnSnippet": true
 }
}
```

`returnSnippet` : If set to `true` , return a snippet. 

2. Get snippets from the search response. Snippets are returned with each search result in `derivedStructData.snippets` . 

In this example of a document that was returned as one of the results in a search response, a snippet with bold hit highlighting is included with the result: 

```
{
 "id": "54321",
 "document": {
   "name":
"projects/123/locations/global/collections/default_collection/dataStores/e
xample-datastore/branches/0/documents/54321",
   "id": "54321",
   "derivedStructData": {
     "link": "gs://cloud-samples-data/gen-app-builder/search/alphabet-
investor-pdfs/2008_google_annual_report.pdf",
     "snippets": [
       {
         "snippet": "Google Chrome. Google Chrome is an open-source
browser that combines a minimal design with technologies to make the web
faster, safer, and easier to navigate.",
         "snippet_status": "SUCCESS"
       }
     ]
   }
 }
}
```

- `snippet` : Contains a snippet generated for the document search result. Hit highlighting is included in bold HTML tags. 

- `snippet_status` : If a snippet is generated, this field is returned as `SUCCESS` . If no snippet is generated, this field is returned as `NO_SNIPPET_AVAILABLE` . 

### Extractive answers

An extractive answer is a section of text derived verbatim from a document. When a document is returned as a search result in a search response, a relevant extractive answer can be returned with that result. 

An extractive answer can be text such as a paragraph, table, or bulleted list that is extracted from the search result document. Extractive answers are shorter than extractive segments (#extractive-segments). 

Extractive answers can be used as an alternative to summarized responses in cases where precise, verbatim answers are preferable to rephrased summaries. 

Extractive answers are available for data stores with unstructured data. 

#### Get extractive answers

To get extractive answers: 

1. Send a search request that uses `ContentSearchSpec.extractiveContentSpec` (/gemini/enterprise/docs/reference/rest/v1/ContentSearchSpec#extractivecontentspec) to specify `maxExtractiveAnswerCount` . 

The following example of `extractiveContentSpec` specifies that an answer can be returned for each search result. 

```
"contentSearchSpec":
{
 "extractiveContentSpec": {
   "maxExtractiveAnswerCount": 1
 }
}
```

   - `maxExtractiveAnswerCount` : The number of extractive answers to return for each search result. The default value is 0 and the maximum is 5. 

2. Get extractive answers from the search response. Extractive answers are returned with each search result in `extractive_answers` . 

In this example of a document that was returned as one of the results in a search response, an extractive answer was included with the result: 

```
{
 "id": "54321",
 "document": {
   "name":
"projects/123/locations/global/collections/default_collection/dataStores/e
xample-datastore/branches/0/documents/54321",
   "id": "54321",
   "derivedStructData": {
     "extractive_answers": [
       {
         "pageNumber": "2",
         "content": "Google saw growth throughout the year both in our
domestic business and internationally, both on Google owned sites and on
the Google Network. Specifically, revenues from Google owned sites
increased 101% on a year over year basis, from $792 million to $1.6
billion."
       }
     ],
     "link": "gs://cloud-samples-data/gen-app-builder/search/alphabet-
investor-pdfs/2004Q4_earnings_google.pdf"
   }
}
}
```

`pageNumber` : If page numbers can be extracted from the document, this field indicates where the answer was extracted from. 

`content` : The content of the extractive answer. 

### Extractive segments

An extractive segment is a section of text that is extracted verbatim from a search result document. Extractive segments are similar to extractive answers (#extractive-answers), but extractive segments usually more complete and verbose. Typically, extractive segments are used as input for your own LLMs to generate answers or new text. 

Extractive segments can be multiple paragraphs, including formatted text such as tables and bulleted lists. 

Extractive segments are available for data stores with unstructured data. 

#### Extractive segment options

The following options are available for extractive segments: 

- **Number of segments** : You can specify up to 10 extractive segments to return for each search result. 

- **Relevance scores** : Relevance scores are based on the similarity of the query to the extracted segment. You can specify that extractive segments be returned with relevance scores. Scores range from -1.0 (less relevant) to 1.0 (more relevant). Turning on relevance scores can increase latency. 

**Note:** The order in which results are returned is based on many factors. Although relevance scores are considered during ranking, they don't solely determine the ranking of results. 

- **Adjacent segments** : You can set `numPreviousSegments` and `numNextSegments` to get up to 3 segments from immediately before and after the relevant segment. Adjacent segments can add context and accuracy to the relevant segment. 

Turning on adjacent segments can increase latency. 

#### Get extractive segments

The following steps show how to get extractive segments for unstructured data. 

1. Send a search request that uses `ContentSearchSpec.extractiveContentSpec` (/gemini/enterprise/docs/reference/rest/v1/ContentSearchSpec#extractivecontentspec) to specify `maxExtractiveSegmentCount` . 

The following example of `extractiveContentSpec` specifies that one segment can be returned for each search result. 

```
"contentSearchSpec":
{
 "extractiveContentSpec": {
   "maxExtractiveSegmentCount": 1
 }
}
```

- `maxExtractiveSegmentCount` : The number of extractive segments to return for each search result. The default value is 0 and the maximum is 10. 

Additional options: 

- `returnExtractiveSegmentScore` : Set to `true` to return a relevance score with each segment returned. 

- `numPreviousSegments` : The number of adjacent segments to return before the relevant segment. The default value is 0 and the maximum is 3. Using adjacent segments can increase latency. 

- `numNextSegments` : The number of adjacent segments to return after the relevant segment. The default value is 0 and the maximum is 3. Using adjacent segments can increase latency. 

For more information about these options, see Extractive segment options 

(#segment-options). 

2. Get segments from the search response. Segments are returned with each search result in `extractive_segments` . 

In this example of a document that was returned as one of the results in a search response, a segment was included with the result: 

```
{
 "id": "54321",
 "document": {
   "name":
"projects/123/locations/global/collections/default_collection/dataStores/e
xample-datastore/branches/0/documents/54321",
   "id": "54321",
   "derivedStructData": {
     "extractive_segments": [
       {
         "pageNumber": "2",
         "content": "Client\nGoogle Toolbar. Google Toolbar is a free
application that adds a Google search box to web browsers
(Internet\nExplorer and Firefox) and improves user web experience through
features such as a pop-up blocker that blocks\npop-up advertising, an
autofill feature that completes web forms with information saved on a
user's computer, and\ncustomizable buttons that let users search their
favorite web sites and stay updated on their favorite feeds.\n\nGoogle
Chrome. Google Chrome is an open-source browser that combines a minimal
design with\ntechnologies to make the web faster, safer, and easier to
navigate.\nGoogle Pack. Google Pack is a free collection of safe, useful
software programs from Google and other\ncompanies that improve the user
experience online and on the desktop. It includes programs that help
users\nbrowse the web faster, remove spyware and viruses.\n\nPicasa.
Picasa is a free service that allows users to view, manage and share their
photos. Picasa enables users\nto import, organize and edit their photos,
and upload them to Picasa Web Albums where the photos can be shared\nwith
others on the internet.\n\nGoogle Desktop. Google Desktop lets people
perform a full-text search on the contents of their own\ncomputer,
including email, files, instant messenger chats and web browser history.
Users can view web pages they\nhave visited even when they are not online.
Google Desktop also includes a customizable Sidebar that includes\nmodules
for weather, stock tickers and news.\n\n5"
       }
     ],
     "link": "gs://cloud-samples-data/gen-app-builder/search/alphabet-
investor-pdfs/2004Q4_earnings_google.pdf"
   }
}
}
```

`pageNumber` : If page numbers can be extracted from the document, this field indicates where the answer was extracted from. 

`content` : The content of the extractive segment. 

### What's next

Preview search results (/gemini/enterprise/docs/preview-search-results) 

Last updated 2026-10-14 UTC.
