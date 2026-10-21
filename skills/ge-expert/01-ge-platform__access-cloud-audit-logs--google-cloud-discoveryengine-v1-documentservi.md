# Gemini Enterprise: platform, security, agents, cost, monitoring / Access Cloud Audit Logs: API interface audit logs / google.cloud.discoveryengine.v1.DocumentService to API interface audit logs / google.cloud.discoveryengine.v1alpha.AssistantService
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 791-830, extracted 2026-10-18

## Access Cloud Audit Logs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.DocumentService` . 

`BatchGetDocumentsMetadata` 

**Method** : 

```
google.cloud.discoveryengine.v1.DocumentService.BatchGetDocumentsMetada
ta
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentServic
e.BatchGetDocumentsMetadata"
```

`CreateDocument` 

**Method** : `google.cloud.discoveryengine.v1.DocumentService.CreateDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.documents.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentServic
```

`e.CreateDocument"` 

```
DeleteDocument
```

**Method** : `google.cloud.discoveryengine.v1.DocumentService.DeleteDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.delete - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentServic
e.DeleteDocument"
GetDocument
```

**Method** : `google.cloud.discoveryengine.v1.DocumentService.GetDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.get - DATA_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentServic
e.GetDocument"
ImportDocuments
```

**Method** : 

`google.cloud.discoveryengine.v1.DocumentService.ImportDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.import - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentServic
e.ImportDocuments"
ListDocuments
```

**Method** : `google.cloud.discoveryengine.v1.DocumentService.ListDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentServic
e.ListDocuments"
PurgeDocuments
```

**Method** : `google.cloud.discoveryengine.v1.DocumentService.PurgeDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.purge - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentServic
e.PurgeDocuments"
UpdateDocument
```

**Method** : `google.cloud.discoveryengine.v1.DocumentService.UpdateDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.update - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.DocumentServic
e.UpdateDocument"
google.cloud.discoveryengine.v1.EngineService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.EngineService` . 

```
CreateEngine
```

- **Method** : `google.cloud.discoveryengine.v1.EngineService.CreateEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.engines.create - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.
CreateEngine"
DeleteEngine
```

- **Method** : `google.cloud.discoveryengine.v1.EngineService.DeleteEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.engines.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.
DeleteEngine"
```

`GetEngine` 

**Method** : `google.cloud.discoveryengine.v1.EngineService.GetEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.engines.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.
GetEngine"
```

`GetIamPolicy` 

**Method** : `google.cloud.discoveryengine.v1.EngineService.GetIamPolicy` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.engines.getIamPolicy - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.
GetIamPolicy"
```

`ListEngines` 

**Method** : `google.cloud.discoveryengine.v1.EngineService.ListEngines` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.engines.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.
ListEngines"
```

`SetIamPolicy` 

**Method** : `google.cloud.discoveryengine.v1.EngineService.SetIamPolicy` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.engines.setIamPolicy - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.
SetIamPolicy"
UpdateEngine
```

**Method** : `google.cloud.discoveryengine.v1.EngineService.UpdateEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.engines.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.EngineService.
UpdateEngine"
google.cloud.discoveryengine.v1.GroundedGenerationService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.GroundedGenerationService` . 

`CheckGrounding` 

**Method** : 

- `google.cloud.discoveryengine.v1.GroundedGenerationService.CheckGroundin` `g` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.groundingConfigs.check - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.GroundedGenera
tionService.CheckGrounding"
google.cloud.discoveryengine.v1.IdentityMappingStoreService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.IdentityMappingStoreService` . 

`CreateIdentityMappingStore` 

**Method** : 

```
google.cloud.discoveryengine.v1.IdentityMappingStoreService.CreateIdent
ityMappingStore
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.identityMappingStores.create - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappin
gStoreService.CreateIdentityMappingStore"
DeleteIdentityMappingStore
```

**Method** : 

