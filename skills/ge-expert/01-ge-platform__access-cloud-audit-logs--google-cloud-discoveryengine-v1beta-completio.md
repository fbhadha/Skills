# Gemini Enterprise: platform, security, agents, cost, monitoring / Access Cloud Audit Logs: API interface audit logs / google.cloud.discoveryengine.v1beta.CompletionService to API interface audit logs / google.cloud.discoveryengine.v1beta.ServingConfigService
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 907-944, extracted 2026-10-18

## Access Cloud Audit Logs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.CompletionService` . 

`AdvancedCompleteQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.CompletionService.AdvancedCompleteQ
uery
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.completionConfigs.completeQuery - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Completion
Service.AdvancedCompleteQuery"
```

`CompleteQuery` 

**Method** : 

`google.cloud.discoveryengine.v1beta.CompletionService.CompleteQuery` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.dataStores.completeQuery - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Completion
Service.CompleteQuery"
```

`ImportCompletionSuggestions` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.CompletionService.ImportCompletionS
uggestions
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.completionSuggestions.import - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Completion
Service.ImportCompletionSuggestions"
```

`ImportSuggestionDenyListEntries` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.CompletionService.ImportSuggestionD
enyListEntries
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.suggestionDenyListEntries.import - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Completion
Service.ImportSuggestionDenyListEntries"
PurgeCompletionSuggestions
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.CompletionService.PurgeCompletionSu
ggestions
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.completionSuggestions.purge - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Completion
Service.PurgeCompletionSuggestions"
```

`PurgeSuggestionDenyListEntries` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.CompletionService.PurgeSuggestionDe
nyListEntries
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Completion
Service.PurgeSuggestionDenyListEntries"
RemoveSuggestion
```

**Method** : 

`google.cloud.discoveryengine.v1beta.CompletionService.RemoveSuggestion` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.completionConfigs.removeSuggestion - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Completion
Service.RemoveSuggestion"
google.cloud.discoveryengine.v1beta.ControlService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.ControlService` . 

```
CreateControl
```

**Method** : 

`google.cloud.discoveryengine.v1beta.ControlService.CreateControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.controls.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlSer
vice.CreateControl"
DeleteControl
```

**Method** : 

`google.cloud.discoveryengine.v1beta.ControlService.DeleteControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.controls.delete - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlSer
vice.DeleteControl"
GetControl
```

**Method** : `google.cloud.discoveryengine.v1beta.ControlService.GetControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.controls.get - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlSer
vice.GetControl"
ListControls
```

**Method** : 

`google.cloud.discoveryengine.v1beta.ControlService.ListControls` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.controls.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlSer
vice.ListControls"
```

`UpdateControl` 

**Method** : 

`google.cloud.discoveryengine.v1beta.ControlService.UpdateControl` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.controls.update - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ControlSer
vice.UpdateControl"
google.cloud.discoveryengine.v1beta.ConversationalSearch
Service
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.ConversationalSearchService` . 

`AnswerQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.AnswerQ
uery
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.answer - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.AnswerQuery"
```

`ConverseConversation` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.Convers
eConversation
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.conversations.converse - DATA_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.ConverseConversation"
CreateConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateC
onversation
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.conversations.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.CreateConversation"
CreateSession
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.CreateS
ession
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.CreateSession"
DeleteConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteC
onversation
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.conversations.delete - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.DeleteConversation"
```

`DeleteSession` 

**Method** : 

- `google.cloud.discoveryengine.v1beta.ConversationalSearchService.DeleteS ession` 

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.sessions.delete - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.DeleteSession"
```

`GetAnswer` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetAnsw
er
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.answers.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.GetAnswer"
GetConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetConv
ersation
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.conversations.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.GetConversation"
GetSession
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.GetSess
ion
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.GetSession"
ListConversations
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListCon
versations
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.conversations.list - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.ListConversations"
```

