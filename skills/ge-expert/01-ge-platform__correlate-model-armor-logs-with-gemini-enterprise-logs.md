# Gemini Enterprise: platform, security, agents, cost, monitoring / Correlate Model Armor logs with Gemini Enterprise logs to Protect sensitive data in sources
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 219-241, extracted 2026-10-18

Contains:
- Correlate Model Armor logs with Gemini Enterprise logs (pages 219-228) https://docs.cloud.google.com/gemini/enterprise/docs/correlate-model-armor-logs
- Protect sensitive data in sources (pages 229-241) https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data

## Correlate Model Armor logs with Gemini Enterprise logs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/correlate-model-armor-logs

This document describes how to correlate Model Armor sanitization logs with Gemini Enterprise platform logs and trace spans in Cloud Logging. It explains the correlation mechanisms for Client-to-Agent (ingress) and Agent-to-Anywhere (egress) traffic flows, outlines the prerequisites for trace generation, and provides step-by-step instructions and code samples to join these log entries in your log processing pipeline. 

When investigating a Model Armor trace span or log entry, you might need to locate the corresponding records in Cloud Logging to get the complete context of the request. For example: 

- If you start from a trace span, you might need to determine the end-user's identity or inspect the detailed sanitization findings. 

- If you start from a Model Armor sanitization log entry, you might need to correlate it with the user identity or trace information. 

### How log correlation works

Model Armor can screen prompts and responses at the following communication points in Gemini Enterprise: 

