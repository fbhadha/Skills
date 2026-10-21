# Gemini Enterprise: connectors and data stores / Create a data store using Terraform to Third-party connectors: overview
Source: 02-Gemini-Enterprise-Connectors-and-data-stores.pdf, pages 199-242, extracted 2026-10-18

Contains:
- Create a data store using Terraform (pages 199-209) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-terraform
- Third-party connectors: overview (pages 210-242) https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source

## Create a data store using Terraform

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-terraform

You can use Terraform to create a generic Gemini Enterprise data store or to set up data connectors for Atlassian Confluence, Atlassian Jira, BigQuery, Microsoft SharePoint, or Salesforce. 

**Tip:** To learn how to apply or remove a Terraform configuration, see Basic Terraform commands (/docs/terraform/basic-commands). 

### Before you begin

Before using Terraform to create a data store, do the following: 

- Check whether billing is enabled on your Google Cloud project 

- (/billing/docs/how-to/verify-billing-enabled). 

- Ensure that you have the Project IAM Admin 

- ( `roles/resourcemanager.projectIamAdmin` ) role for your Google Cloud project, as well as the Gemini Enterprise Admin 

- ( `roles/discoveryengine.agentspaceAdmin` ) role. 

- Optional: If you are connecting a third-party data source like Microsoft SharePoint to Gemini Enterprise, obtain access credentials (such as API keys or database authentication) for the data source. 