`ListSessions` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.ListSes
sions
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.ListSessions"
```

`StreamAnswerQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.StreamA
nswerQuery
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.servingConfigs.answer - DATA_READ` **Method is a long-running or streaming operation** : **Streaming RPC** (/logging/docs/audit/understanding-audit-logs#streaming) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.StreamAnswerQuery"
UpdateConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.ConversationalSearchService.UpdateC
onversation
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.conversations.update - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Conversati
onalSearchService.UpdateConversation"
```

`google.cloud.discoveryengine.v1beta.DataStoreService` 

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.DataStoreService` . 

```
CreateDataStore
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DataStoreService.CreateDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataStores.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreS
ervice.CreateDataStore"
DeleteDataStore
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DataStoreService.DeleteDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataStores.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreS
ervice.DeleteDataStore"
GetDataStore
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DataStoreService.GetDataStore` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataStores.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreS
ervice.GetDataStore"
ListDataStores
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DataStoreService.ListDataStores` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.dataStores.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreS
ervice.ListDataStores"
UpdateDataStore
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DataStoreService.UpdateDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.dataStores.update - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DataStoreS
ervice.UpdateDataStore"
google.cloud.discoveryengine.v1beta.DocumentService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.DocumentService` . 

```
BatchGetDocumentsMetadata
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.DocumentService.BatchGetDocumentsMe
tadata
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ` 

- **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentSe
rvice.BatchGetDocumentsMetadata"
CreateDocument
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DocumentService.CreateDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.documents.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentSe
rvice.CreateDocument"
DeleteDocument
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DocumentService.DeleteDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.documents.delete - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentSe
rvice.DeleteDocument"
GetDocument
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.DocumentService.GetDocument
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentSe
rvice.GetDocument"
ImportDocuments
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DocumentService.ImportDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.import - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentSe
rvice.ImportDocuments"
ListDocuments
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.documents.list - DATA_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentSe
rvice.ListDocuments"
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DocumentService.PurgeDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.documents.purge - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentSe
rvice.PurgeDocuments"
UpdateDocument
```

**Method** : 

`google.cloud.discoveryengine.v1beta.DocumentService.UpdateDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.update - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.DocumentSe
rvice.UpdateDocument"
```

`google.cloud.discoveryengine.v1beta.EngineService` The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.EngineService` . 

```
CreateEngine
```

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.CreateEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

**Permissions** : 

```
discoveryengine.engines.create - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.CreateEngine"
```

`DeleteEngine` 

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.DeleteEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.engines.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.DeleteEngine"
```

`GetEngine` 

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.GetEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.engines.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.GetEngine"
```

`GetIamPolicy` 

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.GetIamPolicy` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.engines.getIamPolicy - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.GetIamPolicy"
ListEngines
```

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.ListEngines` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.engines.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.ListEngines"
```

`PauseEngine` 

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.PauseEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.engines.pause - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.PauseEngine"
```

`ResumeEngine` 

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.ResumeEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.engines.resume - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.ResumeEngine"
```

`SetIamPolicy` 

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.SetIamPolicy` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.engines.setIamPolicy - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.SetIamPolicy"
```

`TuneEngine` 

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.TuneEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.engines.tune - DATA_WRITE
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.TuneEngine"
```

**Method** : `google.cloud.discoveryengine.v1beta.EngineService.UpdateEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.engines.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.EngineServ
ice.UpdateEngine"
google.cloud.discoveryengine.v1beta.EvaluationService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.EvaluationService` . 

```
CreateEvaluation
```

**Method** : 

`google.cloud.discoveryengine.v1beta.EvaluationService.CreateEvaluation` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.evaluations.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Evaluation
Service.CreateEvaluation"
GetEvaluation
```

**Method** : 

`google.cloud.discoveryengine.v1beta.EvaluationService.GetEvaluation` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.evaluations.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Evaluation
Service.GetEvaluation"
ListEvaluationResults
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluationRes
ults
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.evaluations.get - DATA_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Evaluation
Service.ListEvaluationResults"
```

`ListEvaluations` 

**Method** : 

