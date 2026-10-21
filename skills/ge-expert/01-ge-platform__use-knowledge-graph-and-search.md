# Gemini Enterprise: platform, security, agents, cost, monitoring / Use Knowledge Graph and search to Record real-time user events
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 364-400, extracted 2026-10-18

Contains:
- Use Knowledge Graph and search (pages 364-382) https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search
- About user events (pages 383-387) https://docs.cloud.google.com/gemini/enterprise/docs/user-events
- Import historical user events (pages 388-394) https://docs.cloud.google.com/gemini/enterprise/docs/import-user-events
- Record real-time user events (pages 395-400) https://docs.cloud.google.com/gemini/enterprise/docs/record-user-events

## Use Knowledge Graph and search

URL: https://docs.cloud.google.com/gemini/enterprise/docs/use-knowledge-graph-search

Knowledge Graph enhances Gemini Enterprise by linking data across three core pillars: **people** , **content** , and **interactions** . Knowledge Graph improves search quality and experience by understanding the relationship between different instances and entities in your corpus, providing deeper, context-aware search. 

Knowledge Graph enhances search capabilities by: 

- Enriching people-related data with organizational context, including derived reporting lines and relationships to other entities. 

- Improving entity recognition, relationships, and intent understanding to discover more insights from user queries. 

- Improving search responses with precise, context-driven data, making it easier for users to locate relevant people and organizational information. 

### Supported data sources for Knowledge Graph

Knowledge Graph is available for apps that have the following data sources: 

- People data sources (/gemini/enterprise/docs/connectors/connect-people) 

- People using custom connector 

- (/gemini/enterprise/docs/connectors/connect-people-custom) 

- Microsoft Entra ID (/gemini/enterprise/docs/connectors/entra-id/connect-entra-id) 

- Jira Cloud (/gemini/enterprise/docs/connectors/jira-cloud) 

- Jira Data Center (/gemini/enterprise/docs/connectors/jira-dc) 

- SharePoint Cloud (/gemini/enterprise/docs/connectors/ms-sharepoint) 

### Before you begin

To use Knowledge Graph features, you **must** first connect people data to the Knowledge Graph by configuring a People connector 

(/gemini/enterprise/docs/connectors/connect-people). Without connecting people data, these features don't function properly. 

People data powers key Knowledge Graph capabilities, including the following: 

- Entity resolution 

- Context understanding 

- Personalization 

- Autocomplete 

- Recommendations 

#### Supported sources for people data

Each app can have only one people connector. However, you can set up different people connectors for different apps. Choose a data source based on your identity system: 

- If your organization uses Google Cloud Identity, use the Advanced Google Identity connector (/gemini/enterprise/docs/connectors/connect-people). 

- If you are using the Workforce Identity Federation 

- (/iam/docs/workforce-identity-federation), select the corresponding third-party sources or native sources. 

Gemini Enterprise supports the following options for ingesting people's data into the Knowledge Graph: 

- Workspace sources 

The Advanced Google Identity connector syncs people data from Google Workspace, directly copying into the Gemini Enterprise index. By copying data into the index, this connector enables full Knowledge Graph functionality, including natural language processing (NLP). The Advanced Google Identity connector (/gemini/enterprise/docs/connectors/connect-people) is _cloud-native_ and behaves similarly to the Advanced Drive connector by persisting data in the index. 

When the connector is active, you must: 

   1. Unlink the existing **People Search** data store if it is in use. 

   2. Add the new data store to your engine. 

- Native sources 

Custom people connector lets you to upload people data from BigQuery or Cloud Storage using a Google-specified schema. This is ideal for organizations with custom or hybrid identity sources. 

Third-party sources 

Gemini Enterprise supports third-party identity providers to ingest people data. For more information see Workforce Identity Federation for third-party identity providers 