- `google.cloud.discoveryengine.v1.IdentityMappingStoreService.DeleteIdent ityMappingStore` 

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.identityMappingStores.delete - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappin
gStoreService.DeleteIdentityMappingStore"
```

`ImportIdentityMappings` 

**Method** : 

```
google.cloud.discoveryengine.v1.IdentityMappingStoreService.ImportIdent
ityMappings
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

   - `discoveryengine.identityMappingStores.importIdentityMappings - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappin
gStoreService.ImportIdentityMappings"
ListIdentityMappings
```

**Method** : 

```
google.cloud.discoveryengine.v1.IdentityMappingStoreService.ListIdentit
yMappings
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.identityMappingStores.listIdentityMappings -
DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappin
gStoreService.ListIdentityMappings"
PurgeIdentityMappings
```

**Method** : 

```
google.cloud.discoveryengine.v1.IdentityMappingStoreService.PurgeIdenti
tyMappings
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.identityMappingStores.purgeIdentityMappings -
DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.IdentityMappin
gStoreService.PurgeIdentityMappings"
```

`google.cloud.discoveryengine.v1.LicenseConfigService` 

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.LicenseConfigService` . 

`CreateLicenseConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1.LicenseConfigService.CreateLicenseConfi
g
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

**Permissions** : 

`discoveryengine.licenseConfigs.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigS
ervice.CreateLicenseConfig"
DistributeLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1.LicenseConfigService.DistributeLicenseC
onfig
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.billingAccountLicenseConfigs.distribute -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigS
ervice.DistributeLicenseConfig"
GetLicenseConfig
```

**Method** : 

`google.cloud.discoveryengine.v1.LicenseConfigService.GetLicenseConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.licenseConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigS
ervice.GetLicenseConfig"
RetractLicenseConfig
```

**Method** : 

- `google.cloud.discoveryengine.v1.LicenseConfigService.RetractLicenseConf` `ig` 

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigS
ervice.RetractLicenseConfig"
UpdateLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1.LicenseConfigService.UpdateLicenseConfi
g
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.licenseConfigs.update - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.LicenseConfigS
ervice.UpdateLicenseConfig"
```

`google.cloud.discoveryengine.v1.ProjectService` 

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.ProjectService` . 

```
ProvisionProject
```

**Method** : 

`google.cloud.discoveryengine.v1.ProjectService.ProvisionProject` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.projects.provision - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ProjectService
.ProvisionProject"
google.cloud.discoveryengine.v1.RankService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.RankService` . 

`Rank` 

**Method** : `google.cloud.discoveryengine.v1.RankService.Rank` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.rankingConfigs.rank - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.RankService.Ra
nk"
google.cloud.discoveryengine.v1.RecommendationService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.RecommendationService` . 

```
Recommend
```

- **Method** : 

`google.cloud.discoveryengine.v1.RecommendationService.Recommend` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.recommend - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.Recommendation
Service.Recommend"
google.cloud.discoveryengine.v1.SchemaService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SchemaService` . 

```
CreateSchema
```

- **Method** : `google.cloud.discoveryengine.v1.SchemaService.CreateSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.schemas.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.
CreateSchema"
DeleteSchema
```

- **Method** : `google.cloud.discoveryengine.v1.SchemaService.DeleteSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.schemas.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.
DeleteSchema"
```

`GetSchema` 

**Method** : `google.cloud.discoveryengine.v1.SchemaService.GetSchema` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.schemas.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.
GetSchema"
```

`ListSchemas` 

**Method** : `google.cloud.discoveryengine.v1.SchemaService.ListSchemas` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.schemas.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.
ListSchemas"
```

`UpdateSchema` 

**Method** : `google.cloud.discoveryengine.v1.SchemaService.UpdateSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

**Permissions** : 

```
discoveryengine.schemas.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SchemaService.
UpdateSchema"
google.cloud.discoveryengine.v1.SearchService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SearchService` . 

`Search` 