`google.cloud.discoveryengine.v1beta.EvaluationService.ListEvaluations` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.evaluations.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Evaluation
Service.ListEvaluations"
google.cloud.discoveryengine.v1beta.GroundedGenerationService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.GroundedGenerationService` . 

`CheckGrounding` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.GroundedGenerationService.CheckGrou
nding
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

- `discoveryengine.groundingConfigs.check - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.GroundedGe
nerationService.CheckGrounding"
google.cloud.discoveryengine.v1beta.IdentityMappingStore
Service
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.IdentityMappingStoreService` . 

`CreateIdentityMappingStore` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.CreateI
dentityMappingStore
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.identityMappingStores.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMa
ppingStoreService.CreateIdentityMappingStore"
DeleteIdentityMappingStore
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.DeleteI
dentityMappingStore
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.identityMappingStores.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMa
ppingStoreService.DeleteIdentityMappingStore"
ImportIdentityMappings
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ImportI
dentityMappings
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.identityMappingStores.importIdentityMappings -
DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMa
ppingStoreService.ImportIdentityMappings"
ListIdentityMappings
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.ListIde
ntityMappings
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.identityMappingStores.listIdentityMappings -
DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMa
ppingStoreService.ListIdentityMappings"
PurgeIdentityMappings
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.IdentityMappingStoreService.PurgeId
entityMappings
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.identityMappingStores.purgeIdentityMappings -
DATA_WRITE
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.IdentityMa
ppingStoreService.PurgeIdentityMappings"
google.cloud.discoveryengine.v1beta.LicenseConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.LicenseConfigService` . 

```
CreateLicenseConfig
```

**Method** : 

- `google.cloud.discoveryengine.v1beta.LicenseConfigService.CreateLicenseC onfig` 

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.licenseConfigs.create - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseCon
figService.CreateLicenseConfig"
DistributeLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.LicenseConfigService.DistributeLice
nseConfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.billingAccountLicenseConfigs.distribute -
ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseCon
figService.DistributeLicenseConfig"
```

`GetLicenseConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.LicenseConfigService.GetLicenseConf
ig
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.licenseConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseCon
figService.GetLicenseConfig"
RetractLicenseConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.LicenseConfigService.RetractLicense
Config
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseCon
figService.RetractLicenseConfig"
```

`UpdateLicenseConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.LicenseConfigService.UpdateLicenseC
onfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.licenseConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.LicenseCon
figService.UpdateLicenseConfig"
google.cloud.discoveryengine.v1beta.ProjectService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.ProjectService` . 

```
ProvisionProject
```

**Method** : 

`google.cloud.discoveryengine.v1beta.ProjectService.ProvisionProject` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.projects.provision - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ProjectSer
vice.ProvisionProject"
google.cloud.discoveryengine.v1beta.RankService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.RankService` . 

```
Rank
```

**Method** : `google.cloud.discoveryengine.v1beta.RankService.Rank` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.rankingConfigs.rank - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.RankServic
e.Rank"
google.cloud.discoveryengine.v1beta.RecommendationService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.RecommendationService` . 

`Recommend` 

**Method** : 

`google.cloud.discoveryengine.v1beta.RecommendationService.Recommend` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.recommend - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.Recommenda
tionService.Recommend"
google.cloud.discoveryengine.v1beta.SampleQueryService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SampleQueryService` . 

`CreateSampleQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SampleQueryService.CreateSampleQuer
y
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQueries.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
yService.CreateSampleQuery"
```

`DeleteSampleQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SampleQueryService.DeleteSampleQuer
y
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.sampleQueries.delete - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
yService.DeleteSampleQuery"
```

`GetSampleQuery` 

**Method** : 

`google.cloud.discoveryengine.v1beta.SampleQueryService.GetSampleQuery` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

   - `discoveryengine.sampleQueries.get - DATA_READ` 

