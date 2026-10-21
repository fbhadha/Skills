# Gemini Enterprise Docs (Monitor usage) / Access Gemini Enterprise Cloud Audit Logs (part 4 of 5: API interface audit logs: google.cloud.discoveryengine.v1alpha.SampleQueryService to google.cloud.discoveryengine.v1beta.DocumentService)
Source: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging, page last updated 2026-10-14, extracted 2026-10-19

## API interface audit logs

### `google.cloud.discoveryengine.v1alpha.SampleQueryService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.SampleQueryService`.

#### `CreateSampleQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQueryService.CreateSampleQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.CreateSampleQuery"`

#### `DeleteSampleQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQueryService.DeleteSampleQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.DeleteSampleQuery"`

#### `GetSampleQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQueryService.GetSampleQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.GetSampleQuery"`

#### `ImportSampleQueries`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQueryService.ImportSampleQueries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.ImportSampleQueries"`

#### `ListSampleQueries`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQueryService.ListSampleQueries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.ListSampleQueries"`

#### `UpdateSampleQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQueryService.UpdateSampleQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQueryService.UpdateSampleQuery"`

### `google.cloud.discoveryengine.v1alpha.SampleQuerySetService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.SampleQuerySetService`.

#### `CreateSampleQuerySet`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.CreateSampleQuerySet`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.CreateSampleQuerySet"`

#### `DeleteSampleQuerySet`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.DeleteSampleQuerySet`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.DeleteSampleQuerySet"`

#### `GetSampleQuerySet`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.GetSampleQuerySet`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.GetSampleQuerySet"`

#### `ListSampleQuerySets`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.ListSampleQuerySets`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.ListSampleQuerySets"`

#### `UpdateSampleQuerySet`

- **Method**: `google.cloud.discoveryengine.v1alpha.SampleQuerySetService.UpdateSampleQuerySet`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQuerySetService.UpdateSampleQuerySet"`

### `google.cloud.discoveryengine.v1alpha.SchemaService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.SchemaService`.

#### `CreateSchema`

- **Method**: `google.cloud.discoveryengine.v1alpha.SchemaService.CreateSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.CreateSchema"`

#### `DeleteSchema`

- **Method**: `google.cloud.discoveryengine.v1alpha.SchemaService.DeleteSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.DeleteSchema"`

#### `GetSchema`

- **Method**: `google.cloud.discoveryengine.v1alpha.SchemaService.GetSchema`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.schemas.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.GetSchema"`

#### `ListSchemas`

- **Method**: `google.cloud.discoveryengine.v1alpha.SchemaService.ListSchemas`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.schemas.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.ListSchemas"`

#### `UpdateSchema`

- **Method**: `google.cloud.discoveryengine.v1alpha.SchemaService.UpdateSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaService.UpdateSchema"`

### `google.cloud.discoveryengine.v1alpha.SearchService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.SearchService`.

#### `Search`

- **Method**: `google.cloud.discoveryengine.v1alpha.SearchService.Search`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.search - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchService.Search"`

### `google.cloud.discoveryengine.v1alpha.SearchTuningService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.SearchTuningService`.

#### `ListCustomModels`

- **Method**: `google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustomModels`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.listCustomModels - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustomModels"`

#### `TrainCustomModel`

- **Method**: `google.cloud.discoveryengine.v1alpha.SearchTuningService.TrainCustomModel`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.trainCustomModel - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchTuningService.TrainCustomModel"`

### `google.cloud.discoveryengine.v1alpha.ServingConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.ServingConfigService`.

#### `CreateServingConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.ServingConfigService.CreateServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.CreateServingConfig"`

#### `DeleteServingConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.ServingConfigService.DeleteServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.DeleteServingConfig"`

#### `GetServingConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.ServingConfigService.GetServingConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.GetServingConfig"`

#### `ListServingConfigs`

