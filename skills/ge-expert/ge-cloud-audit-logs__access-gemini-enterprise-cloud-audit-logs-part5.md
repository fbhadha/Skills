# Gemini Enterprise Docs (Monitor usage) / Access Gemini Enterprise Cloud Audit Logs (part 5 of 5: API interface audit logs: google.cloud.discoveryengine.v1beta.EngineService to google.longrunning.Operations)
Source: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging, page last updated 2026-10-14, extracted 2026-10-19

## API interface audit logs

### `google.cloud.discoveryengine.v1beta.EngineService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.EngineService`.

#### `CreateEngine`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.CreateEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.CreateEngine"`

#### `DeleteEngine`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.DeleteEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.DeleteEngine"`

#### `GetEngine`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.GetEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.GetEngine"`

#### `GetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.GetIamPolicy`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.getIamPolicy - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.GetIamPolicy"`

#### `ListEngines`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.ListEngines`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.ListEngines"`

#### `PauseEngine`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.PauseEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.pause - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.PauseEngine"`

#### `ResumeEngine`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.ResumeEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.resume - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.ResumeEngine"`

#### `SetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.SetIamPolicy`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.setIamPolicy - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.SetIamPolicy"`

#### `TuneEngine`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.TuneEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.tune - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.TuneEngine"`

#### `UpdateEngine`

- **Method**: `google.cloud.discoveryengine.v1beta.EngineService.UpdateEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineService.UpdateEngine"`

### `google.cloud.discoveryengine.v1beta.EvaluationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.EvaluationService`.

#### `CreateEvaluation`

- **Method**: `google.cloud.discoveryengine.v1beta.EvaluationService.CreateEvaluation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.evaluations.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EvaluationService.CreateEvaluation"`

#### `GetEvaluation`

- **Method**: `google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.evaluations.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluation"`

#### `ListEvaluationResults`

- **Method**: `google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationResults`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.evaluations.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationResults"`

#### `ListEvaluations`

- **Method**: `google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluations`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.evaluations.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluations"`

### `google.cloud.discoveryengine.v1beta.GroundedGenerationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.GroundedGenerationService`.

#### `CheckGrounding`

- **Method**: `google.cloud.discoveryengine.v1beta.GroundedGenerationService.CheckGrounding`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.groundingConfigs.check - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.GroundedGenerationService.CheckGrounding"`

### `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.IdentityMappingStoreService`.

#### `CreateIdentityMappingStore`

- **Method**: `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.CreateIdentityMappingStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.identityMappingStores.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.CreateIdentityMappingStore"`

#### `DeleteIdentityMappingStore`

- **Method**: `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.DeleteIdentityMappingStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.identityMappingStores.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.DeleteIdentityMappingStore"`

#### `ImportIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ImportIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.importIdentityMappings - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ImportIdentityMappings"`

#### `ListIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ListIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.listIdentityMappings - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ListIdentityMappings"`

#### `PurgeIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.PurgeIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.purgeIdentityMappings - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.PurgeIdentityMappings"`

### `google.cloud.discoveryengine.v1beta.LicenseConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.LicenseConfigService`.

#### `CreateLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.licenseConfigs.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseConfig"`

#### `DistributeLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.billingAccountLicenseConfigs.distribute - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLicenseConfig"`

#### `GetLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.licenseConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConfig"`

#### `RetractLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicenseConfig"`

#### `UpdateLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.licenseConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseConfig"`

### `google.cloud.discoveryengine.v1beta.ProjectService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.ProjectService`.

#### `ProvisionProject`

- **Method**: `google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.projects.provision - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject"`

### `google.cloud.discoveryengine.v1beta.RankService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.RankService`.

#### `Rank`

- **Method**: `google.cloud.discoveryengine.v1beta.RankService.Rank`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.rankingConfigs.rank - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.RankService.Rank"`

### `google.cloud.discoveryengine.v1beta.RecommendationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.RecommendationService`.

#### `Recommend`

