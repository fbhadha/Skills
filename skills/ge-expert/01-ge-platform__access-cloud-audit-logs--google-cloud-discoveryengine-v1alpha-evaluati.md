# Gemini Enterprise: platform, security, agents, cost, monitoring / Access Cloud Audit Logs: API interface audit logs / google.cloud.discoveryengine.v1alpha.EvaluationService to API interface audit logs / google.cloud.discoveryengine.v1beta.CmekConfigService
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 869-907, extracted 2026-10-18

## Access Cloud Audit Logs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.EvaluationService` . 

`CreateEvaluation` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.EvaluationService.CreateEvaluation` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.evaluations.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Evaluatio
nService.CreateEvaluation"
```

`GetEvaluation` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.EvaluationService.GetEvaluation` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.evaluations.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Evaluatio
nService.GetEvaluation"
```

`ListEvaluationResults` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationRe
sults
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.evaluations.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Evaluatio
nService.ListEvaluationResults"
ListEvaluations
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.evaluations.list - DATA_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Evaluatio
nService.ListEvaluations"
```

`google.cloud.discoveryengine.v1alpha.GroundedGenerationService` The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.GroundedGenerationService` . 

```
CheckGrounding
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.GroundedGenerationService.CheckGro
unding
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.groundingConfigs.check - DATA_READ` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.GroundedG
enerationService.CheckGrounding"
google.cloud.discoveryengine.v1alpha.IdentityMappingStore
Service
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService` . 

`CreateIdentityMappingStore` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.Create
IdentityMappingStore
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.identityMappingStores.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityM
appingStoreService.CreateIdentityMappingStore"
```

`DeleteIdentityMappingStore` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.Delete
IdentityMappingStore
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.identityMappingStores.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityM
appingStoreService.DeleteIdentityMappingStore"
ImportIdentityMappings
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.Import
IdentityMappings
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.identityMappingStores.importIdentityMappings -
DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityM
appingStoreService.ImportIdentityMappings"
ListIdentityMappings
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ListId
entityMappings
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.identityMappingStores.listIdentityMappings -
DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityM
appingStoreService.ListIdentityMappings"
PurgeIdentityMappings
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.PurgeI
dentityMappings
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.identityMappingStores.purgeIdentityMappings -
DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityM
appingStoreService.PurgeIdentityMappings"
google.cloud.discoveryengine.v1alpha.LicenseConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.LicenseConfigService` . 

```
CreateLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.LicenseConfigService.CreateLicense
Config
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.licenseConfigs.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseCo
nfigService.CreateLicenseConfig"
DistributeLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.LicenseConfigService.DistributeLic
enseConfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.billingAccountLicenseConfigs.distribute -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseCo
nfigService.DistributeLicenseConfig"
GetBillingAccountLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetBillingAcc
ountLicenseConfig
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.billingAccountLicenseConfigs.get - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseCo
nfigService.GetBillingAccountLicenseConfig"
```

`GetLicenseConfig` 

**Method** : 

- `google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetLicenseCon fig` 

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.licenseConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseCo
nfigService.GetLicenseConfig"
RetractLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.LicenseConfigService.RetractLicens
eConfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseCo
nfigService.RetractLicenseConfig"
UpdateLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.LicenseConfigService.UpdateLicense
Config
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.licenseConfigs.update - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseCo
nfigService.UpdateLicenseConfig"
google.cloud.discoveryengine.v1alpha.ProjectService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ProjectService` . 

```
ProvisionProject
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.ProjectService.ProvisionProject` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.projects.provision - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectSe
rvice.ProvisionProject"
```

`ReportConsentChange` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.ProjectService.ReportConsentChange` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.projects.reportConsentChange - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectSe
rvice.ReportConsentChange"
UpdateProject
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.ProjectService.UpdateProject` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.projects.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectSe
rvice.UpdateProject"
google.cloud.discoveryengine.v1alpha.RankService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.RankService` . 

`Rank` 

