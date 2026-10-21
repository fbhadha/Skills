# Gemini Enterprise Docs (Monitor usage) / Access Gemini Enterprise Cloud Audit Logs (part 3 of 5: API interface audit logs: google.cloud.discoveryengine.v1alpha.CannedQueryService to google.cloud.discoveryengine.v1alpha.RequirementService)
Source: https://docs.cloud.google.com/gemini/enterprise/docs/audit-logging, page last updated 2026-10-14, extracted 2026-10-19

## API interface audit logs

### `google.cloud.discoveryengine.v1alpha.CannedQueryService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.CannedQueryService`.

#### `CreateCannedQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.CannedQueryService.CreateCannedQuery`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cannedQueries.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.CreateCannedQuery"`

#### `DeleteCannedQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.CannedQueryService.DeleteCannedQuery`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cannedQueries.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.DeleteCannedQuery"`

#### `GetCannedQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.CannedQueryService.GetCannedQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.cannedQueries.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.GetCannedQuery"`

#### `ListCannedQueries`

- **Method**: `google.cloud.discoveryengine.v1alpha.CannedQueryService.ListCannedQueries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.cannedQueries.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.ListCannedQueries"`

#### `UpdateCannedQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.CannedQueryService.UpdateCannedQuery`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cannedQueries.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CannedQueryService.UpdateCannedQuery"`

### `google.cloud.discoveryengine.v1alpha.ChunkService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.ChunkService`.

#### `GetChunk`

- **Method**: `google.cloud.discoveryengine.v1alpha.ChunkService.GetChunk`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.chunks.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ChunkService.GetChunk"`

#### `ListChunks`

- **Method**: `google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.chunks.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks"`

### `google.cloud.discoveryengine.v1alpha.CmekConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.CmekConfigService`.

#### `DeleteCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.CmekConfigService.DeleteCmekConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cmekConfigs.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfigService.DeleteCmekConfig"`

#### `GetCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.CmekConfigService.GetCmekConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.cmekConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfigService.GetCmekConfig"`

#### `ListCmekConfigs`

- **Method**: `google.cloud.discoveryengine.v1alpha.CmekConfigService.ListCmekConfigs`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.cmekConfigs.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfigService.ListCmekConfigs"`

#### `UpdateCmekConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.CmekConfigService.UpdateCmekConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.cmekConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CmekConfigService.UpdateCmekConfig"`

### `google.cloud.discoveryengine.v1alpha.CollectionService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.CollectionService`.

#### `DeleteCollection`

- **Method**: `google.cloud.discoveryengine.v1alpha.CollectionService.DeleteCollection`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.collections.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.DeleteCollection"`

#### `GetCollection`

- **Method**: `google.cloud.discoveryengine.v1alpha.CollectionService.GetCollection`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.collections.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.GetCollection"`

#### `GetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1alpha.CollectionService.GetIamPolicy`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.collections.getIamPolicy - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.GetIamPolicy"`

#### `ListCollections`

- **Method**: `google.cloud.discoveryengine.v1alpha.CollectionService.ListCollections`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.collections.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.ListCollections"`

#### `SetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1alpha.CollectionService.SetIamPolicy`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.collections.setIamPolicy - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.SetIamPolicy"`

#### `UpdateCollection`

- **Method**: `google.cloud.discoveryengine.v1alpha.CollectionService.UpdateCollection`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.collections.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CollectionService.UpdateCollection"`

### `google.cloud.discoveryengine.v1alpha.CompletionService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.CompletionService`.

#### `AdvancedCompleteQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.CompletionService.AdvancedCompleteQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionConfigs.completeQuery - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.AdvancedCompleteQuery"`

#### `CompleteExternalIdentities`

- **Method**: `google.cloud.discoveryengine.v1alpha.CompletionService.CompleteExternalIdentities`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.locations.completeExternalIdentities - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.CompleteExternalIdentities"`

#### `CompleteQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.CompletionService.CompleteQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.completeQuery - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.CompleteQuery"`

#### `ImportCompletionSuggestions`

- **Method**: `google.cloud.discoveryengine.v1alpha.CompletionService.ImportCompletionSuggestions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionSuggestions.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.ImportCompletionSuggestions"`

#### `ImportSuggestionDenyListEntries`

