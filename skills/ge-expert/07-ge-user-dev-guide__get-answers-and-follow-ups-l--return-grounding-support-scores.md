# Gemini Enterprise: user guide, Workflow Builder, developer guide / Get answers and follow-ups (Legacy): Answer phase commands / Return grounding support scores to Answer phase commands / Set the answer language code
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 372-409, extracted 2026-10-18

## Get answers and follow-ups (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/answer

#### Return grounding support scores

The following command shows how to return grounding support scores for answers and claims. 

REST 

(#rest) 

To return a support score for each claim (sentence in the answer) and an aggregated support score for the answer, do the following: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "groundingSpec": {
          "includeGroundingSupports": true,
       }
     }'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

_`APP_ID`_ : the ID of the app that you want to query. 

_`QUERY`_ : a free-text string that contains the question or search query. 

- <sup>Example command and partial result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/
global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer"
-d '{
   "query": { "text": "What is SQL?"},
   "groundingSpec": {
      "includeGroundingSupports": true,
   }
 }'
{
"answer": {
"state": "SUCCEEDED",
"answerText": "SQL stands for Structured Query Language. It is a
database management programming language that is used to access and
manage data in a database. SQL is used to create, update, and delete
data in a database. It can also be used to query data and retrieve
information. SQL is a standard language that is used by many
different database systems.",
"groundingScore" 0.9
"groundingSupports": [
 {
   "endIndex": "41",
   "sources": [
     {
       "referenceId": "1"
     }
   ]
"groundingScore": 0.9
   "groundingCheckRequired": true
 },
 {
   "startIndex": "42",
   "endIndex": "144",
   "sources": [
     {
       "referenceId": "1"
     }
   ]
"groundingScore": 0.8
   "groundingCheckRequired": true
 },
 {
   "startIndex": "267",
   "endIndex": "342",
   "sources": [
     {
       "referenceId": "2"
     }
   ]
"groundingScore": 0.6
   "groundingCheckRequired": true
 }
],
"references": [
 {
   "chunkInfo": {
     "content": "There are a lot of Databases available in the
market such as MS Access, Oracle and many others.For you to write
programs that interact with these databases easily, there has to be a
way where you could get information from all these databases using
the same method.For this purpose SQL was developed.It is a kind of
language (simple when compared to the likes of C or C++) which
enables you to ask all your queries to a database without bothering
about the exact type of database.When you use this Query the database
engine would first find the table called people.Then it would find a
column called firstname.Next it would compare all the values in that
column with 'Reena'.Finally it would return all the details wherever
it finds a match for the firstname.When you write a database program
in VC++ or Java or any other language for that matter, you would make
a database connection to your database and then you would query the
database using SQL queries.When you query the database with any SQL
query the database returns a recordset.A recordset is basically a set
of records (all the entries that your query returns).This recordset
is received in your program and all languages have a data structure
which represents a recordset.",
     "documentMetadata": {
       "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/d993d922043374f5ef7ba297c158b106",
       "uri": "gs://my-bucket-
123/documents/058dee0ec23a3e92f9bfd7cd29840e8f.txt"
       "structData": {
         "fields": [
           {
             "key": "cdoc_url"
             "value": { "stringValue":
"058dee0ec23a3e92f9bfd7cd29840e8f" }
           },
           {
             "key": "doc_id"
             "value": { "stringValue":
"d993d922043374f5ef7ba297c158b106" }
           }
         ]
       }
     }
   }
 },
 {
   "chunkInfo": {
     "content": "The Structured Query Language (SQL) is a database
management programming language.SQL is a tool for accessing
databases, and more specifically, relational databases, and can be
used with different database products.This chapter will prepare you
to learn basic database management using this language.SQLite – To
implement SQL as a library, you need SQLite.SQLite is intended to
provide users and programs a way to store data using a SQL interface
within the program.SQLite3 can be used to manipulate SQLite databases
for major Linux distros.SQL is used to access relational
databases.Each database contains more or less tables which in turn
contain more or less rows and columns.Hereby a single row is seen as
a separate object with features represented by the tables' columns.To
access a table's data you first have to connect to its database.With
the same table, the query SELECT * FROM T WHERE C1 = 1 will result in
all the elements of all the rows where the value of column C1 is '1'
being shown.A WHERE clause specifies that a SQL statement should only
affect rows that meet specified criteria.The criteria are expressed
in the form of predicates.WHERE clauses are not mandatory clauses of
SQL statements, but should be used to limit the number of rows
affected by a SQL DML statement or returned by a query.",
     "documentMetadata": {
       "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/3825eac51ef9e934bbc558faa42f4c71",
       "uri": "gs://my-bucket-
123/documents/26f5872b0719790cb966a697bfa1ea27.txt"
       "structData": {
         "fields": [
           {
             "key": "cdoc_url"
             "value": { "stringValue":
"26f5872b0719790cb966a697bfa1ea27" }
           },
           {
             "key": "doc_id"
             "value": { "stringValue":
"3825eac51ef9e934bbc558faa42f4c71" }
           }
         ]
       }
     }
   }
 },
 {
   "chunkInfo": {
     "content": "This chapter focuses on using Paradox as a
client/server development tool.It does not talk about connecting; it
is assumed you have already connected.If you are having trouble
connecting to a particular SQL server, then refer to the Connection
Guide for that particular server.This chapter does review what a user
can do interactively with Paradox and how to use ObjectPAL with SQL
servers.Structured Query Language (SQL) was developed to create a
standard for accessing database information.The ANSI standard for SQL
allows a user to become familiar with the commands needed to query
many different types of data.After you learn ANSI SQL, you then can
query many different databases.Is SQL a solid standard?Yes and
no.Yes, the core ANSI SQL commands are solid and consistent from
vendor to vendor.Every vendor, however, adds capability to its
version of SQL.These improvements are expected because ANSI SQL does
not go far enough to cover every feature of every high-end DBMS.The
SQL standard is used by many companies for their high-end
products.They include Oracle, Sybase, Microsoft SQL, Informix, and
Interbase.Paradox also provides the capability to use standard ANSI
SQL commands on local Paradox and dBASE tables.Although SQL by
definition is a standard, various flavors are on the market.",
     "documentMetadata": {
       "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/b3e88db8676b87b99af1e6ecc7d8757f",
       "uri": "gs://my-bucket-
123/documents/073c21335d37d8d14982cb3437a721c0.txt"
       "structData": {
         "fields": [
           {
             "key": "cdoc_url"
             "value": { "stringValue":
"073c21335d37d8d14982cb3437a721c0" }
           },
           {
             "key": "doc_id"
             "value": { "stringValue":
"b3e88db8676b87b99af1e6ecc7d8757f" }
           }
         ]
       }
     }
   }
 }
],
...
"steps": [
 {
   "state": "SUCCEEDED",
   "description": "Rephrase the query and search.",
   "actions": [
     {
       "searchAction": {
         "query": "What is SQL?"
       },
       "observation": {
         "searchResults": [
           {
             "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/d993d922043374f5ef7ba297c158b106",
             "uri": "gs://my-bucket-
123/documents/058dee0ec23a3e92f9bfd7cd29840e8f.txt",
             "chunkInfo": [
               {
                 "content": "There are a lot of Databases available
in the market such as MS Access, Oracle and many others.For you to
write programs that interact with these databases easily, there has
to be a way where you could get information from all these databases
using the same method.For this purpose SQL was developed.It is a kind
of language (simple when compared to the likes of C or C++) which
enables you to ask all your queries to a database without bothering
about the exact type of database.When you use this Query the database
engine would first find the table called people.Then it would find a
column called firstname.Next it would compare all the values in that
column with 'Reena'.Finally it would return all the details wherever
it finds a match for the firstname.When you write a database program
in VC++ or Java or any other language for that matter, you would make
a database connection to your database and then you would query the
database using SQL queries.When you query the database with any SQL
query the database returns a recordset.A recordset is basically a set
of records (all the entries that your query returns).This recordset
is received in your program and all languages have a data structure
which represents a recordset."
               }
             ]
           },
           {
             "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/3825eac51ef9e934bbc558faa42f4c71",
             "uri": "gs://my-bucket-
123/documents/26f5872b0719790cb966a697bfa1ea27.txt",
             "chunkInfo": [
               {
                 "content": "The Structured Query Language (SQL) is
a database management programming language.SQL is a tool for
accessing databases, and more specifically, relational databases, and
can be used with different database products.This chapter will
prepare you to learn basic database management using this
language.SQLite – To implement SQL as a library, you need
SQLite.SQLite is intended to provide users and programs a way to
store data using a SQL interface within the program.SQLite3 can be
used to manipulate SQLite databases for major Linux distros.SQL is
used to access relational databases.Each database contains more or
less tables which in turn contain more or less rows and
columns.Hereby a single row is seen as a separate object with
features represented by the tables' columns.To access a table's data
you first have to connect to its database.With the same table, the
query SELECT * FROM T WHERE C1 = 1 will result in all the elements of
all the rows where the value of column C1 is '1' being shown.A WHERE
clause specifies that a SQL statement should only affect rows that
meet specified criteria.The criteria are expressed in the form of
predicates.WHERE clauses are not mandatory clauses of SQL statements,
but should be used to limit the number of rows affected by a SQL DML
statement or returned by a query."
               }
             ]
           },
           {
             "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/b3e88db8676b87b99af1e6ecc7d8757f",
             "uri": "gs://my-bucket-
123/documents/073c21335d37d8d14982cb3437a721c0.txt",
             "chunkInfo": [
               {
                 "content": "This chapter focuses on using Paradox
as a client/server development tool.It does not talk about
connecting; it is assumed you have already connected.If you are
having trouble connecting to a particular SQL server, then refer to
the Connection Guide for that particular server.This chapter does
review what a user can do interactively with Paradox and how to use
ObjectPAL with SQL servers.Structured Query Language (SQL) was
developed to create a standard for accessing database information.The
ANSI standard for SQL allows a user to become familiar with the
commands needed to query many different types of data.After you learn
ANSI SQL, you then can query many different databases.Is SQL a solid
standard?Yes and no.Yes, the core ANSI SQL commands are solid and
consistent from vendor to vendor.Every vendor, however, adds
capability to its version of SQL.These improvements are expected
because ANSI SQL does not go far enough to cover every feature of
every high-end DBMS.The SQL standard is used by many companies for
their high-end products.They include Oracle, Sybase, Microsoft SQL,
Informix, and Interbase.Paradox also provides the capability to use
standard ANSI SQL commands on local Paradox and dBASE tables.Although
SQL by definition is a standard, various flavors are on the market."
               }
             ]
           },
           {
             "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/3dd4014e41044c5dd6a0fe380847f369",
             "uri": "gs://my-bucket-
123/documents/76245cb33a66f4fbd9030a2a11eea00d.txt",
             "chunkInfo": [
               {
                 "content": "SQL injection is a code injection
```

`technique that might destroy your database.You can read more here OWASP sql injection testing sheet.Description: SQL injection ( second order) SQL injection vulnerabilities arise when user- controllable data is incorporated sheet into database SQL queries in an unsafe manner.This sheet cheat wiki assumes you have a basic understanding of SQL injection, please go here for an introduction if you are unfamiliar.Bypass login page with sql SQL injection [ closed].Gone are the days when knowledge sheet of just sql SQL Injection or XSS could help you land a lucrative high- paying InfoSec job.There is many sheet differnet variations you would login have probably have to try to make this exploit work ( sql especially if it is sql a blind SQL exploit).SQL injection usually occurs when you ask a user for input, like their.` ゲストブック `/` コメントの例 `.Submit Text Post.Get an adfree experience with special benefits, and directly support Reddit.get reddit premium.SQL Injection Cheat.Many web applications have an authentication system: a user provides a user name and password, the web application checks them and stores the corresponding user id in the session hash.Login # 1 Login # 2 Login # 3 Login # 4."` 

<!-- Start of picture text -->
               }<br>             ]<br>           }<br>         ]<br>       }<br>     }<br>   ]<br> }<br>]<br>}<br>}<br><!-- End of picture text -->

