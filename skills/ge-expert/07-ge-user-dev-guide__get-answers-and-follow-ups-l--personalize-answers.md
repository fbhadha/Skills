# Gemini Enterprise: user guide, Workflow Builder, developer guide / Get answers and follow-ups (Legacy): Answer phase commands / Personalize answers to Commands for follow-up questions
Source: 07-Gemini-Enterprise-User-guide-Workflow-Builder-developer-guide.pdf, pages 409-446, extracted 2026-10-18

## Get answers and follow-ups (Legacy)

URL: https://docs.cloud.google.com/gemini/enterprise/docs/answer

#### Personalize answers

If there is specific information about the user available—for example, data in a profile, you can specify that information in the `endUserMetadata` 

(/gemini/enterprise/docs/reference/rest/v1/EndUserSpec) object so that the query results can be personalized for the user. 

For example, if a user is searching for information about upgrading a mobile phone, information from their profile, such as current phone model and cellular plan provides information that can personalize the generated answer. 

To add personal information about the user making a query and to generate an answer that takes into account the personal information, do the following: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/gl
obal/collections/default_collection/engines/APP_ID/servingConfigs/default_s
earch:answer" \
-d '{
   "query": { "text": "QUERY"},
   "endUserSpec": {
      "endUserMetadata": [
        {
          "chunkInfo": {
             "content": "PERSONALIZED_INFO",
             "documentMetadata":  { "title": "INFO_DESCRIPTION"}
          }
        }
      ]
   }
 }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : a free-text string that contains the question or search query. 

- _`PERSONALIZATION_INFO`_ : a string that contains information specific to the user who is making the query. For example, `This customer has a` **`Pixel 6 Pro`** `purchased over a period of` 

- **`24-months`** `starting` **`2023-01-15`** `. This customer is on the` **`Business Plus International`** `plan. No payment is due at this` 

- `time.` The length limit for this string is 8,000 characters. 

- _`INFO_DESCRIPTION`_ : a string that briefly describes the personalization information—for example, `Customer` 

`profile data, including model, plan, and billing status.` The model makes use of both this description and the personalization information when generating a customized answer to the query. 

<sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
 -H "Content-Type: application/json" \
 "https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer" \
 -d '{
       "query": { "text": "Can I upgrade my phone now?"},
       "answerGenerationSpec": { "includeCitations": true }
