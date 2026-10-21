# Gemini Enterprise Docs (Monitor usage) / Access Gemini Enterprise Cloud Audit Logs (part 2 of 5: API interface audit logs: google.cloud.discoveryengine.v1.DataStoreService to google.cloud.discoveryengine.v1alpha.BranchService)
Source: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging, page last updated 2026-10-14, extracted 2026-10-19

## API interface audit logs

### `google.cloud.discoveryengine.v1.DataStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.DataStoreService`.

#### `CreateDataStore`

- **Method**: `google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.CreateDataStore"`

#### `DeleteDataStore`

- **Method**: `google.cloud.discoveryengine.v1.DataStoreService.DeleteDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.DeleteDataStore"`

#### `GetDataStore`

- **Method**: `google.cloud.discoveryengine.v1.DataStoreService.GetDataStore`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.GetDataStore"`

#### `ListDataStores`

- **Method**: `google.cloud.discoveryengine.v1.DataStoreService.ListDataStores`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.ListDataStores"`

#### `UpdateDataStore`

- **Method**: `google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DataStoreService.UpdateDataStore"`

### `google.cloud.discoveryengine.v1.DocumentService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.DocumentService`.

#### `BatchGetDocumentsMetadata`

- **Method**: `google.cloud.discoveryengine.v1.DocumentService.BatchGetDocumentsMetadata`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.BatchGetDocumentsMetadata"`

#### `CreateDocument`

- **Method**: `google.cloud.discoveryengine.v1.DocumentService.CreateDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.CreateDocument"`

#### `DeleteDocument`

- **Method**: `google.cloud.discoveryengine.v1.DocumentService.DeleteDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.DeleteDocument"`

#### `GetDocument`

- **Method**: `google.cloud.discoveryengine.v1.DocumentService.GetDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.GetDocument"`

#### `ImportDocuments`

- **Method**: `google.cloud.discoveryengine.v1.DocumentService.ImportDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.ImportDocuments"`

#### `ListDocuments`

- **Method**: `google.cloud.discoveryengine.v1.DocumentService.ListDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.ListDocuments"`

#### `PurgeDocuments`

- **Method**: `google.cloud.discoveryengine.v1.DocumentService.PurgeDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.PurgeDocuments"`

#### `UpdateDocument`

- **Method**: `google.cloud.discoveryengine.v1.DocumentService.UpdateDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentService.UpdateDocument"`

### `google.cloud.discoveryengine.v1.EngineService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.EngineService`.

#### `CreateEngine`

- **Method**: `google.cloud.discoveryengine.v1.EngineService.CreateEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.CreateEngine"`

#### `DeleteEngine`

- **Method**: `google.cloud.discoveryengine.v1.EngineService.DeleteEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.DeleteEngine"`

#### `GetEngine`

- **Method**: `google.cloud.discoveryengine.v1.EngineService.GetEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.GetEngine"`

#### `GetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1.EngineService.GetIamPolicy`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.getIamPolicy - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.GetIamPolicy"`

#### `ListEngines`

- **Method**: `google.cloud.discoveryengine.v1.EngineService.ListEngines`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.ListEngines"`

#### `SetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1.EngineService.SetIamPolicy`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.setIamPolicy - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.SetIamPolicy"`

#### `UpdateEngine`

- **Method**: `google.cloud.discoveryengine.v1.EngineService.UpdateEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.UpdateEngine"`

### `google.cloud.discoveryengine.v1.GroundedGenerationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.GroundedGenerationService`.

#### `CheckGrounding`

- **Method**: `google.cloud.discoveryengine.v1.GroundedGenerationService.CheckGrounding`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.groundingConfigs.check - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.GroundedGenerationService.CheckGrounding"`

### `google.cloud.discoveryengine.v1.IdentityMappingStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.IdentityMappingStoreService`.

#### `CreateIdentityMappingStore`

- **Method**: `google.cloud.discoveryengine.v1.IdentityMappingStoreService.CreateIdentityMappingStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.identityMappingStores.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.CreateIdentityMappingStore"`

#### `DeleteIdentityMappingStore`

- **Method**: `google.cloud.discoveryengine.v1.IdentityMappingStoreService.DeleteIdentityMappingStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.identityMappingStores.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.DeleteIdentityMappingStore"`

#### `ImportIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1.IdentityMappingStoreService.ImportIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.importIdentityMappings - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.ImportIdentityMappings"`

#### `ListIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1.IdentityMappingStoreService.ListIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.listIdentityMappings - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.ListIdentityMappings"`

#### `PurgeIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1.IdentityMappingStoreService.PurgeIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.purgeIdentityMappings - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappingStoreService.PurgeIdentityMappings"`

