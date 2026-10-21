# Gemini Enterprise Docs (Monitor usage) / Access Gemini Enterprise Cloud Audit Logs (part 1 of 5: Service name)
Source: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging, page last updated 2026-10-14, extracted 2026-10-19

This document lists the audited methods for Gemini Enterprise. Google Cloud services
generate audit logs that record administrative and access activities within your Google Cloud resources.
For more information about Cloud Audit Logs, see the following:

- [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
- [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
- [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
- [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
- [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)

## Service name

To view the Gemini Enterprise audit logs, do the following:

1. In the Google Cloud console, go to the Logs Explorer page:

   [Go to Logs Explorer](https://console.cloud.google.com/logs/query)
2. Copy and paste the following query into the **Query** field of the
   Logs Explorer, and then click **Run query**.

   ```
       protoPayload.serviceName="discoveryengine.googleapis.com"
   ```

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum
that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`,
`DATA_READ`, or `DATA_WRITE`. When you call a method,
Gemini Enterprise generates an audit log whose category is dependent on the
`type` property of the permission required to perform the method.
Methods that require an IAM permission with the `type` property value
of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate
[Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs.
Methods that require an IAM permission with the `type` property value
of `ADMIN_WRITE` generate
[Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

API methods in the following list that are marked with (LRO) are long-running operations (LROs).
These methods usually generate two audit log entries: one when the operation starts and
another when it ends. For more information see [Audit logs for long-running operations](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro).

| Permission type | Methods |
| --- | --- |
| `ADMIN_READ` | `a2a.v1.A2AService.GetAgentCard` `google.cloud.discoveryengine.v1.AclConfigService.GetAclConfig` `google.cloud.discoveryengine.v1.AssistantService.GetAssistant` `google.cloud.discoveryengine.v1.AssistantService.ListAssistants` `google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfig` `google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigs` `google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector` `google.cloud.discoveryengine.v1.DataStoreService.GetDataStore` `google.cloud.discoveryengine.v1.DataStoreService.ListDataStores` `google.cloud.discoveryengine.v1.EngineService.GetEngine` `google.cloud.discoveryengine.v1.EngineService.GetIamPolicy` `google.cloud.discoveryengine.v1.EngineService.ListEngines` `google.cloud.discoveryengine.v1.LicenseConfigService.GetLicenseConfig` `google.cloud.discoveryengine.v1.SchemaService.GetSchema` `google.cloud.discoveryengine.v1.SchemaService.ListSchemas` `google.cloud.discoveryengine.v1.ServingConfigService.GetServingConfig` `google.cloud.discoveryengine.v1.ServingConfigService.ListServingConfigs` `google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchDomainVerificationStatus` `google.cloud.discoveryengine.v1.SiteSearchEngineService.GetSiteSearchEngine` `google.cloud.discoveryengine.v1.SiteSearchEngineService.GetTargetSite` `google.cloud.discoveryengine.v1.SiteSearchEngineService.ListTargetSites` `google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig` `google.cloud.discoveryengine.v1alpha.AclConfigService.GetAclConfig` `google.cloud.discoveryengine.v1alpha.AssistantService.GetAssistant` `google.cloud.discoveryengine.v1alpha.AssistantService.ListAssistants` `google.cloud.discoveryengine.v1alpha.AuthorizationService.GetAuthorization` `google.cloud.discoveryengine.v1alpha.AuthorizationService.ListAuthorizations` `google.cloud.discoveryengine.v1alpha.BranchService.GetBranch` `google.cloud.discoveryengine.v1alpha.BranchService.ListBranches` `google.cloud.discoveryengine.v1alpha.CannedQueryService.GetCannedQuery` `google.cloud.discoveryengine.v1alpha.CannedQueryService.ListCannedQueries` `google.cloud.discoveryengine.v1alpha.CmekConfigService.GetCmekConfig` `google.cloud.discoveryengine.v1alpha.CmekConfigService.ListCmekConfigs` `google.cloud.discoveryengine.v1alpha.CollectionService.GetCollection` `google.cloud.discoveryengine.v1alpha.CollectionService.GetIamPolicy` `google.cloud.discoveryengine.v1alpha.CollectionService.ListCollections` `google.cloud.discoveryengine.v1alpha.DataConnectorService.GetConnectorSecret` `google.cloud.discoveryengine.v1alpha.DataConnectorService.GetDataConnector` `google.cloud.discoveryengine.v1alpha.DataConnectorService.ListConnectorRuns` `google.cloud.discoveryengine.v1alpha.DataStoreService.GetCompletionConfig` `google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStore` `google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocumentProcessingConfig` `google.cloud.discoveryengine.v1alpha.DataStoreService.GetIamPolicy` `google.cloud.discoveryengine.v1alpha.DataStoreService.ListDataStores` `google.cloud.discoveryengine.v1alpha.EngineService.GetEngine` `google.cloud.discoveryengine.v1alpha.EngineService.GetIamPolicy` `google.cloud.discoveryengine.v1alpha.EngineService.GetWorkspaceSettings` `google.cloud.discoveryengine.v1alpha.EngineService.ListEngines` `google.cloud.discoveryengine.v1alpha.EstimateBillingService.EstimateDataSize` (LRO) `google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetBillingAccountLicenseConfig` `google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetLicenseConfig` `google.cloud.discoveryengine.v1alpha.ProjectService.ReportConsentChange` `google.cloud.discoveryengine.v1alpha.SchemaService.GetSchema` `google.cloud.discoveryengine.v1alpha.SchemaService.ListSchemas` `google.cloud.discoveryengine.v1alpha.ServingConfigService.GetServingConfig` `google.cloud.discoveryengine.v1alpha.ServingConfigService.ListServingConfigs` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchDomainVerificationStatus` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetSiteSearchEngine` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetTargetSite` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetUriPatternDocumentData` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.ListTargetSites` `google.cloud.discoveryengine.v1alpha.UserLicenseService.ExportUserLicenses` `google.cloud.discoveryengine.v1alpha.WidgetConfigService.GetWidgetConfig` `google.cloud.discoveryengine.v1beta.AclConfigService.GetAclConfig` `google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant` `google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants` `google.cloud.discoveryengine.v1beta.CmekConfigService.GetCmekConfig` `google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmekConfigs` `google.cloud.discoveryengine.v1beta.DataStoreService.GetDataStore` `google.cloud.discoveryengine.v1beta.DataStoreService.ListDataStores` `google.cloud.discoveryengine.v1beta.EngineService.GetEngine` `google.cloud.discoveryengine.v1beta.EngineService.GetIamPolicy` `google.cloud.discoveryengine.v1beta.EngineService.ListEngines` `google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig` `google.cloud.discoveryengine.v1beta.SchemaService.GetSchema` `google.cloud.discoveryengine.v1beta.SchemaService.ListSchemas` `google.cloud.discoveryengine.v1beta.ServingConfigService.GetServingConfig` `google.cloud.discoveryengine.v1beta.ServingConfigService.ListServingConfigs` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchDomainVerificationStatus` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetSiteSearchEngine` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetTargetSite` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.ListTargetSites` `google.cloud.notebooklm.v1alpha.NotebookService.ListRecentlyViewedNotebooks` `google.longrunning.Operations.GetOperation` `google.longrunning.Operations.ListOperations` |
| `ADMIN_WRITE` | `google.cloud.discoveryengine.v1.AclConfigService.UpdateAclConfig` `google.cloud.discoveryengine.v1.AssistantService.CreateAssistant` `google.cloud.discoveryengine.v1.AssistantService.DeleteAssistant` `google.cloud.discoveryengine.v1.AssistantService.UpdateAssistant` `google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfig` (LRO) `google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfig` (LRO) `google.cloud.discoveryengine.v1.CollectionService.DeleteCollection` (LRO) `google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector` (LRO) `google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnector` `google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore` (LRO) `google.cloud.discoveryengine.v1.DataStoreService.DeleteDataStore` (LRO) `google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore` `google.cloud.discoveryengine.v1.EngineService.CreateEngine` (LRO) `google.cloud.discoveryengine.v1.EngineService.DeleteEngine` (LRO) `google.cloud.discoveryengine.v1.EngineService.SetIamPolicy` `google.cloud.discoveryengine.v1.EngineService.UpdateEngine` `google.cloud.discoveryengine.v1.IdentityMappingStoreService.CreateIdentityMappingStore` `google.cloud.discoveryengine.v1.IdentityMappingStoreService.DeleteIdentityMappingStore` (LRO) `google.cloud.discoveryengine.v1.LicenseConfigService.CreateLicenseConfig` `google.cloud.discoveryengine.v1.LicenseConfigService.DistributeLicenseConfig` `google.cloud.discoveryengine.v1.LicenseConfigService.RetractLicenseConfig` `google.cloud.discoveryengine.v1.LicenseConfigService.UpdateLicenseConfig` `google.cloud.discoveryengine.v1.ProjectService.ProvisionProject` (LRO) `google.cloud.discoveryengine.v1.SchemaService.CreateSchema` (LRO) `google.cloud.discoveryengine.v1.SchemaService.DeleteSchema` (LRO) `google.cloud.discoveryengine.v1.SchemaService.UpdateSchema` (LRO) `google.cloud.discoveryengine.v1.ServingConfigService.CreateServingConfig` `google.cloud.discoveryengine.v1.ServingConfigService.DeleteServingConfig` `google.cloud.discoveryengine.v1.ServingConfigService.UpdateServingConfig` `google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchVerifyTargetSites` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateSitemap` `google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateTargetSite` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteSitemap` `google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteTargetSite` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.DisableAdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.EnableAdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.RecrawlUris` (LRO) `google.cloud.discoveryengine.v1.SiteSearchEngineService.UpdateTargetSite` (LRO) `google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUserLicenses` (LRO) `google.cloud.discoveryengine.v1.UserStoreService.UpdateUserStore` `google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidgetConfig` `google.cloud.discoveryengine.v1alpha.AclConfigService.UpdateAclConfig` `google.cloud.discoveryengine.v1alpha.AgentService.CreateAgent` `google.cloud.discoveryengine.v1alpha.AgentService.DeleteAgent` (LRO) `google.cloud.discoveryengine.v1alpha.AgentService.UpdateAgent` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.DeleteAlphaEvolveExperimentAndPrograms` `google.cloud.discoveryengine.v1alpha.AssistantService.CreateAssistant` `google.cloud.discoveryengine.v1alpha.AssistantService.DeleteAssistant` `google.cloud.discoveryengine.v1alpha.AssistantService.UpdateAssistant` `google.cloud.discoveryengine.v1alpha.AuthorizationService.CreateAuthorization` `google.cloud.discoveryengine.v1alpha.AuthorizationService.DeleteAuthorization` `google.cloud.discoveryengine.v1alpha.AuthorizationService.UpdateAuthorization` `google.cloud.discoveryengine.v1alpha.CannedQueryService.CreateCannedQuery` `google.cloud.discoveryengine.v1alpha.CannedQueryService.DeleteCannedQuery` `google.cloud.discoveryengine.v1alpha.CannedQueryService.UpdateCannedQuery` `google.cloud.discoveryengine.v1alpha.CmekConfigService.DeleteCmekConfig` (LRO) `google.cloud.discoveryengine.v1alpha.CmekConfigService.UpdateCmekConfig` (LRO) `google.cloud.discoveryengine.v1alpha.CollectionService.DeleteCollection` (LRO) `google.cloud.discoveryengine.v1alpha.CollectionService.SetIamPolicy` `google.cloud.discoveryengine.v1alpha.CollectionService.UpdateCollection` (LRO) `google.cloud.discoveryengine.v1alpha.DataConnectorService.SetUpDataConnector` (LRO) `google.cloud.discoveryengine.v1alpha.DataConnectorService.UpdateDataConnector` `google.cloud.discoveryengine.v1alpha.DataStoreService.AddPatientFilter` (LRO) `google.cloud.discoveryengine.v1alpha.DataStoreService.CreateDataStore` (LRO) `google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteDataStore` (LRO) `google.cloud.discoveryengine.v1alpha.DataStoreService.DeletePatientFilters` `google.cloud.discoveryengine.v1alpha.DataStoreService.RemovePatientFilter` `google.cloud.discoveryengine.v1alpha.DataStoreService.ReplacePatientFilter` (LRO) `google.cloud.discoveryengine.v1alpha.DataStoreService.SetIamPolicy` `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateCompletionConfig` `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDataStore` `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDocumentProcessingConfig` `google.cloud.discoveryengine.v1alpha.EngineService.CreateEngine` (LRO) `google.cloud.discoveryengine.v1alpha.EngineService.DeleteEngine` (LRO) `google.cloud.discoveryengine.v1alpha.EngineService.SetIamPolicy` `google.cloud.discoveryengine.v1alpha.EngineService.UpdateEngine` `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.CreateIdentityMappingStore` `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.DeleteIdentityMappingStore` (LRO) `google.cloud.discoveryengine.v1alpha.LicenseConfigService.CreateLicenseConfig` `google.cloud.discoveryengine.v1alpha.LicenseConfigService.DistributeLicenseConfig` `google.cloud.discoveryengine.v1alpha.LicenseConfigService.RetractLicenseConfig` `google.cloud.discoveryengine.v1alpha.LicenseConfigService.UpdateLicenseConfig` `google.cloud.discoveryengine.v1alpha.ProjectService.ProvisionProject` (LRO) `google.cloud.discoveryengine.v1alpha.ProjectService.UpdateProject` `google.cloud.discoveryengine.v1alpha.SchemaService.CreateSchema` (LRO) `google.cloud.discoveryengine.v1alpha.SchemaService.DeleteSchema` (LRO) `google.cloud.discoveryengine.v1alpha.SchemaService.UpdateSchema` (LRO) `google.cloud.discoveryengine.v1alpha.ServingConfigService.CreateServingConfig` `google.cloud.discoveryengine.v1alpha.ServingConfigService.DeleteServingConfig` `google.cloud.discoveryengine.v1alpha.ServingConfigService.UpdateServingConfig` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchVerifyTargetSites` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateSitemap` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateTargetSite` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteSitemap` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteTargetSite` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DisableAdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.EnableAdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.RecrawlUris` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.SetUriPatternDocumentData` (LRO) `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.UpdateTargetSite` (LRO) `google.cloud.discoveryengine.v1alpha.UserLicenseService.BatchUpdateUserLicenses` (LRO) `google.cloud.discoveryengine.v1alpha.UserStoreService.UpdateUserStore` `google.cloud.discoveryengine.v1alpha.WidgetConfigService.UpdateWidgetConfig` `google.cloud.discoveryengine.v1beta.AclConfigService.UpdateAclConfig` `google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant` `google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant` `google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant` `google.cloud.discoveryengine.v1beta.CmekConfigService.DeleteCmekConfig` (LRO) `google.cloud.discoveryengine.v1beta.CmekConfigService.UpdateCmekConfig` (LRO) `google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore` (LRO) `google.cloud.discoveryengine.v1beta.DataStoreService.DeleteDataStore` (LRO) `google.cloud.discoveryengine.v1beta.DataStoreService.UpdateDataStore` `google.cloud.discoveryengine.v1beta.EngineService.CreateEngine` (LRO) `google.cloud.discoveryengine.v1beta.EngineService.DeleteEngine` (LRO) `google.cloud.discoveryengine.v1beta.EngineService.SetIamPolicy` `google.cloud.discoveryengine.v1beta.EngineService.UpdateEngine` `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.CreateIdentityMappingStore` `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.DeleteIdentityMappingStore` (LRO) `google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig` `google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig` `google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig` `google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig` `google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject` (LRO) `google.cloud.discoveryengine.v1beta.SchemaService.CreateSchema` (LRO) `google.cloud.discoveryengine.v1beta.SchemaService.DeleteSchema` (LRO) `google.cloud.discoveryengine.v1beta.SchemaService.UpdateSchema` (LRO) `google.cloud.discoveryengine.v1beta.ServingConfigService.CreateServingConfig` `google.cloud.discoveryengine.v1beta.ServingConfigService.DeleteServingConfig` `google.cloud.discoveryengine.v1beta.ServingConfigService.UpdateServingConfig` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchVerifyTargetSites` (LRO) `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateSitemap` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateTargetSite` (LRO) `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteSitemap` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteTargetSite` (LRO) `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DisableAdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.EnableAdvancedSiteSearch` (LRO) `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.RecrawlUris` (LRO) `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.UpdateTargetSite` `google.cloud.discoveryengine.v1beta.UserLicenseService.BatchUpdateUserLicenses` (LRO) `google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUserStore` `google.cloud.notebooklm.v1alpha.NotebookService.ShareNotebook` |
| `DATA_READ` | `google.cloud.discoveryengine.v1.CompletionService.AdvancedCompleteQuery` `google.cloud.discoveryengine.v1.CompletionService.CompleteQuery` `google.cloud.discoveryengine.v1.ControlService.GetControl` `google.cloud.discoveryengine.v1.ControlService.ListControls` `google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQuery` `google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswer` `google.cloud.discoveryengine.v1.ConversationalSearchService.GetConversation` `google.cloud.discoveryengine.v1.ConversationalSearchService.GetSession` `google.cloud.discoveryengine.v1.ConversationalSearchService.ListConversations` `google.cloud.discoveryengine.v1.ConversationalSearchService.ListSessions` `google.cloud.discoveryengine.v1.ConversationalSearchService.StreamAnswerQuery` `google.cloud.discoveryengine.v1.DocumentService.BatchGetDocumentsMetadata` `google.cloud.discoveryengine.v1.DocumentService.GetDocument` `google.cloud.discoveryengine.v1.DocumentService.ListDocuments` `google.cloud.discoveryengine.v1.GroundedGenerationService.CheckGrounding` `google.cloud.discoveryengine.v1.IdentityMappingStoreService.ListIdentityMappings` `google.cloud.discoveryengine.v1.RankService.Rank` `google.cloud.discoveryengine.v1.RecommendationService.Recommend` `google.cloud.discoveryengine.v1.SearchService.Search` `google.cloud.discoveryengine.v1.SearchTuningService.ListCustomModels` `google.cloud.discoveryengine.v1.SessionService.GetSession` `google.cloud.discoveryengine.v1.SessionService.ListSessions` `google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchSitemaps` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveExperiment` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveProgram` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolveExperiments` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolvePrograms` `google.cloud.discoveryengine.v1alpha.AnalyticsService.ExportMetrics` (LRO) `google.cloud.discoveryengine.v1alpha.AnalyticsService.GetAnalyticsConfig` `google.cloud.discoveryengine.v1alpha.ChunkService.GetChunk` `google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks` `google.cloud.discoveryengine.v1alpha.CompletionService.AdvancedCompleteQuery` `google.cloud.discoveryengine.v1alpha.CompletionService.CompleteExternalIdentities` `google.cloud.discoveryengine.v1alpha.CompletionService.CompleteQuery` `google.cloud.discoveryengine.v1alpha.ControlService.GetControl` `google.cloud.discoveryengine.v1alpha.ControlService.ListControls` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.AnswerQuery` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetAnswer` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetConversation` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetSession` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListConversations` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListSessions` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.StreamAnswerQuery` `google.cloud.discoveryengine.v1alpha.DataConnectorService.CheckRefreshToken` `google.cloud.discoveryengine.v1alpha.DocumentService.BatchGetDocumentsMetadata` `google.cloud.discoveryengine.v1alpha.DocumentService.GetDocument` `google.cloud.discoveryengine.v1alpha.DocumentService.GetProcessedDocument` `google.cloud.discoveryengine.v1alpha.DocumentService.ListDocuments` `google.cloud.discoveryengine.v1alpha.EvaluationService.GetEvaluation` `google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationResults` `google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations` `google.cloud.discoveryengine.v1alpha.GroundedGenerationService.CheckGrounding` `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ListIdentityMappings` `google.cloud.discoveryengine.v1alpha.RankService.Rank` `google.cloud.discoveryengine.v1alpha.RecommendationService.Recommend` `google.cloud.discoveryengine.v1alpha.RequirementService.CheckRequirement` `google.cloud.discoveryengine.v1alpha.SampleQueryService.GetSampleQuery` `google.cloud.discoveryengine.v1alpha.SampleQueryService.ListSampleQueries` `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.GetSampleQuerySet` `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.ListSampleQuerySets` `google.cloud.discoveryengine.v1alpha.SearchService.Search` `google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustomModels` `google.cloud.discoveryengine.v1alpha.SessionService.GetSession` `google.cloud.discoveryengine.v1alpha.SessionService.ListFiles` `google.cloud.discoveryengine.v1alpha.SessionService.ListSessions` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchSitemaps` `google.cloud.discoveryengine.v1beta.CompletionService.AdvancedCompleteQuery` `google.cloud.discoveryengine.v1beta.CompletionService.CompleteQuery` `google.cloud.discoveryengine.v1beta.ControlService.GetControl` `google.cloud.discoveryengine.v1beta.ControlService.ListControls` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.AnswerQuery` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetAnswer` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetConversation` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetSession` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListConversations` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListSessions` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.StreamAnswerQuery` `google.cloud.discoveryengine.v1beta.DocumentService.BatchGetDocumentsMetadata` `google.cloud.discoveryengine.v1beta.DocumentService.GetDocument` `google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments` `google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluation` `google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationResults` `google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluations` `google.cloud.discoveryengine.v1beta.GroundedGenerationService.CheckGrounding` `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ListIdentityMappings` `google.cloud.discoveryengine.v1beta.RankService.Rank` `google.cloud.discoveryengine.v1beta.RecommendationService.Recommend` `google.cloud.discoveryengine.v1beta.SampleQueryService.GetSampleQuery` `google.cloud.discoveryengine.v1beta.SampleQueryService.ListSampleQueries` `google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSampleQuerySet` `google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQuerySets` `google.cloud.discoveryengine.v1beta.SearchService.Search` `google.cloud.discoveryengine.v1beta.SearchTuningService.ListCustomModels` `google.cloud.discoveryengine.v1beta.SessionService.GetSession` `google.cloud.discoveryengine.v1beta.SessionService.ListSessions` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchSitemaps` `google.cloud.notebooklm.v1alpha.NotebookService.GetNotebook` `google.cloud.notebooklm.v1alpha.SourceService.GetSource` |
| `DATA_WRITE` | `google.cloud.discoveryengine.v1.AssistantService.StreamAssist` `google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSuggestions` (LRO) `google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSuggestions` (LRO) `google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1.ControlService.CreateControl` `google.cloud.discoveryengine.v1.ControlService.DeleteControl` `google.cloud.discoveryengine.v1.ControlService.UpdateControl` `google.cloud.discoveryengine.v1.ConversationalSearchService.ConverseConversation` `google.cloud.discoveryengine.v1.ConversationalSearchService.CreateConversation` `google.cloud.discoveryengine.v1.ConversationalSearchService.CreateSession` `google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteConversation` `google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteSession` `google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateConversation` `google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateSession` `google.cloud.discoveryengine.v1.DocumentService.CreateDocument` `google.cloud.discoveryengine.v1.DocumentService.DeleteDocument` `google.cloud.discoveryengine.v1.DocumentService.ImportDocuments` (LRO) `google.cloud.discoveryengine.v1.DocumentService.PurgeDocuments` (LRO) `google.cloud.discoveryengine.v1.DocumentService.UpdateDocument` `google.cloud.discoveryengine.v1.IdentityMappingStoreService.ImportIdentityMappings` (LRO) `google.cloud.discoveryengine.v1.IdentityMappingStoreService.PurgeIdentityMappings` (LRO) `google.cloud.discoveryengine.v1.SearchTuningService.TrainCustomModel` `google.cloud.discoveryengine.v1.SessionService.CreateSession` `google.cloud.discoveryengine.v1.SessionService.DeleteSession` `google.cloud.discoveryengine.v1.SessionService.UpdateSession` `google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchCreateTargetSites` (LRO) `google.cloud.discoveryengine.v1.UserEventService.ImportUserEvents` (LRO) `google.cloud.discoveryengine.v1.UserEventService.PurgeUserEvents` (LRO) `google.cloud.discoveryengine.v1.UserEventService.WriteUserEvent` `google.cloud.discoveryengine.v1alpha.AgentService.ImportAgentFile` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.AcquirePrograms` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveExperiment` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveProgram` `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ResumeExperiment` (LRO) `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.StartExperiment` (LRO) `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.SubmitProgramsEvaluations` `google.cloud.discoveryengine.v1alpha.AnalyticsService.UpdateAnalyticsConfig` `google.cloud.discoveryengine.v1alpha.AssistantService.StreamAssist` `google.cloud.discoveryengine.v1alpha.CompletionService.ImportCompletionSuggestions` `google.cloud.discoveryengine.v1alpha.CompletionService.ImportSuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1alpha.CompletionService.PurgeCompletionSuggestions` (LRO) `google.cloud.discoveryengine.v1alpha.CompletionService.PurgeSuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1alpha.CompletionService.RemoveSuggestion` `google.cloud.discoveryengine.v1alpha.ControlService.CreateControl` `google.cloud.discoveryengine.v1alpha.ControlService.DeleteControl` `google.cloud.discoveryengine.v1alpha.ControlService.UpdateControl` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ConverseConversation` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateConversation` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateSession` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteConversation` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteSession` `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.UpdateConversation` `google.cloud.discoveryengine.v1alpha.DataConnectorService.AcquireAccessToken` `google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocument` `google.cloud.discoveryengine.v1alpha.DocumentService.DeleteDocument` `google.cloud.discoveryengine.v1alpha.DocumentService.ImportDocuments` (LRO) `google.cloud.discoveryengine.v1alpha.DocumentService.PurgeDocuments` (LRO) `google.cloud.discoveryengine.v1alpha.DocumentService.UpdateDocument` `google.cloud.discoveryengine.v1alpha.EngineService.PauseEngine` `google.cloud.discoveryengine.v1alpha.EngineService.ResumeEngine` `google.cloud.discoveryengine.v1alpha.EngineService.TuneEngine` (LRO) `google.cloud.discoveryengine.v1alpha.EvaluationService.CreateEvaluation` (LRO) `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ImportIdentityMappings` (LRO) `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.PurgeIdentityMappings` `google.cloud.discoveryengine.v1alpha.SampleQueryService.CreateSampleQuery` `google.cloud.discoveryengine.v1alpha.SampleQueryService.DeleteSampleQuery` `google.cloud.discoveryengine.v1alpha.SampleQueryService.ImportSampleQueries` (LRO) `google.cloud.discoveryengine.v1alpha.SampleQueryService.UpdateSampleQuery` `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.CreateSampleQuerySet` `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.DeleteSampleQuerySet` `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.UpdateSampleQuerySet` `google.cloud.discoveryengine.v1alpha.SearchTuningService.TrainCustomModel` (LRO) `google.cloud.discoveryengine.v1alpha.SessionService.CreateSession` `google.cloud.discoveryengine.v1alpha.SessionService.DeleteSession` `google.cloud.discoveryengine.v1alpha.SessionService.UpdateSession` `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchCreateTargetSites` (LRO) `google.cloud.discoveryengine.v1alpha.UserEventService.ImportUserEvents` (LRO) `google.cloud.discoveryengine.v1alpha.UserEventService.PurgeUserEvents` (LRO) `google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEvent` `google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist` `google.cloud.discoveryengine.v1beta.CompletionService.ImportCompletionSuggestions` `google.cloud.discoveryengine.v1beta.CompletionService.ImportSuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1beta.CompletionService.PurgeCompletionSuggestions` (LRO) `google.cloud.discoveryengine.v1beta.CompletionService.PurgeSuggestionDenyListEntries` (LRO) `google.cloud.discoveryengine.v1beta.CompletionService.RemoveSuggestion` `google.cloud.discoveryengine.v1beta.ControlService.CreateControl` `google.cloud.discoveryengine.v1beta.ControlService.DeleteControl` `google.cloud.discoveryengine.v1beta.ControlService.UpdateControl` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ConverseConversation` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateConversation` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateSession` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteConversation` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteSession` `google.cloud.discoveryengine.v1beta.ConversationalSearchService.UpdateConversation` `google.cloud.discoveryengine.v1beta.DocumentService.CreateDocument` `google.cloud.discoveryengine.v1beta.DocumentService.DeleteDocument` `google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments` (LRO) `google.cloud.discoveryengine.v1beta.DocumentService.PurgeDocuments` (LRO) `google.cloud.discoveryengine.v1beta.DocumentService.UpdateDocument` `google.cloud.discoveryengine.v1beta.EngineService.PauseEngine` `google.cloud.discoveryengine.v1beta.EngineService.ResumeEngine` `google.cloud.discoveryengine.v1beta.EngineService.TuneEngine` `google.cloud.discoveryengine.v1beta.EvaluationService.CreateEvaluation` (LRO) `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ImportIdentityMappings` `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.PurgeIdentityMappings` `google.cloud.discoveryengine.v1beta.SampleQueryService.CreateSampleQuery` `google.cloud.discoveryengine.v1beta.SampleQueryService.DeleteSampleQuery` `google.cloud.discoveryengine.v1beta.SampleQueryService.ImportSampleQueries` (LRO) `google.cloud.discoveryengine.v1beta.SampleQueryService.UpdateSampleQuery` `google.cloud.discoveryengine.v1beta.SampleQuerySetService.CreateSampleQuerySet` `google.cloud.discoveryengine.v1beta.SampleQuerySetService.DeleteSampleQuerySet` `google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQuerySet` `google.cloud.discoveryengine.v1beta.SearchTuningService.TrainCustomModel` `google.cloud.discoveryengine.v1beta.SessionService.CreateSession` `google.cloud.discoveryengine.v1beta.SessionService.DeleteSession` `google.cloud.discoveryengine.v1beta.SessionService.UpdateSession` `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchCreateTargetSites` (LRO) `google.cloud.discoveryengine.v1beta.UserEventService.ImportUserEvents` (LRO) `google.cloud.discoveryengine.v1beta.UserEventService.PurgeUserEvents` `google.cloud.discoveryengine.v1beta.UserEventService.WriteUserEvent` `google.cloud.notebooklm.v1alpha.AudioOverviewService.CreateAudioOverview` `google.cloud.notebooklm.v1alpha.AudioOverviewService.DeleteAudioOverview` `google.cloud.notebooklm.v1alpha.NotebookService.CreateNotebook` `google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources` `google.longrunning.Operations.CancelOperation` |

## API interface audit logs

For information about how and which permissions are evaluated for each method,
see the Identity and Access Management documentation for Gemini Enterprise.

### `a2a.v1.A2AService`

The following audit logs are associated with methods belonging to
`a2a.v1.A2AService`.

#### `GetAgentCard`

- **Method**: `a2a.v1.A2AService.GetAgentCard`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.agents.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="a2a.v1.A2AService.GetAgentCard"`

### `google.cloud.discoveryengine.v1.AclConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.AclConfigService`.

#### `GetAclConfig`

- **Method**: `google.cloud.discoveryengine.v1.AclConfigService.GetAclConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.aclConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.AclConfigService.GetAclConfig"`

#### `UpdateAclConfig`

- **Method**: `google.cloud.discoveryengine.v1.AclConfigService.UpdateAclConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.aclConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.AclConfigService.UpdateAclConfig"`

### `google.cloud.discoveryengine.v1.AssistantService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.AssistantService`.

#### `CreateAssistant`

- **Method**: `google.cloud.discoveryengine.v1.AssistantService.CreateAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.CreateAssistant"`

#### `DeleteAssistant`

- **Method**: `google.cloud.discoveryengine.v1.AssistantService.DeleteAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.DeleteAssistant"`

#### `GetAssistant`

- **Method**: `google.cloud.discoveryengine.v1.AssistantService.GetAssistant`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.GetAssistant"`

#### `ListAssistants`

- **Method**: `google.cloud.discoveryengine.v1.AssistantService.ListAssistants`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.ListAssistants"`

#### `StreamAssist`

- **Method**: `google.cloud.discoveryengine.v1.AssistantService.StreamAssist`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.assist - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.StreamAssist"`

#### `UpdateAssistant`

- **Method**: `google.cloud.discoveryengine.v1.AssistantService.UpdateAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.AssistantService.UpdateAssistant"`

### `google.cloud.discoveryengine.v1.CmekConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.CmekConfigService`.

#### `DeleteCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cmekConfigs.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigService.DeleteCmekConfig"`

#### `GetCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.cmekConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigService.GetCmekConfig"`

#### `ListCmekConfigs`

- **Method**: `google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigs`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.cmekConfigs.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigService.ListCmekConfigs"`

#### `UpdateCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cmekConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CmekConfigService.UpdateCmekConfig"`

### `google.cloud.discoveryengine.v1.CollectionService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.CollectionService`.

#### `DeleteCollection`

- **Method**: `google.cloud.discoveryengine.v1.CollectionService.DeleteCollection`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.collections.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CollectionService.DeleteCollection"`

### `google.cloud.discoveryengine.v1.CompletionService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.CompletionService`.

#### `AdvancedCompleteQuery`

- **Method**: `google.cloud.discoveryengine.v1.CompletionService.AdvancedCompleteQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionConfigs.completeQuery - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.AdvancedCompleteQuery"`

#### `CompleteQuery`

- **Method**: `google.cloud.discoveryengine.v1.CompletionService.CompleteQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.completeQuery - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.CompleteQuery"`

#### `ImportCompletionSuggestions`

- **Method**: `google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSuggestions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionSuggestions.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.ImportCompletionSuggestions"`

#### `ImportSuggestionDenyListEntries`

- **Method**: `google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyListEntries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.suggestionDenyListEntries.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.ImportSuggestionDenyListEntries"`

#### `PurgeCompletionSuggestions`

- **Method**: `google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSuggestions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionSuggestions.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.PurgeCompletionSuggestions"`

#### `PurgeSuggestionDenyListEntries`

- **Method**: `google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyListEntries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.CompletionService.PurgeSuggestionDenyListEntries"`

### `google.cloud.discoveryengine.v1.ControlService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.ControlService`.

#### `CreateControl`

- **Method**: `google.cloud.discoveryengine.v1.ControlService.CreateControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.CreateControl"`

#### `DeleteControl`

- **Method**: `google.cloud.discoveryengine.v1.ControlService.DeleteControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.DeleteControl"`

#### `GetControl`

- **Method**: `google.cloud.discoveryengine.v1.ControlService.GetControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.GetControl"`

#### `ListControls`

- **Method**: `google.cloud.discoveryengine.v1.ControlService.ListControls`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.ListControls"`

#### `UpdateControl`

- **Method**: `google.cloud.discoveryengine.v1.ControlService.UpdateControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ControlService.UpdateControl"`

### `google.cloud.discoveryengine.v1.ConversationalSearchService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.ConversationalSearchService`.

#### `AnswerQuery`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.answer - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.AnswerQuery"`

#### `ConverseConversation`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.ConverseConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.converse - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.ConverseConversation"`

#### `CreateConversation`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.CreateConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.CreateConversation"`

#### `CreateSession`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.CreateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.CreateSession"`

#### `DeleteConversation`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteConversation"`

#### `DeleteSession`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.DeleteSession"`

#### `GetAnswer`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswer`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.answers.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.GetAnswer"`

#### `GetConversation`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.GetConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.GetConversation"`

#### `GetSession`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.GetSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.GetSession"`

#### `ListConversations`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.ListConversations`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.ListConversations"`

#### `ListSessions`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.ListSessions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.ListSessions"`

#### `StreamAnswerQuery`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.StreamAnswerQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.answer - DATA_READ`
- **Method is a long-running or streaming operation**:
  [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.StreamAnswerQuery"`

#### `UpdateConversation`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateConversation"`

#### `UpdateSession`

- **Method**: `google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ConversationalSearchService.UpdateSession"`

### `google.cloud.discoveryengine.v1.DataConnectorService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.DataConnectorService`.

#### `GetDataConnector`

- **Method**: `google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataConnectors.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorService.GetDataConnector"`

#### `SetUpDataConnector`

- **Method**: `google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.locations.setUpDataConnector - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorService.SetUpDataConnector"`

#### `UpdateDataConnector`

- **Method**: `google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnector`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataConnectors.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DataConnectorService.UpdateDataConnector"`