**Method** : `google.cloud.discoveryengine.v1alpha.RankService.Rank` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.rankingConfigs.rank - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.RankServi
ce.Rank"
google.cloud.discoveryengine.v1alpha.RecommendationService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.RecommendationService` . 

`Recommend` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.RecommendationService.Recommend` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.servingConfigs.recommend - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Recommend
ationService.Recommend"
google.cloud.discoveryengine.v1alpha.RequirementService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.RequirementService` . 

`CheckRequirement` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.RequirementService.CheckRequiremen
t
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.requirements.checkRequirement - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Requireme
ntService.CheckRequirement"
google.cloud.discoveryengine.v1alpha.SampleQueryService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SampleQueryService` . 

`CreateSampleQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQueryService.CreateSampleQue
ry
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQueries.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
ryService.CreateSampleQuery"
```

`DeleteSampleQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQueryService.DeleteSampleQue
ry
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQueries.delete - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
ryService.DeleteSampleQuery"
```

`GetSampleQuery` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.SampleQueryService.GetSampleQuery` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQueries.get - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
```

`ryService.GetSampleQuery"` 

`ImportSampleQueries` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQueryService.ImportSampleQue
ries
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQueries.import - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
ryService.ImportSampleQueries"
```

`ListSampleQueries` 

**Method** : 

- `google.cloud.discoveryengine.v1alpha.SampleQueryService.ListSampleQueri` `es` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQueries.list - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
ryService.ListSampleQueries"
```

`UpdateSampleQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQueryService.UpdateSampleQue
ry
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.sampleQueries.update - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
ryService.UpdateSampleQuery"
google.cloud.discoveryengine.v1alpha.SampleQuerySetService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SampleQuerySetService` . 

`CreateSampleQuerySet` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQuerySetService.CreateSample
QuerySet
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.sampleQuerySets.create - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
rySetService.CreateSampleQuerySet"
```

`DeleteSampleQuerySet` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQuerySetService.DeleteSample
QuerySet
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

`discoveryengine.sampleQuerySets.delete - DATA_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
rySetService.DeleteSampleQuerySet"
```

`GetSampleQuerySet` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQuerySetService.GetSampleQue
rySet
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sampleQuerySets.get - DATA_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
rySetService.GetSampleQuerySet"
```

`ListSampleQuerySets` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQuerySetService.ListSampleQu
erySets
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.sampleQuerySets.list - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
rySetService.ListSampleQuerySets"
UpdateSampleQuerySet
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SampleQuerySetService.UpdateSample
QuerySet
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQuerySets.update - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SampleQue
rySetService.UpdateSampleQuerySet"
google.cloud.discoveryengine.v1alpha.SchemaService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SchemaService` . 

```
CreateSchema
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.SchemaService.CreateSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.schemas.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaSer
vice.CreateSchema"
DeleteSchema
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.SchemaService.DeleteSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.schemas.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaSer
vice.DeleteSchema"
```

`GetSchema` 

**Method** : `google.cloud.discoveryengine.v1alpha.SchemaService.GetSchema` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.schemas.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaSer
vice.GetSchema"
```

`ListSchemas` 

**Method** : `google.cloud.discoveryengine.v1alpha.SchemaService.ListSchemas` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.schemas.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaSer
vice.ListSchemas"
```

`UpdateSchema` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.SchemaService.UpdateSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

**Permissions** : 

```
discoveryengine.schemas.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SchemaSer
vice.UpdateSchema"
google.cloud.discoveryengine.v1alpha.SearchService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SearchService` . 

`Search` 

**Method** : `google.cloud.discoveryengine.v1alpha.SearchService.Search` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.search - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchSer
vice.Search"
google.cloud.discoveryengine.v1alpha.SearchTuningService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SearchTuningService` . 

`ListCustomModels` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SearchTuningService.ListCustomMode
ls
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.dataStores.listCustomModels - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchTun
ingService.ListCustomModels"
```

`TrainCustomModel` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SearchTuningService.TrainCustomMod
el
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.dataStores.trainCustomModel - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SearchTun
ingService.TrainCustomModel"
google.cloud.discoveryengine.v1alpha.ServingConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ServingConfigService` . 

```
CreateServingConfig
```

**Method** : 