- **Method**: `google.cloud.discoveryengine.v1alpha.ServingConfigService.ListServingConfigs`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.ListServingConfigs"`

#### `UpdateServingConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.ServingConfigService.UpdateServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingConfigService.UpdateServingConfig"`

### `google.cloud.discoveryengine.v1alpha.SessionService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.SessionService`.

#### `CreateSession`

- **Method**: `google.cloud.discoveryengine.v1alpha.SessionService.CreateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.CreateSession"`

#### `DeleteSession`

- **Method**: `google.cloud.discoveryengine.v1alpha.SessionService.DeleteSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.DeleteSession"`

#### `GetSession`

- **Method**: `google.cloud.discoveryengine.v1alpha.SessionService.GetSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.GetSession"`

#### `ListFiles`

- **Method**: `google.cloud.discoveryengine.v1alpha.SessionService.ListFiles`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.listSessionFileMetadata - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.ListFiles"`

#### `ListSessions`

- **Method**: `google.cloud.discoveryengine.v1alpha.SessionService.ListSessions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.ListSessions"`

#### `UpdateSession`

- **Method**: `google.cloud.discoveryengine.v1alpha.SessionService.UpdateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionService.UpdateSession"`

### `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.SiteSearchEngineService`.

#### `BatchCreateTargetSites`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchCreateTargetSites`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.batchCreate - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchCreateTargetSites"`

#### `BatchVerifyTargetSites`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchVerifyTargetSites`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.batchVerifyTargetSites - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchVerifyTargetSites"`

#### `CreateSitemap`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateSitemap`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.sitemaps.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateSitemap"`

#### `CreateTargetSite`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateTargetSite"`

#### `DeleteSitemap`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteSitemap`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.sitemaps.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteSitemap"`

#### `DeleteTargetSite`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteTargetSite"`

#### `DisableAdvancedSiteSearch`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DisableAdvancedSiteSearch`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.disableAdvancedSiteSearch - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DisableAdvancedSiteSearch"`

#### `EnableAdvancedSiteSearch`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.EnableAdvancedSiteSearch`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.enableAdvancedSiteSearch - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.EnableAdvancedSiteSearch"`

#### `FetchDomainVerificationStatus`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchDomainVerificationStatus`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchDomainVerificationStatus"`

#### `FetchSitemaps`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchSitemaps`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sitemaps.fetch - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchSitemaps"`

#### `GetSiteSearchEngine`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetSiteSearchEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetSiteSearchEngine"`

#### `GetTargetSite`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetTargetSite`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetTargetSite"`

#### `GetUriPatternDocumentData`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetUriPatternDocumentData`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.getUriPatternDocumentData - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetUriPatternDocumentData"`

#### `ListTargetSites`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.ListTargetSites`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.ListTargetSites"`

#### `RecrawlUris`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.RecrawlUris`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.RecrawlUris"`

#### `SetUriPatternDocumentData`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.SetUriPatternDocumentData`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.setUriPatternDocumentData - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.SetUriPatternDocumentData"`

#### `UpdateTargetSite`

- **Method**: `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.UpdateTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.UpdateTargetSite"`

### `google.cloud.discoveryengine.v1alpha.UserEventService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.UserEventService`.

#### `ImportUserEvents`

- **Method**: `google.cloud.discoveryengine.v1alpha.UserEventService.ImportUserEvents`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEventService.ImportUserEvents"`

#### `PurgeUserEvents`

- **Method**: `google.cloud.discoveryengine.v1alpha.UserEventService.PurgeUserEvents`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEventService.PurgeUserEvents"`

#### `WriteUserEvent`

- **Method**: `google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEvent`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEvent"`

### `google.cloud.discoveryengine.v1alpha.UserLicenseService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.UserLicenseService`.

#### `BatchUpdateUserLicenses`

- **Method**: `google.cloud.discoveryengine.v1alpha.UserLicenseService.BatchUpdateUserLicenses`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserLicenseService.BatchUpdateUserLicenses"`