- **Method**: `google.cloud.discoveryengine.v1alpha.CompletionService.ImportSuggestionDenyListEntries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.suggestionDenyListEntries.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.ImportSuggestionDenyListEntries"`

#### `PurgeCompletionSuggestions`

- **Method**: `google.cloud.discoveryengine.v1alpha.CompletionService.PurgeCompletionSuggestions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionSuggestions.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.PurgeCompletionSuggestions"`

#### `PurgeSuggestionDenyListEntries`

- **Method**: `google.cloud.discoveryengine.v1alpha.CompletionService.PurgeSuggestionDenyListEntries`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.suggestionDenyListEntries.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.PurgeSuggestionDenyListEntries"`

#### `RemoveSuggestion`

- **Method**: `google.cloud.discoveryengine.v1alpha.CompletionService.RemoveSuggestion`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionConfigs.removeSuggestion - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.CompletionService.RemoveSuggestion"`

### `google.cloud.discoveryengine.v1alpha.ControlService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.ControlService`.

#### `CreateControl`

- **Method**: `google.cloud.discoveryengine.v1alpha.ControlService.CreateControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.CreateControl"`

#### `DeleteControl`

- **Method**: `google.cloud.discoveryengine.v1alpha.ControlService.DeleteControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.DeleteControl"`

#### `GetControl`

- **Method**: `google.cloud.discoveryengine.v1alpha.ControlService.GetControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.GetControl"`

#### `ListControls`

- **Method**: `google.cloud.discoveryengine.v1alpha.ControlService.ListControls`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.ListControls"`

#### `UpdateControl`

- **Method**: `google.cloud.discoveryengine.v1alpha.ControlService.UpdateControl`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.controls.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ControlService.UpdateControl"`

### `google.cloud.discoveryengine.v1alpha.ConversationalSearchService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.ConversationalSearchService`.

#### `AnswerQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.AnswerQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.answer - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.AnswerQuery"`

#### `ConverseConversation`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ConverseConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.converse - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ConverseConversation"`

#### `CreateConversation`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateConversation"`

#### `CreateSession`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.CreateSession"`

#### `DeleteConversation`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteConversation"`

#### `DeleteSession`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.DeleteSession"`

#### `GetAnswer`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetAnswer`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.answers.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetAnswer"`

#### `GetConversation`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetConversation"`

#### `GetSession`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetSession`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.GetSession"`

#### `ListConversations`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListConversations`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListConversations"`

#### `ListSessions`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListSessions`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.sessions.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.ListSessions"`

