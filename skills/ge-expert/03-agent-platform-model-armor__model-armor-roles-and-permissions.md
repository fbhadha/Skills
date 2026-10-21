# Agent Platform, Model Armor and data governance / Model Armor roles and permissions to Data governance and generative AI
Source: 03-Agent-Platform-Model-Armor-and-data-governance.pdf, pages 110-151, extracted 2026-10-18

Contains:
- Model Armor roles and permissions (pages 110-136) https://docs.cloud.google.com/model-armor/access-control/roles-permissions
- Best practices for scaling and high traffic (pages 137-138) https://docs.cloud.google.com/model-armor/best-practices
- Gemini Enterprise Agent Platform and zero data retention (pages 139-149) https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention
- Data governance and generative AI (pages 150-151) https://docs.cloud.google.com/generative-ai-app-builder/docs/data-governance

## Model Armor roles and permissions

URL: https://docs.cloud.google.com/model-armor/access-control/roles-permissions

This page lists all the IAM roles and permissions for Model Armor. 

### Model Armor roles

Enter a role or permission 

7 results 

|Role||Permissions|
|---|---|---|
|Model Armor Admin<br>(`roles/modelarmor.admin`)<br>Grants full access to all modelarmor res<br>Intended for administrators & owners.|ources<br><br> <br> <br><br>|.<br>`modelarmor.callouts.invoke`<br> <sup>`modelarmor.locations.*`</sup><br>`modelarmor.locations.get`<br>`modelarmor.locations.list`<br> <sup>`modelarmor.templates.*`</sup><br>`modelarmor.templates.create`<br>`modelarmor.templates.delete`<br>`modelarmor.templates.get`<br>`modelarmor.templates.list`<br>`modelarmor.templates.update`<br>`modelarmor.templates.`<br>`useToSanitizeInput`<br>`modelarmor.templates.`<br>`useToSanitizeModelResponse`<br>`modelarmor.templates.`<br>`useToSanitizeOutput`<br>`modelarmor.templates.`<br>`useToSanitizeUserPrompt`<br>`modelarmor.templates.`<br>`useToStreamSanitizeModelResponse`<br>`modelarmor.templates.`<br>`useToStreamSanitizeUserPrompt`<br>`resourcemanager.projects.get`<br>`resourcemanager.projects.list`|

|Role||Permissions|
|---|---|---|
|Model Armor Editor<br>(`roles/modelarmor.editor`)<br>Grants access to create and update all m<br>armor resources. Intended for editors.|odel<br><br>|`modelarmor.callouts.invoke`<br>`modelarmor.floorSettings.`<br>`computeEffectiveFloorSetting`<br>`modelarmor.floorSettings.get`<br> <sup>`modelarmor.locations.*`</sup><br>`modelarmor.locations.get`<br>`modelarmor.locations.list`<br> <sup>`modelarmor.templates.*`</sup><br>`modelarmor.templates.create`<br>`modelarmor.templates.delete`<br>`modelarmor.templates.get`<br>`modelarmor.templates.list`<br>`modelarmor.templates.update`<br>`modelarmor.templates.`<br>`useToSanitizeInput`<br>`modelarmor.templates.`<br>`useToSanitizeModelResponse`<br>`modelarmor.templates.`<br>`useToSanitizeOutput`<br>`modelarmor.templates.`<br>`useToSanitizeUserPrompt`<br>`modelarmor.templates.`<br>`useToStreamSanitizeModelResponse`<br>`modelarmor.templates.`<br>`useToStreamSanitizeUserPrompt`<br>`resourcemanager.projects.get`<br>`resourcemanager.projects.list`|
|Model Armor Viewer<br>(`roles/modelarmor.viewer`)<br>Grants read access to all model armor<br>resources. Intended for viewers.||<sup>`modelarmor.locations.*`</sup><br>`modelarmor.locations.get`<br>`modelarmor.locations.list`<br>`modelarmor.templates.get`<br>`modelarmor.templates.list`<br>`resourcemanager.projects.get`<br>`resourcemanager.projects.list`|

|Role||Permissions|
|---|---|---|
|Model Armor Callout User<sup>Beta</sup>||`modelarmor.callouts.invoke`|
|(`roles/modelarmor.calloutUser`)<br>||<sup>`modelarmor.locations.*`</sup><br>`modelarmor.locations.get`|
|Grants access to use Model Armor Callout||`modelarmor.locations.list`|
|service. Intended for users & applications||`resourcemanager.projects.get`|
|which plan to use Model Armor Callout servi|ce|.<br>`resourcemanager.projects.list`|

|Model Armor Floor Setting Admin<br>(`roles/modelarmor.floorSettingsAdmin`)<br>Grants full access to all Model Armor Floor<br>Setting resources. Intended for administrators<br>& owners.<br> <br>|<sup>`modelarmor.floorSettings.*`</sup><br>`modelarmor.floorSettings.`<br>`computeEffectiveFloorSetting`<br>`modelarmor.floorSettings.get`<br>`modelarmor.floorSettings.update`<br> <sup>`modelarmor.locations.*`</sup><br>`modelarmor.locations.get`<br>`modelarmor.locations.list`<br>`resourcemanager.folders.get`<br>`resourcemanager.folders.list`<br>`resourcemanager.organizations.get`<br>`resourcemanager.projects.get`<br>`resourcemanager.projects.list`|
|---|---|
|Model Armor Floor Setting Viewer<br>(`roles/modelarmor.floorSettingsViewer`)<br>Grants read access to all Model Armor Floor<br>Setting resources. Intended for viewers.<br>|`modelarmor.floorSettings.get`<br> <sup>`modelarmor.locations.*`</sup><br>`modelarmor.locations.get`<br>`modelarmor.locations.list`<br>`resourcemanager.folders.get`<br>`resourcemanager.folders.list`<br>`resourcemanager.organizations.get`<br>`resourcemanager.projects.get`<br>`resourcemanager.projects.list`|

