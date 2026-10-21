# Gemini Enterprise: platform, security, agents, cost, monitoring / Access Cloud Audit Logs: API interface audit logs / google.cloud.discoveryengine.v1alpha.AuthorizationService to API interface audit logs / google.cloud.discoveryengine.v1alpha.EstimateBillingService
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 830-869, extracted 2026-10-18

## Access Cloud Audit Logs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.AuthorizationService` . 

`CreateAuthorization` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AuthorizationService.CreateAuthori
zation
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

`discoveryengine.authorizations.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Authoriza
tionService.CreateAuthorization"
```

`DeleteAuthorization` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AuthorizationService.DeleteAuthori
zation
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.authorizations.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Authoriza
tionService.DeleteAuthorization"
```

`GetAuthorization` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AuthorizationService.GetAuthorizat
ion
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.authorizations.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Authoriza
tionService.GetAuthorization"
```

`ListAuthorizations` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AuthorizationService.ListAuthoriza
tions
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.authorizations.list - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Authoriza
tionService.ListAuthorizations"
```

`UpdateAuthorization` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.AuthorizationService.UpdateAuthori
zation
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.authorizations.update - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Authoriza
tionService.UpdateAuthorization"
google.cloud.discoveryengine.v1alpha.BranchService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.BranchService` . 

`GetBranch` 

**Method** : `google.cloud.discoveryengine.v1alpha.BranchService.GetBranch` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.branches.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.BranchSer
vice.GetBranch"
```

`ListBranches` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.BranchService.ListBranches` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.branches.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.BranchSer
vice.ListBranches"
google.cloud.discoveryengine.v1alpha.CannedQueryService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.CannedQueryService` . 

`CreateCannedQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CannedQueryService.CreateCannedQue
ry
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.cannedQueries.create - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQue
ryService.CreateCannedQuery"
```

`DeleteCannedQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CannedQueryService.DeleteCannedQue
ry
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.cannedQueries.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQue
ryService.DeleteCannedQuery"
```

`GetCannedQuery` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.CannedQueryService.GetCannedQuery` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.cannedQueries.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQue
ryService.GetCannedQuery"
```

`ListCannedQueries` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CannedQueryService.ListCannedQueri
es
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.cannedQueries.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQue
ryService.ListCannedQueries"
```

`UpdateCannedQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CannedQueryService.UpdateCannedQue
ry
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.cannedQueries.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQue
ryService.UpdateCannedQuery"
google.cloud.discoveryengine.v1alpha.ChunkService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ChunkService` . 

`GetChunk` 

**Method** : `google.cloud.discoveryengine.v1alpha.ChunkService.GetChunk` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.chunks.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ChunkServ
ice.GetChunk"
```

`ListChunks` 

**Method** : `google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.chunks.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ChunkServ
ice.ListChunks"
google.cloud.discoveryengine.v1alpha.CmekConfigService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.CmekConfigService` . 

`DeleteCmekConfig` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.CmekConfigService.DeleteCmekConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.cmekConfigs.delete - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfi
gService.DeleteCmekConfig"
GetCmekConfig
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.CmekConfigService.GetCmekConfig` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.cmekConfigs.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfi
gService.GetCmekConfig"
ListCmekConfigs
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.CmekConfigService.ListCmekConfigs` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.cmekConfigs.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfi
```

`gService.ListCmekConfigs"` 

```
UpdateCmekConfig
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.CmekConfigService.UpdateCmekConfig` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.cmekConfigs.update - ADMIN_WRITE
```

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfi
gService.UpdateCmekConfig"
google.cloud.discoveryengine.v1alpha.CollectionService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.CollectionService` . 

```
DeleteCollection
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.CollectionService.DeleteCollection` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.collections.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Collectio
nService.DeleteCollection"
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.CollectionService.GetCollection` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.collections.get - ADMIN_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Collectio
nService.GetCollection"
GetIamPolicy
```

**Method** : 