- **Client-to-Agent (ingress) traffic** : When a user submits a prompt to the Gemini Enterprise assistant, Gemini Enterprise directly calls the Model Armor APIs. The resulting Model Armor platform logs ( `SanitizeOperation` (/logging/docs/api/v2/resource-list#tag_modelarmor.googleapis.com/SanitizeOperation)) don't directly contain OpenTelemetry `trace` or `spanId` fields. To correlate these logs with user identities and trace spans, you perform a _log join_ in your security information and event management (SIEM) or log processing pipeline by using the session token. 

- **Agent-to-Anywhere (egress) traffic** : When an agent calls an external tool, Model Context Protocol (MCP) server, or external large language model (LLM), 

traffic is routed through Agent Gateway and Secure Web Proxy. For egress calls, when OpenTelemetry instrumentation is enabled, Model Armor `SanitizeOperation` logs do contain the `trace` and `spanId` fields directly. You can directly filter logs and view trace spans in Cloud Trace (/trace/docs/finding-traces) or Agent Registry 

(/gemini-enterprise-agent-platform/optimize/observability/traces#exploring_traces). 

#### Summary of correlation mechanisms

|Flow|Path and routing|Trace in Model Armor<br>log|Correlation method|
|---|---|---|---|
|Client-to-Agent|Direct API call from|The`trace`and`spanId`|Log join using the session|
|(ingress)|Gemini Enterprise to<br>Model Armor|aren't populated.|token from`client_`<br>`correlation_id`and<br>`assistToken`|
|Agent-to-<br>Anywhere (egress)|<br>Routed through Agent<br>Gateway and Secure<br>Web Proxy|The`trace`and`spanId`<br>are populated.|Direct match on`trace`ID<br>and Trace span inspection|

### Before you begin

Before you start correlating Model Armor logs with Gemini Enterprise logs, follow these steps: 

1. Enable Model Armor in Gemini Enterprise (/gemini/enterprise/docs/enable-model-armor). 

2. To generate trace context and view trace details in Gemini Enterprise and Model Armor logs, turn on **Enable instrumentation of OpenTelemetry traces and logs** and, optionally, **Enable logging of prompt inputs and response outputs** in your observability settings. For instructions, see Turn on observability settings 

   - (/gemini/enterprise/docs/manage-observability-settings#turn_on_observability_settings) 

3. For egress traffic screening, configure Model Armor on your Agent Gateway (/gemini-enterprise-agent-platform/govern/configure-model-armor). 

#### Required roles

To get the permissions that you need to view and correlate logs and trace spans, ask your administrator to grant you the following IAM roles on your project: 

- Cloud Trace User (/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) ( `roles/cloudtrace.user` ) 

- Logs Viewer (/iam/docs/roles-permissions/logging#logging.viewer) ( `roles/logging.viewer` ) 

For more information about granting roles, see Manage access to projects, folders, and organizations (/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through custom roles (/iam/docs/creating-custom-roles) or other predefined roles (/iam/docs/roles-overview#predefined). 

For information about other roles you might need, see Trace access control (/trace/docs/iam) and Cloud Logging access control (/logging/docs/access-control). 

### Correlate Client-to-Agent (ingress) logs

A single `StreamAssist` interaction produces three distinct log entries in Cloud Logging: 

**Model Armor sanitization log** **(** **`SanitizeOperation` ):** 

- **Monitored resource:** `modelarmor.googleapis.com/SanitizeOperation` 

- **Properties:** Contains the detailed sanitization verdict and safety findings (such as PII redaction, responsible AI filter matches, or prompt injection detection) but doesn't contain trace context or end-user identity. 

**Correlation key:** 

- `labels."modelarmor.googleapis.com/client_correlation_id"` 

**Gemini Enterprise StreamAssist log (** **`consumed_api` ) :** 

- **Monitored resource:** `consumed_api` 

- **Properties:** Contains the end-user identity ( `userIamPrincipal` ), the trace details ( `trace` and `spanId` ), and the session token ( `response.assistToken` ) . 

- **Correlation key:** `jsonPayload.response.assistToken` 

**Gemini Enterprise ModelArmorAudit Log** **(** **`Agent` ):** 

- **Monitored Resource:** `discoveryengine.googleapis.com/Agent` where `jsonPayload.logMetadata.methodName` is `ModelArmorAudit` . 

- **Properties:** Echoes the high-level sanitization verdict and contains the trace context ( `trace` and `spanId` ) , but doesn't contain detailed findings or correlation IDs. 

**Correlation Key:** `trace` 

#### Correlation join key

Model Armor sanitization logs include a `client_correlation_id` label that has a pipe-delimited structure. The third segment of this label is a base64url-encoded session token that matches the `assistToken` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/str eamAssist#response-body) 

field recorded in the `consumed_api` log for `StreamAssist` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistants/str eamAssist) 

The `client_correlation_id` label has the following format: 

```
AS|ASSISTANT_RESOURCE|SESSION_TOKEN
```

The correlation ID includes the following values: 

- _`ASSISTANT_RESOURCE`_ : the full resource name of the Gemini Enterprise `Assistant` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.engines.assistan ts) 

resource in the following format: 

```
projects/PROJECT/locations/LOCATION/collections/COLLECTION/engines/ENGINE/
assistants/ASSISTANT
```

- _`SESSION_TOKEN`_ : the unique session token that matches the `assistToken` in the `consumed_api` log after base64url padding is normalized. 

#### Matching logic

To correlate a Model Armor sanitization log entry with Gemini Enterprise `StreamAssist` logs, implement the following matching logic in your log processing pipeline: 

1. **Extract the session token from the Model Armor entry** : 

   - a. Locate the `labels` object in the Model Armor entry. 

   - b. Retrieve the value of the 

      - `modelarmor.googleapis.com/client_correlation_id` label. 

   - c. Split the value of this label using the pipe character ( `|` ). 

   - d. Extract the third segment, which represents the base64url-encoded session token. 

2. **Extract the** **`assistToken` value from the** **`StreamAssist` entries** : For each candidate `StreamAssist consumed_api` log entry, follow these steps: 

   - a. Locate the `jsonPayload` object. 

   - b. Extract the token value from the `response.assistToken` field. 

3. **Normalize and compare the tokens** : To compare the tokens, normalize both token strings: 

   - a. Replace all hyphens ( `-` ) with plus signs ( `+` ). 

   - b. Replace all underscores ( `_` ) with forward slashes ( `/` ). 

   - c. Strip any trailing equal signs ( `=` ). 

   - d. If the normalized tokens match, correlate the log entries. 

4. **Extract the correlated data** : If you find a match, extract these fields from the matching entries: 

   - **User IAM identity** : the `userIamPrincipal` field from the `StreamAssist` entry 

   - **Trace ID** : the `trace` field from the `StreamAssist` entry 

   - **Span ID** : the `spanId` field from the `StreamAssist` entry 

   - **Sanitization verdict** : the `sanitizationVerdict` field under `jsonPayload.sanitizationResult` in the Model Armor entry 

#### Python correlation sample

The following Python script demonstrates how to query Cloud Logging for both Model Armor and Gemini Enterprise logs, perform the token normalization and matching, and output the correlated records: 

```
#!/usr/bin/env python3
from datetime import datetime, timedelta, timezone
from google.cloud import logging
Google Cloud project ID
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
```

`# 3. Normalize base64url padding for comparison ma_token_normalized = ma_token.replace("-", "+").replace("_", "/").rstrip("=") # 4. Search for matching assistToken in StreamAssist logs for de in de_consumed_entries: payload = de.get("jsonPayload", {}) de_token = payload.get("response", {}).get("assistToken", "") de_token_normalized = ( de_token.replace("-", "+").replace("_", "/").rstrip("=") ) if ma_token_normalized == de_token_normalized: return { "user": payload.get("userIamPrincipal"), "trace": de.get("trace"), "span_id": de.get("spanId"), "verdict": ( ma_entry.get("jsonPayload", {}) .get("sanitizationResult", {}) .get("sanitizationVerdict") ), } return None def main(): # Initialize Google Cloud Logging Client print(f"Connecting to Google Cloud Logging (Project: {PROJECT_ID})...") client = logging.Client` (https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.c lient.Client.html) `(project=PROJECT_ID) # Calculate ISO timestamp for 1 hour ago one_hour_ago = ( datetime.now(timezone.utc) - timedelta(hours=1) ).strftime("%Y-%m-%dT%H:%M:%SZ") print(f"Filtering logs starting from: {one_hour_ago}") # Build log query filters ma_filter = f""" resource.type="modelarmor.googleapis.com/SanitizeOperation" AND timestamp >= "{one_hour_ago}"` 

```
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
     for entry in client.list_entries
```

(https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.c lient.Client.html#google_cloud_logging_v2_client_Client_list_entries) `(filter_=ma_filter, max_results=100) ] print(f"Found {len(ma_entries)} Model Armor entries.") # Fetch Gemini Enterprise log entries print("Fetching Gemini Enterprise StreamAssist log entries...") de_entries = [ entry.to_api_repr() for entry in client.list_entries` 

(https://docs.cloud.google.com/python/docs/reference/logging/latest/google.cloud.logging_v2.c lient.Client.html#google_cloud_logging_v2_client_Client_list_entries) `(filter_=de_filter, max_results=500) ]` 

```
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

### Correlate Agent-to-Anywhere (egress) logs and trace spans

When an agent executes tool calls (such as interacting with an MCP server or external APIs) that are protected by Agent Gateway and Model Armor, the request is part of Agent-to-Anywhere traffic. 

When OpenTelemetry instrumentation is enabled on the app, the resulting `SanitizeOperation` log entries automatically include the `trace` and `spanId` fields. 

#### Filter egress logs in Cloud Logging

To find all Model Armor sanitization logs that are associated with a specific trace in Cloud Logging, use the following query filter: 

```
resource.type="modelarmor.googleapis.com/SanitizeOperation"
trace="TRACE_ID"
```

Replace _`TRACE_ID`_ with the trace ID from the agent interaction. 

For more information, see View and analyze log entries (/logging/docs/view/logs-explorer-interface). 

#### View trace spans

In Trace or Agent Registry, you can view the execution graph and timelines of the agent interaction. Model Armor generates the following spans: 

**Parent span** : `apply_guardrail "Google Cloud Model Armor"` 

**Child spans** : `Request Path` and `Response Path` 

Each span includes attributes such as policy ID, security decisions, and matched filter violations. For more information, see View Model Armor trace spans 

(/gemini-enterprise-agent-platform/govern/view-model-armor-spans). 

### What's next

- Enable Model Armor in Gemini Enterprise 

- (/gemini/enterprise/docs/enable-model-armor) 

- View Model Armor trace spans 

- (/gemini-enterprise-agent-platform/govern/view-model-armor-spans) 

- Configure logging in Model Armor (/model-armor/configure-logging) 

- Manage observability settings in Gemini Enterprise (/gemini/enterprise/docs/manage-observability-settings) 

Last updated 2026-10-14 UTC. 



## Protect sensitive data in sources

URL: https://docs.cloud.google.com/gemini/enterprise/docs/protect-sensitive-data

This document describes how to apply Sensitive Data Protection content policies to Gemini Enterprise connectors and apps and to Gemini Notebook Enterprise notebooks. 

### About Sensitive Data Protection in Gemini Enterprise

Sensitive Data Protection content policies (/sensitive-data-protection/docs/content-policy) are designed to inspect data for data violations or unwanted content and choose when to allow or block this content. This includes blocking confidential or inappropriate source material, such as preventing sensitive data from being shown to users and blocking file uploads to the assistant or Gemini Notebook Enterprise if they violate policy. This capability enhances the security and safety of your Gemini Enterprise apps by protecting against various risks and ensuring responsible AI practices. 

#### Sensitive Data Protection and Model Armor work together

Sensitive Data Protection and Model Armor work together in Gemini Enterprise to provide a layered security defense for your data. They protect different aspects of your AI interactions. 

Sensitive Data Protection safeguards inbound data 

For data connectors, Sensitive Data Protection prevents sensitive data from being ingested or indexed. Content policies can inspect various content types, including textual content (with OCR for images), image object detection, image safety, rich documents (like PDF, DOCx, PPTx, and XLSx) with embedded images, and metadata labels (Microsoft sensitivity labels and Google Workspace labels). Sensitive Data Protection focuses on ensuring only compliant information enters the system as the source. 

For uploaded sources to the assistant and Gemini Notebook Enterprise, if content violates the content policy, the source is not uploaded. 

Model Armor safeguards the serving path 

Model Armor helps protect the user interaction in Gemini Enterprise by screening prompts before LLM processing and in model responses before delivery to the user. By screening prompts, Model Armor guards against prompt injection and malicious URLs. If a policy is violated, Gemini Enterprise blocks the request and displays an error message. 

For more information about using Model Armor with Gemini Enterprise, see Enable Model Armor (/gemini/enterprise/docs/enable-model-armor). 

#### Supported sources

Sensitive Data Protection content policies can inspect data in connectors (#connectors) , metadata labels (#metadata-labels), and file uploads (#file-uploads). 

Connectors 

You can apply content policies to the following connectors: 

- **Third-party connectors:** Sensitive Data Protection supports both ingestion and federated third-party connectors. For a list of these connectors, see Connect a third-party data source 

- (/gemini/enterprise/docs/connectors/connect-third-party-data-source). 

- **Custom MCP servers:** Sensitive Data Protection supports content in custom Model Context Protocol (MCP) servers. For general information about custom MCP servers, see Set up your custom MCP server data store 

- (/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-server). 

**Google Workspace connectors:** 

- Google Calendar (/gemini/enterprise/docs/connectors/gcal) 

- Google Chat (/gemini/enterprise/docs/connectors/gchat) 

- Google Drive (/gemini/enterprise/docs/connectors/gdrive) 

- Gmail (/gemini/enterprise/docs/connectors/gmail) 

Metadata labels 

Sensitive Data Protection supports two types of metadata labels for certain connectors and uploads: 

- **Microsoft sensitivity labels:** Also known as Purview Information Protection (MSIP) labels, Azure Information Protection (AIP) labels, and Microsoft Information Protection (MIP) labels, these are sensitivity labels applied to Microsoft 365 assets (such as Word, Excel, and Outlook). They embed metadata directly into the file or email header to denote sensitivity (for example, "Highly Confidential" or "Internal Only"). Sensitive Data Protection supports Microsoft sensitivity labels in connectors as follows: 

   - **Microsoft SharePoint** (/gemini/enterprise/docs/connectors/ms-sharepoint) **:** Labels on Office 365 files and PDFs. Microsoft sensitivity labels on other file types, such as SharePoint sites and pages, aren't supported. 

   - **Microsoft OneDrive** (/gemini/enterprise/docs/connectors/ms-onedrive) **:** Labels on Office 365 files and PDFs. 

   - **Microsoft Outlook** (/gemini/enterprise/docs/connectors/ms-outlook) **:** Labels on email messages and calendar events. 

   - **Microsoft Teams** (/gemini/enterprise/docs/connectors/ms-teams) **:** Labels on Office 365 files and PDFs. 

   - **Direct uploads and non-Microsoft connectors:** Labels on Office 365 files and PDFs, if the files contain embedded labels. 

**Google Workspace labels:** These labels are for data classification across Google Workspace. Administrators define custom schemas that users or automated systems can apply to Google Workspace items to classify them (for example, "Confidential" or "Internal"). Sensitive Data Protection supports Google Workspace labels for files in Google Workspace connectors and files uploaded to the Gemini Enterprise assistant from Google Drive. 

File uploads 

When you upload files from a local drive, Google Drive, or Microsoft OneDrive to the assistant or Gemini Notebook Enterprise, Sensitive Data Protection scans the files and blocks uploads that violate the content policy. 

The following table lists the supported file types for scanning: 

|MIME type|Description|
|---|---|
|`application/pdf`|PDF|
|`text/html`|HTML|
|`text/plain`|Plain text|
|`application/json`|JSON|
|`application/vnd.openxmlformats-officedocument.`<br>`wordprocessingml.document`|Microsoft Word (DOCX)|
|`application/vnd.openxmlformats-officedocument.`<br>`presentationml.presentation`|Microsoft PowerPoint (PPTX)|
|`application/vnd.openxmlformats-officedocument.`<br>`spreadsheetml.sheet`|Microsoft Excel (XLSX)|
|`application/vnd.ms-excel.sheet.macroenabled.12`|Microsoft Excel Macro-Enabled<br>Worksheet (XLSM)|
|`application/xml`|XML|
|`image/bmp`|BMP image|
|`image/gif`|GIF image|
|`image/jpeg`|JPEG image|
|`image/png`|PNG image|
|`image/tiff`|TIFF image|
|`image/svg+xml`|SVG image|
|`text/csv`|CSV (Comma-separated values)|
|`text/tab-separated-values`|TSV (Tab-separated values)|

**Note:** Although you can upload video and audio files to the assistant, Sensitive Data Protection doesn't scan these file types. 

#### Supported editions of Gemini Enterprise

You can use Sensitive Data Protection with all Gemini Enterprise editions (/gemini/enterprise/docs/editions) except the Gemini Enterprise Business edition. 

There's no additional cost to use Sensitive Data Protection. 

#### Supported regions

Sensitive Data Protection supports the global, EU, and US multi-regions. 

### Limitations

The following limitations apply to Sensitive Data Protection content policies in Gemini Enterprise: 

- Content policies don't apply to the older type of data store, such as data from Cloud Storage or BigQuery or websites. Only the connectors, which contain entity data, can be protected by content policies. 

- Although you can apply a content policy from one project to Gemini Enterprise in another project, the two projects must be in the same VPC Service Controls perimeter. For general information about VPC Service Controls for Gemini Enterprise, see Secure your app with VPC Service Controls 

- (/gemini/enterprise/docs/use-vpc-service-controls). 

- Google Workspace labels (#metadata-labels) and content scanning aren't supported for uploads to Gemini Notebook Enterprise notebooks. 

- Sensitive Data Protection has limits on file size support that can be different from Gemini Enterprise. For information about the maximum size of PDFs, Office 365 files, text files, and image files, see Content policy limits 

- (/sensitive-data-protection/limits#content-policy-limits). By default, content policies allow content in large files. However, you can configure policies to block content in large files. 

- For Microsoft connectors that contain encrypted files, because neither Gemini Enterprise nor Sensitive Data Protection can decrypt the files, the files aren't scanned for content violations. If users ask questions about the content, Gemini Enterprise can't answer because the content is encrypted. But, if users ask questions that can be answered from any unencrypted snippets and metadata, then Gemini Enterprise does provide those answers. 

### Before you begin

Before you begin, make sure that you have completed the following prerequisites: 

- You have the required roles assigned to you and the Gemini Enterprise service account: 

   - You need the Gemini Enterprise Admin 

   - (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role. 

   - The Gemini Enterprise service account needs the DLP User ( `roles/dlp.user` ) role. 

For more information, see Required roles 

(/sensitive-data-protection/docs/manage-content-policies#required-roles) in _Create and manage content policies_ in the Sensitive Data Protection documentation set. 

**Note:** To grant multiple IAM roles to a service account, see Grant or revoke multiple IAM roles using the Google Cloud console 

(/iam/docs/manage-access-service-accounts#multiple-roles-console). 

You have created a Gemini Enterprise app or have Gemini Notebook Enterprise configured. For more information, see Create an app 

(/gemini/enterprise/docs/create-app) or Set up Gemini Notebook Enterprise 

(/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm). 

### Create a content policy

To prepare a Sensitive Data Protection content policy to apply to a Gemini Enterprise connector or app or to Gemini Notebook Enterprise, do the following: 

1. Create a content policy following the instructions in Create and manage content policies (/sensitive-data-protection/docs/manage-content-policies) in the Sensitive Data Protection documentation. 

Make sure to create the policy in the same region as the apps you want to apply it to. 

2. Make a note of the policy name. To add a policy to a connector, you need the full path, in the form 

### Protect sensitive data in connectors with content policies

To block entity information being shown to users if the entity contains sensitive data, apply a Sensitive Data Protection content policy to the connector, follow the instructions in Apply a content policy to a Gemini Enterprise connector (#apply-policy-connector). 

If you subsequently need to remove the content policy from the connector, see Remove the content policy from a connector (#remove-policy-connector). 

#### Apply a content policy to a Gemini Enterprise connector

Applying a Sensitive Data Protection content policy to a connector prevents Gemini Enterprise from returning entity data that contains sensitive content from the connector. 

For certain types of connectors, applying the content policy can also block the return of entity data based on metadata labels (#metadata-labels). 

**Note:** Applying a Sensitive Data Protection content policy can increase latency. 

- To apply a content policy to a connector, do the following: 

   1. In the Google Cloud console, go to the **Gemini Enterprise** page and then click **Data Stores** . 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

2. Click the name of the connector that you want to apply the policy to. 

3. In the **Content policy** field, enter the full name for the content policy resource. After you enter the policy into the field, it is applied right away. 

**Note:** If you don't have the full policy name, do the following: 

   - a. Open the **Content policy** tooltip and click the link to navigate to the content policies list. 

   - b. If the policy is in a different project from your Gemini Enterprise connector, switch to that project. 

   - c. Click the **Resource name** for the policy and copy the policy's **Name** from the **Content Policy Details** page. Policy names typically look like this: **`projects/myproject/locations/global/contentPolicies/123-abc`** . 

4. Optional: Test the content policy. If you have data in the connector that violates the policy, ask the assistant to tell you about it (/gemini/enterprise/docs/assistant-chat). 

#### Remove the content policy from a connector

To remove a policy from a connector, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page, and then click **Data Stores** . 

Go to the Data Stores page (https://console.cloud.google.com/gemini-enterprise/data-stores) 

2. Click the name of the connector that you want to remove the policy from. 

3. Delete the text in the **Content policy** field, and enter an empty field. 

   - The policy is removed right away. 

### Protect uploads to the assistant with content policies

To protect uploads to the assistant for a Gemini Enterprise app, follow the instructions in Apply a content policy to Gemini Enterprise assistant uploads (#apply-policy-assistant) . 

If you subsequently need to remove a Sensitive Data Protection content policy from the assistant, see Remove the content policy from the assistant 

(#remove-policy-assistant). 

#### Apply a content policy to the assistant uploads

Applying a Sensitive Data Protection content policy to the assistant causes Gemini Enterprise to scan and block files uploaded to the app (from a local device, Google Drive, or Microsoft OneDrive) if they contain content or metadata labels that violate the policy. If a user attempts to upload a file that violates the policy, the upload fails and the file is not added to the session. 

**Note:** Applying a Sensitive Data Protection content policy can increase latency. 

To apply a content policy to assistant uploads, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app that you want to apply the policy to. 

3. Click **Security** . 

4. In the **Sensitive Data Protection configuration** , under the **Assistant setting** , select a content policy from the menu. 

If the content policy isn't in the menu, do one of the following: 

- Click **Switch project** to select a policy from a different project. 

- Click **Enter manually** to enter the path to the policy: `projects/PROJECT_ID/locations/LOCATION/contentPolicies/POLICY_ID` . 

- Click **Create new** to navigate to the **Create Content Policy** page. 

Make sure to choose a policy in the same region as the app. 

5. Click **Save** . 

6. Optional: Test the policy: 

   - a. Create a file that contains a harmless violation of the policy. For example, if the content policy blocks US social security numbers, create a file that contains "999-00-0000". 

   - b. Attempt to upload the file to the app's chat. The upload should fail and the file should be blocked. 

#### Remove the content policy from the assistant

To remove the content policy from assistant uploads for an app, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of the app. 

3. Click **Security** . 

4. In the **Sensitive Data Protection configuration** , under the **Assistant setting** , click the drop-down arrow and select **Enter manually** . 

5. Delete the text in the **Resource Name** field so that the field is empty, and then click **Confirm** . 

6. Click **Save** . 

### Protect uploads to Gemini Notebook Enterprise with a content policy

Applying a content policy to Gemini Notebook Enterprise prevents users from uploading source material that violates the policy. 

Gemini Notebook Enterprise notebooks aren't associated with any particular app. To apply the content policy to all notebooks in a project, you apply it to any app in the 

project. Similarly, if you remove a content policy from any app in the project, none of the notebooks associated with the project are protected by the policy. 

Procedures for adding or removing a Sensitive Data Protection content policy in Gemini Notebook Enterprise: 

- Apply a content policy to Gemini Notebook Enterprise (#apply-nblme) 

- Remove the content policy from Gemini Notebook Enterprise 

- (#remove-nblme-policy) 

#### Apply a content policy to Gemini Notebook Enterprise

Applying a content policy to Gemini Notebook Enterprise prevents users from uploading source material that violates the policy. Gemini Notebook Enterprise notebooks aren't associated with any particular app. To apply the content policy to all notebooks, you apply it to any app in the project. 

**Note:** Applying a Sensitive Data Protection content policy can increase latency. 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of any app in the region for which you want to protect notebooks. 

3. Click **Security** . 

4. In the **Sensitive Data Protection configuration** , under the **NotebookLM setting** , select a content policy from the menu. 

If the content policy isn't in the menu, do one of the following: 

- Click **Switch project** to select a policy from a different project. 

- Click **Enter manually** to enter the path to the policy `projects/` _`PROJECT_ID`_ `/locations/` _`LOCATION`_ `/contentPolicies/` _`POLICY_NAME`_ . 

- Click **Create new** to navigate to the **Create Content Policy** page and follow the instructions above. 

However you specify the policy, make sure to choose a policy in the same region as the app. 

5. Click **Save** . 

6. Wait approximately 10 minutes for the content policy to propagate. Gemini Notebook Enterprise will then start using the specified policy to scan uploaded source documents. 

7. Optional: Test the content policy: 

   - a. Create a source document that contains a harmless violation of the policy. For example, if the content policy blocks US social security numbers, create a source file that says "Mickey Mouse's social security number is 999-000000". 

   - b. Upload the source document to a notebook. If the policy is in effect, the document appears as blocked in the source list. 

#### Remove the content policy from Gemini Notebook Enterprise

To remove the content policy from Gemini Notebook Enterprise so that uploaded source files won't be blocked based on content, do the following: 

1. In the Google Cloud console, go to the Gemini Enterprise page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/) 

2. Click the name of any app in the region. 

3. Click **Security** . 

4. In the **Sensitive Data Protection configuration** , under the **NotebookLM setting** , click the drop-down arrow and select **Enter manually** . 

5. Select the text in the field and press delete so that the **Resource Name** field is empty, then click **Confirm** . 

6. Click **Save** . 

7. Wait approximately 10 minutes for the removal of the content policy to propagate. Gemini Notebook Enterprise will then stop scanning source files for all notebooks in that region and project. 

Last updated 2026-10-14 UTC.
