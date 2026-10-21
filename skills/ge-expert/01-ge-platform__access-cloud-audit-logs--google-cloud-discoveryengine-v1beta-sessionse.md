# Gemini Enterprise: platform, security, agents, cost, monitoring / Access Cloud Audit Logs: API interface audit logs / google.cloud.discoveryengine.v1beta.SessionService to Methods that don't produce audit logs to Refresh structured and unstructured data
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 944-983, extracted 2026-10-18

Contains:
- Access Cloud Audit Logs: API interface audit logs / google.cloud.discoveryengine.v1beta.SessionService to Methods that don't produce audit logs (pages 944-961) https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging
- Access traces and spans (pages 962-969) https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans
- Access metrics (pages 970-980) https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics
- Refresh structured and unstructured data (pages 981-983) https://docs.cloud.google.com/gemini/enterprise/docs/refresh-data

## Access Cloud Audit Logs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SessionService` . 

`CreateSession` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SessionService.CreateSession
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionSer
vice.CreateSession"
```

`DeleteSession` 

**Method** : 

`google.cloud.discoveryengine.v1beta.SessionService.DeleteSession` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.sessions.delete - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionSer
vice.DeleteSession"
```

`GetSession` 

**Method** : `google.cloud.discoveryengine.v1beta.SessionService.GetSession` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionSer
vice.GetSession"
ListSessions
```

**Method** : 

`google.cloud.discoveryengine.v1beta.SessionService.ListSessions` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionSer
vice.ListSessions"
UpdateSession
```

**Method** : 

`google.cloud.discoveryengine.v1beta.SessionService.UpdateSession` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.update - DATA_WRITE
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionSer
vice.UpdateSession"
```

`google.cloud.discoveryengine.v1beta.SiteSearchEngineService` The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SiteSearchEngineService` . 

```
BatchCreateTargetSites
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchCreate
TargetSites
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.targetSites.batchCreate - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.BatchCreateTargetSites"
```

`BatchVerifyTargetSites` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchVerify
TargetSites
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.siteSearchEngines.batchVerifyTargetSites -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.BatchVerifyTargetSites"
```

`CreateSitemap` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateSitem
ap
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.sitemaps.create - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.CreateSitemap"
```

`CreateTargetSite` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateTarge
tSite
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.targetSites.create - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.CreateTargetSite"
```

`DeleteSitemap` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteSitem
ap
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.sitemaps.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.DeleteSitemap"
```

`DeleteTargetSite` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteTarge
tSite
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.targetSites.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.DeleteTargetSite"
DisableAdvancedSiteSearch
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DisableAdva
ncedSiteSearch
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.siteSearchEngines.disableAdvancedSiteSearch -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.DisableAdvancedSiteSearch"
```

`EnableAdvancedSiteSearch` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.EnableAdvan
cedSiteSearch
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.siteSearchEngines.enableAdvancedSiteSearch -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.EnableAdvancedSiteSearch"
FetchDomainVerificationStatus
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchDomain
VerificationStatus
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.siteSearchEngines.fetchDomainVerificationStatus -
ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.FetchDomainVerificationStatus"
```

`FetchSitemaps` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchSitema
ps
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.sitemaps.fetch - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.FetchSitemaps"
```

`GetSiteSearchEngine` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetSiteSear
chEngine
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.siteSearchEngines.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.GetSiteSearchEngine"
```

`GetTargetSite` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetTargetSi
te
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.targetSites.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.GetTargetSite"
```

`ListTargetSites` 

**Method** : 

- `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.ListTargetS ites` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.targetSites.list - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.ListTargetSites"
```

`RecrawlUris` 

**Method** : 

`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.RecrawlUris` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.RecrawlUris"
```

`UpdateTargetSite` 

**Method** : 

- `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.UpdateTarge tSite` 

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.targetSites.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearch
EngineService.UpdateTargetSite"
google.cloud.discoveryengine.v1beta.UserEventService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.UserEventService` . 

```
ImportUserEvents
```

**Method** : 

`google.cloud.discoveryengine.v1beta.UserEventService.ImportUserEvents` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.userEvents.import - DATA_WRITE
```

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventS
ervice.ImportUserEvents"
PurgeUserEvents
```

