# Gemini Enterprise Docs (Security) / Correlate Model Armor logs with Gemini Enterprise logs
Source: https://docs.cloud.google.com/gemini/enterprise/docs/correlate-model-armor-logs, page last updated 2026-10-14, extracted 2026-10-19

This document describes how to correlate Model Armor sanitization logs
with Gemini Enterprise platform logs and trace spans in
Cloud Logging. It explains the correlation mechanisms for Client-to-Agent
(ingress) and Agent-to-Anywhere (egress) traffic flows, outlines the
prerequisites for trace generation, and provides step-by-step instructions and
code samples to join these log entries in your log processing pipeline.

When investigating a Model Armor trace span or log entry, you
might need to locate the corresponding records in Cloud Logging to get the
complete context of the request. For example:

- If you start from a trace span, you might need to determine the end-user's
  identity or inspect the detailed sanitization findings.
- If you start from a Model Armor sanitization log entry, you
  might need to correlate it with the user identity or trace information.

## How log correlation works

Model Armor can screen prompts and responses at the following
communication points in Gemini Enterprise:

- **Client-to-Agent (ingress) traffic**: When a user submits a prompt to the
  Gemini Enterprise assistant, Gemini Enterprise directly
  calls the Model Armor APIs. The resulting
  Model Armor platform logs
  ([`SanitizeOperation`](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_modelarmor.googleapis.com/SanitizeOperation))
  don't directly contain OpenTelemetry `trace` or `spanId` fields. To correlate
  these logs with user identities and trace spans, you perform a *log join* in
  your security information and event management (SIEM) or log processing
  pipeline by using the session token.