- **Method**: `google.cloud.discoveryengine.v1beta.RecommendationService.Recommend`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.recommend - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.RecommendationService.Recommend"`

### `google.cloud.discoveryengine.v1beta.SampleQueryService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.SampleQueryService`.

#### `CreateSampleQuery`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQueryService.CreateSampleQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.CreateSampleQuery"`

#### `DeleteSampleQuery`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQueryService.DeleteSampleQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.DeleteSampleQuery"`

#### `GetSampleQuery`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQueryService.GetSampleQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.GetSampleQuery"`

#### `ImportSampleQueries`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQueryService.ImportSampleQueries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.ImportSampleQueries"`

#### `ListSampleQueries`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQueryService.ListSampleQueries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.ListSampleQueries"`

#### `UpdateSampleQuery`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQueryService.UpdateSampleQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQueries.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQueryService.UpdateSampleQuery"`

### `google.cloud.discoveryengine.v1beta.SampleQuerySetService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.SampleQuerySetService`.

#### `CreateSampleQuerySet`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQuerySetService.CreateSampleQuerySet`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.CreateSampleQuerySet"`

#### `DeleteSampleQuerySet`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQuerySetService.DeleteSampleQuerySet`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.DeleteSampleQuerySet"`

#### `GetSampleQuerySet`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSampleQuerySet`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSampleQuerySet"`

#### `ListSampleQuerySets`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQuerySets`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQuerySets"`

#### `UpdateSampleQuerySet`

- **Method**: `google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQuerySet`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sampleQuerySets.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQuerySet"`

### `google.cloud.discoveryengine.v1beta.SchemaService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.SchemaService`.

#### `CreateSchema`

- **Method**: `google.cloud.discoveryengine.v1beta.SchemaService.CreateSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.CreateSchema"`

#### `DeleteSchema`

- **Method**: `google.cloud.discoveryengine.v1beta.SchemaService.DeleteSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.DeleteSchema"`

#### `GetSchema`

- **Method**: `google.cloud.discoveryengine.v1beta.SchemaService.GetSchema`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.schemas.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.GetSchema"`

#### `ListSchemas`

- **Method**: `google.cloud.discoveryengine.v1beta.SchemaService.ListSchemas`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.schemas.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.ListSchemas"`

#### `UpdateSchema`

- **Method**: `google.cloud.discoveryengine.v1beta.SchemaService.UpdateSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaService.UpdateSchema"`

### `google.cloud.discoveryengine.v1beta.SearchService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.SearchService`.

#### `Search`

- **Method**: `google.cloud.discoveryengine.v1beta.SearchService.Search`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.search - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchService.Search"`

### `google.cloud.discoveryengine.v1beta.SearchTuningService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.SearchTuningService`.

#### `ListCustomModels`

- **Method**: `google.cloud.discoveryengine.v1beta.SearchTuningService.ListCustomModels`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.listCustomModels - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchTuningService.ListCustomModels"`

#### `TrainCustomModel`

- **Method**: `google.cloud.discoveryengine.v1beta.SearchTuningService.TrainCustomModel`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.trainCustomModel - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchTuningService.TrainCustomModel"`

### `google.cloud.discoveryengine.v1beta.ServingConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.ServingConfigService`.

#### `CreateServingConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.ServingConfigService.CreateServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.CreateServingConfig"`

#### `DeleteServingConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.ServingConfigService.DeleteServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.DeleteServingConfig"`

#### `GetServingConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.ServingConfigService.GetServingConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.GetServingConfig"`

#### `ListServingConfigs`

- **Method**: `google.cloud.discoveryengine.v1beta.ServingConfigService.ListServingConfigs`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.ListServingConfigs"`

#### `UpdateServingConfig`

- **Method**: `google.cloud.discoveryengine.v1beta.ServingConfigService.UpdateServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingConfigService.UpdateServingConfig"`

### `google.cloud.discoveryengine.v1beta.SessionService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.SessionService`.

#### `CreateSession`

- **Method**: `google.cloud.discoveryengine.v1beta.SessionService.CreateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.CreateSession"`

