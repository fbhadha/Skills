# Gemini Enterprise: platform, security, agents, cost, monitoring / Configure the mobile app to Access connector error logs
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 695-734, extracted 2026-10-18

Contains:
- Configure the mobile app (pages 695-701) https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app
- View analytics data (pages 702-723) https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics
- Monitor long-running operations (pages 724-729) https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations
- Access connector error logs (pages 730-734) https://docs.cloud.google.com/gemini/enterprise/docs/cloud-logging

## Configure the mobile app

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app

This page explains how to configure the Gemini Enterprise mobile app on user devices. Gemini Enterprise app administrator can choose to configure access for users using one of three available methods. 

### Overview

As a Gemini Enterprise administrator, you can configure the mobile app for users with one of three methods: 

- You can use a Mobile Device Management (MDM) solution (#mdm-solution) to remotely install and configure the app on user devices. MDM solutions allow admins to complete set up steps prior to delivering apps to users. 

- You can enable a QR code (#enable-qr-code) within the Gemini Enterprise web app. Users can then configure the mobile app by scanning this QR code. QR codes can simplify the distribution of access to users and can be used in addition to MDM solutions. 

- You can generate an access link (#generate-access-link) and distribute it to users, which lets them configure the app by opening the link on their mobile devices. 

**Note:** MDM configuration overrides all other configuration methods. If you have configured an MDM solution on a device, it takes priority and overrides any attempt by a user to _configure_ the app using a QR code or an access link. In this case, the app displays a message indicating that the configuration is managed. 

The following sections describe the steps required by each method. 

### Before you begin

Before you configure the app for users, set up an identity provider for your Gemini Enterprise organization. The Gemini Enterprise mobile app supports the use of 

Google Identity and third-party identity providers. For more information, see Configure identity provider (/gemini/enterprise/docs/configure-identity-provider). 

**Note:** Signing in with multiple identity providers on a single device can cause authentication conflicts, resulting in an "Incomplete sign-in details" error. If a user encounters this message, they can resolve it by signing out and signing in again. 

### Use a Mobile Device Management (MDM) solution

The Gemini Enterprise administrator panel provides an app URL that contains the parameters required to configure the mobile app in your MDM solution. These parameters map directly to `AppConfig` parameters in the **AppConfig standard** and can be used to configure the app, and enforce security policies. 

The following steps use Google Endpoint Management (GEM) as an example of configuring an MDM, but the `AppConfig` parameters should be applicable to other MDM solutions. These steps require access to your MDM administrator console. If you don't have access, contact your organization administrator for next steps. 

To configure the app for users in the GEM MDM management solution: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click your app. The **Overview** page displays. 

3. Click **Copy URL** to copy the mobile link. The format of the mobile link differs based on your identity provider. 

Google IdentityThird-party identity provid… (#google-identity) 

If your Gemini Enterprise app uses Google as an identity provider, the mobile app URL looks like this: 

```
https://vertexaisearch.cloud.google.com/mobile?
cid=123&cid_location=global
```

4. Extract the parameters from the app URL, and use them to fill in the app configuration in your MDM administrator console: 

|Google Identity<br> (#google-identity<br>Third-|)<br>party identity provid…|||
|---|---|---|---|
|Deeplink parameter|MDM configuration<br>key|MDM configuration<br>name|Example value|
|`cid`|`config_id`|Configuration ID|`123`|
|`cid_location`|`location`|Location|`global`|

Leave all other fields empty. 

**Note:** When you configure the Android app in Google Endpoint Management (GEM), use the _MDM configuration name_ in the managed configuration form. However, for iOS, manually enter the _MDM configuration key_ with its corresponding value. 

For example, the following XML configures an iOS application in GEM: 

```
<dict>
  <key>config_id</key>
  <string>123</string>
  <key>location</key>
  <string>global</string>
</dict>
```

#### Configure citation browser preferences

Gemini Enterprise administrators can use MDM configuration keys to specify how citations and web pages open from Gemini Enterprise mobile sessions. 

**Open citations in the default browser** 

To open citations in the system's default browser using MDM, set the following MDM configuration key: 

```
url_launch_mode = external_browser
```

**Open citations in a specific browser** 

To force citations to open in a specific browser using MDM, set an additional MDM configuration key: 

```
url_launch_mode = external_browser, preferred_browser = chrome (or edge,
or firefox)
```

**Note:** If the specified browser is not installed on the user's device, the citation will automatically open in the system's default browser instead. 

### Enable a QR code on the web app homepage

As a Gemini Enterprise administrator, you can display a QR code on the web app homepage, which allows users to configure the mobile app on their devices by scanning the QR code using their device's camera. This serves as a simpler way to distribute the access link to users. 

To manage the configuration QR code visibility: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to configure. 

3. Click **Configurations** and then click the **Feature Management** tab. 

4. Turn on or turn off the **Enable mobile app access** toggle to display or hide the QR code on the web app user's home page. 

After the QR code is enabled, users can scan the QR code displayed on their Gemini Enterprise web app using their mobile device to configure and connect the mobile app. 

**Note:** If MDM is configured on the user's device, the MDM configuration overrides the QR code setup and displays a message indicating that the configuration is managed. 

To view the QR code on the web app to set up the mobile app: 

1. Open your Gemini Enterprise web app. 

2. Click **Settings & help** . 

3. Click **Mobile login** . 

4. Scan the QR code with your mobile device to sign in to the Gemini Enterprise mobile app. 

### Generate an access link

To generate the access link for distribution to Gemini Enterprise mobile app users, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click your app. The **Overview** page displays. 

3. Click **Copy URL** to copy the mobile link. You can then distribute the link to users. The format of the mobile link differs based on your identity provider. 

Google IdentityThird-party identity provid… (#google-identity) 

If your Gemini Enterprise uses Google as an identity provider, the mobile app URL looks like this: 

```
https://vertexaisearch.cloud.google.com/mobile?
cid=123&cid_location=global
```

**Note:** If MDM is configured on the user's device, the MDM configuration overrides the access link setup and displays a message indicating that the configuration is managed. 

#### Configure citation browser preferences

Gemini Enterprise administrators can use access link parameters to specify how citations and web pages open from Gemini Enterprise mobile sessions. 

**Open citations in the default browser** 

To open citations in the system's default browser with an access link, pass the following parameter in the URL: 

```
url_launch_mode=external_browser
```

**Open citations in a specific browser** 

To force citations to open in a specific browser with an access link, pass set an additional parameter in the URL: 

```
url_launch_mode=external_browser, preferred_browser=chrome (or edge, or
firefox)
```

For example: 

```
https://vertexaisearch.cloud.google.com/mobile?
cid=123&cid_location=global&url_launch_mode=external_browser&preferred_bro
```

**Note:** If the specified browser is not installed on the user's device, the citation will automatically open in the system's default browser instead. 

Last updated 2026-10-14 UTC. 



## View analytics data

URL: https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics

Analytics give you insight into the usage trends, search quality, and end-user engagement of your app. The console provides an interactive dashboard experience powered by Looker. This page describes how to view analytics for your apps. 

**Note:** Metrics are refreshed about every 6 hours, so it can take several hours before you can use the **Analytics** page after you create your app. 

### Before you begin

Ensure your app is connected to a data store. App metrics are only available from the time a data store is linked to an app. 

If you don't have a data store, you need to connect a Google data source (/gemini/enterprise/docs/create-data-store) or a third-party data source (/gemini/enterprise/docs/connect-third-party-data-source) to your app. 

**Warning:** Some app metrics could be lost if a data store is unlinked from the app. If your data is encrypted using CMEK, these specific app metrics cannot be retrieved. 

### User events for analytics

This section describes the user events Gemini Enterprise uses to generate the search-related metrics, such as search count and click-through-rate. No additional configurations are needed if you are using the user interface to search and get answers through the Gemini Enterprise assistant. However, if you use the Gemini Enterprise APIs in your own apps, you must configure the search in your app to capture the user events (/gemini/enterprise/docs/user-events) and then import user events to your app.. 

Gemini Enterprise apps require the following user events to get the metrics: 

- **Search events.** Required for click-through-rate. 

- **View-item events.** Required for click-through-rate. 

The following information is also used for some analytics: 

- **Impressions** . You can provide impressions (item views or clicks) that are attributable to Google by including the associated item in 

- `UserEvent.Documents` when ingesting user events. This information is needed for attribution and to compute per-search metrics. 

- **Attribution tokens** . Attribution tokens are unique IDs generated by Google and returned with each search request. Make sure to include that attribution token as `UserEvent.attributionToken` with any user events resulting from a search. This is needed to identify if a search is served by the API. Only user events with a Google-generated attribution token are used to compute metrics. 

- **Search logs** . Search logs are based on search requests. To allow Google to identify user sessions so that it can deliver per-session analytics and higher quality search results, Google strongly recommends that you set the optional field `SearchRequest.UserPseudoId` . 

If there are no search logs or user events, default values are shown for all metrics. 

### View Gemini Enterprise analytics

**Note:** For apps in US and EU multi-regions, viewing search analytics is in Public preview. Search analytics are GA for global apps. 

You can view search analytics for your app. You see the metrics related to the search calls made to your app. If your app is connected to multiple data stores, then making search calls to the app by specifying the `engine` resource is recommended so that you can get results from across all its connected data stores. 

Use the following instructions to view analytics about your app. 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to view analytics for. 

3. Click **Analytics** . 

4. Click a tab to view that metric group: 

   - **Adoption** : Metrics on user adoption status. 

   - **Usage and Quality** : Metrics on user feedback and app usage. 

   - **Agent** : Metrics for agents in the Gemini Enterprise web app, including Google-made agents, Gemini Notebook Enterprise, and agents your organization created and registered with Gemini Enterprise. 

   - **Value** : Metrics on cost savings achieved by users querying data with the app. 

   - **User Level** : Metrics include the user IDs (email address or unique identifier) of users in the organization and their interactions with Googlemade agents and agents the organization created and registered with Gemini Enterprise. 

**Note:** You must be on an allowlist to see data on the **User Level** tab. To be added to the allowlist, contact your account team (https://cloud.google.com/tam) or the sales team (https://cloud.google.com/contact). 

_See the analytics data for adoption_ 

5. To filter your metrics, specify the filters available for the metric tab and then click the **Refresh** button to apply them. 

### Metrics definitions

The following table describes how metrics are defined. 

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
|Adoption|Total users|Number of unique active<br>users of Gemini Enterprise<br>during the selected date<br>range.|A user is considered active if<br>they sign in and trigger any API<br>calls, such as when landing on<br>the home page. Because the<br>count is unique, a user who calls<br>the assistant, answer, and<br>search API methods is counted<br>only once in the total.|
||Users calling<br>assistant|Number of users who called<br>the`AssistantService`<br>methods or used the<br>Assistant to generate<br>answers.||
||Users calling<br>answer|Number of users who called<br>the`ConversationalSearch`<br>`Service`and`Generative`<br>`SearchAnswerService`<br>methods to generate<br>answers.||
||Users calling<br>search|Number of users who called<br>the`SearchService`<br>methods to get search<br>results.||
||Users calling other<br>API methods|<br>Number of users who called<br>API methods other than<br>`streamAssist`,`stream`<br>`Answer`, and`engines.`<br>`servingConfigs.search`.<br>For example, users who call<br>the authentication API<br>methods.||
||Daily active users|Count of active users per<br>day|A user is considered active if<br>they sign in and trigger any API<br>calls, such as when landing on<br>the home page.|

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
||Weekly active<br>users|Count of active users per<br>week. The week starts on<br>Monday and ends on<br>Sunday.||
||Monthly active<br>users|Count of active users per<br>month||
||7d retention rate|Count of returned user in<br>the current 7-day period /<br>count of active user in the<br>previous 7-day period|A user is considered as a<br>returned user if the user is active<br>during the current 7-day period<br>and the previous 7-day period.|
||7d growth rate|The percentage difference<br>between the number of<br>active users in the current<br>seven-day period and the<br>previous seven-day period||
||7d churn rate|Count of churned users in<br>the current 7-day period /<br>count of active user in the<br>previous 7-day period|A user is considered churned if<br>the user was active in the<br>previous 7-day period, but is not<br>active in the current 7-day<br>period.|
||28d retention rate|Count of returned user in<br>the current 28-day period /<br>count of active user in the<br>previous 28-day period||
||28d growth rate|The percentage difference<br>between the number of<br>active users in the current<br>28-day period and the<br>previous 28-day period||
||28d churn rate|Count of churned users in<br>the current 28-day period /<br>count of active users in the<br>previous 28-day period||

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
||Seats purchased|The number of licenses<br>(seats) the organization h<br>purchased|as<br>Includes all seats purchased<br>since registering with Gemini<br>Enterprise.|
||Seats claimed|The number of user licens<br>that have been assigned t<br>and accepted by individua<br>within your organization|es<br>o<br>ls<br>Includes all seats claimed since<br>registering with Gemini<br>Enterprise.|

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
|Usage and<br>quality|Search count|Total number of search<br>queries by users to Gemini<br>Enterprise.||
||Answer count|Total number of times<br>Gemini Enterprise has<br>generated an answer to a<br>user's query.|Answers generated by an agent<br>are not included in this count.|
||Action count|Total interactions, such as<br>uploading files, creating<br>folders, or using connector<br>actions in Gemini<br>Enterprise.|Includes actions such as creating<br>an email template.|
||Click-through rate<br>(CTR) per search|Total number of search<br>clicks / search count|Search clicks include clicks on<br>search results and internal<br>references.|
||Page view per<br>category|Total number of view for<br>each category page||
||Feedback like and<br>dislike count|Count of likes and dislikes<br>sent by users|A record of the thumbs-<br>up/thumbs-down feedback<br>responses sent by the app's<br>users.|
||Feedback dislike<br>reasons<br>breakdown|Percentage of the dislike<br>reasons|When a user dislikes a generated<br>answer, they can select multiple<br>reasons to explain their dislike.<br>The percentage shows how often<br>each reason was selected.|
||Successful search<br>rate|Successful search count /<br>search count||
||Successful answer<br>rate|Successful answer count /<br>answer count||

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
|Agents|Monthly active<br>agent users|Total number of active user<br>who used the agent per<br>month.|s<br>A user is counted as active for an<br>agent whenever they make an<br>Assistant call to that agent in<br>agent, research, or idea forge<br>mode. This includes activity from<br>the agent's creator during<br>previews or testing in Workflow<br>Builder, because these actions<br>generate regular Assistant calls<br>with the agent's ID, similar to<br>any end-user interaction. Only<br>interactions with unsaved drafts<br>that haven't been assigned an<br>agent ID are excluded from this<br>count.|
||Monthly agent<br>chat sessions|Total number of chat<br>sessions initiated by the<br>users interacting with a<br>specific agent per month.|A chat session is defined as a<br>user interacting with an agent<br>within the same chat thread on a<br>single day. If the user continues<br>the conversation in the same<br>chat thread on a subsequent<br>day, it will be considered a new<br>session. Preview and test<br>sessions initiated from Workflow<br>Builder are counted, because<br>they flow through the same<br>Assistant API path as end-user<br>sessions and receive a session<br>ID.|

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
||Monthly agents<br>used|Total number of agents that<br>had at least one active user<br>per month.|Uses the same definition of<br>active user as Monthly active<br>agent users. This count can<br>occasionally exceed Monthly<br>total chat sessions in a given<br>month when many agents<br>receive short-lived Assistant calls<br>that don't produce a persisted<br>session ID (for example, aborted<br>or cancelled turns, or single-shot<br>calls that don't open a chat<br>session).|
||Monthly total chat<br>sessions|Total number of chat<br>sessions initiated by the<br>users interacting with the<br>agents per month.|A chat session is defined as a<br>user interacting with an agent<br>within the same chat thread on a<br>single day. If the user continues<br>the conversation in the same<br>chat thread on a subsequent<br>day, it will be considered a new<br>session. Preview and test<br>sessions initiated from Workflow<br>Builder are counted, because<br>they flow through the same<br>Assistant API path as end-user<br>sessions and receive a session<br>ID.|
||Monthly agents<br>created|Total number of Agents that<br>were created in the last<br>calendar month.||

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
||Gemini Notebook<br>Enterprise daily<br>active users|Count of Gemini Notebook<br>Enterprise active users per<br>day.|Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|
||||Note: The Gemini Notebook<br>Enterprise metrics include<br>notebook creation, notebook<br>sharing, audio overview<br>creation, and overall active<br>user counts. Metrics for other<br>generated artifacts — like mind<br>maps, video overviews, slide<br>decks, infographics, and<br>tailored reports — are not yet<br>displayed on this dashboard.|
||Gemini Notebook<br>Enterprise daily<br>notebooks created|<br>Count of Gemini Notebook<br>Enterprise notebooks<br>created per day.|Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|
||Gemini Notebook<br>Enterprise daily<br>notebooks created<br>per user|<br>Count of Gemini Notebook<br>Enterprise notebooks<br>created per user per day.|Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|
||Gemini Notebook<br>Enterprise daily<br>notebooks shared|Count of Gemini Notebook<br>Enterprise notebooks share<br>per day.|d<br>Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|
||Gemini Notebook<br>Enterprise daily<br>audio overviews<br>created|Count of Gemini Notebook<br>Enterprise audio overviews<br>created per day.|Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|
||Gemini Notebook<br>Enterprise monthly<br>active users|<br>Count of Gemini Notebook<br>Enterprise active users per<br>month.|Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|
||Gemini Notebook<br>Enterprise monthly<br>notebooks created|<br> <br>Count of Gemini Notebook<br>Enterprise notebooks<br>created per month.|Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
||Gemini Notebook<br>Enterprise monthl<br>notebooks created<br>per user|y<br> <br>Average count of Gemini<br>Notebook Enterprise<br>notebooks created per user<br>per month.|Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|
||Gemini Notebook<br>Enterprise monthl<br>notebooks shared|y<br>Count of Gemini Notebook<br>Enterprise notebooks share<br>per month.|d<br>Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|
||Gemini Notebook<br>Enterprise monthl<br>audio overviews<br>created|y<br>Count of Gemini Notebook<br>Enterprise audio overviews<br>created per month.|Gemini Notebook Enterprise<br>metrics are calculated across the<br>project and not per engine.|

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
|Value<br>(public<br>preview)|Successful search <br>Successful answer|Count of successful<br>searches.<br> Count of successful answers|The number of successful<br>searches are determined by the<br>user behavior after a search. A<br>search is considered successful if<br>one of the following occurs:<br>If a search result is clicked<br>before a new search is<br>initiated.<br>If the response from a search<br>includes a people search<br>result, and isn't followed by<br>another search within two<br>minutes. This is because<br>people-search results are<br>displayed on the search result<br>page and don't typically<br>require a click.<br>An answer's success is<br>determined by user behavior<br>after it is generated. Success is<br>measured by feedback provided<br>or how soon a follow up question<br>was asked.<br>If the user thumbs-up the<br>answer, the query is<br>considered successful.<br>If there is no feedback and the<br>user does not ask another<br>query within 30 seconds, the<br>query is assumed to be<br>successful.|
||Employee hours<br>saved for selected<br>dates|(Successful search count +<br>Successful answer count) x<br>Minutes saved per<br>successful answer||
||Value saved for<br>selected dates|Hours saved within the<br>dates selected ✕ Average<br>employee hourly rate|To view this metric, in the Value<br>tab, specify an hourly rate for<br>the Employee Hourly Rate field.|

|Metric group|Metric name|Metric definition|Notes|
|---|---|---|---|
||Projected annual<br>employee hours<br>saved|(Successful search count +<br>Successful answer count) x<br>Minutes saved per<br>successful search|The projected annual successful<br>search count is derived from the<br>successful search count within<br>the chosen date range. Each<br>query is estimated to save three<br>minutes, an estimate based on<br>Google's internal research.|
||Projected annual<br>value saved|Projected annual employee<br>hours saved ✕ Average<br>employee hourly rate|To view this metric, in the Value<br>tab, specify an hourly rate for<br>the Employee Hourly Rate field.|

|Metric group|Metric name|Metric definition<br>Notes|
|---|---|---|
|User Level|Note: You must<br>to the allowlist,<br>the<br>sales team|be on the allowlist to see the User Level metrics. To be added<br>contact your<br>account team(https://cloud.google.com/tam) or<br>(https://cloud.google.com/contact).|
||User ID|The email address of each<br>user within your<br>organization. If the email<br>address isn't available, the<br>user's original unique<br>identifier is displayed.|
||Total messages|The total number of<br>messages a user sent to the<br>Gemini Enterprise web app.<br>Includes all messages that the<br>user sent and isn't limited to<br>conversations with Gemini<br>Enterprise agents.|
||Messages to<br>Google-made<br>agents|The total number of<br>messages a user has sent to<br>Google-made agents within<br>the selected date and time<br>range.|
||Messages to our<br>agents|The total number of<br>messages a user has sent to<br>agents that were created by<br>the organization and<br>registered with Gemini<br>Enterprise within the<br>selected date and time<br>range.|

### Export metrics

Follow these steps to export the metrics to a BigQuery table in your Google Cloud project: 

1. Verify that you have the required permissions and roles. 

You need to have the Discovery Engine Viewer 

- (/gemini/enterprise/docs/access-control#discoveryengine.viewer) role to be able to call the API. 

- Required permissions to create a BigQuery dataset 

- (/bigquery/docs/datasets#required_permissions) 

Required permissions to create a table 

      - (/bigquery/docs/tables#required_permissions). 

2. Create a BigQuery dataset: 

   - a. Open the BigQuery page in the Google Cloud console. 

Go to the BigQuery page (https://console.cloud.google.com/bigquery) 

- b. In the **Explorer** panel, select the same project that your Gemini Enterprise app is in to create the dataset. 

- c. Click the option and click **Create dataset** . 

- d. On the **Create dataset** page: 

   - For **Dataset ID** , enter a unique dataset name 

   - (/bigquery/docs/datasets#dataset-naming). You need the dataset name to export the metrics through the API. 

   - For **Location type** , the following table shows you how to map the BigQuery locations to the Gemini Enterprise app locations: 

**Note:** After a dataset is created, the location can't be changed. 

|Gemini Enterprise app multi-region<br>location|BigQuery multi-region location|
|---|---|
|Global|US (multiple regions in United States)|
|US (multiple regions in United States)|US (multiple regions in United States)|
|EU (multiple regions in the Europe<br>Union)|EU (multiple regions in the Europe<br>Union)|

- e. Click **Create dataset** . 

3. Create an empty BigQuery table for the dataset you created. 

   - a. In the **Explorer** panel, expand your project, and then select the dataset you created. 

   - b. In the **Dataset info** section, click **Create table** . 

   - c. In the **Create table** panel, specify a name for your table in the **Table** field. You need the table name to export the metrics through the API. 

   - d. Click **Create table** . 

4. Call the `analytics:exportMetrics` 

(/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.an alytics/exportMetrics) 

method to retrieve metrics data for the past 30 days, which includes the current day. 

**Note:** You can only call the **`analytics:exportMetrics`** method 5 times per day for a Google Cloud project, and 25 times per day for a Google Cloud organization (https://support.google.com/googleapi/answer/7053550). 

REST 

(#rest) `curl -X POST \ -H "Authorization: Bearer $(gcloud auth print-access-token)" \ -H "Content-Type: application/json" \ -H "X-Goog-User-Project:` _`PROJECT_ID`_ `" \ -d '{ "analytics": "projects/` _`PROJECT_ID`_ `/locations/` _`LOCATION`_ `/collections/default_collectio` `n/engines/` _`APP_ID`_ `", "outputConfig": { "bigqueryDestination": { "datasetId": "` _`BIGQUERY_DATASET_ID`_ `", "tableId": "` _`BIGQUERY_TABLE_ID`_ `" } }` 

```
  }' \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/
LOCATION/collections/default_collection/engines/APP_ID/analytics:expo
rtMetrics"
```

Replace the following: 

_`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

- `us` for the US multi-region 

- `eu` for the EU multi-region 

- `global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multiregion_for_your_data_store) 

- _`LOCATION`_ : the multi-region of your data store: `global` , `us` , or `eu` 

- _`PROJECT_ID`_ : the ID of your Google Cloud project. 

- _`APP_ID`_ : the ID of the app that you want to export metrics from. 

- _`BIGQUERY_DATASET_ID`_ : the ID of the BigQuery dataset you created. The dataset ID follows the `<PROJECT_ID>.<DATASET_ID>` format. You only need to provide the `<DATASET_ID>` . 

_`BIGQUERY_TABLE_ID`_ : the ID of the BigQuery table you created. In the **Classic explorer** view, the table ID follows the `<PROJECT_ID>.<DATASET_ID>.<TABLE_ID>` format. You only need to provide the `<TABLE_ID>` . 

**Note:** If you want to export metrics data again and retain the previously exported data, create a new BigQuery table and update the **_`BIGQUERY_TABLE_ID`_** before calling the **`analytics:exportMetrics`** method. 

The response includes the operation name and ID. Note the operation ID to use in the next step. 

For example: 

```
{
  "name": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/operations/OPERATION_ID",
  "metadata": {
     "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.ExportMetri
csMetadata"
  }
}
```

<sup>Example command and result</sup> 

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: my-project-123" \
-d '{
  "analytics": "projects/my-project-
123/locations/global/collections/default_collection/engines/my-app",
  "outputConfig":
     {
        "bigqueryDestination":
        {
           "datasetId": "123456789012345678901",
           "tableId": "123456789012345678901"
        }
     }
  }' \
"https://discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global/collections/default_collection/engines/my-
app/analytics:exportMetrics"
{
 "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/operations/export-metrics-123456789012345678901",
 "metadata": {
   "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.ExportMetri
csMetadata"
 }
}
```

5. To see the status of the export metrics operation, call the 

   - `engines.operations.get` 

(/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.op erations/get) 

method: 

REST (#rest) 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-
"https://ENDPOINT_LOCATION
discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/
LOCATION/collections/default_collection/engines/APP_ID/operations/
OPERATION_ID"
```

Replace the following: 

_`ENDPOINT_LOCATION`_ : the multi-region for your API request. Specify one of the following values: 

`us` for the US multi-region 

`eu` for the EU multi-region 

- `global` for the Global location 

For more information, see Specify a multi-region for your data store (/gemini/enterprise/docs/locations#specify_a_multiregion_for_your_data_store) 

- _`LOCATION`_ : the multi-region of your data store: `global` , `us` , or `eu` 

- _`APP_ID`_ : the ID of the app that you want to get the long running operations of. 

- _`OPERATION_ID`_ : the ID of the export metrics operation that was returned in the response when you ran the command to export the metrics. 

<sup>Example command and result</sup> 

Example command: 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1alpha/projects/my-project-
123/locations/global
/collections/default_collection/engines/my-app/operations/export-
metrics-123456789012345678901"
```

Example response when an operation completes successfully: 

```
{
 "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/operations/export-metrics-123456789012345678901",
 "metadata": {
   "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.ExportMetri
csMetadata",
   "createTime": "2025-09-17T20:04:30.449781Z",
   "updateTime": "2025-09-17T20:04:35.089617Z"
 },
 "done": true,
 "response": {
   "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.ExportMetri
csResponse"
 }
}
```

Example response when an operation encounters errors: 

```
{
 "name":
"projects/123456/locations/global/collections/default_collection/engi
nes/my-app/operations/export-metrics-123456789012345678901",
 "metadata": {
   "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.ExportMetri
csMetadata",
   "createTime": "2025-09-17T20:04:30.449781Z",
   "updateTime": "2025-09-17T20:04:35.089617Z"
 },
 "done": true,
 "error": {
   "code": 3,
   "message": "BigQuery job failed with error: Not found: Dataset
my-project-123:123456789012345678901 was not found in location US at
[1:24]"
 }
}
```

Last updated 2026-10-14 UTC. 



## Monitor long-running operations

URL: https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations

This page describes how to manage the lifecycle of a long-running operation (LRO) in Gemini Enterprise. 

A long-running operation (https://google.aip.dev/151) object is returned when a call to a method might take a long time to complete. For example, the Gemini Enterprise API creates a long-running operation when you call `documents.import` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.d ocuments/import) 

through the API or Client Libraries. The operation tracks the status of the processing job. 

You can use the long-running operations methods that the Gemini Enterprise API provides to check the status (https://google.aip.dev/216#common-states) of the operations. You can also list or poll operations. 

The record of an operation is kept for approximately 30 days after the operation finishes, meaning that you can't view or list an operation after that time. 

### List long-running operations

The following show how to list the operations for a Google Cloud resource. 

**Note:** Long running operations can't be filtered or paginated in Gemini Enterprise. That is, when you call the **`operations.list`** method, you can't use the **`filter`** , **`pageSize`** , or **`pageToken`** fields. 

RESTPython (#python) (#rest) 

To list the long-running operations for a Google Cloud resource, follow this step: 

Call the `operations.list` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStore s.branches.operations/list) 

method: 

```
curl -X GET \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locati
ons/global/collections/default_collection/dataStores/DATA_STORE_ID/op
erations"
```

_`DATA_STORE_ID`_ : The ID of the Gemini Enterprise data store that was created with your engine. In the Google Cloud console URL, the data store ID appears after `engines/` and before `/data` . 

### Get details about a long-running operation

The following show how to get details about an operation. 

RESTPython (#python) (#rest) 

To get the status of and view details about a long-running operation, follow these steps: 

1. Find the name of the operation in one of two ways: 

After you've made a call to a method that returns a long-running operation, review the response. 

For example, if you call `documents.import` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.data Stores.branches.documents/import) 

, the start of the response looks something like this: 

```
{
 "operations": [
   {
     "name":
"projects/12345/locations/global/collections/default_collection/
dataStores/my-datastore_4321/branches/0/operations/import-
documents-56789",
     "metadata": {
       "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.ImportDocum
entsMetadata",
     }
   }
 ]
}
```

The `name` value in the response provides the operation name, which can be used to query the operation status. Don't include the quotes when you copy the operation name. 

Get the operation name by listing long-running operations 

(#list-lros). 

2. Call the `operations.get` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStore s.branches.operations/get) 

method on the resource that created the operation: 

```
curl -X GET \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
   "https://discoveryengine.googleapis.com/v1/OPERATION_NAME"
```

_`OPERATION_NAME`_ : Provide the name of the operation for which you need information. You can find the operation name by listing long-running operations (#list-lros). 

The first lines of the response from the `GET` command look something like this: 

```
{
     "name":
"projects/12345/locations/global/collections/default_collection/dataS
tores/my-datastore_4321/branches/0/operations/import-documents-
56789",
     "metadata": {
       "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.ImportDocumentsM
etadata"
     }
   }
```

### Poll a long-running operation

The following show how to poll the status of an operation. 

RESTPython (#python) (#rest) 

To poll the long-running operation until it finishes, follow these steps: 

1. Run the following command, which calls the `operations.get` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStore s.branches.operations/get) method repeatedly, using a backoff of 10 seconds between each request: 

```
while true; \
   do curl -X GET \
   -H "Authorization: Bearer $(gcloud auth print-access-token)" \
   "https://discoveryengine.googleapis.com/v1/OPERATION_NAME"; \
   sleep 10; \
   done
```

_`OPERATION_NAME`_ : Provide the name of the operation you want to poll. You can find the operation name by listing long-running operations (#list-lros) . For example, `projects/12345/locations/global/collections/default_collection/data Stores/my-datastore_4321/branches/0/operations/import-documents56789` . 

### Cancel a long-running operation

The following shows how to cancel an operation: 

RESTPython (#python) (#rest) 

To cancel a long-running operation, follow these steps: 

Call the `operations.cancel` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStore s.branches.operations/cancel) 

method: 

```
curl -X post \
```

- `-H "Authorization: Bearer $(gcloud auth print-access-token)" \ "https://discoveryengine.googleapis.com/v1/` _`OPERATION_NAME`_ `":cancel` 

_`OPERATION_NAME`_ : Provide the name of the operation you want to cancel. You can find the operation name by listing long-running operations (#list-lros). For example, 

`projects/12345/locations/global/collections/default_collection/data Stores/my-datastore_4321/branches/0/operations/import-documents56789` . 

After the API call is made, the server attempts to cancel the operation. The results you see and the actions you can take are as follows: 

- An error with `"code": 400` and `"status": "FAILED_PRECONDITION"` indicates that the request couldn't be canceled. 

- A successful cancellation results in an empty JSON object. To verify the cancellation: 

Use the `operations.get` (#get-details) method. 

- If the operation is successfully cancelled, the response from the `operations.get` method has the error `"code": 1` , which represents the `CANCELLED` status code. 

For example: 

```
{
 "name":
"projects/12345/locations/global/collections/default_collec
tion/dataStores/my-
datastore_4321/branches/0/operations/import-documents-
56789",
 "metadata": {
   "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1alpha.I
mportDocumentsMetadata",
   "createTime": "2025-04-28T21:29:21.199190Z",
   "updateTime": "2025-04-28T21:31:29.076865Z"
 },
 "done": true,
 "error": {
   "code": 1,
   "message": "Operation
projects/12345/locations/global/collections/default_collect
ion/dataStores/my-
datastore_4321/branches/0/operations/import-documents-56789
is cancelled."
 }
}
```

Last updated 2026-10-14 UTC. 



## Access connector error logs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/cloud-logging

Gemini Enterprise provides Cloud Logging for customers to monitor errors and warnings when connecting their data with Gemini Enterprise. 

This document describes how to access federated connector error logs and ingestion connector error logs for Gemini Enterprise using Cloud Logging. 

### Key concepts

This section introduces key concepts related to observability in Gemini Enterprise. 

|Concept|Description|
|---|---|
|Gemini Enterprise<br>connector error<br>logs|Gemini Enterprise connector error logs capture errors and failures<br>encountered when integrating Gemini Enterprise with third-party data<br>sources like Jira and Microsoft OneDrive. These logs include connection<br>problems, data transformation issues, and API errors.|

### Before you begin

Before accessing the error logs, ensure that you have done the following: 

- To turn on logging, you must have the Gemini Enterprise Admin 

- (/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role ( `roles/discoveryengine.agentspaceAdmin` ). 

- To access Cloud Logging, you must have the Logs Viewer 

- (/iam/docs/roles-permissions/logging#logging.viewer) IAM role ( `roles/logging.viewer` ) . 

- Created a Gemini Enterprise app. To create one, see Create an app 

- (/gemini/enterprise/docs/create-app). 

- Ensured your data stores are correctly configured and active. For more information on setting up data stores, see Connect a Google data source (/gemini/enterprise/docs/connectors/create-data-store) or Connect a third-party data source (/gemini/enterprise/docs/connectors/connect-third-party-data-source). 

- Turned on the observability settings to see the federated connector error logs. For more information, see Turn on observability settings 

- (/gemini/enterprise/docs/manage-observability-settings#turn_on_observability_settings). 

### Access federated connector error logs

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

To view the error logs of your data stores that connect to Gemini Enterprise using data federation, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data Stores** . 

3. Select a data store of your choice. 

4. Click **View Logs** . This opens the **Logs Explorer** page. 

5. To only see Gemini Enterprise connector logs, enter the following query in the query editor field, and click **Run Query** : 

```
logName="projects/PROJECT_ID/logs/discoveryengine.googleapis.com%2Fconnect
or_activity"
jsonPayload.logMetadata.name="projects/PROJECT_ID/locations/LOCATION/colle
ctions/COLLECTION_ID/dataConnector"
```

Replace the following: 

   - _`PROJECT_ID`_ : the ID of your project. 

   - _`LOCATION`_ : the location of your connector. For example, `global` . 

   - _`COLLECTION_ID`_ : the ID of the collection that contains your connector, which is also the ID of the data store in the Google Cloud console. 

6. Refine your query scope by using a filter. For example, click **All severities** , and select **Error and higher** . For more information on refining your queries, see Sample queries (/logging/docs/view/query-library). 

### Access ingestion connector error logs

**Key Term:** In Gemini Enterprise, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs. A Gemini Enterprise engine is a generic search engine where the **`app_type`** field is set to **`APP_TYPE_INTRANET`** . 

To view the error logs of your data stores that connect to Gemini Enterprise using data ingestion, follow these steps: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. In the navigation menu, click **Data stores** . 

3. Select a data store of your choice. 

4. Click **View Logs** . This opens the **Logs Explorer** page. 

5. By default, the Logs Explorer page searches the resources listed in the default log scope (/logging/docs/log-scope/create-and-manage) for log entries. To filter to Gemini Enterprise logs, do one of the following: 

   - Select **All Resources > Consumed API > Discovery Engine API** , and then click **Apply** . 

Enter the following into the query bar, and click **Run Query** : 

```
resource.type="consumed_api"
resource.labels.service="discoveryengine.googleapis.com"
```

6. Refine your query scope by filtering on JSON metadata. For example, to query `ImportDocuments` method logs, do one of the following: 

Enter the following into the query bar: 

```
jsonPayload.context.reportLocation.functionName=~"ImportDocuments"
```

Expand the JSON metadata, and click to filter: 

**_Figure 1._** _Filter by clicking on JSON metadata_ 

7. For most warnings and errors, find details in `jsonPayload.message` and `jsonPayload.status` . 

8. For deeper log analysis, dump the logs to a log sink such as BigQuery. For information, see Route logs to supported destinations 

(/logging/docs/export/configure_export_v2) in the Google Cloud Observability documentation. 

Last updated 2026-10-14 UTC.
