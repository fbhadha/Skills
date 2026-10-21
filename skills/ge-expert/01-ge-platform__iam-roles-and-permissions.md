# Gemini Enterprise: platform, security, agents, cost, monitoring / IAM roles and permissions
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 101-140, extracted 2026-10-18

## IAM roles and permissions

URL: https://docs.cloud.google.com/gemini/enterprise/docs/access-control

This page describes how you can control API access and permissions for Gemini Enterprise resources using Identity and Access Management (IAM). 

### Overview

Google Cloud offers IAM, which lets you give more granular access to specific Google Cloud resources and prevents unwanted access to other resources. This page describes the Gemini Enterprise IAM roles and permissions. For a detailed description of Google Cloud IAM, see the IAM documentation (/iam/docs). 

Gemini Enterprise provides a set of predefined roles (#roles) designed to help you control access to your Gemini Enterprise resources. You can also create your own custom roles (/iam/docs/understanding-custom-roles), if the predefined roles don't provide the sets of permissions you need. In addition, the older basic roles (Editor, Viewer, and Owner) are also still available to you, although they don't provide the same fine-grained control as the Gemini Enterprise roles. In particular, the basic roles provide access to resources across Google Cloud rather than just for Gemini Enterprise. See the basic roles (/iam/docs/roles-overview#basic) documentation for more information. 

### Predefined roles

Gemini Enterprise provides some predefined roles that you can use to provide finergrained permissions to principals. The role you grant to a principal controls what actions the principal can take. Principals can be individuals, groups, or service accounts. 

You can grant multiple roles to the same principal, and you can change the roles granted to a principal at any time, provided you have the permissions to do so. 

The broader roles include the more narrowly defined roles. For example, the Discovery Engine Editor role includes all of the permissions of the Discovery Engine Viewer role, along with the addition permissions of the Discovery Engine Editor role. Likewise, the Gemini Enterprise Admin role includes all of the permissions of the Discovery Engine Editor role, along with its additional permissions. 

The basic roles (Owner, Editor, Viewer) provide permissions across Google Cloud. The roles specific to Gemini Enterprise provide only Gemini Enterprise permissions, except for 

the following Google Cloud permissions, which are needed for general Google Cloud usage: 

- `resourcemanager.projects.get` 

- `resourcemanager.projects.list` 

- `serviceusage.services.list` 

- `serviceusage.services.get` 

The following table lists the Gemini Enterprise IAM roles with a corresponding list of all the permissions for each role. 

|Role|Permissions|
|---|---|
|Gemini Enterprise Admin<br>(`roles/discoveryengine.agentspaceAdmin`)<br>|<sup>`cloudaicompanion.aiDevToolsSettings.*`</sup><br>`cloudaicompanion.aiDevToolsSettings.`<br>`create`|
|Grants admin-level access to Gemini Enterprise<br>resources.|`cloudaicompanion.aiDevToolsSettings.`<br>`delete`|
||`cloudaicompanion.aiDevToolsSettings.get`<br>`cloudaicompanion.aiDevToolsSettings.list`<br>`cloudaicompanion.aiDevToolsSettings.`<br>`update`<br> <sup>`cloudaicompanion.codeRepositoryIndexes.*`</sup><br>`cloudaicompanion.codeRepositoryIndexes.`<br>`create`|
||`cloudaicompanion.codeRepositoryIndexes.`<br>`delete`|
||`cloudaicompanion.codeRepositoryIndexes.`<br>`get`<br>`cloudaicompanion.codeRepositoryIndexes.`<br>`list`|
||`cloudaicompanion.codeRepositoryIndexes.`<br>`update`|
|<br><br>|<sup>`cloudaicompanion.codeToolsSettings.*`</sup><br>`cloudaicompanion.codeToolsSettings.create`<br>`cloudaicompanion.codeToolsSettings.delete`<br>`cloudaicompanion.codeToolsSettings.get`<br>`cloudaicompanion.codeToolsSettings.list`<br>`cloudaicompanion.codeToolsSettings.update`<br> <sup>`cloudaicompanion.`</sup><br>`dataSharingWithGoogleSettings.*`<br>`cloudaicompanion.`<br>`dataSharingWithGoogleSettings.create`<br>`cloudaicompanion.`<br>`dataSharingWithGoogleSettings.delete`<br>`cloudaicompanion.`<br>`dataSharingWithGoogleSettings.get`<br>`cloudaicompanion.`<br>`dataSharingWithGoogleSettings.list`<br>`cloudaicompanion.`<br>`dataSharingWithGoogleSettings.update`<br> <sup>`cloudaicompanion.`</sup><br>`geminiGcpEnablementSettings.*`<br>`cloudaicompanion.`<br>`geminiGcpEnablementSettings.create`<br>`cloudaicompanion.`<br>`geminiGcpEnablementSettings.delete`|

|Role|Permissions|
|---|---|
||`cloudaicompanion.`|
||`geminiGcpEnablementSettings.get`<br>`cloudaicompanion.`<br>`geminiGcpEnablementSettings.list`<br>|
||`cloudaicompanion.`<br>|
||`geminiGcpEnablementSettings.update`|
|| <sup>`cloudaicompanion.`</sup>|
||`gibqObservabilitySettings.*`|
||`cloudaicompanion.`|
||`gibqObservabilitySettings.create`<br>`cloudaicompanion.`|
||`gibqObservabilitySettings.delete`<br>`cloudaicompanion.`|
||`gibqObservabilitySettings.get`<br>`cloudaicompanion.`<br>`gibqObservabilitySettings.list`<br>`cloudaicompanion.`|
||`gibqObservabilitySettings.update`<br>`cloudaicompanion.instances.`<br>`queryEffectiveSetting`<br>`cloudaicompanion.instances.`|
||`queryEffectiveSettingBindings`|
|| <sup>`cloudaicompanion.loggingSettings.*`</sup><br>`cloudaicompanion.loggingSettings.create`<br>`cloudaicompanion.loggingSettings.delete`<br>`cloudaicompanion.loggingSettings.get`<br>`cloudaicompanion.loggingSettings.list`<br>`cloudaicompanion.loggingSettings.update`|
|| <sup>`cloudaicompanion.operations.*`</sup>|
||`cloudaicompanion.operations.cancel`|
||`cloudaicompanion.operations.delete`|
||`cloudaicompanion.operations.get`|
||`cloudaicompanion.operations.list`|
|| <sup>`cloudaicompanion.releaseChannelSettings.*`</sup>|
||`cloudaicompanion.releaseChannelSettings.`<br>`create`|
||`cloudaicompanion.releaseChannelSettings.`<br>`delete`|
||`cloudaicompanion.releaseChannelSettings.`<br>`get`|
||`cloudaicompanion.releaseChannelSettings.`<br>`list`|
||`cloudaicompanion.releaseChannelSettings.`<br>`update`|
||`cloudaicompanion.repositoryGroups.create`|
||`cloudaicompanion.repositoryGroups.delete`|

|Role<br>Permissions|
|---|
|`cloudaicompanion.repositoryGroups.get`<br>`cloudaicompanion.repositoryGroups.`<br>`getIamPolicy`<br>`cloudaicompanion.repositoryGroups.list`<br>`cloudaicompanion.repositoryGroups.`<br>`setIamPolicy`<br>`cloudaicompanion.repositoryGroups.update`<br> <sup>`cloudaicompanion.settingBindings.*`</sup><br>`cloudaicompanion.settingBindings.`<br>`aiDevToolsSettingsCreate`<br>`cloudaicompanion.settingBindings.`<br>`aiDevToolsSettingsDelete`|
|`cloudaicompanion.settingBindings.`<br>`aiDevToolsSettingsGet`|
|`cloudaicompanion.settingBindings.`<br>`aiDevToolsSettingsList`<br>`cloudaicompanion.settingBindings.`<br>`aiDevToolsSettingsUpdate`<br>`cloudaicompanion.settingBindings.`<br>`aiDevToolsSettingsUse`|
|`cloudaicompanion.settingBindings.`<br>`codeToolsSettingsCreate`|
|`cloudaicompanion.settingBindings.`<br>`codeToolsSettingsDelete`<br>`cloudaicompanion.settingBindings.`<br>`codeToolsSettingsGet`<br>`cloudaicompanion.settingBindings.`<br>`codeToolsSettingsList`|
|`cloudaicompanion.settingBindings.`<br>`codeToolsSettingsUpdate`<br>`cloudaicompanion.settingBindings.`<br>`codeToolsSettingsUse`<br>`cloudaicompanion.settingBindings.`<br>`dataSharingWithGoogleSettingsCreate`<br>`cloudaicompanion.settingBindings.`<br>`dataSharingWithGoogleSettingsDelete`<br>`cloudaicompanion.settingBindings.`<br>`dataSharingWithGoogleSettingsGet`<br>`cloudaicompanion.settingBindings.`<br>`dataSharingWithGoogleSettingsList`<br>`cloudaicompanion.settingBindings.`<br>`dataSharingWithGoogleSettingsUpdate`<br>`cloudaicompanion.settingBindings.`<br>`dataSharingWithGoogleSettingsUse`<br>`cloudaicompanion.settingBindings.`<br>`geminiGcpEnablementSettingsCreate`|

|Role|Permissions|
|---|---|
||`cloudaicompanion.settingBindings.`<br>`geminiGcpEnablementSettingsDelete`<br>`cloudaicompanion.settingBindings.`<br>`geminiGcpEnablementSettingsGet`<br>`cloudaicompanion.settingBindings.`<br>`geminiGcpEnablementSettingsList`<br>`cloudaicompanion.settingBindings.`<br>`geminiGcpEnablementSettingsUpdate`<br>`cloudaicompanion.settingBindings.`<br>`geminiGcpEnablementSettingsUse`<br>`cloudaicompanion.settingBindings.`<br>`gibqObservabilitySettingsCreate`<br>`cloudaicompanion.settingBindings.`<br>`gibqObservabilitySettingsDelete`<br>`cloudaicompanion.settingBindings.`<br>`gibqObservabilitySettingsGet`|
||`cloudaicompanion.settingBindings.`<br>`gibqObservabilitySettingsList`|
||`cloudaicompanion.settingBindings.`<br>`gibqObservabilitySettingsUpdate`<br>`cloudaicompanion.settingBindings.`<br>`gibqObservabilitySettingsUse`|
||`cloudaicompanion.settingBindings.`<br>`loggingSettingsCreate`|
||`cloudaicompanion.settingBindings.`<br>`loggingSettingsDelete`|
||`cloudaicompanion.settingBindings.`<br>`loggingSettingsGet`|
||`cloudaicompanion.settingBindings.`|
||`loggingSettingsList`|
||`cloudaicompanion.settingBindings.`<br>`loggingSettingsUpdate`|
||`cloudaicompanion.settingBindings.`<br>`loggingSettingsUse`|
||`cloudaicompanion.settingBindings.`<br>`releaseChannelSettingsCreate`<br>`cloudaicompanion.settingBindings.`<br>`releaseChannelSettingsDelete`<br>`cloudaicompanion.settingBindings.`<br>`releaseChannelSettingsGet`|
||`cloudaicompanion.settingBindings.`<br>`releaseChannelSettingsList`|
||`cloudaicompanion.settingBindings.`<br>`releaseChannelSettingsUpdate`|
||`cloudaicompanion.settingBindings.`<br>`releaseChannelSettingsUse`|

Role Permissions `cloudnotifications.activities.list` <sup>`cloudtrace.insights.*`</sup> `cloudtrace.insights.get cloudtrace.insights.list cloudtrace.stats.get` <sup>`cloudtrace.tasks.*`</sup> `cloudtrace.tasks.create cloudtrace.tasks.delete cloudtrace.tasks.get cloudtrace.tasks.list` <sup>`cloudtrace.traceScopes.*`</sup> `cloudtrace.traceScopes.create cloudtrace.traceScopes.delete cloudtrace.traceScopes.get cloudtrace.traceScopes.list cloudtrace.traceScopes.update cloudtrace.traces.get cloudtrace.traces.list` <sup>`consumerprocurement.entitlements.*`</sup> `consumerprocurement.entitlements.get consumerprocurement.entitlements.list discoveryengine.accounts.create` <sup>`discoveryengine.aclConfigs.*`</sup> `discoveryengine.aclConfigs.get discoveryengine.aclConfigs.update` <sup>`discoveryengine.agentFiles.*`</sup> `discoveryengine.agentFiles.delete discoveryengine.agentFiles.download discoveryengine.agentFiles.import discoveryengine.agentFiles.list discoveryengine.agentFiles.upload` <sup>`discoveryengine.agentIamProposals.*`</sup> `discoveryengine.agentIamProposals.create discoveryengine.agentIamProposals.delete discoveryengine.agentIamProposals.get discoveryengine.agentIamProposals.list discoveryengine.agents.create discoveryengine.agents.delete discoveryengine.agents.get discoveryengine.agents.getAgentView discoveryengine.agents.getIamPolicy discoveryengine.agents.list discoveryengine.agents. listAvailableAgentViews discoveryengine.agents.manage discoveryengine.agents.setIamPolicy` 

|Role|Permissions|
|---|---|
||`discoveryengine.agents.update`<br> <sup>`discoveryengine.alertPolicies.*`</sup><br>`discoveryengine.alertPolicies.create`<br>`discoveryengine.alertPolicies.get`<br>`discoveryengine.alertPolicies.update`<br> <sup>`discoveryengine.analytics.*`</sup><br>`discoveryengine.analytics.`<br>`acquireDashboardSession`<br>`discoveryengine.analytics.`<br>`refreshDashboardSessionTokens`<br>`discoveryengine.answers.get`<br>`discoveryengine.assistAnswers.get`<br> <sup>`discoveryengine.assistants.*`</sup><br>`discoveryengine.assistants.assist`<br>`discoveryengine.assistants.create`<br>`discoveryengine.assistants.delete`<br>`discoveryengine.assistants.get`<br>`discoveryengine.assistants.list`<br>`discoveryengine.assistants.update`<br> <sup>`discoveryengine.audioOverviews.*`</sup><br>`discoveryengine.audioOverviews.create`<br>`discoveryengine.audioOverviews.delete`<br>`discoveryengine.audioOverviews.get`<br>`discoveryengine.audioOverviews.`<br>`getIceConfig`<br>`discoveryengine.audioOverviews.`<br>`sendSdpOffer`<br> <sup>`discoveryengine.authorizations.*`</sup><br>`discoveryengine.authorizations.create`<br>`discoveryengine.authorizations.delete`<br>`discoveryengine.authorizations.get`<br>`discoveryengine.authorizations.list`<br>`discoveryengine.authorizations.`<br>`storeUserAuthorization`<br>`discoveryengine.authorizations.update`|
|| <sup>`discoveryengine.`</sup><br>`billingAccountLicenseConfigs.*`<br>`discoveryengine.`<br>`billingAccountLicenseConfigs.distribute`<br>`discoveryengine.`<br>`billingAccountLicenseConfigs.get`<br>`discoveryengine.`<br>`billingAccountLicenseConfigs.list`<br>`discoveryengine.`<br>`billingAccountLicenseConfigs.retract`<br> <sup>`discoveryengine.branches.*`</sup>|

|Role|Permissions|
|---|---|
||`discoveryengine.branches.get`<br>`discoveryengine.branches.list`<br> <sup>`discoveryengine.cannedQueries.*`</sup><br>`discoveryengine.cannedQueries.create`<br>`discoveryengine.cannedQueries.delete`<br>`discoveryengine.cannedQueries.get`<br>`discoveryengine.cannedQueries.list`<br>`discoveryengine.cannedQueries.`<br>`listActiveCannedQueryUserViews`<br>`discoveryengine.cannedQueries.update`<br> <sup>`discoveryengine.cmekConfigs.*`</sup><br>`discoveryengine.cmekConfigs.delete`<br>`discoveryengine.cmekConfigs.get`<br>`discoveryengine.cmekConfigs.list`<br>`discoveryengine.cmekConfigs.update`<br> <sup>`discoveryengine.collections.*`</sup><br>`discoveryengine.collections.delete`<br>`discoveryengine.collections.get`|
||`discoveryengine.collections.getIamPolicy`<br>`discoveryengine.collections.list`|
||`discoveryengine.collections.setIamPolicy`<br> <sup>`discoveryengine.completionConfigs.*`</sup><br>`discoveryengine.completionConfigs.`<br>`completeQuery`|
||`discoveryengine.completionConfigs.get`<br>`discoveryengine.completionConfigs.`<br>`removeSuggestion`<br>`discoveryengine.completionConfigs.update`<br> <sup>`discoveryengine.completionSuggestions.*`</sup><br>`discoveryengine.completionSuggestions.`<br>`import`|
||`discoveryengine.completionSuggestions.`<br>`purge`|
|| <sup>`discoveryengine.connectorRuns.*`</sup>|
||`discoveryengine.connectorRuns.cancel`<br>`discoveryengine.connectorRuns.list`|
|| <sup>`discoveryengine.controls.*`</sup><br>`discoveryengine.controls.create`<br>`discoveryengine.controls.delete`<br>`discoveryengine.controls.get`<br>`discoveryengine.controls.list`<br>`discoveryengine.controls.update`<br> <sup>`discoveryengine.conversations.*`</sup>|
||`discoveryengine.conversations.converse`<br>`discoveryengine.conversations.create`<br>`discoveryengine.conversations.delete`|

|Role|Permissions|
|---|---|
||`discoveryengine.conversations.get`<br>`discoveryengine.conversations.list`<br>`discoveryengine.conversations.update`<br> <sup>`discoveryengine.dataConnectors.*`</sup><br>`discoveryengine.dataConnectors.`<br>`acquireAccessToken`<br>`discoveryengine.dataConnectors.`<br>`acquireAndStoreRefreshToken`<br>`discoveryengine.dataConnectors.`<br>`buildActionInvocation`<br>`discoveryengine.dataConnectors.`<br>`checkRefreshToken`<br>`discoveryengine.dataConnectors.`<br>`executeAction`|
||`discoveryengine.dataConnectors.get`<br>`discoveryengine.dataConnectors.`<br>`queryAvailableActions`|
||`discoveryengine.dataConnectors.`<br>`startConnectorRun`|
||`discoveryengine.dataConnectors.update`<br> <sup>`discoveryengine.dataStores.*`</sup><br>`discoveryengine.dataStores.completeQuery`<br>`discoveryengine.dataStores.create`<br>`discoveryengine.dataStores.delete`<br>`discoveryengine.dataStores.`<br>`enrollSolutions`|
||`discoveryengine.dataStores.get`<br>`discoveryengine.dataStores.getIamPolicy`<br>`discoveryengine.dataStores.list`<br>`discoveryengine.dataStores.`<br>`listCustomModels`|
||`discoveryengine.dataStores.setIamPolicy`<br>`discoveryengine.dataStores.`<br>`trainCustomModel`<br>`discoveryengine.dataStores.update`<br> <sup>`discoveryengine.devToolsConfigs.*`</sup><br>`discoveryengine.devToolsConfigs.get`<br>`discoveryengine.devToolsConfigs.update`<br> <sup>`discoveryengine.documentProcessingConfigs.*`</sup><br>`discoveryengine.`<br>`documentProcessingConfigs.get`<br>`discoveryengine.`<br>`documentProcessingConfigs.update`<br> <sup>`discoveryengine.documents.*`</sup><br>`discoveryengine.documents.`<br>`batchGetDocumentsMetadata`|

Role Permissions `discoveryengine.documents.create discoveryengine.documents.delete discoveryengine.documents.get discoveryengine.documents.import discoveryengine.documents.list discoveryengine.documents.purge discoveryengine.documents.update` <sup>`discoveryengine.engines.*`</sup> `discoveryengine.engines.create discoveryengine.engines. createEngineUserData discoveryengine.engines.delete discoveryengine.engines.generateMemories discoveryengine.engines. generatePersonalContext discoveryengine.engines.get discoveryengine.engines.getEngineUserData discoveryengine.engines.getIamPolicy discoveryengine.engines. getPersonalContext discoveryengine.engines.list discoveryengine.engines.pause discoveryengine.engines.resume discoveryengine.engines.setIamPolicy discoveryengine.engines.tune discoveryengine.engines.update discoveryengine.engines. updateEngineUserData` <sup>`discoveryengine.evaluations.*`</sup> `discoveryengine.evaluations.create discoveryengine.evaluations.get discoveryengine.evaluations.list discoveryengine.groundingConfigs.check discoveryengine.homepageDataConfigs. fetchDocuments` <sup>`discoveryengine.ideaForgeIdeas.*`</sup> `discoveryengine.ideaForgeIdeas.create discoveryengine.ideaForgeIdeas.get` <sup>`discoveryengine.ideaForgeInstances.*`</sup> `discoveryengine.ideaForgeInstances.get discoveryengine.ideaForgeInstances.start discoveryengine.ideaForgeInstances.stop` <sup>`discoveryengine.identityMappingStores.*`</sup> `discoveryengine.identityMappingStores. create` 

|Role|Permissions|
|---|---|
||`discoveryengine.identityMappingStores.`<br>`delete`|
||`discoveryengine.identityMappingStores.get`<br>`discoveryengine.identityMappingStores.`<br>`importIdentityMappings`<br>`discoveryengine.identityMappingStores.`<br>`list`|
||`discoveryengine.identityMappingStores.`<br>`listIdentityMappings`|
||`discoveryengine.identityMappingStores.`<br>`purgeIdentityMappings`|
|| <sup>`discoveryengine.immersiveArtifacts.*`</sup>|
||`discoveryengine.immersiveArtifacts.create`<br>`discoveryengine.immersiveArtifacts.delete`<br>`discoveryengine.immersiveArtifacts.export`<br>`discoveryengine.immersiveArtifacts.get`|
||`discoveryengine.immersiveArtifacts.list`<br>`discoveryengine.immersiveArtifacts.`<br>`navigate`|
||`discoveryengine.immersiveArtifacts.update`<br> <sup>`discoveryengine.licenseConfigs.*`</sup>|
||`discoveryengine.licenseConfigs.create`<br>`discoveryengine.licenseConfigs.get`|
||`discoveryengine.licenseConfigs.list`<br>`discoveryengine.licenseConfigs.update`|
|| <sup>`discoveryengine.locations.*`</sup><br>`discoveryengine.locations.`<br>`buildAuthorizationUrl`|
||`discoveryengine.locations.`|
||`completeExternalIdentities`<br>`discoveryengine.locations.`|
||`estimateDataSize`|
||`discoveryengine.locations.`<br>`exchangeAuthCredentials`|
||`discoveryengine.locations.fetchAgentCards`<br>`discoveryengine.locations.`<br>|
||`getConnectorSource`<br>`discoveryengine.locations.`<br>`listConnectorSources`|
||`discoveryengine.locations.`<br>`setUpDataConnector`|
|| <sup>`discoveryengine.memories.*`</sup>|
||`discoveryengine.memories.delete`|
||`discoveryengine.memories.list`|
||`discoveryengine.memories.retrieve`|
||`discoveryengine.memories.update`|

|Role|Permissions|
|---|---|
|| <sup>`discoveryengine.models.*`</sup><br>`discoveryengine.models.create`<br>`discoveryengine.models.delete`<br>`discoveryengine.models.get`<br>`discoveryengine.models.list`<br>`discoveryengine.models.pause`<br>`discoveryengine.models.resume`<br>`discoveryengine.models.tune`<br>`discoveryengine.models.update`<br> <sup>`discoveryengine.notebooks.*`</sup>|
||`discoveryengine.notebooks.create`<br>`discoveryengine.notebooks.generateGuide`<br>`discoveryengine.notebooks.get`<br>`discoveryengine.notebooks.getAnalytics`<br>`discoveryengine.notebooks.getIamPolicy`<br>`discoveryengine.notebooks.interactSources`<br>|
||`discoveryengine.notebooks.list`<br>`discoveryengine.notebooks.removeSelf`<br>`discoveryengine.notebooks.setIamPolicy`<br>`discoveryengine.notebooks.update`|
|| <sup>`discoveryengine.notes.*`</sup>|
||`discoveryengine.notes.create`<br>`discoveryengine.notes.delete`<br>`discoveryengine.notes.get`<br>`discoveryengine.notes.update`|
|| <sup>`discoveryengine.notificationMessages.*`</sup><br>`discoveryengine.notificationMessages.`<br>`ackAll`|
||`discoveryengine.notificationMessages.list`<br>`discoveryengine.notificationMessages.`<br>`update`|
|| <sup>`discoveryengine.operations.*`</sup>|
||`discoveryengine.operations.get`<br>`discoveryengine.operations.list`<br>`discoveryengine.podcasts.create`|
||`discoveryengine.projectOverageConfigs.get`<br> <sup>`discoveryengine.projects.*`</sup>|
||`discoveryengine.projects.get`<br>`discoveryengine.projects.provision`<br>`discoveryengine.projects.`<br>`reportConsentChange`|
||`discoveryengine.projects.update`<br>`discoveryengine.rankingConfigs.rank`|
|| <sup>`discoveryengine.sampleQueries.*`</sup>|
||`discoveryengine.sampleQueries.create`<br>`discoveryengine.sampleQueries.delete`|

|Role|Permissions|
|---|---|
||`discoveryengine.sampleQueries.get`<br>`discoveryengine.sampleQueries.import`<br>`discoveryengine.sampleQueries.list`<br>`discoveryengine.sampleQueries.update`<br> <sup>`discoveryengine.sampleQuerySets.*`</sup><br>`discoveryengine.sampleQuerySets.create`<br>`discoveryengine.sampleQuerySets.delete`<br>`discoveryengine.sampleQuerySets.get`<br>`discoveryengine.sampleQuerySets.list`<br>`discoveryengine.sampleQuerySets.update`<br> <sup>`discoveryengine.schemas.*`</sup>|
||`discoveryengine.schemas.create`<br>`discoveryengine.schemas.delete`<br>`discoveryengine.schemas.get`<br>`discoveryengine.schemas.list`|
||`discoveryengine.schemas.preview`<br>`discoveryengine.schemas.update`|
||`discoveryengine.schemas.validate`<br> <sup>`discoveryengine.servingConfigs.*`</sup>|
||`discoveryengine.servingConfigs.answer`<br>`discoveryengine.servingConfigs.create`<br>`discoveryengine.servingConfigs.delete`|
||`discoveryengine.servingConfigs.get`<br>`discoveryengine.servingConfigs.list`|
||`discoveryengine.servingConfigs.recommend`<br>`discoveryengine.servingConfigs.search`<br>`discoveryengine.servingConfigs.update`|
|| <sup>`discoveryengine.sessions.*`</sup>|
||`discoveryengine.sessions.addContextFile`<br>`discoveryengine.sessions.create`|
||`discoveryengine.sessions.delete`|
||`discoveryengine.sessions.downloadFile`|
||`discoveryengine.sessions.generateSummary`|
||`discoveryengine.sessions.get`<br>`discoveryengine.sessions.list`<br>`discoveryengine.sessions.`<br>`listSessionFileMetadata`|
||`discoveryengine.sessions.`<br>`recommendQuestions`|
||`discoveryengine.sessions.`<br>`removeContextFile`|
||`discoveryengine.sessions.search`<br>`discoveryengine.sessions.`|
||`selectContextFiles`|
||`discoveryengine.sessions.update`|
||`discoveryengine.sessions.uploadFile`|

|Role|Permissions|
|---|---|
|| <sup>`discoveryengine.sharedContents.*`</sup><br>`discoveryengine.sharedContents.create`<br>`discoveryengine.sharedContents.delete`<br>`discoveryengine.sharedContents.get`<br>`discoveryengine.sharedContents.list`<br> <sup>`discoveryengine.siteSearchEngines.*`</sup><br>`discoveryengine.siteSearchEngines.`<br>`batchVerifyTargetSites`<br>`discoveryengine.siteSearchEngines.`<br>`disableAdvancedSiteSearch`<br>`discoveryengine.siteSearchEngines.`<br>`enableAdvancedSiteSearch`<br>`discoveryengine.siteSearchEngines.`<br>`fetchDomainVerificationStatus`<br>`discoveryengine.siteSearchEngines.get`<br>`discoveryengine.siteSearchEngines.`<br>`recrawlUris`|
|| <sup>`discoveryengine.sitemaps.*`</sup><br>`discoveryengine.sitemaps.create`<br>`discoveryengine.sitemaps.delete`<br>`discoveryengine.sitemaps.fetch`<br> <sup>`discoveryengine.sources.*`</sup><br>`discoveryengine.sources.checkFreshness`<br>`discoveryengine.sources.create`<br>`discoveryengine.sources.delete`<br>`discoveryengine.sources.`<br>`generateDocumentGuide`<br>|
||`discoveryengine.sources.get`<br>`discoveryengine.sources.refresh`<br>`discoveryengine.sources.update`<br> <sup>`discoveryengine.suggestionDenyListEntries.*`</sup><br>`discoveryengine.`<br>`suggestionDenyListEntries.import`<br>`discoveryengine.`<br>`suggestionDenyListEntries.purge`<br> <sup>`discoveryengine.targetSites.*`</sup><br>`discoveryengine.targetSites.batchCreate`<br>`discoveryengine.targetSites.create`<br>`discoveryengine.targetSites.delete`<br>`discoveryengine.targetSites.get`<br>`discoveryengine.targetSites.list`<br>`discoveryengine.targetSites.update`<br> <sup>`discoveryengine.userEvents.*`</sup>|
||`discoveryengine.userEvents.create`<br>`discoveryengine.userEvents.fetchStats`<br>`discoveryengine.userEvents.import`|

Role Permissions `discoveryengine.userEvents.purge` <sup>`discoveryengine.userStores.*`</sup> `discoveryengine.userStores. batchUpdateUserLicenses discoveryengine.userStores.get discoveryengine.userStores. listUserLicenses discoveryengine.userStores.update` <sup>`discoveryengine.users.*`</sup> `discoveryengine.users.get discoveryengine.users.update` <sup>`discoveryengine.widgetConfigs.*`</sup> `discoveryengine.widgetConfigs.get discoveryengine.widgetConfigs.update logging.buckets.get logging.buckets.list logging.buckets.listEffectiveTags logging.buckets.listTagBindings logging.exclusions.get logging.exclusions.list logging.links.get logging.links.list` <sup>`logging.locations.*`</sup> `logging.locations.get logging.locations.list logging.logEntries.list logging.logMetrics.get logging.logMetrics.list logging.logScopes.get logging.logScopes.list logging.logServiceIndexes.list logging.logServices.list logging.logs.list logging.notificationRules.get logging.notificationRules.list logging.operations.get logging.operations.list logging.queries.getShared logging.queries.listShared logging.queries.usePrivate logging.settings.get logging.sinks.get logging.sinks.list logging.usage.get logging.views.get logging.views.getIamPolicy` 

Role Permissions `logging.views.list monitoring.alertPolicies.get monitoring.alertPolicies.list monitoring.alertPolicies.listEffectiveTags monitoring.alertPolicies.listTagBindings` <sup>`monitoring.alerts.*`</sup> `monitoring.alerts.get monitoring.alerts.list monitoring.dashboards.get monitoring.dashboards.list monitoring.dashboards.listEffectiveTags monitoring.dashboards.listTagBindings monitoring.groups.get monitoring.groups.list monitoring.metricDescriptors.get monitoring.metricDescriptors.list` <sup>`monitoring.monitoredResourceDescriptors.*`</sup> `monitoring.monitoredResourceDescriptors. get monitoring.monitoredResourceDescriptors. list` <sup>`monitoring.notificationChannelDescriptors.*`</sup> `monitoring. notificationChannelDescriptors.get monitoring. notificationChannelDescriptors.list monitoring.notificationChannels.get monitoring.notificationChannels.list monitoring.services.get monitoring.services.list monitoring.slos.get monitoring.slos.list monitoring.snoozes.get monitoring.snoozes.list monitoring.timeSeries.list monitoring.uptimeCheckConfigs.get monitoring.uptimeCheckConfigs.list observability.scopes.get` <sup>`observability.traceScopes.*`</sup> `observability.traceScopes.create observability.traceScopes.delete observability.traceScopes.get observability.traceScopes.list observability.traceScopes.update opsconfigmonitoring.resourceMetadata.list resourcemanager.projects.get` 

|Role|Permissions|
|---|---|
||`resourcemanager.projects.list`|
||`stackdriver.projects.get`|
||`stackdriver.resourceMetadata.list`|

|Role|Permissions|
|---|---|
|Discovery Engine Editor<br>(`roles/discoveryengine.editor`)<br>Grants read and write access to all discovery<br>engine resources.<br>|`discoveryengine.accounts.create`<br>`discoveryengine.aclConfigs.get`<br> <sup>`discoveryengine.agentFiles.*`</sup><br>`discoveryengine.agentFiles.delete`<br>`discoveryengine.agentFiles.download`<br>`discoveryengine.agentFiles.import`<br>`discoveryengine.agentFiles.list`<br>`discoveryengine.agentFiles.upload`<br>`discoveryengine.agents.create`<br>`discoveryengine.agents.delete`<br>`discoveryengine.agents.get`<br>`discoveryengine.agents.getAgentView`<br>`discoveryengine.agents.getIamPolicy`<br>`discoveryengine.agents.list`<br>`discoveryengine.agents.`<br>`listAvailableAgentViews`|
||`discoveryengine.agents.manage`<br>`discoveryengine.agents.update`<br> <sup>`discoveryengine.alertPolicies.*`</sup><br>`discoveryengine.alertPolicies.create`<br>`discoveryengine.alertPolicies.get`<br>`discoveryengine.alertPolicies.update`<br> <sup>`discoveryengine.analytics.*`</sup><br>`discoveryengine.analytics.`<br>`acquireDashboardSession`<br>`discoveryengine.analytics.`<br>`refreshDashboardSessionTokens`<br>`discoveryengine.answers.get`<br>`discoveryengine.assistAnswers.get`<br> <sup>`discoveryengine.assistants.*`</sup><br>`discoveryengine.assistants.assist`<br>`discoveryengine.assistants.create`<br>`discoveryengine.assistants.delete`<br>`discoveryengine.assistants.get`<br>`discoveryengine.assistants.list`<br>`discoveryengine.assistants.update`<br>`discoveryengine.authorizations.`<br>`storeUserAuthorization`<br> <sup>`discoveryengine.branches.*`</sup><br>`discoveryengine.branches.get`<br>`discoveryengine.branches.list`<br>`discoveryengine.cannedQueries.get`<br>`discoveryengine.cannedQueries.list`<br>`discoveryengine.cannedQueries.`<br>`listActiveCannedQueryUserViews`|

|Role|Permissions|
|---|---|
||`discoveryengine.cmekConfigs.get`<br>`discoveryengine.cmekConfigs.list`<br>`discoveryengine.collections.get`<br>`discoveryengine.collections.list`<br> <sup>`discoveryengine.completionConfigs.*`</sup><br>`discoveryengine.completionConfigs.`<br>`completeQuery`|
||`discoveryengine.completionConfigs.get`<br>`discoveryengine.completionConfigs.`<br>`removeSuggestion`<br>`discoveryengine.completionConfigs.update`<br>`discoveryengine.connectorRuns.list`<br> <sup>`discoveryengine.controls.*`</sup><br>`discoveryengine.controls.create`<br>`discoveryengine.controls.delete`<br>`discoveryengine.controls.get`<br>`discoveryengine.controls.list`|
||`discoveryengine.controls.update`<br> <sup>`discoveryengine.conversations.*`</sup>|
||`discoveryengine.conversations.converse`<br>`discoveryengine.conversations.create`<br>`discoveryengine.conversations.delete`|
||`discoveryengine.conversations.get`<br>`discoveryengine.conversations.list`<br>`discoveryengine.conversations.update`<br> <sup>`discoveryengine.dataConnectors.*`</sup>|
||`discoveryengine.dataConnectors.`<br>`acquireAccessToken`|
||`discoveryengine.dataConnectors.`<br>`acquireAndStoreRefreshToken`<br>`discoveryengine.dataConnectors.`<br>`buildActionInvocation`|
||`discoveryengine.dataConnectors.`<br>`checkRefreshToken`|
||`discoveryengine.dataConnectors.`<br>`executeAction`|
||`discoveryengine.dataConnectors.get`<br>`discoveryengine.dataConnectors.`<br>`queryAvailableActions`<br>`discoveryengine.dataConnectors.`<br>`startConnectorRun`|
||`discoveryengine.dataConnectors.update`<br>`discoveryengine.dataStores.completeQuery`<br>`discoveryengine.dataStores.create`<br>`discoveryengine.dataStores.delete`|
||`discoveryengine.dataStores.enrollSolutions`|

Role Permissions `discoveryengine.dataStores.get discoveryengine.dataStores.list discoveryengine.dataStores.listCustomModels discoveryengine.dataStores.trainCustomModel discoveryengine.dataStores.update discoveryengine.devToolsConfigs.get` <sup>`discoveryengine.documentProcessingConfigs.*`</sup> `discoveryengine. documentProcessingConfigs.get discoveryengine. documentProcessingConfigs.update` <sup>`discoveryengine.documents.*`</sup> `discoveryengine.documents. batchGetDocumentsMetadata discoveryengine.documents.create discoveryengine.documents.delete discoveryengine.documents.get discoveryengine.documents.import discoveryengine.documents.list discoveryengine.documents.purge discoveryengine.documents.update discoveryengine.engines.create discoveryengine.engines. createEngineUserData discoveryengine.engines.delete discoveryengine.engines.generateMemories discoveryengine.engines. generatePersonalContext discoveryengine.engines.get discoveryengine.engines.getEngineUserData discoveryengine.engines.getIamPolicy discoveryengine.engines.getPersonalContext discoveryengine.engines.list discoveryengine.engines.pause discoveryengine.engines.resume discoveryengine.engines.tune discoveryengine.engines.update discoveryengine.engines. updateEngineUserData` <sup>`discoveryengine.evaluations.*`</sup> `discoveryengine.evaluations.create discoveryengine.evaluations.get discoveryengine.evaluations.list discoveryengine.groundingConfigs.check discoveryengine.homepageDataConfigs. fetchDocuments` 

|Role|Permissions|
|---|---|
|| <sup>`discoveryengine.ideaForgeIdeas.*`</sup><br>`discoveryengine.ideaForgeIdeas.create`<br>`discoveryengine.ideaForgeIdeas.get`<br> <sup>`discoveryengine.ideaForgeInstances.*`</sup><br>`discoveryengine.ideaForgeInstances.get`<br>`discoveryengine.ideaForgeInstances.start`<br>`discoveryengine.ideaForgeInstances.stop`<br> <sup>`discoveryengine.identityMappingStores.*`</sup><br>`discoveryengine.identityMappingStores.`<br>`create`|
||`discoveryengine.identityMappingStores.`<br>`delete`|
||`discoveryengine.identityMappingStores.get`<br>`discoveryengine.identityMappingStores.`<br>`importIdentityMappings`|
||`discoveryengine.identityMappingStores.`<br>`list`|
||`discoveryengine.identityMappingStores.`<br>`listIdentityMappings`|
||`discoveryengine.identityMappingStores.`<br>`purgeIdentityMappings`<br> <sup>`discoveryengine.immersiveArtifacts.*`</sup><br>`discoveryengine.immersiveArtifacts.create`<br>`discoveryengine.immersiveArtifacts.delete`<br>`discoveryengine.immersiveArtifacts.export`<br>`discoveryengine.immersiveArtifacts.get`|
||`discoveryengine.immersiveArtifacts.list`<br>`discoveryengine.immersiveArtifacts.`<br>`navigate`<br>`discoveryengine.immersiveArtifacts.update`<br> <sup>`discoveryengine.licenseConfigs.*`</sup>|
||`discoveryengine.licenseConfigs.create`<br>`discoveryengine.licenseConfigs.get`<br>`discoveryengine.licenseConfigs.list`<br>`discoveryengine.licenseConfigs.update`<br>`discoveryengine.locations.`<br>`completeExternalIdentities`<br>`discoveryengine.locations.estimateDataSize`<br>`discoveryengine.locations.`<br>`exchangeAuthCredentials`<br>`discoveryengine.locations.fetchAgentCards`<br>`discoveryengine.locations.`<br>`getConnectorSource`<br>`discoveryengine.locations.`<br>`listConnectorSources`|

Role Permissions `discoveryengine.locations. setUpDataConnector` <sup>`discoveryengine.memories.*`</sup> `discoveryengine.memories.delete discoveryengine.memories.list discoveryengine.memories.retrieve discoveryengine.memories.update` <sup>`discoveryengine.models.*`</sup> `discoveryengine.models.create discoveryengine.models.delete discoveryengine.models.get discoveryengine.models.list discoveryengine.models.pause discoveryengine.models.resume discoveryengine.models.tune discoveryengine.models.update discoveryengine.notebooks.create discoveryengine.notebooks.list` <sup>`discoveryengine.notificationMessages.*`</sup> `discoveryengine.notificationMessages. ackAll discoveryengine.notificationMessages.list discoveryengine.notificationMessages. update` <sup>`discoveryengine.operations.*`</sup> `discoveryengine.operations.get discoveryengine.operations.list discoveryengine.podcasts.create discoveryengine.projectOverageConfigs.get discoveryengine.projects.get discoveryengine.projects.provision discoveryengine.projects. reportConsentChange discoveryengine.rankingConfigs.rank` <sup>`discoveryengine.sampleQueries.*`</sup> `discoveryengine.sampleQueries.create discoveryengine.sampleQueries.delete discoveryengine.sampleQueries.get discoveryengine.sampleQueries.import discoveryengine.sampleQueries.list discoveryengine.sampleQueries.update` <sup>`discoveryengine.sampleQuerySets.*`</sup> `discoveryengine.sampleQuerySets.create discoveryengine.sampleQuerySets.delete discoveryengine.sampleQuerySets.get discoveryengine.sampleQuerySets.list` 

|Role|Permissions|
|---|---|
||`discoveryengine.sampleQuerySets.update`<br> <sup>`discoveryengine.schemas.*`</sup><br>`discoveryengine.schemas.create`<br>`discoveryengine.schemas.delete`<br>`discoveryengine.schemas.get`<br>`discoveryengine.schemas.list`<br>`discoveryengine.schemas.preview`<br>`discoveryengine.schemas.update`<br>`discoveryengine.schemas.validate`<br> <sup>`discoveryengine.servingConfigs.*`</sup>|
||`discoveryengine.servingConfigs.answer`<br>`discoveryengine.servingConfigs.create`<br>`discoveryengine.servingConfigs.delete`|
||`discoveryengine.servingConfigs.get`<br>`discoveryengine.servingConfigs.list`<br>`discoveryengine.servingConfigs.recommend`<br>`discoveryengine.servingConfigs.search`<br>`discoveryengine.servingConfigs.update`<br> <sup>`discoveryengine.sessions.*`</sup>|
||`discoveryengine.sessions.addContextFile`<br>`discoveryengine.sessions.create`|
||`discoveryengine.sessions.delete`<br>`discoveryengine.sessions.downloadFile`<br>`discoveryengine.sessions.generateSummary`<br>`discoveryengine.sessions.get`<br>`discoveryengine.sessions.list`<br>`discoveryengine.sessions.`<br>`listSessionFileMetadata`|
||`discoveryengine.sessions.`<br>`recommendQuestions`<br>`discoveryengine.sessions.`<br>`removeContextFile`|
||`discoveryengine.sessions.search`<br>`discoveryengine.sessions.`<br>`selectContextFiles`|
||`discoveryengine.sessions.update`<br>`discoveryengine.sessions.uploadFile`<br> <sup>`discoveryengine.sharedContents.*`</sup><br>`discoveryengine.sharedContents.create`<br>`discoveryengine.sharedContents.delete`<br>`discoveryengine.sharedContents.get`<br>`discoveryengine.sharedContents.list`<br> <sup>`discoveryengine.siteSearchEngines.*`</sup>|
||`discoveryengine.siteSearchEngines.`<br>`batchVerifyTargetSites`|

Role Permissions `discoveryengine.siteSearchEngines. disableAdvancedSiteSearch discoveryengine.siteSearchEngines. enableAdvancedSiteSearch discoveryengine.siteSearchEngines. fetchDomainVerificationStatus discoveryengine.siteSearchEngines.get discoveryengine.siteSearchEngines. recrawlUris` <sup>`discoveryengine.sitemaps.*`</sup> `discoveryengine.sitemaps.create discoveryengine.sitemaps.delete discoveryengine.sitemaps.fetch` <sup>`discoveryengine.suggestionDenyListEntries.*`</sup> `discoveryengine. suggestionDenyListEntries.import discoveryengine. suggestionDenyListEntries.purge discoveryengine.targetSites.create discoveryengine.targetSites.delete discoveryengine.targetSites.get discoveryengine.targetSites.list discoveryengine.targetSites.update` <sup>`discoveryengine.userEvents.*`</sup> `discoveryengine.userEvents.create discoveryengine.userEvents.fetchStats discoveryengine.userEvents.import discoveryengine.userEvents.purge discoveryengine.userStores. batchUpdateUserLicenses discoveryengine.userStores.get discoveryengine.userStores.listUserLicenses` <sup>`discoveryengine.widgetConfigs.*`</sup> `discoveryengine.widgetConfigs.get discoveryengine.widgetConfigs.update resourcemanager.projects.get resourcemanager.projects.list` 

|Role|Permissions|
|---|---|
|Gemini Enterprise User<br>| <sup>`businessaicode.*`</sup>|
|(`roles/discoveryengine.agentspaceUser`)<br>Grants user-level access to Gemini Enterprise<br>resources.<br><br><br><br>|`businessaicode.locations.fetchQuotaStatus`<br>`businessaicode.locations.generateContent`<br>`businessaicode.locations.`<br>`queryConfiguration`<br>`businessaicode.locations.`<br>`selfAssignLicense`<br>`businessaicode.locations.sendTelemetry`<br> <sup>`cloudaicompanion.companions.*`</sup><br>`cloudaicompanion.companions.generateChat`<br>`cloudaicompanion.companions.generateCode`<br>`cloudaicompanion.entitlements.get`<br> <sup>`cloudaicompanion.instances.*`</sup><br>`cloudaicompanion.instances.completeCode`<br>`cloudaicompanion.instances.completeTask`<br>`cloudaicompanion.instances.exportMetrics`<br>`cloudaicompanion.instances.generateCode`<br>`cloudaicompanion.instances.generateText`<br>`cloudaicompanion.instances.`<br>`queryEffectiveSetting`<br>`cloudaicompanion.instances.`<br>`queryEffectiveSettingBindings`<br>`cloudaicompanion.licenses.selfAssign`<br>`cloudaicompanion.operations.get`<br>`cloudaicompanion.topics.create`<br>`discoveryengine.accounts.create`<br> <sup>`discoveryengine.agentFiles.*`</sup><br>`discoveryengine.agentFiles.delete`<br>`discoveryengine.agentFiles.download`<br>`discoveryengine.agentFiles.import`<br>`discoveryengine.agentFiles.list`<br>`discoveryengine.agentFiles.upload`<br> <sup>`discoveryengine.agentIamProposals.*`</sup><br>`discoveryengine.agentIamProposals.create`<br>`discoveryengine.agentIamProposals.delete`<br>`discoveryengine.agentIamProposals.get`<br>`discoveryengine.agentIamProposals.list`<br>`discoveryengine.agents.create`<br>`discoveryengine.agents.delete`<br>`discoveryengine.agents.get`<br>`discoveryengine.agents.getAgentView`<br>`discoveryengine.agents.list`<br>`discoveryengine.agents.`<br>`listAvailableAgentViews`<br>`discoveryengine.agents.requestReview`|

Role Permissions `discoveryengine.agents.update discoveryengine.answers.get discoveryengine.assistAnswers.get discoveryengine.assistants.assist discoveryengine.authorizations. storeUserAuthorization discoveryengine.cannedQueries. listActiveCannedQueryUserViews discoveryengine.collections.get discoveryengine.completionConfigs. completeQuery discoveryengine.completionConfigs. removeSuggestion discoveryengine.dataConnectors. acquireAccessToken discoveryengine.dataConnectors. acquireAndStoreRefreshToken discoveryengine.dataConnectors. buildActionInvocation discoveryengine.dataConnectors. checkRefreshToken discoveryengine.dataConnectors. executeAction discoveryengine.dataConnectors. queryAvailableActions discoveryengine.dataStores.get discoveryengine.devToolsConfigs.get discoveryengine.engines. createEngineUserData discoveryengine.engines.generateMemories discoveryengine.engines. generatePersonalContext discoveryengine.engines.get discoveryengine.engines.getEngineUserData discoveryengine.engines.getPersonalContext discoveryengine.engines. updateEngineUserData discoveryengine.homepageDataConfigs. fetchDocuments` <sup>`discoveryengine.ideaForgeIdeas.*`</sup> `discoveryengine.ideaForgeIdeas.create discoveryengine.ideaForgeIdeas.get` <sup>`discoveryengine.ideaForgeInstances.*`</sup> `discoveryengine.ideaForgeInstances.get discoveryengine.ideaForgeInstances.start discoveryengine.ideaForgeInstances.stop` 

Role Permissions <sup>`discoveryengine.immersiveArtifacts.*`</sup> `discoveryengine.immersiveArtifacts.create discoveryengine.immersiveArtifacts.delete discoveryengine.immersiveArtifacts.export discoveryengine.immersiveArtifacts.get discoveryengine.immersiveArtifacts.list discoveryengine.immersiveArtifacts. navigate discoveryengine.immersiveArtifacts.update discoveryengine.locations. buildAuthorizationUrl discoveryengine.locations. completeExternalIdentities discoveryengine.locations.fetchAgentCards` <sup>`discoveryengine.memories.*`</sup> `discoveryengine.memories.delete discoveryengine.memories.list discoveryengine.memories.retrieve discoveryengine.memories.update discoveryengine.notebooks.create discoveryengine.notebooks.list` <sup>`discoveryengine.notificationMessages.*`</sup> `discoveryengine.notificationMessages. ackAll discoveryengine.notificationMessages.list discoveryengine.notificationMessages. update discoveryengine.servingConfigs.answer discoveryengine.servingConfigs.recommend discoveryengine.servingConfigs.search` <sup>`discoveryengine.sessions.*`</sup> `discoveryengine.sessions.addContextFile discoveryengine.sessions.create discoveryengine.sessions.delete discoveryengine.sessions.downloadFile discoveryengine.sessions.generateSummary discoveryengine.sessions.get discoveryengine.sessions.list discoveryengine.sessions. listSessionFileMetadata discoveryengine.sessions. recommendQuestions discoveryengine.sessions. removeContextFile discoveryengine.sessions.search` 

|Role|Permissions|
|---|---|
||`discoveryengine.sessions.`<br>`selectContextFiles`|
||`discoveryengine.sessions.update`<br>`discoveryengine.sessions.uploadFile`<br> <sup>`discoveryengine.sharedContents.*`</sup><br>`discoveryengine.sharedContents.create`<br>`discoveryengine.sharedContents.delete`<br>`discoveryengine.sharedContents.get`<br>`discoveryengine.sharedContents.list`<br>`discoveryengine.userEvents.create`|
|| <sup>`discoveryengine.users.*`</sup>|
||`discoveryengine.users.get`|
||`discoveryengine.users.update`|
||`discoveryengine.widgetConfigs.get`<br>`geminicloudassist.agents.invoke`<br>`monitoring.timeSeries.list`<br>`resourcemanager.projects.get`<br>`resourcemanager.projects.list`<br>`serviceusage.consumerpolicy.analyze`<br>`serviceusage.consumerpolicy.get`|
||`serviceusage.contentsecuritypolicy.get`<br>`serviceusage.effectivemcppolicy.get`<br>`serviceusage.effectivepolicy.get`|
|| <sup>`serviceusage.groups.*`</sup>|
||`serviceusage.groups.list`|
||`serviceusage.groups.listExpandedMembers`<br>`serviceusage.groups.listMembers`<br>`serviceusage.mcppolicy.get`<br>`serviceusage.operations.get`<br>`serviceusage.quotas.get`<br>`serviceusage.services.get`|
||`serviceusage.services.list`|
||`serviceusage.services.use`|
||`serviceusage.values.test`|

|Role|Permissions|
|---|---|
|Gemini Enterprise Restricted User<br>(`roles/`<br>`discoveryengine.agentspaceRestrictedUser`)<br>Grants restricted user-level access to Gemini<br>Enterprise resources, for fine-grained control over<br>multiple Gemini Enterprise instances in the same<br>project. Principals with this role will need to be<br>granted an unrestricted user-level role (e.g.<br>/agentspaceUser) on an Engine policy in order to<br>use Gemini Enterprise.<br>|i<br>`discoveryengine.accounts.create`<br>`discoveryengine.authorizations.`<br>`storeUserAuthorization`<br>`discoveryengine.collections.get`<br>`discoveryengine.dataConnectors.`<br>`acquireAccessToken`<br>`discoveryengine.dataConnectors.`<br>`acquireAndStoreRefreshToken`<br>`discoveryengine.dataConnectors.`<br>`buildActionInvocation`<br>`discoveryengine.dataConnectors.`<br>`checkRefreshToken`<br>`discoveryengine.dataConnectors.`<br>`executeAction`<br>`discoveryengine.dataConnectors.`<br>`queryAvailableActions`<br>`discoveryengine.dataStores.get`<br>`discoveryengine.devToolsConfigs.get`<br>`discoveryengine.locations.`<br>`buildAuthorizationUrl`<br>`discoveryengine.locations.`<br>`completeExternalIdentities`<br>`discoveryengine.locations.fetchAgentCards`<br>`discoveryengine.notebooks.create`<br>`discoveryengine.notebooks.list`<br>`discoveryengine.userEvents.create`<br> <sup>`discoveryengine.users.*`</sup><br>`discoveryengine.users.get`<br>`discoveryengine.users.update`<br>`resourcemanager.projects.get`<br>`resourcemanager.projects.list`|

Role Permissions Gemini Enterprise Viewer `discoveryengine.aclConfigs.get` ( `roles/discoveryengine.agentspaceViewer` ) `discoveryengine.agentFiles.list discoveryengine.agents.get` Grants access to view the details of Gemini `discoveryengine.agents.getAgentView` Enterprise resources. `discoveryengine.agents.getIamPolicy discoveryengine.agents.list discoveryengine.agents. listAvailableAgentViews discoveryengine.alertPolicies.get` <sup>`discoveryengine.analytics.*`</sup> `discoveryengine.analytics. acquireDashboardSession discoveryengine.analytics. refreshDashboardSessionTokens discoveryengine.answers.get discoveryengine.assistAnswers.get discoveryengine.assistants.get discoveryengine.assistants.list` <sup>`discoveryengine.branches.*`</sup> `discoveryengine.branches.get discoveryengine.branches.list discoveryengine.cannedQueries.get discoveryengine.cannedQueries.list discoveryengine.cannedQueries. listActiveCannedQueryUserViews discoveryengine.cmekConfigs.get discoveryengine.cmekConfigs.list discoveryengine.collections.get discoveryengine.collections.list discoveryengine.completionConfigs. completeQuery discoveryengine.completionConfigs.get discoveryengine.connectorRuns.list discoveryengine.controls.get discoveryengine.controls.list discoveryengine.conversations.converse discoveryengine.conversations.get discoveryengine.conversations.list discoveryengine.dataConnectors. buildActionInvocation discoveryengine.dataConnectors. checkRefreshToken discoveryengine.dataConnectors.get discoveryengine.dataConnectors. queryAvailableActions discoveryengine.dataStores.completeQuery` 

Role Permissions `discoveryengine.dataStores.get discoveryengine.dataStores.list discoveryengine.dataStores.listCustomModels discoveryengine.devToolsConfigs.get discoveryengine.documentProcessingConfigs. get discoveryengine.documents. batchGetDocumentsMetadata discoveryengine.documents.get discoveryengine.documents.list discoveryengine.engines.get discoveryengine.engines.getIamPolicy discoveryengine.engines.getPersonalContext discoveryengine.engines.list discoveryengine.evaluations.get discoveryengine.evaluations.list discoveryengine.groundingConfigs.check discoveryengine.homepageDataConfigs. fetchDocuments discoveryengine.ideaForgeIdeas.get discoveryengine.ideaForgeInstances.get discoveryengine.identityMappingStores.get discoveryengine.identityMappingStores.list discoveryengine.identityMappingStores. listIdentityMappings discoveryengine.immersiveArtifacts.export discoveryengine.immersiveArtifacts.get discoveryengine.immersiveArtifacts.list discoveryengine.locations. completeExternalIdentities discoveryengine.locations.fetchAgentCards discoveryengine.locations. getConnectorSource discoveryengine.locations. listConnectorSources discoveryengine.memories.list discoveryengine.memories.retrieve discoveryengine.models.get discoveryengine.models.list discoveryengine.notebooks.list discoveryengine.notificationMessages.list` <sup>`discoveryengine.operations.*`</sup> `discoveryengine.operations.get discoveryengine.operations.list discoveryengine.projectOverageConfigs.get discoveryengine.projects.get` 

Role Permissions `discoveryengine.rankingConfigs.rank discoveryengine.sampleQueries.get discoveryengine.sampleQueries.list discoveryengine.sampleQuerySets.get discoveryengine.sampleQuerySets.list discoveryengine.schemas.get discoveryengine.schemas.list discoveryengine.schemas.preview discoveryengine.schemas.validate discoveryengine.servingConfigs.answer discoveryengine.servingConfigs.get discoveryengine.servingConfigs.list discoveryengine.servingConfigs.recommend discoveryengine.servingConfigs.search discoveryengine.sessions.downloadFile discoveryengine.sessions.generateSummary discoveryengine.sessions.get discoveryengine.sessions.list discoveryengine.sessions. listSessionFileMetadata discoveryengine.sessions.recommendQuestions discoveryengine.sharedContents.get discoveryengine.sharedContents.list discoveryengine.siteSearchEngines. fetchDomainVerificationStatus discoveryengine.siteSearchEngines.get discoveryengine.sitemaps.fetch discoveryengine.targetSites.get discoveryengine.targetSites.list discoveryengine.userEvents.fetchStats discoveryengine.userStores.get discoveryengine.widgetConfigs.get resourcemanager.projects.get resourcemanager.projects.list` 

Role Permissions Discovery Engine Viewer `discoveryengine.aclConfigs.get` ( `roles/discoveryengine.viewer` ) `discoveryengine.agentFiles.list discoveryengine.agents.get` Grants read access to all discovery engine `discoveryengine.agents.getAgentView` resources. `discoveryengine.agents.getIamPolicy discoveryengine.agents.list discoveryengine.agents. listAvailableAgentViews discoveryengine.alertPolicies.get` <sup>`discoveryengine.analytics.*`</sup> `discoveryengine.analytics. acquireDashboardSession discoveryengine.analytics. refreshDashboardSessionTokens discoveryengine.answers.get discoveryengine.assistAnswers.get discoveryengine.assistants.get discoveryengine.assistants.list` <sup>`discoveryengine.branches.*`</sup> `discoveryengine.branches.get discoveryengine.branches.list discoveryengine.cannedQueries.get discoveryengine.cannedQueries.list discoveryengine.cannedQueries. listActiveCannedQueryUserViews discoveryengine.cmekConfigs.get discoveryengine.cmekConfigs.list discoveryengine.collections.get discoveryengine.collections.list discoveryengine.completionConfigs. completeQuery discoveryengine.completionConfigs.get discoveryengine.connectorRuns.list discoveryengine.controls.get discoveryengine.controls.list discoveryengine.conversations.converse discoveryengine.conversations.get discoveryengine.conversations.list discoveryengine.dataConnectors. buildActionInvocation discoveryengine.dataConnectors. checkRefreshToken discoveryengine.dataConnectors.get discoveryengine.dataConnectors. queryAvailableActions discoveryengine.dataStores.completeQuery` 

Role Permissions `discoveryengine.dataStores.get discoveryengine.dataStores.list discoveryengine.dataStores.listCustomModels discoveryengine.devToolsConfigs.get discoveryengine.documentProcessingConfigs. get discoveryengine.documents. batchGetDocumentsMetadata discoveryengine.documents.get discoveryengine.documents.list discoveryengine.engines.get discoveryengine.engines.getIamPolicy discoveryengine.engines.getPersonalContext discoveryengine.engines.list discoveryengine.evaluations.get discoveryengine.evaluations.list discoveryengine.groundingConfigs.check discoveryengine.homepageDataConfigs. fetchDocuments discoveryengine.ideaForgeIdeas.get discoveryengine.ideaForgeInstances.get discoveryengine.identityMappingStores.get discoveryengine.identityMappingStores.list discoveryengine.identityMappingStores. listIdentityMappings discoveryengine.immersiveArtifacts.export discoveryengine.immersiveArtifacts.get discoveryengine.immersiveArtifacts.list discoveryengine.locations. completeExternalIdentities discoveryengine.locations.fetchAgentCards discoveryengine.locations. getConnectorSource discoveryengine.locations. listConnectorSources discoveryengine.memories.list discoveryengine.memories.retrieve discoveryengine.models.get discoveryengine.models.list discoveryengine.notebooks.list discoveryengine.notificationMessages.list` <sup>`discoveryengine.operations.*`</sup> `discoveryengine.operations.get discoveryengine.operations.list discoveryengine.projectOverageConfigs.get discoveryengine.projects.get` 

|Role|Permissions|
|---|---|
||`discoveryengine.rankingConfigs.rank`|
||`discoveryengine.sampleQueries.get`|
||`discoveryengine.sampleQueries.list`|
||`discoveryengine.sampleQuerySets.get`<br>`discoveryengine.sampleQuerySets.list`<br>`discoveryengine.schemas.get`|
||`discoveryengine.schemas.list`|
||`discoveryengine.schemas.preview`|
||`discoveryengine.schemas.validate`|
||`discoveryengine.servingConfigs.answer`|
||`discoveryengine.servingConfigs.get`|
||`discoveryengine.servingConfigs.list`|
||`discoveryengine.servingConfigs.recommend`|
||`discoveryengine.servingConfigs.search`|
||`discoveryengine.sessions.downloadFile`|
||`discoveryengine.sessions.generateSummary`|
||`discoveryengine.sessions.get`|
||`discoveryengine.sessions.list`|
||`discoveryengine.sessions.`<br>`listSessionFileMetadata`|
||`discoveryengine.sessions.recommendQuestions`|
||`discoveryengine.sharedContents.get`|
||`discoveryengine.sharedContents.list`|
||`discoveryengine.siteSearchEngines.`|
||`fetchDomainVerificationStatus`|
||`discoveryengine.siteSearchEngines.get`|
||`discoveryengine.sitemaps.fetch`|
||`discoveryengine.targetSites.get`|
||`discoveryengine.targetSites.list`|
||`discoveryengine.userEvents.fetchStats`|
||`discoveryengine.userStores.get`|
||`discoveryengine.widgetConfigs.get`|
||`resourcemanager.projects.get`|
||`resourcemanager.projects.list`|

### Manage Gemini Enterprise IAM

You can get and set IAM allow policies and IAM roles using the Google Cloud Console. For more information, see Manage access to projects, folders, and organizations (/iam/docs/granting-changing-revoking-access). 

### Grant permissions to admins

As a project owner, you can grant the `Gemini Enterprise Admin` , `Service Usage Consumer` , and `Logs Viewer` roles to the users who want to be administrators. 

Follow these steps to add the roles: 

1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=) 