(/gemini/enterprise/docs/configure-identity-provider#workforce-id-fed-for-third-partyidps) 

### About query annotation with Knowledge Graph

Query annotation with Knowledge Graph enhances search query understanding by associating structured data with search terms. This process improves the accuracy and relevance of search results by leveraging contextual insights from the Knowledge Graph. 

Unlike standalone information panels, query annotation functions independently by enriching search queries with metadata, allowing for more precise entity detection, entity linking, and user context understanding. When you enter a search term, the Knowledge Graph helps categorize and interpret the query based on its relationship to people, organizations, issues, or other entities. 

The key components of query annotation include: 

- **Mention detection** : Identifies key entities (for example, people) and relationships (for example, manager) in a search query and associates them with structured data. 

- **User context understanding** : Analyzes the context of the user and retrieves related user signals (for example, top coworkers) to refine search relevance. 

- **Entity linking** : Resolves ambiguities by linking terms to their most relevant entities (for example, distinguishing between "Apple" as a company versus a fruit). 

### Knowledge Graph panels

After the knowledge graph is enabled, the search engine integrates the enriched panels into search results, delivering more precise, context-driven information to help users quickly find relevant people, roles, and organizations. When you perform a search, the `search` API responds with detailed panels that provide additional context and insights related to the search query. 

The following panel types appear on the search results page, enhancing your ability to identify relevant entities. 

- **People panel** : This panel includes information such as the person's job title, department, and relationships to other people (for example, management chain, direct reports, and teammates). It helps you to quickly find relevant people and their roles within the organization. The People panel is enhanced with Knowledge Graph and people are displayed as long-form cards, providing a comprehensive view of the person's role and relationships within the organization. The Knowledge Graph search API response includes enriched data panels in a unified, one-box search format. The People panel contains job title, department, and related people information (such as management chain, direct reports, or teammates with the same managers). The Knowledge Graph-derived fields are returned in `derived_struct_data` within the People panel result. 

- **Organization panel** : This panel provides key details about the organization, such as its name, description, and website information. The Knowledge Graph search API response includes enriched data panels in a unified, one-box search format. The Organization panel displays organization name, description, and website information.The Organization results are returned in the `knowledge_graph_results` field within the Organization panel result. 

**Note:** Security is maintained by applying access control lists (ACL) checks to ensure users see only authorized Knowledge Graph entities. 

### Knowledge Graph configurations

Knowledge Graph enhances search results by integrating enriched panels with precise, context-driven information from internal and external data sources. 

#### Types of Knowledge Graphs

There are two types of Knowledge Graphs: 

- **Google Cloud Knowledge Graph** : Expands search results by incorporating external data sources. This broadens the scope of search results and enhances relevance with additional insights. Google Cloud Knowledge Graph is only available on apps set to the **Global** location. 

- **Private Knowledge Graph** : Leverages internal organizational data to generate enriched search results. It improves relevance by incorporating proprietary knowledge, such as relationships, roles, and job titles, and provides more contextually accurate query annotations. 

#### Change Knowledge Graph configurations

Knowledge Graph configurations are enabled for all Gemini Enterprise apps. Before making changes, you can see the impact on search results as follows: 

|Configuration|Enabled|Disabled|
|---|---|---|
|Google Cloud Knowledge<br>Graph|Expands search with external<br>data.|Limits search to internal data.|
|Private Knowledge Graph|Enhances search with internal|Removes internal derived|
||data.|data.|

To modify Knowledge Graph configurations, see the Manage Knowledge Graph configuration (#manage-kg-config) section. 

#### Private Knowledge Graph structure and mapping

The private Knowledge Graph uses a property graph data model. It is designed for enterprise use cases and supports specific types of entities and relationships. You can retrieve the data from documents imported through supported connectors. The private Knowledge Graph uses internal rules to: 

1. Map data from the original data store schema to entity properties. 

2. Create relationships between entities by linking identifiers. 

The Knowledge Graph engine constructs its graph by applying these internal rules to all documents from the supported connectors. 

Knowledge Graph entity types and relationships 

|Knowledge Graph entity<br>types|Knowledge Graph relationship<br>types|Connectors supported|
|---|---|---|
|Person|Manager|Workspace sources → People|
|||search|
||Dotted-line report|People using custom connector|

Mapping from data source schema to entity properties 

|Source document field|Notes|
|---|---|
|`name.familyName`,`name.givenName`,|A concatenation of`givenName`and`familyName`. If|
|`name.displayName`|empty, use`displayName`.|
|`personId`|Used to uniquely identify a person.|
|`employeeId`|-|
|`employmentStatus`|-|

|`organizations[0].jobTitle`|The job title in the first element of organizations<br>(array).|
|---|---|
|`websites[0].value`|The first value of the websites (array).|
|`topCoworkers`|-|

### Lifecycle of the Knowledge Graph

The Knowledge Graph for your engine goes through several states as it is enabled, updated, and managed. Understanding the following states helps you know what to expect and what actions are available to you. 

```
unspecified
```

The Knowledge Graph is not enabled for the engine or is pending initialization. To enable it, you must configure the `knowledge_graph_config.enable_private_knowledge_graph` setting to `true` . 

```
initialization
```

The initial Knowledge Graph construction is running. During this state, the Knowledge Graph is not available for processing. 

While in the `initialization` state: 

- You cannot enable or disable the Knowledge Graph. 

- You cannot delete the engine. 

- Changes from linking or unlinking Knowledge Graph-supported data stores are not immediately reflected in the graph. For more information, see the supported data sources for Knowledge Graph (#supported-ds-kg). 

`active` 

The Knowledge Graph is reliable and actively serving. This is the selected state for a functional Knowledge Graph. 

- `batch_update` 

The Knowledge Graph is updating to incorporate recent changes from its source data. A change in the supported data source for the Knowledge Graph, 

or a periodic synchronization between the Knowledge Graph and its supported data source, triggers this action. The Knowledge Graph remains active, but it is potentially out of sync with the changed source data because the updates are still in progress. 

While in the `batch_update` state: 

   - You cannot enable or disable the Knowledge Graph. 

   - You cannot delete the engine. 

   - Changes from linking or unlinking Knowledge Graph-supported data stores are subject to delayed reflection in the graph. For more information, see the supported data sources for Knowledge Graph (#supported-ds-kg). 

- `deleting` 

The Knowledge Graph is disabled for the engine and is being deleted. The Knowledge Graph is not available for processing. 

While in the `deleting` state: 

- You cannot enable or disable the Knowledge Graph. 

- You cannot delete the engine. 

**Note:** The current Knowledge Graph state does not reflect the availability or quality of your data. For example, a Knowledge Graph can be in the **`active`** state even if it is empty because it lacks supported data sources. 

### Manage Knowledge Graph configuration

You can manage configurations using the console or API. 

Before you begin: 

1. You must have created a Gemini Enterprise app. 

2. Review Changing Knowledge Graph configurations (#change-kg-config) to see the impact of changing configurations on existing apps. 

Use the following procedure to update Knowledge Graph configurations in the console: 

ConsoleAPI  (#api) (#console) 

To use the Google Cloud console to manage Knowledge Graph configurations, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. On the **Apps** page, click the app whose Knowledge Graph configurations you want to update. 

3. Navigate to **Configurations** > **Knowledge Graph** tab. 

4. Toggle **Google Cloud Knowledge Graph** or **Private Knowledge Graph** based on your needs. 

5. Click the **Save** button after confirming any prompts or warnings. 

The effects of enabling and disabling Knowledge Graph are as follows: 

1. **Google Cloud Knowledge Graph** : 

   - Enabling the Google Cloud Knowledge Graph grants access to enriched data from external sources, broadening search context. 

   - Disabling it limits search results to internal data, removing access to external context. 

2. **Private Knowledge Graph** : 

   - Enabling the private Knowledge Graph regenerates internal derived data, and query annotations return after up to a day. 

   - Disabling it deletes internal derived data and removes query annotations, reducing search accuracy and richness. 

#### View knowledge panels in search results

You can view how the Knowledge Graph-enriched search results are displayed in your search application. For panel-based search interfaces, the Knowledge Graph panel appears as an enriched information box alongside regular search results. It integrates relevant entity details, such as names, descriptions, images, and relationships, providing a more informative and contextually relevant search experience. These boosted results help you quickly find key insights related to your query. 

The following JSON example shows how a People panel appears in an API response: 

```
     one_box_results: [
       {
         one_box_type: PEOPLE
         search_results: [
           {
             document: {
               name: "projects/<pii
data>/locations/global/collections/default_collection/dataStores/people-v17-df-
sprint_1731449540556/branches/0/documents/<name>"
               derived_struct_data: {
                 fields: [
                   {
                     key: "management_chain"
                     value: {
                       list_value: {
                         values: [
                           {
                             struct_value: {
                               fields: [
                                 {
                                   key: "person_id"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 },
                                 {
                                   key: "job_title"
                                   value: {
                                     string_value: "Account Executive"
                                   }
                                 },
                                 {
                                   key: "name"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 }
                               ]
                             }
                           },
                           {
                             struct_value: {
                               fields: [
                                 {
                                   key: "name"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 },
                                 {
                                   key: "job_title"
                                   value: {
                                     string_value: "Account Executive"
                                   }
                                 },
                                 {
                                   key: "person_id"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 }
                               ]
                             }
                           }
                         ]
                       }
                     }
                   },
                   {
                     key: "teammates_with_same_manager"
                     value: {
                       list_value: {
                         values: [
                           {
                             struct_value: {
                               fields: [
                                 {
                                   key: "person_id"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 },
                                 {
                                   key: "job_title"
                                   value: {
                                     string_value: "Account Executive"
                                   }
                                 },
                                 {
                                   key: "name"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 }
                               ]
                             }
                           }
                         ]
                       }
                     }
                   },
                   {
                     key: "direct_reports"
                     value: {
                       list_value: {
                         values: [
                           {
                             struct_value: {
                               fields: [
                                 {
                                   key: "job_title"
                                   value: {
                                     string_value: "Account Strategist, Lead
Generation"
                                   }
                                 },
                                 {
                                   key: "name"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 },
                                 {
                                   key: "person_id"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 }
                               ]
                             }
                           },
                           {
                             struct_value: {
                               fields: [
                                 {
                                   key: "person_id"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 },
                                 {
                                   key: "name"
                                   value: {
                                     string_value: "<persons name>"
                                   }
                                 },
                                 {
                                   key: "job_title"
                                   value: {
                                     string_value: "Account Strategist, Mid-
Market Sales, Google Customer Solutions"
                                   }
                                 }
                               ]
                             }
                           }
                         ]
                       }
                     }
                   }
                 ]
               }
             }
           }
         ]
       }
     ]
```

The following JSON example shows how an Organization panel appears in an API response: 

```
     {
       one_box_type: ORGANIZATION
       knowledge_graph_results: [
         {
           knowledge_graph_source_type: CLOUD_KG
           context: {
             struct_value: {
               fields: [
                 {
                   key: "@vocab"
                   value: {
                     string_value: "http://schema.org/"
                   }
                 }
               ]
             }
           }
           type: {
             string_value: "ItemList"
           }
           item_list_element: {
             values: [
               {
                 struct_value: {
                   fields: [
                     {
                       key: "result"
                       value: {
                         struct_value: {
                           fields: [
                             {
                               key: "@id"
                               value: {
                                 string_value: "c-025prnpgp"
                               }
                             },
                             {
                               key: "identifier"
                               value: {
                                 list_value: {
                                   values: [
                                     {
                                       struct_value: {
                                         fields: [
                                           {
                                             key: "name"
                                             value: {
                                               string_value: "googleKgMID"
                                             }
                                           },
                                           {
                                             key: "value"
                                             value: {
                                               string_value: "/m/0k8z"
                                             }
                                           },
                                           {
                                             key: "@type"
                                             value: {
                                               string_value: "PropertyValue"
                                             }
                                           }
                                         ]
                                       }
                                     },
                                     {
                                       struct_value: {
                                         fields: [
                                           {
                                             key: "value"
                                             value: {
                                               string_value: "Q312"
                                             }
                                           },
                                           {
                                             key: "@type"
                                             value: {
                                               string_value: "PropertyValue"
                                             }
                                           },
                                           {
                                             key: "name"
                                             value: {
                                               string_value: "wikidataQID"
                                             }
                                           }
                                         ]
                                       }
                                     }
                                   ]
                                 }
                               }
                             },
                             {
                               key: "@type"
                               value: {
                                 list_value: {
                                   values: [
                                     {
                                       string_value: "Corporation"
                                     },
                                     {
                                       string_value: "Thing"
                                     },
                                     {
                                       string_value: "Organization"
                                     }
                                   ]
                                 }
                               }
                             },
                             {
                               key: "name"
                               value: {
                                 string_value: "Apple"
                               }
                             },
                             {
                               key: "detailedDescription"
                               value: {
                                 struct_value: {
                                   fields: [
                                     {
                                       key: "url"
                                       value: {
                                         string_value:
"https://en.wikipedia.org/wiki/Apple_Inc."
                                       }
                                     },
                                     {
                                       key: "articleBody"
                                       value: {
                                         string_value: "Apple Inc. is an
American multinational corporation and technology company headquartered and
incorporated in Cupertino, California, in Silicon Valley. It is best known for
its consumer electronics, software, and services. "
                                       }
                                     },
                                     {
                                       key: "license"
                                       value: {
                                         string_value:
"https://en.wikipedia.org/wiki/Wikipedia:Text_of_Creative_Commons_Attribution-
ShareAlike_3.0_Unported_License"
                                       }
                                     }
                                   ]
                                 }
                               }
                             },
                             {
                               key: "description"
                               value: {
                                 string_value: "Technology company"
                               }
                             },
                             {
                               key: "image"
                               value: {
                                 struct_value: {
                                   fields: [
                                     {
                                       key: "contentUrl"
                                       value: {
                                         string_value: "https://encrypted-
tbn1.gstatic.com/images?
q=tbn:ANd9GcTMHrvLPmr_8yVjoTYsyxhRGtPMcA90bcJl9_RehtJU0tr64KNR"
                                       }
                                     },
                                     {
                                       key: "url"
                                       value: {
                                         string_value:
"https://commons.wikimedia.org/wiki/File:Apple_logo_black.svg"
                                       }
                                     }
                                   ]
                                 }
                               }
                             },
                             {
                               key: "url"
                               value: {
                                 string_value: "http://www.apple.com/"
                               }
                             }
                           ]
                         }
                       }
                     }
                   ]
                 }
               }
             ]
           }
         }
       ]
     }
```

Last updated 2026-10-14 UTC. 



## About user events

URL: https://docs.cloud.google.com/gemini/enterprise/docs/user-events

This page describes user events for Gemini Enterprise apps, including user event types, requirements, and examples for user event types. 

If you use the Gemini Enterprise APIs in your own apps, you need to configure search in your app to get the user events and then add the user events data to your Gemini Enterprise app. 

If you create your app through the Google Cloud console (/gemini/enterprise/docs/create-app), then you don't need to manually import user events (and you don't need to read this page). 

For help with recording user events, see Record real-time user events (/gemini/enterprise/docs/record-user-events). To import past user events in bulk, see Import historical user events (/gemini/enterprise/docs/import-user-events). 

### User event types

You can record the following types of user events as end users browse or search your site: 

|User event name|User action|
|---|---|
|`view-item` (#view-item)|Views details of a document.|
|`search` (#search)|Searches data in the Gemini Enterprise app.|

For details about the user event object, see the [ `UserEvent` API reference documentation][user-event]. 

### User event type examples and schemas

This section provides the data formats for each event type supported by Gemini Enterprise apps. Examples for JavaScript Pixel are provided. For BigQuery, the full table schema for each type is provided. 

For all user events types, `userId` is optional. 

For more details about the user event object, see the [ `UserEvent` API reference documentation][user-event]. 

#### view-item

The following shows the `view-item` user event data format. 

Search optimization requirements for view-item events 

To let search automatically optimize the search experience based on overall user trends, upload the following data. 

Events should be uploaded at least daily with a maximum delay of 24 hours. 

|Events metric|Events<br>volume/frequency|Description|
|---|---|---|
|Volume of`view-item`|250k view items|At least 250,000 view items are required to optimize the search experience based|
|events||on events ingested.|

Minimum required view-item object 

The following examples show only the required fields of the `view-item` user event format. 

The `documents` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo) object contains the document's ID ( `id` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its resource name ( `name` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)). 

- When you ingest or record user events at a data-store level, you can provide the document's ID ( `id` ) or resource name ( `name` ) . 

- When you ingest or record events at a location level, you must supply the document's resource name ( `name` ) because it indicates a document's full path and refers to the data store where the document resides. You can provide the document's ID as an optional, additional information. 

JavaScript PixelBigQuery  (#bigquery) (#javascript-pixel) 

```
var user_event = {
 "eventType": "view-item",
 "userPseudoId": "USER_PSEUDO_ID",
 "engine": "APP_ID",
 "eventTime": "2020-01-01T03:33:33.000001Z",
 "documents": [{
   "name": "DOCUMENT_NAME"
 }]
};
```

<sup>Complete view-item object example</sup> 

The following examples include both required and optional fields for the `view-item` user event. 

JavaScript PixelBigQuery  (#bigquery) (#javascript-pixel) 

```
var user_event = {
 eventType: "view-item",
 userPseudoId: "visitor0",
 "engine": "APP_ID",
 eventTime: "2020-01-01T03:33:33.000001Z",
 userInfo: {
   userId: "abc@example.com",
   userAgent: "Mozilla/5.0",
 },
 pageInfo: {
   pageViewId: "currentPageUri",
   uri: "http://example",
   referrerUri: "https://google",
 },
 attributionToken: "abcd",
 documents: [
   {
     id: "abcd",
   },
 ],
 tagIds: ["Treatment_B"],
 attributes: {
   example_text_attribute: {
     text: ["text_1", "text_2"],
   },
   example_number_attribute: {
     numbers: [3.14, 42, 1.2345],
   },
 },
 panels: [
        {
          panelId: "HOME_RFY_1",
          documents: [
            {
              id: "123"
            },
            {
              id: "456"
            }
          ],
          panelPosition: 1,
          totalPanels: 2
        }
     ]
};
```

#### search

The following shows the `search` user event format. 

Search optimization requirements for search events 

To let search automatically optimize the search experience based on overall user trends, upload the following data. 

Events should be uploaded at least daily with a maximum delay of 24 hours. 

|Events metric|Events<br>volume/frequency|Description|
|---|---|---|
|Volume of`search`|100k searches|At least 100,000 searches are required to optimize the search experience based on|
|events||events ingested.|

Minimum required search object 

The following examples show only the required fields of the `search` user event format. 

Provide `searchQuery` for search events where the user entered a text query. 

The `attributionToken` is returned with the search query results. 

The `documents` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo) object contains the document's ID ( `id` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.id)) and its 

resource name ( `name` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#DocumentInfo.FIELDS.name)). 

- When you ingest or record user events at a data-store level, you can provide the document's ID ( `id` ) or resource name ( `name` ) . 

- When you ingest or record events at a location level, you must supply the document's resource name ( `name` ) because it indicates a document's full path and refers to the data store where the document resides. You can provide the document's ID as an optional, additional information. 

JavaScript PixelBigQuery  (#bigquery) (#javascript-pixel) 

```
var user_event = {
 "eventType": "search",
 "userPseudoId": "USER_PSEUDO_ID",
 "engine": "APP_ID",
 "eventTime": "2020-01-01T03:33:33.000001Z",
 "searchInfo": {
   "searchQuery": "SEARCH_QUERY",
 },
 "attributionToken": "ATTRIBUTION_TOKEN",
 "documents": [
   {
     "name": "DOCUMENT_NAME_1",
   },
   {
     "name": "DOCUMENT_NAME_2",
   },
 ]
};
```

### About user information

`userPseudoId` represents the unique user identifier and is required when you record a user event. 

The user information ([ `UserInfo` ][user-info]) included when you record a user event contains the `userPseudoId` value and, if available, the `userId` value. `userId` is optional and can be used as a unique, persistent identifier for a user across devices whenever a user logs in to your site. When you record the `userId` for a user, Gemini Enterprise apps can generate more personalized results for one user across multiple devices, such as both a mobile device and a web browser. 

**Note:** Use a secure form of a unique identifier to keep users anonymous to Gemini Enterprise and protect your users' privacy. You are responsible for redacting PII (personally identifiable information), such as email or home addresses, from your data. 

### About the timestamp

When you record a user event, be sure to include an accurate timestamp of when the event occurred. Accurate timestamps make sure that your events are stored in the correct order. Timestamps are recorded automatically 

for events collected using the JavaScript Pixel. When you import events, you must provide the timestamp in the [ `eventTime` ][event-time] field in the format specified by RFC 3339 (https://tools.ietf.org/html/rfc3339). 

[rec-type-reqs]: /gemini/enterprise/docs/about-media-recommendations-types [record-events]: /gemini/enterprise/docs/record-user-events [event-time]: 

/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.event_time [user-event]: /gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents [user-info]: /gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#userinfo 

Last updated 2026-10-14 UTC. 



## Import historical user events

URL: https://docs.cloud.google.com/gemini/enterprise/docs/import-user-events

This page describes how to import user event data from past events in bulk. 

For the user event types that you can import, see the `eventType` field of the `userEvents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents) object. By importing user events, you can improve the quality of your results. For example, user events affect the ranking of search results. Results with higher click-through rates are boosted, while results with lower click-through rates are buried. Only import user events for documents that you are already imported into your data store. 

If an event has documents listed in `userEvents.Documents` , then Gemini Enterprise automatically joins the events with that document. Joining allows Gemini Enterprise to attribute events such as clicks and views to the correct document in a search result or recommendation. For custom search and recommendations apps, joining occurs _asynchronously_ , that is, user events are joined to documents after the batch import is complete (generally happening within minutes). 

If you are using a search app with multiple data stores attached, import user events at the location level instead of the data-store level. This allows a given user event to be sent to the data store that it's associated with. When importing user events at a location level, include the `engine` field in the user event to associate the event with the correct app. For examples of user events that include the `engine` field, see the following: 

Custom apps user event type examples and schemas 

(/gemini/enterprise/docs/user-events#formats) 

For more information on the import method, see `userEvents.import` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import). 

To import user events in real-time, see Record real-time user events (/gemini/enterprise/docs/record-user-events). 

You can import historical events in the following ways: 

From Cloud Storage (#import-user-events-from-cloud-storage) 

From BigQuery (#import-user-events-from-big-query) 

As local JSON data (#import-user-events-inline) 

For the JSON representation for user events, see `userEvents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents) in the API reference. 

### Before you begin

Before you import user events: 

- Create a data store and an app. 

- Review About user events (/gemini/enterprise/docs/user-events) for user event requirements. 

### Import historical user events from Cloud Storage

REST 

(#rest) 

To import historical user events in bulk from Cloud Storage, follow these steps: 

1. Create one or more data files for the input parameters for the import. Use the `gcsSource` (/gemini/enterprise/docs/reference/rest/v1/GcsSource) object to point to your Cloud Storage bucket. 

```
{
"gcsSource": {
 "inputUris": ["INPUT_FILE_1", "INPUT_FILE_2"],
 "dataSchema": "user_event"
 },
 "errorConfig":{
     "gcsPrefix":"ERROR_DIRECTORY"
 }
}
```

Replace the following: 

_`INPUT_FILE`_ : a file in Cloud Storage containing your user event data. Make sure each user event is on its own single line, with no line breaks. For the JSON representation for user events, see `userEvents` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.use rEvents) 

in the API reference. The input file fields must be in this format: `gs://<bucket>/<path-to-file>/` . 

_`ERROR_DIRECTORY`_ : optional. A Cloud Storage directory for error information about the import—for example, `gs://<your-gcsbucket>/directory/import_errors` . Google recommends leaving this field empty to let Gemini Enterprise automatically create a temporary directory. 

2. Import your events by making a POST request to the `userEvents.import` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the data file. 

```
curl -X POST \
   -v \
   -H "Content-Type: application/json; charset=utf-8" \
   -H "Authorization: Bearer "$(gcloud auth print-access-token)"" \
   --data @DATA_FILE.json \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/lo
cations/global/userEvents:import"
```

### Import historical user events from BigQuery

When creating tables for user events in BigQuery, use the schemas documented in About user events for custom apps (/gemini/enterprise/docs/user-events#bigquery). Each `search` user event must include an `engine` field to associate the event with an app. For more information, see `engine` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEven t.FIELDS.engine) 

#### Set up BigQuery access

If your BigQuery dataset is in a different project than your data store, follow these steps to set up access to BigQuery. 

1. Open the IAM & Admin (https://console.cloud.google.com/iam-admin/iam) page in the Google Cloud console. 

2. Select the project that contains the data store that you want to import user events into. 

3. Select the **Include Google-provided role grants** checkbox. 

4. Find the service account with the name **Discovery Engine Service Account** . 

5. If you have not previously initiated an import operation with Discovery Engine, this service account might not be listed. If you don't see this service account, return to the import task and initiate the import. When it fails due to permission errors, return here and complete this task. The Discovery Engine service account will be listed. 

6. Copy the identifier for the service account, which looks like an email address —for example, `service-525@gcp-sa-discoveryengine.iam.gserviceaccount.com` . 

7. Switch to your BigQuery project (on the same **IAM & Admin** page) and click **Grant Access** . 

8. For **New principals** , enter the identifier for the service account and select the **BigQuery > BigQuery Data Viewer** role. 

9. Click **Save** . 

For more information about BigQuery access, see Controlling access to datasets (/bigquery/docs/dataset-access-controls) in the BigQuery documentation. 

#### Import events from BigQuery

REST 

(# t) 

To import historical user events in bulk from BigQuery, follow these steps: 

1. Import your user events by making a POST request to the `userEvents.import` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the BigQuery project, dataset ID, and table ID. 

When importing your events, use the value `user_event` for `dataSchema` . 

```
curl \
 -v \
 -X POST \
 -H "Content-Type: application/json; charset=utf-8" \
 -H "Authorization: Bearer "$(gcloud auth print-access-token)"" \
"https://discoveryengine.googleapis.com/v1/projects/[PROJECT_NUMBER]/
locations/global/userEvents:import" \
 --data '{
     "bigquerySource": {
         "projectId":"PROJECT_ID",
         "datasetId": "DATASET_ID",
         "tableId": "TABLE_ID",
         "dataSchema": "user_event"
     }
   }'
```

### Import historical user events as local JSON data

You can import user events by including local JSON data for the events in your call to the `userEvents.import` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import) method. 

To put user event data into a JSON file and specify the file in an API request, follow these instructions: 

1. Create a JSON file containing your user event data. For the JSON representation for user events, see `userEvents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents) in the API reference documentation. 

```
{
 "inlineSource": {
   "userEvents": [
     {
USER_EVENT_1
     },
     {
USER_EVENT_2
     }
   ]
 }
}
```

2. Import your events by making a POST request to the `userEvents.import` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the data file. 

```
curl -X POST \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json; charset=utf-8" \` 

- `--data @[JSON_FILE] \` 

```
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locatio
ns/global/userEvents:import"
```

Last updated 2026-10-14 UTC. 



## Record real-time user events

URL: https://docs.cloud.google.com/gemini/enterprise/docs/record-user-events

This page describes how to record user events in real time. 

For the user event types that you can record, see the `eventType` field of the 

`userEvents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource: -userevent) 

object. By ingesting user events, you can improve the quality of your results. For example, user events affect the ranking of search results. Results with higher clickthrough rates are boosted, while results with lower click-through rates are buried. Don't record user events for documents that you have not yet imported. 

If you are using an app with multiple data stores attached, ingest user events at the location level instead of the data-store level. This allows a given user event to be sent to the data store that it's associated with. When recording user events at a location level, you must include the `engine` field in the user events to associate the event with the correct app. For examples of user events that include the `engine` field, see the following: 

Custom apps user event type examples and schemas 

(/gemini/enterprise/docs/user-events#formats) 

To import historical user events in bulk, see Import historical user events (/gemini/enterprise/docs/import-user-events). 

You can record user events in the following ways: 

With a JavaScript pixel (#record-with-javascript-pixel). 

With the `userEvents.write` method (#record-with-userevents-write-method). 

For the JSON representation for user events, see `userEvents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource: -userevent) 

in the API reference. 

### Before you begin

Before you import user events: 

- Create a data store and an app. 

- Review About user events (/gemini/enterprise/docs/user-events) for user event requirements. 

### Record real-time user events with a JavaScript pixel

To record user events with a JavaScript pixel: 

1. Create an API key (#create-key) for calls to the `userEvents.collect` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/collect) method. 

2. See the JavaScript pixel example (#js-pixel-example) for an example of a JavaScript tag that collects user events. 

#### Create an API key

An API key is required if you use a JavaScript pixel to collect user events from users' browsers. 

To create an API key for calls to the `userEvents.collect` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/collect) method, complete the following steps: 

1. In the Google Cloud console, go to the **Credentials** page. 

Credentials (https://console.cloud.google.com/apis/credentials) 

2. In the project list at the top of the Google Cloud console page, select your project (the project might already be selected). 

3. Click **Create credentials** and then select **API key** . _Don't add any referrer restrictions_ . Some user privacy settings don't pass the referrer URL. 

   - Take note of the generated API key, which you will use when calling user event logging. 

4. For increased security, add an HTTP restriction (/docs/authentication/api-keys#api_key_restrictions) to your API Key to restrict access to the Gemini Enterprise service at 

`https://discoveryengine.googleapis.com/*` . 

**Note:** The API key is only for authenticating the **`userEvents.collect`** 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/collect) method and the **`servingConfigs.searchLite`** 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConf igs/searchLite) 

method. Other Gemini Enterprise methods require OAuth 2.0 through a service account or a user account. 

#### JavaScript pixel example

The following example records a `view-item` user event using a JavaScript pixel. 

For the JSON representation for user events, see `userEvents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#resource: -userevent) 

in the API reference. 

```
<script type="text/javascript">
var user_event = {
 "eventType" : "view-item",
 "userPseudoId": "USER_PSEUDO_ID",
 "engine":
"projects/PROJECT_ID/locations/LOCATION_ID/collections/default_collection/engin
es/APP_ID",
 "userInfo": {
     "userId": "USER_ID"
 },
 "attributionToken": "ATTRIBUTION_TOKEN",
 "tagIds": "TAG_ID",
 "documents": [
     {
       "id": "DOCUMENT_ID"
     }
 ]
};
var _gre = _gre || {};
// Credentials for project.
_gre.apiKey = '[API_KEY]';
_gre.logEvent = user_event;
_gre.projectId = 'PROJECT_ID';
_gre.locationId = 'LOCATION_ID';
_gre.dataStoreId = 'DATA_STORE_ID';
(function() {
 var gre = document.createElement('script'); gre.type = 'text/javascript';
gre.async = true;
 gre.src = 'https://www.gstatic.com/discoveryengine/v1beta_event.js';
 var s = document.getElementsByTagName('script')[0];
s.parentNode.insertBefore(gre, s);
})();
</script>
```

### Record real-time user events with the `userEvents.write` method

RESTC# (#c)Go (#go)Java (#java)Python (#python)Ruby (#ruby) (#rest) 

You can use the `userEvents.write` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write) method to send user events directly to the API from your backend server. 

To record user events, send a POST request to the `userEvents.write` method and provide the appropriate request body. For the JSON representation for user events, see `userEvents` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#re source:-userevent) in the API reference. 

If you are recording user events at the location level, use the endpoint `https://discoveryengine.googleapis.com/v1/projects/` _`PROJECT_NUMBER`_ `/locati` 

`ons/` _`LOCATION`_ `/userEvents:write` . 

```
curl -X POST \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json; charset=utf-8" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locatio
ns/global/userEvents:write" \
    -d '{
        "eventType": "view-item",
        "userPseudoId": "visitor0",
        "engine":
"projects/PROJECT_NUMBER/locations/global/collections/default_collection/e
ngines/APP_ID",
        "eventTime": "2020-01-01T03:33:33.000001Z",
        "tagIds": ["321"],
        "attributionToken": "ABC",
        "attributes": {
           "example_text_attribute": {
             "text": ["text_1", "text_2"]
           },
           "example_number_attribute": {
              "numbers": [3.14, 42, 1.2345]
           }
         },
        "documents": [{
           "id": "abc"
         }],
        "userInfo": {
          "userId": "abc",
          "userAgent": "Mozilla/5.0"
        },
        "pageInfo": {
         "uri": "http://example",
         "referrerUri": "http://example",
         "pageViewId": "currentPageUri"
        }
       }'
```

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC.