- Ensure that you are using version 7.7.0 or later of the hashicorp/google (https://registry.terraform.io/providers/hashicorp/google) Terraform provider: 

```
terraform {
 required_providers {
   google = {
     source  = "hashicorp/google"
     version = "7.7.0"
   }
 }
```

### Create a generic data store

To use Terraform to create an empty data store, use the `google_discovery_engine_data_store` 

(https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engin e_data_store) 

Terraform resource. 

1. Create the Terraform configuration: 

```
terraform {
 required_providers {
   google = {
     source  = "hashicorp/google"
     version = "7.7.0"
   }
 }
}
provider "google" {
 project                 = "PROJECT_ID"
 user_project_override   = true
 billing_project         = "BILLING_PROJECT_ID"
}
resource "google_discovery_engine_data_store" "gemini_search_store" {
 location                    = "LOCATION"
 data_store_id               = "DATA_STORE_ID"
 display_name                = "DATA_STORE_NAME"
 industry_vertical           = "GENERIC"
 content_config              = "NO_CONTENT"
 solution_types              = ["SOLUTION_TYPE_SEARCH"]
 create_advanced_site_search = false
}
```

Replace the following: 

- _`PROJECT_ID`_ : your Google Cloud project ID 

- _`BILLING_PROJECT_ID`_ : your Google Cloud billing project ID 

- _`LOCATION`_ : the location for the data store, such as `us` or `global` (for more information, see Gemini Enterprise Standard and Plus Editions data residency and ML regional processing commitments 

- (/gemini/enterprise/docs/locations)) 

- _`DATA_STORE_ID`_ : the data store ID 

_`DATA_STORE_NAME`_ : the data store name 

2. Initialize Terraform: 

```
terraform init -upgrade
```

3. Preview your configuration: 

```
terraform plan
```

4. Apply the configuration: 

```
terraform apply
```

After creating the empty data store, you can ingest data into the data store using the Google Cloud console or API commands. 

### Create a data connector

To use Terraform to create a data connector for a supported service, use the `google_discovery_engine_data_connector` 

(https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engin e_data_connector) 

Terraform resource. Include credentials for the service, as well as search filter configuration, in `json_params` . 

1. Create the Terraform configuration: 

```
terraform {
 required_providers {
   google = {
     source  = "hashicorp/google"
     version = "7.7.0"
   }
 }
}
provider "google" {
 project                 = "PROJECT_ID"
 user_project_override   = true
 billing_project         = "BILLING_PROJECT_ID"
}
resource "google_discovery_engine_data_connector" "LOCAL_NAME" {
 provider = google
 project                 = "PROJECT_ID"
 location                = "LOCATION"
 collection_id           = "COLLECTION_ID"
 collection_display_name = "COLLECTION_DISPLAY_NAME"
 data_source = "DATA_SOURCE"
 json_params = jsonencode({
   "client_id"                = "CLIENT_ID"
   "client_secret"            = "CLIENT_SECRET"
   "instance_uri"             = "INSTANCE_URI"
   "tenant_id"                = "TENANT_ID"
   "structured_search_filter" = { "FILTER_KEY" = ["FILTER_VALUE"] }
 })
 refresh_interval = "7200s"
 connector_modes = [CONNECTOR_MODES]
 entities {
   entity_name = "ENTITY_NAME"
 }
}
```

Replace the following: 

- _`PROJECT_ID`_ : your Google Cloud project ID 

- _`BILLING_PROJECT_ID`_ : your Google Cloud billing project ID 

- _`LOCAL_NAME`_ : the local name of the Terraform resource 

- _`LOCATION`_ : the location for the data store, such as `us` or `global` (for more information, see Gemini Enterprise Standard and Plus Editions data residency and ML regional processing commitments 

- (/gemini/enterprise/docs/locations)) 

- _`COLLECTION_ID`_ : the collection ID 

- _`COLLECTION_DISPLAY_NAME`_ : the collection display name 

- _`DATA_SOURCE`_ : the data source type. The following values are supported: 

   - `bigquery` 

   - `confluence` 

   - `jira` 

   - `salesforce` 

   - `sharepoint_federated_search` 

- _`CLIENT_ID`_ : the client ID for the service 

- _`CLIENT_SECRET`_ : the client secret for the service 

- _`INSTANCE_URI`_ : the URI of your instance (for example, `https://yourtenant.sharepoint.com` ) 

- _`TENANT_ID`_ : the tenant ID 

- _`FILTER_KEY`_ : a filter key (for example, `Path` ) 

- _`FILTER_VALUE`_ : a filter value (for example, 

`"https://example.sharepoint.com/*"` ) 

- _`ENTITY_NAME`_ : the name of an entity for the connector to search (see the resource documentation 

(https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/disco very_engine_data_connector#argument-reference) ) 

_`CONNECTOR_MODES`_ : the modes to enable for the connector (for example, `"FEDERATED"` ) 

2. Initialize Terraform: 

```
terraform init -upgrade
```

3. Preview your configuration: 

```
terraform plan
```

4. Apply the configuration: 

```
terraform apply
```

When prompted, confirm your changes. 

After applying the configuration, you can see the data connector in the list of data stores and can connect it to a Gemini Enterprise app. For more information, see Connect a data store to app and authorize Gemini Enterprise (/gemini/enterprise/docs/connectors/connect-existing-data-store). 

### Update a data connector

To use Terraform to update settings for an existing data connector, provide the new settings in `json_params` , and provide any unchanged arguments with their current values so that Terraform doesn't replace the resource. Add any required arguments that don't need to be updated to `ignore_changes` in the `lifecycle` block. 

**Tip:** For the list of required arguments, see the **`google_discovery_engine_data_connector`** resource documentation 

(https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engin e_data_connector#argument-reference) 

1. Create the Terraform configuration. This example updates the `structured_search_filter` setting with a new filter value, but lists other required fields such as `refresh_interval` , `entities` , and `connector_modes` with their current values. 

```
terraform {
 required_providers {
   google = {
     source  = "hashicorp/google"
     version = "7.7.0"
   }
 }
}
provider "google" {
 project               = "PROJECT_ID"
 user_project_override = true
 billing_project       = "BILLING_PROJECT_ID"
}
resource "google_discovery_engine_data_connector" "LOCAL_NAME" {
 provider = google
 project                 = "PROJECT_ID"
 location                = "LOCATION"
 collection_id           = "COLLECTION_ID"
 collection_display_name = "COLLECTION_DISPLAY_NAME"
 data_source = "DATA_SOURCE"
 json_params = jsonencode({
   "structured_search_filter" = { "FILTER_KEY" = ["UPDATED_FILTER_VALUE"]
}
 })
 refresh_interval = "REFRESH_INTERVAL"
 entities {
   entity_name           = "ENTITY_NAME"
   key_property_mappings = {}
 }
 static_ip_enabled = false
 connector_modes   = [CONNECTOR_MODES]
 lifecycle {
   ignore_changes = [
     collection_display_name,
     entities,
     refresh_interval
   ]
 }
}
```

Replace the following: 

- _`PROJECT_ID`_ : your Google Cloud project ID 

- _`BILLING_PROJECT_ID`_ : your Google Cloud billing project ID 

- _`LOCAL_NAME`_ : the local name of the Terraform resource 

- _`LOCATION`_ : the location for the data store, such as `us` or `global` (for more information, see Gemini Enterprise Standard and Plus Editions data residency and ML regional processing commitments 

- (/gemini/enterprise/docs/locations)) 

- _`COLLECTION_ID`_ : the collection ID 

- _`COLLECTION_DISPLAY_NAME`_ : the collection display name 

- _`DATA_SOURCE`_ : the data source type. The following values are supported: 

   - `bigquery` 

   - `confluence` 

   - `jira` 

   - `salesforce` 

   - `sharepoint_federated_search` 

- _`FILTER_KEY`_ : a filter key for which you want to update the value (for example, `Path` ) 

- _`UPDATED_FILTER_VALUE`_ : the new filter value (for example, 

- `https://other.sharepoint.com/*` ) 

- _`REFRESH_INTERVAL`_ : the refresh interval 

- _`ENTITY_NAME`_ : the name of an entity for the connector to search (see the resource documentation 

(https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/disco very_engine_data_connector#argument-reference) 

) 

   - _`CONNECTOR_MODES`_ : the modes to enable for the connector (for example, `"FEDERATED"` ) 

2. Run `terraform import` to indicate that this is an update operation: 

```
terraform import \
google_discovery_engine_data_connector.LOCAL_NAME \
projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConne
ctor
```

**Note:** The local name of the resource in the **`terraform import`** command must match the local name of the resource in the Terraform configuration. 

3. Preview your configuration: 

```
terraform plan
```

The output should be similar to the following: 

```
Terraform used the selected providers to generate the following execution
plan. Resource actions are indicated with the following symbols:
 ~ update in-place
Terraform will perform the following actions:
 google_discovery_engine_data_connector.update-sharepoint-connector will
be updated in-place
 ~ resource "google_discovery_engine_data_connector" "update-sharepoint-
connector" {
       id                              = "projects/my-project-
123/locations/global/collections/default_collection/dataConnector"
     ~ json_params                     = jsonencode(
         ~ {
             ~ structured_search_filter = {
                 ~ "Path" = [
                     ~ "https://other.sharepoint.com/*" -
"https://example.sharepoint.com/*",
                       (1 unchanged element hidden)
                   ]
               }
           }
       )
       name                            = "projects/my-project-
123/locations/global/collections/default_collection/dataConnector"
       (21 unchanged attributes hidden)
       (2 unchanged blocks hidden)
   }
Plan: 0 to add, 1 to change, 0 to destroy.
```

Ensure that the final line of output specifies `0 to add, 1 to change, 0 to destroy` . 

4. Apply the configuration: 

```
terraform apply
```

When prompted, confirm your changes. 

The output should be similar to the following: 

```
Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
```

### What's next

- To provide a user interface for querying your data, create an app (/gemini/enterprise/docs/create-app) in Gemini Enterprise and connect it to your data store (/gemini/enterprise/docs/connect-existing-data-store). 

- To manage the list of actions for a data connector, see Manage actions (/gemini/enterprise/docs/manage-actions). 

Last updated 2026-10-14 UTC. 



## Third-party connectors: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source

When you connect a third-party data source, Gemini Enterprise creates a _data store_ and associates _entity_ data stores with it for each specified entity. Entity types are specific to the connected data source (for example, Jira Cloud entities include issues, attachments, comments, and worklogs). 

- To import data from a Google data source instead, see Create a first-party data store (/gemini/enterprise/docs/create-data-store). 

- If you are using customer-managed encryption keys, see Register single- region keys for third-party connectors 

- (/gemini/enterprise/docs/cmek#third-party-connectors-key-registration). 

- If you want outbound traffic from the data store to originate from a fixed set of IP addresses (for example, to allowlist them on the source system), and if the data store supports it, see Configure static IP egress 

- (/gemini/enterprise/docs/connectors/configure-static-ip-egress). 

**Note:** When using federated search or federated connectors, your query string is sent to all enabled third-party search backends. The query string sent to a third-party system might contain parts of the data in your search request and conversation history. The third-party system can link the query with your identity. Once data is in the third-party system, it is subject to that system's Terms of Service and privacy policies, not Google Cloud's Terms of Service. 

### Sources by launch stage

Visit a source-specific page for information on how to connect that source to Gemini Enterprise. 

The following tables list each supported connector with the value to use in the `discoveryengine.managed.allowedDataSources` 

(/gemini/enterprise/docs/connectors/configure-allowed-data-sources) organization policy. Where available, the connector name links to its setup instructions. 

#### Generally available

|Data source|Value for`allowedData`<br>`Sources`|
|---|---|
|Box(/gemini/enterprise/docs/connectors/box)|`box`|
|Confluence Cloud<br>(/gemini/enterprise/docs/connectors/confluence-cloud)|`confluence`|
|Confluence Data Center<br>(/gemini/enterprise/docs/connectors/confluence-dc)|`confluence_server`|
|Dropbox(/gemini/enterprise/docs/connectors/dropbox)|`dropbox`|
|GitHub(/gemini/enterprise/docs/connectors/github)|`github`|
|Google Calendar(/gemini/enterprise/docs/connectors/gcal)|`google_calendar`|
|Google Drive(/gemini/enterprise/docs/connectors/gdrive)|`google_drive`|
|Google Mail(/gemini/enterprise/docs/connectors/gmail)|`google_mail`|
|HubSpot(/gemini/enterprise/docs/connectors/hubspot)|`hubspot`|
|Jira Cloud(/gemini/enterprise/docs/connectors/jira-cloud)|`jira`|
|Jira Data Center(/gemini/enterprise/docs/connectors/jira-dc)|`jira_server`|
|Microsoft Entra ID<br>(/gemini/enterprise/docs/connectors/entra-id/connect-entra-id)|`azure_active_`<br>`directory`|
|Microsoft Outlook(/gemini/enterprise/docs/connectors/ms-outlook)|`outlook`|
|Microsoft Teams(/gemini/enterprise/docs/connectors/ms-teams)|`teams`|
|Monday(/gemini/enterprise/docs/connectors/monday)|`monday`|
|OneDrive(/gemini/enterprise/docs/connectors/ms-onedrive)|`onedrive`|
|ServiceNow(/gemini/enterprise/docs/connectors/servicenow)|`servicenow`|
|SharePoint(/gemini/enterprise/docs/connectors/ms-sharepoint)|`sharepoint`|
|Slack(/gemini/enterprise/docs/connectors/slack)|`slack`|

#### Public preview

|Data source|Value for<br>`allowedData`<br>`Sources`|
|---|---|
|Adobe Workfront(/gemini/enterprise/docs/connectors/adobe-workfront)|`adobe_`<br>`workfront`|
|AirOps(/gemini/enterprise/docs/connectors/airops)|`airops`|
|Airtable(/gemini/enterprise/docs/connectors/airtable)|`airtable`|
|Aiwyn Tax(/gemini/enterprise/docs/connectors/aiwyn_tax)|`aiwyn_tax`|
|AllTrails(/gemini/enterprise/docs/connectors/alltrails)|`alltrails`|
|Apollo GraphOS(/gemini/enterprise/docs/connectors/apollo-graphos)|`apollo_`<br>`graphos`|
|Asana(/gemini/enterprise/docs/connectors/asana)|`asana`|
|Atlan(/gemini/enterprise/docs/connectors/atlan-mcp)|`atlan_mcp`|
|Attio(/gemini/enterprise/docs/connectors/attio)|`attio`|
|Autodesk Product Help<br>(/gemini/enterprise/docs/connectors/autodesk-product-help)|`autodesk_`<br>`product_help`|
|AWS Marketplace(/gemini/enterprise/docs/connectors/aws-marketplace)|`aws-`<br>`marketplace`|
|Bitly(/gemini/enterprise/docs/connectors/bitly)|`bitly`|
|Blockscout(/gemini/enterprise/docs/connectors/blockscout)|`blockscout`|
|Calendly(/gemini/enterprise/docs/connectors/calendly)|`calendly`|
|Campfire(/gemini/enterprise/docs/connectors/campfire)|`campfire`|
|Cisco Workspaces(/gemini/enterprise/docs/connectors/cisco-workspaces)|`cisco_`<br>`workspaces`|
|Clay(/gemini/enterprise/docs/connectors/clay)|`clay`|
|Cohesity(/gemini/enterprise/docs/connectors/cohesity)|`cohesity`|
|CoinDesk(/gemini/enterprise/docs/connectors/coindesk)|`coindesk`|
|CourtListener(/gemini/enterprise/docs/connectors/courtlistener)|`courtlistener`|

|Data source|Value for<br>`allowedData`<br>`Sources`|
|---|---|
|Courtroom5(/gemini/enterprise/docs/connectors/courtroom5)|`courtroom5`|
|Crossbeam(/gemini/enterprise/docs/connectors/crossbeam)|`crossbeam`|
|Crypto(/gemini/enterprise/docs/connectors/crypto)|`crypto`|
|Custom MCP Server<br>(/gemini/enterprise/docs/connectors/custom-mcp-server/set-up-custom-mcp-<br>server)|`custom_mcp`|
|Descript(/gemini/enterprise/docs/connectors/descript)|`descript`|
|Dice(/gemini/enterprise/docs/connectors/dice)|`dice`|
|DirectBooker(/gemini/enterprise/docs/connectors/directbooker)|`directbooker`|
|Docusign(/gemini/enterprise/docs/connectors/docusign)|`docusign`|
|D&B Commercial Graph<br>(/gemini/enterprise/docs/connectors/d-and-b-commercial-graph)|`dun_and_`<br>`bradstreet`|
|D&B Finance Analytics<br>(/gemini/enterprise/docs/connectors/d_b_finance_analytics)|`d_b_finance_`<br>`analytics`|
|D&B Risk Analytics(/gemini/enterprise/docs/connectors/d_b_risk_analytics)|`d_b_risk_`<br>`analytics`|
|Daloopa(/gemini/enterprise/docs/connectors/daloopa)|`daloopa`|
|Dynamics 365(/gemini/enterprise/docs/connectors/dynamics365)|`dynamics365`|
|Egnyte(/gemini/enterprise/docs/connectors/egnyte)|`egnyte`|
|Excalidraw(/gemini/enterprise/docs/connectors/excalidraw)|`excalidraw`|
|FactSet AI-Ready Data|`factset_ai_`|
|(/gemini/enterprise/docs/connectors/factset_ai_ready_data)|`ready_data`|
|Fibery(/gemini/enterprise/docs/connectors/fibery)|`fibery`|
|Finnhub(/gemini/enterprise/docs/connectors/finnhub)|`finnhub`|
|Fiscal.ai(/gemini/enterprise/docs/connectors/fiscal-ai)|`fiscal_ai`|

|Data source|Value for<br>`allowedData`<br>`Sources`|
|---|---|
|Freshservice(/gemini/enterprise/docs/connectors/freshservice)|`freshservice`|
|Fullstory(/gemini/enterprise/docs/connectors/fullstory)|`fullstory`|
|Gamma(/gemini/enterprise/docs/connectors/gamma)|`gamma`|
|GitLab(/gemini/enterprise/docs/connectors/gitlab)|`gitlab`|
|Globalping(/gemini/enterprise/docs/connectors/globalping)|`globalping`|
|GoDaddy(/gemini/enterprise/docs/connectors/godaddy)|`godaddy`|
|Gong(/gemini/enterprise/docs/connectors/gong)|`gong`|
|Google Chat(/gemini/enterprise/docs/connectors/gchat)|`google_chat`|
|Compute Engine(/gemini/enterprise/docs/connectors/google-compute-engin|e) `google_`<br>`compute_`<br>`engine`|
|Google Stitch(/gemini/enterprise/docs/connectors/googlestitch)|`googlestitch`|
|Grafana(/gemini/enterprise/docs/connectors/grafana)|`grafana`|
|Grafana(/gemini/enterprise/docs/connectors/grafana)|`grafana`|
|Granted(/gemini/enterprise/docs/connectors/granted)|`granted`|
|Guru(/gemini/enterprise/docs/connectors/guru)|`guru`|
|Hex(/gemini/enterprise/docs/connectors/hex)|`hex`|
|Hugging Face(/gemini/enterprise/docs/connectors/huggingface)|`huggingface`|
|iManage platform(/gemini/enterprise/docs/connectors/imanage-platform)|`imanage_`<br>`platform`|
|Intercom(/gemini/enterprise/docs/connectors/intercom)|`intercom`|
|Invideo(/gemini/enterprise/docs/connectors/invideo)|`invideo`|
|Kiwi(/gemini/enterprise/docs/connectors/kiwi)|`kiwi`|
|Kiwi.com(/gemini/enterprise/docs/connectors/kiwi-com)|`kiwi_com`|

|Data source|Value for<br>`allowedData`<br>`Sources`|
|---|---|
|Lastminute(/gemini/enterprise/docs/connectors/lastminute)|`lastminute`|
|LegalZoom(/gemini/enterprise/docs/connectors/legalzoom)|`legalzoom`|
|Linear(/gemini/enterprise/docs/connectors/linear)|`linear`|
|Lovable(/gemini/enterprise/docs/connectors/lovable)|`lovable`|
|LumApps(/gemini/enterprise/docs/connectors/lumapps)|`lumapps`|
|MailerLite(/gemini/enterprise/docs/connectors/mailerlite)|`mailerlite`|
|Mercury(/gemini/enterprise/docs/connectors/mercury-mcp)|`mercury_mcp`|
|Mermaid Chart(/gemini/enterprise/docs/connectors/mermaid_chart)|`mermaid_chart`|
|Microsoft Learn(/gemini/enterprise/docs/connectors/microsoft-learn)|`microsoft_`<br>`learn`|
|Microsoft Outlook (OpenAPI)(/gemini/enterprise/docs/connectors/ms-outlook)|`outlookopenap`<br>`i`|
|Midpage(/gemini/enterprise/docs/connectors/midpage)|`midpage`|
|Miro(/gemini/enterprise/docs/connectors/miro)|`miro`|
|Moody's(/gemini/enterprise/docs/connectors/moody_s)|`moody_s`|
|MSCI(/gemini/enterprise/docs/connectors/msci)|`msci`|
|NetDocuments(/gemini/enterprise/docs/connectors/netdocuments)|`netdocuments_`<br>`us_vault`|
|Nexla(/gemini/enterprise/docs/connectors/nexla-mcp-studio)|`nexla_mcp_`<br>`studio`|
|Notion(/gemini/enterprise/docs/connectors/notion)|`notion`|
|Omni Analytics(/gemini/enterprise/docs/connectors/omni_analytics)|`omni_`<br>`analytics`|
|Open Targets(/gemini/enterprise/docs/connectors/open_targets)|`open_targets`|

|Data source|Value for<br>`allowedData`<br>`Sources`|
|---|---|
|Oracle NetSuite(/gemini/enterprise/docs/connectors/oracle_netsuite)|`oracle_`<br>`netsuite`|
|PagerDuty(/gemini/enterprise/docs/connectors/pagerduty)|`pagerduty`|
|PandaDoc(/gemini/enterprise/docs/connectors/pandadoc)|`pandadoc`|
|Pendo(/gemini/enterprise/docs/connectors/pendo_mcp)|`pendo_mcp`|
|pg-aiguide(/gemini/enterprise/docs/connectors/pg_aiguide)|`pg_aiguide`|
|Pylon(/gemini/enterprise/docs/connectors/pylon)|`pylon`|
|Ramp(/gemini/enterprise/docs/connectors/ramp-mcp)|`ramp_mcp`|
|Relativity(/gemini/enterprise/docs/connectors/relativity)|`relativity`|
|S&P Global-Deterministic Retrieval<br>(/gemini/enterprise/docs/connectors/s_p_global)|`s_p_global`|
|Salesforce(/gemini/enterprise/docs/connectors/salesforce/connect-salesforce)|`salesforce`|
|Sanity(/gemini/enterprise/docs/connectors/sanity)|`sanity`|
|ServiceM8(/gemini/enterprise/docs/connectors/servicem8)|`servicem8`|
|Shopify(/gemini/enterprise/docs/connectors/shopify)|`shopify`|
|Smartsheet(/gemini/enterprise/docs/connectors/smartsheet)|`smartsheet`|
|Solve Intelligence(/gemini/enterprise/docs/connectors/solve-intelligence)|`solve_`<br>`intelligence`|
|Sourcegraph(/gemini/enterprise/docs/connectors/sourcegraph)|`sourcegraph`|
|Squarespace(/gemini/enterprise/docs/connectors/squarespace)|`squarespace`|
|Starburst(/gemini/enterprise/docs/connectors/starburst)|`starburst`|
|Streak(/gemini/enterprise/docs/connectors/streak)|`streak`|
|Stripe(/gemini/enterprise/docs/connectors/stripe)|`stripe`|

|Data source|Value for<br>`allowedData`<br>`Sources`|
|---|---|
|Superhuman Mail(/gemini/enterprise/docs/connectors/superhuman-mail)|`superhuman_`<br>`mail`|
|Supermetrics(/gemini/enterprise/docs/connectors/supermetrics)|`supermetrics`|
|Supabase(/gemini/enterprise/docs/connectors/supabase)|`supabase`|
|SurveyMonkey(/gemini/enterprise/docs/connectors/surveymonkey)|`surveymonkey`|
|Taskrabbit(/gemini/enterprise/docs/connectors/taskrabbit)|`taskrabbit`|
|Tavily(/gemini/enterprise/docs/connectors/tavily)|`tavily`|
|Trivago(/gemini/enterprise/docs/connectors/trivago)|`trivago`|
|Twilio Docs(/gemini/enterprise/docs/connectors/twilio_docs)|`twilio_docs`|
|Vanta(/gemini/enterprise/docs/connectors/vanta)|`vanta`|
|Viator(/gemini/enterprise/docs/connectors/viator)|`viator`|
|Webex Meetings(/gemini/enterprise/docs/connectors/webex-meetings)|`webex_`<br>`meetings`|
|Windsor.ai(/gemini/enterprise/docs/connectors/windsor-ai)|`windsor`|
|Wix(/gemini/enterprise/docs/connectors/wix)|`wix`|
|Wrike(/gemini/enterprise/docs/connectors/wrike)|`wrike`|
|Zapier(/gemini/enterprise/docs/connectors/zapier)|`zapier`|
|Zendesk(/gemini/enterprise/docs/connectors/zendesk)|`zendesk`|
|Zoho Books(/gemini/enterprise/docs/connectors/zohobooks)|`zohobooks`|
|Zoho CRM(/gemini/enterprise/docs/connectors/zohocrm)|`zohocrm`|
|Zoho Desk(/gemini/enterprise/docs/connectors/zohodesk)|`zohodesk`|
|Zoho Projects(/gemini/enterprise/docs/connectors/zohoprojects)|`zohoprojects`|
|ZoomInfo(/gemini/enterprise/docs/connectors/zoominfo)|`zoominfo`|

#### Private preview

To connect data sources that are in private preview, contact your Google account team and request to be added to the allowlist. 

- Connect Confluence Data Center On-premises with data ingestion (/gemini/enterprise/docs/connectors/confluence-dc) 

- Connect Jira Data Center On-premises with data ingestion (/gemini/enterprise/docs/connectors/jira-dc) 

Connect Salesforce with data ingestion 

(/gemini/enterprise/docs/connectors/salesforce/connect-salesforce) 

### Supported actions

Expand the data store name in the following list to reveal the available actions for each. 

**Note:** Not all third-party data stores support actions, such as data stores supporting limited functionality (federated search only or search only). 

Asana 

|Launch<br>date|Action|Description|
|---|---|---|
|06/05/26|Create project|Create a new project with optional sections and tasks<br>in a single operation.|
||Create project<br>status update|Post a status update to a project or portfolio.|
||Create tasks|Create one or more tasks immediately without visual<br>preview or asking for confirmation.|
||Update tasks|Update one or more tasks in a single operation.|

AirOps 

|Launch<br>date|Action|Description|
|---|---|---|
|6/4/26|Add grid column|Add a new column to a grid table.|
||Add URLs to knowledge<br>base|Add one or more URLs to a knowledge base<br>for indexing.|
||Create action grid|Create a grid with power agents for taking<br>action on AEO insights.|
||Create grid|Create a new grid (spreadsheet-like table for<br>organizing and processing data).|
||Create grid sheet|Create a new sheet (table) within an existing<br>grid.|
||Create knowledge base<br>direct upload|Initiate a direct file upload to a knowledge<br>base.|
||Create report|Create a new analytics report for a Brand Kit.|
||Manage knowledge base|Create or update a knowledge base.|
|8/28/26|Update knowledge base<br>document metadata|Update metadata for a document in a<br>knowledge base.|
|7/29/26|Suggest Brand Kit edits|Suggest edits to a Brand Kit's fields without<br>applying them.|
|Airtab|Write grid<br>le|Create or update rows in a grid table.|
|Launch<br>date|Action|Description|

|8/28/26|Create records for<br>table|Create new records in a specific table.|
|---|---|---|
|8/11/26|Update records for<br>table|Update existing records in a specific table.|
|6/23/26|Create base|Create a new base in a specified workspace.|
||Create field|Create a new field in an existing table.|
||Create record<br>comment|Create a new comment on a specific record.|
||Create table|Create a new table in an existing base.|
||Update table|Update an existing table's name and/or<br>description.|

Bitly 

|Launch date|Action|Description|
|---|---|---|
|08/17/26|Create QR code|Create a QR code.|
||Create short link|Create a short link.|
||Update QR code|Update a QR code.|
||Update short link|Update short link properties.|

Box 

Box supports the tools exposed by Box as actions within the data store. For a list of supported tools, see the Box MCP tools documentation 

(https://docs.box.com/en/box-mcp/tools). 

Box (Legacy) 

|Launch<br>date|Action|Description|
|---|---|---|
|1/23/26|Upload file|Uploads a new document or file to a specific folder in Box.|
||Download<br>file|Downloads a file from Box.|
|12/19/25|Copy file|Creates a duplicate of a file within a destination folder while<br>leaving the original file unchanged.|

Clay 

|Launch<br>date|Action|Description|
|---|---|---|
|9/22/26|Find and enrich company|Find and enrich a single company by domain or<br>LinkedIn URL.|
||Find and enrich contacts<br>at company|Search for contacts at a company by role, title,<br>name, or department.|
||Find and enrich list of|Find and enrich specific named contacts at their|
||contacts|companies.|

Confluence Cloud 

|Launch<br>date|Action|Description|
|---|---|---|
|8/5/26|Create blog post|Creates a new Confluence blog post in a specified<br>space with content and a title.|
||Create space|Creates a new Confluence space with a specified name<br>and key.|
||Update page|Updates the title or content of an existing Confluence|
|||page.|

|1/23/26|Upload<br>attachment|Uploads a file to be attached to a specific page.|
|---|---|---|
||Download<br>attachment|Retrieves the actual file content of a specific<br>attachment.|
|12/19/25|Create page|Creates a new Confluence Cloud page.|

Confluence Data Center 

|Launch<br>date|Action|Description|
|---|---|---|
|3/4/26|Download<br>attachment|Downloads an attachment from a Confluence Data<br>Center page.|
|2/19/26|Upload attachm|ent Uploads an attachment to a Confluence Data Center<br>page.|

Descript 

|Launch<br>date|Action|Description|
|---|---|---|
|8/17/26|Import media|Import media into a Descript project.|
||Prompt project|Query, create, and edit Descript projects using natural|
||agent|language.|
||Publish project|Publish a Descript project composition.|

Dropbox 

|Launch<br>date|Action|Description|
|---|---|---|
|1/28/26|Download file|Downloads a file from Dropbox.|

|1/23/26|Upload file|Uploads a new file to a specified path within a Dropbox<br>account.|
|---|---|---|
|12/12/25|Create folder|Creates a folder in Dropbox.|
||Copy file or<br>folder|Copies a file or folder in Dropbox.|

Egnyte 

|Launch<br>date|Action|Description|
|---|---|---|
|7/29/26|Create|Create a new comment (note) on an existing file in|
||comment|Egnyte.|
||Create folder|Create a new folder in Egnyte.|
||Create link|Create a link to a file or folder in Egnyte.|
||Upload file|Upload a file.|

Freshservice 

|Launch<br>date|Action|Description|
|---|---|---|
|8/03/26|Create ticket note|Adds a note (conversation) to an existing ticket<br>in Freshservice.|
|7/12/26|Update ticket|Updates an existing ticket in Freshservice.|
|6/23/26|Create ticket|Creates a new ticket in Freshservice.|
||Place service catalog<br>item request|Submits a request for a service catalog item.|

Gamma 

|Launch<br>date|Action|Description|
|---|---|---|
|8/17/26<br>GitHub|Generate<br>Gamma<br>|Creates a new presentation, document, webpage, or social<br>media post in Gamma.|
|Launch<br>date|Action|Description|

|07/15/26|Create gist|Create a new GitHub Gist.|
|---|---|---|
||Dismiss notification|Mark a GitHub notification as read or done.|
||Manage notification<br>subscription|Ignore, watch, or delete a notification thread<br>subscription.|
||Manage repository<br>notification subscription|Ignore, watch, or delete a repository's<br>notification subscription.|
||Mark all notifications read|Mark all notifications as read, optionally<br>scoped to a repository.|
||Reply to pull request<br>comment|Add a reply to an existing pull request<br>comment.|
||Star repository|Star a repository on behalf of the<br>authenticated user.|
||Trigger Actions workflow|Trigger a GitHub Actions workflow (run, cancel,<br>or rerun jobs).|
||Unstar repository|Unstar a repository on behalf of the<br>authenticated user.|
||Update gist|Update an existing GitHub Gist.|
||Write discussion comment|Add, reply to, update, delete, or mark/unmark<br>as answer a discussion comment.|
||Write GitHub project|Create or update GitHub Projects (project,<br>items, fields, status updates).|
||Write repository label|Create, update, or delete a label on a<br>repository.|
|03/18/26|Create or update file|Create or update a single file in a repository.|
||Fork repository|Fork a repository to your account or a<br>specified organization.|
||Push files|Push multiple files to a repository in a single<br>commit.|
||Write issue|Create or update an issue in a repository.|

|03/11/26|Add comment to pending<br>review|Add a review comment to your latest pending<br>pull request review.|
|---|---|---|
||Add issue comment|Add a comment to a specific issue or pull<br>request.|
||Create branch|Create a new branch in a repository.|
||Merge pull request|Merge a pull request.|
||Update pull request|Update an existing pull request.|

Hex 

|Launch dat|e Action|Description|
|---|---|---|
|08/11/26|Create thread|Create a Hex Thread to ask questions about your data.|
||Continue threa|d Add follow-up questions to an idle thread.|

HubSpot 

|Launch date|Action|Description|
|---|---|---|
|03/18/26|Manage CRM Objects|Manages CRM objects in HubSpot.|

Jira Cloud 

Launch Action Description date 

|8/5/26|Assign issue|Assigns an existing Jira issue to a specified user.|
|---|---|---|
||Create project       i|Creates a new Jira project with a specified name, key,<br>project type, and template.|
||Create<br>worklog|Adds a time-tracking worklog entry to a Jira issue.|
||Get board|Gets a board in Jira.|
||Get issues for<br>board|Gets issues for a board in Jira.|
||Link issues|Creates a link between two Jira issues (for example, blocks,<br>is blocked by, relates to).|
||List boards|Lists boards in Jira.|
||Update<br>project|Updates an existing Jira project's settings, such as name,<br>key, description, or lead.|
||Update<br>worklog|Updates an existing worklog entry on a Jira issue.|
|1/23/26|Upload<br>attachment|Uploads an attachment to an existing issue in Jira.|
|12/19/25|Change issue<br>status|Changes a Jira issue's status.|
|12/12/25|Create<br>comment|Creates a comment on a Jira issue.|
||Update<br>comment|Edits an existing comment.|
||Create issue|Creates a new Jira issue (requires summary, project ID, and<br>issue type ID).|
||Update issue|Updates an existing issue in Jira Cloud. You need to provide<br>the issue ID to identify it, and you can modify various fields|
|||such as the summary, description, and assignee.|

Jira Data Center 

|Launch<br>date|Action|Description|
|---|---|---|
|2/19/26|Create issue|Creates a new issue or ticket.|
||Update issue|Changes the details of a ticket, like updating its<br>summary, description, priority, or assignee.|
||Change Issue<br>Status|Changes the status of an issue.|
||Create commen|t Adds a comment on an issue.|
||Update commei|ntModifies an existing comment on an issue.|
||Download<br>attachment|Downloads an attachment from an issue.|
||Upload<br>attachment|Adds an attachment to an issue.|
|Linear<br>Launch da|te<br>Action|Description|
|2/6/26|Save com|ment<br>Saves a comment to a Linear issue.|
||Save issu|e<br>Saves an issue in Linear.|
||Save a pr|oject<br>Saves a new Linear project.|
|Lovabl<br>Launch<br>date|e<br>Action|Description|

|7/29/26|Deploy project|Deploy (publish) a project to production hosting on<br>lovable.app.|
|---|---|---|
||Enable database|Provision a cloud PostgreSQL database (Supabase)<br>for a project.|
||Send message|Send a chat message to a project's AI agent.|
||Set workspace<br>knowledge|Set the workspace's knowledge content.|
|6/23/26|Add connector|Add a connector to a workspace.|
||Remix project|Remix (fork) an existing project into a workspace.|
||Set project knowledg|eSet a project's knowledge content.|
||Set project visibility|Set a project's visibility level: draft, private, or<br>public.|

Microsoft OneDrive 

|Launch<br>date|Action|Description|
|---|---|---|
|9/17/26|Copy folder|Copies a folder in OneDrive to a destination folder.|
||Move file|Moves a file in OneDrive to another folder.|
||Move folder|Moves a folder in OneDrive to another folder.|
||Rename file|Renames a file in OneDrive.|
||Rename folder|Renames a folder in OneDrive.|
||Share file or folder|Shares a file or folder in OneDrive with specified<br>recipients.|
||Update file<br>properties|Updates metadata properties on a file in OneDrive.|
|1/23/26|Upload file|Uploads a file to OneDrive.|
||Download file|Downloads a file from OneDrive.|

|12/12/25|Create folder|Creates a new folder in OneDrive at a specified path.|
|---|---|---|
||Copy file|Copies a file in OneDrive from a source to a<br>destination.|

Microsoft Outlook 

|Launch<br>date|Action|Description|
|---|---|---|
|9/22/26|Create message|Creates a new draft email message in the signed-in<br>user's mailbox.|
||Reply to message|Replies to an email message.|
||Update message|Updates an existing draft email message in the<br>signed-in user's mailbox.|
|9/17/26|Add attachments|Adds an attachment to an existing message.|
||Forward mail|Forwards an email message.|
||Move mail|Moves an email message to another folder.|
||Create calendar|Creates a new calendar for the signed-in user.|
||Update calendar|Updates an existing calendar for the signed-in user.|
||RSVP to event|Responds (accept, decline, or tentatively accept) to<br>a calendar event invitation.|
||Create Word<br>document|Creates a new Word (.docx) document in the user's<br>OneDrive.|
||Convert Word<br>document to PDF|Converts a Word (.docx) document stored in<br>OneDrive or SharePoint to PDF.|
||Create PowerPoint<br>presentation|Creates a new PowerPoint (.pptx) presentation in<br>the user's OneDrive.|
||Convert PowerPoint to<br>PDF|Converts a PowerPoint (.pptx) presentation stored<br>in OneDrive or SharePoint to PDF.|
|1/23/26|Download attachment|Downloads an attachment from an email.|

|12/19/25|Create contact|Creates a new Outlook contact.|
|---|---|---|
||Update contact|Updates an existing Outlook contact.|
|12/12/25|Create event|Creates a new event.|
||Update event|Updates an existing event.|
||Send mail|Sends an email, including attachments.|

Microsoft SharePoint 

|Launch<br>date|Action|Description|
|---|---|---|
|9/17/26|Discard check out<br>document|Discards the check out of a document in a<br>SharePoint library.|
||Share resource|Shares a file, folder, or site in SharePoint with<br>specified recipients.|
||Update file properti  i|i esUpdates metadata fields on a document in a<br>SharePoint library.|
||Update page|Updates an existing page on a SharePoint site.|
||Update list|Updates properties of an existing SharePoint list.|
||Create list item|Creates a new item in a SharePoint list.|
||Update list item|Updates an existing item in a SharePoint list.|
||List lists|Lists all SharePoint lists on a site.|
||Get list item|Retrieves a specific item from a SharePoint list.|
||Get list fields|Retrieves column field definitions for a SharePoint<br>list.|

|3/11/26|Add page|Creates a new page on the SharePoint site.|
|---|---|---|
||Check out document|Checks out a document from a SharePoint library.|
||Check in document|Checks a document into a SharePoint library.|
||Rename attachment<br>or document|Renames an attachment or a document in a<br>SharePoint library.|
||Move attachment or<br>document|Moves a document from a SharePoint library to a<br>destination library, folder, or another SharePoint site.|
|1/23/26|Upload document|Uploads a file to a SharePoint list item.|
||Download document|Downloads a file attached to a SharePoint list item.|
|12/12/25|Create folder|Creates a new folder in a specified path.|
|Micros|Add list<br>oft Teams|Creates a new structured data list (for example,<br>tasks, contacts) on SharePoint.|
|Launch<br>date|Action|Description|

|9/17/26|Update channel<br>message|Updates an existing message in a Microsoft Teams<br>channel.|
|---|---|---|
||Update chat message|Updates an existing message in a Microsoft Teams<br>chat.|
||Create channel|Creates a new channel in a Microsoft Teams team.|
||Update channel|Updates an existing channel in a Microsoft Teams<br>team.|
||Create chat|Creates a new chat in Microsoft Teams.|
||Update chat|Updates an existing chat in Microsoft Teams.|
||Add member to<br>channel|Adds a member to a Microsoft Teams channel.|
||Create schedule|Creates a schedule for a team in Microsoft Teams<br>Shifts.|
||Create time off entry|Creates a time-off entry in Microsoft Teams Shifts.|
||Update time off entry|Updates an existing time-off entry in Microsoft<br>Teams Shifts.|
|12/19/25|Send channel<br>message|Sends a message to a specified channel.|
||Send chat message|Sends a message in a chat.|

Miro 

|Launch date|Action|Description|
|---|---|---|
|8/11/26|Create doc|Create doc|
||Update doc|Update doc|

Monday 

|Launch<br>date|Action|Description|
|---|---|---|
|3/17/26|Change item column<br>values|Changes the column values of an item in<br>Monday.|
||Create board|Creates a new board in Monday.|
||Create column|Creates a new column in Monday.|
||Create dashboard|Creates a new dashboard in Monday.|
||Create doc|Creates a new doc in Monday.|
||Create form|Creates a new form in Monday.|
||Create group|Creates a new group in Monday.|
||Create item|Creates a new item in Monday.|
|3/4/26|Create workspace|Creates a new workspace in Monday.|

Notion 

|Launch date|Action|Description|
|---|---|---|
|03/11/26|Create database|Creates a new database in Notion.|
||Update database|Updates the attributes of a database in Notion.|
||Create page|Creates a new page in Notion.|
||Update page|Updates attributes of a Notion page.|
|2/19/26|Create comment|Creates a new comment on a Notion page or block.|

PagerDuty 

|Launch<br>date|Action|Description|
|---|---|---|

|5/25/26|Create incident|Create an incident synchronously without a corresponding<br>event from a monitoring service.|
|---|---|---|
||Update incident|Acknowledge, resolve, escalate, or reassign an incident.|
||Add note to<br>incident|Add a note to an incident's timeline.|
||Create service|Create a new service.|
||Update service|Update an existing service.|
||Create user|Create a new user account in PagerDuty.|
||Update user|Update an existing user's details.|
||Create on-call<br>override|Create an override for a specific user covering a specified<br>time range on a schedule.|
||Search|Search for incidents, services, users, schedules, and<br>escalation policies.|
||List on-call<br>entries|List the on-call entries during a given time range.|
||List log entries|Get the full timeline of an incident.|

Salesforce 

|Launch date|Action|Description|
|---|---|---|
|6/23/26|Create case|Creates a case in Salesforce.|

ServiceM8 

|Launch<br>date|Action|Description|
|---|---|---|

|7/31/26|Add job note|Adds a note to a job specified by its UUID.|
|---|---|---|
||Change job status|Change the status of a job.|
||Compose email<br>message|Compose and send an email message linked to a Job<br>UUID.|
||Create job|Create a new job with client and scheduling<br>information.|
||Create job activity|Create a scheduled booking for a staff member to<br>attend the job.|
||Send job to queue|Send a job to a queue with expiry date.|

ServiceNow 

|Launch<br>date|Action|Description|
|---|---|---|
|12/12/25|Create<br>incident|Creates a new ServiceNow incident to report and track<br>service interruptions.|
||Update<br>incident|Updates an existing ServiceNow incident using its system<br>ID.|

Shopify 

|Launch<br>date|Action|Description|
|---|---|---|
|3/11/26|Create order|Creates a new order in Shopify.|
||Send fulfillment<br>request|Sends a fulfillment request for an order on your<br>Shopify site.|
|3/4/26|Create customer|Creates a new customer in Shopify.|
||Update customer|Updates an existing customer in Shopify.|

Smartsheet 

|Launch<br>date|Action|Description|
|---|---|---|
|8/11/26|Add rows|Adds one or more new rows to a sheet.|
|7/29/26|Add favorites|Marks one or more assets (sheets, reports, dashboards,<br>folders, workspaces, or templates) as favorites for the current<br>user.|
||Create sheet|Creates a new sheet in a folder or workspace, either from<br>scratch with custom column definitions or based on an<br>existing template.|
||Create<br>workspace|Creates a new workspace.|
||Update rows|Updates one or more rows in a sheet.|

Slack 

|Launch date|Action|Description|
|---|---|---|
|5/26/26|Send Slack message|Send a Slack message.|
||Schedule Slack message|Schedule a Slack message.|
||Create Slack canvas|Create a Slack canvas.|
||Send Slack message draft|Send a Slack message draft.|

Streak 

Launch Action Description date 

|8/30/26|Add call log|Add a call log entry to a box with notes and<br>duration.|
|---|---|---|
||Add thread to box|Add a Gmail thread to a box.|
||Assign box|Assign a box to users by email address.|
||Create box|Create a new box in a pipeline.|
||Create comment|Create a new top-level comment on a box.|
||Create contact|Create a team contact and link it to a box.|
||Create organization|Create a team organization and link it to a box.|
||Create task|Create a new task in a box.|
||Regenerate box<br>summary|Regenerate and return a fresh AI summary for a<br>box.|
||Update box|Update a box.|
||Update box stage|Move a box to a different stage in its pipeline.|
||Update task|Update a task.|

Supabase 

|Launch<br>date|Action|Description|
|---|---|---|
|8/17/26|Apply<br>migration|Applies a migration to the database.|
||Deploy edge<br>function|Deploys an Edge Function to a Supabase project. If the<br>function already exists, this will create a new version.|
||Execute SQL|Executes raw SQL in the Postgres database.|
||Pause project|Pauses a Supabase project.|
||Restore projec|t Restores a Supabase project.|

Windsor.ai 

|Launch<br>date|Action|Description|
|---|---|---|
|09/10/26|Contact<br>Windsor|Send feedback, support, or feature requests to<br>Windsor.ai.|
||Execute action|Execute a write action on a Windsor.ai connector<br>account.|
|Wrike<br>Launch da|te Action|Description|
|5/15/26|Create folder/|project<br>Create a new folder/project in Wrike.|
|6/5/26|Create task|Create a new task in Wrike.|
||Update folder/|project<br>Update an existing folder/project in Wrike.|
||Update task|Update an existing task in Wrike.|

Zendesk 

|Launch date|Action|Description|
|---|---|---|
|3/4/26|Update article|Updates an existing article in Zendesk.|
|2/19/26|Update ticket|Updates an existing ticket in Zendesk.|
||Create category|Creates a new category in Zendesk.|
||Update post|Updates a post in Zendesk.|
||Merge tickets|Merges multiple tickets in Zendesk.|
||Add a comment to a ticket|Adds a comment to a ticket in Zendesk.|
|1/30/26|Create ticket|Creates a new ticket in Zendesk.|

Zoho Books 

|Launch<br>date|Action|Description|
|---|---|---|
|5/15/26|Create Contact|Create a new contact in zohobooks.|
||Create Customer<br>Payment|Create a new customer payment in zohobooks.|
||Create Estimate|Create a new estimate in zohobooks.|
||Create Invoice|Create a new invoice in zohobooks.|
||Create Item|Create a new item in zohobooks.|
||Create Purchase Order|Create a new purchase order in zohobooks.|
||Create Sales Order|Create a new sales order in zohobooks.|
||Create Tax|Create a new tax in zohobooks.|
||Update Contact|Update an existing contact in zohobooks.|
||Update Estimate|Update an existing estimate in zohobooks.|
||Update Invoice|Update an existing invoice in zohobooks.|
||Update Item|Update an existing item in zohobooks.|
||Update Purchase Order|Update an existing purchase order in<br>zohobooks.|
||Update Sales Order|Update an existing sales order in zohobooks.|
|Zoho<br>Launch d|Desk<br>ate Action|Description|
|8/28/26|Update event|Updates the details of an event.|

|6/23/26|Create call|Creates a new call.|
|---|---|---|
||Send reply|Sends an email reply.|
||Update call|Updates the details of a call.|
||Update task|Updates the details of a task.|
|5/15/26|Create event|Adds an event entry to your help desk portal.|
||Create task|Creates a task in your help desk portal.|
||Create ticket|Creates a ticket in your helpdesk.|
||Create ticket comment|Adds a comment to a ticket.|
||Mark ticket as read|Marks a ticket as read by the user.|
||Update ticket|Updates the details of an existing ticket.|
|7/12/26|Update ticket comment|Updates a comment on a ticket.|

Zoho Projects 

|Launch da|te Action|Description|
|---|---|---|
|5/15/26|Create task list|Add a Task list to the project.|
||Update issue|Update an issue in a project.|
||Update phase|Update a phase in a project.|
||Update task|Modify details of the task in a project.|
|6/5/26|Create default tasklist|Create default tasklist for a project.|
||Create phase|Create a phase in a project.|
||Create project issue|Create an issue in a project.|
||Update project|Modify details of an existing project.|

|6/23/26|Create project|Create a new project in the Zoho Projects portal.|
|---|---|---|
||Create task|Add a task to the project.|
||Update task list|Modify details of the task list in a project.|

ZoomInfo 

|Launch<br>date|Action|Description|
|---|---|---|
|7/12/26|Submit|Use this tool to submit feedback on ZoomInfo MCPs or other|
||feedback|feedback for ZoomInfo.|

Last updated 2026-10-15 UTC.