In this example, a support score (`groundingScore`) is returned for each citation. 

#### Show only well-grounded answers

The following command shows how to return only those answers that are deemed to be well grounded in the _corpus_ , the information in the data store. Poorlygrounded answers are filtered out. 

You choose a low or high level threshold for the grounding support score. Then, the answer is only returned if it meets or exceeds that level. You can experiment with 

the two filter thresholds and with no threshold to determine what level of filter is likely to provide the best results for your users. 

REST 

(#rest) 

To return an answer only if it meets a support-score threshold, do the following: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "groundingSpec": {
          "filteringLevel": "FILTER_LEVEL"
       }
     }'
```

- Replace the following: 

   - _`PROJECT_ID`_ : the ID of your project. 

   - _`APP_ID`_ : the ID of the app that you want to query. 

   - _`QUERY`_ : a free-text string that contains the question or search query. 

   - _`FILTER_LEVEL`_ : an enumeration for filtering answers based on grounding support score. Options are: `FILTERING_LEVEL_LOW` and `FILTERING_LEVEL_HIGH` . If `filteringLevel` is not included, then no support-score filter is applied to the answer. 

- <sup>Example command and partial result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/
global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer" \
-d '{
   "query": { "text": "When can an NCD be made?"},
   "groundingSpec": {
      "filtering_level": "FILTERING_LEVEL_HIGH"
   }
 }'
 {
   answer {
     state: SUCCEEDED
answer_text: "We do not have a summary for your query."
     steps {
       state: SUCCEEDED
       description: "Rephrase the query and search."
       actions {
         search_action {
           query: "test?"
         }
         observation {
           search_results {
             document:
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-store/branches/0/documents/f7f5cfde02"
             uri: "gs://my-bucket-
123/data/CoverageDocumentation.pdf"
             title: "ABC345_0101"
             chunk_info {
               content: "This notice implements part of section 731
of the Medicare Prescription Drug, Improvement, and Modernization Act
of 2003 by describing a method of developing, and making available to
the public, guidance documents under the Medicare program… "
             }
   ...
           search_results {
             document:
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-store/branches/0/documents/f7f5cfde02"
             uri: "gs://my-bucket-
123/data/CoverageDocumentation.pdf"
             title: "ABC345_0101"
             chunk_info {
               content: "For the purposes of this notice, the term
guidance documents means documents prepared for our staff, potential
requestors of National Coverage Determinations, and other interested
parties explaining the NCD process… "
             }
           }
         }
       }
     }
answer_skipped_reasons: LOW_GROUNDED_CONTENT
   }
```