**Method** : 

`google.cloud.discoveryengine.v1beta.UserEventService.PurgeUserEvents` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.userEvents.purge - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventS
ervice.PurgeUserEvents"
WriteUserEvent
```

**Method** : 

`google.cloud.discoveryengine.v1beta.UserEventService.WriteUserEvent` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.userEvents.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventS
ervice.WriteUserEvent"
google.cloud.discoveryengine.v1beta.UserLicenseService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.UserLicenseService` . 

```
BatchUpdateUserLicenses
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.UserLicenseService.BatchUpdateUserL
icenses
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserLicens
eService.BatchUpdateUserLicenses"
google.cloud.discoveryengine.v1beta.UserStoreService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.UserStoreService` . 

`UpdateUserStore` 

**Method** : 

`google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUserStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.userStores.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserStoreS
ervice.UpdateUserStore"
google.cloud.notebooklm.v1alpha.AudioOverviewService
```

The following audit logs are associated with methods belonging to `google.cloud.notebooklm.v1alpha.AudioOverviewService` . 

`CreateAudioOverview` 

**Method** : 

```
google.cloud.notebooklm.v1alpha.AudioOverviewService.CreateAudioOvervie
w
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.audioOverviews.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.notebooklm.v1alpha.AudioOverviewS
ervice.CreateAudioOverview"
```

`DeleteAudioOverview` 

**Method** : 

```
google.cloud.notebooklm.v1alpha.AudioOverviewService.DeleteAudioOvervie
w
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.audioOverviews.delete - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.notebooklm.v1alpha.AudioOverviewS
ervice.DeleteAudioOverview"
google.cloud.notebooklm.v1alpha.NotebookService
```

The following audit logs are associated with methods belonging to `google.cloud.notebooklm.v1alpha.NotebookService` . 

`CreateNotebook` 

- **Method** : `google.cloud.notebooklm.v1alpha.NotebookService.CreateNotebook` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.notebooks.create - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookServic
e.CreateNotebook"
```

`GetNotebook` 

- **Method** : `google.cloud.notebooklm.v1alpha.NotebookService.GetNotebook` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.notebooks.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookServic
e.GetNotebook"
```

`ListRecentlyViewedNotebooks` 

**Method** : 

```
google.cloud.notebooklm.v1alpha.NotebookService.ListRecentlyViewedNoteb
ooks
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

   - `discoveryengine.notebooks.list - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookServic
e.ListRecentlyViewedNotebooks"
```

`ShareNotebook` 

**Method** : `google.cloud.notebooklm.v1alpha.NotebookService.ShareNotebook` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

   - `discoveryengine.notebooks.getIamPolicy - ADMIN_WRITE discoveryengine.notebooks.setIamPolicy - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookServic
e.ShareNotebook"
google.cloud.notebooklm.v1alpha.SourceService
```

The following audit logs are associated with methods belonging to `google.cloud.notebooklm.v1alpha.SourceService` . 

```
BatchCreateSources
```

**Method** : 

`google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sources.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.notebooklm.v1alpha.SourceService.
BatchCreateSources"
GetSource
```

**Method** : `google.cloud.notebooklm.v1alpha.SourceService.GetSource` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sources.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.notebooklm.v1alpha.SourceService.
GetSource"
```

`google.longrunning.Operations` 

The following audit logs are associated with methods belonging to `google.longrunning.Operations` . 

```
CancelOperation
```

**Method** : `google.longrunning.Operations.CancelOperation` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.operations.cancel - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.longrunning.Operations.CancelOperation"
GetOperation
```

**Method** : `google.longrunning.Operations.GetOperation` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.operations.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.longrunning.Operations.GetOperation"
```

`ListOperations` 