- `google.cloud.discoveryengine.v1alpha.ServingConfigService.CreateServing Config` 

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.servingConfigs.create - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingCo
nfigService.CreateServingConfig"
```

`DeleteServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ServingConfigService.DeleteServing
Config
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.servingConfigs.delete - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingCo
nfigService.DeleteServingConfig"
```

`GetServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ServingConfigService.GetServingCon
fig
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingCo
nfigService.GetServingConfig"
```

`ListServingConfigs` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ServingConfigService.ListServingCo
nfigs
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.servingConfigs.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingCo
nfigService.ListServingConfigs"
```

`UpdateServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ServingConfigService.UpdateServing
Config
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.servingConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ServingCo
nfigService.UpdateServingConfig"
google.cloud.discoveryengine.v1alpha.SessionService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SessionService` . 

`CreateSession` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.SessionService.CreateSession` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sessions.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionSe
rvice.CreateSession"
```

`DeleteSession` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.SessionService.DeleteSession` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.delete - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionSe
rvice.DeleteSession"
```

`GetSession` 

**Method** : `google.cloud.discoveryengine.v1alpha.SessionService.GetSession` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sessions.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionSe
rvice.GetSession"
```

`ListFiles` 

**Method** : `google.cloud.discoveryengine.v1alpha.SessionService.ListFiles` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sessions.listSessionFileMetadata - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionSe
rvice.ListFiles"
```

`ListSessions` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.SessionService.ListSessions` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sessions.list - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionSe
rvice.ListSessions"
```

`UpdateSession` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.SessionService.UpdateSession` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.sessions.update - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SessionSe
rvice.UpdateSession"
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService` . 

```
BatchCreateTargetSites
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchCreat
eTargetSites
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.targetSites.batchCreate - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.BatchCreateTargetSites"
BatchVerifyTargetSites
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.BatchVerif
yTargetSites
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.siteSearchEngines.batchVerifyTargetSites -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.BatchVerifyTargetSites"
```

`CreateSitemap` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateSite
map
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.sitemaps.create - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.CreateSitemap"
```

`CreateTargetSite` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.CreateTarg
etSite
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.targetSites.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
```

`hEngineService.CreateTargetSite"` 

`DeleteSitemap` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteSite
map
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.sitemaps.delete - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.DeleteSitemap"
```

`DeleteTargetSite` 

**Method** : 

- `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DeleteTarg etSite` 

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

   - `discoveryengine.targetSites.delete - ADMIN_WRITE` 

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.DeleteTargetSite"
DisableAdvancedSiteSearch
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.DisableAdv
```

`ancedSiteSearch` 

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.siteSearchEngines.disableAdvancedSiteSearch -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.DisableAdvancedSiteSearch"
EnableAdvancedSiteSearch
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.EnableAdva
ncedSiteSearch
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.siteSearchEngines.enableAdvancedSiteSearch -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.EnableAdvancedSiteSearch"
FetchDomainVerificationStatus
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchDomai
nVerificationStatus
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.siteSearchEngines.fetchDomainVerificationStatus -
ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.FetchDomainVerificationStatus"
```

`FetchSitemaps` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.FetchSitem
aps
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sitemaps.fetch - DATA_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.FetchSitemaps"
```

`GetSiteSearchEngine` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetSiteSea
rchEngine
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.siteSearchEngines.get - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.GetSiteSearchEngine"
```

`GetTargetSite` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetTargetS
ite
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.targetSites.get - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.GetTargetSite"
```

`GetUriPatternDocumentData` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.GetUriPatt
ernDocumentData
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

   - `discoveryengine.siteSearchEngines.getUriPatternDocumentData - ADMIN_READ` 

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.GetUriPatternDocumentData"
```

`ListTargetSites` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.ListTarget
Sites
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.targetSites.list - ADMIN_READ` 

**Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.ListTargetSites"
```

`RecrawlUris` 

**Method** : 

- `google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.RecrawlUri` `s` 

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.siteSearchEngines.recrawlUris - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.RecrawlUris"
```

`SetUriPatternDocumentData` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.SetUriPatt
ernDocumentData
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

   - `discoveryengine.siteSearchEngines.setUriPatternDocumentData - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
UpdateTargetSite
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.SiteSearchEngineService.UpdateTarg
etSite
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.targetSites.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.SiteSearc
hEngineService.UpdateTargetSite"
google.cloud.discoveryengine.v1alpha.UserEventService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.UserEventService` . 