- `google.cloud.discoveryengine.v1alpha.CollectionService.GetIamPolicy` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.collections.getIamPolicy - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Collectio
nService.GetIamPolicy"
ListCollections
```

**Method** : 

- `google.cloud.discoveryengine.v1alpha.CollectionService.ListCollections` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.collections.list - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Collectio
nService.ListCollections"
SetIamPolicy
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.CollectionService.SetIamPolicy` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.collections.setIamPolicy - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Collectio
nService.SetIamPolicy"
UpdateCollection
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.CollectionService.UpdateCollection` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.collections.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Collectio
nService.UpdateCollection"
google.cloud.discoveryengine.v1alpha.CompletionService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.CompletionService` . 

`AdvancedCompleteQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CompletionService.AdvancedComplete
Query
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.completionConfigs.completeQuery - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Completio
nService.AdvancedCompleteQuery"
```

`CompleteExternalIdentities` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CompletionService.CompleteExternal
Identities
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.locations.completeExternalIdentities - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Completio
nService.CompleteExternalIdentities"
```

`CompleteQuery` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.CompletionService.CompleteQuery` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.dataStores.completeQuery - DATA_READ` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Completio
nService.CompleteQuery"
```

`ImportCompletionSuggestions` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CompletionService.ImportCompletion
Suggestions
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.completionSuggestions.import - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Completio
nService.ImportCompletionSuggestions"
```

`ImportSuggestionDenyListEntries` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CompletionService.ImportSuggestion
DenyListEntries
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.suggestionDenyListEntries.import - DATA_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Completio
nService.ImportSuggestionDenyListEntries"
PurgeCompletionSuggestions
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.CompletionService.PurgeCompletionS
uggestions
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.completionSuggestions.purge - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Completio
nService.PurgeCompletionSuggestions"
```

`PurgeSuggestionDenyListEntries` 

**Method** : 

- `google.cloud.discoveryengine.v1alpha.CompletionService.PurgeSuggestionD enyListEntries` 

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE` 

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Completio
nService.PurgeSuggestionDenyListEntries"
RemoveSuggestion
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.CompletionService.RemoveSuggestion` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.completionConfigs.removeSuggestion - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Completio
nService.RemoveSuggestion"
google.cloud.discoveryengine.v1alpha.ControlService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ControlService` . 

```
CreateControl
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.ControlService.CreateControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.controls.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlSe
rvice.CreateControl"
DeleteControl
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.ControlService.DeleteControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.controls.delete - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlSe
rvice.DeleteControl"
GetControl
```

**Method** : `google.cloud.discoveryengine.v1alpha.ControlService.GetControl` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.controls.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlSe
rvice.GetControl"
```

`ListControls` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.ControlService.ListControls` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.controls.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlSe
rvice.ListControls"
```

`UpdateControl` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.ControlService.UpdateControl` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.controls.update - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlSe
rvice.UpdateControl"
google.cloud.discoveryengine.v1alpha.ConversationalSearch
Service
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.ConversationalSearchService` . 

`AnswerQuery` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.Answer
Query
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.servingConfigs.answer - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.AnswerQuery"
```

`ConverseConversation` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.Conver
seConversation
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.conversations.converse - DATA_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.ConverseConversation"
CreateConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.Create
Conversation
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.conversations.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.CreateConversation"
CreateSession
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.Create
Session
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.create - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.CreateSession"
DeleteConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.Delete
Conversation
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.conversations.delete - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.DeleteConversation"
```

`DeleteSession` 

**Method** : 

- `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.Delete Session` 

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

- `discoveryengine.sessions.delete - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.DeleteSession"
```

`GetAnswer` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetAns
wer
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.answers.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.GetAnswer"
GetConversation
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetCon
versation
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.conversations.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.GetConversation"
```

`GetSession` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetSes
sion
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.GetSession"
```

`ListConversations` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListCo
nversations
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.conversations.list - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.ListConversations"
ListSessions
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListSe
ssions
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.sessions.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.ListSessions"
StreamAnswerQuery
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.Stream
AnswerQuery
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.servingConfigs.answer - DATA_READ` **Method is a long-running or streaming operation** : **Streaming RPC** (/logging/docs/audit/understanding-audit-logs#streaming) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.StreamAnswerQuery"
```