Role Permissions Model Armor User `modelarmor.callouts.invoke` ( `roles/modelarmor.user` ) <sup>`modelarmor.locations.*`</sup> `modelarmor.locations.get` Grants access to sanitize APIs for templates, to `modelarmor.locations.list` use and test topics, and to use Model Armor `modelarmor.templates.useToSanitizeInput` Callout service. Intended for users & `modelarmor.templates.` applications which plan to use a template, `useToSanitizeModelResponse` topic, or callout service for sanitization. `modelarmor.templates.useToSanitizeOutput modelarmor.templates. useToSanitizeUserPrompt modelarmor.templates. useToStreamSanitizeModelResponse modelarmor.templates. useToStreamSanitizeUserPrompt resourcemanager.projects.get resourcemanager.projects.list` 

#### Service agent roles

Service agent roles should only be granted to service agents (/iam/docs/service-agents). 

Enter a role or permission 

1 result 

|Role|Permissions|
|---|---|
|Model Armor Service Agent<br>(`roles/modelarmor.serviceAgent`)<br>Gives Model Armor Service Account permis<br>to make DLP calls.<br>Warning: Do not grant service agent role<br>any principals except<br>service agents<br>(/iam/docs/service-agents).<br>|sion<br>s to<br>`dlp.analyzeRiskTemplates.get`<br>`dlp.analyzeRiskTemplates.list`<br>`dlp.deidentifyTemplates.get`<br>`dlp.deidentifyTemplates.list`<br>`dlp.inspectFindings.list`<br>`dlp.inspectTemplates.get`<br>`dlp.inspectTemplates.list`<br>`dlp.jobTriggers.get`<br>`dlp.jobTriggers.list`<br>`dlp.jobs.get`<br>`dlp.jobs.list`<br>`dlp.kms.encrypt`<br> <sup>`dlp.locations.*`</sup><br>`dlp.locations.get`<br>`dlp.locations.list`<br>`dlp.storedInfoTypes.get`<br>`dlp.storedInfoTypes.list`<br>`serviceusage.services.use`|

### Model Armor permissions

Enter a permission 

17 results 

