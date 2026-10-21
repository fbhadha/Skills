# Gemini Enterprise: platform, security, agents, cost, monitoring / Advanced autocomplete to About custom preambles
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 612-653, extracted 2026-10-18

Contains:
- Advanced autocomplete (pages 612-626) https://docs.cloud.google.com/gemini/enterprise/docs/configure-advanced-autocomplete
- Configure the app home page (pages 627-631) https://docs.cloud.google.com/gemini/enterprise/docs/app-home-page
- Configure results for the UI (pages 632-636) https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-results
- Configure facets for the UI (pages 637-638) https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-facets
- Configure feedback (pages 639-640) https://docs.cloud.google.com/gemini/enterprise/docs/configure-feedback
- Configure the assistant (pages 641-644) https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant
- About custom preambles (pages 645-653) https://docs.cloud.google.com/gemini/enterprise/docs/preamble

## Advanced autocomplete

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-advanced-autocomplete

This page describes Gemini Enterprise's advanced autocomplete feature. 

In the same way as basic autocomplete, advanced autocomplete generates query suggestions based on the first few characters entered for the query. 

Before reading this page, become familiar with Gemini Enterprise's basic autocomplete. See Configure autocomplete 

(/gemini/enterprise/docs/configure-autocomplete). 

### Key features of advanced autocomplete

The key features of advanced autocomplete that distinguish it from the basic autocomplete are as follows: 

- **Blended search:** Advanced autocomplete can be used with apps that are connected to more than one data store. 

- **Access control:** Advanced autocomplete respects access controls. (Access controls are also referred to as ACLs, access control lists.) Advanced autocomplete only suggests search queries that are related to documents that the searcher has access to. For information about access control, see Identity and permissions (/gemini/enterprise/docs/identity). 