### `google.cloud.discoveryengine.v1.LicenseConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.LicenseConfigService`.

#### `CreateLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1.LicenseConfigService.CreateLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.licenseConfigs.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.CreateLicenseConfig"`

#### `DistributeLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1.LicenseConfigService.DistributeLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.billingAccountLicenseConfigs.distribute - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.DistributeLicenseConfig"`

#### `GetLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1.LicenseConfigService.GetLicenseConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.licenseConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.GetLicenseConfig"`

#### `RetractLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1.LicenseConfigService.RetractLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.RetractLicenseConfig"`

#### `UpdateLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1.LicenseConfigService.UpdateLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.licenseConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigService.UpdateLicenseConfig"`

### `google.cloud.discoveryengine.v1.ProjectService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.ProjectService`.

#### `ProvisionProject`

- **Method**: `google.cloud.discoveryengine.v1.ProjectService.ProvisionProject`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.projects.provision - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ProjectService.ProvisionProject"`

### `google.cloud.discoveryengine.v1.RankService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.RankService`.

#### `Rank`

- **Method**: `google.cloud.discoveryengine.v1.RankService.Rank`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.rankingConfigs.rank - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.RankService.Rank"`

### `google.cloud.discoveryengine.v1.RecommendationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.RecommendationService`.

#### `Recommend`

- **Method**: `google.cloud.discoveryengine.v1.RecommendationService.Recommend`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.recommend - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.RecommendationService.Recommend"`

### `google.cloud.discoveryengine.v1.SchemaService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.SchemaService`.

#### `CreateSchema`

- **Method**: `google.cloud.discoveryengine.v1.SchemaService.CreateSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.CreateSchema"`

#### `DeleteSchema`

- **Method**: `google.cloud.discoveryengine.v1.SchemaService.DeleteSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.DeleteSchema"`

#### `GetSchema`

- **Method**: `google.cloud.discoveryengine.v1.SchemaService.GetSchema`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.schemas.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.GetSchema"`

#### `ListSchemas`

- **Method**: `google.cloud.discoveryengine.v1.SchemaService.ListSchemas`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.schemas.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.ListSchemas"`

#### `UpdateSchema`

- **Method**: `google.cloud.discoveryengine.v1.SchemaService.UpdateSchema`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.schemas.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.UpdateSchema"`

### `google.cloud.discoveryengine.v1.SearchService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.SearchService`.

#### `Search`

- **Method**: `google.cloud.discoveryengine.v1.SearchService.Search`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.search - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SearchService.Search"`

### `google.cloud.discoveryengine.v1.SearchTuningService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.SearchTuningService`.

#### `ListCustomModels`

- **Method**: `google.cloud.discoveryengine.v1.SearchTuningService.ListCustomModels`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.listCustomModels - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SearchTuningService.ListCustomModels"`

#### `TrainCustomModel`

- **Method**: `google.cloud.discoveryengine.v1.SearchTuningService.TrainCustomModel`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.trainCustomModel - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SearchTuningService.TrainCustomModel"`

### `google.cloud.discoveryengine.v1.ServingConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.ServingConfigService`.

#### `CreateServingConfig`

- **Method**: `google.cloud.discoveryengine.v1.ServingConfigService.CreateServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.CreateServingConfig"`

#### `DeleteServingConfig`

- **Method**: `google.cloud.discoveryengine.v1.ServingConfigService.DeleteServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.DeleteServingConfig"`

#### `GetServingConfig`

- **Method**: `google.cloud.discoveryengine.v1.ServingConfigService.GetServingConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.GetServingConfig"`

#### `ListServingConfigs`

- **Method**: `google.cloud.discoveryengine.v1.ServingConfigService.ListServingConfigs`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.ListServingConfigs"`

#### `UpdateServingConfig`

- **Method**: `google.cloud.discoveryengine.v1.ServingConfigService.UpdateServingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.servingConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigService.UpdateServingConfig"`

### `google.cloud.discoveryengine.v1.SessionService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.SessionService`.

#### `CreateSession`

- **Method**: `google.cloud.discoveryengine.v1.SessionService.CreateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.CreateSession"`

#### `DeleteSession`

- **Method**: `google.cloud.discoveryengine.v1.SessionService.DeleteSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.DeleteSession"`

#### `GetSession`

- **Method**: `google.cloud.discoveryengine.v1.SessionService.GetSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.GetSession"`

#### `ListSessions`

- **Method**: `google.cloud.discoveryengine.v1.SessionService.ListSessions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.ListSessions"`

#### `UpdateSession`

- **Method**: `google.cloud.discoveryengine.v1.SessionService.UpdateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService.UpdateSession"`