#### `ExportUserLicenses`

- **Method**: `google.cloud.discoveryengine.v1alpha.UserLicenseService.ExportUserLicenses`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userStores.listUserLicenses - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserLicenseService.ExportUserLicenses"`

### `google.cloud.discoveryengine.v1alpha.UserStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.UserStoreService`.

#### `UpdateUserStore`

- **Method**: `google.cloud.discoveryengine.v1alpha.UserStoreService.UpdateUserStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.userStores.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserStoreService.UpdateUserStore"`

### `google.cloud.discoveryengine.v1alpha.WidgetConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.WidgetConfigService`.

#### `GetWidgetConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.WidgetConfigService.GetWidgetConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.widgetConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.WidgetConfigService.GetWidgetConfig"`

#### `UpdateWidgetConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.WidgetConfigService.UpdateWidgetConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.widgetConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.WidgetConfigService.UpdateWidgetConfig"`

### `google.cloud.discoveryengine.v1beta.AclConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.AclConfigService`.

#### `GetAclConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.AclConfigService.GetAclConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.aclConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.AclConfigService.GetAclConfig"`

#### `UpdateAclConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.AclConfigService.UpdateAclConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.aclConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.AclConfigService.UpdateAclConfig"`

### `google.cloud.discoveryengine.v1beta.AssistantService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.AssistantService`.

#### `CreateAssistant`

- **Method**: `google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant"`

#### `DeleteAssistant`

- **Method**: `google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant"`

#### `GetAssistant`

- **Method**: `google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant"`

#### `ListAssistants`

- **Method**: `google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants"`

#### `StreamAssist`

- **Method**: `google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.assist - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist"`

#### `UpdateAssistant`

- **Method**: `google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant"`

### `google.cloud.discoveryengine.v1beta.CmekConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.CmekConfigService`.

#### `DeleteCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.CmekConfigService.DeleteCmekConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cmekConfigs.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfigService.DeleteCmekConfig"`

#### `GetCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.CmekConfigService.GetCmekConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.cmekConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfigService.GetCmekConfig"`

#### `ListCmekConfigs`

- **Method**: `google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmekConfigs`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.cmekConfigs.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmekConfigs"`

#### `UpdateCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.CmekConfigService.UpdateCmekConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cmekConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfigService.UpdateCmekConfig"`

### `google.cloud.discoveryengine.v1beta.CompletionService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.CompletionService`.

#### `AdvancedCompleteQuery`

- **Method**: `google.cloud.discoveryengine.v1beta.CompletionService.AdvancedCompleteQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionConfigs.completeQuery - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.AdvancedCompleteQuery"`

#### `CompleteQuery`

- **Method**: `google.cloud.discoveryengine.v1beta.CompletionService.CompleteQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.completeQuery - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.CompleteQuery"`

#### `ImportCompletionSuggestions`

- **Method**: `google.cloud.discoveryengine.v1beta.CompletionService.ImportCompletionSuggestions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionSuggestions.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.ImportCompletionSuggestions"`

#### `ImportSuggestionDenyListEntries`

- **Method**: `google.cloud.discoveryengine.v1beta.CompletionService.ImportSuggestionDenyListEntries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.suggestionDenyListEntries.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.ImportSuggestionDenyListEntries"`

#### `PurgeCompletionSuggestions`

- **Method**: `google.cloud.discoveryengine.v1beta.CompletionService.PurgeCompletionSuggestions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionSuggestions.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.PurgeCompletionSuggestions"`

#### `PurgeSuggestionDenyListEntries`

- **Method**: `google.cloud.discoveryengine.v1beta.CompletionService.PurgeSuggestionDenyListEntries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.PurgeSuggestionDenyListEntries"`

#### `RemoveSuggestion`

- **Method**: `google.cloud.discoveryengine.v1beta.CompletionService.RemoveSuggestion`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionConfigs.removeSuggestion - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.CompletionService.RemoveSuggestion"`

