# Gemini Enterprise: user guide, Workflow Builder, developer guide / Stream answers (Legacy) to Filter and sort search results in the app (Legacy)
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 447-486, extracted 2026-10-18

Contains:
- Stream answers (Legacy) (pages 447-461) https://docs.cloud.google.com/gemini/enterprise/docs/stream-answer
- Answer generation model versions and lifecycle for the Answer API (Legacy) (pages 462-463) https://docs.cloud.google.com/gemini/enterprise/docs/answer-generation-models
- Get search summaries (Legacy) (pages 464-485) https://docs.cloud.google.com/gemini/enterprise/docs/get-search-summaries
- Filter and sort search results in the app (Legacy) (pages 486-486) https://docs.cloud.google.com/gemini/enterprise/docs/filter-app

## Stream answers (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/stream-answer

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

This page introduces the streaming answer method. 

The streaming answer method has many of the same features as the answer (/gemini/enterprise/docs/answer) method plus one additional feature: _streaming_ . When you stream an answer, the generated answer is broken into multiple parts that are sent in sequence. 

Streaming answers is particularly useful if the generated answers are long, so that sending the entire answer at once causes a delay. Streaming answers reduces the appearance of latency. 

### Limitations

The streaming answer method has the same features as the answer method with the following exceptions: 

- Streaming answer is supported only for English. 

- The number of rephrase steps is one. You can't disable rephrasing, nor can you change the maximum number of steps. 

- You can't get grounding scores for streaming answers, nor can you choose to return only well-grounded answers. 

