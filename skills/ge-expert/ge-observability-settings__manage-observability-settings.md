# Gemini Enterprise Docs (Configure settings) / Manage observability settings
Source: https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings, page last updated 2026-10-14, extracted 2026-10-19

This document describes how to configure the observability settings
for your Gemini Enterprise app or individual agents using the Google Cloud console or
the REST API.

The enablement logic depends on the agent type:

- **Core Assistant agent**: Use the application-level (engine-level) toggle
  in configurations.
- **Other agents**: (Limited to Workflow Builder employee-made agents
  and Deep Research agents at this time): Use the agent-level toggle inside
  the individual agent's settings.

After you enable the settings, you can view the following data from your
interactions with the assistant or agents in your Gemini Enterprise web app:

- View metrics in Metrics Explorer.
- View traces and spans in Trace Explorer.

## Key concepts

This section introduces key concepts related to observability in
Gemini Enterprise.

| Concept | Description |
| --- | --- |
| Trace | A trace is a collection of spans that represents a single request or transaction as it flows through different services and components.   For example, a trace represents the entire lifecycle of a request. This includes a user asking a question from the Gemini Enterprise assistant, the Gemini Enterprise assistant responding, and any subsequent actions triggered by the answer, such as sending an email. |
| Span | A span is a single, timed unit of work within a trace. It represents a specific operation, such as a function call, an API request, or a database query. Each span includes details like its start and end times, a unique ID, and its relationship to other spans. These relationships together form a trace. |
| Span logs | Span logs are timestamped, free-form messages or events associated with a specific span. They provide detailed, contextual information about a span's execution, helping users debug issues and understand the flow of a request. |
| Metrics | Metrics are numerical measurements that systems collect over time. These measurements represent the performance, resource utilization, or behavior of a system. Engineers use metrics to monitor system health, identify trends, and trigger alerts. |
| Usage audit logs | Usage audit logs are records of administrative activities and accesses within your Google Cloud resources. They provide detailed information about who performed what action, when, and from where. These logs are essential for security auditing, compliance, and understanding how your resources are being used. |
| Gemini Enterprise connector error logs | Gemini Enterprise connector error logs capture errors and failures encountered when integrating Gemini Enterprise with third-party data sources like Jira and Microsoft OneDrive. These logs include connection problems, data transformation issues, and API errors. |

## Before you begin

Make sure you have the following:

- The [Gemini Enterprise Admin](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin)
  role.
- An existing Gemini Enterprise web app. For information about creating a new
  app, see [Create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app).

## Turn on observability settings

To turn on observability for your Gemini Enterprise app or individual agents, you
can use either the Google Cloud console or the REST API.

### Console

To turn on the observability settings using the Google Cloud console, follow these steps:

1. In the Google Cloud console, go to the Gemini Enterprise page.

   [Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)
2. Click the name of the app that you want to configure.
3. Depending on the agent type you are configuring, do one of the following:

   - **Core Assistant agent**: Click **Configurations**, and then click the
     **Observability** tab.
   - **Other agents (Workflow Builder employee-made agents and
     Deep Research agents)**: Click **Agents**, click the name of the agent
     you want to configure, and then click the **Configuration** tab.
4. You can turn on or turn off the following settings:

   | Observability setting | Description |
   | --- | --- |
   | **Enable instrumentation of OpenTelemetry traces and logs** | When enabled, you can view traces, spans, span logs, and metrics associated with your logs in Cloud Logging. |
   | **Enable logging of prompt inputs and response outputs** | When enabled, Cloud Logging logs the full content of user prompts and responses. This includes sensitive data or Personally Identifiable Information (PII). To enable this setting, you must first enable **Enable instrumentation of OpenTelemetry traces and logs**.    **Caution:** Enabling this setting logs potentially sensitive data, including PII. Restrict log access to authorized personnel only. |

### REST

To configure observability settings using the REST API, see the following sections:

### Configure observability settings for the Core Assistant (app level)

To configure observability settings using the REST API at the app level (which
applies to the Core Assistant agent), see the following sections:

#### Turn on observability when creating an app

To create a new app with observability turned on, run the following
command:

**Key Term:** In Gemini Enterprise, the term *app* can be used
interchangeably with the term *engine* in the context of APIs. A Gemini Enterprise engine is a
generic search engine where the `app_type` field is set to
`APP_TYPE_INTRANET`.

```
curl -X POST \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines?engineId=APP_ID" \
-d '{
  "name": "projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID",
  "displayName": "APP_DISPLAY_NAME",
  "solutionType": "SOLUTION_TYPE_SEARCH",
  "searchEngineConfig": {
    "searchTier": "SEARCH_TIER_ENTERPRISE",
    "searchAddOns": ["SEARCH_ADD_ON_LLM"],
    "requiredSubscriptionTier": "SUBSCRIPTION_TIER_SEARCH_AND_ASSISTANT"
  },
  "industryVertical": "GENERIC",
  "appType": "APP_TYPE_INTRANET",
  "observabilityConfig": {
    "observabilityEnabled": true,
    "sensitiveLoggingEnabled": true
  }
}'
```

Replace the following:

- `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following
  values:
  - `us` for the US multi-region
  - `eu` for the EU multi-region
  - `global` for the Global locationFor more information, see
  [Specify a multi-region
  for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store).
- `PROJECT_ID`: the ID of your project.
- `LOCATION`: the multi-region of your data store:
  `global`, `us`, or `eu`
- `APP_ID`: the ID of the app that you want to create.
- `APP_DISPLAY_NAME`: the display name of the app that you want to create.

### Turn on observability for an existing app

To turn on observability on an existing app, run the following command:

**Key Term:** In Gemini Enterprise, the term *app* can be used
interchangeably with the term *engine* in the context of APIs. A Gemini Enterprise engine is a
generic search engine where the `app_type` field is set to
`APP_TYPE_INTRANET`.

```
curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID?updateMask=observabilityConfig" \
-d '{
  "observabilityConfig": {
    "observabilityEnabled": true,
    "sensitiveLoggingEnabled": true
  }
}'
```

Replace the following:

- `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following
  values:
  - `us` for the US multi-region
  - `eu` for the EU multi-region
  - `global` for the Global locationFor more information, see
  [Specify a multi-region
  for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store).
- `PROJECT_ID`: the ID of your project.
- `LOCATION`: the multi-region of your data store:
  `global`, `us`, or `eu`
- `APP_ID`: the ID of the app.

### Configure observability settings for an individual agent

To turn on observability for an individual agent (such as an
Workflow Builder agent or a Deep Research agent) using the REST
API, run the following command to update the agent's `observabilityConfig`:

```
curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID?updateMask=observabilityConfig" \
-d '{
  "observabilityConfig": {
    "observabilityEnabled": true,
    "sensitiveLoggingEnabled": true
  }
}'
```

Replace the following:

- `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following
  values:
  - `us` for the US multi-region
  - `eu` for the EU multi-region
  - `global` for the Global locationFor more information, see
  [Specify a multi-region
  for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store).
- `PROJECT_ID`: the ID of your project.
- `LOCATION`: the multi-region of your data store:
  `global`, `us`, or `eu`
- `APP_ID`: the ID of the app.
- `AGENT_ID`: the ID of the agent you want to configure

## Turn off observability settings

To turn off the observability settings for your Gemini Enterprise app or individual agents, use either
the Google Cloud console or the REST API.

### Console

To turn off the observability settings using the Google Cloud console, follow these
steps:

1. In the Google Cloud console, go to the Gemini Enterprise page.

   [Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)
2. Click the name of the app for which you want to turn off the observability
   settings.
3. Depending on the agent type you are configuring, do one of the following:

   - **Core Assistant agent**: Click **Configurations**, and then click the **Observability** tab.
   - **Other agents (including Workflow Builder employee-made
     agents and Deep Research agents)**: Click **Agents**, click the name of
     the agent you want to configure, and then click the **Configuration** tab.
4. You can turn off the following settings:

   | Observability setting | Description |
   | --- | --- |
   | **Enable instrumentation of OpenTelemetry traces and logs** | When turned off, this setting stops the collection of traces, spans, span logs, and metrics. It also turns off the **Enable logging of prompt inputs and response outputs** setting, which means no logs are sent to Cloud Logging. |
   | **Enable logging of prompt inputs and response outputs** | When turned off, Cloud Logging does not log prompt inputs and response outputs. |

### REST

To turn off observability settings using the REST API, see the following sections:

### Turn off observability at the app level (Core Assistant)

To turn off observability at the application (app) level, run the following
command:

**Key Term:** In Gemini Enterprise, the term *app* can be used
interchangeably with the term *engine* in the context of APIs. A Gemini Enterprise engine is a
generic search engine where the `app_type` field is set to
`APP_TYPE_INTRANET`.

```
curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID?updateMask=observabilityConfig" \
-d '{
  "observabilityConfig": {
    "observabilityEnabled": false,
    "sensitiveLoggingEnabled": false
  }
}'
```

Replace the following:

- `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following
  values:
  - `us` for the US multi-region
  - `eu` for the EU multi-region
  - `global` for the Global locationFor more information, see
  [Specify a multi-region
  for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store).
- `PROJECT_ID`: the ID of your project.
- `LOCATION`: the multi-region of your data store:
  `global`, `us`, or `eu`
- `APP_ID`: the ID of the app.

### Turn off observability for an individual agent

To turn off observability for an individual agent (such as an
Workflow Builder agent or a Deep Research agent), run the
following command:

```
curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "X-Goog-User-Project: PROJECT_ID" \
"https://ENDPOINT_LOCATION-discoveryengine.googleapis.com/v1alpha/projects/PROJECT_ID/locations/LOCATION/collections/default_collection/engines/APP_ID/assistants/default_assistant/agents/AGENT_ID?updateMask=observabilityConfig" \
-d '{
  "observabilityConfig": {
    "observabilityEnabled": false,
    "sensitiveLoggingEnabled": false
  }
}'
```

Replace the following:

- `ENDPOINT_LOCATION`: the multi-region for your API request. Specify one of the following
  values:
  - `us` for the US multi-region
  - `eu` for the EU multi-region
  - `global` for the Global locationFor more information, see
  [Specify a multi-region
  for your data store](https://docs.cloud.google.com/gemini/enterprise/docs/locations#specify_a_multi-region_for_your_data_store).
- `PROJECT_ID`: the ID of your project.
- `LOCATION`: the multi-region of your data store:
  `global`, `us`, or `eu`
- `APP_ID`: the ID of the app.
- `AGENT_ID`: the ID of the agent you want to configure

## What's next

- To learn more about how to access the Gemini Enterprise logs,
  see [Access usage audit logs](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs).
- To learn more about how to access the Gemini Enterprise trace and span data,
  see [Access traces and spans in Trace Explorer](https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans).
- To learn more about how to access the Gemini Enterprise metrics, see
  [Access metrics in Metrics Explorer](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics).