`UpdateConversation` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.ConversationalSearchService.Update
Conversation
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.conversations.update - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.Conversat
ionalSearchService.UpdateConversation"
google.cloud.discoveryengine.v1alpha.DataConnectorService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.DataConnectorService` . 

`AcquireAccessToken` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataConnectorService.AcquireAccess
Token
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.dataConnectors.acquireAccessToken - DATA_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConne
ctorService.AcquireAccessToken"
CheckRefreshToken
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataConnectorService.CheckRefreshT
oken
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataConnectors.checkRefreshToken - DATA_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConne
ctorService.CheckRefreshToken"
GetConnectorSecret
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataConnectorService.GetConnectorS
ecret
```

**Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataConnectors.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConne
ctorService.GetConnectorSecret"
GetDataConnector
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataConnectorService.GetDataConnec
tor
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.dataConnectors.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConne
ctorService.GetDataConnector"
```

`ListConnectorRuns` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataConnectorService.ListConnector
Runs
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.connectorRuns.list - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConne
ctorService.ListConnectorRuns"
```

`SetUpDataConnector` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataConnectorService.SetUpDataConn
ector
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.locations.setUpDataConnector - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConne
ctorService.SetUpDataConnector"
UpdateDataConnector
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataConnectorService.UpdateDataCon
nector
```

**Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataConnectors.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConne
ctorService.UpdateDataConnector"
google.cloud.discoveryengine.v1alpha.DataStoreService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.DataStoreService` . 

```
AddPatientFilter
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.DataStoreService.AddPatientFilter` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataStores.addPatientFilters - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
```

`Service.AddPatientFilter"` 

`CreateDataStore` 

**Method** : 

- `google.cloud.discoveryengine.v1alpha.DataStoreService.CreateDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataStores.create - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.CreateDataStore"
```

`DeleteDataStore` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.dataStores.delete - ADMIN_WRITE
```

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.DeleteDataStore"
```

`DeletePatientFilters` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataStoreService.DeletePatientFilt
ers
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataStores.deletePatientFilters - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.DeletePatientFilters"
```

`GetCompletionConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataStoreService.GetCompletionConf
ig
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.completionConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.GetCompletionConfig"
```

`GetDataStore` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStore` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.dataStores.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.GetDataStore"
GetDocumentProcessingConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocumentProces
singConfig
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.documentProcessingConfigs.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.GetDocumentProcessingConfig"
GetIamPolicy
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.DataStoreService.GetIamPolicy` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.dataStores.getIamPolicy - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.GetIamPolicy"
ListDataStores
```

**Method** : 

- `google.cloud.discoveryengine.v1alpha.DataStoreService.ListDataStores` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.dataStores.list - ADMIN_READ` 

- **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.ListDataStores"
```

`RemovePatientFilter` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataStoreService.RemovePatientFilt
er
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.dataStores.deletePatientFilters - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.RemovePatientFilter"
```

`ReplacePatientFilter` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataStoreService.ReplacePatientFil
ter
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataStores.updatePatientFilters - ADMIN_WRITE` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.ReplacePatientFilter"
```

`SetIamPolicy` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.DataStoreService.SetIamPolicy` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataStores.setIamPolicy - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.SetIamPolicy"
```

`UpdateCompletionConfig` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateCompletionC
onfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.completionConfigs.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.UpdateCompletionConfig"
```

`UpdateDataStore` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDataStore` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.dataStores.update - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.UpdateDataStore"
UpdateDocumentProcessingConfig
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDocumentPro
cessingConfig
```

- **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

- `discoveryengine.documentProcessingConfigs.update - ADMIN_WRITE` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStore
Service.UpdateDocumentProcessingConfig"
google.cloud.discoveryengine.v1alpha.DocumentService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.DocumentService` . 

```
BatchGetDocumentsMetadata
```

**Method** : 

```
google.cloud.discoveryengine.v1alpha.DocumentService.BatchGetDocumentsM
etadata
```

- **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

- `discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ` 

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.BatchGetDocumentsMetadata"
CreateDocument
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.documents.create - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.CreateDocument"
DeleteDocument
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.DocumentService.DeleteDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.documents.delete - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.DeleteDocument"
GetDocument
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.DocumentService.GetDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.get - DATA_READ
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.GetDocument"
GetProcessedDocument
```