- **Language boost:** Advanced autocomplete can be set to boost suggestions in one or more languages. For example, if the browser language is Dutch, autocomplete suggestions in that language could be boosted. For more information, see Send an autocomplete request with a language boost (#language-boost). 

- **Different types of suggestions:** With advanced autocomplete, instead of regular autocomplete query suggestions, you can specify that you want different types of suggestions: 

   - **Rich suggestions:** As autocomplete suggestions, users get information about documents where the titles prefix-match the letters that they type. For more information, see Send an autocomplete request and return rich suggestions (#rich-autocomplete). 

- **Recent queries:** As autocomplete suggestions, users get their recent queries that prefix-match the letters that they type. For more information, see Send an autocomplete request and return recent queries (#recent-queries). 

### Before you begin

Before you begin to use advanced autocomplete, do the following: 

- Review and optionally edit the autocomplete settings for your app. See Update autocomplete settings 

- (/gemini/enterprise/docs/configure-autocomplete#update-autocomplete). 

- For smaller data stores, set **Enable autocomplete** to **Now** . We recommend this because small data stores might not contain sufficient data to provide accurate suggestions. 

- If your data stores contain any personally identifiable information (PII) or if you use the search history or user events query suggestions model, review Protect against PII leaks (/gemini/enterprise/docs/configure-autocomplete#pii) and set up data loss prevention (DLP) safeguards that might be needed to prevent leaks of PII. 

- If you plan to use recent search suggestions ( `RECENT_SEARCH` ), ensure that you record search user events. Gemini Enterprise doesn't automatically populate the recent search index when searches are performed using the `SearchService.Search` 

- (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.serving Configs/search) 

method. To return recent queries, you must record search user events by using the `userEvents.write` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write) method. See Before you begin for recent queries (#recent-queries-prerequisites). 

### Send autocomplete requests

The following shows how to send advanced autocomplete requests using the `completionConfig.completeQuery` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.completionCo nfig/completeQuery) 

method. 

REST 

(#rest) 

To send an autocomplete request using the API, follow these steps: 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

   - b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. Call the `completionConfig.completeQuery` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.c ompletionConfig/completeQuery) 

method. 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/completionCo
nfig:completeQuery" \
-d '{
     "query":"QUERY_STRING"
   }'
```

Replace the following: 

_`PROJECT_ID`_ : the ID of your project. 

_`APP_ID`_ : the ID of the app. 

### Send an autocomplete request with a language boost

You can boost or bury autocomplete suggestions according to language code, for example, make autocomplete suggestions in some languages more or less likely to appear. 

The boost value must be between -1 and 1. Setting a negative number "buries" autocomplete suggestions in that language and a positive number boosts the language. 

Use two-letter language tags defined by BCP 47—for example, `en` , `fr` , `hi` , and `zh` . 

REST 

(#rest) 

To send an autocomplete request that includes a language boost value, follow these steps: 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

   - b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. Call the `completionConfig.completeQuery` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.c ompletionConfig/completeQuery) 

method. 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/completionCo
nfig:completeQuery" \
-d '{
     "query":"QUERY_STRING",
     "boostSpec": {
        "conditionBoostSpecs": [{
          "condition": "(langCode: ANY(LANG_CODE))",
          "boost": BOOST_VALUE
        }]
     }
   }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app. 

- _`QUERY_STRING`_ : the typeahead input used to fetch suggestions. 

- _`LANG_CODE`_ : the two-letter code for one or more languages, in escaped quotes. For example, `\"fr\", \"es\"` to apply the boost value to Spanish and French. 

- _`BOOST_VALUE`_ : a floating point number between -1 and 1. When the value is negative, autosuggestions in the language are demoted (they appear lower down in the list of suggestions). When the value is positive, suggestions are promoted (they appear higher up in the list). 

<sup>Example command</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/completionConfig:completeQuery" \
-d '{
    "query": "hol",
    "boostSpec": {
       "conditionBoostSpecs": [{
         "condition": "(langCode: ANY(\"es\", \"fr\"))",
         "boost": 0.75 }, {
         "condition": "(langCode: ANY(\"en\"))",
         "boost": -1
       }]
     }
   }'
```

In this example, the autocomplete suggestions for the query `Co` are boosted (placed higher in the autosuggestion list) if they are in French or Spanish and buried (placed lower in the autosuggestion list) if they are in English. 

### Send an autocomplete request and return rich suggestions

Rich autocomplete returns content (documents) where the titles contain words that start with the query. 

In addition to the title for the document, the autocomplete request returns the `source_type` and `entity_type` , and, if available, the key properties: `uri` , `create_time` , and `update_time` . You can view and edit key property mappings on the **Schema** tab of the data store page. 

As with all advanced autocomplete suggestions, ACLs are respected for any suggested documents. 

#### Example

An employee is querying their company intranet site looking for technical information about access permissions. 

The employee begins typing `tec` , and the following documents might be returned: `Data technicians handbook` , `Access technology guide` , and `Techniques for troubleshooting access issues` . 

With rich suggestions, for each of these suggested documents, you can display the following information about the document: 

- the document title ( `title` ), a link to the document ( `uri` ) 

- when it was last updated ( `update_time` ) 

- the source ( `source_type` ), for example, whether the document was found in Confluence Cloud or Slack. 

Knowing how recently a document was updated and the source for the document helps the employee choose which document to look at first. 

#### Limitations

Rich autocomplete only applies to third-party connectors and only to certain entity data stores for those third-party connectors. The following table shows which entities are supported for which connectors. 

|Third-party connector|Entities suppor|ted|||
|---|---|---|---|---|
|Box|File||||
|Confluence Cloud|Page|Space|||
|Dropbox|File||||
|Jira Cloud|Issue|Space|||
|OneDrive|File||||
|Salesforce|Account|Lead|Opportunity||
|ServiceNow|Incident|Knowledge|||
|Sharepoint Online|Attachment|Event|File|Page|
|Slack|Message||||

#### Procedure

To send an autocomplete request that returns a rich suggestion, follow these steps: 

REST 

(#rest) 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

   - b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. Call the `completionConfig.completeQuery` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.c ompletionConfig/completeQuery) 

method. 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/completionCo
nfig:completeQuery" \
-d '{
     "query":"QUERY_STRING",
     "suggestionTypes": ["CONTENT"]
   }'
```

Replace the following: 

   - _`PROJECT_ID`_ : the ID of your project. 

   - _`APP_ID`_ : the ID of the app. 

   - _`QUERY_STRING`_ : the typeahead input used to fetch suggestions. 

- <sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/1234/locations/gl
obal/collections/default_collection/engines/my_app/completionConfig:c
ompleteQuery" \
- d {
     "query": "C",
     "suggestionTypes": ["CONTENT"]
   }'
{
 "contentSuggestions": [{
   "suggestion": "critical crash in payment module",
   "document": {
     "name":
"projects/1234/locations/global/collections/default_collection/dataSt
ores/my_data_store/branches/0/documents/10000",
     "derivedStructData": {
       "title": "Critical Crash in Payment Module",
       "uri": "https://cymballabs.atlassian.net/browse/CPT-1",
       "source_type": "jira",
       "entity_type": "issue"
     }
   },
   "dataStore":
"projects/1234/locations/global/collections/default_collection/dataSt
ores/my_data_store"
 }]
}
```

**Note:** If you specify **`suggestionTypes`** as **`CONTENT`** , then any **`boostSpec`** 

(#language-boost), **`queryModel`** (/gemini/enterprise/docs/configure-autocomplete#diff-model), or 

```
includeTailSuggestions
```

(/gemini/enterprise/docs/configure-autocomplete#tail-match-suggestions) 

parameters in your curl command are ignored. 

### Send an autocomplete request and return recent queries

Return, as suggestions, a list of the user's most recent queries that prefix-match the query in the request. 

The matching query suggestions are listed from the most recent to the oldest. To use recent search, the user pseudo ID must be provided. 

**Important:** Gemini Enterprise doesn't automatically record search queries executed using the **`SearchService.Search`** 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.servingConf igs/search) 

method into a user's recent search history. To return recent queries, you must record search user events. For details, see Before you begin (#recent-queries-prerequisites). 

#### Before you begin

Before you can retrieve recent queries with autocomplete, you must record user searches as search user events by calling the `userEvents.write` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write) method. 

If search user events are not written, requests to `completionConfig.completeQuery` with `suggestionTypes: ["RECENT_SEARCH"]` return an empty list of suggestions ( `{}` ). 

To record a search user event, send a POST request to the `userEvents.write` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/write) method with the following values: 

`eventType` : set to `"search"` 

- `userPseudoId` : set to the user's unique pseudonymized identifier 

- `engine` : set to the resource name of your engine 

- `searchInfo.searchQuery` : set to the search query string entered by the user 

```
curl -X POST \
 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
 -H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/
LOCATION/userEvents:write" \
 -d '{
       "eventType": "search",
       "userPseudoId": "USER_PSEUDO_ID",
       "engine":
"projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/
APP_ID",
       "searchInfo": {
         "searchQuery": "SEARCH_QUERY"
       }
     }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`LOCATION`_ : the location of your app or data store (for example, `global` or `us` ). _`APP_ID`_ : the ID of the app. 

