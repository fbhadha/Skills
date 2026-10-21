# INDEX / Gemini Enterprise activity logging, audit, and reporting docs
Source: compiled from the files below, extracted 2026-10-19

Scope: everything Google documents for tracking what people do in Gemini Enterprise (actions, agent use, searches, adoption metrics) without needing prompt text, plus the Workspace Reports API for the separate "Gemini in Workspace apps" product. Google product docs are CC BY 4.0; the one blog post is summarized, not copied.

## Which source answers which question

| Question | Start with |
| --- | --- |
| Which actions did users take (chat, search, file upload, agent use), without prompt text? | Usage audit logs |
| Which API methods are audited, and which log type (Admin Activity or Data Access) each lands in? | Cloud Audit Logs parts 1 to 5 |
| How do I turn logging on, and keep prompt text out? | Observability settings |
| Active users, DAU/WAU/MAU, retention, seats claimed, per-agent usage | View and export analytics, exportMetrics API |
| Getting all of this into BigQuery for dashboards | BigQuery blog summary, exportMetrics API |
| Which user (identity) took an action? | Blog summary (user activity table carries IAM user emails); Model Armor correlation (`userIamPrincipal`) |
| Sign-in events | Not in Gemini Enterprise logs. Analytics counts a user as active once they sign in and trigger any API call. Raw logins come from the identity provider. |
| Gemini inside Gmail, Docs, Slides, Sheets, Meet, Classroom | Workspace Reports API files (different product) |

## Files