#### `StreamAnswerQuery`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.StreamAnswerQuery`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.answer - DATA_READ`
- **Method is a long-running or streaming operation**:
  [**Streaming RPC**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#streaming)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.StreamAnswerQuery"`

#### `UpdateConversation`

- **Method**: `google.cloud.discoveryengine.v1alpha.ConversationalSearchService.UpdateConversation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.conversations.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ConversationalSearchService.UpdateConversation"`

### `google.cloud.discoveryengine.v1alpha.DataConnectorService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.DataConnectorService`.

#### `AcquireAccessToken`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataConnectorService.AcquireAccessToken`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataConnectors.acquireAccessToken - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.AcquireAccessToken"`

#### `CheckRefreshToken`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataConnectorService.CheckRefreshToken`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataConnectors.checkRefreshToken - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.CheckRefreshToken"`

#### `GetConnectorSecret`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataConnectorService.GetConnectorSecret`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataConnectors.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.GetConnectorSecret"`

#### `GetDataConnector`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataConnectorService.GetDataConnector`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataConnectors.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.GetDataConnector"`

#### `ListConnectorRuns`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataConnectorService.ListConnectorRuns`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.connectorRuns.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.ListConnectorRuns"`

#### `SetUpDataConnector`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataConnectorService.SetUpDataConnector`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.locations.setUpDataConnector - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.SetUpDataConnector"`

#### `UpdateDataConnector`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataConnectorService.UpdateDataConnector`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataConnectors.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataConnectorService.UpdateDataConnector"`

### `google.cloud.discoveryengine.v1alpha.DataStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.DataStoreService`.

#### `AddPatientFilter`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.AddPatientFilter`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.addPatientFilters - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.AddPatientFilter"`

#### `CreateDataStore`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.CreateDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.CreateDataStore"`

#### `DeleteDataStore`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.DeleteDataStore"`

#### `DeletePatientFilters`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.DeletePatientFilters`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.deletePatientFilters - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.DeletePatientFilters"`

#### `GetCompletionConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.GetCompletionConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.completionConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.GetCompletionConfig"`

#### `GetDataStore`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStore`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.GetDataStore"`

#### `GetDocumentProcessingConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocumentProcessingConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documentProcessingConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.GetDocumentProcessingConfig"`

#### `GetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.GetIamPolicy`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.getIamPolicy - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.GetIamPolicy"`

#### `ListDataStores`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.ListDataStores`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.dataStores.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.ListDataStores"`

#### `RemovePatientFilter`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.RemovePatientFilter`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.deletePatientFilters - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.RemovePatientFilter"`

#### `ReplacePatientFilter`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.ReplacePatientFilter`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.updatePatientFilters - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.ReplacePatientFilter"`

#### `SetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.SetIamPolicy`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.setIamPolicy - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.SetIamPolicy"`

#### `UpdateCompletionConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateCompletionConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.completionConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateCompletionConfig"`

#### `UpdateDataStore`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDataStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.dataStores.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDataStore"`

#### `UpdateDocumentProcessingConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDocumentProcessingConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.documentProcessingConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DataStoreService.UpdateDocumentProcessingConfig"`

### `google.cloud.discoveryengine.v1alpha.DocumentService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.DocumentService`.

#### `BatchGetDocumentsMetadata`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.BatchGetDocumentsMetadata`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.batchGetDocumentsMetadata - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.BatchGetDocumentsMetadata"`

#### `CreateDocument`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.CreateDocument"`

#### `DeleteDocument`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.DeleteDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.delete - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.DeleteDocument"`

#### `GetDocument`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.GetDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.GetDocument"`

#### `GetProcessedDocument`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.GetProcessedDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.GetProcessedDocument"`

#### `ImportDocuments`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.ImportDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.import - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.ImportDocuments"`

#### `ListDocuments`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.ListDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.ListDocuments"`

#### `PurgeDocuments`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.PurgeDocuments`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.purge - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.PurgeDocuments"`

#### `UpdateDocument`

- **Method**: `google.cloud.discoveryengine.v1alpha.DocumentService.UpdateDocument`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.documents.update - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.DocumentService.UpdateDocument"`

### `google.cloud.discoveryengine.v1alpha.EngineService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.EngineService`.

#### `CreateEngine`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.CreateEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.CreateEngine"`

#### `DeleteEngine`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.DeleteEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.DeleteEngine"`

#### `GetEngine`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.GetEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.GetEngine"`

#### `GetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.GetIamPolicy`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.getIamPolicy - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.GetIamPolicy"`

#### `GetWorkspaceSettings`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.GetWorkspaceSettings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.GetWorkspaceSettings"`

#### `ListEngines`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.ListEngines`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.list - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.ListEngines"`

#### `PauseEngine`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.PauseEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.pause - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.PauseEngine"`

#### `ResumeEngine`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.ResumeEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.resume - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.ResumeEngine"`

#### `SetIamPolicy`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.SetIamPolicy`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.setIamPolicy - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.SetIamPolicy"`

#### `TuneEngine`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.TuneEngine`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.engines.tune - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.TuneEngine"`

#### `UpdateEngine`

- **Method**: `google.cloud.discoveryengine.v1alpha.EngineService.UpdateEngine`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.engines.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EngineService.UpdateEngine"`

### `google.cloud.discoveryengine.v1alpha.EstimateBillingService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.EstimateBillingService`.

#### `EstimateDataSize`

- **Method**: `google.cloud.discoveryengine.v1alpha.EstimateBillingService.EstimateDataSize`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.locations.estimateDataSize - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EstimateBillingService.EstimateDataSize"`

### `google.cloud.discoveryengine.v1alpha.EvaluationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.EvaluationService`.

#### `CreateEvaluation`

- **Method**: `google.cloud.discoveryengine.v1alpha.EvaluationService.CreateEvaluation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.evaluations.create - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EvaluationService.CreateEvaluation"`

#### `GetEvaluation`

- **Method**: `google.cloud.discoveryengine.v1alpha.EvaluationService.GetEvaluation`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.evaluations.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EvaluationService.GetEvaluation"`

#### `ListEvaluationResults`

- **Method**: `google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationResults`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.evaluations.get - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluationResults"`

#### `ListEvaluations`

- **Method**: `google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.evaluations.list - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.EvaluationService.ListEvaluations"`

### `google.cloud.discoveryengine.v1alpha.GroundedGenerationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.GroundedGenerationService`.

#### `CheckGrounding`

- **Method**: `google.cloud.discoveryengine.v1alpha.GroundedGenerationService.CheckGrounding`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.groundingConfigs.check - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.GroundedGenerationService.CheckGrounding"`

### `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService`.

#### `CreateIdentityMappingStore`

- **Method**: `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.CreateIdentityMappingStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.identityMappingStores.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.CreateIdentityMappingStore"`

#### `DeleteIdentityMappingStore`

- **Method**: `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.DeleteIdentityMappingStore`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.identityMappingStores.delete - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.DeleteIdentityMappingStore"`

#### `ImportIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ImportIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.importIdentityMappings - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ImportIdentityMappings"`

#### `ListIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ListIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.listIdentityMappings - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.ListIdentityMappings"`

#### `PurgeIdentityMappings`

- **Method**: `google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.PurgeIdentityMappings`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.identityMappingStores.purgeIdentityMappings - DATA_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.IdentityMappingStoreService.PurgeIdentityMappings"`

### `google.cloud.discoveryengine.v1alpha.LicenseConfigService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.LicenseConfigService`.

#### `CreateLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.LicenseConfigService.CreateLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.licenseConfigs.create - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.CreateLicenseConfig"`

#### `DistributeLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.LicenseConfigService.DistributeLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.billingAccountLicenseConfigs.distribute - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.DistributeLicenseConfig"`

#### `GetBillingAccountLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetBillingAccountLicenseConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.billingAccountLicenseConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetBillingAccountLicenseConfig"`

#### `GetLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetLicenseConfig`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.licenseConfigs.get - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.GetLicenseConfig"`

#### `RetractLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.LicenseConfigService.RetractLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.billingAccountLicenseConfigs.retract - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.RetractLicenseConfig"`

#### `UpdateLicenseConfig`

- **Method**: `google.cloud.discoveryengine.v1alpha.LicenseConfigService.UpdateLicenseConfig`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.licenseConfigs.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.LicenseConfigService.UpdateLicenseConfig"`

### `google.cloud.discoveryengine.v1alpha.ProjectService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.ProjectService`.

#### `ProvisionProject`

- **Method**: `google.cloud.discoveryengine.v1alpha.ProjectService.ProvisionProject`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.projects.provision - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  [**Long-running operation**](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#lro)
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectService.ProvisionProject"`

#### `ReportConsentChange`

- **Method**: `google.cloud.discoveryengine.v1alpha.ProjectService.ReportConsentChange`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.projects.reportConsentChange - ADMIN_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectService.ReportConsentChange"`

#### `UpdateProject`

- **Method**: `google.cloud.discoveryengine.v1alpha.ProjectService.UpdateProject`
- **Audit log type**: [Admin activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity)
- **Permissions**:
  - `discoveryengine.projects.update - ADMIN_WRITE`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.ProjectService.UpdateProject"`

### `google.cloud.discoveryengine.v1alpha.RankService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.RankService`.

#### `Rank`

- **Method**: `google.cloud.discoveryengine.v1alpha.RankService.Rank`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.rankingConfigs.rank - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.RankService.Rank"`

### `google.cloud.discoveryengine.v1alpha.RecommendationService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.RecommendationService`.

#### `Recommend`

- **Method**: `google.cloud.discoveryengine.v1alpha.RecommendationService.Recommend`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.servingConfigs.recommend - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.RecommendationService.Recommend"`

### `google.cloud.discoveryengine.v1alpha.RequirementService`

The following audit logs are associated with methods belonging to
`google.cloud.discoveryengine.v1alpha.RequirementService`.

#### `CheckRequirement`

- **Method**: `google.cloud.discoveryengine.v1alpha.RequirementService.CheckRequirement`
- **Audit log type**: [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)
- **Permissions**:
  - `discoveryengine.requirements.checkRequirement - DATA_READ`
- **Method is a long-running or streaming operation**:
  No.
- **Filter for this method**: `protoPayload.methodName="google.cloud.discoveryengine.v1alpha.RequirementService.CheckRequirement"`
