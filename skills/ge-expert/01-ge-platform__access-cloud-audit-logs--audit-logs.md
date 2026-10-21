# Gemini Enterprise: platform, security, agents, cost, monitoring / Access Cloud Audit Logs: Access Cloud Audit Logs to API interface audit logs / google.cloud.discoveryengine.v1.DataStoreService
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 752-791, extracted 2026-10-18

## Access Cloud Audit Logs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging

This document lists the audited methods for Gemini Enterprise. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

- Types of audit logs (/logging/docs/audit#types) 

- Audit log entry structure (/logging/docs/audit#audit_log_entry_structure) Storing and routing audit logs (/logging/docs/audit#storing_and_routing_audit_logs) Cloud Logging pricing summary (/stackdriver/pricing#logs-pricing-summary) Enable Data Access audit logs (/logging/docs/audit/configure-data-access) 

### Service name

To view the Gemini Enterprise audit logs, do the following: 

1. In the Google Cloud console, go to the Logs Explorer page: 

Go to Logs Explorer (https://console.cloud.google.com/logs/query) 

2. Copy and paste the following query into the **Query** field of the Logs Explorer, and then click **Run query** . 

```
   protoPayload.serviceName="discoveryengine.googleapis.com"
```

### Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ` , `ADMIN_WRITE` , `DATA_READ` , or `DATA_WRITE` . When you call a method, Gemini Enterprise generates an audit log whose category is dependent on 

the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ` , `DATA_WRITE` , or `ADMIN_READ` generate Data Access (/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate Admin Activity (/logging/docs/audit#admin-activity) audit logs. 

API methods in the following list that are marked with (LRO) are long-running operations (LROs). These methods usually generate two audit log entries: one when the operation starts and another when it ends. For more information see Audit logs for long-running operations (/logging/docs/audit/understanding-audit-logs#lro). 

Permission Methods type 

```
ADMIN_READa2a.v1.A2AService.GetAgentCard
google.cloud.discoveryengine.v1.AclConfigService.GetAclConfig
google.cloud.discoveryengine.v1.AssistantService.GetAssistant
google.cloud.discoveryengine.v1.AssistantService.ListAssistants
google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfig
google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigs
google.cloud.discoveryengine.v1.DataConnectorService.GetData
Connector
google.cloud.discoveryengine.v1.DataStoreService.GetDataStore
google.cloud.discoveryengine.v1.DataStoreService.ListDataStores
google.cloud.discoveryengine.v1.EngineService.GetEngine
google.cloud.discoveryengine.v1.EngineService.GetIamPolicy
google.cloud.discoveryengine.v1.EngineService.ListEngines
google.cloud.discoveryengine.v1.LicenseConfigService.GetLicense
Config
google.cloud.discoveryengine.v1.SchemaService.GetSchema
google.cloud.discoveryengine.v1.SchemaService.ListSchemas
google.cloud.discoveryengine.v1.ServingConfigService.GetServing
Config
google.cloud.discoveryengine.v1.ServingConfigService.ListServing
Configs
google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchDomain
VerificationStatus
google.cloud.discoveryengine.v1.SiteSearchEngineService.GetSite
SearchEngine
google.cloud.discoveryengine.v1.SiteSearchEngineService.GetTarget
Site
google.cloud.discoveryengine.v1.SiteSearchEngineService.ListTarget
Sites
google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig
google.cloud.discoveryengine.v1alpha.AclConfigService.GetAclConfig
google.cloud.discoveryengine.v1alpha.AssistantService.GetAssistant
google.cloud.discoveryengine.v1alpha.AssistantService.List
Assistants
google.cloud.discoveryengine.v1alpha.AuthorizationService.Get
Authorization
google.cloud.discoveryengine.v1alpha.AuthorizationService.List
Authorizations
google.cloud.discoveryengine.v1alpha.BranchService.GetBranch
google.cloud.discoveryengine.v1alpha.BranchService.ListBranches
google.cloud.discoveryengine.v1alpha.CannedQueryService.GetCanned
Query
google.cloud.discoveryengine.v1alpha.CannedQueryService.ListCanned
Queries
google.cloud.discoveryengine.v1alpha.CmekConfigService.GetCmek
```

`Config google.cloud.discoveryengine.v1alpha.CmekConfigService.ListCmek Configs google.cloud.discoveryengine.v1alpha.CollectionService.Get Collection google.cloud.discoveryengine.v1alpha.CollectionService.GetIamPolicy google.cloud.discoveryengine.v1alpha.CollectionService.List Collections google.cloud.discoveryengine.v1alpha.DataConnectorService.Get ConnectorSecret google.cloud.discoveryengine.v1alpha.DataConnectorService.GetData Connector google.cloud.discoveryengine.v1alpha.DataConnectorService.List ConnectorRuns google.cloud.discoveryengine.v1alpha.DataStoreService.GetCompletion Config google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStore google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocument ProcessingConfig google.cloud.discoveryengine.v1alpha.DataStoreService.GetIamPolicy google.cloud.discoveryengine.v1alpha.DataStoreService.ListData Stores google.cloud.discoveryengine.v1alpha.EngineService.GetEngine google.cloud.discoveryengine.v1alpha.EngineService.GetIamPolicy google.cloud.discoveryengine.v1alpha.EngineService.GetWorkspace Settings google.cloud.discoveryengine.v1alpha.EngineService.ListEngines google.cloud.discoveryengine.v1alpha.EstimateBillingService. EstimateDataSize` (LRO) `google.cloud.discoveryengine.v1alpha.LicenseConfigService.Get BillingAccountLicenseConfig google.cloud.discoveryengine.v1alpha.LicenseConfigService.Get LicenseConfig google.cloud.discoveryengine.v1alpha.ProjectService.ReportConsent Change google.cloud.discoveryengine.v1alpha.SchemaService.GetSchema google.cloud.discoveryengine.v1alpha.SchemaService.ListSchemas google.cloud.discoveryengine.v1alpha.ServingConfigService.Get ServingConfig google.cloud.discoveryengine.v1alpha.ServingConfigService.List ServingConfigs google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Fetch DomainVerificationStatus google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Get SiteSearchEngine` 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Get
TargetSite
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetUri
PatternDocumentData
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.List
TargetSites
google.cloud.discoveryengine.v1alpha.UserLicenseService.ExportUser
Licenses
google.cloud.discoveryengine.v1alpha.WidgetConfigService.GetWidget
Config
google.cloud.discoveryengine.v1beta.AclConfigService.GetAclConfig
google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant
google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants
google.cloud.discoveryengine.v1beta.CmekConfigService.GetCmekConfig
google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmek
Configs
google.cloud.discoveryengine.v1beta.DataStoreService.GetDataStore
google.cloud.discoveryengine.v1beta.DataStoreService.ListDataStores
google.cloud.discoveryengine.v1beta.EngineService.GetEngine
google.cloud.discoveryengine.v1beta.EngineService.GetIamPolicy
google.cloud.discoveryengine.v1beta.EngineService.ListEngines
google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicense
Config
google.cloud.discoveryengine.v1beta.SchemaService.GetSchema
google.cloud.discoveryengine.v1beta.SchemaService.ListSchemas
google.cloud.discoveryengine.v1beta.ServingConfigService.GetServing
Config
google.cloud.discoveryengine.v1beta.ServingConfigService.List
ServingConfigs
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Fetch
DomainVerificationStatus
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetSite
SearchEngine
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Get
TargetSite
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.List
TargetSites
google.cloud.notebooklm.v1alpha.NotebookService.ListRecentlyViewed
Notebooks
google.longrunning.Operations.GetOperation
google.longrunning.Operations.ListOperations
```

`ADMIN_WRITE google.cloud.discoveryengine.v1.AclConfigService.UpdateAclConfig google.cloud.discoveryengine.v1.AssistantService.CreateAssistant google.cloud.discoveryengine.v1.AssistantService.DeleteAssistant google.cloud.discoveryengine.v1.AssistantService.UpdateAssistant google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfig` (LRO) `google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfig` (LRO) `google.cloud.discoveryengine.v1.CollectionService.DeleteCollection` (LRO) `google.cloud.discoveryengine.v1.DataConnectorService.SetUpData Connector` (LRO) `google.cloud.discoveryengine.v1.DataConnectorService.UpdateData Connector google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore` (LRO) `google.cloud.discoveryengine.v1.DataStoreService.DeleteDataStore` (LRO) `google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore google.cloud.discoveryengine.v1.EngineService.CreateEngine` (LRO) `google.cloud.discoveryengine.v1.EngineService.DeleteEngine` (LRO) `google.cloud.discoveryengine.v1.EngineService.SetIamPolicy google.cloud.discoveryengine.v1.EngineService.UpdateEngine google.cloud.discoveryengine.v1.IdentityMappingStoreService.Create IdentityMappingStore google.cloud.discoveryengine.v1.IdentityMappingStoreService.Delete IdentityMappingStore` (LRO) `google.cloud.discoveryengine.v1.LicenseConfigService.CreateLicense Config google.cloud.discoveryengine.v1.LicenseConfigService.Distribute LicenseConfig google.cloud.discoveryengine.v1.LicenseConfigService.RetractLicense Config google.cloud.discoveryengine.v1.LicenseConfigService.UpdateLicense Config google.cloud.discoveryengine.v1.ProjectService.ProvisionProject` (LRO) `google.cloud.discoveryengine.v1.SchemaService.CreateSchema` (LRO) `google.cloud.discoveryengine.v1.SchemaService.DeleteSchema` (LRO) `google.cloud.discoveryengine.v1.SchemaService.UpdateSchema` (LRO) `google.cloud.discoveryengine.v1.ServingConfigService.CreateServing Config google.cloud.discoveryengine.v1.ServingConfigService.DeleteServing Config google.cloud.discoveryengine.v1.ServingConfigService.UpdateServing` 

`Config google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchVerify TargetSites` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.Create Sitemap google.cloud.discoveryengine.v1.SiteSearchEngineService.Create TargetSite` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.Delete Sitemap google.cloud.discoveryengine.v1.SiteSearchEngineService.Delete TargetSite` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.Disable AdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.Enable AdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.RecrawlUris` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.Update TargetSite` (LRO) `google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUser Licenses` (LRO) `google.cloud.discoveryengine.v1.UserStoreService.UpdateUserStore google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidget Config google.cloud.discoveryengine.v1alpha.AclConfigService.UpdateAcl Config google.cloud.discoveryengine.v1alpha.AgentService.CreateAgent google.cloud.discoveryengine.v1alpha.AgentService.DeleteAgent` (LRO) `google.cloud.discoveryengine.v1alpha.AgentService.UpdateAgent google.cloud.discoveryengine.v1alpha.AlphaEvolveService.DeleteAlpha EvolveExperimentAndPrograms google.cloud.discoveryengine.v1alpha.AssistantService.Create Assistant google.cloud.discoveryengine.v1alpha.AssistantService.Delete Assistant google.cloud.discoveryengine.v1alpha.AssistantService.Update Assistant google.cloud.discoveryengine.v1alpha.AuthorizationService.Create Authorization google.cloud.discoveryengine.v1alpha.AuthorizationService.Delete Authorization google.cloud.discoveryengine.v1alpha.AuthorizationService.Update Authorization google.cloud.discoveryengine.v1alpha.CannedQueryService.Create CannedQuery` 

`google.cloud.discoveryengine.v1alpha.CannedQueryService.Delete CannedQuery google.cloud.discoveryengine.v1alpha.CannedQueryService.Update CannedQuery google.cloud.discoveryengine.v1alpha.CmekConfigService.DeleteCmek Config` (LRO) `google.cloud.discoveryengine.v1alpha.CmekConfigService.UpdateCmek Config` (LRO) `google.cloud.discoveryengine.v1alpha.CollectionService.Delete Collection` (LRO) `google.cloud.discoveryengine.v1alpha.CollectionService.SetIamPolicy google.cloud.discoveryengine.v1alpha.CollectionService.Update Collection` (LRO) `google.cloud.discoveryengine.v1alpha.DataConnectorService.SetUpData Connector` (LRO) `google.cloud.discoveryengine.v1alpha.DataConnectorService.Update DataConnector google.cloud.discoveryengine.v1alpha.DataStoreService.AddPatient Filter` (LRO) `google.cloud.discoveryengine.v1alpha.DataStoreService.CreateData Store` (LRO) `google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteData Store` (LRO) `google.cloud.discoveryengine.v1alpha.DataStoreService.DeletePatient Filters google.cloud.discoveryengine.v1alpha.DataStoreService.RemovePatient Filter google.cloud.discoveryengine.v1alpha.DataStoreService.Replace PatientFilter` (LRO) `google.cloud.discoveryengine.v1alpha.DataStoreService.SetIamPolicy google.cloud.discoveryengine.v1alpha.DataStoreService.Update CompletionConfig google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateData Store google.cloud.discoveryengine.v1alpha.DataStoreService.Update DocumentProcessingConfig google.cloud.discoveryengine.v1alpha.EngineService.CreateEngine` (LRO) `google.cloud.discoveryengine.v1alpha.EngineService.DeleteEngine` (LRO) `google.cloud.discoveryengine.v1alpha.EngineService.SetIamPolicy google.cloud.discoveryengine.v1alpha.EngineService.UpdateEngine google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService. CreateIdentityMappingStore google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.` 

`DeleteIdentityMappingStore` (LRO) `google.cloud.discoveryengine.v1alpha.LicenseConfigService.Create LicenseConfig google.cloud.discoveryengine.v1alpha.LicenseConfigService. DistributeLicenseConfig google.cloud.discoveryengine.v1alpha.LicenseConfigService.Retract LicenseConfig google.cloud.discoveryengine.v1alpha.LicenseConfigService.Update LicenseConfig google.cloud.discoveryengine.v1alpha.ProjectService.Provision Project` (LRO) `google.cloud.discoveryengine.v1alpha.ProjectService.UpdateProject google.cloud.discoveryengine.v1alpha.SchemaService.CreateSchema` (LRO) `google.cloud.discoveryengine.v1alpha.SchemaService.DeleteSchema` (LRO) `google.cloud.discoveryengine.v1alpha.SchemaService.UpdateSchema` (LRO) `google.cloud.discoveryengine.v1alpha.ServingConfigService.Create ServingConfig google.cloud.discoveryengine.v1alpha.ServingConfigService.Delete ServingConfig google.cloud.discoveryengine.v1alpha.ServingConfigService.Update ServingConfig google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Batch VerifyTargetSites` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Create Sitemap google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Create TargetSite` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Delete Sitemap google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Delete TargetSite` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService. DisableAdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Enable AdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService. RecrawlUris` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.SetUri PatternDocumentData` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Update TargetSite` (LRO) `google.cloud.discoveryengine.v1alpha.UserLicenseService.BatchUpdate` 

`UserLicenses` (LRO) `google.cloud.discoveryengine.v1alpha.UserStoreService.UpdateUser Store google.cloud.discoveryengine.v1alpha.WidgetConfigService.Update WidgetConfig google.cloud.discoveryengine.v1beta.AclConfigService.UpdateAcl Config google.cloud.discoveryengine.v1beta.AssistantService.Create Assistant google.cloud.discoveryengine.v1beta.AssistantService.Delete Assistant google.cloud.discoveryengine.v1beta.AssistantService.Update Assistant google.cloud.discoveryengine.v1beta.CmekConfigService.DeleteCmek Config` (LRO) `google.cloud.discoveryengine.v1beta.CmekConfigService.UpdateCmek Config` (LRO) `google.cloud.discoveryengine.v1beta.DataStoreService.CreateData Store` (LRO) `google.cloud.discoveryengine.v1beta.DataStoreService.DeleteData Store` (LRO) `google.cloud.discoveryengine.v1beta.DataStoreService.UpdateData Store google.cloud.discoveryengine.v1beta.EngineService.CreateEngine` (LRO) `google.cloud.discoveryengine.v1beta.EngineService.DeleteEngine` (LRO) `google.cloud.discoveryengine.v1beta.EngineService.SetIamPolicy google.cloud.discoveryengine.v1beta.EngineService.UpdateEngine google.cloud.discoveryengine.v1beta.IdentityMappingStoreService. CreateIdentityMappingStore google.cloud.discoveryengine.v1beta.IdentityMappingStoreService. DeleteIdentityMappingStore` (LRO) `google.cloud.discoveryengine.v1beta.LicenseConfigService.Create LicenseConfig google.cloud.discoveryengine.v1beta.LicenseConfigService.Distribute LicenseConfig google.cloud.discoveryengine.v1beta.LicenseConfigService.Retract LicenseConfig google.cloud.discoveryengine.v1beta.LicenseConfigService.Update LicenseConfig google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject` (LRO) `google.cloud.discoveryengine.v1beta.SchemaService.CreateSchema` (LRO) `google.cloud.discoveryengine.v1beta.SchemaService.DeleteSchema` (LRO) `google.cloud.discoveryengine.v1beta.SchemaService.UpdateSchema` (LRO) `google.cloud.discoveryengine.v1beta.ServingConfigService.Create` 

`ServingConfig google.cloud.discoveryengine.v1beta.ServingConfigService.Delete ServingConfig google.cloud.discoveryengine.v1beta.ServingConfigService.Update ServingConfig google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Batch VerifyTargetSites` (LRO) `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Create Sitemap` 

`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Create TargetSite` (LRO) 

```
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Delete
Sitemap
```

`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Delete TargetSite` (LRO) 

`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Disable AdvancedSiteSearch` (LRO) 

`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Enable AdvancedSiteSearch` (LRO) 

`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Recrawl Uris` (LRO) 

`google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Update TargetSite google.cloud.discoveryengine.v1beta.UserLicenseService.BatchUpdate UserLicenses` (LRO) `google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUser Store` 

```
google.cloud.notebooklm.v1alpha.NotebookService.ShareNotebook
DATA_READgoogle.cloud.discoveryengine.v1.CompletionService.AdvancedComplete
Query
google.cloud.discoveryengine.v1.CompletionService.CompleteQuery
google.cloud.discoveryengine.v1.ControlService.GetControl
google.cloud.discoveryengine.v1.ControlService.ListControls
google.cloud.discoveryengine.v1.ConversationalSearchService.Answer
Query
google.cloud.discoveryengine.v1.ConversationalSearchService.Get
Answer
google.cloud.discoveryengine.v1.ConversationalSearchService.Get
Conversation
google.cloud.discoveryengine.v1.ConversationalSearchService.Get
Session
google.cloud.discoveryengine.v1.ConversationalSearchService.List
Conversations
google.cloud.discoveryengine.v1.ConversationalSearchService.List
Sessions
google.cloud.discoveryengine.v1.ConversationalSearchService.Stream
AnswerQuery
google.cloud.discoveryengine.v1.DocumentService.BatchGetDocuments
Metadata
google.cloud.discoveryengine.v1.DocumentService.GetDocument
google.cloud.discoveryengine.v1.DocumentService.ListDocuments
google.cloud.discoveryengine.v1.GroundedGenerationService.Check
Grounding
google.cloud.discoveryengine.v1.IdentityMappingStoreService.List
IdentityMappings
google.cloud.discoveryengine.v1.RankService.Rank
google.cloud.discoveryengine.v1.RecommendationService.Recommend
google.cloud.discoveryengine.v1.SearchService.Search
google.cloud.discoveryengine.v1.SearchTuningService.ListCustom
Models
google.cloud.discoveryengine.v1.SessionService.GetSession
google.cloud.discoveryengine.v1.SessionService.ListSessions
google.cloud.discoveryengine.v1.SiteSearchEngineService.Fetch
Sitemaps
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlpha
EvolveExperiment
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlpha
EvolveProgram
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlpha
EvolveExperiments
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlpha
EvolvePrograms
google.cloud.discoveryengine.v1alpha.AnalyticsService.ExportMetrics
```

(LRO) `google.cloud.discoveryengine.v1alpha.AnalyticsService.GetAnalytics Config google.cloud.discoveryengine.v1alpha.ChunkService.GetChunk google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks google.cloud.discoveryengine.v1alpha.CompletionService.Advanced CompleteQuery google.cloud.discoveryengine.v1alpha.CompletionService.Complete ExternalIdentities google.cloud.discoveryengine.v1alpha.CompletionService.Complete Query google.cloud.discoveryengine.v1alpha.ControlService.GetControl google.cloud.discoveryengine.v1alpha.ControlService.ListControls google.cloud.discoveryengine.v1alpha.ConversationalSearchService. AnswerQuery google.cloud.discoveryengine.v1alpha.ConversationalSearchService. GetAnswer google.cloud.discoveryengine.v1alpha.ConversationalSearchService. GetConversation google.cloud.discoveryengine.v1alpha.ConversationalSearchService. GetSession google.cloud.discoveryengine.v1alpha.ConversationalSearchService. ListConversations google.cloud.discoveryengine.v1alpha.ConversationalSearchService. ListSessions google.cloud.discoveryengine.v1alpha.ConversationalSearchService. StreamAnswerQuery google.cloud.discoveryengine.v1alpha.DataConnectorService.Check RefreshToken google.cloud.discoveryengine.v1alpha.DocumentService.BatchGet DocumentsMetadata google.cloud.discoveryengine.v1alpha.DocumentService.GetDocument google.cloud.discoveryengine.v1alpha.DocumentService.GetProcessed Document google.cloud.discoveryengine.v1alpha.DocumentService.ListDocuments google.cloud.discoveryengine.v1alpha.EvaluationService.Get Evaluation google.cloud.discoveryengine.v1alpha.EvaluationService.List EvaluationResults google.cloud.discoveryengine.v1alpha.EvaluationService.List Evaluations google.cloud.discoveryengine.v1alpha.GroundedGenerationService. CheckGrounding google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService. ListIdentityMappings` 

```
google.cloud.discoveryengine.v1alpha.RankService.Rank
google.cloud.discoveryengine.v1alpha.RecommendationService.
Recommend
google.cloud.discoveryengine.v1alpha.RequirementService.Check
Requirement
google.cloud.discoveryengine.v1alpha.SampleQueryService.GetSample
Query
google.cloud.discoveryengine.v1alpha.SampleQueryService.ListSample
Queries
google.cloud.discoveryengine.v1alpha.SampleQuerySetService.Get
SampleQuerySet
google.cloud.discoveryengine.v1alpha.SampleQuerySetService.List
SampleQuerySets
google.cloud.discoveryengine.v1alpha.SearchService.Search
google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustom
Models
google.cloud.discoveryengine.v1alpha.SessionService.GetSession
google.cloud.discoveryengine.v1alpha.SessionService.ListFiles
google.cloud.discoveryengine.v1alpha.SessionService.ListSessions
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Fetch
Sitemaps
google.cloud.discoveryengine.v1beta.CompletionService.Advanced
CompleteQuery
google.cloud.discoveryengine.v1beta.CompletionService.CompleteQuery
google.cloud.discoveryengine.v1beta.ControlService.GetControl
google.cloud.discoveryengine.v1beta.ControlService.ListControls
google.cloud.discoveryengine.v1beta.ConversationalSearchService.
AnswerQuery
google.cloud.discoveryengine.v1beta.ConversationalSearchService.Get
Answer
google.cloud.discoveryengine.v1beta.ConversationalSearchService.Get
Conversation
google.cloud.discoveryengine.v1beta.ConversationalSearchService.Get
Session
google.cloud.discoveryengine.v1beta.ConversationalSearchService.
ListConversations
google.cloud.discoveryengine.v1beta.ConversationalSearchService.
ListSessions
google.cloud.discoveryengine.v1beta.ConversationalSearchService.
StreamAnswerQuery
google.cloud.discoveryengine.v1beta.DocumentService.BatchGet
DocumentsMetadata
google.cloud.discoveryengine.v1beta.DocumentService.GetDocument
google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments
google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluation
google.cloud.discoveryengine.v1beta.EvaluationService.List
EvaluationResults
google.cloud.discoveryengine.v1beta.EvaluationService.List
Evaluations
google.cloud.discoveryengine.v1beta.GroundedGenerationService.Check
Grounding
google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.
ListIdentityMappings
google.cloud.discoveryengine.v1beta.RankService.Rank
google.cloud.discoveryengine.v1beta.RecommendationService.Recommend
google.cloud.discoveryengine.v1beta.SampleQueryService.GetSample
Query
google.cloud.discoveryengine.v1beta.SampleQueryService.ListSample
Queries
google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSample
QuerySet
google.cloud.discoveryengine.v1beta.SampleQuerySetService.List
SampleQuerySets
google.cloud.discoveryengine.v1beta.SearchService.Search
google.cloud.discoveryengine.v1beta.SearchTuningService.ListCustom
Models
google.cloud.discoveryengine.v1beta.SessionService.GetSession
google.cloud.discoveryengine.v1beta.SessionService.ListSessions
google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Fetch
Sitemaps
google.cloud.notebooklm.v1alpha.NotebookService.GetNotebook
google.cloud.notebooklm.v1alpha.SourceService.GetSource
```

`DATA_WRITE google.cloud.discoveryengine.v1.AssistantService.StreamAssist google.cloud.discoveryengine.v1.CompletionService.ImportCompletion Suggestions` (LRO) `google.cloud.discoveryengine.v1.CompletionService.ImportSuggestion DenyListEntries` (LRO) `google.cloud.discoveryengine.v1.CompletionService.PurgeCompletion Suggestions` (LRO) `google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestion DenyListEntries` (LRO) `google.cloud.discoveryengine.v1.ControlService.CreateControl google.cloud.discoveryengine.v1.ControlService.DeleteControl google.cloud.discoveryengine.v1.ControlService.UpdateControl google.cloud.discoveryengine.v1.ConversationalSearchService. ConverseConversation google.cloud.discoveryengine.v1.ConversationalSearchService.Create Conversation google.cloud.discoveryengine.v1.ConversationalSearchService.Create Session google.cloud.discoveryengine.v1.ConversationalSearchService.Delete Conversation google.cloud.discoveryengine.v1.ConversationalSearchService.Delete Session google.cloud.discoveryengine.v1.ConversationalSearchService.Update Conversation google.cloud.discoveryengine.v1.ConversationalSearchService.Update Session google.cloud.discoveryengine.v1.DocumentService.CreateDocument google.cloud.discoveryengine.v1.DocumentService.DeleteDocument google.cloud.discoveryengine.v1.DocumentService.ImportDocuments` (LRO) `google.cloud.discoveryengine.v1.DocumentService.PurgeDocuments` (LRO) `google.cloud.discoveryengine.v1.DocumentService.UpdateDocument google.cloud.discoveryengine.v1.IdentityMappingStoreService.Import IdentityMappings` (LRO) `google.cloud.discoveryengine.v1.IdentityMappingStoreService.Purge IdentityMappings` (LRO) `google.cloud.discoveryengine.v1.SearchTuningService.TrainCustom Model google.cloud.discoveryengine.v1.SessionService.CreateSession google.cloud.discoveryengine.v1.SessionService.DeleteSession google.cloud.discoveryengine.v1.SessionService.UpdateSession google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchCreate TargetSites` (LRO) `google.cloud.discoveryengine.v1.UserEventService.ImportUserEvents` (LRO) 

`google.cloud.discoveryengine.v1.UserEventService.PurgeUserEvents` (LRO) `google.cloud.discoveryengine.v1.UserEventService.WriteUserEvent google.cloud.discoveryengine.v1alpha.AgentService.ImportAgentFile google.cloud.discoveryengine.v1alpha.AlphaEvolveService.Acquire Programs google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlpha EvolveExperiment google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlpha EvolveProgram google.cloud.discoveryengine.v1alpha.AlphaEvolveService.Resume Experiment` (LRO) `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.Start Experiment` (LRO) `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.Submit ProgramsEvaluations google.cloud.discoveryengine.v1alpha.AnalyticsService.Update AnalyticsConfig google.cloud.discoveryengine.v1alpha.AssistantService.StreamAssist google.cloud.discoveryengine.v1alpha.CompletionService.Import CompletionSuggestions google.cloud.discoveryengine.v1alpha.CompletionService.Import SuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1alpha.CompletionService.Purge CompletionSuggestions` (LRO) `google.cloud.discoveryengine.v1alpha.CompletionService.Purge SuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1alpha.CompletionService.Remove Suggestion google.cloud.discoveryengine.v1alpha.ControlService.CreateControl google.cloud.discoveryengine.v1alpha.ControlService.DeleteControl google.cloud.discoveryengine.v1alpha.ControlService.UpdateControl google.cloud.discoveryengine.v1alpha.ConversationalSearchService. ConverseConversation google.cloud.discoveryengine.v1alpha.ConversationalSearchService. CreateConversation google.cloud.discoveryengine.v1alpha.ConversationalSearchService. CreateSession google.cloud.discoveryengine.v1alpha.ConversationalSearchService. DeleteConversation google.cloud.discoveryengine.v1alpha.ConversationalSearchService. DeleteSession google.cloud.discoveryengine.v1alpha.ConversationalSearchService. UpdateConversation google.cloud.discoveryengine.v1alpha.DataConnectorService.Acquire` 

`AccessToken google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocument google.cloud.discoveryengine.v1alpha.DocumentService.DeleteDocument google.cloud.discoveryengine.v1alpha.DocumentService.Import Documents` (LRO) `google.cloud.discoveryengine.v1alpha.DocumentService.PurgeDocuments` (LRO) `google.cloud.discoveryengine.v1alpha.DocumentService.UpdateDocument google.cloud.discoveryengine.v1alpha.EngineService.PauseEngine google.cloud.discoveryengine.v1alpha.EngineService.ResumeEngine google.cloud.discoveryengine.v1alpha.EngineService.TuneEngine` (LRO) `google.cloud.discoveryengine.v1alpha.EvaluationService.Create Evaluation` (LRO) `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService. ImportIdentityMappings` (LRO) `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService. PurgeIdentityMappings google.cloud.discoveryengine.v1alpha.SampleQueryService.Create SampleQuery google.cloud.discoveryengine.v1alpha.SampleQueryService.Delete SampleQuery google.cloud.discoveryengine.v1alpha.SampleQueryService.Import SampleQueries` (LRO) `google.cloud.discoveryengine.v1alpha.SampleQueryService.Update SampleQuery google.cloud.discoveryengine.v1alpha.SampleQuerySetService.Create SampleQuerySet google.cloud.discoveryengine.v1alpha.SampleQuerySetService.Delete SampleQuerySet google.cloud.discoveryengine.v1alpha.SampleQuerySetService.Update SampleQuerySet google.cloud.discoveryengine.v1alpha.SearchTuningService.Train CustomModel` (LRO) `google.cloud.discoveryengine.v1alpha.SessionService.CreateSession google.cloud.discoveryengine.v1alpha.SessionService.DeleteSession google.cloud.discoveryengine.v1alpha.SessionService.UpdateSession google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.Batch CreateTargetSites` (LRO) `google.cloud.discoveryengine.v1alpha.UserEventService.ImportUser Events` (LRO) `google.cloud.discoveryengine.v1alpha.UserEventService.PurgeUser Events` (LRO) `google.cloud.discoveryengine.v1alpha.UserEventService.WriteUser Event google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist` 

`google.cloud.discoveryengine.v1beta.CompletionService.Import CompletionSuggestions google.cloud.discoveryengine.v1beta.CompletionService.Import SuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1beta.CompletionService.Purge CompletionSuggestions` (LRO) `google.cloud.discoveryengine.v1beta.CompletionService.Purge SuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1beta.CompletionService.Remove Suggestion google.cloud.discoveryengine.v1beta.ControlService.CreateControl google.cloud.discoveryengine.v1beta.ControlService.DeleteControl google.cloud.discoveryengine.v1beta.ControlService.UpdateControl google.cloud.discoveryengine.v1beta.ConversationalSearchService. ConverseConversation google.cloud.discoveryengine.v1beta.ConversationalSearchService. CreateConversation google.cloud.discoveryengine.v1beta.ConversationalSearchService. CreateSession google.cloud.discoveryengine.v1beta.ConversationalSearchService. DeleteConversation google.cloud.discoveryengine.v1beta.ConversationalSearchService. DeleteSession google.cloud.discoveryengine.v1beta.ConversationalSearchService. UpdateConversation google.cloud.discoveryengine.v1beta.DocumentService.CreateDocument google.cloud.discoveryengine.v1beta.DocumentService.DeleteDocument google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments` (LRO) `google.cloud.discoveryengine.v1beta.DocumentService.PurgeDocuments` (LRO) 

`google.cloud.discoveryengine.v1beta.DocumentService.UpdateDocument google.cloud.discoveryengine.v1beta.EngineService.PauseEngine google.cloud.discoveryengine.v1beta.EngineService.ResumeEngine google.cloud.discoveryengine.v1beta.EngineService.TuneEngine google.cloud.discoveryengine.v1beta.EvaluationService.Create Evaluation` (LRO) 

```
google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.
ImportIdentityMappings
google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.
PurgeIdentityMappings
google.cloud.discoveryengine.v1beta.SampleQueryService.CreateSample
Query
google.cloud.discoveryengine.v1beta.SampleQueryService.DeleteSample
Query
```

`google.cloud.discoveryengine.v1beta.SampleQueryService.ImportSample Queries` (LRO) `google.cloud.discoveryengine.v1beta.SampleQueryService.UpdateSample Query google.cloud.discoveryengine.v1beta.SampleQuerySetService.Create SampleQuerySet google.cloud.discoveryengine.v1beta.SampleQuerySetService.Delete SampleQuerySet google.cloud.discoveryengine.v1beta.SampleQuerySetService.Update SampleQuerySet google.cloud.discoveryengine.v1beta.SearchTuningService.TrainCustom Model google.cloud.discoveryengine.v1beta.SessionService.CreateSession google.cloud.discoveryengine.v1beta.SessionService.DeleteSession google.cloud.discoveryengine.v1beta.SessionService.UpdateSession google.cloud.discoveryengine.v1beta.SiteSearchEngineService.Batch CreateTargetSites` (LRO) `google.cloud.discoveryengine.v1beta.UserEventService.ImportUser Events` (LRO) `google.cloud.discoveryengine.v1beta.UserEventService.PurgeUser Events google.cloud.discoveryengine.v1beta.UserEventService.WriteUserEvent google.cloud.notebooklm.v1alpha.AudioOverviewService.CreateAudio Overview google.cloud.notebooklm.v1alpha.AudioOverviewService.DeleteAudio Overview google.cloud.notebooklm.v1alpha.NotebookService.CreateNotebook google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources google.longrunning.Operations.CancelOperation` 

### API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Gemini Enterprise. 

`a2a.v1.A2AService` 

The following audit logs are associated with methods belonging to `a2a.v1.A2AService` . 

`GetAgentCard` 

**Method** : `a2a.v1.A2AService.GetAgentCard` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.agents.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
    protoPayload.methodName="a2a.v1.A2AService.GetAgentCard"
```

`google.cloud.discoveryengine.v1.AclConfigService` The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.AclConfigService` . 

```
GetAclConfig
```

**Method** : `google.cloud.discoveryengine.v1.AclConfigService.GetAclConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.aclConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.AclConfigServi
ce.GetAclConfig"
UpdateAclConfig
```

**Method** : 

`google.cloud.discoveryengine.v1.AclConfigService.UpdateAclConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.aclConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.AclConfigServi
ce.UpdateAclConfig"
google.cloud.discoveryengine.v1.AssistantService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.AssistantService` . 

```
CreateAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1.AssistantService.CreateAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.assistants.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantServi
ce.CreateAssistant"
DeleteAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1.AssistantService.DeleteAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.assistants.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantServi
```

`ce.DeleteAssistant"` 

```
GetAssistant
```

**Method** : `google.cloud.discoveryengine.v1.AssistantService.GetAssistant` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.assistants.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantServi
ce.GetAssistant"
ListAssistants
```

**Method** : 

`google.cloud.discoveryengine.v1.AssistantService.ListAssistants` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.assistants.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantServi
ce.ListAssistants"
StreamAssist
```

**Method** : `google.cloud.discoveryengine.v1.AssistantService.StreamAssist` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.assistants.assist - DATA_WRITE` **Method is a long-running or streaming operation** : **Streaming RPC** (/logging/docs/audit/understanding-audit-logs#streaming) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantServi
ce.StreamAssist"
UpdateAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1.AssistantService.UpdateAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.assistants.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantServi
ce.UpdateAssistant"
google.cloud.discoveryengine.v1.CmekConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.CmekConfigService` . 

```
DeleteCmekConfig
```

**Method** : 

`google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.cmekConfigs.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigServ
```

`ice.DeleteCmekConfig"` 

```
GetCmekConfig
```

**Method** : 

`google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.cmekConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigServ
ice.GetCmekConfig"
ListCmekConfigs
```

**Method** : 

`google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigs` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.cmekConfigs.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigServ
ice.ListCmekConfigs"
UpdateCmekConfig
```

**Method** : 

`google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.cmekConfigs.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigServ
ice.UpdateCmekConfig"
google.cloud.discoveryengine.v1.CollectionService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.CollectionService` . 

```
DeleteCollection
```

**Method** : 

`google.cloud.discoveryengine.v1.CollectionService.DeleteCollection` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.collections.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CollectionServ
ice.DeleteCollection"
google.cloud.discoveryengine.v1.CompletionService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.CompletionService` . 

```
AdvancedCompleteQuery
```

**Method** : 

```
google.cloud.discoveryengine.v1.CompletionService.AdvancedCompleteQuery
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.completionConfigs.completeQuery - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionServ
ice.AdvancedCompleteQuery"
```

`CompleteQuery` 

**Method** : 

`google.cloud.discoveryengine.v1.CompletionService.CompleteQuery` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.dataStores.completeQuery - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionServ
ice.CompleteQuery"
```

`ImportCompletionSuggestions` 

**Method** : 

```
google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSugge
stions
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.completionSuggestions.import - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionServ
```

`ice.ImportCompletionSuggestions"` 

```
ImportSuggestionDenyListEntries
```

**Method** : 

- `google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyL istEntries` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.suggestionDenyListEntries.import - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionServ
ice.ImportSuggestionDenyListEntries"
```

`PurgeCompletionSuggestions` 

**Method** : 

```
google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSugges
tions
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.completionSuggestions.purge - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionServ
ice.PurgeCompletionSuggestions"
PurgeSuggestionDenyListEntries
```

- **Method** : 

- `google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyLi stEntries` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionServ
ice.PurgeSuggestionDenyListEntries"
google.cloud.discoveryengine.v1.ControlService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.ControlService` . 

`CreateControl` 

- **Method** : `google.cloud.discoveryengine.v1.ControlService.CreateControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.controls.create - DATA_WRITE
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService
.CreateControl"
DeleteControl
```

- **Method** : `google.cloud.discoveryengine.v1.ControlService.DeleteControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.controls.delete - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService
.DeleteControl"
```

`GetControl` 

**Method** : `google.cloud.discoveryengine.v1.ControlService.GetControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.controls.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService
.GetControl"
```

`ListControls` 

**Method** : `google.cloud.discoveryengine.v1.ControlService.ListControls` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.controls.list - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService
.ListControls"
```

`UpdateControl` 

**Method** : `google.cloud.discoveryengine.v1.ControlService.UpdateControl` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.controls.update - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService
.UpdateControl"
google.cloud.discoveryengine.v1.ConversationalSearchService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.ConversationalSearchService` . 

```
AnswerQuery
```

**Method** : 

`google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQuery` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.servingConfigs.answer - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.AnswerQuery"
ConverseConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1.ConversationalSearchService.ConverseCon
versation
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.conversations.converse - DATA_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.ConverseConversation"
```

`CreateConversation` 

**Method** : 

```
google.cloud.discoveryengine.v1.ConversationalSearchService.CreateConve
rsation
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.conversations.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.CreateConversation"
```

`CreateSession` 

**Method** : 

```
google.cloud.discoveryengine.v1.ConversationalSearchService.CreateSessi
on
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.CreateSession"
DeleteConversation
```

**Method** : 

- `google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteConve rsation` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.conversations.delete - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.DeleteConversation"
```

`DeleteSession` 

**Method** : 

- `google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteSessi` `on` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.sessions.delete - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.DeleteSession"
```

`GetAnswer` 

**Method** : 

`google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswer` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.answers.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.GetAnswer"
GetConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1.ConversationalSearchService.GetConversa
tion
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

`discoveryengine.conversations.get - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.GetConversation"
GetSession
```

**Method** : 

`google.cloud.discoveryengine.v1.ConversationalSearchService.GetSession` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.GetSession"
```

`ListConversations` 

**Method** : 

```
google.cloud.discoveryengine.v1.ConversationalSearchService.ListConvers
ations
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.conversations.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.ListConversations"
```

`ListSessions` 

**Method** : 

```
google.cloud.discoveryengine.v1.ConversationalSearchService.ListSession
s
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.ListSessions"
```

`StreamAnswerQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1.ConversationalSearchService.StreamAnswe
rQuery
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.answer - DATA_READ` **Method is a long-running or streaming operation** : **Streaming RPC** (/logging/docs/audit/understanding-audit-logs#streaming) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
```

`SearchService.StreamAnswerQuery"` 

`UpdateConversation` 

**Method** : 

- `google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateConve rsation` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.conversations.update - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.UpdateConversation"
```

`UpdateSession` 

**Method** : 

- `google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateSessi` `on` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.sessions.update - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Conversational
SearchService.UpdateSession"
google.cloud.discoveryengine.v1.DataConnectorService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.DataConnectorService` . 

`GetDataConnector` 

**Method** : 

`google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataConnectors.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorS
ervice.GetDataConnector"
```

`SetUpDataConnector` 

**Method** : 

`google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.locations.setUpDataConnector - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorS
ervice.SetUpDataConnector"
```

`UpdateDataConnector` 

**Method** : 

```
google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnecto
r
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataConnectors.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorS
ervice.UpdateDataConnector"
google.cloud.discoveryengine.v1.DataStoreService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.DataStoreService` . 

```
CreateDataStore
```

**Method** : 

`google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.dataStores.create - ADMIN_WRITE
```

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreServi
ce.CreateDataStore"
DeleteDataStore
```

**Method** : 

`google.cloud.discoveryengine.v1.DataStoreService.DeleteDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.dataStores.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreServi
ce.DeleteDataStore"
GetDataStore
```

**Method** : `google.cloud.discoveryengine.v1.DataStoreService.GetDataStore` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataStores.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreServi
ce.GetDataStore"
ListDataStores
```

**Method** : 

`google.cloud.discoveryengine.v1.DataStoreService.ListDataStores` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.dataStores.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreServi
ce.ListDataStores"
UpdateDataStore
```

**Method** : 

`google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.dataStores.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreServi
ce.UpdateDataStore"
google.cloud.discoveryengine.v1.DocumentService
```