#### `DeleteSession`

- **Method**: `google.cloud.discoveryengine.v1beta.SessionService.DeleteSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.DeleteSession"`

#### `GetSession`

- **Method**: `google.cloud.discoveryengine.v1beta.SessionService.GetSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.GetSession"`

#### `ListSessions`

- **Method**: `google.cloud.discoveryengine.v1beta.SessionService.ListSessions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.ListSessions"`

#### `UpdateSession`

- **Method**: `google.cloud.discoveryengine.v1beta.SessionService.UpdateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SessionService.UpdateSession"`

### `google.cloud.discoveryengine.v1beta.SiteSearchEngineService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.SiteSearchEngineService`.

#### `BatchCreateTargetSites`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchCreateTargetSites`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.batchCreate - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchCreateTargetSites"`

#### `BatchVerifyTargetSites`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchVerifyTargetSites`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.batchVerifyTargetSites - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.BatchVerifyTargetSites"`

#### `CreateSitemap`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateSitemap`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.sitemaps.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateSitemap"`

#### `CreateTargetSite`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.CreateTargetSite"`

#### `DeleteSitemap`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteSitemap`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.sitemaps.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteSitemap"`

#### `DeleteTargetSite`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DeleteTargetSite"`

#### `DisableAdvancedSiteSearch`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DisableAdvancedSiteSearch`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.disableAdvancedSiteSearch - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.DisableAdvancedSiteSearch"`

#### `EnableAdvancedSiteSearch`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.EnableAdvancedSiteSearch`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.enableAdvancedSiteSearch - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.EnableAdvancedSiteSearch"`

#### `FetchDomainVerificationStatus`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchDomainVerificationStatus`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchDomainVerificationStatus"`

#### `FetchSitemaps`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchSitemaps`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sitemaps.fetch - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.FetchSitemaps"`

#### `GetSiteSearchEngine`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetSiteSearchEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetSiteSearchEngine"`

#### `GetTargetSite`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetTargetSite`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.GetTargetSite"`

#### `ListTargetSites`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.ListTargetSites`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.ListTargetSites"`

#### `RecrawlUris`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.RecrawlUris`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.RecrawlUris"`

#### `UpdateTargetSite`

- **Method**: `google.cloud.discoveryengine.v1beta.SiteSearchEngineService.UpdateTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.SiteSearchEngineService.UpdateTargetSite"`

### `google.cloud.discoveryengine.v1beta.UserEventService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.UserEventService`.

#### `ImportUserEvents`

- **Method**: `google.cloud.discoveryengine.v1beta.UserEventService.ImportUserEvents`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventService.ImportUserEvents"`

#### `PurgeUserEvents`

- **Method**: `google.cloud.discoveryengine.v1beta.UserEventService.PurgeUserEvents`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventService.PurgeUserEvents"`

#### `WriteUserEvent`

- **Method**: `google.cloud.discoveryengine.v1beta.UserEventService.WriteUserEvent`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserEventService.WriteUserEvent"`

### `google.cloud.discoveryengine.v1beta.UserLicenseService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.UserLicenseService`.

#### `BatchUpdateUserLicenses`

- **Method**: `google.cloud.discoveryengine.v1beta.UserLicenseService.BatchUpdateUserLicenses`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserLicenseService.BatchUpdateUserLicenses"`

### `google.cloud.discoveryengine.v1beta.UserStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1beta.UserStoreService`.

#### `UpdateUserStore`

- **Method**: `google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUserStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.userStores.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1beta.UserStoreService.UpdateUserStore"`

### `google.cloud.notebooklm.v1alpha.AudioOverviewService`

The following audit logs are associated with methods belonging to
`google.cloud.notebooklm.v1alpha.AudioOverviewService`.

#### `CreateAudioOverview`

- **Method**: `google.cloud.notebooklm.v1alpha.AudioOverviewService.CreateAudioOverview`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.audioOverviews.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.notebooklm.v1alpha.AudioOverviewService.CreateAudioOverview"`

#### `DeleteAudioOverview`