**Method** : `google.longrunning.Operations.ListOperations` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.operations.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.longrunning.Operations.ListOperations"
```

### Methods that don't produce audit logs

- A method might not produce audit logs for one or more of the following reasons: 

   - It is a high volume method involving significant log generation and storage costs. 

   - It has low auditing value. 

   - Another audit or platform log already provides method coverage. 

The following methods don't produce audit logs: 

- `a2a.v1.A2AService.CancelTask` 

- `a2a.v1.A2AService.CreateTaskPushNotificationConfig` 

- `a2a.v1.A2AService.DeleteTaskPushNotificationConfig` 

- `a2a.v1.A2AService.GetTask` 

- `a2a.v1.A2AService.GetTaskPushNotificationConfig` 

- `a2a.v1.A2AService.ListTaskPushNotificationConfig` 

- `a2a.v1.A2AService.TaskSubscription` 

- `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpDeleteR equest` 

- `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpGetRequ est` 

- `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpPostReq uest` 

- `google.cloud.discoveryengine.v1.SearchService.SearchLite google.cloud.discoveryengine.v1.UserEventService.CollectUserEvent` 

- `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpDe leteRequest` 

- `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpGe tRequest` 

- `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpPo stRequest` 

- `google.cloud.discoveryengine.v1alpha.DataConnectorService.StartConnecto rRun` 

- `google.cloud.discoveryengine.v1alpha.SearchService.SearchLite google.cloud.discoveryengine.v1alpha.UserEventService.CollectUserEvent google.cloud.discoveryengine.v1alpha.WidgetService.LookupWidgetConfig` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAcquireAccessT oken` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAcquireAndStor eRefreshToken` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAdvancedComple teQuery` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAnswerQuery google.cloud.discoveryengine.v1alpha.WidgetService.WidgetCompleteQuery google.cloud.discoveryengine.v1alpha.WidgetService.WidgetConverseConver sation` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetCreateSession google.cloud.discoveryengine.v1alpha.WidgetService.WidgetDeleteSession google.cloud.discoveryengine.v1alpha.WidgetService.WidgetDisconnectConn ector` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetExecuteAction google.cloud.discoveryengine.v1alpha.WidgetService.WidgetGetSession` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetHomepageFetchD ocuments` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetListSessions google.cloud.discoveryengine.v1alpha.WidgetService.WidgetSearch` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetStreamAnswerQu ery` 

- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetUpdateSession google.cloud.discoveryengine.v1alpha.WidgetService.WidgetWriteUserEvent google.cloud.discoveryengine.v1beta.SearchService.SearchLite google.cloud.discoveryengine.v1beta.UserEventService.CollectUserEvent` 

Last updated 2026-10-14 UTC. 



## Access traces and spans

URL: https://docs.cloud.google.com/gemini/enterprise/docs/access-traces-and-spans

This document describes how to access and view traces and spans generated by your Gemini Enterprise app. Traces and spans provide detailed insights into the performance and execution flow of requests within your application, such as when using the assistant or agents. 

You can view trace data using either the **Trace Explorer** or directly within individual agents using the agent's **Traces** tab. 

### Key concepts

This section introduces key concepts related to observability in Gemini Enterprise. 

|Concept|Description|
|---|---|
||A trace is a collection of spans that represents a single request or<br>transaction as it flows through different services and components.|
|Trace|For example, a trace represents the entire lifecycle of a request. This<br>includes a user asking a question from the Gemini Enterprise assistant, the<br>Gemini Enterprise assistant responding, and any subsequent actions<br>triggered by the answer, such as sending an email.|
|Span|A span is a single, timed unit of work within a trace. It represents a specific<br>operation, such as a function call, an API request, or a database query. Each<br>span includes details like its start and end times, a unique ID, and its<br>relationship to other spans. These relationships together form a trace.|
|Span logs|Span logs are timestamped, free-form messages or events associated with<br>a specific span. They provide detailed, contextual information about a<br>span's execution, helping users debug issues and understand the flow of a<br>request.|

### Before you begin

Make sure you have the following: 

- The Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role or Google Cloud console Gemini Enterprise User role. 

- An existing Gemini Enterprise web app. For information about creating a new app, see Create an app (/gemini/enterprise/docs/create-app). 

- To access traces, you must have the Cloud Trace User (/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) role ( `roles/cloudtrace.user` ). 

- Enable the **Enable instrumentation of OpenTelemetry traces and logs** observability setting. Depending on the agent type, you enable this in the app-level configurations (for the **Core Assistant** agent) or inside the agent's **Configuration** tab (for **Workflow Builder** employee-made agents and **Deep Research** agents). For more information, see Manage observability settings (/gemini/enterprise/docs/manage-observability-settings). 

### Data retention

Traces and spans generated by your Gemini Enterprise app are stored in Cloud Trace in your Google Cloud project, and their retention is governed by Cloud Trace. By default, Cloud Trace retains span data for **30 days** ; data older than the retention period is automatically deleted. For the authoritative and most current retention values, see Cloud Trace retention periods 

(/trace/docs/quotas#trace-retention-periods) in the Cloud Trace quotas and limits (/trace/docs/quotas) documentation. 

### Access traces in Trace Explorer

To access traces and spans using the Trace Explorer, follow these steps: 

1. In the Google Cloud console, go to the **Trace Explorer** page. 

Go to Trace Explorer (https://console.cloud.google.com/traces/explorer) 

2. Select the Google Cloud project where your Gemini Enterprise app was created. You see all the spans for your project. 

3. In the table, click a **Span ID** to view the trace details, including the span's duration and other attributes. 

**Note:** For more information on using the Trace Explorer, see Find and explore traces (/trace/docs/finding-traces). 

#### Filter and search traces

Within the Trace Explorer for your project, you can isolate and analyze Gemini Enterprise agent and data connector executions using these filters, query parameters, and attributes: 

**Faceted filters** : 

- **Service** : Filter by `AssistantService` or `connectorsexecution` to isolate the platform agent and data connector request paths. 

- **Span** : Filter by `/AssistantService.StreamAssist` to locate the root userturn spans, or search for child spans like `execute_tool <tool_name>` and `invoke_connector <connector>` . 

**Direct Trace ID Lookup** : Find traces directly using the standard 32-character W3C trace ID, which can be extracted from the `x-cloud-trace-context` response headers from `StreamAssist` . 

- **Custom attributes** : Query by the `gemini_enterprise.assist_token` attribute on `execute_tool` or `invoke_connector` spans to map turn-level legacy assist tokens to the W3C trace waterfall. 

- **Resource attributes** : Every exported span carries `cloud.region` , the 

- **Resource attributes** : Every exported span carries the `cloud.region` attribute. This attribute represents the Gemini Enterprise serving location that handled the request, such as `global` , `us` , or `eu` . You can filter by this attribute to compare performance across regions. This comparison is useful when a data connector succeeds in one location but fails in another. This value represents the location serving your app, not the region hosting the thirdparty data source. To apply this filter, see Apply span filters 

- (/trace/docs/finding-traces#apply-span-filters). 

### Access traces for agents

You can also view trace spans directly for individual agents on the agent's **Traces** tab, which displays a detailed chronological summary of span trace records and parent-child execution structures. 

**Note:** The **Traces** tab is available for the **Core Assistant** agent, **Workflow Builder** employee-made agents, and **Deep Research** agents. 

To access traces for an agent: 

1. In the Google Cloud console, navigate to your app, and then click **Agents** . 

2. Select the agent you want to inspect, and then click the **Traces** tab. 

#### Trace summary table

The main table in the **Traces** tab shows the following information for each trace span: 

**Status** : The current status of the trace (currently displays **Unset** ). 

- **Trace span ID** : The unique identifier for the trace span. Click the span ID link to drill down into its details. 

- **Span Name** : A brief description of the work the span is doing. Examples of spans for Gemini Enterprise data connectors include: 

   - `execute_tool <tool_name>` : Emitted during the tool-dispatch layer in the agent runtime (for example, `execute_tool federated_search` ). 

   - `invoke_connector <connector>` : Generated by the connectors execution layer to represent the request logic to the specific connector (for example, `invoke_connector jira` or `invoke_connector servicenow` ), which replaces the default service-side RPC spans. 

- **Span Type** : The type of span. Options include: 

   - `Agent to Tool` : An invocation from the agent to an external tool (reused for `execute_tool` and `invoke_connector` operations). 

   - `Invoke Agent` : An invocation of an agent. 

   - `Agent to Model` : A request from the agent to a large language model. 

- **Duration** : The time taken to complete the trace span (in minutes). 

- **Input** : The input data or message sent to the span, if any. 

- **Output** : The output result returned by the span, if any. 

- **Start Time** : The exact timestamp when the span began execution. 

#### Detailed trace view

Clicking a **Trace span ID** opens a detailed page featuring: 

1. **Summary** : View the baseline metadata including **Start time** , **Duration** , and total **Spans** count. You can click to **View in Cloud Trace** or switch between **Graph** and **Timeline** view buttons. 

2. **Visualizations** : Toggle between a graphical hierarchy or a timeline view showing parent-child relationships of all trace spans. 

3. **Selected span details** : Select a single span to display detailed sections, which can include: 

- **Summary** : Displays the name of the span, target service, count of total spans with this action, and total duration (in seconds). 

- **Logs** : View relevant event details if configured. Click **View logs** to navigate directly to standard logs. 

- **Evaluation** : Shows any evaluation results, if configured. 

- **Input & Output** : Complete request and response payloads. 

- **Logs & Events** : List of events that occurred during this span execution. 

- **Stacktraces** : Error details if a span execution fails. 

- **Metadata & Links** : Links referencing related cloud explorer entities. 

- **Attributes** : Resource tags and additional key-value observability parameters. 

#### Parent-child span hierarchy

For data connectors execution, parent-child span nesting within a single W3C trace helps pinpoint exactly where latency or errors occur: 

1. `/AssistantService.StreamAssist` : Root C++ platform span initiating the request. 

2. `invoke_agent core_assistant` : The agent execution span. 

3. `execute_tool <tool_name>` : The active tool execution span (for example, `execute_tool federated_search` ). 

4. `invoke_connector <connector_name>` (for example, `invoke_connector jira` or `invoke_connector servicenow` ) : The connectors execution span, representing the request lifecycle to the third-party endpoint. 

### Experimental generative AI semantic convention telemetry

**Warning:** The generative AI semantic convention telemetry described in this section is experimental. The attributes, schemas, and formats are subject to change in future releases. 

In addition to the stable telemetry, Gemini Enterprise trace spans include richer metadata based on the OpenTelemetry generative AI semantic conventions (https://github.com/open-telemetry/semantic-conventions-genai/blob/main/docs/genai/README.md) 

. OpenTelemetry classifies these conventions as Development status 

(https://opentelemetry.io/docs/specs/otel/document-status). That status applies to earlystage specifications that can change or be removed and shouldn't be relied on in production. Because these conventions aren't yet stable, this Gemini Enterprise telemetry is experimental. These spans include `gen_ai.*` attributes that describe agent, model, and tool activity, such as agent and tool execution and prompt-andresponse steps. 

Prompt and response content in trace spans (such as prompt text and generated answers) appears only when your observability settings allow logging of prompt inputs and response outputs. Otherwise, the content is redacted or omitted. To change these settings, see Manage observability settings 

(/gemini/enterprise/docs/manage-observability-settings). 



## Access metrics

URL: https://docs.cloud.google.com/gemini/enterprise/docs/access-metrics

This document describes how to access the metrics generated by your Gemini Enterprise app. These metrics provide insights into the performance and health of your application. 

You can view metric telemetry using either the **Metrics Explorer** or directly within individual agents using the agent's **Observability** tab. 

### Key concepts

This section introduces key concepts related to observability in Gemini Enterprise. 

|Concept|Description|
|---|---|
|Metrics|Metrics are numerical measurements that systems collect over time. These<br>measurements represent the performance, resource utilization, or behavior<br>of a system. Engineers use metrics to monitor system health, identify<br>trends, and trigger alerts.|
|Agent-scoped<br>metrics|Metrics that measure the activity of an individual agent, such as its<br>sessions, conversational turns, and tool invocations. They are listed under<br>the Gemini Enterprise Agent resource type, and they are collected only<br>when the Enable instrumentation of OpenTelemetry traces and logs<br>observability setting is turned on for that agent.|
|App-scoped<br>metrics|Metrics that measure all traffic to an app rather than to a single agent, such<br>as its request count and end-to-end latency. They are listed under the<br>Gemini Enterprise Engine resource type, where_Engine_is the API name for a<br>Gemini Enterprise app, and they are collected regardless of the<br>observability settings.|

### Before you begin

Make sure you have the following: 

- The Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role or Google Cloud console Gemini Enterprise User role. 

- An existing Gemini Enterprise web app. For information about creating a new app, see Create an app (/gemini/enterprise/docs/create-app). 

- To access the Metrics Explorer, you must have the Monitoring Viewer (/monitoring/access-control#monitoring.viewer) role ( `roles/monitoring.viewer` ). 

- Enable the **Enable instrumentation of OpenTelemetry traces and logs** observability setting. Depending on the agent type, enable this in the applevel configurations (for the **Core Assistant** agent) or inside the agent's **Configuration** tab (for Workflow Builder employee-made agents and Deep Research agents). For more information, see Manage observability settings (/gemini/enterprise/docs/manage-observability-settings). This setting is required for the agent-scoped metrics. The app-scoped metrics, which are listed under the **Gemini Enterprise Engine** resource type, are collected without it. 

### Data retention

Metrics generated by your Gemini Enterprise app are stored in Cloud Monitoring in your Google Cloud project, and their retention is governed by Cloud Monitoring. Gemini Enterprise metrics are published under the `discoveryengine.googleapis.com/` prefix, which falls under the "all other Google Cloud metrics" tier and is retained for **6 weeks** by default. Data older than the retention period is automatically deleted. For the authoritative and most current retention values, see Data retention (/monitoring/quotas#data_retention) in the Cloud Monitoring quotas and limits (/monitoring/quotas) documentation. 

### Access metrics in Metrics Explorer

To access the metrics, follow these steps: 

1. In the Google Cloud console, go to the **Metrics Explorer** page. 

Go to Metrics Explorer (https://console.cloud.google.com/monitoring/metrics-explorer) 

2. Select the Google Cloud project where your Gemini Enterprise app was created. 

3. Click **Select a metric** to open a search bar. 

4. In the search bar, look for the following metrics: 

**Note:** Metrics data refreshes every minute. Metric names are prefixed with the resource they are scoped to. Your app is represented by the **Gemini Enterprise Engine** resource type, which is the API name for a Gemini Enterprise app. 

Metric Name Description Gemini Enterprise Agent - The number of sessions handled by the Gemini Enterprise Gemini Enterprise Agent Agent. Session Count Gemini Enterprise Agent - The number of times tools were invoked by the Gemini Gemini Enterprise Agent Tool Enterprise Agent. Count Gemini Enterprise Agent - The number of conversational turns within Gemini Gemini Enterprise Agent Turn Enterprise Agent sessions. Count Gemini Enterprise Agent - The total latency of responses from the Gemini Enterprise Gemini Enterprise Agent Total Agent. Latency 

|Gemini Enterprise Agent -<br>Gemini Enterprise Agent Tool<br>Total Latency|The total latency incurred by tool executions within the<br>Gemini Enterprise Agent.|
|---|---|
|Gemini Enterprise<br>DataConnector - Gemini<br>Enterprise DataConnector<br>Request Count|The total count of requests made to the Gemini Enterprise<br>data connectors (also referred to as data stores in the<br>Google Cloud console).|
|Gemini Enterprise|(Beta) The latency of requests made to the Gemini|
|DataConnector - Gemini<br>Enterprise DataConnector<br>Request Latencies|Enterprise data connectors (also referred to as data stores<br>in the Google Cloud console) in milliseconds.|

|Metric Name|Description|
|---|---|
|Gemini Enterprise Engine -<br>Gemini Enterprise Engine<br>Request Count|The total number of requests received by your Gemini<br>Enterprise app, across all traffic to the app rather than a<br>single agent. Broken down by API method, canonical gRPC<br>response code, response code class, query type, and<br>model.|
|Gemini Enterprise Engine -<br>Gemini Enterprise Engine<br>Request Total Latency|The distribution of end-to-end request latency for your<br>Gemini Enterprise app. Recorded for every request,<br>including requests that return an error.|
|Gemini Enterprise Engine -<br>Gemini Enterprise Engine<br>Time to First Answer Latency|The distribution of latency between receiving a request and<br>streaming the first answer token. Recorded only for<br>requests that produce at least one answer token.|
|Gemini Enterprise Engine -<br>Gemini Enterprise Engine<br>Time to First Token Latency|The distribution of latency between receiving a request and<br>streaming the first token, whether that token is part of the<br>model's thinking process or a final answer. Recorded only<br>for requests that produce at least one streamed token.|

5. Select the metric you want to explore and click **Apply** . 

6. Optionally, set additional label filters, aggregation elements, and adjust the time range. 

**Note:** For more information on using the Metrics Explorer, see Create charts with Metrics Explorer (/monitoring/charts/metrics-explorer). 

### Access metrics for agents

You can also view operational, tool-specific, and session metric dashboards directly for individual agents on the agent's **Observability** tab in the Google Cloud console. 

**Note:** The **Observability** tab is available for the **Core Assistant** agent, **Workflow Builder** agents, and **Deep Research** agents. 

To access metrics for an agent: 

1. In the Google Cloud console, navigate to your app, and then click **Agents** . 

2. Select the agent you want to inspect, and then click the **Observability** tab. 

The **Observability** tab provides key operational telemetry divided into four views: **Overview** , **Tools** , **Latency** , and **Error rate** . 

#### Overview metrics

This view provides a dashboard summarizing standard session and agent health data, which includes: 

**Sessions** : Total user session count. 

- **Avg. time per session** : Average time elapsed during a session. 

- **Agent invocations** : Total times that the agent was called. 

- **Agent latency** : Latency across time and specific metrics. 

- **Agent traffic** : Inbound request volume. 

- **Agent error rate** : Percentage of failed agent invocations. 

#### Tools metrics

This view focuses specifically on the usage and latency of tools connected to your agent, which includes: 

- **Total calls** : Number of tool execution requests. 

- **P95 duration by tool** : The 95th percentile latency of executions, categorized by tool. 

- **Count of calls by tool** : Total call count divided among different tools. 

- **Error rate by tool** : The failure rate of executions by tool. 

- **"No tool called" rate** : The rate at which interactions did not trigger any tool execution. 

#### Latency metrics

This view displays your agent's response latency. Each metric is shown as a p50 and p95 summary card for the selected time range, and as a time-series chart showing trends over time. You can also filter the latency metrics by feature. The view displays the following metrics: 

- **Time to First Token (TTFT)** : The latency between receiving a request and streaming the first token, whether that token is part of the model's thinking process or of the answer. 

- **Time to First Answer (TTFA)** : The latency between receiving a request and streaming the first answer token, which is the first token that isn't part of the model's thinking. If the agent calls a tool after it starts answering, the measurement restarts, so TTFA reflects when the answer that the user reads began streaming, not any interim narration. 

- **Time to Last Token (TTLT)** : The latency between receiving a request and streaming the last token, which is when the response is complete. 

Filter latency metrics by feature 

A feature is the kind of interaction that a turn represents, such as a web search or an image generation. Filter the latency metrics by feature to see which kinds of interaction are slowest, and to keep one slow feature from skewing your overall latency. 

To filter the latency metrics by feature: 

1. On the agent's **Observability** tab, click the **Latency** view. 

2. Click **Filter by feature** . 

3. Select the feature that you want to inspect. 

The summary cards and the time-series charts then show only the turns for that feature. 

To compare all of the features at once, use the **Features telemetry** table, which lists the following for each feature: 

- **Share of traffic** : The percentage of turns attributed to the feature. 

- **TTFT** , **TTFA** , and **TTLT** : The p50 and p95 latency for the feature. 

You can filter using the following features: 

- **Parametric** : Interactions that send requests to the model for text output only, without tools, such as translation tasks. 

- **Media generation** : Image and video generation tasks. 

- **Web search only** : Interactions that send requests to the model using the web search tool. 

- **Uploaded file analysis** : Interactions that send requests to the model alongside user-uploaded files. 

- **Connector** : Queries that send requests to internal or third-party connectors. 

- **Canvas** : Generation tasks that use Canvas. 

- **Skill** : Interactions that invoke a skill. 

- **Other** : A catch-all for turns that span several features or that are not yet classified. 

#### Error rate metrics

This view shows how your agent's requests resolve, grouped by response class: **OK (2xx)** , **Client errors (4xx)** , **Server errors (5xx)** , and **Canceled** . It includes: 

- **Request volume by response class** : Inbound request count over time, stacked by response class. 

- **Error rate by response class** : The percentage of requests that failed over time, split by response class. 

- **Client error codes (4xx)** and **Server error codes (5xx)** : The individual canonical gRPC response codes over time, such as `INVALID_ARGUMENT` or `INTERNAL` , so you can tell which specific errors drive a spike. 

- **Totals** : The number of requests and the percentage of total requests for each outcome over the selected time range, with separate tables that rank the individual client and server error codes. 

### What's next

- Create dashboards with the Gemini Enterprise metrics. For more information, see Create and manage custom dashboards (/monitoring/charts/dashboards). 

- Create alerts when metrics cross a threshold. For more information, see Create metric-threshold alerting policies (/monitoring/alerts/using-alerting-ui) 

- To turn off Metrics Explorer tracking, see Turn off observability settings 

- (/gemini/enterprise/docs/manage-observability-settings#turn_off_observability_settings). 

Last updated 2026-10-14 UTC. 



## Refresh structured and unstructured data

URL: https://docs.cloud.google.com/gemini/enterprise/docs/refresh-data

This page describes refreshing structured (#refresh-structured) and unstructured (#refresh-unstructured) data. 

### Refresh structured data

You can refresh the data in a structured data store as long as you use a schema that is the same or backward compatible with the schema in the data store. For example, adding only new fields to an existing schema is backward compatible. 

You can refresh structured data in the Google Cloud console or using the API. 

ConsoleREST (#rest)Python (#python) (#console) 

To use the Google Cloud console to refresh structured data from a branch of a data store, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/apps) 

2. In the navigation menu, click **Data Stores** . 

3. In the **Name** column, click the data store that you want to edit. 

4. On the **Documents** tab, click **Import data** . 

5. To refresh from Cloud Storage: 

   - a. In the **Select a data source** pane, select **Cloud Storage** . 

   - b. In the **Import data from Cloud Storage** pane, click **Browse** , select the bucket that contains your refreshed data, and then click **Select** . Alternatively, enter the bucket location directly in the **gs://** field. 

   - c. Under **Data Import Options** , select an import option. 

   - d. Click **Import** . 

6. To refresh from BigQuery: 

   - a. In the **Select a data source** pane, select **BigQuery** . 

   - b. In the **Import data from BigQuery** pane, click **Browse** , select a table that contains your refreshed data, and then click **Select** . Alternatively, enter the table location directly in the **BigQuery path** field. 

   - c. Under **Data Import Options** , select an import option. 

   - d. Click **Import** . 

### Refresh unstructured data

You can refresh unstructured data in the Google Cloud console or using the API. 

ConsoleREST (#rest)Python (#python) (#console) 

To use the Google Cloud console to refresh unstructured data from a branch of a data store, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

Gemini Enterprise (https://console.cloud.google.com/gemini-enterprise/apps) 

2. In the navigation menu, click **Data Stores** . 

3. In the **Name** column, click the data store that you want to edit. 

4. On the **Documents** tab, click **Import data** . 

5. To ingest from a Cloud Storage bucket (with or without metadata): 

   - a. In the **Select a data source** pane, select **Cloud Storage** . 

   - b. In the **Import data from Cloud Storage** pane, click **Browse** , select the bucket that contains your refreshed data, and then click 

**Select** . Alternatively, enter the bucket location directly in the **`gs://`** field. 

   - c. Under **Data Import Options** , select an import option. 

   - d. Click **Import** . 

6. To ingest from BigQuery: 

   - a. In the **Select a data source** pane, select **BigQuery** . 

   - b. In the **Import data from BigQuery** pane, click **Browse** , select a table that contains your refreshed data, and then click **Select** . Alternatively, enter the table location directly in the **BigQuery path** field. 

   - c. Under **Data Import Options** , select an import option. 

   - d. Click **Import** . 

Last updated 2026-10-14 UTC.