2. Select the project. 

3. Click **Grant access** . 

4. In the **New principals** field, enter the user identifier. This is typically the email address for a Google Account or a user group. 

5. Add the roles: 

   - a. Click **Add another role** . 

   - b. In the **Select a role** list, select **Gemini Enterprise Admin** 

      - (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin). 

   - c. Repeat the steps a and b to add the **Service usage consumer** and **Logs viewer** roles. 

6. Click **Save** . 

Depending on the administrative task, also verify the following role bindings: 

- **Data connectors** : Grant `roles/discoveryengine.editor` to manage data connectors. When you authorize a connector for the first time in a project, you also need both the `discoveryengine.locations.setUpDataConnector` and `discoveryengine.locations.exchangeAuthCredentials` permissions. Both of these permissions are included in the `roles/discoveryengine.admin` role and in the `roles/discoveryengine.agentspaceAdmin` role. 

**License distribution** : Grant **Billing Account Administrator** 

( `roles/billing.admin` , which includes 

`discoveryengine.billingAccountLicenseConfigs.distribute` ) on the **Cloud Billing account** in addition to `roles/discoveryengine.agentspaceAdmin` on the project to distribute licenses (/gemini/enterprise/docs/licenses#before-you-begin). 

- **Service agent** : Ensure the Discovery Engine service agent ( `service-` _`PROJECT_NUMBER`_ `@gcp-sa-discoveryengine.iam.gserviceaccount.com` ) has `roles/discoveryengine.serviceAgent` on the project, or app creation fails with `Internal error encountered (Code 13)` . 

### Grant permissions to your users

This section describes how to grant your users the project-level roles that they need to access Gemini Enterprise apps. Depending on your access model, choose one of the following roles: 

- **Access all apps in the project** : Grant the Gemini Enterprise User 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) ( `roles/discoveryengine.agentspaceUser` ) role at the project level. 