- **Method**: `google.cloud.notebooklm.v1alpha.AudioOverviewService.DeleteAudioOverview`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.audioOverviews.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.notebooklm.v1alpha.AudioOverviewService.DeleteAudioOverview"`

### `google.cloud.notebooklm.v1alpha.NotebookService`

The following audit logs are associated with methods belonging to
`google.cloud.notebooklm.v1alpha.NotebookService`.

#### `CreateNotebook`

- **Method**: `google.cloud.notebooklm.v1alpha.NotebookService.CreateNotebook`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.notebooks.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookService.CreateNotebook"`

#### `GetNotebook`

- **Method**: `google.cloud.notebooklm.v1alpha.NotebookService.GetNotebook`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.notebooks.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookService.GetNotebook"`

#### `ListRecentlyViewedNotebooks`

- **Method**: `google.cloud.notebooklm.v1alpha.NotebookService.ListRecentlyViewedNotebooks`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.notebooks.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookService.ListRecentlyViewedNotebooks"`

#### `ShareNotebook`

- **Method**: `google.cloud.notebooklm.v1alpha.NotebookService.ShareNotebook`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.notebooks.getIamPolicy - ADMIN_WRITE`
  - `discoveryengine.notebooks.setIamPolicy - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.notebooklm.v1alpha.NotebookService.ShareNotebook"`

### `google.cloud.notebooklm.v1alpha.SourceService`

The following audit logs are associated with methods belonging to
`google.cloud.notebooklm.v1alpha.SourceService`.

#### `BatchCreateSources`

- **Method**: `google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sources.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.notebooklm.v1alpha.SourceService.BatchCreateSources"`

#### `GetSource`

- **Method**: `google.cloud.notebooklm.v1alpha.SourceService.GetSource`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sources.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.notebooklm.v1alpha.SourceService.GetSource"`

### `google.longrunning.Operations`

The following audit logs are associated with methods belonging to
`google.longrunning.Operations`.

#### `CancelOperation`

- **Method**: `google.longrunning.Operations.CancelOperation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.operations.cancel - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.longrunning.Operations.CancelOperation"`

#### `GetOperation`

- **Method**: `google.longrunning.Operations.GetOperation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.operations.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.longrunning.Operations.GetOperation"`

#### `ListOperations`

- **Method**: `google.longrunning.Operations.ListOperations`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.operations.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.longrunning.Operations.ListOperations"`

## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following
reasons:

- It is a high volume method involving significant log generation and storage
  costs.
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
- `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpDeleteRequest`
- `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpGetRequest`
- `google.cloud.discoveryengine.v1.DataConnectorMcpService.ServeMcpPostRequest`
- `google.cloud.discoveryengine.v1.SearchService.SearchLite`
- `google.cloud.discoveryengine.v1.UserEventService.CollectUserEvent`
- `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpDeleteRequest`
- `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpGetRequest`
- `google.cloud.discoveryengine.v1alpha.DataConnectorMcpService.ServeMcpPostRequest`
- `google.cloud.discoveryengine.v1alpha.DataConnectorService.StartConnectorRun`
- `google.cloud.discoveryengine.v1alpha.SearchService.SearchLite`
- `google.cloud.discoveryengine.v1alpha.UserEventService.CollectUserEvent`
- `google.cloud.discoveryengine.v1alpha.WidgetService.LookupWidgetConfig`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAcquireAccessToken`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAcquireAndStoreRefreshToken`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAdvancedCompleteQuery`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetAnswerQuery`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetCompleteQuery`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetConverseConversation`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetCreateSession`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetDeleteSession`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetDisconnectConnector`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetExecuteAction`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetGetSession`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetHomepageFetchDocuments`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetListSessions`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetSearch`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetStreamAnswerQuery`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetUpdateSession`
- `google.cloud.discoveryengine.v1alpha.WidgetService.WidgetWriteUserEvent`
- `google.cloud.discoveryengine.v1beta.SearchService.SearchLite`
- `google.cloud.discoveryengine.v1beta.UserEventService.CollectUserEvent`
