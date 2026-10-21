# Gemini Enterprise Docs (User events) / Import historical user events
Source: https://docs.cloud.google.com/gemini/enterprise/docs/import-user-events, page last updated 2026-10-14, extracted 2026-10-19

This page describes how to import user event data from past events in bulk.

For the user event types that you can import, see the `eventType` field of the
[`userEvents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents) object. By importing user events, you can improve the
quality of your results. For example, user events affect the ranking of search
results. Results with higher click-through rates are boosted, while results with
lower click-through rates are buried. Only import user events for documents
that you are already imported into your data store.

If an event has documents listed in `userEvents.Documents`, then
Gemini Enterprise automatically joins the events with that document.
Joining allows Gemini Enterprise to attribute events such as clicks and
views to the correct document in a search result or recommendation. For
custom search and recommendations apps, joining occurs *asynchronously*, that is, user
events are joined to documents after the batch import is complete (generally
happening within minutes).

If you are using a search app with multiple data stores attached, import user
events at the location level instead of the data-store level. This allows a
given user event to be sent to the data store that it's associated with. When
importing user events at a location level, include the `engine` field in the
user event to associate the event with the correct app. For examples of user
events that include the `engine` field, see the following:

- [Custom apps user event type examples and schemas](https://docs.cloud.google.com/gemini/enterprise/docs/user-events#formats)

For more information on the import method, see
[`userEvents.import`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import).

To import user events in real-time, see
[Record real-time user events](https://docs.cloud.google.com/gemini/enterprise/docs/record-user-events).

You can import historical events in the following ways:

For the JSON representation for user events, see
[`userEvents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents)
in the API reference.

## Before you begin

Before you import user events:

- Create a data store and an app.
- Review [About user events](https://docs.cloud.google.com/gemini/enterprise/docs/user-events)
  for user event requirements.

## Import historical user events from Cloud Storage

### REST

To import historical user events in bulk from Cloud Storage, follow these
steps:

1. Create one or more data files for the input parameters for the import. Use the
   [`gcsSource`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/GcsSource)
   object to point to your Cloud Storage bucket.

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

   - `INPUT_FILE`: a file in Cloud Storage containing your user
     event data. Make sure each user event is on its own single line, with
     no line breaks. For the JSON representation for user events, see
     [`userEvents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents) in the API
     reference. The input file fields must be in this format:
     `gs://<bucket>/<path-to-file>/`.
   - `ERROR_DIRECTORY`: optional. A Cloud Storage directory for
     error information about the import—for example,
     `gs://<your-gcs-bucket>/directory/import_errors`. Google recommends
     leaving this field empty to let Gemini Enterprise automatically create
     a temporary directory.
2. Import your events by making a POST request to the
   [`userEvents.import`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the
   data file.

   ```
   curl -X POST \
       -v \
       -H "Content-Type: application/json; charset=utf-8" \
       -H "Authorization: Bearer "$(gcloud auth print-access-token)"" \
       --data @DATA_FILE.json \
   "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/userEvents:import"
   ```

## Import historical user events from BigQuery

When creating tables for user events in BigQuery, use the schemas
documented in [About user events for custom apps](https://docs.cloud.google.com/gemini/enterprise/docs/user-events#bigquery).
Each `search` user event must include an `engine` field to associate the event with an
app. For more information, see [`engine`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent.FIELDS.engine).

### Set up BigQuery access

If your BigQuery dataset is in a different project than your
data store, follow these steps to set up access to BigQuery.

1. Open
   the [IAM & Admin](https://console.cloud.google.com/iam-admin/iam) page
   in the Google Cloud console.
2. Select the project that contains the data store that you want to import user
   events into.
3. Select the **Include Google-provided role grants** checkbox.
4. Find the service account with the name **Discovery Engine Service Account**.
5. If you have not previously initiated an import operation with
   Discovery Engine, this service account might not be listed. If you
   don't see this service account, return to the import task and initiate the
   import. When it fails due to permission errors, return here and complete
   this task. The Discovery Engine service account will be listed.
6. Copy the identifier for the service account, which looks like an email
   address—for example,
   `service-525@gcp-sa-discoveryengine.iam.gserviceaccount.com`.
7. Switch to your BigQuery project (on the same **IAM & Admin** page)
   and click **Grant Access**.
8. For **New principals**, enter the identifier for the service account and
   select the **BigQuery > BigQuery Data Viewer** role.
9. Click **Save**.

For more information about BigQuery access, see
[Controlling access to datasets](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls)
in the BigQuery documentation.

### Import events from BigQuery

### REST

To import historical user events in bulk from BigQuery, follow these
steps:

1. Import your user events by making a POST request to the
   [`userEvents.import`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the
   BigQuery project, dataset ID, and table ID.

   When importing your events, use the value `user_event` for `dataSchema`.

   ```
   curl \
     -v \
     -X POST \
     -H "Content-Type: application/json; charset=utf-8" \
     -H "Authorization: Bearer "$(gcloud auth print-access-token)"" \
     "https://discoveryengine.googleapis.com/v1/projects/[PROJECT_NUMBER]/locations/global/userEvents:import" \
     --data '{
         "bigquerySource": {
             "projectId":"PROJECT_ID",
             "datasetId": "DATASET_ID",
             "tableId": "TABLE_ID",
             "dataSchema": "user_event"
         }
       }'
   ```

## Import historical user events as local JSON data

You can import user events by including local JSON data for the
events in your call to the [`userEvents.import`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import) method.

To put user event data into a JSON file and specify the file in an API request,
follow these instructions:

1. Create a JSON file containing your user event data. For the JSON
   representation for user events, see
   [`userEvents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents)
   in the API reference documentation.

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
2. Import your events by making a POST request to the
   [`userEvents.import`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.userEvents/import) method, providing the name of the
   data file.

   ```
   curl -X POST \
       -H "Authorization: Bearer $(gcloud auth print-access-token)" \
       -H "Content-Type: application/json; charset=utf-8" \
       --data @[JSON_FILE] \
     "https://discoveryengine.googleapis.com/v1/projects/PROJECT_NUMBER/locations/global/userEvents:import"
   ```