In this example, no answer is returned because the high threshold wasn't met. 

#### Specify the answer model

The following command shows how to change the model version used to generate answers. 

For information about the supported models, see Answer generation model versions and lifecycle (/gemini/enterprise/docs/answer-generation-models). 

RESTPython (#python) (#rest) 

To generate an answer using a model different from the default model, do the following: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "answerGenerationSpec": {
          "modelSpec": {
             "modelVersion": "MODEL_VERSION",
          }
        }
     }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : a free-text string that contains the question or search query. 

- _`MODEL_VERSION`_ : the model version that you want to use to generate the answer. For more information, see Answer generation model versions and lifecycle 

(/gemini/enterprise/docs/answer-generation-models). 

<sup>Example command and partial result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer" \
-d '{"query": { "text": "Compare bigquery with spanner database?"},
"answerGenerationSpec": {
    "modelSpec": {
"modelVersion": "preview",
    }
  } }'
  {
 "answer": {
   "state": "SUCCEEDED",
   "answerText": "Cloud Spanner is a fully managed relational
database optimized for transactional workloads. BigQuery is a
serverless, highly scalable, and cost-effective multi-cloud data
warehouse designed for business agility. BigQuery is optimized for
ad-hoc analysis and reporting. Both Spanner and BigQuery are built on
Google's distributed storage system, Colossus, and their internal
cluster management system, Borg. They are also built on Jupiter,
Google's in-house custom network hardware and software.\n\nBigQuery
can query data stored in Spanner in real time without moving or
copying the data. This is possible with BigQuery's query federation
support. To run a federated query, you need to configure an external
data source in BigQuery that points to the intended Spanner instance.
You can then write queries that can be used to populate a BigQuery
table on demand or scheduled to run as needed. You can also join the
query with another BigQuery result set dynamically.\n\nYou can also
use Dataflow to copy data from Spanner to BigQuery. Dataflow is a
service that can be used to ingest Spanner data into BigQuery. This
is useful for more complex transformations or external dependencies.
For example, an online gaming company might use Spanner to store game
data and BigQuery to perform analytics on player behavior. They can
replicate data from Spanner into BigQuery and perform analytics
against local data, or they can use federated queries to retrieve
data from Spanner on-demand.\n",
   "steps": [
     {
       "state": "SUCCEEDED",
       "description": "Rephrase the query and search.",
       "actions": [
         {
           "searchAction": {
             "query": "Compare bigquery with spanner database?"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/ecc0e7547253f4ca3ff3328ce89995af",
                 "uri":
"https://cloud.google.com/blog/topics/developers-practitioners/how-
spanner-and-bigquery-work-together-handle-transactional-and-
analytical-workloads",
                 "title": "How Spanner and BigQuery work together to
handle transactional and analytical workloads | Google Cloud Blog",
                 "snippetInfo": [
                   {
                     "snippet": "Using Cloud
\u003cb\u003eSpanner\u003c/b\u003e and
\u003cb\u003eBigQuery\u003c/b\u003e also allows customers to build
their \u003cb\u003edata\u003c/b\u003e clouds using Google Cloud, a
unified, open approach to \u003cb\u003edata\u003c/b\u003e-driven
transformation ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/d7e238f73608a860e00b752ef80e2941",
                 "uri":
"https://cloud.google.com/blog/products/databases/cloud-spanner-gets-
stronger-with-bigquery-federated-queries",
                 "title": "Cloud Spanner gets stronger with
BigQuery-federated queries | Google Cloud Blog",
                 "snippetInfo": [
                   {
                     "snippet": "As enterprises compete for market
share, their need for real-time insights has given rise to increased
demand for transactional \u003cb\u003edatabases\u003c/b\u003e to
support \u003cb\u003edata\u003c/b\u003e ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/e10a5a3c267dc61579e7c00fefe656eb",
                 "uri":
"https://cloud.google.com/blog/topics/developers-
practitioners/replicating-cloud-spanner-bigquery-scale",
                 "title": "Replicating from Cloud Spanner to
BigQuery at scale | Google Cloud Blog",
                 "snippetInfo": [
                   {
                     "snippet": "... \u003cb\u003eSpanner
data\u003c/b\u003e into \u003cb\u003eBigQuery\u003c/b\u003e for
analytics. In this post, you will learn how to efficiently use this
feature to replicate large tables with high throughput ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               ...
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/648c220055c1d2ac369165007d9f6650",
                 "uri":
"https://cloud.google.com/blog/products/databases/choosing-cloud-
spanner-for-game-development",
                 "title": "Choosing Cloud Spanner for game
development | Google Cloud Blog",
                 "snippetInfo": [
                   {
                     "snippet": "To get started with
\u003cb\u003eSpanner\u003c/b\u003e, create a
\u003cb\u003edatabase\u003c/b\u003e, or try it out with a
\u003cb\u003eSpanner\u003c/b\u003e Qwiklab. ... AlloyDB
\u003cb\u003evs\u003c/b\u003e. ... SQL for SQL Server to
\u003cb\u003eBigQuery\u003c/b\u003e. By Alexander ...",
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
 },
 "answerQueryToken":
"NMwKDAivmvy2BhCxnsqdARIkNjZkOTQ0NWEtMDAwMC0yMTBkLTllNmItZjQwMzA0NWRi
ZDMw"
}
```

In this example, the preview version of the model is used instead of the default model. 

#### Specify a custom preamble

The following command shows how to set a preamble for the generated answer. A preamble contains natural language instructions for customizing the answer. You can request customizations such as length, level of detail, style of output (such as "simple"), language of output, focus of answer, and format (such as tables, bullets, and XML). For example, a preamble might be "Explain like you are a ten years old kid." 

The preamble can have a significant effect on the quality of the generated answer. For information about what to write in preambles and examples of good preambles, see About custom preambles (/gemini/enterprise/docs/preamble). 

RESTPython (#python) (#rest) 

To generate an answer using a model different from the default model, do the following: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "answerGenerationSpec": {
          "promptSpec": {
              "preamble": "PREAMBLE",
          }
       }
     }'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : a free-text string that contains the question or search query. 

_`PREAMBLE`_ : a natural-language instruction for customizing the answer. For example, try `show the answer format in an ordered list` or `give a very detailed answer` . 

<sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)"
   -H "Content-Type: application/json"
   "https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer" \
   -d '{
         "query": { "text": "what is bigquery?"},
         "answerGenerationSpec": {
            "promptSpec": {
               "preamble": "Explain like you are a ten years old
               kid",
    }
 }
}'
{
 "answer": {
   "state": "SUCCEEDED",
   "answerText": "BigQuery is like a super-powered storage space for
your data, but it's in the cloud, not on your computer. It's like a
giant warehouse for all your information, but you don't have to build
or manage it yourself. You can use BigQuery to find patterns and
insights in your data, like figuring out what people like to buy or
how many people visited your website. It's like having a super-smart
assistant that can help you understand your data better. BigQuery is
really good at working with lots of data, even billions of pieces of
information. \n",
   "steps": [
     {
       "state": "SUCCEEDED",
       "description": "Rephrase the query and search.",
       "actions": [
         {
           "searchAction": {
             "query": "What is BigQuery?"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/2d032dc582689e8c0ecea7fc7bfa3189",
                 "uri": "https://cloud.google.com/bigquery",
                 "title": "BigQuery enterprise data warehouse |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "\u003cb\u003eBigQuery\u003c/b\u003e
is a fully managed, AI-ready data analytics platform that helps you
maximize value from your data and is designed to be multi-engine,
multi-format, ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/4474f4a5a18ecd611dedfe323dfe55d9",
                 "uri":
"https://cloud.google.com/bigquery/docs/introduction",
                 "title": "BigQuery overview | Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "\u003cb\u003eBigQuery\u003c/b\u003e
is a fully managed, AI-ready data platform that helps you manage and
analyze your data with built-in features like machine learning,
search, ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/c840fdef90d86328f13bbedbdbf0ac10",
                 "uri":
"https://cloud.google.com/bigquery/docs/query-overview",
                 "title": "Overview of BigQuery analytics | Google
Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "\u003cb\u003eBigQuery\u003c/b\u003e
lets you save queries and share queries with others. When you save a
query, it can be private (visible only to you), shared at the project
level ( ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
...
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/5cbfab8ce1d5f6ffe45fef22900c9a00",
                 "uri": "https://cloud.google.com/curated-
resources/bigquery",
                 "title": "Guides BigQuery | Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "\u003cb\u003eBigQuery\u003c/b\u003e
is Google Cloud's fully managed and serverless enterprise data
warehouse solution, designed to help you make informed decisions
quickly, so you can ...",
                     "snippetStatus": "SUCCESS"
                   }
```

<!-- Start of picture text -->
                 ]<br>               }<br>             ]<br>           }<br>         }<br>       ]<br>     }<br>   ]<br> },<br> "answerQueryToken": "NMwKDAi8hN-<br>2BhC0jMCPARIkNjZkN2I4MzItMDAwMC0yMTliLTkxN2EtMDg5ZTA4MjA0YjFj"<br>}<br><!-- End of picture text -->

In this example, the preamble requests a simpler answer than the default might provide. 

#### Include citations

The following command shows how to request citations to be included with the answer. 

RESTPython (#python) (#rest) 

To generate an answer using a model different from the default model, do the following: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "answerGenerationSpec": {
          "includeCitations": INCLUDE_CITATIONS
       }
     }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : a free-text string that contains the question or search query. 

- _`INCLUDE_CITATIONS`_ : specifies whether to include citation metadata in the answer. The default value is `false` . 

<sup>Example command and partial result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer" \
-d '{"query": { "text": "What is SQL"},   "answerGenerationSpec": {
   "includeCitations": true
}
}'
{
 "answer": {
   "state": "SUCCEEDED",
   "answerText": "SQL stands for Structured Query Language and is a
programming language used to manage, query, and retrieve data in a
relational database. It is the standard language used by relational
database management systems (RDBMS) such as PostgreSQL, SQL Server,
MySQL, and Oracle Database. SQL statements are written in a statement
format for queries and other database operations, allowing users to
manipulate data in relational database tables. SQL is used to create
and update the structure of tables, read and write data, manage user
permissions, and perform administrative tasks. While originally
created for relational databases, SQL is now a foundation for many
technology capabilities, making SQL knowledge essential for many
technology roles. \n",
"citations": [
     {
       "endIndex": "137",
       "sources": [
         {
           "referenceId": "0"
         },
         {
           "referenceId": "1"
         }
       ]
     },
     {
       "startIndex": "138",
       "endIndex": "437",
       "sources": [
         {
           "referenceId": "3"
         }
       ]
     },
     {
       "startIndex": "438",
       "endIndex": "575",
       "sources": [
         {
           "referenceId": "2"
         }
       ]
     },
     {
       "startIndex": "576",
       "endIndex": "742",
       "sources": [
         {
           "referenceId": "3"
         }
       ]
     }
   ],
   "references": [
     {
       "chunkInfo": {
         "content": "There may be a second table that stores visit
information. A relational database uses a unique ID for each row to
maintain the linked patient information across the two tables. This
way, you can quickly look up the visits of each patient. Sign up for
a free trial for any of Google Cloud's SQL databases, which include
AlloyDB, Cloud SQL, and Spanner. Get started for free What is SQL?
SQL (Structured Query Language) is a programming language used to
store, retrieve, and manage data in a relational database. SQL
statements are English-like, making the language accessible to
software developers, data analysts, and other practitioners. Benefits
of SQL databases Enterprises choose SQL databases for being:
Efficient. Relational databases are incredibly efficient in managing
complex queries. Fast. SQL databases can retrieve large amounts of
data, quickly. This makes them highly desirable for real-time
transactional data. Reliable. SQL databases provide a high degree of
data integrity and are ACID-compliant. SQL database engines There are
numerous SQL database engines (products) used to build software
applications. Some of the most popular include PostgreSQL, MySQL, SQL
Server, and Oracle. Some database engines are open source while
others are commercial offerings. ",
         "relevanceScore": 0.9,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
           "uri": "https://cloud.google.com/discover/what-are-sql-
databases",
           "title": "SQL Databases | Google Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "PostgreSQL vs. SQL Server: What's the
difference? | Google Cloud Page Contents Topics PostgreSQL vs. SQL
PostgreSQL vs SQL Server: What are the key differences? Trying to
find the right database for your applications? When it comes to
choosing a database technology, the most common SQL options to
consider are PostgreSQL vs. SQL Server. While both systems share many
core features, there are some key differences—the major one being
that PostgreSQL is open source and SQL Server is owned by Microsoft.
Today, it is more vital than ever for companies to be able to manage,
store, and activate data for modern business operations. With the
growing assortment of databases available to choose from, it can be
overwhelming to pick the right one for your applications. The most
important thing to remember is that no single database will be a good
match for every project requirement, so it's critical to understand
the option that will work best for your specific use case. So, what
is PostgreSQL vs. SQL Server? In this short guide, we'll discuss the
basic differences between PostgreSQL and SQL Server. Get started for
freeStay informed What is SQL? Structured Query Language or SQL, as
it's more commonly known, is a programming language used to manage,
query, and retrieve data in a relational database. ",
         "relevanceScore": 0.8,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f7cd9afab1282a9f57cdcee1885bb4c6",
           "uri": "https://cloud.google.com/learn/postgresql-vs-
sql",
           "title": "PostgreSQL vs. SQL Server: What's the
difference? | Google Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "SQL Databases | Google Cloud Page Contents
Topics What are SQL databases? What are SQL databases? A SQL
database, also known as a relational database, is a system that
stores and organizes data into highly structured tables of rows and
columns. These databases offer Structured Query Language (SQL) to
read and write the data, and are categorized as relational database
management systems (RDBMS). SQL statements are used to create and
update the structure of tables, read and write data, manage user
permissions, and perform administrative tasks. For example, a CREATE
statement is used to create a table, an INSERT statement adds a new
row to a table, and a SELECT statement performs a database query.
Statements that make structural or administrative changes are usually
reserved for software developers and administrators, while read and
write operations are performed by end-user applications. A relational
database maintains the ability to link information across multiple
tables. This format makes it easy to quickly gain insights about the
relationships between various columns or data points in these tables.
A relational database can create indexes for particular columns for
faster lookups. For example, a healthcare facility might maintain a
table containing rows of patient information, where each row is one
patient and the columns contain data points, such as the patient's
name, insurance information, and contact details. ",
         "relevanceScore": 0.8,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
           "uri": "https://cloud.google.com/discover/what-are-sql-
databases",
           "title": "SQL Databases | Google Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "It is the standard language used by relational
database management systems (RDBMS), including PostgreSQL, SQL
Server, MySQL, and Oracle Database. SQL typically uses commands
written in statement format for queries and other database
operations, which allow users to manipulate data in relational
database tables. While originally created for relational databases,
SQL acts as a foundation for many of today's technology capabilities,
making SQL knowledge an essential skill for many technology roles
today, including data analysts, database engineers, and even backend
programming. However, you will find that there are different variants
of SQL depending on the database or database management system that
you choose. What is Microsoft SQL Server? SQL Server is a leading
RDBMS that is built on top of SQL and developed by Microsoft. It is
used to manage and store data to support numerous enterprise use
cases for business intelligence, transaction processing, data
analytics, and machine learning services. SQL Server has a row-based
table structure that allows you to connect related data elements from
different tables without having to store data multiple times in a
database. In general, Microsoft SQL Server is known for its high
availability, fast performance when handling large workloads, and
easy integration with other applications to gain business
intelligence across your entire data estate. For more information, we
recommend reviewing the official SQL Server documentation. ",
         "relevanceScore": 0.8,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f7cd9afab1282a9f57cdcee1885bb4c6",
           "uri": "https://cloud.google.com/learn/postgresql-vs-
sql",
           "title": "PostgreSQL vs. SQL Server: What's the
difference? | Google Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "Send feedback The GoogleSQL language in Spanner
bookmark_borderbookmark Stay organized with collections Save and
categorize content based on your preferences. Dismiss Got it
GoogleSQL is the new name for Google Standard SQL! New name, same
great SQL dialect. This page provides an overview of supported
statements in GoogleSQL. GoogleSQL is an ANSI compliant Structured
Query Language (SQL) which includes the following types of supported
statements: Query statements, also known as Data Query Language (DQL)
statements, are the primary method to analyze data in Spanner. They
scan one or more tables or expressions and return the computed result
rows. Data Definition Language (DDL) statements let you create and
modify database objects such as tables, views, and database roles.
Data Manipulation Language (DML) statements enable you to update,
insert, and delete data from your Spanner tables. Data Access Control
statements let you grant and revoke access privileges at the table
and column level. Transaction Control statements allow you to manage
transactions for data modifications. Was this helpful? Send feedback
       "chunkInfo": {
         "content": "FAQ Expand all What is Cloud SQL? Cloud SQL is
a service that delivers fully managed relational databases in the
cloud. It offers MySQL, PostgreSQL, and SQL Server database engines.
How is Cloud SQL different from other cloud databases? Cloud SQL is
valued for its openness, ease of use, security, cost-efficiency, and
Google Cloud integration—in fact, more than 95% of Google Cloud's top
100 customers use it. If you're comparing PostgreSQL options on
Google Cloud, view our comparison chart. What's the difference
between the Enterprise and Enterprise Plus editions? For PostgreSQL,
the Enterprise Plus edition brings enhanced availability,
performance, and data protection capabilities. Specifically, it
provides a 99.99% availability SLA with near-zero downtime
maintenance, optimized hardware and software configurations,
intelligent data caching for read-intensive transactional workloads,
a configurable data cache option and 35 days of log retention. For
MySQL, the Enterprise Plus edition brings enhanced availability,
performance, and data protection capabilities. Specifically, it
provides a 99.99% availability SLA with near-zero downtime
maintenance, optimized hardware and software configurations,
intelligent data caching for read-intensive transactional workloads,
a configurable data cache option, 35 days of log retention and
advanced disaster recovery capabilities like orchestrated failover
and switchback. ",
         "relevanceScore": 0.7,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/931f2c8e19ed54a407857f1cad3b5aaa",
           "uri": "https://cloud.google.com/sql",
           "title": "Cloud SQL for MySQL, PostgreSQL, and SQL Server
| Google Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "PostgreSQL versus SQL PostgreSQL is an open-
source, object-relational database (ORDBMS) designed for enterprise-
level performance and is valued for its reliability and robust
features. Its long history of development and its use of SQL makes it
one of the most popular open source databases worldwide. Its default
procedural language is an extension of pgSQL (PL/pgSQL), with
procedural language extensions of Tcl, Perl, and Python included in
the standard distribution (written as PL/Tcl, PL/Perl, and
PL/Python). Many more languages are supported through extensions,
including Java, Ruby, C, C++, Delphi, and JavaScript. For a more in-
depth comparison, visit our PostgreSQL versus SQL guide. MySQL versus
SQL MySQL is a popular open source relational database created in
1995 and currently sponsored by Oracle. It supports SQL queries and
can be administered either through a graphical user interface (GUI)
or a command line. MySQL can be deployed manually on a physical
machine or through a cloud service provider. Enterprises are
increasingly choosing fully managed services to reduce the
maintenance burden of their databases. What is SQL Server? SQL Server
is a Microsoft-owned database that runs SQL queries. Dive into the
differences between PostgreSQL and SQL Server. ",
         "relevanceScore": 0.6,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
           "uri": "https://cloud.google.com/discover/what-are-sql-
databases",
           "title": "SQL Databases | Google Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "Send feedback On this page BigQuery SQL
dialects Changing from the default dialect What's next Introduction
to SQL in BigQuery bookmark_borderbookmark Stay organized with
collections Save and categorize content based on your preferences.
Dismiss Got it GoogleSQL is the new name for Google Standard SQL! New
name, same great SQL dialect. This document provides an overview of
supported statements and SQL dialects in BigQuery. GoogleSQL is an
ANSI compliant Structured Query Language (SQL) which includes the
following types of supported statements: Query statements, also known
as Data Query Language (DQL) statements, are the primary method to
analyze data in BigQuery. They scan one or more tables or expressions
and return the computed result rows. Procedural language statements
are procedural extensions to GoogleSQL that allow you to execute
multiple SQL statements in one request. Procedural statements can use
variables and control-flow statements, and can have side effects.
Data Definition Language (DDL) statements let you create and modify
database objects such as tables, views, functions, and row-level
access policies. Data Manipulation Language (DML) statements enable
you to update, insert, and delete data from your BigQuery tables.
Data Control Language (DCL) statements let you control BigQuery
system resources such as access and capacity. Transaction Control
Language (TCL) statements allow you to manage transactions for data
modifications. ",
         "relevanceScore": 0.6,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/2f6fc3e29873518196cb50195d7ded45",
           "uri":
"https://cloud.google.com/bigquery/docs/introduction-sql",
           "title": "Introduction to SQL in BigQuery | Google Cloud"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "Database administration Cloud SQL pricing
Connect to a Cloud SQL managed database Cloud SQL updates
Configuration updates System updates What's next Home Cloud SQL
Documentation Guides Was this helpful? Send feedback Cloud SQL
overview bookmark_borderbookmark Stay organized with collections Save
and categorize content based on your preferences. Dismiss Got it On
this page Database configurations with Cloud SQL Use cases for Cloud
SQL What Cloud SQL provides What is a Cloud SQL instance? Database
administration Cloud SQL pricing Connect to a Cloud SQL managed
database Cloud SQL updates Configuration updates System updates
What's next Cloud SQL is a fully managed relational database service
for MySQL, PostgreSQL, and SQL Server. This frees you from database
administration tasks so that you have more time to manage your data.
This page discusses basic concepts and terminology for Cloud SQL,
which provides SQL data storage for Google Cloud. For a more in-depth
explanation of key concepts, see the key terms and features pages.
For information about how Cloud SQL databases compare with one
another, see Cloud SQL feature support by database engine. Database
configurations with Cloud SQL The following video shows you the
benefits of using Cloud SQL. ",
         "relevanceScore": 0.6,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/4098ae11bfa400e8f1b8e9ba59d2b71b",
           "uri": "https://cloud.google.com/sql/docs/introduction",
           "title": "Cloud SQL overview"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "Cloud SQL documentation View all product
documentation Cloud SQL is a fully-managed database service that
helps you set up, maintain, manage, and administer your relational
databases on Google Cloud Platform. You can use Cloud SQL with MySQL,
PostgreSQL, or SQL Server. Not sure what database option is right for
you? Learn more about our database services. Learn more about Cloud
SQL. Documentation resources Find quickstarts and guides, review key
references, and get help with common issues. format_list_numbered
Guides Cloud SQL overview Database engine feature support MySQL
PostgreSQL SQL Server find_in_page Reference gcloud commands REST API
Client libraries info Resources Pricing Release notes Resources Try
Cloud SQL for yourself Create an account to evaluate how our products
perform in real-world scenarios. New customers also get $300 in free
credits to run, test, and deploy workloads. Try Cloud SQL free Was
this helpful? Except as otherwise noted, the content of this page is
licensed under the Creative Commons Attribution 4.0 License, and code
samples are licensed under the Apache 2.0 License. For details, see
the Google Developers Site Policies. Java is a registered trademark
of Oracle and/or its affiliates. Last updated 2024-08-29 UTC. ",
         "relevanceScore": 0.5,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/37935181d99a6ad3b4897e673a7a7986",
           "uri": "https://cloud.google.com/sql/docs",
           "title": "Cloud SQL documentation"
         }
       }
     }
     ],
   "steps": [
     {
       "state": "SUCCEEDED",
       "description": "Rephrase the query and search.",
       "actions": [
         {
           "searchAction": {
             "query": "What is SQL?"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
                 "uri": "https://cloud.google.com/discover/what-are-
sql-databases",
                 "title": "SQL Databases | Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "\u003cb\u003eSQL\u003c/b\u003e
(Structured Query Language) is a programming language used to store,
retrieve, and manage data in a relational database.
\u003cb\u003eSQL\u003c/b\u003e statements are English-like, ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f7cd9afab1282a9f57cdcee1885bb4c6",
                 "uri": "https://cloud.google.com/learn/postgresql-
vs-sql",
                 "title": "PostgreSQL vs. SQL Server: What's the
difference? | Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "\u003cb\u003eSQL\u003c/b\u003e
typically uses commands written in statement format for queries and
other database operations, which allow users to manipulate data in
relational database ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/3afdede140d0906c2146a2f2b3a7821e",
                 "uri":
"https://cloud.google.com/blog/topics/developers-practitioners/what-
cloud-sql",
                 "title": "What is Cloud SQL? | Google Cloud Blog",
                 "snippetInfo": [
                   {
                     "snippet": "It is a fully managed relational
database for MySQL, PostgreSQL and \u003cb\u003eSQL\u003c/b\u003e
Server. It reduces maintenance cost and automates database
provisioning, storage ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               ...
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/0c5c094170756eeb6bdfec6eb5c7d081",
                 "uri":
"https://cloud.google.com/spanner/docs/reference/standard-
sql/overview",
                 "title": "The GoogleSQL language in Spanner |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet":
"\u003cb\u003eGoogleSQL\u003c/b\u003e is the new name for Google
Standard \u003cb\u003eSQL\u003c/b\u003e! New name, same great
\u003cb\u003eSQL\u003c/b\u003e dialect. This page provides an
overview of supported statements in
\u003cb\u003eGoogleSQL\u003c/b\u003e.",
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
 },
 "answerQueryToken":
"NMwKDAiFm_y2BhC_nfrYAxIkNjZkYjg3NjItMDAwMC0yZTBkLTg0ZDAtMDg5ZTA4MmRj
Yjg0"
}
```

#### Set the answer language code

The following command shows how to set the language code for answers. 

RESTPython (#python) (#rest) 

To generate an answer using a model different from the default model, do the following: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "answerGenerationSpec": {
          "answerLanguageCode": "ANSWER_LANGUAGE_CODE"
          }
     }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

_`APP_ID`_ : the ID of the app that you want to query. 

_`QUERY`_ : a free-text string that contains the question or search query. 

_`ANSWER_LANGUAGE_CODE`_ : a language code for the answer. Use language tags defined by BCP47: Tags for Identifying Languages (https://www.rfc-editor.org/rfc/bcp/bcp47.txt). 

<sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer" \
-d '{"query": { "text": "What is SQL"},   "answerGenerationSpec": {
 "answerLanguageCode": "es"
    }
}'
{
 "answer": {
   "state": "SUCCEEDED",
"answerText": "SQL, que significa Structured Query Language, es
un lenguaje de programación utilizado para almacenar, recuperar y
administrar datos en una base de datos relacional. Las instrucciones
de SQL son similares al inglés, lo que hace que el lenguaje sea
accesible para desarrolladores de software, analistas de datos y
otros profesionales. Las bases de datos SQL se utilizan para
administrar y almacenar datos para apoyar numerosos casos de uso
empresariales, como la inteligencia empresarial, el procesamiento de
transacciones, el análisis de datos y los servicios de aprendizaje
automático. SQL es el lenguaje estándar utilizado por los sistemas de
gestión de bases de datos relacionales (RDBMS), incluidos PostgreSQL,
SQL Server, MySQL y Oracle Database. SQL se utiliza para crear y
actualizar la estructura de las tablas, leer y escribir datos,
administrar los permisos de los usuarios y realizar tareas
administrativas. \n",
   "steps": [
     {
       "state": "SUCCEEDED",
       "description": "Rephrase the query and search.",
       "actions": [
         {
           "searchAction": {
             "query": "What is SQL?"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/7218ff4f57328d86059246d4af3a9953",
                 "uri": "https://cloud.google.com/discover/what-are-
sql-databases",
                 "title": "SQL Databases | Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "\u003cb\u003eSQL\u003c/b\u003e
(Structured Query Language) is a programming language used to store,
retrieve, and manage data in a relational database.
\u003cb\u003eSQL\u003c/b\u003e statements are English-like, ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f7cd9afab1282a9f57cdcee1885bb4c6",
                 "uri": "https://cloud.google.com/learn/postgresql-
vs-sql",
                 "title": "PostgreSQL vs. SQL Server: What's the
difference? | Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet": "\u003cb\u003eSQL\u003c/b\u003e
typically uses commands written in statement format for queries and
other database operations, which allow users to manipulate data in
relational database ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/3afdede140d0906c2146a2f2b3a7821e",
                 "uri":
"https://cloud.google.com/blog/topics/developers-practitioners/what-
cloud-sql",
                 "title": "What is Cloud SQL? | Google Cloud Blog",
                 "snippetInfo": [
                   {
                     "snippet": "It is a fully managed relational
database for MySQL, PostgreSQL and \u003cb\u003eSQL\u003c/b\u003e
Server. It reduces maintenance cost and automates database
provisioning, storage ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               ...
                               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/0c5c094170756eeb6bdfec6eb5c7d081",
                 "uri":
"https://cloud.google.com/spanner/docs/reference/standard-
sql/overview",
                 "title": "The GoogleSQL language in Spanner |
Google Cloud",
                 "snippetInfo": [
                   {
                     "snippet":
"\u003cb\u003eGoogleSQL\u003c/b\u003e is the new name for Google
Standard \u003cb\u003eSQL\u003c/b\u003e! New name, same great
\u003cb\u003eSQL\u003c/b\u003e dialect. This page provides an
overview of supported statements in
\u003cb\u003eGoogleSQL\u003c/b\u003e.",
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
 },
 "answerQueryToken":
"NMwKDAjim_y2BhDftIjEAhIkNjZkOTQ0NWQtMDAwMC0yMTBkLTllNmItZjQwMzA0NWRi
ZDMw"
}
```

In this example, although the source documents are in English, the answer is provided in Spanish.