### `google.cloud.discoveryengine.v1.SiteSearchEngineService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.SiteSearchEngineService`.

#### `BatchCreateTargetSites`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchCreateTargetSites`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.batchCreate - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchCreateTargetSites"`

#### `BatchVerifyTargetSites`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchVerifyTargetSites`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.batchVerifyTargetSites - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchVerifyTargetSites"`

#### `CreateSitemap`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateSitemap`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.sitemaps.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateSitemap"`

#### `CreateTargetSite`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateTargetSite"`

#### `DeleteSitemap`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteSitemap`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.sitemaps.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteSitemap"`

#### `DeleteTargetSite`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteTargetSite"`

#### `DisableAdvancedSiteSearch`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.DisableAdvancedSiteSearch`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.disableAdvancedSiteSearch - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.DisableAdvancedSiteSearch"`

#### `EnableAdvancedSiteSearch`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.EnableAdvancedSiteSearch`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.enableAdvancedSiteSearch - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.EnableAdvancedSiteSearch"`

#### `FetchDomainVerificationStatus`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchDomainVerificationStatus`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.fetchDomainVerificationStatus - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchDomainVerificationStatus"`

#### `FetchSitemaps`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchSitemaps`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sitemaps.fetch - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchSitemaps"`

#### `GetSiteSearchEngine`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.GetSiteSearchEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.GetSiteSearchEngine"`

#### `GetTargetSite`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.GetTargetSite`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.GetTargetSite"`

#### `ListTargetSites`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.ListTargetSites`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.targetSites.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.ListTargetSites"`

#### `RecrawlUris`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.RecrawlUris`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.RecrawlUris"`

#### `UpdateTargetSite`

- **Method**: `google.cloud.discoveryengine.v1.SiteSearchEngineService.UpdateTargetSite`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.targetSites.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngineService.UpdateTargetSite"`

### `google.cloud.discoveryengine.v1.UserEventService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.UserEventService`.

#### `ImportUserEvents`

- **Method**: `google.cloud.discoveryengine.v1.UserEventService.ImportUserEvents`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventService.ImportUserEvents"`

#### `PurgeUserEvents`

- **Method**: `google.cloud.discoveryengine.v1.UserEventService.PurgeUserEvents`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventService.PurgeUserEvents"`

#### `WriteUserEvent`

- **Method**: `google.cloud.discoveryengine.v1.UserEventService.WriteUserEvent`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.userEvents.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventService.WriteUserEvent"`

### `google.cloud.discoveryengine.v1.UserLicenseService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.UserLicenseService`.

#### `BatchUpdateUserLicenses`

- **Method**: `google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUserLicenses`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUserLicenses"`

### `google.cloud.discoveryengine.v1.UserStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.UserStoreService`.

#### `UpdateUserStore`

- **Method**: `google.cloud.discoveryengine.v1.UserStoreService.UpdateUserStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.userStores.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.UserStoreService.UpdateUserStore"`

### `google.cloud.discoveryengine.v1.WidgetConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1.WidgetConfigService`.

#### `GetWidgetConfig`

- **Method**: `google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.widgetConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig"`

#### `UpdateWidgetConfig`

- **Method**: `google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidgetConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.widgetConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidgetConfig"`

### `google.cloud.discoveryengine.v1alpha.AclConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.AclConfigService`.

#### `GetAclConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.AclConfigService.GetAclConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.aclConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AclConfigService.GetAclConfig"`

#### `UpdateAclConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.AclConfigService.UpdateAclConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.aclConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AclConfigService.UpdateAclConfig"`

### `google.cloud.discoveryengine.v1alpha.AgentService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.AgentService`.

#### `CreateAgent`

- **Method**: `google.cloud.discoveryengine.v1alpha.AgentService.CreateAgent`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.agents.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentService.CreateAgent"`

#### `DeleteAgent`

- **Method**: `google.cloud.discoveryengine.v1alpha.AgentService.DeleteAgent`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.agents.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentService.DeleteAgent"`

#### `ImportAgentFile`

- **Method**: `google.cloud.discoveryengine.v1alpha.AgentService.ImportAgentFile`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.agentFiles.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentService.ImportAgentFile"`

#### `UpdateAgent`

- **Method**: `google.cloud.discoveryengine.v1alpha.AgentService.UpdateAgent`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.agents.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentService.UpdateAgent"`

### `google.cloud.discoveryengine.v1alpha.AlphaEvolveService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.AlphaEvolveService`.

#### `AcquirePrograms`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.AcquirePrograms`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolveExperiments.acquirePrograms - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.AcquirePrograms"`