**Method** : 

- `google.cloud.discoveryengine.v1alpha.DocumentService.GetProcessedDocume` `nt` 

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.documents.get - DATA_READ
```

- **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.GetProcessedDocument"
```

`ImportDocuments` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.DocumentService.ImportDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.import - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.ImportDocuments"
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.DocumentService.ListDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.documents.list - DATA_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.ListDocuments"
PurgeDocuments
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.DocumentService.PurgeDocuments` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.documents.purge - DATA_WRITE
```

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.PurgeDocuments"
UpdateDocument
```

**Method** : 

- `google.cloud.discoveryengine.v1alpha.DocumentService.UpdateDocument` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

```
discoveryengine.documents.update - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentS
ervice.UpdateDocument"
google.cloud.discoveryengine.v1alpha.EngineService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.EngineService` . 

```
CreateEngine
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.EngineService.CreateEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

```
discoveryengine.engines.create - ADMIN_WRITE
```

- **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.CreateEngine"
DeleteEngine
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.EngineService.DeleteEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.engines.delete - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.DeleteEngine"
```

`GetEngine` 

**Method** : `google.cloud.discoveryengine.v1alpha.EngineService.GetEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.engines.get - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.GetEngine"
```

`GetIamPolicy` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.EngineService.GetIamPolicy` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.engines.getIamPolicy - ADMIN_READ` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.GetIamPolicy"
GetWorkspaceSettings
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.EngineService.GetWorkspaceSettings` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.engines.get - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.GetWorkspaceSettings"
ListEngines
```

**Method** : `google.cloud.discoveryengine.v1alpha.EngineService.ListEngines` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.engines.list - ADMIN_READ
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.ListEngines"
PauseEngine
```

**Method** : `google.cloud.discoveryengine.v1alpha.EngineService.PauseEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

`discoveryengine.engines.pause - DATA_WRITE` **Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.PauseEngine"
ResumeEngine
```

**Method** : 

`google.cloud.discoveryengine.v1alpha.EngineService.ResumeEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) 

**Permissions** : 

```
discoveryengine.engines.resume - DATA_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.ResumeEngine"
```

`SetIamPolicy` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.EngineService.SetIamPolicy` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) **Permissions** : 

`discoveryengine.engines.setIamPolicy - ADMIN_WRITE` **Method is a long-running or streaming operation** : No. 

- **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.SetIamPolicy"
```

`TuneEngine` 

**Method** : `google.cloud.discoveryengine.v1alpha.EngineService.TuneEngine` **Audit log type** : Data access (/logging/docs/audit#data-access) **Permissions** : 

```
discoveryengine.engines.tune - DATA_WRITE
```

**Method is a long-running or streaming operation** : **Long-running** 

**operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.TuneEngine"
```

`UpdateEngine` 

**Method** : 

`google.cloud.discoveryengine.v1alpha.EngineService.UpdateEngine` **Audit log type** : Admin activity (/logging/docs/audit#admin-activity) 

- **Permissions** : 

```
discoveryengine.engines.update - ADMIN_WRITE
```

**Method is a long-running or streaming operation** : No. **Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineSer
vice.UpdateEngine"
google.cloud.discoveryengine.v1alpha.EstimateBillingService
```

The following audit logs are associated with methods belonging to `google.cloud.discoveryengine.v1alpha.EstimateBillingService` . 

`EstimateDataSize` 

**Method** : 

```
google.cloud.discoveryengine.v1alpha.EstimateBillingService.EstimateDat
aSize
```

**Audit log type** : Data access (/logging/docs/audit#data-access) 

- **Permissions** : 

`discoveryengine.locations.estimateDataSize - ADMIN_READ` **Method is a long-running or streaming operation** : **Long-running operation** (/logging/docs/audit/understanding-audit-logs#lro) 

**Filter for this method** : 

```
protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EstimateB
illingService.EstimateDataSize"
google.cloud.discoveryengine.v1alpha.EvaluationService
```