```
ImportUserEvents
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.UserEventService.ImportUserEvents` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.userEvents.import - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEvent
Service.ImportUserEvents"
PurgeUserEvents
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.UserEventService.PurgeUserEvents` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.userEvents.purge - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEvent
Service.PurgeUserEvents"
WriteUserEvent
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.UserEventService.WriteUserEvent` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.userEvents.create - DATA_WRITE
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserEvent
Service.WriteUserEvent"
google.cloud.discoveryengine.v1alpha.UserLicenseService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.UserLicenseService` . 

```
BatchUpdateUserLicenses
```

**Method** : 

- `google.cloud.discoveryengine.v1alpha.UserLicenseService.BatchUpdateUser Licenses` 

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.userStores.batchUpdateUserLicenses - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserLicen
seService.BatchUpdateUserLicenses"
```

`ExportUserLicenses` 

**Method** : 

- `google.cloud.discoveryengine.v1alpha.UserLicenseService.ExportUserLicen ses` 

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.userStores.listUserLicenses - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserLicen
seService.ExportUserLicenses"
google.cloud.discoveryengine.v1alpha.UserStoreService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.UserStoreService` . 

```
UpdateUserStore
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.UserStoreService.UpdateUserStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.userStores.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.UserStore
Service.UpdateUserStore"
google.cloud.discoveryengine.v1alpha.WidgetConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.WidgetConfigService` . 

`GetWidgetConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.WidgetConfigService.GetWidgetConfi
g
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.widgetConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.WidgetCon
figService.GetWidgetConfig"
```

`UpdateWidgetConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.WidgetConfigService.UpdateWidgetCo
nfig
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.widgetConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.WidgetCon
figService.UpdateWidgetConfig"
google.cloud.discoveryengine.v1beta.AclConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.AclConfigService` . 

```
GetAclConfig
```

**Method** : 

`google.cloud.discoveryengine.v1beta.AclConfigService.GetAclConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.aclConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.AclConfigS
ervice.GetAclConfig"
UpdateAclConfig
```

**Method** : 

`google.cloud.discoveryengine.v1beta.AclConfigService.UpdateAclConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.aclConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.AclConfigS
ervice.UpdateAclConfig"
google.cloud.discoveryengine.v1beta.AssistantService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.AssistantService` . 

```
CreateAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1beta.AssistantService.CreateAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.assistants.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantS
ervice.CreateAssistant"
DeleteAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1beta.AssistantService.DeleteAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.assistants.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantS
```

`ervice.DeleteAssistant"` 

```
GetAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1beta.AssistantService.GetAssistant` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.assistants.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantS
ervice.GetAssistant"
```

`ListAssistants` 

**Method** : 

`google.cloud.discoveryengine.v1beta.AssistantService.ListAssistants` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.assistants.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantS
ervice.ListAssistants"
StreamAssist
```

**Method** : 

`google.cloud.discoveryengine.v1beta.AssistantService.StreamAssist` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.assistants.assist - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Streaming RPC** 

(/logging/docs/audit/understanding-audit-logs#streaming) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantS
ervice.StreamAssist"
UpdateAssistant
```

**Method** : 

`google.cloud.discoveryengine.v1beta.AssistantService.UpdateAssistant` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.assistants.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.AssistantS
ervice.UpdateAssistant"
google.cloud.discoveryengine.v1beta.CmekConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.CmekConfigService` . 

```
DeleteCmekConfig
```

**Method** : 

`google.cloud.discoveryengine.v1beta.CmekConfigService.DeleteCmekConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.cmekConfigs.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfig
Service.DeleteCmekConfig"
GetCmekConfig
```

**Method** : 

`google.cloud.discoveryengine.v1beta.CmekConfigService.GetCmekConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.cmekConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfig
Service.GetCmekConfig"
ListCmekConfigs
```

**Method** : 

`google.cloud.discoveryengine.v1beta.CmekConfigService.ListCmekConfigs` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.cmekConfigs.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfig
Service.ListCmekConfigs"
UpdateCmekConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.CmekConfigService.UpdateCmekConfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.cmekConfigs.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.CmekConfig
Service.UpdateCmekConfig"
google.cloud.discoveryengine.v1beta.CompletionService
```