**Method** : `google.cloud.discoveryengine.v1.SearchService.Search` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.search - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SearchService.
Search"
google.cloud.discoveryengine.v1.SearchTuningService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SearchTuningService` . 

```
ListCustomModels
```

**Method** : 

```
google.cloud.discoveryengine.v1.SearchTuningService.ListCustomModels
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataStores.listCustomModels - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SearchTuningSe
rvice.ListCustomModels"
```

`TrainCustomModel` 

**Method** : 

`google.cloud.discoveryengine.v1.SearchTuningService.TrainCustomModel` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataStores.trainCustomModel - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SearchTuningSe
rvice.TrainCustomModel"
google.cloud.discoveryengine.v1.ServingConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.ServingConfigService` . 

`CreateServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1.ServingConfigService.CreateServingConfi
g
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.servingConfigs.create - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigS
ervice.CreateServingConfig"
```

`DeleteServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1.ServingConfigService.DeleteServingConfi
g
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.servingConfigs.delete - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigS
ervice.DeleteServingConfig"
```

`GetServingConfig` 

**Method** : 

`google.cloud.discoveryengine.v1.ServingConfigService.GetServingConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.servingConfigs.get - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigS
ervice.GetServingConfig"
```

`ListServingConfigs` 

**Method** : 

`google.cloud.discoveryengine.v1.ServingConfigService.ListServingConfigs` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigS
ervice.ListServingConfigs"
```

`UpdateServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1.ServingConfigService.UpdateServingConfi
g
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.servingConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.ServingConfigS
ervice.UpdateServingConfig"
google.cloud.discoveryengine.v1.SessionService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SessionService` . 

`CreateSession` 

**Method** : `google.cloud.discoveryengine.v1.SessionService.CreateSession` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService
.CreateSession"
```

`DeleteSession` 

**Method** : `google.cloud.discoveryengine.v1.SessionService.DeleteSession` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.delete - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService
.DeleteSession"
```

`GetSession` 

**Method** : `google.cloud.discoveryengine.v1.SessionService.GetSession` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sessions.get - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService
.GetSession"
```

`ListSessions` 

**Method** : `google.cloud.discoveryengine.v1.SessionService.ListSessions` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.sessions.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService
.ListSessions"
UpdateSession
```

**Method** : `google.cloud.discoveryengine.v1.SessionService.UpdateSession` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.update - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SessionService
.UpdateSession"
google.cloud.discoveryengine.v1.SiteSearchEngineService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.SiteSearchEngineService` . 

```
BatchCreateTargetSites
```

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchCreateTarg
etSites
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.targetSites.batchCreate - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.BatchCreateTargetSites"
```

`BatchVerifyTargetSites` 

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.BatchVerifyTarg
etSites
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.siteSearchEngines.batchVerifyTargetSites -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.BatchVerifyTargetSites"
CreateSitemap
```

**Method** : 

`google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateSitemap` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.sitemaps.create - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.CreateSitemap"
```

`CreateTargetSite` 

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.CreateTargetSit
e
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.targetSites.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.CreateTargetSite"
```

`DeleteSitemap` 

**Method** : 

`google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteSitemap` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.sitemaps.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.DeleteSitemap"
```

`DeleteTargetSite` 

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.DeleteTargetSit
e
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.targetSites.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.DeleteTargetSite"
DisableAdvancedSiteSearch
```

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.DisableAdvanced
SiteSearch
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.siteSearchEngines.disableAdvancedSiteSearch -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.DisableAdvancedSiteSearch"
EnableAdvancedSiteSearch
```

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.EnableAdvancedS
iteSearch
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.siteSearchEngines.enableAdvancedSiteSearch -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.EnableAdvancedSiteSearch"
FetchDomainVerificationStatus
```

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchDomainVeri
ficationStatus
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.siteSearchEngines.fetchDomainVerificationStatus -
ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.FetchDomainVerificationStatus"
FetchSitemaps
```

**Method** : 

`google.cloud.discoveryengine.v1.SiteSearchEngineService.FetchSitemaps` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sitemaps.fetch - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.FetchSitemaps"
GetSiteSearchEngine
```

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.GetSiteSearchEn
gine
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.siteSearchEngines.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.GetSiteSearchEngine"
```

`GetTargetSite` 

**Method** : 

`google.cloud.discoveryengine.v1.SiteSearchEngineService.GetTargetSite` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.targetSites.get - ADMIN_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.GetTargetSite"
```