#### `CreateAlphaEvolveExperiment`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveExperiment`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolveExperiments.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveExperiment"`

#### `CreateAlphaEvolveProgram`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveProgram`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolvePrograms.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvolveProgram"`

#### `DeleteAlphaEvolveExperimentAndPrograms`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.DeleteAlphaEvolveExperimentAndPrograms`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.alphaEvolveExperiments.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.DeleteAlphaEvolveExperimentAndPrograms"`

#### `GetAlphaEvolveExperiment`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveExperiment`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolveExperiments.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveExperiment"`

#### `GetAlphaEvolveProgram`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveProgram`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolvePrograms.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveProgram"`

#### `ListAlphaEvolveExperiments`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolveExperiments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolveExperiments.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolveExperiments"`

#### `ListAlphaEvolvePrograms`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolvePrograms`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolvePrograms.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolvePrograms"`

#### `ResumeExperiment`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ResumeExperiment`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolveExperiments.resume - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ResumeExperiment"`

#### `StartExperiment`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.StartExperiment`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolveExperiments.start - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.StartExperiment"`

#### `SubmitProgramsEvaluations`

- **Method**: `google.cloud.discoveryengine.v1alpha.AlphaEvolveService.SubmitProgramsEvaluations`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.alphaEvolveExperiments.submitProgramsEvaluations - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvolveService.SubmitProgramsEvaluations"`

### `google.cloud.discoveryengine.v1alpha.AnalyticsService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.AnalyticsService`.

#### `ExportMetrics`

- **Method**: `google.cloud.discoveryengine.v1alpha.AnalyticsService.ExportMetrics`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.analytics.exportMetrics - DATA_READ`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AnalyticsService.ExportMetrics"`

#### `GetAnalyticsConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.AnalyticsService.GetAnalyticsConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.analyticsConfigs.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AnalyticsService.GetAnalyticsConfig"`

#### `UpdateAnalyticsConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.AnalyticsService.UpdateAnalyticsConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.analyticsConfigs.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AnalyticsService.UpdateAnalyticsConfig"`

### `google.cloud.discoveryengine.v1alpha.AssistantService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.AssistantService`.

#### `CreateAssistant`

- **Method**: `google.cloud.discoveryengine.v1alpha.AssistantService.CreateAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.CreateAssistant"`

#### `DeleteAssistant`

- **Method**: `google.cloud.discoveryengine.v1alpha.AssistantService.DeleteAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.DeleteAssistant"`

#### `GetAssistant`

- **Method**: `google.cloud.discoveryengine.v1alpha.AssistantService.GetAssistant`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.GetAssistant"`

#### `ListAssistants`

- **Method**: `google.cloud.discoveryengine.v1alpha.AssistantService.ListAssistants`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.ListAssistants"`

#### `StreamAssist`

- **Method**: `google.cloud.discoveryengine.v1alpha.AssistantService.StreamAssist`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.assistants.assist - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.StreamAssist"`

#### `UpdateAssistant`

- **Method**: `google.cloud.discoveryengine.v1alpha.AssistantService.UpdateAssistant`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.assistants.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AssistantService.UpdateAssistant"`

### `google.cloud.discoveryengine.v1alpha.AuthorizationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.AuthorizationService`.

#### `CreateAuthorization`

- **Method**: `google.cloud.discoveryengine.v1alpha.AuthorizationService.CreateAuthorization`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.authorizations.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.CreateAuthorization"`

#### `DeleteAuthorization`

- **Method**: `google.cloud.discoveryengine.v1alpha.AuthorizationService.DeleteAuthorization`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.authorizations.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.DeleteAuthorization"`

#### `GetAuthorization`

- **Method**: `google.cloud.discoveryengine.v1alpha.AuthorizationService.GetAuthorization`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.authorizations.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.GetAuthorization"`

#### `ListAuthorizations`

- **Method**: `google.cloud.discoveryengine.v1alpha.AuthorizationService.ListAuthorizations`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.authorizations.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.ListAuthorizations"`

#### `UpdateAuthorization`

- **Method**: `google.cloud.discoveryengine.v1alpha.AuthorizationService.UpdateAuthorization`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.authorizations.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AuthorizationService.UpdateAuthorization"`

### `google.cloud.discoveryengine.v1alpha.BranchService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.BranchService`.

#### `GetBranch`

- **Method**: `google.cloud.discoveryengine.v1alpha.BranchService.GetBranch`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.branches.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.BranchService.GetBranch"`

#### `ListBranches`

- **Method**: `google.cloud.discoveryengine.v1alpha.BranchService.ListBranches`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.branches.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.BranchService.ListBranches"`