- Only Gemini models can be used with the streaming answer method. For a list of models, see Available models (/gemini/enterprise/docs/answer-generation-models#models). 

### Stream an answer

The following command shows how to call the streaming answer (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConfig s/streamAnswer) 

method and return a generated answer in the form of a series of JSON responses. Typically, each response contains one sentence of the answer. 

This basic command shows the required input only. The options are left at their defaults. 

For examples of other options, see Get answers and follow-ups 

(/gemini/enterprise/docs/answer). Some answer options aren't available for answer streaming; see the limitations (#limitations) on this page. 

REST 

(#rest) 

To search and get results with a streamed generated answer, do the following: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:streamAnswer" \
 -d '{
       "query": { "text": "QUERY"}
     }'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : a free-text string that contains the question or search query. For example, "Which database is faster, bigquery or spanner?". 

<sup>Example command and partial result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
 "https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:streamAnswer" \
 -d '{
       "query":{"text":"Which database is faster, bigquery or
spanner?"}
     }'
[{
 "answer": {
 "state": "STREAMING",
   "steps": [
     {
       "description": "Rephrase the query and search.",
       "actions": [
         {
           "searchAction": {
             "query": " What is the performance of Spanner?"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
                 "uri":
"https://cloud.google.com/example/docs/answer",
                 "title": "Get answers and follow-ups | Example |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "QUERY : a free-text string that
contains the question or search query. For example, "Compare the
BigQuery and \u003cb\u003eSpanner\u003c/b\u003e databases?". Example
command and result.",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
...
              {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/b95bb201a0adb24f769627f56cf34405",
                 "uri":
"https://abc.xyz/assets/investor/static/pdf/2017_Q1_Earnings_Transcri
pt.pdf",
                 "title": "\u200b \u200b",
                 "snippetInfo": [
                   {
                     "snippet": "well as Hardware related costs,
reflecting the continued strong
\u003cb\u003eperformance\u003c/b\u003e of our new Made by ... We
introduced dozens of new products, including
\u003cb\u003eSpanner\u003c/b\u003e, a ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               }
             ]
           }
         },
         {
           "searchAction": {
             "query": " What is the performance of BigQuery?"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/18bcc727bfd6a3d1be0aa4bd49fe2c50",
                 "uri":
"https://cloud.google.com/example/docs/evaluate-search-quality",
                 "title": "Evaluate search quality | Example |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "You can evaluate the
\u003cb\u003eperformance\u003c/b\u003e of generic search apps that
contain structured, unstructured, and website data. ... Import from
\u003cb\u003eBigQuery\u003c/b\u003e: import
\u003cb\u003eBigQuery\u003c/b\u003e data ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
...
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
                 "uri":
"https://cloud.google.com/example/docs/answer",
                 "title": "Get answers and follow-ups | Example |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "QUERY : a free-text string that
contains the question or search query. For example, "Compare the
\u003cb\u003eBigQuery\u003c/b\u003e and Spanner databases?". Example
command and result.",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               }
             ]
           }
         }
       ]
     }
   ]
 }
}
,
{
 "answer": {
   "state": "STREAMING",
   "references": [
     {
       "chunkInfo": {
         "content": "Example command and partial result curl -X POST
-H \"Authorization: Bearer $(gcloud auth print-access-token)\" -H
\"Content-Type: application/json\"
\"https://discoveryengine.googleapis.com/v1/projects/123456/locations
/global/collections/default_collection/dataStores/my-data-
store/servingConfigs/default_search:answer\" -d '{ \"query\": {
\"text\": \"Compare bigquery with spanner database?\"}
\"queryUnderstandingSpec\": { \"queryRephraserSpec\": { \"disable\":
true } } }' { \"answer\": { \"state\": \"SUCCEEDED\", \"answerText\":
\"You can compare BigQuery and Spanner databases using the following
criteria:\\n\\n* **Pricing:** BigQuery is priced per GB of data
processed, while Spanner is priced per hour of compute time.\\n*
**Performance:** BigQuery is designed for fast analytics, while
Spanner is designed for high availability and scalability.\\n*
**Features:** BigQuery supports a wide range of features, including
SQL, machine learning, and streaming. ",
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
           "uri": "https://cloud.google.com/example/docs/answer",
           "title": "Get answers and follow-ups | Example | Google
Cloud"
         }
       }
     },
     ...
     {
       "chunkInfo": {
         "content": "Here is an example of a summary, with citations
and citation metadata, returned at the end of a search response: See
more code actions. Dismiss View Light code theme Dark code theme
\"summary\": { \"summaryText\": \"BigQuery is Google Cloud's fully
managed and completely serverless enterprise data warehouse [1].
BigQuery supports all data types, works across clouds, and has built-
in machine learning and business intelligence, all within a unified
platform [2, 3].\", \"summaryWithMetadata\": { \"summary\":
\"BigQuery is Google Cloud's fully managed and completely serverless
enterprise data warehouse. ",
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f7ba2e8666f5514b5bc14f5e300d7678",
           "uri": "https://cloud.google.com/example/docs/get-search-
summaries",
           "title": "Get search summaries | Example | Google Cloud"
         }
       }
     }
   ]
 }
}
,
{
 "answer": {
 "state": "STREAMING",
   "answerText": "Span"
 }
}
,
{
 "answer": {
 "state": "STREAMING",
   "answerText": "ner is Google's large-scale database that scales
20 times better than"
 }
}
,
...
{
 "answer": {
 "state": "STREAMING",
   "answerText": " Web Services, and on-premises data sources. "
 }
}
,
{
 "answer": {
 "state": "STREAMING",
   "answerText": "Spanner is a distributed, strongly consistent, SQL
database designed to scale to 10 million servers. \n"
 }
}
,
{
 "answer": {
 "state": "SUCCEEDED",
   "answerText": "Spanner is Google's large-scale database that
scales 20 times better than any competitor. Spanner is designed for
high availability and scalability, while BigQuery is designed for
fast analytics. BigQuery is a serverless, highly scalable, and cost-
effective cloud data warehouse that enables businesses to analyze all
their data very quickly. BigQuery is a very powerful tool that can be
used to analyze data from many different sources, including Google
Cloud Platform, Amazon Web Services, and on-premises data sources.
Spanner is a distributed, strongly consistent, SQL database designed
to scale to 10 million servers. \n",
   "references": [
     {
       "chunkInfo": {
         "content": "Example command and partial result curl -X POST
-H \"Authorization: Bearer $(gcloud auth print-access-token)\" -H
\"Content-Type: application/json\"
\"https://discoveryengine.googleapis.com/v1/projects/123456/locations
/global/collections/default_collection/dataStores/my-data-
store/servingConfigs/default_search:answer\" -d '{ \"query\": {
\"text\": \"Compare bigquery with spanner database?\"}
\"queryUnderstandingSpec\": { \"queryRephraserSpec\": { \"disable\":
true } } }' { \"answer\": { \"state\": \"SUCCEEDED\", \"answerText\":
\"You can compare BigQuery and Spanner databases using the following
criteria:\\n\\n* **Pricing:** BigQuery is priced per GB of data
processed, while Spanner is priced per hour of compute time.\\n*
**Performance:** BigQuery is designed for fast analytics, while
Spanner is designed for high availability and scalability.\\n*
**Features:** BigQuery supports a wide range of features, including
SQL, machine learning, and streaming. ",
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
           "uri": "https://cloud.google.com/example/docs/answer",
           "title": "Get answers and follow-ups | Example | Google
Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "Second, we also give them the ability to build
applications using a set of technology that can run on any
environment that they have. When we say on any environment - at their
premise, on our cloud or on any other cloud. So, in other words, they
can learn once, write once, deploy anywhere; and we make money no
matter where they deploy. An example of that is a recent product we
introduced called AlloyDB. It's the fastest-performing relational
database in the market. We run it in all four environments: Our
cloud, on-premise and on other clouds. And it's the only relational
database that can run in any of those configurations. You see that in
our adoption, both at the top end of the market where a system - for
example, like Spanner, which is our large-scale database - scales 20
times better than the largest scalable system of any competitor. So
for high-end, we work extremely well. And, also, because we made it
so easy to use, startups and small businesses are growing very
quickly in their adoption of our platform. When we introduced our AI
systems, we introduced a platform called Vertex AI. ",
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/8ad08d0844d601733e135381512e2a16",
           "uri": "http://abc.xyz/thomas-kurian-ceo-google-cloud-at-
the-goldman-sachs-2023-communacopia-technology-conference-on-
september-7th-2023",
           "title": "Thomas Kurian, CEO, Google Cloud at the Goldman
Sachs 2023 Communacopia + Technology Conference on September 7th,
2023 - Alphabet Investor Relations"
         }
       }
     },
     ...
     {
       "chunkInfo": {
         "content": "BigQuery is also integrated with other Google
Cloud services, such as Google Kubernetes Engine, Cloud Data Fusion,
and Cloud Dataproc, making it easy to build and deploy data
pipelines. Here are some of the benefits of using BigQuery: * **Fast
and scalable:** BigQuery can process petabytes of data very quickly,
and it can scale to handle even the most demanding workloads. *
**Cost-effective:** BigQuery is a very cost-effective way to store
and analyze data. You only pay for the data that you use, and there
are no upfront costs or commitments. * **Secure:** BigQuery is a
secure platform that meets the needs of even the most security-
conscious organizations. * **Easy to use:** BigQuery is easy to use,
even for non-technical users. It has a simple and intuitive user
interface, and it supports a variety of data sources. * **Integrated
with other Google Cloud services:** BigQuery is integrated with other
Google Cloud services, making it easy to build and deploy data
pipelines. If you are looking for a fast, scalable, and cost-
effective way to analyze your data, then BigQuery is a great option.
",
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f7ba2e8666f5514b5bc14f5e300d7678",
           "uri": "https://cloud.google.com/example/docs/get-search-
summaries",
           "title": "Get search summaries | Example | Google Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "Here is an example of a summary, with citations
and citation metadata, returned at the end of a search response: See
more code actions. Dismiss View Light code theme Dark code theme
\"summary\": { \"summaryText\": \"BigQuery is Google Cloud's fully
managed and completely serverless enterprise data warehouse [1].
BigQuery supports all data types, works across clouds, and has built-
in machine learning and business intelligence, all within a unified
platform [2, 3].\", \"summaryWithMetadata\": { \"summary\":
\"BigQuery is Google Cloud's fully managed and completely serverless
enterprise data warehouse. ",
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f7ba2e8666f5514b5bc14f5e300d7678",
           "uri": "https://cloud.google.com/example/docs/get-search-
summaries",
           "title": "Get search summaries | Example | Google Cloud"
         }
       }
     }
   ],
   "steps": [
     {
       "description": "Rephrase the query and search.",
       "actions": [
         {
           "searchAction": {
             "query": " What is the performance of Spanner?"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
                 "uri":
"https://cloud.google.com/example/docs/answer",
                 "title": "Get answers and follow-ups | Example |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "QUERY : a free-text string that
contains the question or search query. For example, "Compare the
BigQuery and \u003cb\u003eSpanner\u003c/b\u003e databases?". Example
command and result.",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/9d022f7bdf24bac6714a9cf61a5458c7",
                 "uri":
"https://abc.xyz/assets/87/4c/162ca71d4178a3f4d39002467439/thomas-
kurian-goldman-sachs-090723.pdf",
                 "title": "Thomas Kurian Goldman Sachs 090723",
                 "snippetInfo": [
                   {
                     "snippet": "2X better training
\u003cb\u003eperformance\u003c/b\u003e per dollar1 compared to a
leading cloud alternative. More than 70% of gen AI unicorns are
Google Cloud customers. Best ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
...
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/20641e370fa86c78f1c81f3dab22efe1",
                 "uri":
"https://cloud.google.com/example/docs/release-notes",
                 "title": "Example release notes | Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "Generative answers have been
updated with \u003cb\u003eperformance\u003c/b\u003e improvements. ...
This lets you assess your search engine's
\u003cb\u003eperformance\u003c/b\u003e ... Importing data from
\u003cb\u003eSpanner\u003c/b\u003e, Cloud ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/b95bb201a0adb24f769627f56cf34405",
                 "uri":
"https://abc.xyz/assets/investor/static/pdf/2017_Q1_Earnings_Transcri
pt.pdf",
                 "title": "\u200b \u200b",
                 "snippetInfo": [
                   {
                     "snippet": "well as Hardware related costs,
reflecting the continued strong
\u003cb\u003eperformance\u003c/b\u003e of our new Made by ... We
introduced dozens of new products, including
\u003cb\u003eSpanner\u003c/b\u003e, a ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               }
             ]
           }
         },
         {
           "searchAction": {
             "query": " What is the performance of BigQuery?"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/18bcc727bfd6a3d1be0aa4bd49fe2c50",
                 "uri":
"https://cloud.google.com/example/docs/evaluate-search-quality",
                 "title": "Evaluate search quality | Example |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "You can evaluate the
\u003cb\u003eperformance\u003c/b\u003e of generic search apps that
contain structured, unstructured, and website data. ... Import from
\u003cb\u003eBigQuery\u003c/b\u003e: import
\u003cb\u003eBigQuery\u003c/b\u003e data ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/2a3221d40533a4bdaf35778962a2a079",
                 "uri":
"https://cloud.google.com/example/docs/check-media-data-quality",
                 "title": "Check data quality for media
recommendations | Example | Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "... model that will result in
\u003cb\u003eperformance\u003c/b\u003e issue if not met for all media
recommendations models and all business objectives.", "condition": {
"expression ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
...
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/18c258b9c770f4d762e6233d1a1bc81c",
                 "uri": "https://cloud.google.com/example/docs/user-
events",
                 "title": "About user events | Example | Google
Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "This section provides the data
formats for each event type supported by media recommendations.
Examples for JavaScript Pixel are provided. For
\u003cb\u003eBigQuery\u003c/b\u003e, the ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/1a9f55e00c42c06ca97bf5a5868dbcdc",
                 "uri":
"https://cloud.google.com/example/docs/answer",
                 "title": "Get answers and follow-ups | Example |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "QUERY : a free-text string that
contains the question or search query. For example, "Compare the
\u003cb\u003eBigQuery\u003c/b\u003e and Spanner databases?". Example
command and result.",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               }
             ]
           }
         }
       ]
     }
   ]
 }
}
```

In this example, the answer to the query "Which database is faster, bigquery or spanner?" appears in a series of JSON outputs. The final output is given the state `SUCCEEDED` and includes the complete answer. 

### Other examples

The basic command shown in Stream an answer (#search-answer-basic) is the simplest command with no options specified. However, you can apply the same options available with the answer (/gemini/enterprise/docs/answer) method, with the exception of the limitations (#limitations) listed on this page. 

Streaming answers can also used with follow-up sessions 

(/gemini/enterprise/docs/answer#commands_for_follow-up_questions). 

Last updated 2026-10-14 UTC. 



## Answer generation model versions and lifecycle for the Answer API (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/answer-generation-models

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

Gemini Enterprise offers multiple model versions for you to choose when generating answers. You can choose the model versions when using search summaries (/gemini/enterprise/docs/get-search-summaries) and answers and follow-ups (/gemini/enterprise/docs/answer). 

### Available models

Gemini Enterprise uses two types of models for question and answering use cases: 

- Gemini Enterprise Agent Platform LLM models that have been tested on question and answering tasks 

- Gemini Enterprise models that are based on Agent Platform LLM models and further trained to address question and answering tasks 

Gemini Enterprise models share the same discontinuation date as their base Agent Platform LLM models. The base LLM model is available for six months after the release date of the next version of the model, according to the Model versions and lifecycle (/gemini-enterprise-agent-platform/models/model-versions). Leave enough time to migrate to new models before the discontinuation dates. 

The following table lists model version specifications. When you set a model specification, the API uses the specified model to generate answers. 

|Model version<sup>1</sup>|Description|Context<br>window<sup>2</sup>|Discontinuation<br>date|
|---|---|---|---|
|`stable`|The default model choice if the model version<br>not set.|is<br>128K|N/A|
||The`stable`model specification points to<br>`gemini-3.5-flash/answer_gen/v1`.<br>The model designated as`stable`changes<br>periodically as new models and versions<br>become available.|||
|`gemini-3.1-pro-`<br>`preview/answer_`<br>`gen/v1`|The<br>`gemini-3.1-pro-preview`<br>(/gemini-enterprise-agent-<br>platform/models/gemini/3-1-pro)<br>model.|128K|N/A|
|`gemini-3-flash-`<br>`preview/answer_`<br>`gen/v1`|The<br>`gemini-3-flash-preview`<br>(/gemini-enterprise-agent-<br>platform/models/gemini/3-flash)<br>model.|128K|N/A|
|`gemini-3.5-`<br>`flash/answer_`<br>`gen/v1`|The<br>`gemini-3.5-flash`<br>(/gemini-enterprise-agent-<br>platform/models/gemini/3-5-flash)<br>model.|128K|N/A|

- 1 The latest Gemini models might not be available for use with this API. 

- 2 For quality and latency reasons, this context window is smaller than allowed elsewhere for these models. 

Last updated 2026-10-16 UTC. 



## Get search summaries (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/get-search-summaries

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

This page shows how to use the API to get search summaries with your search results. It also explains the options that are available with search summaries. For unstructured and website data only. 

**Note:** _Search summaries_ are also called _answers_ . 

### Get a search summary

A search summary is a short summarization of the top one or more search results returned in a search response. The summary itself is taken from the extractive answers returned in the response. Therefore, to get a summary, you must also get extractive answers with your search results. For more information, see Get extractive answers (Preview) (/gemini/enterprise/docs/snippets#extractive-answers). 

The following image shows the summary when PDFs in a data store are queried with the `summaryResultCount` set to `5` . The summary content can vary depending on the app configurations. 

Search summaries can include Markdown-formatted text and simple HTML tags commonly understood by Markdown parsers. For this reason, consider using a Markdown parser in your application to render Markdown text. 

**Note:** By default, search summaries returned by the API don't include citations. To get citations with your summary, see Get citations (#get-citations). 

To get a search summary, follow these steps: 

1. Submit a search request that includes `contentSearchSpec.summarySpec` (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.s ervingConfigs#ServingConfig.SummarySpec) and specifies values for `summaryResultCount` and `maxExtractiveAnswerCount` . For more information about submitting a search request, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

In the following example, `summarySpec` indicates that you want a search summary and that the summary should be generated from the top three search results. 

```
"contentSearchSpec":
{
  "summarySpec":
  {
    "summaryResultCount": 3
  },
  "extractiveContentSpec": { "maxExtractiveAnswerCount" : 1}
}
```

   - `summaryResultCount` : The number of top results to generate the search summary from. If the number of results returned is less than `summaryResultCount` , the summary is generated from all of the results. 

   - `maxExtractiveAnswerCount` : The number of extractive answers to return for each search result. The default value is 0 and the maximum is 1. 

2. Get the summary from the search response. One `summary` property is returned in each response. 

Here is an example of a summary returned at the end of a search response: 

```
"summary":
{
 "summaryText": "BigQuery is Google Cloud's fully managed and completely
 serverless enterprise data warehouse. BigQuery supports all data types,
 works across clouds, and has built-in machine learning and business
 intelligence, all within a unified platform."
```

### Generate summaries from semantic chunks

You can turn on `use_semantic_chunks` to generate summaries from the most relevant document chunks. Using semantic chunks for summary generation increases recall and retrieval compared the default behavior of using extractive answers. 

When semantic chunking is turned on for summaries, the response returns the summary and the content of each chunk that the summary used. 

To use semantic chunks for summary generation, follow these steps: 

1. Submit a search request that includes `contentSearchSpec.summarySpec` (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.s ervingConfigs#ServingConfig.SummarySpec) 

and specifies `"use_semantic_chunks": true` . For more information about submitting a search request, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

The following example of `summarySpec` indicates that you want a search summary that uses semantic chunks, how many results to include, and whether to include citations. 

```
"contentSearchSpec":
{
  "summarySpec":
  {
    "useSemanticChunks": SEMANTIC_CHUNK_BOOLEAN,
    "summaryResultCount": SUMMARY_RESULT_COUNT,
    "includeCitations": CITATIONS_BOOLEAN,
  }
}
```

_`SEMANTIC_CHUNK_BOOLEAN`_ : A boolean that specifies whether to use semantic chunks to generate the search summary. If set to `true` , 

semantic chunks are used. 

   - _`SUMMARY_RESULT_COUNT`_ : The number of top results to generate the search summary from. The maximum value is `10` . 

   - _`CITATIONS_BOOLEAN`_ : A boolean that specifies whether citations are returned. If you turned on chunk mode when you created your data store, then citations refer to chunks. Otherwise, citations refer to source documents. For more about chunk mode, see Parse and chunk documents (/gemini/enterprise/docs/parse-chunk-documents). 

2. Get the summary from the search response. 

Here is an example of a search response that includes a summary that is generated from chunks and includes citations. The `references` part of the response contains the content of the chunks that the summary is generated from. 

<sup>Response</sup> 

```
{
 "results": [
   {
     "id": "123xyz",
     "document": {
       "name":
"projects/exampleproject/locations/global/collections/default_collection/d
ataStores/exampledatastore/branches/0/documents/123xyz",
       "id": "123xyz",
       "derivedStructData": {
         "link": "gs://examplebucket/alphabet-investor-
pdfs/2004_google_annual_report.pdf"
       }
     }
   }
 ],
 "totalSize": 8375,
 "attributionToken": "abcdefg",
 "nextPageToken": "hijklmnop",
 "guidedSearchResult": {},
 "summary": {
   "summaryText": "Google's search technology uses a combination of
techniques to determine the importance of a web page independent of a
particular search query and to determine the relevance of that page to a
particular search query. [1]",
   "summaryWithMetadata": {
     "summary": "Google's search technology uses a combination of
techniques to determine the importance of a web page independent of a
particular search query and to determine the relevance of that page to a
particular search query.",
     "citationMetadata": {
       "citations": [
         {
           "endIndex": "216",
           "sources": [
             {}
           ]
         }
       ]
     },
     "references": [
       {
         "document":
"projects/exampleproject/locations/global/collections/default_collection/d
ataStores/exampledatastore/branches/0/documents/123xyz",
         "chunkContents": [
           {
             "content": "Groups contains more than 1 billion messages
from Usenet Internet discussion groups dating back to
1981.The\ndiscussions in these groups cover a broad range of discourse and
provide a comprehensive look at evolving\nviewpoints, debate and advice on
many subjects.The new Google Groups adds in the ability to create your
own\ngroups for you and your friends and an improved user interface.Google
Mobile.Google Mobile offers people the ability to search and view both the
"mobile web,"\nconsisting of pages created specifically for wireless
devices, and the entire Google index of more than 8 billion\nweb
pages.Google Mobile works on devices that support WAP, WAP 2.0, i-mode or
j-sky mobile Internet\nprotocols.In addition, users can access a variety
of information using Google SMS by typing a query to the\nGoogle
shortcode.Google Mobile is available through many wireless and mobile
phone services worldwide.",
             "pageIdentifier": "17"
           },
           {
             "content": "Google Labs is our playground for our engineers
and for adventurous Google users.On Google\nLabs, we post product
prototypes and solicit feedback on how the technology could be used or
improved.Current Google Labs examples include:Google Personalized Search—
provides customized search results based on an individual user's
interests.Froogle Wireless—gives people the ability to search for product
information from their mobile phones\nand other wireless devices.Google
Maps—enables users to see maps, get directions, and find local businesses
and services quickly\nand easily.Google Maps has several unique features,
including draggable maps, integrated local search\nfrom Google Local, and
keyboard shortcuts.Google Scholar—enables users to search specifically for
scholarly literature, including peer-reviewed\npapers, theses, books,
preprints, abstracts and technical reports from all broad areas of
research.Google\nScholar can be used to find articles from a wide variety
of academic publishers, professional societies,\npreprint repositories and
universities, as well as scholarly articles available across the
web.Google Suggest—guesses what you're typing and offers suggestions in
real time.This is similar to\nGoogle's "Did you mean?"feature that offers
alternative spellings for your query after you search, except\nthat it
works in real time.",
             "pageIdentifier": "17"
           },
           {
             "content": "Groups contains more than 1 billion messages
from Usenet Internet discussion groups dating back to
1981.The\ndiscussions in these groups cover a broad range of discourse and
provide a comprehensive look at evolving\nviewpoints, debate and advice on
many subjects.The new Google Groups adds in the ability to create your
own\ngroups for you and your friends and an improved user interface.Google
Mobile.Google Mobile offers people the ability to search and view both the
"mobile web,"\nconsisting of pages created specifically for wireless
devices, and the entire Google index of more than 8 billion\nweb
pages.Google Mobile works on devices that support WAP, WAP 2.0, i-mode or
j-sky mobile Internet\nprotocols.In addition, users can access a variety
of information using Google SMS by typing a query to the\nGoogle
shortcode.Google Mobile is available through many wireless and mobile
phone services worldwide.\n\nGoogle Local.Google Local enables users to
find relevant local businesses near a city, postal code, or
specific\naddress.This service combines Yellow Page listings with
information found on web pages, and plots their\nlocations on interactive
maps.Google Print.Google Print brings information online that had
previously not been available to web\nsearchers.Under this program, we
enable a number of publishers to host their content and show
their\npublications at the top of our search results.",
             "pageIdentifier": "17"
           },
           {
             "content": "Votes cast by important web pages with high
PageRank weigh more heavily and are\nmore influential in deciding the
PageRank of pages on the web.Text-Matching Techniques.Our technology
employs text-matching techniques that compare search queries\nwith the
content of web pages to help determine relevance.Our text-based scoring
techniques do far more than\ncount the number of times a search term
appears on a web page.For example, our technology determines
the\nproximity of individual search terms to each other on a given web
page, and prioritizes results that have the\nsearch terms near each
other.Many other aspects of a page's content are factored into the
equation, as is the\ncontent of pages that link to the page in question.By
combining query independent measures such as PageRank\nwith our text-
matching techniques, we are able to deliver search results that are
relevant to what people are\ntrying to find.\n\nAdvertising
Technology\nOur advertising program serves millions of relevant, targeted
ads each day based on search terms people\n\nenter or content they view on
the web.The key elements of our advertising technology include:\n\nGoogle
AdWords Auction System.We use the Google AdWords auction system to enable
advertisers to\nautomatically deliver relevant, targeted advertising.",
             "pageIdentifier": "21"
           },
           {
             "content": "Votes cast by important web pages with high
PageRank weigh more heavily and are\nmore influential in deciding the
PageRank of pages on the web.Text-Matching Techniques.Our technology
employs text-matching techniques that compare search queries\nwith the
content of web pages to help determine relevance.Our text-based scoring
techniques do far more than\ncount the number of times a search term
appears on a web page.For example, our technology determines
the\nproximity of individual search terms to each other on a given web
page, and prioritizes results that have the\nsearch terms near each
other.Many other aspects of a page's content are factored into the
equation, as is the\ncontent of pages that link to the page in question.By
combining query independent measures such as PageRank\nwith our text-
matching techniques, we are able to deliver search results that are
relevant to what people are\ntrying to find.\n\nAdvertising
Technology\nOur advertising program serves millions of relevant, targeted
ads each day based on search terms people\n\nenter or content they view on
the web.The key elements of our advertising technology include:",
             "pageIdentifier": "21"
           },
           {
             "content": "Google Maps—enables users to see maps, get
directions, and find local businesses and services quickly\nand
easily.Google Maps has several unique features, including draggable maps,
integrated local search\nfrom Google Local, and keyboard shortcuts.Google
Scholar—enables users to search specifically for scholarly literature,
including peer-reviewed\npapers, theses, books, preprints, abstracts and
technical reports from all broad areas of research.Google\nScholar can be
used to find articles from a wide variety of academic publishers,
professional societies,\npreprint repositories and universities, as well
as scholarly articles available across the web.Google Suggest—guesses what
you're typing and offers suggestions in real time.This is similar
to\nGoogle's "Did you mean?"feature that offers alternative spellings for
your query after you search, except\nthat it works in real time.Google
Video—includes thousands of programs that play on our TVs every day.Google
Video enables\nyou to search a growing archive of televised content—
everything from sports to dinosaur\ndocumentaries to news shows.\n\n6",
             "pageIdentifier": "17"
           },
           {
             "content": "Every search query we process involves the
automated\nexecution of an auction, resulting in our advertising system
often processing hundreds of millions of auctions per\nday.To determine
whether an ad is relevant to a particular query, this system weighs an
advertiser's willingness\nto pay for prominence in the ad listings (the
CPC) and interest from users in the ad as measured by the click\nthrough
rate and other factors.If an ad does not attract user clicks, it moves to
a less prominent position on the\npage, even if the advertiser offers to
pay a high amount.This prevents advertisers with irrelevant ads
from\n"squatting" in top positions to gain exposure.Conversely, more
relevant, well-targeted ads that are clicked on\nfrequently move up in
ranking, with no need for advertisers to increase their bids.Because we
are paid only\nwhen users click on ads, the AdWords ranking system aligns
our interests equally with those of our advertisers\nand our users.The
more relevant and useful the ad, the better for our users, for our
advertisers and for us.\n\nThe AdWords auction system also incorporates
our AdWords discounter, which automatically lowers the\namount advertisers
actually pay to the minimum needed to maintain their ad position.",
             "pageIdentifier": "21"
           },
           {
             "content": "Web Search Technology\nOur web search technology
uses a combination of techniques to determine the importance of a web
page\nindependent of a particular search query and to determine the
relevance of that page to a particular search\nquery.We do not explain how
we do ranking in great detail because some people try to manipulate our
search\nresults for their own gain, rather than in an attempt to provide
high-quality information to users.\n\nRanking Technology.One element of
our technology for ranking web pages is called PageRank.While
we\ndeveloped much of our ranking technology after Google was formed,
PageRank was developed at Stanford\nUniversity with the involvement of our
founders, and was therefore published as research.Most of our
current\nranking technology is protected as trade-secret.PageRank is a
query-independent technique for determining the\nimportance of web pages
by looking at the link structure of the web.PageRank treats a link from
web page A to\nweb page B as a "vote" by page A in favor of page B.The
PageRank of a page is the sum of the PageRank of the\npages that link to
it.The PageRank of a web page also depends on the importance (or PageRank)
of the other\nweb pages casting the votes.",
             "pageIdentifier": "21"
           },
           {
             "content": "The Company recognizes as revenue the fees
charged advertisers each time a user clicks on one of the text\nbased ads
that are displayed next to the search results on Google web
sites.Effective January 1, 2004, the\nCompany offered a single pricing
structure to all of its advertisers based on the AdWords cost per click
model.\n\nGoogle AdSense is the program through which the Company
distributes its advertisers' text-based ads for\ndisplay on the web sites
of the Google Network members.In accordance with Emerging Issues Task
Force\n("EITF") Issue No. 99 19, Reporting Revenue Gross as a Principal
Versus Net as an Agent, the Company recognizes\nas revenues the fees it
receives from its advertisers.This revenue is reported gross primarily
because the\nCompany is the primary obligor to its advertisers.\n\nThe
Company generates fees from search services through a variety of
contractual arrangements, which\ninclude per-query search fees and search
service hosting fees.Revenues from set up and support fees and
search\nservice hosting fees are recognized on a straight-line basis over
the term of the contract, which is the expected\nperiod during which these
services will be provided.The Company's policy is to recognize revenues
from per\nquery search fees in the period queries are made and results are
delivered.\n\nThe Company provides search services pursuant to certain
AdSense agreements.",
             "pageIdentifier": "85"
           },
           {
             "content": "On Google Print pages, we provide links to book
sellers that may\noffer the full versions of these publications for sale,
and we show content-targeted ads that are served through\nthe Google
AdSense program.Google Desktop Search.Google Desktop Search enables our
users to perform a full text search on the\ncontents of their own
computer, including email, files, instant messenger chats and web browser
history.Users\ncan use this service to view web pages they have visited
even when they are not online.Google Alerts.Google Alerts are email
updates of the latest relevant Google results (web, news, etc.) based\non
the user's choice of query or topic.Typical uses include monitoring a
developing news story, keeping current\non a competitor or industry,
getting the latest on a celebrity or event, or keeping tabs on a favorite
sports team.Google Labs.Google Labs is our playground for our engineers
and for adventurous Google users.On Google\nLabs, we post product
prototypes and solicit feedback on how the technology could be used or
improved.Current Google Labs examples include:Google Personalized Search—
provides customized search results based on an individual user's
interests.Froogle Wireless—gives people the ability to search for product
information from their mobile phones\nand other wireless devices.",
             "pageIdentifier": "17"
           }
         ]
       }
     ]
   }
 }
}
```

### Get citations

Citations, when specified, are numbers that are placed inline in a search summary. These numbers indicate from which search results specific sentences in the summary are taken. 

To get citations, follow these steps: 

1. Submit a search request that includes `contentSearchSpec.summarySpec` (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.s ervingConfigs#ServingConfig.SummarySpec) 

and specifies `"includeCitations": true` . For more information about submitting a search request, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

In the following example, `summarySpec` indicates that you want a search summary, that the summary should be generated from the top three search results, and that citations should be included in the summary. 

   - `"contentSearchSpec": {` 

   - `"summarySpec": { "summaryResultCount": 3,` 

   - `"includeCitations": true },` 

   - `"extractiveContentSpec": { "maxExtractiveAnswerCount" : 1} }` 

      - `summaryResultCount` : The number of top results to generate the search summary from. If the number of results returned is less than `summaryResultCount` , the summary is generated from all of the results. The maximum value is `5` . 

      - `includeCitations` : A boolean that specifies whether citations are returned. 

      - `maxExtractiveAnswerCount` : The number of extractive answers to return for each search result. The default value is 0 and the maximum is 1. 

2. Get the summary, with citations, from the search response. One `summary` property is returned in each response. 

Here is an example of a summary, with citations and citation metadata, returned at the end of a search response: 

- `"summary": {` 

- `"summaryText": "BigQuery is Google Cloud's fully managed and completely serverless enterprise data warehouse [1]. BigQuery supports all data` 

- `types,` 

- `works across clouds, and has built-in machine learning and business intelligence, all within a unified platform [2, 3].", "summaryWithMetadata": {` 

- `"summary": "BigQuery is Google Cloud's fully managed and completely serverless enterprise data warehouse. BigQuery supports all data types, works across clouds, and has built-in machine learning and business intelligence, all within a unified platform.", "citationMetadata": {` 

```
    "citations": [
      {
        "startIndex": "0",
        "endIndex": "101",
        "sources": [
          {
            "uri": "gs://example-dataset/html/6344007140738632642.html",
            "title": "About BigQuery",
            "id": "b6344007140738632642",
            "referenceIndex": "0"
          },
          {
            "uri": "gs://example-dataset/html/1365490014946172719.html",
            "title": "Google Cloud article",
            "id": "b1365490014946172719",
            "referenceIndex": "1"
          },
          {
            "uri": "gs://example-dataset/html/2687910668117268120.html",
            "title": "BigQuery document",
            "id": "a2687910668117268120",
            "referenceIndex": "2"
          }
        ]
      },
      {
        "startIndex": "103",
        "endIndex": "230",
        "sources": [
          {
            "referenceIndex": "0"
           },
          {
            "referenceIndex": "1"
          },
          {
            "referenceIndex": "2",
          }
        ]
      }
    ]
  },
  "references": [
  {
    "title": "Sports in the United States",
    "docName":
"projects/123/locations/global/collections/default_collection/dataStores/d
s-123/branches/0/documents/b6344007140738632642",
    "uri": "https://example.com/bigqueryA"
  },
  {
    "title": "Sports in the United States",
    "docName":
"projects/123/locations/global/collections/default_collection/dataStores/d
s-123/branches/0/documents/b1365490014946172719",
    "uri": "https://example.com/bigqueryB"
  },
  {
    "title": "Sports in the United States",
    "docName":
"projects/123/locations/global/collections/default_collection/dataStores/d
s-123/branches/0/documents/a268791066811726812",
    "uri": "https://example.com/bigqueryC"
  }
]
}
}
```

- `summaryText` : The search summary, with citation numbers. The citation numbers refer to the returned search results and are 1-indexed. For example, `[1]` means that the sentence is attributed to the first search result. `[2, 3]` means that the sentence is attributed to both the second and third search results. 

- `citations` : For each sentence in the summary that has a citation, lists the metadata for that citation. 

- `startIndex` : Indicates the start of the sentence, measured in unicode bytes. 

- `endIndex` : Indicates the end of the sentence, measured in unicode bytes. 

- `sources` : Lists the `referenceIndex` for each source that was included in the sentence's citation. `referenceIndex` is the index number assigned to a source. The first source's `referenceIndex` isn't always explicitly returned in the response. Because `referenceIndex` is 0-indexed, the first source always has a `referenceIndex` of 0. 

- `references` : Lists metadata for each reference that was cited in the summary. Metadata includes `title` , `docName` , and `uri` . 

### Ignore adversarial queries

Adversarial queries include negative comments or are designed to generate unsafe, policy-violating output. You can specify that no search summaries should be returned for adversarial queries. When an adversarial query is ignored, the `summaryText` property contains boilerplate text indicating that no search summary is returned. Search documents are returned for adversarial queries even though search summaries are not. 

To specify that no search summaries should be returned for adversarial queries, follow these steps: 

1. Submit a search request that includes `contentSearchSpec.summarySpec` (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.s ervingConfigs#ServingConfig.SummarySpec) 

and specifies `"ignoreAdversarialQuery": true` . For more information about submitting a search request, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

In the following example, `summarySpec` indicates that you want a search summary, that the summary should be generated from the top three search results, but that no summary should be returned for adversarial queries. 

```
"contentSearchSpec":
{
  "summarySpec":
  {
    "summaryResultCount": 3,
    "ignoreAdversarialQuery": true
  },
  "extractiveContentSpec": { "maxExtractiveAnswerCount" : 1}
}
```

      - `summaryResultCount` : The number of top results to generate the search summary from. If the number of results returned is less than `summaryResultCount` , the summary is generated from all of the results. The maximum value is `5` . 

      - `ignoreAdversarialQuery` : A boolean that specifies that no search summaries should be returned for adversarial queries. 

      - `maxExtractiveAnswerCount` : The number of extractive answers to return for each search result. The default value is 0 and the maximum is 1. 

2. See the `summary` property that is returned for an adversarial search request. 

   - Here is an example: 

```
"summary":
{
```

- `"summaryText": "We do not have a summary for your query. Here are some search results.",` 

- `"summarySkippedReasons": [` 

- `"ADVERSARIAL_QUERY_IGNORED"` 

- `]` 

```
}
```

- `summaryText` : Boilerplate text indicating that no search summary is returned. 

- `summarySkippedReasons` : An enumeration with values for summaryskipped reasons. 

### Ignore non-summary seeking queries

Non-summary seeking queries return results that are not suitable for summarization. For example, "why is the sky blue" and "Who is the best soccer player in the world?" are summary-seeking queries, but "SFO airport" and "world cup 2026" are not. They are most likely navigational queries. You can specify that no search summaries should be returned for non-summary seeking queries. Search 

documents are returned for non-summary seeking queries even though search summaries are not. 

To specify that no search summaries should be returned for non-summary seeking queries, follow these steps: 

1. Submit a search request that includes `contentSearchSpec.summarySpec` 

   - (/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.s ervingConfigs#ServingConfig.SummarySpec) 

and specifies `"ignoreNonSummarySeekingQuery": true` . For more information about submitting a search request, see Preview search results (/gemini/enterprise/docs/preview-search-results). 

In the following example, `summarySpec` indicates that you want a search summary, the summary should be generated from the top three search results, but that no summary should be returned for non-summary seeking queries. 

```
"contentSearchSpec":
{
  "summarySpec":
  {
    "summaryResultCount": 3,
    "ignoreNonSummarySeekingQuery": true
  },
  "extractiveContentSpec": { "maxExtractiveAnswerCount" : 1}
}
```

- `summaryResultCount` : The number of top results to generate the search summary from. If the number of results returned is less than `summaryResultCount` , the summary is generated from all of the results. The maximum value is `5` . 

- `ignoreNonSummarySeekingQuery` : A boolean that specifies that no search summaries should be returned for non-summary seeking queries. 

- `maxExtractiveAnswerCount` : The number of extractive answers to return for each search result. The default value is 0 and the maximum is 1. 

2. See the `summary` property that is returned for a non-summary seeking search request. 

Here is an example: 

```
"summary":
{
 "summaryText": "We do not have a summary for your query. Here are some
 search results.",
 "summarySkippedReasons": [
   "NON_SUMMARY_SEEKING_QUERY_IGNORED"
]
}
```

- `summaryText` : Boilerplate text indicating that no search summary is returned. 

- `summarySkippedReasons` : An enumeration with values for summaryskipped reasons. 

### Get customized summaries

You can get customized summaries by providing natural-language instructions. This feature is available for the search widget by using the console, and for the API by entering instructions in the `modelPromptSpec.preamble` field. 

You can request customizations such as length, level of detail, style of output (such as "simple"), language of output, focus of answer, and format (such as tables, bullets, and XML). 

For example, for the query `What are the benefits of bigquery?` , you could enter customization instructions like in the following examples: 

- Example instruction: `please show the answer format in an ordered list` Example answer: 

```
The benefits of BigQuery are:
```

`1. Increased business productivity` 

`2. IT staff productivity` 

`3. Reduced infrastructure costs` 

`4. Loading and exporting data are free` 

Example instruction: `give a very detailed answer` 

Example answer: 

```
BigQuery is a serverless, highly scalable, and cost-effective cloud data
warehouse that enables businesses to analyze all their data very quickly.
It is a fully managed service that takes care of provisioning, scaling,
and managing the underlying infrastructure, so you can focus on analyzing
your data. BigQuery is also integrated with other Google Cloud services,
such as Google Kubernetes Engine, Cloud Data Fusion, and Cloud Dataproc,
making it easy to build and deploy data pipelines.
Here are some of the benefits of using BigQuery:
* **Fast and scalable:** BigQuery can process petabytes of data very
quickly, and it can scale to handle even the most demanding workloads. *
**Cost-effective:** BigQuery is a very cost-effective way to store and
analyze data. You only pay for the data that you use, and there are no
upfront costs or commitments. * **Secure:** BigQuery is a secure platform
that meets the needs of even the most security-conscious organizations. *
**Easy to use:** BigQuery is easy to use, even for non-technical users. It
has a simple and intuitive user interface, and it supports a variety of
data sources. * **Integrated with other Google Cloud services:** BigQuery
is integrated with other Google Cloud services, making it easy to build
and deploy data pipelines.
If you are looking for a fast, scalable, and cost-effective way to analyze
your data, then BigQuery is a great option.
```

#### Best practices for customized summaries

If you plan to use this feature, do the following: 

- Request only one customization at a time. Don't combine customizations—for example, requesting an HTML table in French. 

- Google recommends that you impose limits on what customizations your end users can request—for example, by offering a selector with a set of predefined customizations. 

#### Customize summaries

You can get customized summaries for only the search widget by using the console or, for any search request, by using the API. 

To get a customized summary, follow these steps: 

ConsoleREST  (#rest) (#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the app that you want to edit. 

3. Go to **Configurations** > **UI** . 

4. Make sure your search widget's **Search type** is set to **Search with an answer** or **Search with follow-ups** . This feature isn't available if **Search** is selected. 

5. Turn on **Enable summary customization** . 

6. To enter summary instructions, do one of the following: 

   - Enter free-form instructions: Enter your own natural language instructions in the **Preamble** field. 

   - Use template instructions: Click **Replace with a template** and select one of the predefined template instructions. The predefined template appears in the **Preamble** field after you select it. 

7. Test the customized summary generation for your app by searching in the **Preview** pane. 

8. To reset to the last saved set of instructions, click **Reset preamble** . 

9. To save your settings to the widget, click **Save and publish** . 

### Specify the summarization model

You can specify the model that you want to use to generate summaries. 

You can specify `stable` , `preview` , or a specific model version by name. For available model versions, see Answer generation model versions and lifecycle 

(/gemini/enterprise/docs/answer-generation-models). 

To change the model version: 

1. Submit a search request that includes 

   - `ContentSearchSpec.SummarySpec.ModelSpec` 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.dataStores.s ervingConfigs#ServingConfig.ModelSpec) 

to specify the model version. 

```
"contentSearchSpec": {
 "summarySpec": {
   "modelSpec": {
     "version": "MODEL_VERSION"
    }
  }
}
```

- _MODEL_VERSION_ : Specifies which model to use to generate summaries. Supported values are: 

   - `stable` : string. Default specification when no value is specified. `stable` points to a GA model version that's fine-tuned for answer generation. Which model `stable` points to changes as new GA model versions are released and previous model versions are discontinued. 

For the up-to-date version that `stable` points to, see Answer generation model versions and lifecycle 

(/gemini/enterprise/docs/answer-generation-models). 

- `preview` : string. `preview` points to the latest Gemini model for question and answering. For more information about Gemini, see Overview of models (/vertex-ai/generative-ai/docs/learn/models). 

- To specify a certain model version instead, enter the version name, such as `gemini-1.5-flash-002/answer_gen/v1` . For supported versions, see Answer generation model versions and lifecycle (/gemini/enterprise/docs/answer-generation-models). 

For example, the following search request specifies `preview` as the model version: 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/exampleproject/locations/gl
obal/collections/default_collection/dataStores/exampledatastore/servingConfigs/
default_search:search" \
-d '{
 "query": "what is bigquery",
 "contentSearchSpec": {
   "summarySpec": {
     "modelSpec": {
       "version": "preview"
     }
   }
 }
}'
```

### Limitations of search summaries

You might encounter the following limitations when using search summaries: 

Because LLMs are used to generate search summaries and citations, the limitations of LLMs also apply to Gemini Enterprise summaries. 

For general information about these LLM limitations, see Model limitations (/vertex-ai/docs/generative-ai/learn/responsible-ai#limitations) in the _Vertex AI_ documentation. 

- Search queries that require complex logical or analytical reasoning or understanding of the world can lead to search summaries that contain incorrect information (hallucinations) or information that is not present in the unstructured or website data. 

- Some statements in the search summary might not contain a citation: 

   - If the system determines a statement doesn't require grounding, it won't include a citation. Sentences like "Here is what I found" or "There are many methods you can follow" lack citations. 

   - Missing citations can also indicate that a valid reference wasn't found. Facts without citations might not be reliable. 

- In rare cases, citations might be incorrectly attributed to a statement. 

- Complex documents might be incorrectly parsed by the LLM. In this case, the summary might be incomplete or incorrect. 

- Because customization instructions are in natural language, adherence to instructions can't be guaranteed for all requests. 

Last updated 2026-10-14 UTC. 



## Filter and sort search results in the app (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/filter-app

**Important:** Gemini Enterprise retrieves search results from the assistant using StreamAssist. We recommend using the StreamAssist instead of the Search and Answer. For more information, see Get search results using StreamAssist (/gemini/enterprise/docs/get-answers-from-streamassist). 

Users can filter results in the app by data source and date range. 

For example, if you have an app that you've connected to a Jira Cloud connector and a Cloud Storage data store, you could use filters in the app to get results only from Jira Cloud and exclude Cloud Storage results. 

To filter and sort, do the following: 

1. In the search app, enter your query in the search bar to search for and retrieve results. 

2. To filter results by data source, select the data sources to filter by. All available data sources are listed as filter buttons after you perform a search. 

   - If more than four data sources are attached to your app, additional sources appear in a drop-down menu. 

3. To filter results by date range, click **Last Updated** and select a date range to filter by. 

Last updated 2026-10-14 UTC.