`ListTargetSites` 

**Method** : 

`google.cloud.discoveryengine.v1.SiteSearchEngineService.ListTargetSites` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.targetSites.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.ListTargetSites"
```

`RecrawlUris` 

**Method** : 

`google.cloud.discoveryengine.v1.SiteSearchEngineService.RecrawlUris` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.RecrawlUris"
```

`UpdateTargetSite` 

**Method** : 

```
google.cloud.discoveryengine.v1.SiteSearchEngineService.UpdateTargetSit
e
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.targetSites.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.SiteSearchEngi
neService.UpdateTargetSite"
google.cloud.discoveryengine.v1.UserEventService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.UserEventService` . 

```
ImportUserEvents
```

**Method** : 

`google.cloud.discoveryengine.v1.UserEventService.ImportUserEvents` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.userEvents.import - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventServi
ce.ImportUserEvents"
PurgeUserEvents
```

**Method** : 

`google.cloud.discoveryengine.v1.UserEventService.PurgeUserEvents` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.userEvents.purge - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventServi
ce.PurgeUserEvents"
```

`WriteUserEvent` 

**Method** : 

`google.cloud.discoveryengine.v1.UserEventService.WriteUserEvent` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.userEvents.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.UserEventServi
ce.WriteUserEvent"
google.cloud.discoveryengine.v1.UserLicenseService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.UserLicenseService` . 

```
BatchUpdateUserLicenses
```

**Method** : 

```
google.cloud.discoveryengine.v1.UserLicenseService.BatchUpdateUserLicen
ses
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.UserLicenseSer
vice.BatchUpdateUserLicenses"
```

`google.cloud.discoveryengine.v1.UserStoreService` 

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.UserStoreService` . 

`UpdateUserStore` 

**Method** : 

`google.cloud.discoveryengine.v1.UserStoreService.UpdateUserStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.userStores.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.UserStoreServi
ce.UpdateUserStore"
```

`google.cloud.discoveryengine.v1.WidgetConfigService` The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1.WidgetConfigService` . 

```
GetWidgetConfig
```

**Method** : 

`google.cloud.discoveryengine.v1.WidgetConfigService.GetWidgetConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.widgetConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.WidgetConfigSe
rvice.GetWidgetConfig"
UpdateWidgetConfig
```

**Method** : 

`google.cloud.discoveryengine.v1.WidgetConfigService.UpdateWidgetConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.widgetConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1.WidgetConfigSe
rvice.UpdateWidgetConfig"
google.cloud.discoveryengine.v1alpha.AclConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AclConfigService` . 

```
GetAclConfig
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AclConfigService.GetAclConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.aclConfigs.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AclConfig
Service.GetAclConfig"
UpdateAclConfig
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AclConfigService.UpdateAclConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.aclConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AclConfig
Service.UpdateAclConfig"
google.cloud.discoveryengine.v1alpha.AgentService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AgentService` . 

```
CreateAgent
```

**Method** : `google.cloud.discoveryengine.v1alpha.AgentService.CreateAgent` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.agents.create - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentServ
ice.CreateAgent"
DeleteAgent
```

**Method** : `google.cloud.discoveryengine.v1alpha.AgentService.DeleteAgent` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.agents.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentServ
ice.DeleteAgent"
ImportAgentFile
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AgentService.ImportAgentFile` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.agentFiles.import - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentServ
ice.ImportAgentFile"
UpdateAgent
```

