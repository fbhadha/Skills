# Gemini Enterprise: user guide, Workflow Builder, developer guide / Get search results (Legacy)
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 324-334, extracted 2026-10-18

## Get search results (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/preview-search-results

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

This page shows how to get search results using the API. 

You can make API calls and integrate those calls into your server or application. This page includes code samples for how to make search queries using the gRPC client libraries with a service account. 

**Note:** Depending on the amount of data, it can take hours after data ingestion to generate a preview. 

### Get search results

You can get search results using the API. 

REST 

(#rest) 

To use the API to get search results for an app with structured or unstructured data, use the `engines.servingConfigs.search` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.serving Configs/search) method: 

**Note:** You can search over an app using the **`engines.servingConfigs.search`** (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servi ngConfigs/search) 

method and you can search over a data store using the **`dataStores.servingConfigs.search`** 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.se rvingConfigs/search) 

method. For the following procedure, Google recommends searching using the **`engines.servingConfigs.search`** method. 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

   - b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. Preview search results. 

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:search" \
-d '{
"query": "QUERY",
"userPseudoId": "USER_PSEUDO_ID",
"pageSize": "PAGE_SIZE",
"offset": "OFFSET",
"orderBy": "ORDER_BY",
"filter": "FILTER",
"boostSpec": "BOOST_SPEC",
"facetSpec": "FACET_SPEC",
"queryExpansionSpec": "QUERY_EXPANSION_SPEC",
"spellCorrectionSpec": "SPELL_CORRECTION_SPEC",
"contentSearchSpec": "CONTENT_SEARCH_SPEC",
"dataStoreSpecs": [{"DATA_STORE_SPEC"}],
}'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : the query text to search. 

- _`USER_PSEUDO_ID`_ : a UTF-8 encoded string, which acts as a unique pseudonymized identifier that tracks the users. It can have a maximum length of 128 characters. Google strongly recommends using this field because it improves model performance and personalization quality. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Some important considerations are as follows: 

   - This identifier doesn't change when the visitor signs in or out of a website. 

   - This field must not be set to the same identifier for multiple users. Otherwise, using the same user ID for multiple users can combine event histories of different users and degrade model quality. 

   - This field must not include personally identifiable information (PII). 

   - For a given search or browse request, this field must map to the corresponding `userPseudoId` field in the user events. 

For more information, see `userPseudoId` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engi nes.servingConfigs/search#body.request_body.FIELDS.user_pseudo_id) . 

- _`PAGE_SIZE`_ : the number of results returned by the search. The maximum allowed page size depends on the data type. Page sizes above the maximum value are coerced to the maximum value. 

- _`OFFSET`_ : optional. The starting index of the results. The default value is 0. 

For example, if the offset is 2, the page size is 10, and there are 15 results to return, results 2 through 11 are returned on the first page. 

- _`ORDER_BY`_ : optional. The order in which the results are arranged. 

- _`FILTER`_ : optional. A text field for filtering your search using a filter expression. The default value is an empty string, which means no filter is applied. 

Example: `color: ANY("red", "blue") AND score: IN(*, 100.0e)` 

For more information, see Filter search for structured or unstructured data (/gemini/enterprise/docs/filter-search-metadata). 