**Access specific apps only** : Grant the Gemini Enterprise Restricted User 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceRestrictedUser) ( `roles/discoveryengine.agentspaceRestrictedUser` ) role at the project level, and then grant the Gemini Enterprise User 

(/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) ( `roles/discoveryengine.agentspaceUser` ) role on the individual apps. The Restricted User role doesn't grant access to any app on its own, so users can open only the apps where you grant them the Gemini Enterprise User role. For more information, see Configure access controls for apps (/gemini/enterprise/docs/iam-policy-for-apps). 

To grant the project-level role in the Google Cloud console, follow these steps: 

1. In the Google Cloud console, go to the **IAM** page. 

Go to IAM (https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=) 

2. Select the project. 

3. Click **Grant access** . 

4. In the **New principals** field, enter the user identifier. This is typically the email address for a Google Account, a user group, or the identifier for a user in a workforce identity pool. For details, see Principal identifiers for allow policies (/iam/docs/principal-identifiers#allow). 

5. Add the project-level role: 

   - a. Click **Add another role** . 

- b. In the **Select a role** list, select one of the following roles: 

   - To grant access across all apps in the project, select **Gemini Enterprise User** (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser). 

   - To restrict access to specific apps, select **Gemini Enterprise Restricted User** 

(/gemini/enterprise/docs/access- 

control#discoveryengine.agentspaceRestrictedUser) 

6. Click **Save** . 

7. If you granted the **Gemini Enterprise Restricted User** role, grant the **Gemini Enterprise User** ( `roles/discoveryengine.agentspaceUser` ) role on each individual app that the user needs to access. For step-by-step instructions, see Configure access controls for apps 

(/gemini/enterprise/docs/iam-policy-for-apps#manage-iam-policies-for-apps). 

**Note:** In addition to the IAM role, users need a license for Gemini Enterprise. See Get licenses for Gemini Enterprise (/gemini/enterprise/docs/licenses). 

To allow users to manage and share apps, grant them the Discovery Engine Viewer (/gemini/enterprise/docs/access-control#discoveryengine.viewer) ( `roles/discoveryengine.viewer` ) role. 

### What's next

- Learn how to manage access to projects, folders, and organizations 

- (/iam/docs/granting-changing-revoking-access). 

- Learn more about IAM (/iam/docs). 

- Learn more about basic roles (/iam/docs/roles-overview#basic). 

- Learn more about custom roles (/iam/docs/understanding-custom-roles).
