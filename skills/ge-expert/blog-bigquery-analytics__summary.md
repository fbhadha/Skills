# Google Cloud Blog / How to Analyze and Govern Gemini Enterprise App Usage at Scale with BigQuery (summary)
Source: https://cloud.google.com/blog/products/data-analytics/analyze-and-govern-gemini-enterprise-at-scale-with-bigquery, published 2026-07-15, extracted 2026-10-19

This file is a paraphrased summary, not the original text. The blog post is not under the Creative Commons license that covers Google's product documentation, so it is summarized here instead of copied. Authors: Aishwarya Prabhat (Solutions Acceleration Architect) and Sudipto Guha (Data Analytics & AI Tech Lead), Google Cloud.

## Two ingestion paths

- **Log Router sinks to BigQuery** stream row-level events continuously. One sink carries conversational and user activity logs; a second carries Cloud Audit Logs for governance.
- **`analytics:exportMetrics` batch export** pulls pre-aggregated seat and engagement metrics. You schedule it yourself (the post suggests a daily run). It covers the trailing 30 days.

## BigQuery tables the sinks create

| BigQuery table | What it holds | Path |
| --- | --- | --- |
| `discoveryengine_googleapis_com_gen_ai_user_message` | User prompts | Streaming sink |
| `discoveryengine_googleapis_com_gen_ai_choice` | Model responses, finish reasons, reasoning steps | Streaming sink |
| `discoveryengine_googleapis_com_gemini_enterprise_user_activity` | User activity, including IAM user emails and the file paths used for grounding | Streaming sink |
| `cloudaudit_googleapis_com_activity` | Admin Activity audit logs (configuration and resource changes, such as agent create, update, delete) | Governance sink |
| `cloudaudit_googleapis_com_data_access` | Data Access audit logs (data-plane calls and search queries) | Governance sink |
| Batch export table (name you choose) | Seats claimed, seats purchased, engagement metrics for the past 30 days | `exportMetrics` batch |

## Sink filters described

- **Streaming sink:** includes the log IDs `gemini_enterprise_user_activity`, `gen_ai.user.message`, and `gen_ai.choice` in your project.
- **Governance sink:** `cloudaudit.googleapis.com` logs where `protoPayload.serviceName="discoveryengine.googleapis.com"`.
- Admin Activity audit logs are on by default. Data Access audit logs are off by default and must be turned on in the project's IAM audit configuration for the Discovery Engine API to capture user-level read and write calls.

## Prerequisites listed

1. A Gemini Enterprise deployment.
2. Prompt and response logging turned on in the admin console (the post lists this as a requirement for the streaming pipeline).
3. Log Router sinks to BigQuery with the filters above.
4. Data Access audit logs turned on for the Discovery Engine API, if you want user-level data access records.
5. A scheduled job that calls `analytics:exportMetrics`, if you want aggregate seat metrics.
6. Optional: Model Armor, HR or line-of-business datasets for value analysis, Data Studio or Looker for dashboards.

## Use cases the post describes

- Adoption by department, custom agent creation, NotebookLM use, agent-to-employee ratios.
- Estimating hours saved by joining usage with HR or line-of-business data.
- Compliance checks on which Drive folders and directories are used for grounding.
- Investigating which prompts triggered a Model Armor block.
- Dashboards for seat ROI, grounding traffic by connector (SharePoint, Drive, Gmail), Model Armor blocks, and prompt sentiment.
- BigQuery Conversational Analytics agents that answer plain-language questions over the tables. The post includes no hand-written SQL.

## Conflict with the product documentation

The post says prompt and response logging must be on for the streaming pipeline. The usage audit logs page (`ge-usage-audit-logs__...md`) says fields marked "not sensitive" are logged whether or not that setting is on, and that sensitive text is replaced with `<elided>` when it is off. If the goal is activity metadata without prompt text, follow the product documentation and test with the setting off. The `gen_ai_user_message` and `gen_ai_choice` tables carry prompt and response content, so they are only useful with the setting on.