- _`BOOST_SPEC`_ : optional. A specification to boost or bury documents. Values: 

   - `BOOST` : a floating point number in the range [-1,1]. When the value is negative, results are demoted (they appear lower down in the results). When the value is positive, results are promoted (they appear higher up in the results). 

   - `CONDITION` : a text filter expression 

   - (/gemini/enterprise/docs/filter-search-metadata#filter-expressionsyntax) 

to select the documents to which boost is applied. The filter must evaluate to a boolean value. 

To learn about boost for structured search, see Boost search results (/gemini/enterprise/docs/boost-search-results). 

- _`FACET_SPEC`_ : optional. A facet specification to perform faceted search. 

- _`QUERY_EXPANSION_SPEC`_ : optional. A specification to determine under which conditions query expansion should occur. Default is `DISABLED` . 

- _`SPELL_CORRECTION_SPEC`_ : optional. A specification to determine under which conditions spell correction should occur. Default is `AUTO` . 

- _`CONTENT_SEARCH_SPEC`_ : optional. For getting snippets, extractive answers, extractive segments, and search summaries. For 

unstructured data only. For more information, see: 

Use snippets and extractive content 

(/gemini/enterprise/docs/snippets) 

Get search summaries 

(/gemini/enterprise/docs/get-search-summaries) 

_`DATA_STORE_SPEC`_ : filters for a specific data store to search across. This can be used if your search app is connected to multiple data stores. For more information, see DataStoreSpec (/gemini/enterprise/docs/reference/rest/v1/DataStoreSpec). 

Viewing guided search results in the search response: 

Guided search results are returned with search responses for structured and unstructured search. The guided search result contains a list of extracted attribute key-value pairs based on search result documents. This allows users to refine their search results by using some attribute keys and values as filters. 

In this example response, the color green was used to refine search results by issuing a new search request with the filter field specified as `_gs.color: ANY("green")` : 

```
{
"guidedSearchResult": {
 "refinementAttributes": [
   {
     "attributeKey": "_gs.color",
     "attributeValue": "green"
   },
   {
     "attributeKey": "_gs.category",
     "attributeValue": "shoe"
   }
 ]
}
}
```

### Get document-relevance scores with search results

Document-relevance scores are based on the similarity of the query to the document. Scores are put into 11 buckets in the range: 0, 0.1, 0.2, … to 1.0. The higher the score, the more relevant the document. 

Consider document-relevance scores for these use cases: 

- Post-search filtering based on the relevance score to remove irrelevant results Post-search ranking or as input to other applications 

- Debugging: relevance scores can provide insight into why some search results are returned 

For each search result, a relevance score can be returned: 

```
 "results": [
   {
     "id": "DOCUMENT_ID",
     "document": {
     ...
     },
     "modelScores": {
       "relevance_score": {
         "values": [
DOCUMENT-RELEVANCE-SCORE
         ]
       }
     }
   },
   ...
```

Also see the example command in the procedure below. 

**Before you begin:** Make sure that the search app is associated with a structured or unstructured data store. 

REST (#rest) 

To request that document-relevance scores be returned with search results, use the `engines.servingConfigs.search` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.serving Configs/search) 

method as follows: 

**Note:** The scores might not always be returned. Make sure that your post-processing of search results doesn't rely on scores being present. 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

   - b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. Run the following curl command to get scores returned with search results. 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:search" \
-d '{
    "servingConfig":
"projects/PROJECT_ID/locations/global/collections/default_collection/
engines/APP_ID/servingConfigs/default_search",
    "query": "QUERY",
"relevanceScoreSpec": {
      "returnRelevanceScore": true
    }
}'
```

_`PROJECT_ID`_ : the ID of your project. 

_`APP_ID`_ : the ID of the app that you want to query. 

_`QUERY`_ : the query text to search. 

<sup>Example command and partial result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:search" \
-d '{
     "servingConfig": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search",
     "query": "When was Verily founded and what is its mission?",
"relevanceScoreSpec": {
       "returnRelevanceScore": true
     }
}'
{
 "results": [
   {
     "id": "f1b0d98bd2a078a6dfb4f809c3028565",
     "document": {
       "name":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f1b0d98bd2a078a6dfb4f809c3028565",
       "id": "f1b0d98bd2a078a6dfb4f809c3028565",
       "derivedStructData": {
         "link": "gs://cloud-samples-data/gen-app-
builder/search/alphabet-investor-
pdfs/2019_alphabet_annual_report.pdf",
         "extractive_answers": [
           {
             "pageNumber": "70",
             "content": "VERILY Verily is a life science and
healthcare company with a mission to make the world's health data
useful so that people enjoy healthier lives. In December 2018, Verily
received $900 million in cash from a $1.0 billion investment round.
The remaining $100 million was received in the first quarter of
2019."
           }
         ],
         "title": "2019_alphabet_annual_report"
       }
     },
"modelScores": {
       "relevance_score": {
         "values": [
           0.7
         ]
       }
     }
   },
   {
     "id": "0371b29bfa18ac43896b86a7b63d00b0",
     "document": {
       "name":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/0371b29bfa18ac43896b86a7b63d00b0",
       "id": "0371b29bfa18ac43896b86a7b63d00b0",
       "derivedStructData": {
         "link": "gs://cloud-samples-data/gen-app-
builder/search/alphabet-investor-pdfs/20190429_alphabet_10Q.pdf",
         "title": "GOOG 10-Q Q1 2019",
         "extractive_answers": [
           {
             "content": "Verily Verily is a life science company
with a mission to make the world's health data useful so that people
enjoy healthier lives. In December 2018, Verily received $900 million
in cash from a $1.0 billion investment round. The remaining $100
million was received in the first quarter of 2019.",
             "pageNumber": "21"
           }
         ]
       }
     },
"modelScores": {
       "relevance_score": {
         "values": [
           0.5
         ]
       }
     }
   },
   ...
   {
     "id": "e6bbd0d82dc2a2fc7ccf1bd82ac6334f",
     "document": {
       "name":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/e6bbd0d82dc2a2fc7ccf1bd82ac6334f",
       "id": "e6bbd0d82dc2a2fc7ccf1bd82ac6334f",
       "derivedStructData": {
         "title": "2021_Q1_Earnings_Transcript",
         "link": "gs://cloud-samples-data/gen-app-
builder/search/alphabet-investor-
pdfs/2021_Q1_Earnings_Transcript.pdf",
         "extractive_answers": [
           {
             "pageNumber": "2",
             "content": "Our strength in AI and ML is also helping
Financial Services customers improve efficiency of payments, reduce
fraud and risk, and deliver faster payment solutions."
           }
         ]
       }
     },
"modelScores": {
       "relevance_score": {
         "values": [
         ]
       }
     }
   }
 ],
 "totalSize": 76,
 "attributionToken":
"8QHw8AoLCIW4_b0GELHd3lgSJDY3YmU1ZGMwLTAwMDAtMmM1OC04NzcyLTc0NzQ0NjNi
OGMyNSIHR0VORVJJQyqcAcb77TDHy_MX8tntMI6-
nRWK4uQwwvCeFYX77TDvifIwq8SKLauR3zCq-
LMt0IrIMNSynRWc1rctv_7kML7l3zDZveQwkPeyMMP77TD12e0wpd_hMIfi5DCRv9owgv
vtMJWSxTCOkckwu-XfMK7Eii3sifIwqJHfMKjf4TCt-
LMtlL_aMJ_Wty23t4wto4CXIs2KyDDcveQwwv7kMDABShIweDU3MGFkYWI4MzQ4NmY0MG
E",
 "nextPageToken":
"UjMjhjYzYDN0cDN30iM3cDOtgTNjJTLwADMw0iZiRWNlJ2N2QiGBUd0gWLEG4bjhWICM
IBM1IgC",
 "summary": {},
 "queryExpansionInfo": {}
}
```

**Note:** This document-relevance score is different from and more precise than the relevance level (/gemini/enterprise/docs/filter-by-relevance) used to filter documents returned by a search. 

### Search summarization differs by model

If you generate search summaries for your queries, you might notice that the summaries differ between the console results and the API results. If you see this, the likely reason is that the console is using a different LLM model from the API. The curl and code examples on this page use the stable LLM model. 

- To change or view the LLM model used in the **Preview** page of the UI, go to the **Configurations** page > **UI** tab for your app. 

- For method calls, the stable model is the default model. To use an LLM model other than the stable model, see Specify the summarization model 

- (/gemini/enterprise/docs/get-search-summaries#summary-model) and Specify the answer model (/gemini/enterprise/docs/answer#answer-model). 

Last updated 2026-10-14 UTC.