- **Agent-to-Anywhere (egress) traffic**: When an agent calls an external tool,
  Model Context Protocol (MCP) server, or external large language model (LLM),
  traffic is routed through Agent Gateway and Secure Web Proxy. For egress
  calls, when OpenTelemetry instrumentation is enabled,
  Model Armor `SanitizeOperation` logs do contain the `trace`
  and `spanId` fields directly. You can directly filter logs and view trace
  spans in [Cloud Trace](https://docs.cloud.google.com/trace/docs/finding-traces) or
  [Agent Registry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/observability/traces#exploring_traces).

### Summary of correlation mechanisms

| Flow | Path and routing | Trace in Model Armor log | Correlation method |
| --- | --- | --- | --- |
| **Client-to-Agent (ingress)** | Direct API call from Gemini Enterprise to Model Armor | The `trace` and `spanId` aren't populated. | Log join using the session token from `client_correlation_id` and `assistToken` |
| **Agent-to-Anywhere (egress)** | Routed through Agent Gateway and Secure Web Proxy | The `trace` and `spanId` are populated. | Direct match on `trace` ID and Trace span inspection |

## Before you begin

Before you start correlating Model Armor logs with
Gemini Enterprise logs, follow these steps:

1. [Enable Model Armor in
   Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor).
2. To generate trace context and view trace details in
   Gemini Enterprise and Model Armor logs, turn on
   **Enable instrumentation of OpenTelemetry traces and logs** and, optionally,
   **Enable logging of prompt inputs and response outputs** in your
   observability settings. For instructions, see [Turn on observability
   settings](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings#turn_on_observability_settings)
3. For egress traffic screening, [configure Model Armor on your
   Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/configure-model-armor).

### Required roles

To get the permissions that
you need to view and correlate logs and trace spans,
ask your administrator to grant you the
following IAM roles on your project:

- [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user)  (`roles/cloudtrace.user`)
- [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer)  (`roles/logging.viewer`)

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

You might also be able to get
the required permissions through [custom
roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined
roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

For information about other roles you might need, see [Trace
access control](https://docs.cloud.google.com/trace/docs/iam) and [Cloud Logging access
control](https://docs.cloud.google.com/logging/docs/access-control).

## Correlate Client-to-Agent (ingress) logs

A single `StreamAssist` interaction produces three distinct log entries in
Cloud Logging:

- **Model Armor sanitization log (`SanitizeOperation`):**
  - **Monitored resource:** `modelarmor.googleapis.com/SanitizeOperation`
  - **Properties:** Contains the detailed sanitization verdict and safety
    findings (such as PII redaction, responsible AI filter matches, or prompt
    injection detection) but doesn't contain trace context or end-user
    identity.
  - **Correlation key:**
    `labels."modelarmor.googleapis.com/client_correlation_id"`
- **Gemini Enterprise StreamAssist log (`consumed_api`):**
  - **Monitored resource:** `consumed_api`
  - **Properties:** Contains the end-user identity (`userIamPrincipal`), the
    trace details (`trace` and `spanId`), and the session token
    (`response.assistToken`).
  - **Correlation key:** `jsonPayload.response.assistToken`
- **Gemini Enterprise ModelArmorAudit Log (`Agent`):**
  - **Monitored Resource:** `discoveryengine.googleapis.com/Agent` where
    `jsonPayload.logMetadata.methodName` is `ModelArmorAudit`.
  - **Properties:** Echoes the high-level sanitization verdict and contains the
    trace context (`trace` and `spanId`), but doesn't contain detailed findings
    or correlation IDs.
  - **Correlation Key:** `trace`

### Correlation join key

Model Armor sanitization logs include a `client_correlation_id`
label that has a pipe-delimited structure. The third segment of this label
is a base64url-encoded session token that matches the
[`assistToken`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist#response-body)
field recorded in the `consumed_api` log for
[`StreamAssist`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/streamAssist).

The `client_correlation_id` label has the following format:

```
AS|ASSISTANT_RESOURCE|SESSION_TOKEN
```

The correlation ID includes the following values:

- `ASSISTANT_RESOURCE`: the full resource name of the
  Gemini Enterprise
  [`Assistant`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants)
  resource in the following format:

  ```
  projects/PROJECT/locations/LOCATION/collections/COLLECTION/engines/ENGINE/assistants/ASSISTANT
  ```
- `SESSION_TOKEN`: the unique session token that matches
  the `assistToken` in the `consumed_api` log after base64url padding is
  normalized.

### Matching logic

To correlate a Model Armor sanitization log entry with
Gemini Enterprise `StreamAssist` logs, implement the following
matching logic in your log processing pipeline:

1. **Extract the session token from the Model Armor entry**:

   1. Locate the `labels` object in the Model Armor entry.
   2. Retrieve the value of the
      `modelarmor.googleapis.com/client_correlation_id` label.
   3. Split the value of this label using the pipe character (`|`).
   4. Extract the third segment, which represents the base64url-encoded session
      token.
2. **Extract the `assistToken` value from the `StreamAssist` entries**: For
   each candidate `StreamAssist` `consumed_api` log entry, follow these steps:

   1. Locate the `jsonPayload` object.
   2. Extract the token value from the `response.assistToken` field.
3. **Normalize and compare the tokens**: To compare the tokens, normalize both
   token strings:

   1. Replace all hyphens (`-`) with plus signs (`+`).
   2. Replace all underscores (`_`) with forward slashes (`/`).
   3. Strip any trailing equal signs (`=`).
   4. If the normalized tokens match, correlate the log entries.
4. **Extract the correlated data**: If you find a match, extract these fields
   from the matching entries:

   - **User IAM identity**: the `userIamPrincipal` field from
     the `StreamAssist` entry
   - **Trace ID**: the `trace` field from the `StreamAssist` entry
   - **Span ID**: the `spanId` field from the `StreamAssist` entry
   - **Sanitization verdict**: the `sanitizationVerdict` field under
     `jsonPayload.sanitizationResult` in the Model Armor
     entry

### Python correlation sample

The following Python script demonstrates how to query Cloud Logging for
both Model Armor and Gemini Enterprise logs, perform
the token normalization and matching, and output the correlated records:

```
#!/usr/bin/env python3
from datetime import datetime, timedelta, timezone
from google.cloud import logging

# Google Cloud project ID
PROJECT_ID = "YOUR_PROJECT_ID"

def correlate_logs(ma_entry, de_consumed_entries):
  """Correlates a Model Armor log entry with StreamAssist logs."""
  # 1. Extract client_correlation_id from Model Armor log labels
  labels = ma_entry.get("labels", {})
  client_corr_id = labels.get(
      "modelarmor.googleapis.com/client_correlation_id", ""
  )
  if not client_corr_id:
    return None

  # 2. Extract session token (3rd pipe-delimited segment)
  parts = client_corr_id.split("|")
  if len(parts) < 3:
    return None
  ma_token = parts[2]

  # 3. Normalize base64url padding for comparison
  ma_token_normalized = ma_token.replace("-", "+").replace("_", "/").rstrip("=")

  # 4. Search for matching assistToken in StreamAssist logs
  for de in de_consumed_entries:
    payload = de.get("jsonPayload", {})
    de_token = payload.get("response", {}).get("assistToken", "")
    de_token_normalized = (
        de_token.replace("-", "+").replace("_", "/").rstrip("=")
    )

    if ma_token_normalized == de_token_normalized:
      return {
          "user": payload.get("userIamPrincipal"),
          "trace": de.get("trace"),
          "span_id": de.get("spanId"),
          "verdict": (
              ma_entry.get("jsonPayload", {})
              .get("sanitizationResult", {})
              .get("sanitizationVerdict")
          ),
      }
  return None

def main():
  # Initialize Google Cloud Logging Client
  print(f"Connecting to Google Cloud Logging (Project: {PROJECT_ID})...")
  client = logging.Client(project=PROJECT_ID)

  # Calculate ISO timestamp for 1 hour ago
  one_hour_ago = (
      datetime.now(timezone.utc) - timedelta(hours=1)
  ).strftime("%Y-%m-%dT%H:%M:%SZ")
  print(f"Filtering logs starting from: {one_hour_ago}")

  # Build log query filters
  ma_filter = f"""
    resource.type="modelarmor.googleapis.com/SanitizeOperation"
    AND timestamp >= "{one_hour_ago}"
    """

  de_filter = f"""
    resource.type="consumed_api"
    AND jsonPayload.response.assistToken:*
    AND timestamp >= "{one_hour_ago}"
    """

  # Fetch Model Armor log entries
  print("Fetching Model Armor log entries...")
  ma_entries = [
      entry.to_api_repr()
      for entry in client.list_entries(filter_=ma_filter, max_results=100)
  ]
  print(f"Found {len(ma_entries)} Model Armor entries.")

  # Fetch Gemini Enterprise log entries
  print("Fetching Gemini Enterprise StreamAssist log entries...")
  de_entries = [
      entry.to_api_repr()
      for entry in client.list_entries(filter_=de_filter, max_results=500)
  ]
  print(f"Found {len(de_entries)} Gemini Enterprise entries.")

  # Perform Correlation
  print("\n================ Correlating Logs ================")
  correlated_results = []
  for ma in ma_entries:
    match = correlate_logs(ma, de_entries)
    if match:
      correlated_results.append(match)
      print(f"  User IAM Principal  : {match['user']}")
      print(f"  Sanitization Verdict: {match['verdict']}")
      print(f"  Trace ID            : {match['trace']}")
      print(f"  Span ID             : {match['span_id']}")
      print("-" * 50)

  print(f"\nDone. Total Correlated Records: {len(correlated_results)}")

if __name__ == "__main__":
  main()
```

## Correlate Agent-to-Anywhere (egress) logs and trace spans

When an agent executes tool calls (such as interacting with an MCP server or
external APIs) that are protected by Agent Gateway and
Model Armor, the request is part of Agent-to-Anywhere traffic.

When OpenTelemetry instrumentation is enabled on the app, the resulting
`SanitizeOperation` log entries automatically include the `trace` and `spanId`
fields.

### Filter egress logs in Cloud Logging

To find all Model Armor sanitization logs that are associated
with a specific trace in Cloud Logging, use the following query filter:

```
resource.type="modelarmor.googleapis.com/SanitizeOperation"
trace="TRACE_ID"
```

Replace `TRACE_ID` with the trace ID from the agent
interaction.

For more information, see [View and analyze log
entries](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).

### View trace spans

In Trace or Agent Registry, you can view the execution
graph and timelines of the agent interaction. Model Armor
generates the following spans:

- **Parent span**: `apply_guardrail "Google Cloud Model Armor"`
- **Child spans**: `Request Path` and `Response Path`

Each span includes attributes such as policy ID, security decisions, and matched
filter violations. For more information, see [View Model Armor trace
spans](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-model-armor-spans).

## What's next

- [Enable Model Armor in
  Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor)
- [View Model Armor trace
  spans](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/view-model-armor-spans)
- [Configure logging in Model Armor](https://docs.cloud.google.com/model-armor/configure-logging)
- [Manage observability settings in
  Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/manage-observability-settings)
