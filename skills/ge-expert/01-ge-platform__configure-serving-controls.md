# Gemini Enterprise: platform, security, agents, cost, monitoring / Configure serving controls to Basic autocomplete
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 578-611, extracted 2026-10-18

Contains:
- Configure serving controls (pages 578-589) https://docs.cloud.google.com/gemini/enterprise/docs/configure-serving-controls
- Basic autocomplete (pages 590-611) https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete

## Configure serving controls

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-serving-controls

Serving controls (also called controls) change the default behavior of how a request is served when results are returned. Serving controls act at a data-store level. 

For example, controls can boost and bury results, filter entries from returned results, associate strings with each other as synonyms, or redirect results to specified URIs. 

### About serving controls

To change the results of a request, first create a serving control. Then, attach that control to the _serving config_ of an app. A serving config 

(/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.serving Configs) 

configures metadata that's used to generate serving time results, such as search results or answers. A serving control only affects requests served by the app if the control is attached to the app's serving config. 

Some controls, such as boost controls, have dependencies on data stores. If a data store is removed from an app, then any data store-dependent controls are also removed from that app and become inactive, but are not deleted. 

#### Serving control types

The following types of serving controls are available: 

|Control|Description|Available for|
|---|---|---|
|Boost control|Changes the|Search apps with data stores that support a schema,|
|(#boost)|returned order of<br>results|such as data stores that contain structured data or<br>unstructured data with metadata|
|Filter control|Removes entries|Search apps with data stores that support a schema,|
|(#filter)|from returned<br>results|such as data stores that contain structured data or<br>unstructured data with metadata|

|Control|Description|Available for|
|---|---|---|
|Synonyms control<br>(#synonyms)|Associates queries<br>with each other|Search apps with structured or unstructured data<br>stores|
|Redirect control|Redirects to a|All search apps|
|(#redirect)|specified URI||
|Promote control|Promotes a|Search apps with structured or unstructured data|
|(#promote)|specified link for a<br>query|stores|

### About conditions

When creating a control, you can optionally define a condition that determines when the control is applied. Conditions are defined using condition fields. The following condition fields are available: 

- **`queryTerms`** . An optional control that's applied when specific queries are searched for. When the `queryTerms` condition is used, the control is applied when the value of `queryTerms` matches a term in `SearchRequest.query` . Query terms can only be used when the `Control.searchUseCase` is set as `SOLUTION_TYPE_SEARCH` . Up to 10 different `queryTerms` can be specified on a single `Control.condition` . If no query terms are specified, the `queryTerms` field is ignored. 

To successfully create a promote control, you must specify the `queryTerms` field with `fullMatch` set to `true` or `false` . 

- **`activeTimeRange`** . An optional control that's applied when a request occurs within a specified time range. It checks that the time a request was received is between `activeTimeRange.startTime` and `activeTimeRange.endTime` . Up to 10 `activeTimeRange` ranges can be specified on a single `Control.condition` . If th e `activeTimeRange` field isn't specified, the field is ignored. 

If multiple conditions are specified for a control, the control is applied to the search request when both condition types are satisfied. If multiple values for the same condition are specified, only one of the values needs to match for that condition to be satisfied. 

For example, consider the following condition with two query terms specified: 

```
"queryTerms": [
 {
   "value": "gShoe",
   "fullMatch": true
 },
 {
   "value": "gBoot",
   "fullMatch": true
 }
]
```

The condition will be satisfied for a request with `SearchRequest.query="gShoe"` or a request with `SearchRequest.query="gBoot"` , but won't be satisfied with `SearchRequest.query="gSandal"` or any other string. 

If no conditions are specified, the control is always applied. 

For more information, see the `Condition` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.controls#C ontrol.Condition) 

field in the API reference. 

### Create and attach boost serving controls

A boost serving control reorders the results by promoting or demoting them based on the applied conditions. Boost works by applying a multiplying factor to the ranking of a document that meets the boost conditions. 

Use the following instructions to create a boost serving control. 

ConsoleREST (#rest) (#console) 

To create and attach a boost control using the Google Cloud console, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select the app for which you want to create the boost control. 

3. Click **Configurations** and then click the **Control** tab. 

4. Click **Create control** . 

5. For **What do you want to do?** , specify the control name and type: 

   - a. For **Control name** , enter a name for your boost/bury control. 

   - b. For **Control Type** , select **Boost/bury** . 

   - c. Click **Continue** . 

6. For **Set Rule Scope & Impact** , define the actions that you want to trigger with this control: 

   - a. Select a data store from the list. If you want the action to be applied to multiple data stores, create a control for each data store. 

   - b. For **Filter** , add a filter. 

This is a string specifying requirements that must be met by the document. Only if the document matches all the requirements, the boost condition is applied. Otherwise, there is no change. If you don't specify a filter, then the boost is applied to all documents in the data store. 

For information about the filtering syntax, see Filter expression syntax 

      - (/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax). 

   - c. For **Boost/bury value** , select a boost/bury value in the range [-1, 1] using the slider. The slider moves in steps of 0.01. 

   - d. Click **Continue** . 

7. For **Optional: When This Rule Activates** , set the following conditions that trigger the control. If no conditions are configured, the control is always in effect: 

   - a. Add **Partial match query terms** . The control takes effect when these query terms match partially. 

   - b. Add **Exact match query terms** . The control takes effect when these query terms match exactly. 

   - c. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1** . This defines the window when the condition is active. You can add a maximum of 10 time ranges. 

   - d. Click **Continue** . 

8. For **Additional settings** , choose if you want to activate the rule: 

   - a. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately** . 

   - b. Click **Continue** . 

9. Click **Submit** . 

### Create and attach filter serving controls

A filter serving control is defined as a control with a `filterAction` . 

Use the following instructions to create a filter serving control. 

ConsoleREST (#rest) 

(#console) 

To create and attach a filter control using the Google Cloud console, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select the app for which you want to create the filter control. 

3. Click **Configurations** and then click the **Control** tab. 

4. Click **Create control** . 

5. For **What do you want to do?** , specify the control name and type: 

   - a. For **Control name** , enter a name for your filter control. 

   - b. For **Control Type** , select **Filter** . 

   - c. Click **Continue** . 

6. For **Set Rule Scope & Impact** , define the actions that you want to trigger with this control: 

   - a. Select a data store from the list. If you want the action to be applied to multiple data stores, create a control for each data store. 

   - b. For **Filter** , tell the rule which specific items to look for. You can combine search terms using `AND` , `OR` `NOT` and group terms with `()` . For exact phrases, use quotation marks ( `""` ). For example: `category: "electronics" AND price < 500, status: "open" AND priority:"P1"` . 

For information about the filtering syntax, see Filter expression syntax 

      - (/gemini/enterprise/docs/filter-search-metadata#filter-expression-syntax). 

   - c. Click **Continue** . 

7. For **Optional: When This Rule Activates** , set the following conditions that trigger the control. If no conditions are configured, the control is always in effect: 

   - a. Add **Partial match query terms** . The control takes effect when these query terms match partially. 

   - b. Add **Exact match query terms** . The control takes effect when these query terms match exactly. 

   - c. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1** . This defines the window when the condition is active. You can add a maximum of 10 time ranges. 

   - d. Click **Continue** . 

8. For **Additional settings** , choose if you want to activate the rule: 

   - a. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately** . 

   - b. Click **Continue** . 

9. Click **Submit** . 

### Create and attach synonyms serving controls

A synonyms serving control is defined as a control with a `synonymsAction` . 

Use the following instructions to create a synonyms serving control. 

ConsoleREST (#rest) 

(#console) 

To create and attach a synonyms control using the Google Cloud console, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select the app for which you want to create the synonyms control. 

3. Click **Configurations** and then click the **Control** tab. 

4. Click **Create control** . 

5. For **What do you want to do?** , specify the control name and type: 

   - a. For **Name Your Control** , enter a name for your synonyms control. 

   - b. For **Control Type** , select **Synonyms** . 

   - c. Click **Continue** . 

6. For **Set Rule Scope & Impact** , define the actions that you want to trigger with this control: 

   - a. Enter the synonyms you want to have considered in the control. For example, enter _cats_ followed by a return (not comma), then _feline._ 

   - b. Click **Continue** . 

7. For **Optional: When This Rule Activates** , set the following conditions that trigger the control. If no conditions are configured, the control is always in effect: 

   - a. To add an active time range, click **Add time range** and set **Start Time 1** and **End Time 1** . This defines the window when the condition is active. You can add a maximum of 10 time ranges. 

   - b. Click **Continue** . 

8. For **Additional settings** , choose if you want to activate the rule: 

   - a. If you don't want to activate this control as soon as it's created, turn off **Publish this control immediately** . 

   - b. Click **Continue** . 

9. Click **Submit** . 

### Create and attach redirect serving controls

A redirect serving control allows redirecting users to a provided URI. Redirect controls are defined as a control with a `redirectAction` . 

Use the following instructions to create a redirect serving control. 

For field details, see the `engines.controls` API reference 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls) and the `engines.controls.create` API reference 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.controls/creat e) 

1. Find your app ID. If you already have your app ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Go to Apps (https://console.cloud.google.com/gemini-enterprise/apps) 

   - b. On the **Apps** page, find the name of your app and get the app's ID from the **ID** column. 

2. Run the following curl commands to create your controls. 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/g
lobal/collections/default_collection/engines/APP_ID/controls?
controlId=CONTROL_ID" \
-d '{
"displayName": "DISPLAY_NAME",
"solutionType": "SOLUTION_TYPE_SEARCH",
"useCases": ["USE_CASE"],
"conditions": {
 "queryTerms": [
   {
     "value": "VALUE",
     "fullMatch": FULL_MATCH
   }
 ],
 "activeTimeRange": [
   {
     "startTime": "START_TIMESTAMP",
     "endTime": "END_TIMESTAMP"
   }
 ]
},
"redirectAction": {
 "redirectURI": "REDIRECT_URI"
}
}'
```

Replace the following: 

_`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

_`APP_ID`_ : the ID of the app. 

   - _`CONTROL_ID`_ : a unique identifier for the control. The ID can contain [1-63] characters that can be letters, digits, hyphens, and underscores. 

   - _`DISPLAY_NAME`_ : the human-readable name for the control. Google recommends that this name provide an indication of when or why to use the control. Must be a UTF-8 encoded string with length [1,128]. 

   - _`USE_CASE`_ : must be either `SEARCH_USE_CASE_SEARCH` or `SEARCH_USE_CASE_BROWSE` . If `SEARCH_USE_CASE_BROWSE` is specified, then `Condition.queryTerms` can't be used in the condition. 

   - _`CONDITION`_ : an optional field that defines when the control should be applied. Contains the following fields: 

      - _`VALUE`_ : the specific query value to match against. It's a lowercase UTF-8 string with length `[1, 5000]` . If _`FULL_MATCH_1`_ is `true` , this field can have at most three space-separated terms. 

      - _`FULL_MATCH`_ : a boolean that indicates whether the search query needs to exactly match the query term. When set to `true` , it requires `SearchRequest.query` to completely match the `queryTerm.value` . When set to `false` , it requires `SearchRequest.query` to contain `queryTerm.value` as a substring. 

      - _`START_TIMESTAMP`_ : a timestamp in RFC 3339 UTC "Zulu" format to indicate the start of a time range. 

      - _`END_TIMESTAMP`_ : a timestamp in RFC 3339 UTC "Zulu" format to indicate the end of a time range. 

   - _`REDIRECT_URI_N`_ : a URI where you are redirected. Can have a maximum length of 2000 characters. For example, if the value of the query term is "support", you can set a redirect to your technical support page instead of returning (or failing to return) search results for "support". In this example, the redirect URI becomes `"https://www.example.com/support"` . For more information, see `redirectAction` 

   - (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores .controls#redirectaction) 

3. Attach the control to the app's serving config using the `engines.servingConfigs.patch` 

(/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.se rvingConfigs/patch) 

method. 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locati
ons/global/collections/default_collection/engines/APP_ID/servingConfigs/de
fault_search?update_mask=redirect_control_ids" \
-d '{
 "redirectControlIds": ["REDIRECT_ID_1", "REDIRECT_ID_2"]
}'
```

Replace _`REDIRECT_ID_N`_ with the control IDs that you created in the previous step. 

### Create and attach promote serving controls

A promote serving control lets you display a link as a promoted result. This control is available for search apps with structured or unstructured data stores and blended search apps. 

For the promote control to take effect, you must attach it to the serving config of the app. 

Promote controls are defined using a `promoteAction` . 

To successfully create a promote control, you must specify the `queryTerms` field with `fullMatch` set to `true` or `false` . 

Use the following instructions to create a promote serving control. 

ConsoleREST (#rest) (#console) 

### Modify serving controls

To modify a control's configuration, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Select the app for which you want to modify controls. 

3. Click **Configurations** and then click the **Control** tab. 

4. In the list of the app's controls, click for a control that you want to modify and click **Edit** . 

5. Edit the control in the **Edit control** pane: 

   - a. To enable or disable a control, in the list of the app's filter controls, click for a control that you want to enable or disable and click **Enable** or **Disable** , respectively. 

   - b. To delete a control, in the list of the app's controls, click for a control that you want to delete and click **Delete** . 

### What's next

- To understand the impact of a serving control on the search quality of an app, evaluate search quality (/gemini/enterprise/docs/evaluate-search-quality). 

Last updated 2026-10-14 UTC. 



## Basic autocomplete

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-autocomplete

This page describes Gemini Enterprise's basic autocomplete feature. Autocomplete generates query suggestions based on the first few characters entered for the query. 

**Caution:** This version of autocomplete doesn't support third-party data stores or apps with multiple data stores attached. Google recommends that you use advanced autocomplete (/gemini/enterprise/docs/configure-advanced-autocomplete) instead. 

For structured and unstructured data, by default, autocomplete generates suggestions based on the content of documents in the data store. After document import, by default, autocomplete doesn't start generating suggestions until there is sufficient quality data, typically a couple of days. If you make autocomplete requests through the API, autocomplete can generate suggestions that are based on the search history or user events. 

The query suggestions model determines what type of data autocomplete uses to generate suggestions. There are four query suggestions models: 

- **Document.** The document model generates suggestions from user-imported documents. 

- **Completable Fields.** The completable fields model suggests text taken directly from structured data fields. Only those fields that are annotated with `completable` are used for autocomplete suggestions. This model is only available for structured data. 

- **Search history.** The search history model generates suggestions from the history of `SearchService.search` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/search#goog le.cloud.discoveryengine.v1.SearchService.Search) 

API calls. Don't use this model if there is no traffic available for the 

`servingConfigs.search` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.servingConfigs/s earch) 

method. 

   - **User event.** The user event model generates suggestions from user-imported search events. 

- Autocomplete requests are sent using the `dataStores.completeQuery` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/completeQuery) method. 

The following table shows the query suggestions model types available for each data type. 

|Query suggestions<br>model|Data source|Website<br>data|Structured<br>data|Unstructured<br>data|
|---|---|---|---|---|
|Document|Imported by user||✔* (default)|✔ (default)|
|Completable fields|Imported by user||✔||
|Search history|Automatically collected|✔ (default)|✔|✔|
|User events|Imported by user or automatically<br>collected by widget|✔|✔|✔|

* : The document schema must contain `title` or `description` fields, or there must be fields that have been specified as `title` or `description` key properties. See Update a schema for structured data (/gemini/enterprise/docs/update-schemas). 

If you don't want to use the default model for your data type, you can specify a different model when you send your autocomplete request. Autocomplete requests are sent using the `dataStores.completeQuery` method. For information, see API instructions: Send an autocomplete request to choose a different model (#diff-model). 

### Autocomplete features

Gemini Enterprise supports the following autocomplete features to show the most helpful predictions during search: 

|Feature|Description|Example or more information|
|---|---|---|
|Correct typos|Correct word spellings that are typos.|`Milc`→`Milk`.|
|Remove unsafe<br>terms|Powered by Google Safe Search.<br>Remove inappropriate queries.|Text that's offensive, such as porn, racy,<br>vulgar, violence.|
||Supported in English (`en`), French (`fr`),<br>German (`de`), Italian (`it`), Polish (`pl`),<br>Portuguese (`pt`), Russian (`ru`), Spanish<br>(`es`), and Ukrainian (`uk`).||

|Feature|Description|Example or more information|
|---|---|---|
|Prevent display of<br>basic personally<br>identifiable<br>information (PII)|Powered by<br>Sensitive Data Protection<br>(/sensitive-data-protection/docs), Gemini<br>Enterprise makes a reasonable effort to<br>prevent display of basic types of PII, such<br>as phone numbers and email addresses.|If there is an email address<br>`jeffersonloveshiking@gmail.com`in the<br>data store, Gemini Enterprise won't return the<br>email address as an autocomplete suggestion<br>if the user types`jef`in the search bar.<br>To more thoroughly safeguard against PII<br>leaks, Google recommends that you apply<br>your own_Data Loss Protection (DLP)_solution<br>in addition to the detectors that are provided<br>by Gemini Enterprise. For more information,<br>see<br>Protect against PII leaks(#pii).|
|Denylist|Remove terms that are listed in the<br>denylist.|For more information, see<br>Use an<br>autocomplete denylist(#denylist).|
|Deduplicate Terms|Powered by AI-driven semantic<br>understanding.<br>For near-identical terms, either term<br>matches, but only the more popular<br>one is suggested.|`Shoes for Women`,`Womens Shoes`, and<br>`Womans Shoes`are deduplicated, and only the<br>most popular one is suggested.|
|Tail match<br>suggestions|Not available in US and EU multi-<br>regions.<br>Optional setting.<br>If there are no autocomplete matches<br>for the entire query, suggest matches<br>for only the trailing word of the query.<br>Not available for healthcare search.|For more information, see<br>Tail match<br>suggestions(#tail-match-suggestions).|

### Tail match suggestions

Tail match suggestions are made using exact prefix matching against the last word in a query string. 

For example, say the query "songs with he" is sent in an autocomplete request. When tail matching is enabled, autocomplete might find that the full prefix "songs with he" does not have any matches. However, the last word in the query, "he", has an exact prefix match with "hello world" and "hello kitty". In that case, the returned suggestions are "songs with hello world" and "songs with hello kitty" because there are no full match suggestions. 

You can use this feature to reduce empty suggestion results and increase suggestion diversity, making this especially useful in cases where data sources (user event count, search history, and document topic coverage) is limited. However, enabling tail match suggestions can reduce the overall quality of suggestions. Because tail match only matches the trailing word of the prefix, some returned suggestions might not make sense. For example, a query such as "songs with he" might get a tail match suggestion like "songs with helpers guides". 

Tail match suggestions are only returned if: 

1. `include_tail_suggestions` is set to `true` in the `dataStores.completeQuery` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/completeQuery) request. 

2. There are no full prefix match suggestions for the query. 

### Protect against PII leaks

The definition of PII is broad, and PII can be difficult to detect. As a result, Gemini Enterprise can't guarantee that PII won't be returned in autocomplete suggestions. 

Gemini Enterprise applies the Sensitive Data Protection (/sensitive-data-protection/docs) inspection service to look for and block common types of PII from appearing as suggestions. However, if your data stores contain PII or if you use the search history or user events query suggestions models, review the following and take appropriate action: 

1. If the types of PII that you want to protect are fairly standard, such as phone numbers and email addresses, begin by extensively testing autocomplete suggestions for your app. Gemini Enterprise can't guarantee that PII won't be returned in autocomplete suggestions. 

2. If PII leaks are discovered during autocomplete testing or if you already know that you have non-standard PII to protect (for example, proprietary user IDs), then try adjusting the autocomplete threshold and content serving parameters. For more information, see Reduce the risk of returning suggestions that contain PII (#update-thresholds). 

3. If adjusting the parameters isn't sufficient to prevent PII leaks, then implement your own DLP solution. Customize the DLP solution for the types of PII most likely to be found in your data stores, user events, or users' search queries. You can use Sensitive Data Protection (/sensitive-data-protection/docs) or a third-party DLP service. Take one of the following approaches: 

   - Filter out PII before you import the documents and user events in your data stores. 

   - Review autocomplete suggestions before presenting suggestions to the user at serving time and block the suggestions that contain any PII. 

4. If you use the search history or user events model, add some informational text on the search bar, telling your users not to put PII in their search queries. 

5. If you have questions or encounter particular challenges with blocking PII, contact your customer engineer (CE) or Google account team. 

### Turn autocomplete on or off for a widget

To turn autocomplete on or off for a widget, follow these steps: 

Console (#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the app that you want to edit. 

3. Click **Configurations** . 

4. Click the **UI** tab. 

5. Toggle the **Show autocomplete suggestions** option to turn autocomplete suggestions for the widget on or off. When you enable autocomplete, expect to wait a day or two before suggestions start. 

### Update autocomplete settings

To configure the autocomplete settings in the UI, follow these steps: 

Console 

<!-- Start of picture text -->
 (#console)<br><!-- End of picture text -->

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the app that you want to edit. 3. Click **Configurations** . 

4. Click the **Autocomplete** tab. 

5. Enter or select new values for the autocomplete settings you want to update: 

- **Maximum number of suggestions:** The maximum number of autocomplete suggestions that can be offered for a query. 

- **Minimum length to trigger:** The minimum number of characters that can be typed before autocomplete suggestions are offered. 

- **Matching order** : The location in a query string that autocomplete can start matching its suggestions from. 

- **Query suggestions model** : The query suggestions model used to generate the retrieved suggestions. This can be overridden in the `dataStores.completeQuery` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/completeQuery) using the `queryModel` parameter. 

- **Enable autocomplete** : By default, autocomplete doesn't start making suggestions until it has sufficient quality data, typically a couple of days. If you want to override this default and start getting some autocomplete suggestions sooner, select **Now** . 

Even when you select **Now** , it can take a day for suggestions to be generated and still some autocomplete suggestions will be missing or poor quality until there is sufficient good data. 

   - **Deny list** : Import a denylist as a JSON file in a Cloud Storage bucket. For more information about the denylist constraints and specifications, see Use an autocomplete denylist (#denylist). 

6. Click **Save and publish.** Changes take effect within a few minutes for engines where autocomplete has already been turned on. 

### Reduce the risk of returning suggestions that contain PII

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

End users have all kinds of PII information, such as driver licenses and telephone numbers, which they are supposed to keep private. But, any of this PII information might be typed into the search bar by users looking for results that are specific to themselves. 

If you use the search history or user events model and there is a likelihood of your users typing PII into the search bar, then you can reduce PII leaks by adjusting the following parameters: 

- `queryFrequencyThreshold` : Before a query can be returned as an autocomplete suggestion, it must have been entered this many times. 

- `numUniqueUsersThreshold` : Before a query can be returned as an autocomplete suggestion, it must have been entered by this many unique users. The value of the `userPseudoId` field in the search user event (/gemini/enterprise/docs/user-events#search) determines if the user is unique. 

#### Use case example

For example, take a case where users have account numbers that should be kept private. 

If the search history or user events suggestion model is in use, then these account numbers, along with all the other terms that end users search for, are used to generate suggestions. Thus, if user-A's account number `YZ-46789A` has repeatedly been entered into the search bar and user-B has an account number of `YZ-42345B` , when user-B types `YZ-4` into the search bar, the autocomplete suggestion returned might be user-A's account number. 

To reduce the likelihood of this kind of leak happening, the Gemini Enterprise administrator decides to: 

- Increase the value of the `queryFrequencyThreshold` parameter to `30` . In this case, it is very unlikely for one account number to be entered so often. However, popular search queries will be entered at least that often. 

- Increase the value of the `numUniqueUsersThreshold` parameter to `6` . The administrator thinks it unlikely for the same account number to be entered in the search bar in six search events each associated with a different `userPseudoId` . 

#### Procedure

There are two threshold parameters for autocomplete. These parameters aren't available on the Google Cloud console but can be set with a REST API call to the `updateCompletionConfig` (/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores/updateCompletio nConfig) 

method. 

**Note:** These parameters only apply to the search history and user events models. 

To configure the autocomplete threshold settings, follow these steps. Each step is optional, depending on the parameter you want to change. 

REST 

(#rest) 

1. Update the `CompletionConfig.queryFrequencyThreshold` field: 

```
curl -X PATCH \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \` 

```
 -H "X-Goog-User-Project: PROJECT_ID" \
https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/gl
obal/collections/default_collection/dataStores/DATA_STORE_ID/completionConfig?
updateMask=queryFrequencyThreshold \
 -d '{
   "name":
"projects/PROJECT_ID/locations/global/collections/default_collection/dataStores
/DATA_STORE_ID/completionConfig",
   "queryFrequencyThreshold":QUERY_FREQUENCY_THRESHOLD
 }'
```

Replace the following: 

_`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

- _`DATA_STORE_ID`_ : the ID of the data store that is associated with your app. 

- _`QUERY_FREQUENCY_THRESHOLD`_ : an integer value that indicates the minimum number of times that a search query must be entered before it can be returned as an autocomplete suggestion. The count is summed over a months-long, rolling, time window. The default is `8` . 

<sup>Example command and result</sup> 

`curl -X PATCH \` 

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \$ curl -X PATCH \` 

- `-H "X-Goog-User-Project: my-project-123" \t-access-token)" \ https://discoveryengine.googleapis.com/v1alpha/projects/my-project-` 

- `123/locations/global/collections/default_collection/dataStores/my-datastore/completionConfig?updateMask=queryFrequencyThreshold \ -d '{` 

```
 "name": "projects/my-project-
123/locations/global/collections/default_collection/dataStores/my-data-
store/completionConfig",
"queryFrequencyThreshold": 30
 }'
{
 "name":
"projects/123456/locations/global/collections/default_collection/dataStores/my-
data-store/completionConfig",
 "matchingOrder": "exact-prefix",
 "maxSuggestions": 20,
```

- `"minPrefixLength": 1,` 

```
 "queryModel": "automatic",
 "enableMode": "AUTOMATIC",
"queryFrequencyThreshold": 30
}
```

2. Update the `CompletionConfig.numUniqueUsersThreshold` field: 

```
curl -X PATCH \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \` 

- `-H "Content-Type: application/json" \` 

- `-H "X-Goog-User-Project:` _`PROJECT_ID`_ `" \` 

```
https://discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/gl
obal/collections/default_collection/dataStores/DATA_STORE_ID/completionConfig?
updateMask=numUniqueUsersThreshold \
```

- `-d '{` 

```
   "name":
"projects/PROJECT_ID/locations/global/collections/default_collection/dataStores
/DATA_STORE_ID/completionConfig",
   "numUniqueUsersThreshold":UNIQUE_USERS
 }'
```

Replace _`UNIQUE_USERS`_ with an integer value that represents the minimum number of unique users who must enter a given search query before it can be returned as an autocomplete suggestion. The count is summed over a months-long, rolling, time window. The default is `3` . 

<sup>Example command and result</sup> 

```
curl -X PATCH \
 -H "Authorization: Bearer $(gcloud auth print-access-token)" \
 -H "Content-Type: application/json" \
 -H "X-Goog-User-Project: my-project-123" \
 https://discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/dataStores/my-data-
store/completionConfig?updateMask=numUniqueUsersThreshold \
 -d '{
 "name": "projects/my-project-
123/locations/global/collections/default_collection/dataStores/my-data-
store/completionConfig",
"numUniqueUsersThreshold": 6
 }'
{
"name":
"projects/123456/locations/global/collections/default_collection/dataStores/my-
data-store/completionConfig",
 "matchingOrder": "exact-prefix",
 "maxSuggestions": 20,
 "minPrefixLength": 1,
 "queryModel": "automatic",
 "enableMode": "AUTOMATIC",
"numUniqueUsersThreshold": 6,
 "queryFrequencyThreshold": 30
}
```

### Update completable field annotations in schema

To turn on autocomplete for fields in structured data schema, follow these steps: 

Console 

(#console) 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/start) 

2. Click the name of the app that you want to edit. It must use structured data. 

3. Click **Data** . 

4. Click the **Schema** tab. 

5. Click **Edit** to select the schema fields to mark as `completable` . 

6. Click **Save** to save the updated field configurations. These suggestions take around a day to be generated and returned. 

### Send autocomplete requests

The following samples show how to send autocomplete requests. 

RESTC# (#c)Go (#go)Java (#java)Node.js (#node.js)Python (#python)Ruby (#ruby) (#rest) 

To send an autocomplete request using the API, follow these steps: 

1. Find your data store ID. If you already have your data store ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page and in the navigation menu, click **Data Stores** . 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

   - b. Click the name of your data store. 

   - c. On the **Data** page for your data store, get the data store ID. 

2. Call the `dataStores.completeQuery` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/completeQuery) method. 

```
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global
/collections/default_collection/dataStores/DATA_STORE_ID:completeQuery?
query=QUERY_STRING"
```

Replace the following: 

_`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

_`DATA_STORE_ID`_ : the ID of the data store that is associated with your app. 

_`QUERY_STRING`_ : the typeahead input used to fetch suggestions. 

#### Send an autocomplete request to a different model

To send an autocomplete request with a different query suggestions model, follow these steps: 

1. Find your data store ID. If you already have your data store ID, skip to the next step. 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page and in the navigation menu, click **Data Stores** . 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

      - b. Click the name of your data store. 

      - c. On the **Data** page for your data store, get the data store ID. 

2. Call the `dataStores.completeQuery` 

   - (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores/completeQuery) method. 

```
curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global
/collections/default_collection/dataStores/DATA_STORE_ID:completeQuery?
query=QUERY_STRING&query_model=QUERY_SUGGESTIONS_MODEL"
```

Replace the following: 

_`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

- _`DATA_STORE_ID`_ : the unique ID of the data store that is associated with your app. 

- _`QUERY_STRING`_ : the typeahead input used to fetch suggestions. 

- _`QUERY_SUGGESTIONS_MODEL`_ : the query suggestions model to use for the request: `document` , `document-completable` , `search-history` , or `user-event` . For healthcare data, use `healthcare-default` . 

### Use an autocomplete denylist

You can use a denylist to prevent specific terms from appearing as autocomplete suggestions. 

For example, take a pharmaceutical company. If a medication is no longer FDA-approved but is mentioned in documents in their data store, they might want to prevent that medication from appearing as a suggested query. The company could add the name of that medication to a denylist to prevent it from being suggested. 

The following limits apply: 

- One denylist per data store 

- Uploading a denylist overwrites any existing denylist for that data store 

- Up to 1000 terms per denylist 

- Terms are case-insensitive 

After importing a denylist, it takes 1-2 days to take effect 

Each entry of your denylist consists of a `blockPhrase` and `matchOperator` : 

- `blockPhrase` : Enter a string as your denylist term. Terms are case-insensitive. 

- `matchOperator` : Accepts the following values: 

   - `EXACT_MATCH` : Prevents an exact match of the denylist term from appearing as a suggested query. 

`CONTAINS` : Prevents any suggestion that contains the denylist term from appearing. 

The following is an example of a denylist with four entries: 

```
{
   "entries": [
       {"blockPhrase":"Oranges","matchOperator":"CONTAINS"},
       {"blockPhrase":"bAd apples","matchOperator":"EXACT_MATCH"},
       {"blockPhrase":"Cool as A Cucumber","matchOperator":"EXACT_MATCH"},
       {"blockPhrase":"cherry pick","matchOperator":"CONTAINS"}
   ]
}
```

Before importing a denylist, verify that the necessary access controls (/gemini/enterprise/docs/access-control) are set for Discovery Engine editor access. 

Denylists can be imported either from local JSON data (#denylist-local) or from Cloud Storage (#denylist-storage). To remove a denylist from a data store, purge the denylist (#denylist-purge). 

#### Import a denylist from local JSON data

To import a denylist from a local JSON file containing your denylist, do the following: 

1. Create your denylist in a local JSON file with the following format. Make sure each denylist entry is in a new line with no line breaks. 

```
{
   "inlineSource": {
       "entries": [
           { "blockPhrase":"TERM_1","matchOperator":"MATCH_OPERATOR_1" },
           { "blockPhrase":"TERM_2","matchOperator":"MATCH_OPERATOR_2" }
       ]
   }
}
```

2. Make a POST request to the `suggestionDenyListEntries:import` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.completionSuggestions/imp ort) 

method, providing the name of your JSON file. 

```
curl -X POST \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
   -H "Content-Type: application/json; charset=utf-8" \
   --data @DENYLIST_FILE \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataS
tores/DATA_STORE_ID/suggestionDenyListEntries:import"
```

Replace the following: 

_`DENYLIST_FILE`_ : the local path of the JSON file containing the denylist terms. 

- _`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

_`DATA_STORE_ID`_ : the ID of the data store that is associated with your app. 

After importing your denylist, it takes 1-2 days to start filtering suggestions. 

#### Import a denylist from Cloud Storage

To import a denylist from a JSON file in Cloud Storage, do the following: 

1. Create your denylist in a JSON file with the following format and import to a Cloud Storage bucket. Make sure each denylist entry is in a new line with no line breaks. 

```
{ "blockPhrase":"TERM_1","matchOperator":"MATCH_OPERATOR_1" }
{ "blockPhrase":"TERM_2","matchOperator":"MATCH_OPERATOR_2" }
```

2. Create a local JSON file containing the `gcsSource` 

(/gemini/enterprise/docs/reference/rest/v1/GcsSource) object. Use this to point to your denylist file's location in a Cloud Storage bucket. 

```
{
   "gcsSource": {
       "inputUris": [ "DENYLIST_STORAGE_LOCATION" ]
   }
}
```

Replace _`DENYLIST_STORAGE_LOCATION`_ with the location of your denylist in Cloud Storage. You can enter only one URI. The URI must be entered in this format: 

`gs://` _`BUCKET`_ `/` _`FILE_PATH`_ . 

3. Make a POST request to the `suggestionDenyListEntries:import` 

   - (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.completionSuggestions/imp ort) 

method, including the `gcsSource` object. 

```
curl -X POST \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
   -H "Content-Type: application/json; charset=utf-8" \
   --data @GCS_SOURCE_FILE\
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataS
tores/DATA_STORE_ID/suggestionDenyListEntries:import"
```

Replace the following: 

- _`GCS_SOURCE_FILE`_ : the local path of the file containing the `gcsSource` object that points to your denylist. 

_`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

- _`DATA_STORE_ID`_ : the ID of the data store that is associated with your app. 

After importing your denylist, it takes 1-2 days to start filtering suggestions. 

#### Purge a denylist

To purge a denylist from your data store, do the following: 

1. Make a POST request to the `suggestionDenyListEntries:purge` 

   - (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.completionSuggestions/purg e) 

method. 

```
curl -X POST \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataS
tores/DATA_STORE_ID/suggestionDenyListEntries:purge"
```

Replace the following: 

_`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

_`DATA_STORE_ID`_ : the ID of the data store that is associated with your app. 

### Use an imported list of autocomplete suggestions

You can choose to provide your own list of autocomplete suggestions instead of using autocomplete suggestions generated from an autocomplete data model. 

**Note:** Imported suggestions don't go through spell correction. However, the following processing is applied before serving: 

- **Text normalization.** Suggestion text is lowercased, Unicode-normalized, has internal whitespace collapsed, has curly apostrophes (U+2018, U+2019) folded to the ASCII apostrophe (U+0027), and has embedded double-quote characters and trailing periods removed. 

- **Length filtering.** Suggestions shorter than three characters or longer than 125 characters are dropped. 

- **Deduplication by score aggregation.** If two or more imported suggestions normalize to the same text (for example, `"Pixel 10 Pro Moonstone"` and `"Pixel 10 Pro moonstone"` , or `"jobseeker’s allowance"` with a curly apostrophe and `"jobseeker's allowance"` with an ASCII apostrophe), they are merged into a single suggestion whose score is the sum 

of the input scores. Submit each distinct suggestion only once if you want its score preserved as-is. 

- **PII filtering.** Suggestions identified as containing personally identifiable information are filtered out. 

- **Denylist filtering.** Suggestions matching phrases in the data store's suggestion denylist (#denylist) are filtered out. 

SafeSearch (/generative-ai-app-builder/docs/responsible-ai) is not applied to imported suggestions; it is your responsibility to ensure imported suggestions are appropriate for your users. 

For most applications, using generated suggestions from one of autocomplete data models yields better results. However, there might be some rare situations where the model's suggestions don't match your needs and providing a discrete list of suggestions gives your users a better autocomplete experience. 

For example, a small online bookstore imports their list of book titles as the autocomplete suggestions. When a customer begins to type in the search bar, the autocomplete suggestion will always be a book title from the imported list. When the list of books changes, the bookstore purges the current list and imports the new list. An excerpt from the list might look something like: 

```
{"suggestion": "Wuthering Heights", "globalScore": "0.52" },
{"suggestion": "The Time Machine", "globalScore": "0.26" },
{"suggestion": "Nicholas Nickleby", "globalScore": "0.38" },
{"suggestion": "A Little Princess", "globalScore": "0.71" },
{"suggestion": "The Scarlet Letter", "globalScore": "0.32" }
```

The `globalScore` is a floating point number in the range [0, 1] that's used to rank the suggestion. Alternatively, you can use a `frequency` score which is an integer greater than one. The `frequency` score is used to rank suggestions when the `globalScore` is not available (set as null). 

**Note:** Even though in the data, you could just provide one score (either **`globalScore`** or **`frequency`** ), in the following steps to create a BigQuery table, both **`globalScore`** and **`frequency`** is a must-have in the schema. Incorrect schema will lead to suggestions importation failure. 

#### Before you begin

To import autocomplete suggestions, you need the **Discovery Engine Admin** IAM role, which includes the `discoveryengine.completionSuggestions.import` permission. 

For more information, see IAM roles and permissions (/gemini/enterprise/docs/access-control). 

#### Set up and import autocomplete suggestions

To set up and import a list of autocomplete suggestions from a BigQuery, follow these steps: 

1. Create your list of suggestions and load it into a BigQuery table. 

At minimum you need to provide each suggestion as a string and either a global score or a frequency. 

Use the following table schema for your list of suggestions: 

```
[
 {
   "description": "The suggestion text",
   "mode": "REQUIRED",
   "name": "suggestion",
   "type": "STRING"
 },
 {
   "description": "Global score of this suggestion. Control how this suggestion
would be scored and ranked. Set global score or frequency; not both.",
   "mode": "NULLABLE",
   "name": "globalScore",
   "type": "FLOAT"
 },
 {
   "description": "Frequency of this suggestion. Used to rank suggestions when the
global score is not available.",
   "mode": "NULLABLE",
   "name": "frequency",
   "type": "INTEGER"
 }
]
```

See the BigQuery documentation (/bigquery/docs/loading-data) for instructions on how to create a BigQuery table (/bigquery/docs/tables#creating_an_empty_table_with_a_schema_definition) and load the table (/bigquery/docs/loading-data) with your autocomplete suggestion list. 

2. Import the list from BigQuery. 

Make a POST request to the `completionSuggestions:import` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.completionSuggestions/imp ort) 

method, including the `bigquerySource` object. 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataS
tores/DATA_STORE_ID/completionSuggestions:import" \
-d '{
     "bigquery_source": {"project_id": "PROJECT_ID_SOURCE", "dataset_id":
"DATASET_ID", "table_id": "TABLE_ID"}
}'
```

Replace the following: 

- _`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

- _`DATA_STORE_ID`_ : the ID of the data store. 

- _`PROJECT_ID_SOURCE`_ : the project that contains the dataset that you want to import. 

- _`DATASET_ID`_ : the dataset ID for the suggestion list that you want to import 

- _`TABLE_ID`_ : the table ID for the suggestion list that you want to import 

<sup>Example command and result</sup> 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-H "X-Goog-User-Project: my-project-123" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/dataStores/my-data-store/completionSuggestions:import" \
-d '{
"bigquery_source": {"project_id": "my-project-123", "dataset_id": "autocomplete",
"table_id": "import_suggestion2"}
}'
{
 "name":
"projects/123456/locations/global/collections/default_collection/dataStores/my-data-
store/operations/import-completion-suggestion-7659310803143180509",
 "metadata": {
   "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.ImportCompletionSuggestionsMetad
ata"
 }
}
```

3. Optional: Make note of the `name` value returned, and follow the instructions in Get details about a long-running operation (/gemini/enterprise/docs/long-running-operations#get-details) to see when the import operation is complete. 

4. If you haven't enabled autocomplete for the app, follow the procedure Update autocomplete settings (#update-autocomplete). Make sure to set **Enable autocomplete** to **Now** . 

5. Wait a couple of days for indexing to complete and the imported suggestions to become available. 

#### Send an autocomplete request

To send an autocomplete request that returns an imported suggestion instead of a suggestion from an autocomplete model: 

1. Follow the procedure to send an autocomplete request to a diferent modelf 

   - (#send_autocomplete_requests) and set _`QUERY_SUGGESTIONS_MODEL`_ to `imported-suggestion` . 

<sup>Example command and result</sup> 

```
curl -X GET \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
   -H "X-Goog-User-Project: my-project-123" \
   "https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/collections/default_collection/dataStores/my-data-
store:completeQuery?query=t&query_model=imported-suggestion"
Response:
{
 "querySuggestions": [
   {
     "suggestion": "The Time Machine"
   },
   {
     "suggestion": "The Scarlet Letter"
   }
 ]
}
```

#### Purge the list of imported autocomplete suggestions

Before importing a new list of autocomplete suggestions, remove the existing one. 

To purge an existing list of autocomplete suggestions, follow this step: 

1. Make a POST request to the `completionSuggestions:purge` 

   - (/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.completionSuggestions/purg e) 

method. 

```
curl -X POST \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/dataS
tores/DATA_STORE_ID/completionSuggestions:purge"
```

Replace the following: 

_`PROJECT_ID`_ : the number or ID of your Google Cloud project. 

_`DATA_STORE_ID`_ : the ID of the data store that is associated with your app. 

<sup>Example command and result</sup> 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json; charset=utf-8" \
-H "X-Goog-User-Project: my-project-123" \
"https://discoveryengine.googleapis.com/v1/projects/my-project-
123/locations/global/dataStores/my-data-store/completionSuggestions:purge"
{
 "name":
"projects/123456/locations/global/collections/default_collection/dataStores/my-data-
store/operations/purge-customer-imported_suggestions-3197526711414652502",
 "metadata": {
   "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.PurgeCompletionSuggestionsMetada
ta",
   "createTime": "2024-06-27T17:07:09.551726728Z",
   "updateTime": "2024-06-27T17:07:09.551726728Z"
 }
}
```

2. Optional: Make note of the `name` value returned, and follow the instructions in Get details about a long-running operation (/gemini/enterprise/docs/long-running-operations#get-details) to see when the purge operation is complete. 

### Advanced document data model

**Experimental** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

Gemini Enterprise provides an advanced data model for autocomplete. Based on the documents you import, this data model generates high-quality autocomplete suggestions by leveraging Google large language models (LLMs). 

This feature is experimental. If you're interested in using this feature, contact your Google Cloud account team and ask to be added to the allowlist. 

The advanced document data model is not available for healthcare search or in the US and EU multi-regions. 

Last updated 2026-10-14 UTC.