### `google.cloud.discoveryengine.v1beta.ControlService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.ControlService`.

#### `CreateControl`

- **Method**: `google.cloud.discoveryengine.v1beta.ControlService.CreateControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.CreateControl"`

#### `DeleteControl`

- **Method**: `google.cloud.discoveryengine.v1beta.ControlService.DeleteControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.DeleteControl"`

#### `GetControl`

- **Method**: `google.cloud.discoveryengine.v1beta.ControlService.GetControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.GetControl"`

#### `ListControls`

- **Method**: `google.cloud.discoveryengine.v1beta.ControlService.ListControls`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.ListControls"`

#### `UpdateControl`

- **Method**: `google.cloud.discoveryengine.v1beta.ControlService.UpdateControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlService.UpdateControl"`

### `google.cloud.discoveryengine.v1beta.ConversationalSearchService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.ConversationalSearchService`.

#### `AnswerQuery`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.AnswerQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.answer - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.AnswerQuery"`

#### `ConverseConversation`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ConverseConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.converse - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.ConverseConversation"`

#### `CreateConversation`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateConversation"`

#### `CreateSession`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateSession"`

#### `DeleteConversation`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteConversation"`

#### `DeleteSession`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteSession"`

#### `GetAnswer`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetAnswer`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.answers.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetAnswer"`

#### `GetConversation`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetConversation"`

#### `GetSession`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetSession"`

#### `ListConversations`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListConversations`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListConversations"`

#### `ListSessions`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListSessions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListSessions"`

#### `StreamAnswerQuery`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.StreamAnswerQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.answer - DATA_READ`
- **Method is a long-running or streaming operation**:
  [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.StreamAnswerQuery"`

#### `UpdateConversation`

- **Method**: `google.cloud.discoveryengine.v1beta.ConversationalSearchService.UpdateConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ConversationalSearchService.UpdateConversation"`

### `google.cloud.discoveryengine.v1beta.DataStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.DataStoreService`.

#### `CreateDataStore`

- **Method**: `google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore"`

#### `DeleteDataStore`

- **Method**: `google.cloud.discoveryengine.v1beta.DataStoreService.DeleteDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.DeleteDataStore"`

#### `GetDataStore`

- **Method**: `google.cloud.discoveryengine.v1beta.DataStoreService.GetDataStore`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.GetDataStore"`

#### `ListDataStores`

- **Method**: `google.cloud.discoveryengine.v1beta.DataStoreService.ListDataStores`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.ListDataStores"`

#### `UpdateDataStore`

- **Method**: `google.cloud.discoveryengine.v1beta.DataStoreService.UpdateDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreService.UpdateDataStore"`

### `google.cloud.discoveryengine.v1beta.DocumentService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.DocumentService`.

#### `BatchGetDocumentsMetadata`

- **Method**: `google.cloud.discoveryengine.v1beta.DocumentService.BatchGetDocumentsMetadata`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.BatchGetDocumentsMetadata"`

#### `CreateDocument`

- **Method**: `google.cloud.discoveryengine.v1beta.DocumentService.CreateDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.CreateDocument"`

#### `DeleteDocument`

- **Method**: `google.cloud.discoveryengine.v1beta.DocumentService.DeleteDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.DeleteDocument"`

#### `GetDocument`

- **Method**: `google.cloud.discoveryengine.v1beta.DocumentService.GetDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.GetDocument"`

#### `ImportDocuments`

- **Method**: `google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments"`

#### `ListDocuments`

- **Method**: `google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments"`

#### `PurgeDocuments`

- **Method**: `google.cloud.discoveryengine.v1beta.DocumentService.PurgeDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.PurgeDocuments"`

#### `UpdateDocument`

- **Method**: `google.cloud.discoveryengine.v1beta.DocumentService.UpdateDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentService.UpdateDocument"`