- _`USER_PSEUDO_ID`_ : a pseudonymized identifier of the user. This must match the `userPseudoId` passed in subsequent `completionConfig.completeQuery` requests. _`SEARCH_QUERY`_ : the query string searched by the user. 

For more information, see Record real-time user events with the `userEvents.write` method (/gemini/enterprise/docs/record-user-events#record-with-userevents-write-method). 

#### Example

An employee is querying their company intranet site to get information about taking vacations. The employee has performed the following queries, listed from most recent to oldest: 

`PTO` , `Vacation blackout periods` , `How much vacation time do I have?` , `Time off` , `Vacation policy` , `covering a vacant position during absences` , and `Can I` 

`take unpaid time off?` . 

Now, in response to the employee typing `vac` in the search box, the autocomplete suggestions would be as follows: 

- `Vacation blackout periods` 

- `How much vacation time do I have?` 

- `Vacation policy` 

- `Covering a vacant position during absences` 

#### Procedure

To send an autocomplete request that returns the user's most recent queries, follow these steps: 

REST 

(#rest) 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

      - b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. Call the `completionConfig.completeQuery` 

   - (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.c ompletionConfig/completeQuery) 

method. 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/completionCo
nfig:completeQuery" \
-d '{
     "query":"QUERY_STRING",
     "suggestionTypes": ["RECENT_SEARCH"],
     "userPseudoId": "USER_PSEUDO_ID"
   }'
```

Replace the following: 

- _`PROJECT_ID`_ : the ID of your project. 

- _`APP_ID`_ : the ID of the app. 

- _`QUERY_STRING`_ : the typeahead input used to fetch suggestions. 

- _`USER_PSEUDO_ID`_ : a pseudonymized identifier of the user. You can use an HTTP cookie for this field, which uniquely identifies a visitor on a single device. Don't set this field to the same identifier for multiple users. This would combine their query histories. Don't include personally identifiable information (PII) in this field. 

<sup>Example command and result</sup> 

```
curl -X POST -H "Authorization: Bearer $(gcloud auth print-access-
token)" \
-H "Content-Type: application/json" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/completionConfig:completeQuery" \
-d '{
     "query": "hol",
     "suggestionTypes": ["RECENT_SEARCH"],
     "userPseudoId": "test_user"
   }'
{
 "recentSearchSuggestions": [
   {
     "suggestion": "holiday readiness",
     "recentSearchTime": "2025-05-19T18:27:07.261698Z"
   },
   {
     "suggestion": "holiday freeze",
     "recentSearchTime": "2025-05-19T18:25:45.744021Z"
   },
   {
     "suggestion": "holiday",
     "recentSearchTime": "2025-05-19T18:20:08.916884Z"
   }
 ]
}
```

**Note:** If you specify **`suggestionTypes`** as **`RECENT_SEARCH`** , then any **`boostSpec`** (#language-boost), **`queryModel`** (/gemini/enterprise/docs/configure-autocomplete#diff-model), or **`includeTailSuggestions`** (/gemini/enterprise/docs/configure-autocomplete#tail-match-suggestions) parameters in your curl command are ignored. 

### Use an autocomplete denylist

You can use a denylist to prevent specific terms from appearing as autocomplete suggestions. 

Although advanced autocomplete is at the app-level, denylists are at the datastore-level. This is significant if your app is a blended search app. Create a denylist for each data store connected to the app. 

For information about creating and using denylists, see Use an autocomplete denylist (/gemini/enterprise/docs/configure-autocomplete#denylist). 

### Use an imported list of autocomplete suggestions

You can choose to provide your own list of autocomplete suggestions instead of using autocomplete suggestions generated from an autocomplete data model. 

For information about how to import a list, see Use an imported list of autocomplete suggestions 

(/gemini/enterprise/docs/configure-autocomplete#imported-suggestions). 

Last updated 2026-10-14 UTC. 



## Configure the app home page

URL: https://docs.cloud.google.com/gemini/enterprise/docs/app-home-page

The home page serves as the central hub for accessing key features and information within your app. It provides navigation to important areas of the app and enhances user productivity by offering quick access to commonly used resources. The key items on the home page include personalized announcements, shortcuts, and other customizable elements designed to streamline the user experience. These tools allow users to efficiently interact with essential internal resources, stay updated on the latest announcements, and manage their day-today tasks with ease. 

- Create and manage announcements (#announcements) 

Show new team member announcements (#new-team-member) 

- Create and manage shortcuts (#shortcuts) 

### Create and manage announcements

Announcements are used to display important updates, news, and notifications for all end users. These announcements appear prominently on the home page, so that key messages reach the entire organization. The primary purpose is to broadcast company-wide information, such as top news, policy changes, and upcoming events. 

An administrator configures the items that appear on the home page. End users can see only these configured items. 

Announcements can be viewed only in the app. They can't be targeted to specific groups. 

#### Before you begin

Before creating announcements, verify you have already set up an app with connected data stores. 

#### Create announcements

Set up announcements to share important news with your organization. Configure details such as title, description, images, links, and scheduling so that the announcement reaches users at the right time. 

To create announcements: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Go to the **Data Stores** page and click **Create Data Store** . 

3. Select **Announcements** . 

4. In the **Configure your data store** pane, enter a name for your data store and click **Create** to create your announcement data store. 

5. Go to your announcement data store, and, in the **Announcements** pane, click **+New** to create an announcement. 

6. In the **New announcement** pane, fill in the following fields: 

   - **Title** : Name of the announcement. 

   - **Description** : Describe your announcement. 

   - **Image URL** : The URL for an image that represents the announcement. **Note** : The **Image URL** must be accessible to all users within the organization. 

   - **Link URL** : The URL for a link that represents the announcement. 

   - **Start date** : Enter the start date of your announcement. 

   - **End date** : Enter the end date of your announcement. 

7. Click **Publish** to create a new announcement. 

8. To see the announcements for a data store, go to the **Data Stores** page and click the name of the announcements data store. 

The app displays the announcement only if the current date falls within the specified start and end times. It sorts announcements in descending order by start time. 

#### Manage announcements

Announcements are managed similarly to how regular data stores are, but offer a custom UI for creating and updating individual rows of announcements. 

### Show new team member announcements

New team member announcements welcome people who recently joined. These cards are shown in the announcements area of the home page. Each user sees only recent joiners from their own part of the organization, not every new hire in the company. 

#### Limitations

People data from Google Workspace isn't supported. 

#### Enable new team member announcements

To enable new team member announcements, do the following: 

1. Make sure that your people data includes each person's hire date and management chain. These appear in a person's record as the `hireDate` and `managers` fields: 

```
{"id":"jdoe","structData":{"personId":"jdoe","hireDate":"2025-06-
02T00:00:00Z","managers":[{"personId":"asmith"},{"personId":"bwong"}]}}
```

2. Create an announcements data store and connect it to your app. For more information, see Create and manage announcements (#announcements). 

3. Connect a people data store to the same app. Supported people data sources include Microsoft Entra ID 

(/gemini/enterprise/docs/connectors/entra-id/connect-entra-id) and People via Custom Connector (/gemini/enterprise/docs/connectors/connect-people-custom) (Preview). 

### Create and manage shortcuts

Shortcuts in the app provide users with quick access to commonly accessed links, such as internal document sites, knowledge bases, or frequently used tools. These shortcuts appear on the app's home page, letting your users navigate to important resources without searching through menus. Although shortcuts are optional, they offer a way to boost productivity by reducing the time spent looking for frequently used resources. 

The administrator configures items on the home page. Up to six shortcuts can appear on the home page. 

#### Before you begin

Verify an app is set up before creating shortcuts. 

#### Create shortcuts

To create shortcuts, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to edit. 

3. In the navigation menu, click **Configurations** . 

4. Click the **Search UI** tab. 

5. Under **Pinned Links / Shortcuts** , click **Add shortcut** . 

6. Fill in the following fields: 

   - **Title** : Name of the shortcut. 

   - **Icon URL** : Optional: The URL for the icon that represents the shortcut. 

   - **Shortcut URL** : The direct link to the resource you provide. 

7. In the **Preview** pane, verify that the shortcut appears correctly. 

8. Click **Save and Publish** . 

#### Manage shortcuts

Organize shortcuts by reordering and removing them as needed to keep the home page streamlined and up-to-date with the most relevant links. 

To rearrange or delete shortcuts, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to edit. 

3. In the navigation menu, click **Configurations** . 

4. Click the **Search UI** tab. 

5. Under **General configurations** > **Pinned Links / Shortcuts** , click the up arrow or down arrow icons to rearrange the shortcuts. 

6. To delete a shortcut, click the delete icon. 

7. Click **Save and Publish** . 

Last updated 2026-10-14 UTC. 



## Configure results for the UI

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-results

This page describes how to configure results for the web app UI, which is the interface that your users use to access your app. 

### Search widget concepts

Here are some concepts to help you understand how to use the controls on the **UI** tab. 

- **Snippet.** A short section of text, typically a sentence, under the document title. By default, a snippet is displayed for each search result for website and unstructured data. 

- **Search with an answer.** This feature provides a paragraph of information (the answer) synthesized from the top results of website or unstructured data. You can customize the number of top results that the answer is based on. By default, the top five results are summarized to create the answer. Search with an answer cannot be combined with Search with follow-ups. 

- **Search with follow-ups.** This feature for website and unstructured data allows for follow-up questions that keep the context of the initial search query. 

- **Autocomplete.** Suggests search queries based on the first letters that users enter into the search bar. For more information, see Configure autocomplete (/gemini/enterprise/docs/configure-autocomplete). 

- **Feedback.** Provides buttons and so that users can rate the quality of the search results. This information is sent only to Google. For more information, see Configure feedback (/gemini/enterprise/docs/configure-feedback). 

- **Metadata.** If the data is structured or contains metadata, you can configure which metadata fields to include in the search results. You can also map fields to display names for facets. For more information, see Configure facets for the UI (/gemini/enterprise/docs/configure-ui-facets). 

- **Admin-configured display name for sources.** Displays the administratorconfigured display name for data sources in the web app instead of the 

connector type. For more information, see Show administrator-configured display names for data sources (#configure-source-display-names). 

### Configure search results for unstructured or website data

The UI for unstructured and website data offers the following search customizations: 

- Search (single-turn) 

- Search with an answer (single-turn search with summarization) 

- Search with follow-ups (multi-turn search) 

To configure how the UI displays search results for unstructured data: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the app that you want to edit. 

3. In the navigation menu, click **Configurations** . 

4. Click the **UI** tab. 

5. Edit the fields on the tab. 

6. Use the **Preview** pane to make sure your changes are displayed as expected. 

7. Click **Save and publish** to apply your changes. 

### Configure search results for structured data

For structured data, by default, the UI displays all of the name-value pairs for each item in the search results. You can use the **Configurations** page in the Google Cloud console to customize how the UI displays search results. 

The following list shows the primary fields for displaying search results: 

- **Title.** An item title that a user can click to select that item in a search result. 

- **Thumbnail.** The URL of an image to be shown next to the item title in a search result. 

**URL.** A URL that the user is taken to when they click the item's title. 

You can display up to three additional fields in your search results and configure how they appear. 

In addition, you can select facets to filter search results on and set display names for them. For more about configuring facets, see Configure facets for the UI (/gemini/enterprise/docs/configure-ui-facets). 

To configure how the UI displays search results for structured data: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the search app that you want to edit. 

3. Click **Configurations** . 

4. Click the **UI** tab. 

5. If you have multiple data stores connected to your app, select the data store to configure results for. 

6. Expand the **Configure fields in results** section. 

7. In the **Preview** pane, type a query and press **Enter** to view how search results are displayed with your current settings. The preview updates automatically when you enter new settings. 

8. Optional: Click a device icon to see the preview in desktop or mobile format. 

9. To configure the primary fields ( **Title** , **Thumbnail** , and **URL** ) in your search results: 

   - a. Click the **Title** box and select a field to map to the titles of your search results. Or, select **None** if you don't want titles to appear in search results. 

   - b. Click the **Thumbnail** box and select a field to map to the thumbnail images in your search results. Or, select **None** if you don't want thumbnail images to appear in search results. 

   - c. Click the **URL** box and select a field that maps to the items that open when users click item titles in search results. Or, select **None** if you don't want item titles in your search results to link to items. 

10. To add additional fields to your search results: 

   - a. Click the **Text 1** box and select a field that you want to display in your search results. By default, only the field value is displayed in search results. 

   - b. Click the arrow next to the **Text 1** box to display the **Template** box. The **{value}** field in **Template** box represents the field value to display in the search result. Add text before or after the **{value}** field (or both) to give context to the value in the search results. For example, suppose you selected `price` in the **Text 1** box, and the price value for a particular item is 42. If you update the **Template** field to `"Total` 

`Price: {value} USD"` , then "Total Price: 42 USD" is displayed in the search results for that item. 

   - c. To add additional fields, repeat these steps for the **Text 2** and **Text 3** boxes. 

11. To configure facet settings: 

   - a. Expand the **Facet settings** section. 

   - b. Select a field to set as a facet and enter a display name. 

   - c. To add more facets, click **Add facet** . 

12. Check the **Preview** pane to make sure your changes display correctly. 

13. Click **Save and publish** to apply your changes. 

**Note:** For information about enabling autocomplete, see Configure autocomplete (/gemini/enterprise/docs/configure-autocomplete). For information about enabling feedback, see Configure feedback (/gemini/enterprise/docs/configure-feedback). 

### Show administrator-configured display names for data sources

By default, the web app displays the connector type as the label for single-instance data sources. You can turn on the **Use admin-configured display name for sources** setting so that the web app instead displays the custom display name that you configured for each data source. 

To turn administrator-configured display names for data sources on or off: 

ConsoleREST (#rest) (#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the app that you want to edit. 

3. In the navigation menu, click **Configurations** . 

4. Click the **Search UI** tab. 

5. In the **General configurations** section, turn the **Use adminconfigured display name for sources** toggle on or off. 

6. Click **Save and publish** to apply your changes. 

### Next steps

Preview search results (/gemini/enterprise/docs/preview-search-results) 

Last updated 2026-10-14 UTC. 



## Configure facets for the UI

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-ui-facets

Facets can be shown next to results in the web app UI to help users filter the results. You can use the **Configurations** page in the Google Cloud console to specify which fields to use as facets on your UI for apps with structured data or unstructured data with metadata. 

Facet configuration is not supported for apps with website data or unstructured data without metadata. 

Before setting a field as a facet, make sure that the field is set to **Retrievable** and **Indexable** . For more information, see Configure feld settingsi 

(/gemini/enterprise/docs/configure-field-settings). 

To set a field as a facet: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the app that you want to edit. 

3. Click **Configurations** . 

4. Click the **UI** tab. 

5. If you have multiple data stores connected to your app, select the data store to configure facet settings for. 

6. Expand the **Facet settings** section. 

7. Click **Add facet** . 

8. Select a field to use as a facet. 

9. Enter a display name for the facet. 

10. Click **Save and publish** . 

see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2026-10-14 UTC. 



## Configure feedback

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-feedback

The search widget includes feedback buttons that help assess search quality issues. This page explains how to turn this feature on or off using the Google Cloud console. 

When the feedback feature is turned on, the widget rendered on your web page displays **Thumbs up** and **Thumbs down** buttons. Your end users can click the buttons to indicate whether the quality of the results appeared as expected. If a user clicks the **Thumbs down** button, they are prompted to select from a list of reasons why the quality is not as expected and to provide additional comments. 

If your app is located in the global region, then the widget feedback is visible to your Google Cloud administrator and Google. If your app is located in a multiregion, then only your Google Cloud administrator sees the feedback. Regardless, your users shouldn't include Personally Identifiable Information (PII) or sensitive data with feedback. 

### Turn feedback buttons on or off

To turn feedback buttons, and , in your widget on or off, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the search app that you want to edit. 

3. Click **Configurations** . 

4. Click the **Search UI** tab. 

5. Toggle **Enable feedback** to turn feedback buttons on or off. 

6. Click **Save and publish** . 

Your users' feedback can be viewed on the app's Analytics page. See View analytics (/gemini/enterprise/docs/view-analytics). 

### What's next

Preview search results (/gemini/enterprise/docs/preview-search-results). 

Last updated 2026-10-14 UTC. 



## Configure the assistant

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-assistant

This page describes how to configure the assistant's behavior. 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** . 

4. Select the **Assistant** tab. 

5. In the **Additional LLM system instructions** section, select **Customize** . 

6. Enter the additional LLM system instructions. 

For example: 

```
Make the summary headings bold
List the resources as an unordered list
```

7. In the **Enable web grounding** section, make sure the toggle is switched on and then select one of the following options: 

   - **Google search (not Data Residency compliant)** to use the standard Google Search index for grounding. 

   - **Enterprise web search (Data Residency compliant)** to use the enterprise-grade and compliant web index. 

8. In the **Default web search state** section, use the toggle to define the default behavior for queries: 

   - Switch the toggle on to enable web search by default for new queries. 

   - Switch the toggle off to disable web search by default. 

**Note:** Users can always change this setting manually for each search. 

9. In the **Enable location context** section, use the toggle switch to enable or disable the feature: 

   - Switch the toggle on to allow the Gemini Enterprise app to use location data to improve the quality of responses. 

   - Switch the toggle off to disable the use of location context. 

_Configure the web setting and location context_ 

10. In the **Enable Model Armor** section, follow the instructions to configure **Model Armor** and setup the Model Armor templates. For more information, see the Configure Model Armor 

   - (/gemini/enterprise/docs/enable-model-armor#configure-model-armor-console) page. 

11. In the **Enable Knowledge Catalog** section, use the toggle to turn the Knowledge Catalog integration on or off. This setting is automatically enabled when you attach a BigQuery, Spanner, Cloud SQL, or AlloyDB for PostgreSQL data store in federated query mode, or you can turn it on or off manually at any time. For more information, see Connect to Knowledge Catalog 

   - (/gemini/enterprise/docs/connectors/connect-knowledge-catalog). 

12. In the **Banned phrases** section, click **Add banned phrase** to add a phrase. 

13. In the dialog, enter the banned phrase and choose the match type. 

**Simple string match** : This is a substring match. For example, if **Hello** is a banned phrase, both **Hello world** and **Helloworld** are rejected. 

_Enter the banned phrase and choose the_ **_Single string match_** _type_ 

**Word boundary string match** : This blocks the phrase as a whole word. For example, if **Hello** is a banned phrase, **Hello world** is rejected, but **Helloworld** is accepted. 

_Enter the banned phrase and choose the_ **_Word boundary string match_** _type_ 

**Note:** When you use multiple phrases, the matching logic ensures the query is blocked if any of the configured banned phrases are present in your input. 

14. In the **Chat history retention period** section, select a retention period for assistant chat sessions. You can select 1, 30, 60, 90, 120, or 180 days (the default is 60 days). Chat sessions older than the selected retention period are automatically deleted. 

**Important:** The chat age is based on the **creation date.** Inform your users of this because it means that chats, which they might have interacted with as recently as yesterday, disappear without warning when the retention period is reached. 

15. Click **Save and publish** . 

Last updated 2026-10-14 UTC. 



## About custom preambles

URL: https://docs.cloud.google.com/gemini/enterprise/docs/preamble

This page discusses custom preambles and how you can write preambles to improve the quality of generated answers from the Answer API. 

The preamble sets the initial context and expectations for the LLM before it processes your input document. The preamble influences the quality of the generated summaries. There is a default preamble supplied whenever you call the answer 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/answe r) 

method. However, you have the option to specify your own preamble instead of using the default. 

For instructions on how to specify the preamble in the answer method call, see Specify a custom preamble (/gemini/enterprise/docs/answer#preamble-rest). 

For example, you can use the preamble to do the following: 

- Specify words that the model can and can't use. 

- Specify topics to focus on or avoid. 

- Specify the style, tone, and format of the response. 

Tailoring the preamble can significantly improve the quality of summaries. 

The preamble should have two parts: 

- **The task description** that describes the task you are asking the LLM to perform. See Examples of task descriptions (#task-descriptions). 

- **Additional instructions** that the LLM should follow. See Examples and tips for additional instructions (#additional-instructions). 

### Examples of task descriptions

Here are some examples of task descriptions. The scenario is that your employees want answers from a data store that contains many company documents. 

#### Example 1

Task description to comprehensively cite sources: 

```
Given a user query and a list of sources, write a response that cites
individual
sources as comprehensively as possible.
```

#### Example 2

Task description to understand the user and focus on helpfulness: 

```
You are an enterprise LLM summarization tool. Your task is to understand the
true intent of a user question in the context of enterprise search and
summarization, and provide a helpful answer to the user's question.
```

#### Example 3

Task description to summarize a conversation between a customer and an assistant: 

```
Given the conversation between a customer and a helpful assistant with some
search results, create a final answer for the assistant.
```

### Examples and tips for additional instructions

The additional instructions should capture your specific key requirements. 

The following table gives examples of additional instructions that you might provide after the task description, what kind of problems each example addresses, 

Problem to solve Solution Examples The answers need to be Provide additional context and Example 1 more tailored to the instructions to ensure that the business needs summary is tailored to the specific use `Utilize the` case and target audience. `specific context of the workspace (e.g. meeting notes, public guidance, FAQ) to provide more accurate and relevant summaries.` Example 2 `Summarize customer feedback, focusing on their pain points, feature request and overall satisfaction. Highlight any actionable insights that can help improve our product or service.` Example 3 `For input documents of troubleshooting website, please summary the problem statement, step-by-step solutions and any relevant tips or warnings.` 

Example 4 

|Problem to solve<br>Solution|Examples|
|---|---|
||`"XYZ" is an`<br>`internal forum for`<br>`engineers to discuss`<br>`technical problems,`<br>`you can use it to`<br>`summarize technical`<br>`issues, proposed`<br>`solutions and any`<br>`unresolved`<br>`challenges or next steps`<br>`identified in the`<br>`discussion.`|
|Answer needs to be in a<br>specific style<br>Clearly specify the style or tone and<br>the intended audience.|Example 1|
||`Summarize`<br>`troubleshooting guide for`<br>`customer support agent in`<br>`a clear and`<br>`concise manner.`<br>`The summary should be`<br>`easy for a non-technical`<br>`user to`<br>`understand.`|
||Example 2|
||`Summarize the`<br>`technical documents for`<br>`engineers. Focus on the`<br>`core`<br>`functionality,`<br>`system architecture, and`<br>`potential challenges.`|

|Problem to solve<br>Solution|Examples|
|---|---|
|Answer needs to be in a<br>specific format<br>Specify output format|Example 1|
||`Use bullet points`<br>`for steps, numbered lists`<br>`for rankings, tables for`<br>`comparisons, code`<br>`block for coding example`|
||Example 2|
||`Summarize the key`<br>`takeaways in a numbered`<br>`lists`|
|Answer needs to be shortExplicitly instruct the LLM to generate<br>"concise" or "brief" summaries. You<br>can also specify the word or sentence<br>count if applicable.|Example 1<br>`Please keep`<br>`summaries concise and`<br>`focused, providing only`<br>`the most`<br>`essential`<br>`information to address`<br>`the user's query.`|
||Example 2|
||`The answer should`<br>`be less than 200 words.`|

|Problem to solve|Solution|Examples|
|---|---|---|
|Answer needs to be<br>more comprehensive|Encourage the LLM to include key<br>details and important points.|Example|
|||`Please ensure key`<br>`details are included.`|
|Inclusion of prohibited<br>topics|Define how the model should respond<br>in certain situations.|Example<br>`For political`<br>`questions, the most`<br>`helpful way is to`<br>`politely refuse to`<br>`answer the`<br>`question.`|
|Reduce Hallucination<br>(incorrect information)|Emphasize the importance of accuracy<br>and instruct the LLM to strictly adhere<br>to the information presented in the<br>text.|<br>Example 1<br>`Keep the summary`<br>`accurate, ensuring all`<br>`claims are verifiable`<br>`within the given context.`|
|||Example 2|
|||`Use exact words from the`<br>`context if possible.`|

### Examples of complete preamble

Here are some more examples of complete preamble, made up of the task description and the additional instructions. 

#### Example 1

Request a concise, accurate, and relevant summary and present it in a userfriendly format. 

```
You are an enterprise LLM summarization tool. Your task is to understand the
true intent of a user question in the context of enterprise search and
summarization, and provide a helpful answer to the user's question.  Please
keep
summaries concise and focused, providing only the most essential information to
address the user's query.
Please also structure and format the summary by
1) prioritize most relevant and accurate information to user's question
```

- `2) highlight critical information` 

```
3) structure the response and adapt the formatting to be user friendly (e.g.,
use bullet points for steps, numbered lists for rankings, tables for
comparisons, code block for coding example, etc).
```

#### Example 2

Provide a concise, friendly, and helpful final answer to a customer's query based on a conversation. 

```
Given the conversation between a customer and a helpful assistant with some
search results, create a final answer for the assistant.
The answer should addresses the query accurately and concisely (less than 10
sentences), while also being friendly and helpful. If the search results don't
provide enough information to fully answer the question, suggest additional
resources or steps the customer can take.
```

#### Example 3

Provide comprehensive and understandable answers and cite given sources. Politely decline to answer any political questions. 

```
Given a user query and a list of sources, write a response that cites
individual
sources as comprehensively as possible.
The response should be suitable for a non-expert audience.
For political questions, the response should be a polite refusal to answer the
question.
```

### Best Practices

The following are some best practices for writing and tuning preamble: 

- **Iterative Refinement:** Experiment with different preamble variations and observe the impact on the answer quality. 

- **User Feedback:** Gather feedback from users to identify recurring issues and areas for improvement. 

- **Stay Updated:** The effectiveness of preamble tuning can vary depending on the model version and the nature of your documents. Continuously experiment and refine your approach to achieve optimal results. 

- **Thorough Evaluation:** Verifying modified preamble across all intended use cases helps identify and mitigate potential biases or unexpected behavior that may negatively impact summary quality in certain scenarios. 

Last updated 2026-10-14 UTC.