**Method** : `google.cloud.discoveryengine.v1alpha.AgentService.UpdateAgent` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.agents.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AgentServ
ice.UpdateAgent"
google.cloud.discoveryengine.v1alpha.AlphaEvolveService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AlphaEvolveService` . 

```
AcquirePrograms
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.AcquirePrograms` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.alphaEvolveExperiments.acquirePrograms -
DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.AcquirePrograms"
CreateAlphaEvolveExperiment
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvol
veExperiment
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.alphaEvolveExperiments.create - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.CreateAlphaEvolveExperiment"
```

`CreateAlphaEvolveProgram` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.CreateAlphaEvol
veProgram
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.alphaEvolvePrograms.create - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.CreateAlphaEvolveProgram"
```

`DeleteAlphaEvolveExperimentAndPrograms` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.DeleteAlphaEvol
veExperimentAndPrograms
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.alphaEvolveExperiments.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.DeleteAlphaEvolveExperimentAndPrograms"
GetAlphaEvolveExperiment
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveE
xperiment
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.alphaEvolveExperiments.get - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.GetAlphaEvolveExperiment"
GetAlphaEvolveProgram
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.GetAlphaEvolveP
rogram
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.alphaEvolvePrograms.get - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
```

`veService.GetAlphaEvolveProgram"` 

`ListAlphaEvolveExperiments` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolve
Experiments
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.alphaEvolveExperiments.list - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.ListAlphaEvolveExperiments"
```

`ListAlphaEvolvePrograms` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolve
Programs
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.alphaEvolvePrograms.list - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.ListAlphaEvolvePrograms"
```

`ResumeExperiment` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ResumeExperimen
t
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.alphaEvolveExperiments.resume - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.ResumeExperiment"
StartExperiment
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AlphaEvolveService.StartExperiment` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.alphaEvolveExperiments.start - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.StartExperiment"
SubmitProgramsEvaluations
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AlphaEvolveService.SubmitProgramsE
valuations
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.alphaEvolveExperiments.submitProgramsEvaluations -
DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.AlphaEvol
veService.SubmitProgramsEvaluations"
google.cloud.discoveryengine.v1alpha.AnalyticsService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AnalyticsService` . 

`ExportMetrics` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.AnalyticsService.ExportMetrics` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.analytics.exportMetrics - DATA_READ` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Analytics
Service.ExportMetrics"
```

`GetAnalyticsConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AnalyticsService.GetAnalyticsConfi
g
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.analyticsConfigs.get - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Analytics
```

`Service.GetAnalyticsConfig"` 

```
UpdateAnalyticsConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AnalyticsService.UpdateAnalyticsCo
nfig
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.analyticsConfigs.update - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Analytics
Service.UpdateAnalyticsConfig"
google.cloud.discoveryengine.v1alpha.AssistantService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AssistantService` . 

`CreateAssistant` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.AssistantService.CreateAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

   - `discoveryengine.assistants.create - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Assistant
Service.CreateAssistant"
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AssistantService.DeleteAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.assistants.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Assistant
Service.DeleteAssistant"
GetAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AssistantService.GetAssistant` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.assistants.get - ADMIN_READ
```

- **Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Assistant
Service.GetAssistant"
ListAssistants
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AssistantService.ListAssistants` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.assistants.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Assistant
Service.ListAssistants"
StreamAssist
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AssistantService.StreamAssist` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.assistants.assist - DATA_WRITE` **Method is a long-running or streaming operation** : **Streaming RPC** (/logging/docs/audit/understanding-audit-logs#streaming) **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Assistant
Service.StreamAssist"
UpdateAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.AssistantService.UpdateAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.assistants.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Assistant
Service.UpdateAssistant"
google.cloud.discoveryengine.v1alpha.AuthorizationService
```