- **Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
yService.GetSampleQuery"
```

`ImportSampleQueries` 

**Method** : 

- `google.cloud.discoveryengine.v1beta.SampleQueryService.ImportSampleQuer ies` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.sampleQueries.import - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
yService.ImportSampleQueries"
```

`ListSampleQueries` 

**Method** : 

- `google.cloud.discoveryengine.v1beta.SampleQueryService.ListSampleQuerie` `s` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQueries.list - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
yService.ListSampleQueries"
```

`UpdateSampleQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SampleQueryService.UpdateSampleQuer
y
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQueries.update - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
yService.UpdateSampleQuery"
google.cloud.discoveryengine.v1beta.SampleQuerySetService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SampleQuerySetService` . 

`CreateSampleQuerySet` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SampleQuerySetService.CreateSampleQ
uerySet
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQuerySets.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
ySetService.CreateSampleQuerySet"
DeleteSampleQuerySet
```

**Method** : 

```
google.cloud.discoveryengine.v1beta.SampleQuerySetService.DeleteSampleQ
uerySet
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQuerySets.delete - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
ySetService.DeleteSampleQuerySet"
GetSampleQuerySet
```

**Method** : 

- `google.cloud.discoveryengine.v1beta.SampleQuerySetService.GetSampleQuer ySet` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.sampleQuerySets.get - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
ySetService.GetSampleQuerySet"
```

`ListSampleQuerySets` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SampleQuerySetService.ListSampleQue
rySets
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQuerySets.list - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
ySetService.ListSampleQuerySets"
```

`UpdateSampleQuerySet` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SampleQuerySetService.UpdateSampleQ
uerySet
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.sampleQuerySets.update - DATA_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SampleQuer
ySetService.UpdateSampleQuerySet"
google.cloud.discoveryengine.v1beta.SchemaService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SchemaService` . 

```
CreateSchema
```

- **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.CreateSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.schemas.create - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaServ
ice.CreateSchema"
DeleteSchema
```

- **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.DeleteSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.schemas.delete - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaServ
```

`ice.DeleteSchema"` 

`GetSchema` 

- **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.GetSchema` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.schemas.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaServ
ice.GetSchema"
```

`ListSchemas` 

- **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.ListSchemas` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.schemas.list - ADMIN_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaServ
ice.ListSchemas"
```

`UpdateSchema` 

- **Method** : `google.cloud.discoveryengine.v1beta.SchemaService.UpdateSchema` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.schemas.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SchemaServ
ice.UpdateSchema"
google.cloud.discoveryengine.v1beta.SearchService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SearchService` . 

`Search` 

**Method** : `google.cloud.discoveryengine.v1beta.SearchService.Search` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.servingConfigs.search - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchServ
ice.Search"
google.cloud.discoveryengine.v1beta.SearchTuningService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.SearchTuningService` . 

`ListCustomModels` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SearchTuningService.ListCustomModel
s
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.dataStores.listCustomModels - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchTuni
ngService.ListCustomModels"
```

`TrainCustomModel` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.SearchTuningService.TrainCustomMode
l
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataStores.trainCustomModel - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.SearchTuni
ngService.TrainCustomModel"
google.cloud.discoveryengine.v1beta.ServingConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1beta.ServingConfigService` . 

`CreateServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ServingConfigService.CreateServingC
onfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.servingConfigs.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingCon
figService.CreateServingConfig"
```

`DeleteServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ServingConfigService.DeleteServingC
onfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.servingConfigs.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingCon
figService.DeleteServingConfig"
```

`GetServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ServingConfigService.GetServingConf
ig
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.servingConfigs.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingCon
figService.GetServingConfig"
```

`ListServingConfigs` 

**Method** : 

- `google.cloud.discoveryengine.v1beta.ServingConfigService.ListServingCon figs` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingCon
figService.ListServingConfigs"
```

`UpdateServingConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1beta.ServingConfigService.UpdateServingC
onfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.servingConfigs.update - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1beta.ServingCon
figService.UpdateServingConfig"
google.cloud.discoveryengine.v1beta.SessionService
```