Permission Included in roles `modelarmor.callouts.invoke` Admin (/iam/docs/roles-overview#basic) ( `roles/ admin` ) Owner (/iam/docs/roles-overview#basic) ( `roles/ owner` ) Writer (/iam/docs/roles-overview#basic) ( `roles/ writer` ) Editor (/iam/docs/roles-overview#basic) ( `roles/ editor` ) Model Armor Admin (/iam/docs/rolespermissions/modelarmor#modelarmor.admin) ( `roles/modelarmor.admin` ) Model Armor Editor (/iam/docs/rolespermissions/modelarmor#modelarmor.editor) ( `roles/modelarmor.editor` ) Security Center Admin (/iam/docs/rolespermissions/securitycenter#securitycenter.admin) ( `roles/securitycenter.admin` ) Model Armor Callout User (/iam/docs/rolespermissions/modelarmor#modelarmor.calloutUser) ( `roles/modelarmor.calloutUser` ) Model Armor User (/iam/docs/rolespermissions/modelarmor#modelarmor.user) ( `roles/modelarmor.user` ) 

<sup>Service agent roles</sup> 

Warning: Don't grant service agent roles to any principals except service agents (/iam/docs/service-agents). 

Vertex AI Reasoning Engine Service Agent (/iam/docs/rolespermissions/aiplatform#aiplatform.reasoningEngin eServiceAgent) 

|Permission|Included in roles|
|---|---|
||(`roles/`<br>`aiplatform.reasoningEngineServiceAgent`)|
|`modelarmor.floorSettings.`<br>`computeEffectiveFloorSetting`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)|
||Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)|
||Reader(/iam/docs/roles-overview#basic) (`roles/`<br>`reader`)<br>Viewer(/iam/docs/roles-overview#basic) (`roles/`<br>`viewer`)|
||Model Armor Editor<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)|
||Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)|
||Support User<br>(/iam/docs/roles-<br>permissions/jobfunctions#iam.supportUser)<br>(`roles/iam.supportUser`)|
||Model Armor Floor Setting Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.floorSettings<br>Admin)<br>(`roles/modelarmor.floorSettingsAdmin`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.floorSettings.get`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)|
||Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)|
||Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)|
||Reader(/iam/docs/roles-overview#basic) (`roles/`<br>`reader`)|
||Viewer(/iam/docs/roles-overview#basic) (`roles/`<br>`viewer`)|
||Model Armor Editor<br>(/iam/docs/roles-|
||permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)|
||Security Center Admin<br>(/iam/docs/roles-|
||permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)<br>Support User<br>(/iam/docs/roles-<br>permissions/jobfunctions#iam.supportUser)<br>(`roles/iam.supportUser`)|
||Model Armor Floor Setting Admin<br>(/iam/docs/roles-|
||permissions/modelarmor#modelarmor.floorSettings<br>Admin)<br>(`roles/modelarmor.floorSettingsAdmin`)|
||Model Armor Floor Setting Viewer<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.floorSettings<br>Viewer)|
||(`roles/modelarmor.floorSettingsViewer`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.floorSettings.`<br>`update`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)|
||Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)|
||Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)|
||Model Armor Floor Setting Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.floorSettings<br>Admin)<br>(`roles/modelarmor.floorSettingsAdmin`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.locations.get`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)|
||Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)<br>Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)|
||Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Reader(/iam/docs/roles-overview#basic) (`roles/`<br>`reader`)|
||Viewer(/iam/docs/roles-overview#basic) (`roles/`<br>`viewer`)|
||Model Armor Admin<br>(/iam/docs/roles-|
||permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)|
||Model Armor Editor<br>(/iam/docs/roles-|
||permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)|
||Model Armor Viewer|
||(/iam/docs/roles-|
||permissions/modelarmor#modelarmor.viewer)<br>(`roles/modelarmor.viewer`)|
||Security Center Admin<br>(/iam/docs/roles-|
||permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)|
||Support User<br>(/iam/docs/roles-|
||permissions/jobfunctions#iam.supportUser)<br>(`roles/iam.supportUser`)|
||Model Armor Callout User<br>(/iam/docs/roles-|
||permissions/modelarmor#modelarmor.calloutUser)<br>(`roles/modelarmor.calloutUser`)|

Permission Included in roles Model Armor Floor Setting Admin (/iam/docs/rolespermissions/modelarmor#modelarmor.floorSettings Admin) ( `roles/modelarmor.floorSettingsAdmin` ) Model Armor Floor Setting Viewer (/iam/docs/rolespermissions/modelarmor#modelarmor.floorSettings Viewer) ( `roles/modelarmor.floorSettingsViewer` ) Model Armor User (/iam/docs/rolespermissions/modelarmor#modelarmor.user) ( `roles/modelarmor.user` ) <sup>Service agent roles</sup> Warning: Don't grant service agent roles to any principals except service agents (/iam/docs/service-agents). Vertex AI Reasoning Engine Service Agent (/iam/docs/rolespermissions/aiplatform#aiplatform.reasoningEngin eServiceAgent) ( `roles/ aiplatform.reasoningEngineServiceAgent` ) 

Permission Included in roles `modelarmor.locations.list` Admin (/iam/docs/roles-overview#basic) ( `roles/ admin` ) Owner (/iam/docs/roles-overview#basic) ( `roles/ owner` ) Writer (/iam/docs/roles-overview#basic) ( `roles/ writer` ) Editor (/iam/docs/roles-overview#basic) ( `roles/ editor` ) Reader (/iam/docs/roles-overview#basic) ( `roles/ reader` ) Viewer (/iam/docs/roles-overview#basic) ( `roles/ viewer` ) Security Admin (/iam/docs/rolespermissions/iam#iam.securityAdmin) ( `roles/iam.securityAdmin` ) Security Reviewer (/iam/docs/rolespermissions/iam#iam.securityReviewer) ( `roles/iam.securityReviewer` ) Model Armor Admin (/iam/docs/rolespermissions/modelarmor#modelarmor.admin) ( `roles/modelarmor.admin` ) Model Armor Editor (/iam/docs/rolespermissions/modelarmor#modelarmor.editor) ( `roles/modelarmor.editor` ) Model Armor Viewer (/iam/docs/rolespermissions/modelarmor#modelarmor.viewer) ( `roles/modelarmor.viewer` ) Security Center Admin (/iam/docs/rolespermissions/securitycenter#securitycenter.admin) ( `roles/securitycenter.admin` ) Security Auditor (/iam/docs/rolespermissions/jobfunctions#iam.securityAuditor) 

Permission Included in roles ( `roles/iam.securityAuditor` ) Support User (/iam/docs/rolespermissions/jobfunctions#iam.supportUser) ( `roles/iam.supportUser` ) Model Armor Callout User (/iam/docs/rolespermissions/modelarmor#modelarmor.calloutUser) ( `roles/modelarmor.calloutUser` ) Model Armor Floor Setting Admin (/iam/docs/rolespermissions/modelarmor#modelarmor.floorSettings Admin) ( `roles/modelarmor.floorSettingsAdmin` ) Model Armor Floor Setting Viewer (/iam/docs/rolespermissions/modelarmor#modelarmor.floorSettings Viewer) ( `roles/modelarmor.floorSettingsViewer` ) Model Armor User (/iam/docs/rolespermissions/modelarmor#modelarmor.user) ( `roles/modelarmor.user` ) <sup>Service agent roles</sup> 

Warning: Don't grant service agent roles to any principals except service agents (/iam/docs/service-agents). 

Vertex AI Reasoning Engine Service Agent 

(/iam/docs/rolespermissions/aiplatform#aiplatform.reasoningEngin eServiceAgent) ( `roles/ aiplatform.reasoningEngineServiceAgent` ) 

|Permission|Included in roles|
|---|---|
|`modelarmor.templates.create`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)<br>Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)<br>Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)|
||<sup>Service agent roles</sup>|
||Warning: Don't grant service agent roles to any<br>principals except<br>service agents<br>(/iam/docs/service-agents).|
||Discovery Engine Service Agent<br>(/iam/docs/roles-<br>permissions/discoveryengine#discoveryengine.ser<br>viceAgent)<br>(`roles/discoveryengine.serviceAgent`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.templates.delete`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)<br>Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)<br>Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)|
||<sup>Service agent roles</sup>|
||Warning: Don't grant service agent roles to any<br>principals except<br>service agents<br>(/iam/docs/service-agents).|
||Discovery Engine Service Agent<br>(/iam/docs/roles-<br>permissions/discoveryengine#discoveryengine.ser<br>viceAgent)<br>(`roles/discoveryengine.serviceAgent`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.templates.get`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)<br>Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Reader(/iam/docs/roles-overview#basic) (`roles/`<br>`reader`)<br>Viewer(/iam/docs/roles-overview#basic) (`roles/`<br>`viewer`)|
||Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)<br>Model Armor Viewer<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.viewer)<br>(`roles/modelarmor.viewer`)<br>Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)<br>Support User<br>(/iam/docs/roles-<br>permissions/jobfunctions#iam.supportUser)<br>(`roles/iam.supportUser`)|
||<sup>Service agent roles</sup>|

Warning: Don't grant service agent roles to any principals except service agents (/iam/docs/service-agents). 

Permission Included in roles Discovery Engine Service Agent (/iam/docs/rolespermissions/discoveryengine#discoveryengine.ser viceAgent) ( `roles/discoveryengine.serviceAgent` ) 

Permission Included in roles `modelarmor.templates.list` Admin (/iam/docs/roles-overview#basic) ( `roles/ admin` ) Owner (/iam/docs/roles-overview#basic) ( `roles/ owner` ) Writer (/iam/docs/roles-overview#basic) ( `roles/ writer` ) Editor (/iam/docs/roles-overview#basic) ( `roles/ editor` ) Reader (/iam/docs/roles-overview#basic) ( `roles/ reader` ) Viewer (/iam/docs/roles-overview#basic) ( `roles/ viewer` ) Security Admin (/iam/docs/rolespermissions/iam#iam.securityAdmin) ( `roles/iam.securityAdmin` ) Security Reviewer (/iam/docs/rolespermissions/iam#iam.securityReviewer) ( `roles/iam.securityReviewer` ) Model Armor Admin (/iam/docs/rolespermissions/modelarmor#modelarmor.admin) ( `roles/modelarmor.admin` ) Model Armor Editor (/iam/docs/rolespermissions/modelarmor#modelarmor.editor) ( `roles/modelarmor.editor` ) Model Armor Viewer (/iam/docs/rolespermissions/modelarmor#modelarmor.viewer) ( `roles/modelarmor.viewer` ) Security Center Admin (/iam/docs/rolespermissions/securitycenter#securitycenter.admin) ( `roles/securitycenter.admin` ) Security Auditor (/iam/docs/rolespermissions/jobfunctions#iam.securityAuditor) 

Permission Included in roles ( `roles/iam.securityAuditor` ) Support User (/iam/docs/rolespermissions/jobfunctions#iam.supportUser) ( `roles/iam.supportUser` ) 

<sup>Service agent roles</sup> 

Warning: Don't grant service agent roles to any principals except service agents (/iam/docs/service-agents). 

Discovery Engine Service Agent (/iam/docs/rolespermissions/discoveryengine#discoveryengine.ser viceAgent) ( `roles/discoveryengine.serviceAgent` ) 

|Permission|Included in roles|
|---|---|
|`modelarmor.templates.update`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)<br>Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)<br>Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)|
||<sup>Service agent roles</sup>|
||Warning: Don't grant service agent roles to any<br>principals except<br>service agents<br>(/iam/docs/service-agents).|
||Discovery Engine Service Agent<br>(/iam/docs/roles-<br>permissions/discoveryengine#discoveryengine.ser<br>viceAgent)<br>(`roles/discoveryengine.serviceAgent`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.templates.useTo`<br>`SanitizeInput`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)|
||Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)|
||Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-|
||permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)|
||Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)|
||Model Armor User<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.user)<br>(`roles/modelarmor.user`)|
||<sup>Service agent roles</sup>|
||Warning: Don't grant service agent roles to any<br>principals except<br>service agents<br>(/iam/docs/service-agents).|
||Vertex AI Reasoning Engine Service Agent<br>(/iam/docs/roles-<br>permissions/aiplatform#aiplatform.reasoningEngin<br>eServiceAgent)<br>(`roles/`<br>`aiplatform.reasoningEngineServiceAgent`)|

Permission Included in roles `modelarmor.templates.useTo` Admin (/iam/docs/roles-overview#basic) ( `roles/ SanitizeModelResponse admin` ) Owner (/iam/docs/roles-overview#basic) ( `roles/ owner` ) Writer (/iam/docs/roles-overview#basic) ( `roles/ writer` ) Editor (/iam/docs/roles-overview#basic) ( `roles/ editor` ) Model Armor Admin (/iam/docs/rolespermissions/modelarmor#modelarmor.admin) ( `roles/modelarmor.admin` ) Model Armor Editor (/iam/docs/rolespermissions/modelarmor#modelarmor.editor) ( `roles/modelarmor.editor` ) Security Center Admin (/iam/docs/rolespermissions/securitycenter#securitycenter.admin) ( `roles/securitycenter.admin` ) Model Armor User (/iam/docs/rolespermissions/modelarmor#modelarmor.user) ( `roles/modelarmor.user` ) <sup>Service agent roles</sup> 

Warning: Don't grant service agent roles to any principals except service agents (/iam/docs/service-agents). 

Vertex AI Reasoning Engine Service Agent (/iam/docs/rolespermissions/aiplatform#aiplatform.reasoningEngin eServiceAgent) ( `roles/ aiplatform.reasoningEngineServiceAgent` ) 

|Permission|Included in roles|
|---|---|
||Discovery Engine Service Agent<br>(/iam/docs/roles-|
||permissions/discoveryengine#discoveryengine.ser<br>viceAgent)|
||(`roles/discoveryengine.serviceAgent`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.templates.useTo`<br>`SanitizeOutput`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)|
||Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)|
||Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-|
||permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)|
||Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)|
||Model Armor User<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.user)<br>(`roles/modelarmor.user`)|
||<sup>Service agent roles</sup>|
||Warning: Don't grant service agent roles to any<br>principals except<br>service agents<br>(/iam/docs/service-agents).|
||Vertex AI Reasoning Engine Service Agent<br>(/iam/docs/roles-<br>permissions/aiplatform#aiplatform.reasoningEngin<br>eServiceAgent)<br>(`roles/`<br>`aiplatform.reasoningEngineServiceAgent`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.templates.useTo`<br>`SanitizeUserPrompt`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)<br>Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)<br>Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)<br>Model Armor User<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.user)<br>(`roles/modelarmor.user`)|
||<sup>Service agent roles</sup>|

Warning: Don't grant service agent roles to any principals except service agents (/iam/docs/service-agents). 

Vertex AI Reasoning Engine Service Agent (/iam/docs/rolespermissions/aiplatform#aiplatform.reasoningEngin eServiceAgent) ( `roles/ aiplatform.reasoningEngineServiceAgent` ) 

|Permission|Included in roles|
|---|---|
||Discovery Engine Service Agent<br>(/iam/docs/roles-<br>permissions/discoveryengine#discoveryengine.ser<br>viceAgent)<br>(`roles/discoveryengine.serviceAgent`)|
|`modelarmor.templates.useTo`<br>`StreamSanitizeModelResponse`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)<br>Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)|
||Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)<br>Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)<br>Model Armor User<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.user)<br>(`roles/modelarmor.user`)|

