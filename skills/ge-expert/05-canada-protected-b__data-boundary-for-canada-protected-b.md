# Canada Protected B, Assured Workloads and access controls / Data Boundary for Canada Protected B
Source: 05-Canada-Protected-B-Assured-Workloads-and-access-controls.pdf, pages 31-52, extracted 2026-10-18

## Data Boundary for Canada Protected B

URL: https://docs.cloud.google.com/assured-workloads/docs/control-packages/canada-protected-b

This page describes the set of controls that are applied on Data Boundary for Canada Protected B workloads in Assured Workloads. It provides detailed information about data residency (/assured-workloads/docs/data-residency), supported Google Cloud products (#products_endpoints) and their API endpoints, and any applicable restrictions or limitations (#restrictions_limitations) on those products. The following additional information applies to Data Boundary for Canada Protected B: 

- **Data residency** : The Data Boundary for Canada Protected B control package sets data location controls to support Canada-only regions 

- (/assured-workloads/docs/locations#americas). See the Google Cloud-wide organization policy constraints (#org_cloud) section for more information. 

- **Support** : Technical support services for Data Boundary for Canada Protected B workloads are available with Enhanced or Premium Cloud Customer Care (/support) subscriptions. Data Boundary for Canada Protected B workloads support cases are routed to Canadian support personnel who have completed Reliability Status screenings. See Getting support 

- (/assured-workloads/docs/getting-support#ca-protected-b) for more information. 

- **Pricing** : The Data Boundary for Canada Protected B control package is included in Assured Workloads' _Premium tier_ , which incurs a 5% additional charge. See Assured Workloads pricing 

- (https://cloud.google.com/assured-workloads/pricing) for more information. 

### Supported products and API endpoints

Unless otherwise noted, users can access all supported products through the Google Cloud console. Restrictions or limitations that affect the features of a supported product, including those that are enforced through organization policy constraint settings 

(/resource-manager/docs/organization-policy/overview#how_organization_policy_works), are listed in the following table. 

If a product is not listed, that product is unsupported and has not met the control requirements for Data Boundary for Canada Protected B. Unsupported products are not recommended for use without due diligence and a thorough understanding of your responsibilities in the shared responsibility model 

(/assured-workloads/docs/shared-responsibility). Before using an unsupported product, ensure that you are aware of and are willing to accept any associated risks involved, such as negative impacts to data residency or data sovereignty. 

**Note** : Unsupported products may share an API service endpoint with supported products, making them available to all users. 

**Important** : Google Cloud MCP servers (/mcp/overview) aren't supported for any Data Boundary for Canada Protected B products unless otherwise noted. Data Boundary for Canada Protected B doesn't provide data residency controls for in-use data and in-transit data with Google Cloud MCP servers. It's your responsibility to ensure that Google Cloud MCP servers endpoints aren't used with any Data Boundary for Canada Protected B products. To block unwanted Google Cloud MCP servers access, see the Control Google Cloud MCP servers use with IAM (/mcp/control-mcp-use-iam) page. 

Type a product or service name to filter 

|Supported product<br>|API endpoints|Restrictions or limitations|
|---|---|---|
|Access Approval|`accessapproval.`|None|
|(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`||
|Access Context Manager|`accesscontextmana`|`ge`<br>None|
|(/access-context-manager/docs/overview)|`r.googleapis.com`||
|Access Transparency|`accessapproval.`|None|
|(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`||
|Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|None|

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Agent Search|`discoveryengine.`|None|
|(/gemini-enterprise-agent-<br>platform/models/vertex-ai-search)|`googleapis.com`||
|AlloyDB for PostgreSQL<br>(/alloydb/docs/overview)|`alloydb.googleapis.`<br>`com`|None|
|Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|None|
|Apigee Hybrid<br>(/apigee/docs/hybrid/latest/what-is-hybrid)|`apigee.googleapis.`<br>`com`|None|
|App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|None|
|Artifact Registry<br>(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|None|
|AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|None|
|Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-<br>for-gke)|`gkebackup.`<br>`googleapis.com`|None|
|BigQuery(/bigquery/docs/introduction)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection.`<br>`googleapis.com`<br>`bigquerydatapolicy.`<br>`googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservation`<br>`.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|Affected features<br>(#features_bigquery)|
|BigQuery Data Transfer Service|`bigquerydatatransfe`|None|
|(/bigquery/docs/dts-introduction)|`r.googleapis.com`||

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|None|
|Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`.googleapis.com`|`n`<br>None|
|Certificate Authority Service<br>(/certificate-authority-service/docs/ca-<br>service-overview)|`privateca.`<br>`googleapis.com`|None|
|Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`googleapis.com`|`.`<br>None|
|Cloud Asset Inventory|`cloudasset.`|None|
|(/asset-inventory/docs/asset-inventory-<br>overview)|`googleapis.com`||
|Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|None|
|Cloud Data Fusion<br>(/data-fusion/docs/concepts/overview)|`datafusion.`<br>`googleapis.com`|None|
|Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|None|
|Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|None|
|Cloud Domains(/domains/docs/overview)|`domains.googleapis`<br>`com`|`.`<br>None|
|Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|None|
|Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|None|
|Cloud Interconnect|`compute.googleapis`|`.`<br>None|
|(/network-connectivity/docs/interconnect)|`com`||

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|None|
|Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-<br>overview)|`compute.googleapis.`<br>`com`|None|
|Cloud Logging(/logging/docs/overview)|`logging.googleapis.`<br>`com`|Affected features<br>(#features_logging)|
|Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)|`monitoring.`<br>`googleapis.com`|None|
|Cloud NAT(/nat/docs/overview)|`compute.googleapis.`<br>`com`|None|
|Cloud OS Login API(/compute/docs/oslogin)|`oslogin.googleapis.`<br>`com`|None|
|Cloud Router<br>(/network-connectivity/docs/router)|`compute.googleapis.`<br>`com`|None|
|Cloud Run<br>(/run/docs/overview/what-is-cloud-run)|`run.googleapis.com`|Affected features<br>(#features_run)|
|Cloud Run functions<br>(/run/docs/functions-with-run)|`cloudfunctions.`<br>`googleapis.com`|None|
|Cloud Run functions(/functions/docs)|`run.googleapis.com`|None|
|Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|None|
|Cloud Service Mesh<br>(/service-mesh/docs/overview)|`mesh.googleapis.com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`networkservices.`<br>`googleapis.com`|None|

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|None|
|Cloud SQL for PostgreSQL<br>(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|None|
|Cloud Storage(/storage/docs/introduction)|`storage.googleapis.`<br>`com`|None|
|Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|None|
|Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|None|
|Cloud VPN|`compute.googleapis.`|Affected features|
|(/network-<br>connectivity/docs/vpn/concepts/overview)|`com`|(#features_vpn)|
|Cloud Workstations<br>(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|None|
|Compliance Manager<br>(/security-command-<br>center/docs/compliance-manager-overview)|`cloudsecuritycompli`<br>`ance.googleapis.com`|None|
|Compute Engine(/compute/docs/overview)|`compute.googleapis.`<br>`com`|Affected features<br>(#features_compute) and<br>organization policy<br>constraints(#org_compute)|
|Config Sync<br>(/kubernetes-engine/config-<br>sync/docs/overview)|`anthosconfigmanagem`<br>`ent.googleapis.com`|None|
|Database Center|`Not applicable`|None|
|(/database-center/docs/overview)|||

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|None|
|Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|None|
|Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|None|
|Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|None|
|Essential Contacts<br>(/resource-manager/docs/managing-<br>notification-contacts)|`essentialcontacts.`<br>`googleapis.com`|None|
|Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|None|
|External passthrough Network Load<br>Balancer<br>(/load-balancing/docs/passthrough-network-<br>load-balancer)|`compute.googleapis`<br>`com`|`.`<br>None|
|Filestore(/filestore/docs/overview)|`file.googleapis.co`|`m`None|
|Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|None|
|Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|None|
|Generative AI on Vertex AI|`aiplatform.`|None|
|(/vertex-ai/generative-<br>ai/docs/learn/overview)|`googleapis.com`||

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)|`compute.googleapis.`<br>`com`<br>`networksecurity.`<br>`googleapis.com`|Affected features<br>(#features_armor)|
|Google Cloud Managed Service for Apache<br>Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|None|
|Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|Affected features<br>(#features_netapp_volumes)|
|Google Kubernetes Engine (GKE)|`container.`|None|
|(/kubernetes-<br>engine/docs/concepts/kubernetes-engine-<br>overview)|`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`||
|Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect|)<br>`gkeconnect.`<br>`googleapis.com`|None|
|Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|None|
|Google Kubernetes Engine (GKE) Identity<br>Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication|)<br>`anthosidentityservi`<br>`ce.googleapis.com`|None|
|Google Kubernetes Engine (GKE) Image<br>streaming<br>(/kubernetes-engine/docs/how-to/image-<br>streaming)|`containerfilesystem`<br>`.googleapis.com`|None|
|Google Security Operations SIEM<br>(/security/products/security-information-<br>event-management)|`chronicle.`<br>`googleapis.com`<br>`chronicleserviceman`<br>`ager.googleapis.com`|None|
|Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|None|

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|None|
|Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|None|
|Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|None|
|Internal passthrough Network Load Balanc<br>(/load-balancing/docs/internal)|er<br>`compute.googleapis`<br>`com`|`.`<br>None|
|Knowledge Catalog<br>(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|Affected features<br>(#features_dataplex)|
|Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|None|
|Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-<br>overview)|`composer.`<br>`googleapis.com`|None|
|Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|None|
|Memorystore for Redis<br>(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|None|
|Network Connectivity Center<br>(/network-connectivity/docs/network-<br>connectivity-center/concepts/overview)|`networkconnectivit`<br>`.googleapis.com`|`y`<br>None|
|Organization Policy Service|`orgpolicy.`|None|
|(/resource-manager/docs/organization-|`googleapis.com`||
|policy/using-constraints)|||

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.googleapis`<br>`com`|`.`<br>None|
|Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|None|
|Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|None|
|Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.googleapis`<br>`com`|`.`<br>None|
|Regional external proxy Network Load<br>Balancer<br>(/load-balancing/docs/tcp#regional-<br>external-proxy-network-load-balancer)|`compute.googleapis`<br>`com`|`.`<br>None|
|Regional internal Application Load Balancer<br>(/load-balancing/docs/l7-internal)|`compute.googleapis`<br>`com`|`.`<br>None|
|Regional internal proxy Network Load<br>Balancer<br>(/load-balancing/docs/tcp#regional-internal-<br>proxy-network-load-balancer)|`compute.googleapis`<br>`com`|`.`<br>None|
|Resource Manager<br>(/resource-manager/docs/resource-<br>manager-overview)|`cloudresourcemanag`<br>`r.googleapis.com`|`e`<br>None|
|Secret Manager<br>(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|None|
|Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`.googleapis.com`|`r`<br>None|
|Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`|None|
||`googleapis.com`||

|Supported product|API endpoints|Restrictions or limitations|
|---|---|---|
|Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-<br>data-protection-overview)|`dlp.googleapis.com`|None|
|Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|None|
|Service Directory<br>(/service-directory/docs/overview)|`servicedirectory.`<br>`googleapis.com`|None|
|Spanner(/spanner/docs)|`spanner.googleapis`<br>`com`|`.`<br>None|
|Speech-to-Text|`speech.googleapis.`|None|
|(/speech-to-text/docs/overview)|`com`||
|Storage Transfer Service|`storagetransfer.`|None|
|(/storage-transfer/docs/overview)|`googleapis.com`||
|Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|None|
|Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|None|
|Vertex AI Pipelines|`aiplatform.`|None|
|(/vertex-ai/docs/pipelines)|`googleapis.com`||
|Vertex AI Training|`aiplatform.`|None|
|(/vertex-ai/docs/training-overview)|`googleapis.com`||
|Virtual Private Cloud (VPC)|`compute.googleapis`|`.`<br>None|
|(/vpc/docs/overview)|`com`||
|VM Manager|`osconfig.`|None|
|(/compute/vm-manager/docs/overview)|`googleapis.com`||

|Supported product|API endpoints<br>Restrictions or limitations|
|---|---|
|VPC Service Controls|`accesscontextmanage`<br>None|
|(/vpc-service-controls/docs/overview)|`r.googleapis.com`<br>`accesscontextintell`<br>`igence.googleapis.`<br>`com`|
|Web Risk(/web-risk/docs/overview)|`webrisk.googleapis.`<br>`com`<br>None|
|Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`<br>None|
|Workload Identity Federation|`iam.googleapis.com`<br>None|
|(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

### Restrictions and limitations

The following sections describe Google Cloud-wide or product-specific restrictions or limitations for features, including any organization policy constraints that are set by default on Data Boundary for Canada Protected B folders. Other applicable organization policy constraints—even if not set by default—can provide additional defense-in-depth to further protect your organization's Google Cloud resources. 

We strongly recommend not changing the values of the required organization policy constraints listed in the following sections. Doing so may undermine data residency. When such a change has been made, the effects of the change are difficult or impossible to reverse. Ensure that you understand the ramifications of changing an organization policy constraint's value before proceeding. 

Additionally, ensure that any automated mechanisms your organization uses to manage organization policies are updated to prevent these values from being changed unintentionally. 

#### Google Cloud-wide

Google Cloud-wide organization policy constraints 

The following organization policy constraints 

(/resource-manager/docs/organization-policy/org-policy-constraints) apply across Google Cloud. 

|Organization policy constraint|Description|
|---|---|
|`gcp.resourceLocations`<br>(/resource-<br>manager/docs/organization-<br>policy/defining-locations)|Set to the following locations in the`allowedValues`list:<br>`ca`<br>`northamerica-northeast1`<br>`northamerica-northeast2`<br>This value restricts creation of new resources to the<br>selected values. When set, no resources can be created in<br>any other regions, multi-regions, or locations outside of the<br>selection. See<br>Resource locations supported services<br>(/resource-manager/docs/organization-policy/defining-<br>locations-supported-services)<br>for a list of resources that can be restricted by the<br>Resource Locations organization policy constraint, as some<br>resources may be out of scope and cannot be restricted.<br>Changing this value by making it less restrictive potentially<br>undermines data residency by allowing data to be created<br>or stored outside of a compliant data boundary.|
|`gcp.restrictServiceUsage`<br>(/resource-<br>manager/docs/organization-<br>policy/restricting-resources)|Set to allow all<br>supported products and API endpoints<br>(#products_endpoints).<br>Determines which services can be used by restricting<br>runtime access to their resources. For more information,<br>see<br>Restricting resource usage<br>(/resource-manager/docs/organization-policy/restricting-<br>resources)<br>.|

|Organization policy constraint|Description|
|---|---|
|`gcp.restrictTLSVersion`|Set to deny the following TLS versions:|
|(/docs/security/compliance/restr<br>tls-versions)|ict-<br>`TLS_1_0`|
||`TLS_1_1`|
||For more information, see<br>Restrict TLS versions<br>(/docs/security/compliance/restrict-tls-versions).|

#### BigQuery

Affected BigQuery features 

|Feature|Description|
|---|---|
|Enabling BigQuer|y on<br>BigQuery is supported, but it isn't automatically enabled when you create|
|a new folder|Workloads folder due to an internal configuration process. This process no<br>ten minutes, but can take much longer in some circumstances. To check w|
||is finished and to enable BigQuery, complete the following steps:|
||1. In the Google Cloud console, go to the Assured Workloads page.|

Go to Assured Workloads (https://console.cloud.google.com/compliance 2. Select your new Assured Workloads folder from the list. 

3. On the Folder Details page in the Allowed services section, click Review 

4. In the Allowed services pane, review the services to be added to the Re Restriction (/resource-manager/docs/organization-policy/restricting-res policy for the folder. If BigQuery services are listed, click Allow Services If BigQuery services are not listed, wait for the internal process to com are not listed within 12 hours of folder creation, contact Cloud Custome 

After the enablement process is completed, you can use BigQuery in your folder. 

Gemini in BigQuery is not supported by Assured Workloads. 

|Feature|Description|
|---|---|
|Unsupported feature|s The following BigQuery features are not supported and should not be use<br>CLI. It is your responsibility not to use them in BigQuery for Assured Work<br>Interaction with remote data sources<br>Externally-trained BQML models<br>(/bigquery/docs/bqml-introduction#externally_trained_models) are not<br>Internally-trained BQML models<br>(/bigquery/docs/bqml-introduction#internally_trained_models) are sup<br>Data masking with policy tags<br>(/bigquery/docs/column-data-masking#mask_data_with_policy_tags) is<br>Data masking by applying data policies directly to columns<br>(/bigquery/docs/column-data-masking#data-policies-on-column) is sup<br>GDrive export<br>Remote functions(/bigquery/docs/reference/standard-sql/remote-funct<br>Saved queries(/bigquery/docs/work-with-saved-queries)<br>Workflow scheduling<br>For BigQuery Studio,<br>notebooks(/bigquery/docs/create-notebooks) are<br>Gemini in BigQuery is not supported.|
|BigQuery CLI<br>(/bigquery/docs/bq-<br>command-line-tool)|The BigQuery CLI is supported.|
|Google Cloud SDK|You must use Google Cloud SDK version 403.0.0 or newer to maintain dat<br>guarantees for technical data. To verify your current Google Cloud SDK ve<br>`-version`and then`gcloud components update`to update to the newest|
|Administrator control        fi|sBigQuery will disable unsupported APIs but administrators with sufficient<br>create Assured Workloads folders can enable an unsupported API. If this o<br>notified of potential non-compliance through the<br>Assured Workloads moni<br>(/assured-workloads/docs/monitor-folder).|
|Loading data|BigQuery Data Transfer Service connectors<br>(/bigquery/docs/dts-introduction#supported_data_sources) for Google So<br>(SaaS) apps, external cloud storage providers, and data warehouses are n<br>your responsibility not to use BigQuery Data Transfer Service connectors f<br>for Canada Protected B workloads.|

|Feature|Description|
|---|---|
|Third-party transfers<br>(/bigquery/docs/third-<br>party-transfer)|BigQuery doesn't verify support for third-party transfers for the BigQuery<br>Service. It is your responsibility to verify support when using any third-pa<br>BigQuery Data Transfer Service.|
|Non-compliant BQML<br>models|Externally-trained BQML models<br>(/bigquery/docs/bqml-introduction#externally_trained_models) are not su|
|Query jobs|Query jobs should only be created within Assured Workloads folders.|
|Queries on datasets<br>in other projects|BigQuery doesn't prevent Assured Workloads datasets from being queried<br>Workloads projects. You should ensure that any query that has a read or a<br>Workloads data be placed in Assured Workloads folders. You can specify a<br>name(/bigquery/docs/reference/bq-cli-reference#bq_query) for their quer<br>`projectname.dataset.table`in the BigQuery CLI.|
|Cloud Logging|BigQuery utilizes Cloud Logging for some of your log data. You should disa<br>logging buckets or restrict`_default`buckets to in-scope regions to maint<br>using the following command:|
||`gcloud alpha logging settings update --organization=ORGANIZATI`<br>`default-sink`|
||For more information, see<br>Regionalize your logs(/logging/docs/regionalize|

#### Cloud Interconnect

Affected Cloud Interconnect features 

|Feature|Description|
|---|---|
|High-availability (HA) VPN|You must enable high-availability (HA) VPN functionality when<br>using Cloud Interconnect with Cloud VPN. Additionally, you<br>must adhere to the encryption and regionalization<br>requirements listed in the<br>Affected Cloud VPN features<br>(#features_vpn) section.|

#### Cloud Logging

Affected Cloud Logging features 

To use Cloud Logging with Customer-managed encryption keys (CMEK), you must complete the steps in the Enable CMEK for an organization (/logging/docs/routing/managed-encryption#enable) page in the Cloud Logging documentation. 

|Feature|Description|
|---|---|
|Log sinks<br>(/logging/docs/export/configure_export_v|i2)<br>Filters shouldn't contain Customer Data.<br>Log sinks include filters which are stored as<br>configuration. Don't create filters that contain<br>Customer Data.|
|Live tailing log entries<br>(/logging/docs/view/streaming-live-tailin|g)<br>Filters shouldn't contain Customer Data.<br>A live tailing session includes a filter which is stored<br>as configuration. Tailing logs doesn't store any log<br>entry data itself, but can query and transmit data<br>across regions. Don't create filters that contain<br>Customer Data.|
|SQL-based alerting policies<br>(/logging/docs/analyze/sql-in-alerting)|This feature is disabled.<br>You cannot use the SQL-based alerting policies<br>feature.|

#### Cloud Monitoring

Affected Cloud Monitoring features 

|Feature|Description|
|---|---|
|Synthetic Monitor<br>(/monitoring/uptime-<br>checks/introduction#about-sm)|This feature is disabled.|
|Uptime checks<br>(/monitoring/uptime-<br>checks/introduction#about-<br>uptime)|This feature is disabled.|

#### Cloud Run

Affected Cloud Run features 

|Feature|Description|
|---|---|
|Unsupported features|The following Cloud Run features aren't supported:|
||Cloud Trace integration(/run/docs/trace)|
||Cloud Run functions(/functions/docs/concepts/overview)|
||Eventarc triggers(/functions/docs/calling/eventarc)|

#### Cloud VPN

Affected Cloud VPN features 

|Feature|Description|
|---|---|
|VPN endpoints|You must use only Cloud VPN endpoints that are located in an<br>in-scope<br>region(#resource_locations). Ensure that your VPN|
||gateway is configured for use in an in-scope region only.|

#### Compute Engine

Affected Compute Engine features 

|Feature|Description|
|---|---|
|Guest environment<br>(/compute/docs/images/guest-<br>environment)|It is possible for scripts, daemons, and binaries that are<br>included with the guest environment to access unencrypted<br>at-rest and in-use data. Depending on your VM configuration,<br>updates to this software may be installed by default. See<br>Guest environment<br>(/compute/docs/images/guest-environment) for specific<br>information about each package's contents, source code, and<br>more.<br>These components help you meet data sovereignty through<br>internal security controls and processes. However, if you want<br>additional control, you can also curate your own images or<br>agents and optionally use the`compute.trustedImage`<br>`Projects`organization policy constraint.|
||For more information, see<br>Building a custom image<br>(/compute/docs/images/building-custom-os).|
|OS policies in VM Manager<br>(/compute/vm-manager/docs/os-<br>policies/working-with-os-policies)|Inline scripts and binary output files within the OS policy files<br>are not encrypted using customer-managed encryption keys<br>(CMEK). Don't include any sensitive information in these files.<br>Consider storing these scripts and output files in Cloud<br>Storage buckets. For more information, see<br>Example OS<br>policies<br>(/compute/vm-manager/docs/os-policies/working-with-os-<br>policies#os-policy)<br>.|

If you want to restrict the creation or modification of OS policy resources that use inline scripts or binary output files, enable the `constraints/osconfig.restrictInlineScript AndOutputFileUsage` organization policy constraint. 

For more information, see Constraints for OS Config (/resource-manager/docs/organization-policy/org-policyconstraints#constraints-for-specific-services) . 

Compute Engine organization policy constraints 

|Organization policy constraint|Description|
|---|---|
|`compute.disableGlobalCloud`<br>`ArmorPolicy`|Set to True.<br>Disables the creation of new global<br>Google Cloud Armor<br>security policies(/armor/docs/security-policy-overview) and<br>the addition or modification of rules to existing global Google<br>Cloud Armor security policies. This constraint doesn't restrict<br>the removal of rules or the ability to remove or change the<br>description and listing of global Google Cloud Armor security<br>policies. Regional Google Cloud Armor security policies are<br>unaffected by this constraint. All global and regional security<br>policies that exist prior to the enforcement of this constraint<br>remain in effect.|
|`compute.restrictNon`<br>`ConfidentialComputing`|(Optional) Value is not set. Set this value to provide additional<br>defense-in-depth. For more information, see the<br>Confidential<br>VM documentation<br>(/confidential-computing/confidential-vm/docs/about-cvm).|
|`compute.trustedImage`<br>`Projects`|(Optional) Value is not set. Set this value to provide additional<br>defense-in-depth.|
||Setting this value constrains image storage and disk<br>instantiation to the specified list of projects. This value affects<br>data sovereignty by preventing use of any unauthorized<br>images or agents.|

#### Knowledge Catalog

Knowledge Catalog features 

|Feature|Description|
|---|---|
|Attribute Store<br>(/dataplex/docs/attribute-store)|This feature is deprecated and disabled.|
|Data Catalog|This feature is deprecated and disabled. You cannot search|
|(/dataplex/docs/catalog-<br>overview)|through nor manage your metadata in Data Catalog.|

|Feature|Description|
|---|---|
|Data insights|This feature is disabled. You cannot generate data insights for|
|(/dataplex/docs/data-insights)|your catalogs.|
|Lakes and Zones|This feature is disabled. You cannot manage lakes, zones and|
|(/dataplex/docs/metadata)|tasks.|

#### Google Cloud NetApp Volumes

Affected Google Cloud NetApp Volumes features 

|Feature|Description|
|---|---|
|Supported service levels|Data Boundary for Canada Protected B supports the|
|(/netapp/volumes/docs/discover<br>levels)|/service-<br>following service levels:<br>Standard|
||Premium|
||Extreme|

#### Spanner

Affected Spanner features 

|Feature|Description|
|---|---|
|Split boundaries|Spanner uses a small subset of primary keys and indexed<br>columns to define<br>split boundaries<br>(/spanner/docs/schema-and-data-model#database-splits),<br>which may include customer data and metadata. A split<br>boundary in Spanner denotes the location where contiguous<br>ranges of rows are split into smaller pieces.|
||These split boundaries are accessible by Google personnel for<br>technical support and debugging purposes, and are not<br>subject to administrative access data controls in Assured<br>Workloads.|

|Organization policy constraint|Description|
|---|---|
|`spanner.assuredWorkloads`|Set to True.|
|`AdvancedServiceControls`|Applies additional data sovereignty and supportability<br>controls to Spanner resources.|
|`spanner.disableMultiRegion`|Set to True.|
|`InstanceIfNoLocation`||
|`Selected`|Disables the ability to create multi-region Spanner instances<br>to enforce data residency and data sovereignty.|

### What's next

Learn how to create an Assured Workloads folder (/assured-workloads/docs/create-folder) 

Understand Assured Workloads pricing 

(https://cloud.google.com/assured-workloads/pricing) 

Last updated 2026-10-13 UTC.