| File | Source | Page date | Scope |
| --- | --- | --- | --- |
| `ge-usage-audit-logs__access-gemini-enterprise-usage-audit-logs-with-cloud-logging.md` | [set-up-usage-audit-logs](https://docs.cloud.google.com/gemini/enterprise/docs/set-up-usage-audit-logs) | 2026-10-14 | The `gemini_enterprise_user_activity` log. Field-by-field table of what each service method logs, marked sensitive or not sensitive; Logs Explorer query; log access controls. |
| `ge-cloud-audit-logs__access-gemini-enterprise-cloud-audit-logs-part1.md` | [audit-logging](https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging) | 2026-10-14 | Cloud Audit Logs for `discoveryengine.googleapis.com`: service name query, and the table of every audited method grouped by permission type (ADMIN_READ, ADMIN_WRITE, DATA_READ, DATA_WRITE). Start of per-method detail. |
| `ge-cloud-audit-logs__...-part2.md` to `part5.md` | same | 2026-10-14 | Per-method detail (method name, audit log type, IAM permission, LRO or streaming, Logs Explorer filter), alphabetical by service, v1 then v1alpha then v1beta. Part labels in each file's first line give the service range. |
| `ge-observability-settings__manage-observability-settings.md` | [manage-observability-settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings) | 2026-10-14 | The two toggles: OpenTelemetry instrumentation (required for any logs, traces, metrics) and prompt/response logging (separate, can stay off). Console and REST (`observabilityConfig`) at app level and per agent. |
| `ge-view-analytics__view-and-export-analytics-data.md` | [view-analytics](https://docs.cloud.google.com/gemini/enterprise/docs/view-analytics) | 2026-10-14 | Looker-based analytics dashboard; definitions of every metric (active users, users calling assistant/answer/search, DAU/WAU/MAU, retention, growth, churn, seats, agent metrics); user events needed for search metrics; BigQuery export steps. |
| `ge-api-exportmetrics__method-projects-locations-collections-engines-analytics-expo.md` | [exportMetrics REST](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.analytics/exportMetrics) | 2026-10-09 | REST reference for `analytics:exportMetrics` (v1alpha): endpoint, `outputConfig` to a BigQuery dataset and table, `startDate` (default 30 days back, max 180), OAuth scopes. Returns a long-running operation. |
| `ge-metrics__access-metrics.md` | [access-metrics](https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics) | 2026-10-14 | Cloud Monitoring metrics under `discoveryengine.googleapis.com/`: agent overview, tools, latency, error rate. Retained 6 weeks by default. |
| `ge-traces-spans__access-traces-and-spans.md` | [access-traces-and-spans](https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans) | 2026-10-14 | Cloud Trace view of each request: trace summary table, span hierarchy, generative AI semantic conventions. Retained 30 days by default. |
| `ge-feature-usage__view-feature-usage.md` | [feature-usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage) | 2026-10-14 | Usage dashboard against pooled quotas (license editions) or actual consumption (Pay-as-you-go); quota reset schedule. |
| `ge-connector-error-logs__access-gemini-enterprise-connector-error-logs-with-cloud-log.md` | [cloud-logging](https://docs.cloud.google.com/gemini/enterprise/docs/cloud-logging) | 2026-10-14 | Error logs for federated and ingestion connectors (third-party sources such as Jira, OneDrive). |
| `ge-model-armor-log-correlation__correlate-model-armor-logs-with-gemini-enterprise-logs.md` | [correlate-model-armor-logs](https://docs.cloud.google.com/gemini/enterprise/docs/correlate-model-armor-logs) | 2026-10-14 | Joining Model Armor safety logs to Gemini Enterprise logs for ingress (user to agent) and egress (agent to tools) traffic; join keys including `userIamPrincipal`; Python sample. |
| `ge-user-events-about__about-user-events.md` | [user-events](https://docs.cloud.google.com/gemini/enterprise/docs/user-events) | 2026-10-14 | User event types (search, view-item and others), schemas, `userPseudoId` and `userId`, timestamps. Only needed when you call the APIs from your own app; the Gemini Enterprise web app records these itself. |
| `ge-user-events-record__record-real-time-user-events.md` | [record-user-events](https://docs.cloud.google.com/gemini/enterprise/docs/record-user-events) | 2026-10-14 | Recording events from your own app with a JavaScript pixel or `userEvents.write` (REST, C#, Go, Java, Python, Ruby samples). |
| `ge-user-events-import__import-historical-user-events.md` | [import-user-events](https://docs.cloud.google.com/gemini/enterprise/docs/import-user-events) | 2026-10-14 | Importing past events from Cloud Storage, BigQuery, or inline JSON. |
| `ge-long-running-operations__monitor-long-running-operations.md` | [long-running-operations](https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations) | 2026-10-14 | List, get, poll, cancel long-running operations (needed to track an `exportMetrics` job). REST and Python. |
| `blog-bigquery-analytics__summary.md` | [Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/analyze-and-govern-gemini-enterprise-at-scale-with-bigquery) | 2026-07-15 | Paraphrased summary of Google's reference architecture: log sinks plus `exportMetrics` into BigQuery, table names, sink filters, use cases. Notes a conflict with the product docs on whether prompt logging must be on. |
| `ws-reports-gemini-activity__gemini-in-workspace-apps-activity-events.md` | [Gemini in Workspace apps events](https://developers.google.com/workspace/admin/reports/v1/appendix/activity/gemini-in-workspace-apps) | 2026-09-22 | Workspace Reports API events for Gemini inside Workspace apps (`applicationName=gemini_in_workspace_apps`): event names, the full list of `action` values per app, sample requests. 180-day history. Not Gemini Enterprise. |
| `ws-reports-activities-list__method-activities-list.md` | [activities.list](https://developers.google.com/workspace/admin/reports/reference/rest/v1/activities/list) | 2026-10-02 | Reports API `activities.list` reference: query parameters, Activity object, actor and identity types. Applies to the Workspace file above. |

## Gaps in this set

- No Gemini Enterprise doc lists a login or sign-in event. Check the identity provider (Google Cloud Identity, Entra ID, Okta) sign-in logs.
- User identity in `gemini_enterprise_user_activity` comes from the BigQuery blog, not from the product doc's field table. Confirm on a real log entry.
- License assignment and user license export (`UserLicenseService`) appear only as audited method names in the Cloud Audit Logs files; their REST reference is not included.