"endUserSpec": {
          "endUserMetadata": [
            {
              "chunkInfo": {
                "content": "This customer has a Pixel 6 Pro purchased over
a period of 24-months starting 2023-01-15. This customer is on the Business
Plus International plan. No payment is due at this time.",
                "documentMetadata":  { "title": "Customer profile data,
including model, plan, and billing status."}
              }
            }
          ]
       }
     }'
{
 "answer": {
   "state": "SUCCEEDED",
"answerText": "Yes, you qualify for the yearly device upgrade because
you've completed your 24-month payment plan.[1,3]  Since your account is
fully paid you will not need to pay any additional monthly fees…  \n",
   "citations": [
     {
       "end_index": 99
       "sources": [
          {
             "reference_id": "0"
          }
       ]
     },
     {
       "start_index": "100"
       "end_index": "240"
       "sources": [
          {
             "reference_id": "0"
          }
       ]
     },
     ...
   ]
   "references": [
     {
       "chunk_info": {
         "content":
         "+ "This customer has a Pixel 6 Pro purchased over a period of
24-months starting 2023-01-15. This customer is on the Business Plus
International plan. No payment is due at this time.",
         "relevance_score": 0.3
         "documentMetadata":  {
           "title": "Customer profile data, including model, plan, and
billing status."
         }
     {
       "chunk_info": {
         "content":
         "+ "For Cymbal Mobile upgrades, you can upgrade when you've paid
off at least half of your current device's cost and have had it for 8
months…",
         "relevance_score": 0.8
         "documentMetadata":  {
           "document":
"projects/123456/locations/us/collections/default_collection/dataStores/my-
data-store/branches/0/documents/abcd1234567890"
           "uri": "https://www.example.com/help/device-upgrade"
           "title": "Upgrade eligibility"
         }
        }
     }
     ...
```

In this example, the model uses the `endUserMetaData` to customize the answer. For illustration, this example includes citations so that you can see the importance of the `endUserMetaData` ; it's always the first reference cited. 

#### Generate charts for answers

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specifc Terms i (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

The answer 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/answer ) 

method can generate charts and return them as part of the answer to a query. 

You can specifically request that an answer include a chart, for example, "Plot the year-on-year growth rate of small business payments over years with available data". If the system determines that sufficient data is present, a chart is returned. Usually, some answer text is returned along with the chart. 

Also, if there is sufficient data to create a chart, the answer method can return a chart even if the query didn't explicitly request a chart. For example, "What was the improvement in HDI scores associated with more access to clean drinking water in the decade between 2010 and 2020?" 

Only one chart is generated per answer. However, the chart might be a composite chart, containing other smaller charts. An example of a composite chart: 

Limitation 

Queries must be in English. 

Common failure scenarios 

You won't always get an image returned with your answer. If there isn't sufficient data, a figure can't be generated. 

Other failure scenarios include code execution failures and timeouts. If either of these happen, rephrase your query and try again. 

Before you begin 

Before you run a query that asks for generated charts, do the following: 

- Make sure that you are using a Gemini 2.0 or later model. For information about the models, see Answer generation model versions and lifecycle (/gemini/enterprise/docs/answer-generation-models). 

- If you have an unstructured data store that includes documents with lots of tables and images, turn on the Layout parser 

(/gemini/enterprise/docs/parse-chunk-documents#layout-parsing). Although this isn't strictly necessary, it gives better quality results. 

Procedure 

REST 

(#rest) 

Call the answer 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.dataStores.servingCon figs/answer) 

method as follows to return an answer that can include a chart generated from the data in the data store: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/lo
cations/global/collections/default_collection/engines/APP_ID/servingC
onfigs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "answerGenerationSpec": {
         "model_spec": {
            "model_version": "MODEL_VERSION"
        },
"multimodalSpec": {
            "imageSource": "IMAGE_SOURCE"
            }
       }
     }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : a free-text string in English that contains the question or search query. 

- _`MODEL_VERSION`_ : Model version `stable` or other supported model, see Answer generation model versions and lifecycle 

- (/generative-ai-app-builder/docs/answer-generation-models). 

- _`IMAGE_SOURCE`_ : an enumeration to request that the answer include a generated chart, `FIGURE_GENERATION_ONLY` , or that the answer can include either a generated chart or an existing image from the data stores (#get-images), `ALL_AVAILABLE_SOURCES` . 

<sup>Example command and partial result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer" \
-d '{
   "query": { "text": "Plot composition of net cash used in
investing activities"},
   "answerGenerationSpec": {
     "model_spec": {
        "model_version": "gemini-3.5-flash/answer_gen/v1"
        },
"multimodalSpec": {
        "image_source": "FIGURE_GENERATION_ONLY"
        }
   }
 }'
{
 "answer": {
   "state": "SUCCEEDED",
   "answerText": "The composition of net cash used in investing
activities for the nine months ended September 30, 2020 and 2019
includes several categories. These categories are purchases of
property and equipment, purchases of marketable securities,
maturities and sales of marketable securities, purchases of non-
marketable investments, maturities and sales of non-marketable
investments, acquisitions net of cash acquired and purchases of
intangible assets, and other investing activities. For the nine
months ended September 30, 2020, the net cash used in investing
activities totaled $(25,492). For the nine months ended September 30,
2019, the net cash used in investing activities totaled
$(24,788).\n\nHere's a breakdown of the specific cash flows for
investing activities (in millions):\n\n*   **Purchases of property
and equipment:** $(16,802) in 2020 and $(17,496) in 2019\n*
**Purchases of marketable securities:** $(104,932) in 2020 and
$(80,968) in 2019\n*   **Maturities and sales of marketable
securities:** $97,751 in 2020 and $74,783 in 2019\n*   **Purchases of
non-marketable investments:** $(1,864) in 2020 and $(1,499) in
2019\n*   **Maturities and sales of non-marketable investments:**
$598 in 2020 and $297 in 2019\n*   **Acquisitions, net of cash
acquired, and purchases of intangible assets:** $(368) in 2020 and
$(373) in 2019\n*   **Other investing activities:** $125 in 2020 and
$468 in 2019",
   "steps": [
     {
       "state": "SUCCEEDED",
       "description": "Rephrase the query and search.",
       "actions": [
         {
           "searchAction": {
             "query": "Plot composition of net cash used in
investing activities"
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/b3133a895e0404984959736488992b53",
                 "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/boa-
tabular/Testing_20201030-alphabet-cash flow statement.pdf",
                 "title": "Testing_20201030-alphabet-cash flow
statement",
                 "snippetInfo": [
                   {
                     "snippet": "... \u003cb\u003eNet cash provided
by operating activities\u003c/b\u003e 42,447 | 40,093 | |
\u003cb\u003eInvesting activities\u003c/b\u003e | | | (16,802)
Purchases of property and equipment | (17,496) ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               }
             ]
           }
         }
       ]
     }
   ],
"blobAttachments": [
     {
       "data": {
         "mimeType": "image/png",
         "data":
"iVBORw0KGgoAAAANSUhEUgAACvAAZd8AEZFKHDp0CE5OTgCAZcuWYfr06QonIqIMXIGX
iIhUITY2Vq4tLCxyNdbMzEyuk5OTtZaJiEgfZd5aMj4+Xq4zr1rztm3SMs/fXIGXiOjDG
RgYyLWpqalcJyUlyfW/V7rJULVqVbl++PChDtIREemXr7766oPHPnr0CK1bt9ZeGCIiPX
XlypWPGr9lyxYtJSEi0k9ly5bFzZs30bNnT0iSBEmS8PLlS1y6dAlHjhzBpUuX8PLlS/l
cjx49cOPGDZQtW1bp6EREquHv7w9JkgAALVq0UDgNEWXGBl4iIlIFc3NzuY6MjMzV2ICA
ALkuVqyY1jIREemjzDdVb926JdeWlpZynXlr98z8/f3lunDhwtoPR0SkJzLPuYGBgXKd+
bOun5/fG8dmXjE9PT1dB+mIiPTL8uXLP2hVm19++QV169aFt7e3DlIREemXDh06wMfHJ9
fjwsLC0K1bN4wePVoHqYiI9EuRIkXwxx9/4MSJE3BycoKFhYXcsCtJEiwsLNC/f38cP34
chw4dyrJQBBERfbxChQrJde...PrTn86//Mu/5Jhjjql1NACAAeP/AX0CwI314+qiAAAA
AElFTkSuQmCC"
       },
       "attributionType": "GENERATED"
```

**`} ]`** `}, "answerQueryToken": "NMwKDAjEjOe-BhDmeX6ARIkNjdkNjBhM2QtMDAwMC0yYzU4LTgxYjctMDg5ZTA4MmNhZDgw"` In this example, a generated chart is included in the answer because the query requested a plot and there was enough data to generate the chart. 

The charts images are returned in the `blobAttachments` output with the `attributionType` of `GENERATED` . 

#### Retrieve existing images from the data store

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specifc Terms i (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

You can choose to have images from the data store returned with the answer and in citation (#citations) references. The data store must be an unstructured data store with the layout parser turned on. 

When `imageSource` is `CORPUS_IMAGE_ONLY` or `ALL_AVAILABLE_SOURCES` , then the answer (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/answer ) 

method can retrieve images from the data store as appropriate. However, turning this on doesn't mean that images are always returned. 

You get one image (maximum) per answer. Citations can contain multiple images. 

Limitations 

- The app that you're using must be connected to an unstructured data store. Images can't be returned from websites or from structured data stores. 

- Queries must be in English. 

- Image annotation through the layout parser must be applied to the data store. For information about the layout parser, see Parse and chunk documents (/gemini/enterprise/docs/parse-chunk-documents#layout-parsing). 

Procedure 

REST 

(#rest) 

Call the answer 

(/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.dataStores.servingCon figs/answer) 

method as follows to return an answer that can include an image from the data store in the answer: 

1. Run the following curl command: 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/PROJECT_ID/lo
cations/global/collections/default_collection/engines/APP_ID/servingC
onfigs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "answerGenerationSpec": {
         "model_spec": {
            "model_version": "MODEL_VERSION"
         },
         includeCitations: true,
"multimodalSpec": {
            "imageSource": "IMAGE_SOURCE"
            }
       }
     }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app that you want to query. 

- _`QUERY`_ : a free-text string in English that contains the question or search query. 

- _`MODEL_VERSION`_ : Model version `stable` or other supported model, see Answer generation model versions and lifecycle 

(/generative-ai-app-builder/docs/answer-generation-models). 

- _`IMAGE_SOURCE`_ : an enumeration to request that the answer include an image from the data store, `CORPUS_IMAGE_ONLY` , or that the answer can include either an image from the data store or a generated chart (#get-charts), `ALL_AVAILABLE_SOURCES` . 

<sup>Example command and partial result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1beta/projects/my-project-
123//locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer"   -d '{
       "query": { "text": "Display the ranking of  generations from
highest to lowest based on their spending on holiday items using
cards."},
       "answerGenerationSpec": {"includeCitations": true,
       "model_spec": {
            "model_version": "gemini-3.5-flash/answer_gen/v1"
            },
"multimodalSpec": {
     "imageSource": "CORPUS_IMAGE_ONLY"
     }
 },
 "searchSpec": {
   "searchParams": {
     "maxReturnResults": 5
   }
 }
}'
{
 "answer": {
   "state": "SUCCEEDED",
   "answerText": "Holiday spending over November-December was
weakest among Gen Xers, followed by Millennials, while Baby Boomer
spending was relatively more solid. In November, Baby Boomers saw
solid spending growth. Both Millennials and Gen X consumers had lower
holiday spending than in the same 30-day period last year. Baby
Boomers' holiday spending started to pick up from the start of
November and continued to rise throughout the month. Meanwhile,
Millennials started to ramp up their holiday spending much later in
the month. Gen X consumers consistently outspent other generations
from late October through the end of November.\n",
   "citations": [
     {
       "endIndex": "146",
       "sources": [
         {
           "referenceId": "3"
         }
       ]
     },
     {
       "startIndex": "147",
       "endIndex": "199",
       "sources": [
         {
           "referenceId": "2"
         }
       ]
     },
     {
       "startIndex": "200",
       "endIndex": "305",
       "sources": [
         {
           "referenceId": "2"
         }
       ]
     },
     {
       "startIndex": "306",
       "endIndex": "426",
       "sources": [
         {
           "referenceId": "2"
         }
       ]
     },
     {
       "startIndex": "427",
       "endIndex": "516",
       "sources": [
         {
           "referenceId": "2"
         }
       ]
     },
     {
       "startIndex": "517",
       "endIndex": "619",
       "sources": [
         {
           "referenceId": "2"
         }
       ]
     }
   ],
   "references": [
     {
       "chunkInfo": {
         "content": "Bank of America aggregated credit/debit card
spending per household includes spending from active US households
only. Only.., Consumer and Small Business Mel Roasa Vice President,
Digital and MarketingBANK OF AMERICA INSTITUTE09 November 20237",
         "relevanceScore": 0.5,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f8d7887862167c5daf6c7a30e1d464e0",
           "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/Bank of
America/1WkoquhDpqHphSnqIVKX45iers7kvmGjZ.pdf",
           "title": "1WkoquhDpqHphSnqIVKX45iers7kvmGjZ",
           "pageIdentifier": "6"
         }
       }
     },
     {
       "chunkInfo": {
         "content": "Bank of America aggregated credit/debit card
spending per household includes spending from active US households
only. Only... Digital and Marketing Riley Fillius Vice President,
Digital and MarketingBANK OF AMERICA INSTITUTE08 February 2024 7",
         "relevanceScore": 0.4,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/c4308d8610bcae3b3d2bb916090ef28b",
           "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/Bank of
America/1B3MJqELqk_S26aWb-KnLdSWwmpuB32os.pdf",
           "title": "1B3MJqELqk_S26aWb-KnLdSWwmpuB32os",
           "pageIdentifier": "6"
         }
       }
     },
...
     {
       "chunkInfo": {
         "content": "Bank of America aggregated credit/debit card
spending per household includes spending from active US households
only. Only consumer card holders making a minimum of five
transactions a month are included in the dataset. Spending from
corporate cards are excluded. Data regarding merchants who receive
payments are identified and classified by the Merchant Categorization
Code (MCC) defined by financial services companies. The data are
mapped using proprietary methods from the MCCs to the North American
Industry Classification System (NAICS), which is also used by the
Census Bureau, in order to classify spending data by subsector.
Spending data may also be classified by other proprietary methods not
using MCCs. Generations, if discussed, are defined as follows: 1. Gen
Z, born after 1995 2. Younger Millennials: born between 1989-1995 3.
Older Millennials: born between 1978-19886 11 March 2024BANK OF
AMERICA INSTITUTE4. Gen Xers: born between 1965-1977 5. Baby Boomer:
1946-1964 6. Traditionalists: pre-1946 Any reference to card spending
per household on gasoline includes all purchases at gasoline stations
and might include purchases of non-gas items. Additional information
about the methodology used to aggregate the data is available upon
request.\n\n## Contributors\n\nDavid Michael Tinsley Senior
Economist, Bank of America Institute Joe Wadford Economist, Bank of
America Institute Taylor Bowley Economist, Bank of America Institute
Liz Everett Krisberg Head of Bank of America Institute\n\n##
Sources\n\nLi Wei Director, Global Risk Analytics Kimberly Warren
Director, Global Risk Analytics Ana Maxim Senior Vice President,
Consumer and Small Business Mel Roasa Vice President, Digital and
MarketingBANK OF AMERICA INSTITUTE11 March 2024 7",
         "relevanceScore": 0.3,
         "documentMetadata": {
           "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/719bfb7c1c0cde3888debd43542aabfe",
           "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/Bank of
America/1odEo6QRllsURLZRDwHNruCXK9bsWmhtR.pdf",
           "title": "1odEo6QRllsURLZRDwHNruCXK9bsWmhtR",
           "pageIdentifier": "6"
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
             "query": "Rank generations from highest to lowest based
on their spending on holiday items using cards."
           },
           "observation": {
             "searchResults": [
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/935c4e1f18ccff2b5fa51d6d00e40dc4",
                 "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/Bank of
America/1baMNJuizoK7u3P2-gYRwpVz_46-uOhn4.pdf",
                 "title": "1baMNJuizoK7u3P2-gYRwpVz_46-uOhn4",
                 "snippetInfo": [
                   {
                     "snippet": "## Exhibit 6: Credit and debit
\u003cb\u003ecard spending\u003c/b\u003e per household on
\u003cb\u003eholiday items\u003c/b\u003e by
\u003cb\u003egeneration\u003c/b\u003e (index, Aug-Sep average=100 for
each year, 7- day moving average) ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/0b4c8cfb6f5ed9ef0df70ffcd79fe2c0",
                 "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/Bank of
America/1pVkzcMDNAy-p7AlrE0LRlhpbbDzCNndJ.pdf",
                 "title": "1pVkzcMDNAy-p7AlrE0LRlhpbbDzCNndJ",
                 "snippetInfo": [
                   {
                     "snippet": "Consumer
\u003cb\u003espending\u003c/b\u003e finished solidly in 2023,
\u003cb\u003ewith\u003c/b\u003e total \u003cb\u003ecard
spending\u003c/b\u003e per household increasing by 0.2% year-over-
year (YoY) in December, according to Bank of ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/f8d7887862167c5daf6c7a30e1d464e0",
                 "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/Bank of
America/1WkoquhDpqHphSnqIVKX45iers7kvmGjZ.pdf",
                 "title": "1WkoquhDpqHphSnqIVKX45iers7kvmGjZ",
                 "snippetInfo": [
                   {
                     "snippet": "This could be due to an increasing
customer \u003cb\u003ebase\u003c/b\u003e or inactive customers
\u003cb\u003eusing their cards\u003c/b\u003e more frequently. Per
household \u003cb\u003ecard spending\u003c/b\u003e growth only looks
at ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/719bfb7c1c0cde3888debd43542aabfe",
                 "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/Bank of
America/1odEo6QRllsURLZRDwHNruCXK9bsWmhtR.pdf",
                 "title": "1odEo6QRllsURLZRDwHNruCXK9bsWmhtR",
                 "snippetInfo": [
                   {
                     "snippet": "This could be due to an increasing
customer \u003cb\u003ebase\u003c/b\u003e or inactive customers
\u003cb\u003eusing their cards\u003c/b\u003e more frequently. Per
household \u003cb\u003ecard spending\u003c/b\u003e growth only looks
at ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               },
               {
                 "document":
"projects/123456/locations/global/collections/default_collection/data
Stores/my-data-
store/branches/0/documents/c4308d8610bcae3b3d2bb916090ef28b",
                 "uri":
"gs://yipeiw_multimodal_0827/rzilleruelo_multimodal_datasets/20240806
/Document Understanding Evaluation Dataset/Bank of
America/1B3MJqELqk_S26aWb-KnLdSWwmpuB32os.pdf",
                 "title": "1B3MJqELqk_S26aWb-KnLdSWwmpuB32os",
                 "snippetInfo": [
                   {
                     "snippet": "This could be due to an increasing
customer \u003cb\u003ebase\u003c/b\u003e or inactive customers
\u003cb\u003eusing their cards\u003c/b\u003e more frequently. Per
household \u003cb\u003ecard spending\u003c/b\u003e growth only looks
at ...",
                     "snippetStatus": "SUCCESS"
                   }
                 ]
               }
             ]
           }
         }
       ]
     }
   ],
"blobAttachments": [
     {
       "data": {
         "mimeType": "image/png",
         "data":
"iVBORw0KGgoAAAANSUhEUgAABcwAAAIjCAIAAACxms+ZAAAgAElEQVR42uzdd1xTV/..
.Vv/F0NDQ4NOp3+waz94PJ5Op7+/ibro6fRiWPX/AaZ6/dAGW00gAAAAAElFTkSuQmCC"
       },
       "attributionType": "CORPUS"
     }
     ]
 },
 "answerQueryToken": "M8gKCwiPuOe-
BhDyhpgIEiQ2N2Q2MWI0Mi0wMDAwLTJjNTgtODFiNy0wODllMDgyY2FkODA"
}
```

The images are returned in the `blobAttachments` portion of the output. The image that is returned with the answer is always in the first `blobAttachments` . If present, other `blobAttachments` would contain images returned in citation references. The image returned with the answer can also be (in fact often is) also returned with a citation. The `blobAttachmentIndexes` is the index that associates the `blobAttachment` to the answer or citation text. 

The `attributionType` for returned images is always `CORPUS` to indicate that the image is from the data store. 

### Commands for follow-up questions

Follow-ups are multi-turn queries. After the first query in a follow-up session, subsequent "turns" take into account prior interactions. With follow-ups, the answer method can also suggest related questions, which your users can choose instead of entering their own follow-up questions. 

All the answer and follow-ups features described in the preceding sections, such as citations, filters, SafeSearch, ignoring certain types of queries, and using a preamble to customize answers can be applied along with follow-ups. 

#### Example of a follow-up session

The following is an example of a session with follow-ups. Suppose that you want to know about vacationing in Mexico: 

_Turn 1:_ 

   - **You:** When is the best time of the year to vacation in Mexico? 

   - **Answer with follow-ups:** The best time to vacation in Mexico is during the dry season, which runs from November to April. 

- _Turn 2:_ 

   - **You:** What is the exchange rate? 

   - **Answer with follow-ups:** 1 USD is equal to approximately 17.65 Mexican pesos. 

- _Turn 3:_ 

   - **You:** What's the average temperature in December? 

   - **Answer with follow-ups:** The average temperature varies from 7078°F. Cancun's average is ~ 77°F. 

Without follow-ups, your question "What is the exchange rate?" wouldn't be answerable because regular search wouldn't know that you wanted the Mexican exchange rate. Similarly, without follow-ups, there wouldn't be the context needed to give you temperatures specifially for Mexico. 

#### Examples of related questions

When you ask "What is the best time of the year to vacation in Mexico?", in addition to answering your question, answer and follow-ups can suggest other questions that you might ask, such as "What is the cheapest month to vacation in Mexico?" and "What are the tourist months in Mexico?". 

After the related questions feature is enabled, questions are returned as strings in the response. 

#### About sessions

To understand how follow-ups work in Gemini Enterprise, you need to understand about sessions. 

A session is made up of text queries provided by a user and responses provided by Gemini Enterprise. 

These query and response pairs are sometimes referred to as _turns_ . In the preceding example, the second turn is made up of "What is the exchange rate?" and "1 USD is equal to approximately 17.65 Mexican pesos." 

Sessions are stored with the app. In the app, a session is represented by the session resource 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions). 

In addition to containing the query and response messages, the session resource has: 

- A unique name (the session ID). 

- A state (in-progress or completed). 

- A user pseudo ID, which is a visitor ID that tracks the user. It can be assigned programmatically. 

- A start time and an end time. 

- A turn, which is a query answer pair. 

#### Store session information and get responses

You can use the command line to generate search responses and answers and to store these, along with each query in a session. 

RESTPython (#python) (#rest) 

To use the command line to create a session and generate responses from the user's input, follow these steps: 

1. Specify the app where you want to store the session: 

```
curl -X POST \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \` 

```
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/sessions" \
 -d '{
       "userPseudoId": "USER_PSEUDO_ID"
     }'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app. 

- _`USER_PSEUDO_ID`_ : this is a unique identifier for tracking a search visitor. For example, you can implement this with an HTTP cookie, which uniquely identifies a visitor on a single device. 

<sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/sessions"
-d '{
"userPseudoId": "test_user"
}'
{
 "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943",
 "state": "IN_PROGRESS",
 "userPseudoId": "test_user",
 "startTime": "2024-09-13T18:47:10.465311Z",
 "endTime": "2024-09-13T18:47:10.465311Z"
}
```

2. Note down the session ID, the numbers at the end of the `name:` field in the JSON response. In the example result, the ID is `5386462384953257772` . You need this ID in the next step. 

3. Generate an answer and add it to a session in your app: 

```
curl -X POST \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \` 

```
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfi
gs/default_search:answer" \
 -d '{
       "query": { "text": "QUERY"},
       "session":
"projects/PROJECT_ID/locations/global/collections/default_collection/
engines/APP_ID/sessions/SESSION_ID",
         "searchSpec":{ "searchParams": {"filter": "FILTER"} }
}'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app. 

- _`QUERY`_ : a free-text string that contains the question or search query. 

- _`SESSION_ID`_ : the ID for the session that you created in step 1. These are the digits at the end of the `name:` field, noted step 2. For a session, use the same session ID in every turn. 

- _`FILTER`_ : a text field for filtering search using a filter expression. The default value is an empty string. The way you construct your filter varies depending on whether you have unstructured data with metadata, structured data, or website data. For more information, see Filter custom search for structured or unstructured data 

(/gemini/enterprise/docs/filter-search-metadata). 

<sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/servingConfigs/default_search:answer"
-d '{
"query": { "text": "Compare bigquery with spanner database?"},
"session":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943",
}'
{
 "answer": {
   "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-
app/sessions/16002628354770206943/answers/4861507376861383072",
   "state": "SUCCEEDED",
   "answerText": "BigQuery and Spanner are both powerful tools that
can be used together to handle transactional and analytical
workloads. Spanner is a fully managed relational database optimized
for transactional workloads, while BigQuery is a serverless data
warehouse designed for business agility. Spanner provides seamless
replication across regions in Google Cloud and processes over 1
billion requests per second at peak. BigQuery analyzes over 110
terabytes of data per second. Users can leverage federated queries to
read data from Spanner and write to a native BigQuery table. \n",
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
store/branches/0/documents/8100ad36e1cac149eb9fc180a41d8f25",
                 "uri":
"https://cloud.google.com/blog/products/gcp/from-nosql-to-new-sql-
how-spanner-became-a-global-mission-critical-database",
                 "title": "How Spanner became a global, mission-
critical database | Google Cloud Blog",
                 "snippetInfo": [
                   {
                     "snippet": "... SQL
\u003cb\u003evs\u003c/b\u003e. NoSQL dichotomy may no longer be
relevant." The \u003cb\u003eSpanner\u003c/b\u003e SQL query
processor, while recognizable as a standard implementation, has
unique ...",
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
 "session": {
   "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943",
   "state": "IN_PROGRESS",
   "userPseudoId": "test_user",
   "turns": [
     {
       "query": {
         "queryId":
"projects/123456/locations/global/questions/741830",
         "text": "Compare bigquery with spanner database?"
       },
       "answer":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943/answers/4861507376861383072"
     }
   ],
   "startTime": "2024-09-13T18:47:10.465311Z",
   "endTime": "2024-09-13T18:47:10.465311Z"
 },
 "answerQueryToken":
"NMwKDAjFkpK3BhDU24uZAhIkNjZlNDIyZWYtMDAwMC0yMjVmLWIxMmQtZjQwMzA0M2Fk
YmNj"
}
```

4. Repeat step 3 for each new query in the session. 

#### Get a session from the data store

The following command shows how to call the `get` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/get) method and get a session from the data store. 

RESTPython (#python) (#rest) 

To get a session from a data store, do the following: 

1. Run the following curl command: 

```
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/sessions/
SESSION_ID"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. _`APP_ID`_ : the ID of the app. 

_`SESSION_ID`_ : the ID of the session that you want to get. 

#### Delete a session from the app

The following command shows how to call the `delete` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/delet e) 

method and delete a session from the data store. 

By default, sessions older than 60 days are automatically deleted. However, if you want to delete a particular session—for example, if it contains sensitive content, then use this API call to delete it. 

RESTPython (#python) (#rest) 

To delete a session from an app, do the following: 

1. Run the following curl command: 

```
curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/sessions/
SESSION_ID"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app. 

_`SESSION_ID`_ : the ID of the session that you want to delete. 

<sup>Example command and result</sup> 

```
curl -X DELETE -H "Authorization: Bearer $(gcloud auth print-access-
token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/
global/collections/default_collection/engines/my-
app/sessions/16002628354770206943"
{}
```

#### Update a session

There are various reasons that you might want to update a session. For example, to do one of the following: 

- Mark a session as completed 

Merge the messages from one session into another 

- Change a user's pseudo ID 

The following command shows how to call the `patch` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/patc h) 

method and update a session in the data store. 

RESTPython (#python) (#rest) 

To update a session from an app, do the following: 

1. Run the following curl command: 

```
curl -X PATCH \
 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
```

- `-H "Content-Type: application/json" \` 

```
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/sessions/
SESSION_ID?updateMask=state" \
 -d '{
       "state": "NEW_STATE"
     }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app. 

- _`SESSION_ID`_ : the ID of the session that you want to update. 

- _`NEW_STATE`_ : the new value for the state—for example, `IN_PROGRESS` . 

<sup>Example command and result</sup> 

```
curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-
token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/
global/collections/default_collection/engines/my-
app/sessions/16002628354770206943?updateMask=state"
-d '{
"state": "IN_PROGRESS"
}'
{
 "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943",
 "state": "IN_PROGRESS",
 "userPseudoId": "test_user",
 "turns": [
   {
     "query": {
       "queryId":
"projects/123456/locations/global/questions/741830",
       "text": "Compare bigquery with spanner database?"
     },
     "answer":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943/answers/4861507376861383072"
   }
 ],
 "startTime": "2024-09-13T18:47:10.465311Z",
 "endTime": "2024-09-13T18:49:41.579151Z"
}
```

This example changes the state of the session to open (in progress). Follow a similar pattern to update the `userPseudoId` . 

#### List all sessions

The following command shows how to call the `list` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/list) method and list the sessions in the data store. 

RESTPython (#python) (#rest) 

To list the sessions for an app, do the following: 

1. Run the following curl command: 

```
curl -X GET \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json" \` 

```
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/sessions"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. _`APP_ID`_ : the ID of the app. 

<sup>Example command and result</sup> 

```
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-
token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/
global/collections/default_collection/engines/my-app/sessions"
{
 "sessions": [
   {
     "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/10000135306311111817",
     "state": "IN_PROGRESS",
     "turns": [
       {
         "query": {
           "queryId":
"projects/123456/locations/global/questions/10000135306311114276",
           "text": "bugs reported by tiktok on grounding"
         }
       }
     ],
     "startTime": "2024-09-03T00:38:40.338623Z",
     "endTime": "2024-09-03T00:38:40.338623Z"
   },
   {
     "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/10000827040519035859",
     "state": "IN_PROGRESS",
     "turns": [
       {
         "query": {
           "queryId":
"projects/123456/locations/global/questions/10000827040519033518",
           "text": "GDM models"
         }
       }
     ],
     "startTime": "2024-07-19T15:53:06.521775Z"
   },
   {
     "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/10003910515245149877",
     "state": "IN_PROGRESS",
     "turns": [
       {
         "query": {
           "queryId":
"projects/123456/locations/global/questions/10003910515245148378",
           "text": "gyorgyattila"
         },
         "answer":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-
app/sessions/10003910515245149877/answers/17036357111873257990"
       }
     ],
     "startTime": "2024-08-08T11:40:04.632463Z",
     "endTime": "2024-08-08T11:40:04.632463Z"
   },
...
   {
     "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/10198752942940073431",
     "state": "IN_PROGRESS",
     "turns": [
       {
         "query": {
           "queryId":
"projects/123456/locations/global/questions/10198752942940071818",
           "text": "hello"
         },
         "answer":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-
app/sessions/10198752942940073431/answers/13411441797796265380"
       }
     ],
     "startTime": "2024-08-14T17:30:21.203439Z",
     "endTime": "2024-08-14T17:30:21.203439Z"
   }
 ],
 "nextPageToken": "IDEDgIwL_vuieLC"
}
```

The response contains a list of sessions and the nextPageToken. If no nextPageToken is returned, there are no more sessions to list. Default page size is 50. 

#### List sessions for a user

The following command shows how to call the `list` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/list) method to list sessions associated with a user or visitor. 

RESTPython (#python) (#rest) 

To list sessions associated with a user or visitor, do the following: 

1. Run the following curl command: 

```
curl -X GET \
 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
```

- `-H "Content-Type: application/json" \` 

```
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/sessions?
filter=userPseudoId=USER_PSEUDO_ID"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

_`APP_ID`_ : the ID of the app. 

- _`USER_PSEUDO_ID`_ : the pseudo ID of the user whose sessions you want to list. 

<sup>Example command and result</sup> 

```
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-
token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/
global/collections/default_collection/engines/my-app/sessions?
filter=userPseudoId=test_user"
{
 "sessions": [
   {
     "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943",
     "state": "IN_PROGRESS",
     "userPseudoId": "test_user",
     "turns": [
       {
         "query": {
           "queryId":
"projects/123456/locations/global/questions/741830",
           "text": "Compare bigquery with spanner database?"
         },
         "answer":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943/answers/4861507376861383072"
       }
     ],
     "startTime": "2024-09-13T18:47:10.465311Z",
     "endTime": "2024-09-13T18:49:41.579151Z"
   }
 ]
}
```

In this example, there is one session associated with the test_user. The queries and answers in the session are listed. 

#### List sessions for a user and state

The following command shows how to call the `list` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.sessions/list) method to list sessions in a given state for a particular user. 

RESTPython (#python) (#rest) 

To list sessions for a user that are open or closed and associated with a given user or visitor, do the following: 

1. Run the following curl command: 

```
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/sessions?
filter=userPseudoId=USER_PSEUDO_ID%20AND%20state=STATE"
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app. 

- _`USER_PSEUDO_ID`_ : the pseudo ID of the user whose sessions you want to list. 

- _`STATE`_ : the state of the session: `STATE_UNSPECIFIED` (closed or unknown) or `IN_PROGRESS` (open). 

<sup>Example command and result</sup> 

```
curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-
token)"
-H "Content-Type: application/json"
"https://discoveryengine.googleapis.com/v1/projects/123456/locations/
global/collections/default_collection/engines/my-app/sessions?
filter=userPseudoId=test_user%20AND%20state=IN_PROGRESS"
{
 "sessions": [
   {
     "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943",
     "state": "IN_PROGRESS",
     "userPseudoId": "test_user",
     "turns": [
       {
         "query": {
           "queryId":
"projects/123456/locations/global/questions/741830",
           "text": "Compare bigquery with spanner database?"
         },
         "answer":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/sessions/16002628354770206943/answers/4861507376861383072"
       }
     ],
     "startTime": "2024-09-13T18:47:10.465311Z",
     "endTime": "2024-09-13T18:49:41.579151Z"
   }
 ]
}
```

The expected result is an empty response. 

Last updated 2026-10-16 UTC.