|Permission|Included in roles|
|---|---|
|`modelarmor.templates.useTo`<br>`StreamSanitizeUserPrompt`|Admin(/iam/docs/roles-overview#basic) (`roles/`<br>`admin`)<br>Owner(/iam/docs/roles-overview#basic) (`roles/`<br>`owner`)<br>Writer(/iam/docs/roles-overview#basic) (`roles/`<br>`writer`)<br>Editor(/iam/docs/roles-overview#basic) (`roles/`<br>`editor`)<br>Model Armor Admin<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.admin)<br>(`roles/modelarmor.admin`)<br>Model Armor Editor<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.editor)<br>(`roles/modelarmor.editor`)<br>Security Center Admin<br>(/iam/docs/roles-<br>permissions/securitycenter#securitycenter.admin)<br>(`roles/securitycenter.admin`)<br>Model Armor User<br>(/iam/docs/roles-<br>permissions/modelarmor#modelarmor.user)<br>(`roles/modelarmor.user`)|

Last updated 2026-10-14 UTC. 



## Best practices for scaling and high traffic

URL: https://docs.cloud.google.com/model-armor/best-practices

As you scale your AI applications and encounter high traffic volumes, it's crucial to design for resilience and performance. This section outlines best practices for using Model Armor effectively in demanding environments. 

### Quotas and system limits

Model Armor includes quotas and system limits to ensure fair usage and system stability. 

- Request quota increases: If you anticipate higher traffic, contact Cloud Customer Care (https://cloud.google.com/support-hub) to request a Model Armor API quota adjustment. 

- Understand system limits: Design your application to handle these limits gracefully, potentially by chunking larger inputs if necessary. For specific values, see Quotas and system limits (/model-armor/quotas). 

### Design for high traffic and resilience

- Client-side retries with exponential backoff: Implement robust error handling in your clients. For errors that you can retry, for example, rate limits or server errors, use an exponential backoff strategy. This prevents overwhelming the service during transient issues. For more information, see Retry strategy (/model-armor/retry-strategy). 

- Caching strategies: If applicable, cache Model Armor responses for identical prompts, especially for common or less sensitive interactions. Be mindful of data freshness and security implications when caching. 

- Asynchronous processing: For non-interactive workloads, consider processing requests asynchronously. Queue requests and process them at a rate that respects API limits and smooths out traffic spikes. 

- Graceful degradation: Design your application to handle potential Model Armor unavailability or errors. Consider implementing a fallback mechanism or temporarily bypassing certain checks while logging the failure. 

### Optimize performance

- Minimize payload size: Only send the necessary data to Model Armor for analysis. Avoid unnecessarily large prompts or files. 

- Optimize template configuration: Configure your Model Armor templates to only include the filters and settings essential for your use case. Enabling unnecessary detectors can increase latency. 

- Keep the application, data, and requests in the same region: Deploy your application and use Model Armor endpoints in the same region to minimize network latency. For more information, see Model Armor locations (/model-armor/locations). 

### Monitoring and alerting

- Set up alerts: Configure alerts (/monitoring/alerts) in Cloud Monitoring to notify you when you are approaching quota limits or experiencing high error rates from the Model Armor API. 

- Analyze logs: Use Cloud Logging to analyze Model Armor usage patterns, errors, and performance metrics. Analyzing logs can help identify bottlenecks or areas for optimization. For more information, see Filter logs (/model-armor/configure-logging#filter-logs). 

Last updated 2026-10-13 UTC. 



## Gemini Enterprise Agent Platform and zero data retention

URL: https://docs.cloud.google.com/gemini-enterprise-agent-platform/resources/zero-data-retention

Google was the first in the industry to publish an AI/ML Privacy Commitment (https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-unveils-ai-and-mlprivacy-commitment) 

, which outlines our belief that customers should have the highest level of security and control over their data that is stored in the cloud. That commitment extends to Google Cloud's generative AI products. Google ensures that its teams are following these commitments through robust data governance practices, which include reviews of the data that Google Cloud uses in the development of its products. More details about how Google processes data can also be found in Google's Cloud Data Processing Addendum (https://cloud.google.com/terms/data-processing-addendum) (CDPA). 

### Training restriction

As outlined in "Training Restriction" in the Service Terms section of the Service Specific Terms (https://cloud.google.com/terms/service-terms), Google won't use your data to train or fine-tune any AI/ML models without your prior permission or instruction. This applies to all managed models on Gemini Enterprise Agent Platform, including GA and pre-GA models. 

### Customer data retention and achieving zero data retention

Customer data is retained in Gemini Enterprise Agent Platform for Models as a Service (MaaS) for limited periods of time in the following scenarios and conditions. To achieve zero data retention, customers must take specific actions within each of these areas: 

**Prompt logging for abuse monitoring for Google models** : As outlined in Section 4.3 "Generative AI Safety and Abuse" of Google Cloud Platform Terms 

of Service (https://cloud.google.com/terms), Google may log prompts to detect potential abuse and violations of its Acceptable Use Policy (https://cloud.google.com/terms/aup) and Prohibited Use Policy (https://policies.google.com/terms/generative-ai/use-policy) as part of providing generative AI services to customers. Only customers whose use of Google Cloud is governed by the Google Cloud Platform Terms of Service (https://cloud.google.com/terms) are subject to prompt logging for abuse monitoring. If you are in scope for prompt logging for abuse monitoring and want zero data retention, you can request an exception for abuse monitoring. See Abuse monitoring (/gemini-enterprise-agent-platform/models/abuse-monitoring). 

**Prompt and response logging for abuse monitoring for Advanced AI** 

**models** : Certain models or features may also be subject to additional prompt and response logging to prevent abuse, as described in the Advanced AI Safety Addendum (http://cloud.google.com/terms/advanced-ai-safety-addendum). Zero data retention may not be possible when using some Advanced AI features. Please contact your account team for clarification. See Abuse monitoring (/gemini-enterprise-agent-platform/models/abuse-monitoring) for more information. 

**Grounding with Google Search** : As outlined in Section 20 "Generative AI Services: Grounding with Google Search" of the Service Specific Terms (https://cloud.google.com/terms/service-terms), Google collects and stores logs, which contains the following Customer Data: queries derived from End User prompts and contextual information that Customer may provide along with the prompts that are not associated with any Customer or its End Users for up to three (3) days, this stored information may be used for debugging of systems that support Grounding with Google Search. There is no way to disable the storage of this information if you use Grounding with Google Search. If you require zero data retention, we recommend using Web Grounding for Enterprise 

- (/gemini-enterprise-agent-platform/models/grounding/web-grounding-enterprise). 

**Grounding with Google Maps** : As outlined in Section 20 "Generative AI Services: Grounding with Google Maps" of the Service Specific Terms (https://cloud.google.com/terms/service-terms), Google stores prompts and contextual information that customers may provide, and generated output for thirty (30) days for the purposes of creating grounded results, and this stored information may only be used for reliability engineering, such as debugging in 

case of service issues, of systems that support grounding with Google Maps. There is no way to disable the storage of this information if you use Grounding with Google Maps. 

- **Request-response logging** : This feature is disabled by default. It can be enabled using a configuration setting on a per-model, per-project basis. Enabling this logging causes certain requests and responses to the specified model to be written to a designated BigQuery table. To achieve zero data retention, do not enable this feature. For more information about this feature, including how to enable or disable it, or read the current configuration setting, see Log requests and responses 

- (/gemini-enterprise-agent-platform/models/capabilities/request-response-logging). 

- **Interactions API** : When using the Interactions API 

- (/gemini-enterprise-agent-platform/reference/models/interactions-api) with `store = true` , Google stores user data (such as prompts, responses, and conversation state) to enable multi-turn conversations and later retrieval. If you do not specify a value for `store` , it defaults to `true` for all models. To achieve zero data retention, explicitly set `store = false` in your API requests. 

This applies to all managed models on Gemini Enterprise Agent Platform, including GA and pre-GA models. 

### Agent products

To achieve zero data retention for agent products, customers must adhere to the following conditions and retention schedules for each product: 

**CodeMender session data** — To enable resumption of long-running find and fix scans, CodeMender (/gemini-enterprise-agent-platform/agents/codemender) stores session state in Spanner. While a scan is in progress, session data — including target source code snippets, diffs, configuration, and analysis checkpoints — is stored encrypted for up to seven (7) days from session creation. When a session reaches a terminal state, source code and related content are cleared within seconds; the remaining session record is deleted automatically at the seven-day TTL. Customers can delete a session (removing all associated data) before the TTL expires. 

- **Deep Research agent session data** — Google stores prompts and session data - including search results and generated images - via the Interactions API for a period of seven (7) days. This session data is encrypted at rest, and is deleted automatically at the end of the seven-day TTL. Customers can delete a session (removing all associated data) before the TTL expires. This feature cannot be disabled when using the Deep Research agent. 

- **Agent Platform Sandbox Snapshots** : If you use the Snapshot API to persist Sandbox state, these snapshots are stored only for the duration of the Sandbox TTL. To achieve zero-data-retention, don't use the Sandbox API. 

### Google models

To achieve zero data retention for Google trained models, customers must take additional specific actions within each of these areas: 

#### Session resumption for Gemini Live API

Session resumption for Gemini Live API is disabled by default. It must be enabled by the user every time they call the API by specifying the field in the API request, and project-level privacy is enforced for cached data. Enabling Session Resumption allows the user to reconnect to a previous session within 24 hours by storing cached data, including text, video, and audio prompt data and model outputs, for up to 24 hours. To achieve zero data retention, do not enable this feature. For more information about this feature, including how to enable it, see Gemini Live API (/gemini-enterprise-agent-platform/models/live-api#session-resumption). 

#### Implicit data caching

By default, Google's published Gemini models cache Customer Data to reduce latency and accelerate responses. Implicit caching uses two storage tiers: 

- **In-memory caching** : Enabled by default for supported Gemini models. 

- **Durable caching** : Enabled by default for supported Gemini models. For the list of supported models, see Context caching overview 

(/gemini-enterprise-agent-platform/models/context-cache/context-cacheoverview#durable-caching-supported-models) 

In-memory data caching 

Implicit caching stores Customer Data (inputs, outputs, and derived data) in memory. In-memory cached data has the following properties: 

- It's stored only in memory, not at rest. 

- It's scoped to your project and is never served to another project. 

- It's deleted no later than 24 hours after it's written. 

- It's processed in the region that serves the request. 

- It's used only to serve your requests faster, and is never used to train or finetune models. 

Durable data caching 

On models that support durable caching, when in-memory cache capacity is exhausted, Google stores derived cache data (key-value representations computed from your inputs) in durable storage within the Agent Platform serving environment. Durable cached data has the following properties: 

   - It's stored at rest and encrypted with Google default encryption. 

   - It's scoped to your project and is never served to another project. 

   - It's deleted no later than 24 hours after it's written, and is often evicted sooner. 

   - It stays within the selected location and adheres to its Data Residency requirements when you use a regional or multi-regional endpoint. When you use the global endpoint, requests and their cached data can be served from any region. 

   - It's used only to serve your requests faster, and is never used to train or finetune models. 

- Customer-managed encryption keys (CMEK) aren't supported for durable caching. 

Control data caching 

If your organization's policy does not permit Customer Data to be stored at rest, you can disable durable caching on a per-project basis (#enabling-disabling-caching) and maintain in-memory caching. Alternatively, you can disable caching entirely. To disable durable caching across your organization rather than on a project level, contact your account team. 

Enable and disable data caching 

You can use the following curl commands to get caching status, disable caching, re-enable caching, or turn durable caching off and on. Turning off caching disables both in-memory caching and durable caching. When you disable or re-enable caching, the change applies to all Google Cloud regions. For more information about using Identity and Access Management to grant permissions required to enable or disable caching, see Gemini Enterprise Agent Platform access control with IAM (/gemini-enterprise-agent-platform/machine-learning/general/access-control). Expand the following sections to learn how to get the current cache setting, to disable caching, to enable caching, and to turn durable caching off and on. 

<sup>Get current caching setting</sup> 

Run the following command to check whether in-memory caching and durable caching are enabled for a project. To run this command, a user must be granted one of the following roles: `roles/aiplatform.viewer` , `roles/aiplatform.user` , or `roles/aiplatform.admin` . 

```
PROJECT_ID=PROJECT_ID
Setup project_id
$ gcloud config set project PROJECT_ID
GetCacheConfig
$ curl -X GET \
   -H "Authorization: Bearer $(gcloud auth application-default print-access-
token)" \
   -H "Content-Type: application/json" \
   https://us-central1-
aiplatform.googleapis.com/v1/projects/PROJECT_ID/cacheConfig
Response if durable caching and in-memory caching are enabled (default).
{
 "name": "projects/PROJECT_ID/cacheConfig",
 "retentionConfig": {
   "retentionType": "DURABLE"
 }
}
Response if durable caching is turned off and in-memory caching is enabled.
{
 "name": "projects/PROJECT_ID/cacheConfig",
 "retentionConfig": {
   "retentionType": "EPHEMERAL"
 }
}
Response if all caching is turned off.
{
 "name": "projects/PROJECT_ID/cacheConfig",
 "disableCache": true
}
```

<sup>Turn off caching</sup> 

Run the following curl command to turn off all caching for a Google Cloud project. This disables both in-memory caching and durable caching, and no cached data is retained. To run this command, a user must be granted the Gemini Enterprise Agent Platform administrator role, `roles/aiplatform.admin` . 

```
PROJECT_ID=PROJECT_ID
Setup project_id
$ gcloud config set project PROJECT_ID
Turn off all caching.
$ curl -X PATCH \
   -H "Authorization: Bearer $(gcloud auth application-default print-access-
token)" \
   -H "Content-Type: application/json" \
   https://us-central1-
aiplatform.googleapis.com/v1/projects/PROJECT_ID/cacheConfig \
   -d '{
     "name": "projects/PROJECT_ID/cacheConfig",
     "disableCache": true
   }'
A successful response confirms that caching is turned off for the project.
{
 "name": "projects/PROJECT_ID/locations/us-
central1/projects/PROJECT_ID/cacheConfig/operations/${OPERATION_ID}",
 "done": true,
 "response": {
   "@type": "type.googleapis.com/google.protobuf.Empty"
 }
}
```

To keep in-memory caching and turn off only durable caching, see **Turn off durable caching** . 

<sup>Enable caching</sup> 

If you disabled caching for a Google Cloud project and want re-enable it, run the following curl command. To run this command, a user must be granted the Gemini Enterprise Agent Platform administrator role, `roles/aiplatform.admin` . 

```
PROJECT_ID=PROJECT_ID
LOCATION_ID="us-central1"
Setup project_id
$ gcloud config set project PROJECT_ID
Setup project_id.
$ gcloud config set project ${PROJECT_ID}
Opt in to caching.
$ curl -X PATCH     -H "Authorization: Bearer $(gcloud auth application-default
print-access-token)" -H "Content-Type: application/json" https://us-central1-
aiplatform.googleapis.com/v1/projects/PROJECT_ID/cacheConfig -d '{
 "name": "projects/PROJECT_ID/cacheConfig",
 "disableCache": false
}'
A successful response confirms that caching is turned on for the project.
{
 "name": "projects/PROJECT_ID/locations/us-
central1/projects/PROJECT_ID/cacheConfig/operations/${OPERATION_NUMBER}",
 "done": true,
 "response": {
   "@type": "type.googleapis.com/google.protobuf.Empty"
 }
}
```

<sup>Turn off durable caching</sup> 

Run the following curl command to turn off durable caching and keep in-memory caching for a Google Cloud project. To run this command, a user must be granted the Gemini Enterprise Agent Platform administrator role, `roles/aiplatform.admin` . 

```
PROJECT_ID=PROJECT_ID
Setup project_id
gcloud config set project PROJECT_ID
Turn off durable caching.
curl -X PATCH \
   -H "Authorization: Bearer $(gcloud auth application-default print-access-
token)" \
   -H "Content-Type: application/json" \
   https://us-central1-
aiplatform.googleapis.com/v1/projects/PROJECT_ID/cacheConfig \
   -d '{
     "name": "projects/PROJECT_ID/cacheConfig",
     "disableCache": false,
     "retentionConfig": {
       "retentionType": "EPHEMERAL"
     }
   }'
A successful response confirms that durable caching is turned off and in-
memory caching stays on.
{
 "name": "projects/PROJECT_ID/locations/us-
central1/projects/PROJECT_ID/cacheConfig/operations/${OPERATION_ID}",
 "done": true,
 "response": {
   "@type": "type.googleapis.com/google.protobuf.Empty"
 }
}
```

<sup>Turn on durable caching</sup> 

If you turned off durable caching for a Google Cloud project and want to turn it back on, run the following curl command. To run this command, a user must be granted the Gemini Enterprise Agent Platform administrator role, `roles/aiplatform.admin` . 

```
PROJECT_ID=PROJECT_ID
Setup project_id
gcloud config set project PROJECT_ID
Turn on durable caching.
curl -X PATCH \
   -H "Authorization: Bearer $(gcloud auth application-default print-access-
token)" \
   -H "Content-Type: application/json" \
   https://us-central1-
aiplatform.googleapis.com/v1/projects/PROJECT_ID/cacheConfig \
   -d '{
     "name": "projects/PROJECT_ID/cacheConfig",
     "disableCache": false,
     "retentionConfig": {
       "retentionType": "DURABLE"
     }
   }'
A successful response confirms that durable caching is turned on for the
project.
{
 "name": "projects/PROJECT_ID/locations/us-
central1/projects/PROJECT_ID/cacheConfig/operations/${OPERATION_ID}",
 "done": true,
 "response": {
   "@type": "type.googleapis.com/google.protobuf.Empty"
 }
}
```

### What's next

Overview 

#### Responsible AI

(/gemini-enterpriseagentplatform/models/respon sible-ai) 

Learn about some of the limitations to generative AI and recommended practices for using generative AI. 

Overview 

#### How Gemini for Google Cloud uses your data

(/gemini/docs/discover/ data-governance) 

Learn how Gemini for Google Cloud conforms to Google's privacy commitment with generative AI technologies. 

Last updated 2026-10-15 UTC. 



## Data governance and generative AI

URL: https://docs.cloud.google.com/generative-ai-app-builder/docs/data-governance

Google was one of the first in the industry to publish an AI/ML Privacy Commitment (https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-unveils-ai-and-mlprivacy-commitment) 

, which outlines our belief that customers should have the highest level of security and control over their data that is stored in the cloud. That commitment extends to Google Cloud generative AI products. Google helps ensure that its teams are following these commitments through robust data governance practices, which includes reviews of the data that Google Cloud uses in the development of its products. More details about how Google processes data can also be found in Google's Customer Data Processing Addendum (CDPA) 

(https://cloud.google.com/terms/data-processing-addendum). 

### Usage of generative AI

Agent Search uses generative AI services for building search, personalized, and conversational experiences. 

As part of the Google Cloud AI/ML Privacy Commitment, customer data used in Agent Search is not used to train foundation models. 

Foundation models are frozen and only process input to provide output for the services provided by Agent Search. 

### Customer-specific models

When applicable, customer-specific models are built automatically and used only in the context of the project that is specific to the customer for the Agent Search service. 

Any customer data used to create these customer-specific models is not used to train foundation models. 

Customer-specific models, much like all customer data, continues to be protected by Google's security controls and best practices (/docs/security/overview/whitepaper). 

Last updated 2026-10-13 UTC.
