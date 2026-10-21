# Canada Protected B, Assured Workloads and access controls / Supported products by control package: Supported products by control package
Source: 05-Canada-Protected-B-Assured-Workloads-and-access-controls.pdf, pages 53-350, extracted 2026-10-18

## Supported products by control package

URL: https://docs.cloud.google.com/assured-workloads/docs/supported-products

The following table is a listing of products and services that are supported by Assured Workloads. If a service is not listed for a given control package, that service is unsupported and has not met all regional, regulatory, or sovereign controls required for the control package. Unsupported products are not recommended for use by Assured Workloads customers without due diligence and waivers from your regulatory agencies or divisions. Unauthorized products may share an API service endpoint with authorized products, making them available to all users. 

For more information about Assured Workloads, see Assured Workloads overview (/assured-workloads/docs/overview). 

**Note:** A resource usage restriction 

(/resource-manager/docs/organization-policy/restricting-resources) organization policy may be enabled in your Assured Workloads folder to prevent non-compliant service usage by restricting available resource types. 

Type a product or service name to filter 

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for|Access Context Manager|`accesscontextmanag`|
|Criminal Justice|(/access-context-manager/docs/overview)|`er.googleapis.com`|
|Information Systems<br>(CJIS)<br>(/assured-<br>workloads/docs/control|-<br>Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
|packages/cjis)|Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Application Integration<br>(/application-integration/docs/overview)|`integrations.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Connection API<br>(/bigquery/docs/reference/bigqueryconnection/rest<br>[2] (#2)|)<br>`bigqueryconnection`<br>`.googleapis.com`|
||BigQuery Data Transfer Service|`bigquerydatatransf`|
||(/bigquery/docs/dts-introduction)<br>[2] (#2)|`er.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Bigtable(/bigtable/docs/overview)|`bigtable.`|
|||`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service<br>(/certificate-authority-service/docs/ca-service-<br>overview)|`privateca.`<br>`googleapis.com`|
||Certificate Manager(/certificate-manager/docs)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Identity(/identity)|`cloudidentity.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing|`compute.`|
||(/load-balancing/docs/load-balancing-overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager|`cloudsecuritycompl`|
||(/security-command-center/docs/compliance-<br>manager-overview)|`iance.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Data Security Posture Management<br>(/security-command-center/docs/dspm-data-<br>security)|`Not applicable`|
||Database Center(/database-center/docs/overview)|`databasecenter.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Admin console<br>(https://support.google.com/a/topic/2413312?<br>ref_topic=4388346)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|
||Key Access Justifications<br>(/assured-workloads/key-access-|`cloudekm.`<br>`googleapis.com`|
||justifications/docs/overview)|`cloudkms.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)|`looker.googleapis.`|
||(/looker/docs/looker-core-overview)|`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Model Armor|`modelarmor.`|
||(/security-command-center/docs/model-armor-<br>overview)|`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer|`compute.`|
||(/load-balancing/docs/l7-internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Security Command Center Premium<br>(/security-command-center/docs/security-<br>command-center-overview)|`securitycenter.`<br>`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`|
|||`ligence.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Workbench<br>(/vertex-ai/docs/workbench/notebook-solution)|`notebooks.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workforce Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for<br>FedRAMP High|AI Platform(/vertex-ai/docs)|`aiplatform.`<br>`googleapis.com`|
|(/assured-<br>workloads/docs/control<br>packages#fedramp-<br>high)|-<br>Vertex AI Neural Architecture Search<br>(/vertex-ai/docs/training/neural-architecture-<br>search/overview)|`ml.googleapis.com`|
||AI Platform Training and Prediction API<br>(/vertex-ai/docs/reference/rest)|`aiplatform.`<br>`googleapis.com`|
||AI Platform Data Labeling Service<br>(/ai-platform/data-labeling/docs)|`datalabeling.`<br>`googleapis.com`|
||AI Protection|`securitycenter.`|
||(/security-command-center/docs/ai-protection-<br>overview)|`googleapis.com`|
||Access Approval|`accessapproval.`|
||(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
||Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency|`accessapproval.`|
||(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Engine<br>(/appengine/docs/an-overview-of-app-engine)|`appengine.`<br>`googleapis.com`|
||Application Integration<br>(/application-integration/docs/overview)|`integrations.`<br>`googleapis.com`|
||Artifact Analysis|`containeranalysis.`|
||(/artifact-analysis/docs/artifact-analysis)|`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Assured Open Source Software (Assured OSS)<br>(/assured-open-source-software/docs/overview)|`assuredoss.`<br>`googleapis.com`|
||Assured Workloads<br>(/assured-workloads/docs/overview)|`assuredworkloads.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Natural Language<br>(/natural-language/docs/basics)|`automl.googleapis.`<br>`com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||AutoML Translation(/translate/docs/overview)|`automl.googleapis.`<br>`com`|
||AutoML Video Intelligence(/video-intelligence/docs|)`videointelligence.`<br>`googleapis.com`|
||AutoML Vision(/vision/docs)|`vision.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||Batch(/batch/docs)|`batch.googleapis.`<br>`com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerydatatransf`<br>`er.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`|
|||`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Care Studio (Cloud Healthcare Search)<br>(http://health.google/for-clinicians/care-studio)|`healthcare.`<br>`googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Chrome Enterprise Premium|`beyondcorp.`|
||(/chrome-enterprise-premium/docs/overview)|`googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Billing API(/billing/docs/concepts)<br>[11] (#11)|`billingbudgets.`<br>`googleapis.com`<br>`cloudbilling.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud CDN(/cdn)|`compute.`|
|||`googleapis.com`|
||Google Cloud console(/cloud-console)|`Not applicable`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Deployment Manager<br>(/deployment-manager)|`deploymentmanager.`<br>`googleapis.com`|
||Cloud Endpoints(/endpoints)|`endpoints.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Run functions for Firebase<br>(https://firebase.google.com/docs/functions)|`cloudfunctions.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Healthcare API(/healthcare-api/docs)|`healthcare.`<br>`googleapis.com`|
||Cloud Identity(/identity)|`cloudidentity.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Intrusion Detection System<br>(/intrusion-detection-system)|`ids.googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Life Sciences<br>(https://cloud.google.com/solutions/life-sciences)|`lifesciences.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud Natural Language API<br>(/natural-language/docs)|`language.`<br>`googleapis.com`|
||Cloud Next Generation Firewall Enterprise<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Next Generation Firewall Essentials<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Cloud Next Generation Firewall Standard<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Profiler(/profiler/docs/about-profiler)|`cloudprofiler.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Knative serving<br>(/kubernetes-engine/docs/concepts/gke-and-cloud-<br>run)|`Not applicable`|
||Cloud Run functions(/functions/docs)|`cloudfunctions.`<br>`googleapis.com`<br>`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`|
||Cloud Shell(/shell)<br>[10] (#10)|`cloudshell.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Source Repositories(/source-repositories)|`sourcerepo.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Storage for Firebase<br>(https://firebase.google.com/docs/storage)|`firebasestorage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud Translation(/translate/docs/api-overview)|`translate.`<br>`googleapis.com`<br>`translation.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`connectgateway.`<br>`googleapis.com`<br>`gkeconnect.`<br>`googleapis.com`|
||Container Registry(/artifact-registry/docs/overview|)`containeranalysis.`<br>`googleapis.com`<br>`containerregistry.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Data Catalog(/data-catalog)|`datacatalog.`<br>`googleapis.com`|
||Data Studio(/looker-studio)|`datastudio.`<br>`googleapis.com`|
||Database Migration Service(/database-migration)|`datamigration.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Datastore(/datastore)|`datastore.`<br>`googleapis.com`|
||Datastream(/datastream)|`datastream.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Earth Engine<br>(https://developers.google.com/earth-<br>engine/guides)|`earthengine.`<br>`googleapis.com`<br>`earthengine-`<br>`highvolume.`<br>`googleapis.com`|
||Error Reporting(/error-reporting)|`clouderrorreportin`<br>`g.googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Authentication<br>(https://firebase.google.com/docs/auth)|`Not applicable`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`|
||Google Cloud SDK(/sdk)|`Not applicable`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud Marketplace(/marketplace)|`cloudcommerceconsu`<br>`merprocurement.`<br>`googleapis.com`|
||Google Cloud app(https://cloud.google.com/app)|`Not applicable`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Google Admin console<br>(https://support.google.com/a/topic/2413312?<br>ref_topic=4388346)|`Not applicable`|
||Identity Platform(/identity-platform)|`identitytoolkit.`<br>`googleapis.com`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`<br>`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors|`connectors.`|
||(/integration-connectors/docs/overview)|`googleapis.com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|
||Key Access Justifications|`cloudekm.`|
||(/assured-workloads/key-access-<br>justifications/docs/overview)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)<br>[|9]<br>`dataplex.`|
||(#9)|`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)|`looker.googleapis.`|
||(/looker/docs/looker-core-overview)|`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Network Intelligence Center<br>(/network-intelligence-center/docs/overview)|`networkmanagement.`<br>`googleapis.com`|
||Network Service Tiers(/network-tiers)|`compute.`<br>`googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Privileged Access Manager<br>(/iam/docs/pam-overview)|`privilegedaccessma`<br>`nager.googleapis.`<br>`com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||reCAPTCHA(/recaptcha/docs/overview)|`recaptchaenterpris`<br>`e.googleapis.com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional internal Application Load Balancer<br>(/load-balancing/docs/l7-internal)|`compute.`<br>`googleapis.com`|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Resource Settings<br>(/resource-manager/docs/resource-<br>settings/overview)|`resourcesettings.`<br>`googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Security Command Center|`containerthreatdet`|
||(/security-command-center/docs/security-|`ection.googleapis.`|
||command-center-overview)|`com`<br>`securitycenter.`<br>`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access|`vpcaccess.`|
||(/vpc/docs/configure-serverless-vpc-access)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Service Directory(/service-directory/docs/overview)|`servicedirectory.`<br>`googleapis.com`|
||Service Infrastructure(/service-infrastructure)|`serviceconsumerman`<br>`agement.`<br>`googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Talent Solution(/talent-solution/docs)|`jobs.googleapis.`<br>`com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Forecasting<br>(/vertex-ai/docs/tabular-data/forecasting/overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Tabular Workflows|`aiplatform.`|
||(/vertex-ai/docs/tabular-data/tabular-<br>workflows/overview)|`googleapis.com`|
||Vertex AI Training|`aiplatform.`|
||(/vertex-ai/docs/training-overview)|`googleapis.com`|
||Vertex AI Vector Search<br>(/vertex-ai/docs/vector-search/overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Workbench<br>(/vertex-ai/docs/workbench/notebook-solution)|`notebooks.`<br>`googleapis.com`|
||Vertex ML Metadata(/vertex-ai/docs/ml-metadata)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Structured Data|`aiplatform.`|
||(/vertex-ai/generative-ai/docs/multimodal/control-<br>generated-output)|`googleapis.com`|
||Video Intelligence API(/video-intelligence/docs)|`videointelligence.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`<br>`servicenetworking.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflowexecutions`<br>`.googleapis.com`<br>`workflows.`<br>`googleapis.com`|
||Workforce Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for|AI Platform(/vertex-ai/docs)|`aiplatform.`|
|FedRAMP Moderate||`googleapis.com`|
|(/assured-<br>workloads/docs/control|-<br>Vertex AI Neural Architecture Search|`ml.googleapis.com`|
|packages#fedramp-<br>moderate)|(/vertex-ai/docs/training/neural-architecture-<br>search/overview)||
||AI Platform Training and Prediction API<br>(/vertex-ai/docs/reference/rest)|`aiplatform.`<br>`googleapis.com`|
||AI Protection<br>(/security-command-center/docs/ai-protection-<br>overview)|`securitycenter.`<br>`googleapis.com`|
||Access Approval<br>(/assured-workloads/access-<br>approval/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Engine<br>(/appengine/docs/an-overview-of-app-engine)|`appengine.`<br>`googleapis.com`|
||Application Integration<br>(/application-integration/docs/overview)|`integrations.`<br>`googleapis.com`|
||Artifact Analysis<br>(/artifact-analysis/docs/artifact-analysis)|`containeranalysis.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Assured Open Source Software (Assured OSS)|`assuredoss.`|
||(/assured-open-source-software/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Assured Workloads<br>(/assured-workloads/docs/overview)|`assuredworkloads.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Natural Language<br>(/natural-language/docs/basics)|`automl.googleapis.`<br>`com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||AutoML Translation(/translate/docs/overview)|`automl.googleapis.`<br>`com`|
||AutoML Video Intelligence(/video-intelligence/docs|)`videointelligence.`<br>`googleapis.com`|
||AutoML Vision(/vision/docs)|`vision.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||Batch(/batch/docs)|`batch.googleapis.`<br>`com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerydatatransf`<br>`er.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Bigtable(/bigtable/docs/overview)|`bigtable.`|
|||`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Care Studio (Cloud Healthcare Search)<br>(http://health.google/for-clinicians/care-studio)|`healthcare.`<br>`googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Chrome Enterprise Premium<br>(/chrome-enterprise-premium/docs/overview)|`beyondcorp.`<br>`googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Billing API(/billing/docs/concepts)<br>[11] (#11)|`billingbudgets.`<br>`googleapis.com`<br>`cloudbilling.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud CDN(/cdn)|`compute.`<br>`googleapis.com`|
||Google Cloud console(/cloud-console)|`Not applicable`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Deployment Manager|`deploymentmanager.`|
||(/deployment-manager)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Endpoints(/endpoints)|`endpoints.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Run functions for Firebase<br>(https://firebase.google.com/docs/functions)|`cloudfunctions.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Healthcare API(/healthcare-api/docs)|`healthcare.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Intrusion Detection System<br>(/intrusion-detection-system)|`ids.googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Life Sciences<br>(https://cloud.google.com/solutions/life-sciences)|`lifesciences.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud Natural Language API<br>(/natural-language/docs)|`language.`<br>`googleapis.com`|
||Cloud Next Generation Firewall Enterprise<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Cloud Next Generation Firewall Essentials<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Next Generation Firewall Standard<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Profiler(/profiler/docs/about-profiler)|`cloudprofiler.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Knative serving<br>(/kubernetes-engine/docs/concepts/gke-and-cloud-<br>run)|`Not applicable`|
||Cloud Run functions(/functions/docs)|`cloudfunctions.`<br>`googleapis.com`<br>`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`|
||Cloud Shell(/shell)|`cloudshell.`<br>`googleapis.com`|
||Cloud Source Repositories(/source-repositories)|`sourcerepo.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Storage for Firebase<br>(https://firebase.google.com/docs/storage)|`firebasestorage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud Translation(/translate/docs/api-overview)|`translate.`<br>`googleapis.com`<br>`translation.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`connectgateway.`<br>`googleapis.com`<br>`gkeconnect.`<br>`googleapis.com`|
||Container Registry(/artifact-registry/docs/overview|)`containeranalysis.`<br>`googleapis.com`<br>`containerregistry.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights|`contactcenterinsig`|
||(/contact-center/insights/docs)|`hts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Data Catalog(/data-catalog)|`datacatalog.`<br>`googleapis.com`|
||Data Studio(/looker-studio)|`datastudio.`<br>`googleapis.com`|
||Database Migration Service(/database-migration)|`datamigration.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Datastore(/datastore)|`datastore.`<br>`googleapis.com`|
||Datastream(/datastream)|`datastream.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Earth Engine<br>(https://developers.google.com/earth-<br>engine/guides)|`earthengine.`<br>`googleapis.com`<br>`earthengine-`<br>`highvolume.`<br>`googleapis.com`|
||Error Reporting(/error-reporting)|`clouderrorreportin`<br>`g.googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Game Servers<br>(https://cloud.google.com/solutions/games)|`gameservices.`<br>`googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`|
||Google Cloud SDK(/sdk)|`Not applicable`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud Marketplace(/marketplace)|`cloudcommerceconsu`<br>`merprocurement.`<br>`googleapis.com`|
||Google Cloud App(https://cloud.google.com/app)|`Not applicable`|
||Google Kubernetes Engine (GKE)|`container.`|
||(/kubernetes-engine/docs/concepts/kubernetes-|`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity Platform(/identity-platform)|`identitytoolkit.`<br>`googleapis.com`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`<br>`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors|`connectors.`|
||(/integration-connectors/docs/overview)|`googleapis.com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|
||IoT Core<br>(https://cloud.google.com/architecture/connected-<br>devices/iot-platform-product-architecture)|`cloudiot.`<br>`googleapis.com`|
||Key Access Justifications|`cloudekm.`|
||(/assured-workloads/key-access-<br>justifications/docs/overview)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)<br>[9|]<br>`dataplex.`|
||(#9)|`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)|`looker.googleapis.`|
||(/looker/docs/looker-core-overview)|`com`|
||Managed Service for Apache Airflow|`composer.`|
||(/composer/docs/composer-3/composer-overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Network Intelligence Center<br>(/network-intelligence-center/docs/overview)|`networkmanagement.`<br>`googleapis.com`|
||Network Service Tiers(/network-tiers)|`compute.`<br>`googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Privileged Access Manager<br>(/iam/docs/pam-overview)|`privilegedaccessma`<br>`nager.googleapis.`<br>`com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||reCAPTCHA(/recaptcha/docs/overview)|`recaptchaenterpris`<br>`e.googleapis.com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer|`compute.`|
||(/load-balancing/docs/l7-internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Resource Settings<br>(/resource-manager/docs/resource-<br>settings/overview)|`resourcesettings.`<br>`googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Security Command Center<br>(/security-command-center/docs/security-<br>command-center-overview)|`containerthreatdet`<br>`ection.googleapis.`<br>`com`<br>`securitycenter.`<br>`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Service Directory(/service-directory/docs/overview|)`servicedirectory.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Service Infrastructure(/service-infrastructure)|`serviceconsumerman`<br>`agement.`<br>`googleapis.com`<br>`servicecontrol.`<br>`googleapis.com`<br>`servicemanagement.`<br>`googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Talent Solution(/talent-solution/docs)|`jobs.googleapis.`<br>`com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-online-predictions)|`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Tabular Workflows<br>(/vertex-ai/docs/tabular-data/tabular-<br>workflows/overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Vector Search|`aiplatform.`|
||(/vertex-ai/docs/vector-search/overview)|`googleapis.com`|
||Vertex AI Workbench<br>(/vertex-ai/docs/workbench/notebook-solution)|`notebooks.`<br>`googleapis.com`|
||Vertex ML Metadata(/vertex-ai/docs/ml-metadata)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Structured Data<br>(/vertex-ai/generative-ai/docs/multimodal/control-<br>generated-output)|`aiplatform.`<br>`googleapis.com`|
||Video Intelligence API(/video-intelligence/docs)|`videointelligence.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`<br>`servicenetworking.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflowexecutions`<br>`.googleapis.com`<br>`workflows.`<br>`googleapis.com`|
||Workforce Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|US Data Boundary for<br>Healthcare and Life|Access Approval<br>(/assured-workloads/access-|`accessapproval.`<br>`googleapis.com`|
|Sciences|approval/docs/overview)||
|(/assured-<br>workloads/docs/control<br>packages/us-data-|-<br>Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
|boundary-healthcare-<br>life-sciences)|Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||Application Integration<br>(/application-integration/docs/overview)|`integrations.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`aiplatform.`<br>`googleapis.com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerydatatransf`<br>`er.googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service<br>(/certificate-authority-service/docs/ca-service-<br>overview)|`privateca.`<br>`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion<br>(/data-fusion/docs/concepts/overview)|`datafusion.`<br>`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Healthcare API(/healthcare-api/docs)|`healthcare.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring|`monitoring.`|
||(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`<br>`networkservices.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights|`contactcenterinsig`|
||(/contact-center/insights/docs)|`hts.googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Identity and Access Management (IAM)|`iam.googleapis.com`|
||(/iam/docs/overview)|`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Internal passthrough Network Load Balancer|`compute.`|
||(/load-balancing/docs/internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Key Access Justifications|`cloudekm.`|
||(/assured-workloads/key-access-<br>justifications/docs/overview)|`googleapis.com`<br>`cloudkms.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Model Armor|`modelarmor.`|
||(/security-command-center/docs/model-armor-<br>overview)|`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer|`compute.`|
||(/load-balancing/docs/l7-internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Security Command Center Premium<br>(/security-command-center/docs/security-<br>command-center-overview)|`securitycenter.`<br>`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-batch-predictions)|`googleapis.com`|
||Vertex AI Online prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-online-predictions)|<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Workbench<br>(/vertex-ai/docs/workbench/notebook-solution)|`notebooks.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|US Data Boundary for|Access Approval|`accessapproval.`|
|Healthcare and Life|(/assured-workloads/access-|`googleapis.com`|
|Sciences with Support|approval/docs/overview)||
|(/assured-<br>workloads/docs/control<br>packages/us-data-|-<br>Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
|boundary-healthcare-<br>life-sciences-support)|Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||Application Integration<br>(/application-integration/docs/overview)|`integrations.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerydatatransf`<br>`er.googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service<br>(/certificate-authority-service/docs/ca-service-<br>overview)|`privateca.`<br>`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion<br>(/data-fusion/docs/concepts/overview)|`datafusion.`<br>`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Healthcare API(/healthcare-api/docs)|`healthcare.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring|`monitoring.`|
||(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`<br>`networkservices.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights|`contactcenterinsig`|
||(/contact-center/insights/docs)|`hts.googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Identity and Access Management (IAM)|`iam.googleapis.com`|
||(/iam/docs/overview)|`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Internal passthrough Network Load Balancer|`compute.`|
||(/load-balancing/docs/internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Key Access Justifications|`cloudekm.`|
||(/assured-workloads/key-access-<br>justifications/docs/overview)|`googleapis.com`<br>`cloudkms.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Model Armor|`modelarmor.`|
||(/security-command-center/docs/model-armor-<br>overview)|`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer|`compute.`|
||(/load-balancing/docs/l7-internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Security Command Center Premium<br>(/security-command-center/docs/security-<br>command-center-overview)|`securitycenter.`<br>`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-batch-predictions)|`googleapis.com`|
||Vertex AI Online prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-online-predictions)|<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Workbench<br>(/vertex-ai/docs/workbench/notebook-solution)|`notebooks.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for<br>Impact Level 2 (IL2)<br>(/assured-|AI Protection<br>(/security-command-center/docs/ai-protection-<br>overview)|`securitycenter.`<br>`googleapis.com`|
|workloads/docs/control<br>packages/il2)|-<br>Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Config Management(/kubernetes-engine/docs)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Engine<br>(/appengine/docs/an-overview-of-app-engine)|`appengine.`<br>`googleapis.com`|
||Application Integration<br>(/application-integration/docs/overview)|`integrations.`<br>`googleapis.com`|
||Artifact Analysis<br>(/artifact-analysis/docs/artifact-analysis)|`containeranalysis.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Assured Open Source Software (Assured OSS)<br>(/assured-open-source-software/docs/overview)|`assuredoss.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||Backup and DR Service|`backupdr.`|
||(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`|
|||`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`|
|||`googleapis.com`<br>`bigtableadmin.`|
|||`googleapis.com`|
||Binary Authorization|`binaryauthorizatio`|
||(/binary-authorization/docs/overview)|`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager(/certificate-manager/docs)|`certificatemanager`<br>`.googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`|
||Cloud Asset Inventory|`cloudasset.`|
||(/asset-inventory/docs/asset-inventory-overview)|`googleapis.com`|
||Cloud Billing API(/billing)<br>[11] (#11)|`billingbudgets.`|
|||`googleapis.com`<br>`cloudbilling.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)<br>[7] (#7)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Data Fusion<br>(/data-fusion/docs/concepts/overview)|`datafusion.`<br>`googleapis.com`|
||Cloud Deploy(/deploy/docs)|`clouddeploy.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Run functions(/run/docs/functions-with-run)|`cloudfunctions.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Identity(/identity)|`cloudidentity.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Intrusion Detection System<br>(/intrusion-detection-system/docs/overview)|`ids.googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud Next Generation Firewall Enterprise<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Cloud Next Generation Firewall Essentials<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Next Generation Firewall Standard<br>(/firewall/docs/about-firewalls)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud Translation(/translate/docs/api-overview)|`translation.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`connectgateway.`<br>`googleapis.com`<br>`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#|8)`discoveryengine.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud Marketplace(/marketplace/docs)|`Not applicable`|
||Google Cloud App(https://cloud.google.com/app)|`Not applicable`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Google Admin console<br>(https://support.google.com/a/topic/2413312?<br>ref_topic=4388346)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`<br>`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors|`connectors.`|
||(/integration-connectors/docs)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Looker (Google Cloud core)|`looker.googleapis.`|
||(/looker/docs/looker-core-overview)|`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Model Armor|`modelarmor.`|
||(/security-command-center/docs/model-armor-<br>overview)|`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Network Intelligence Center<br>(/network-intelligence-center/docs/overview)|`networkmanagement.`<br>`googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Privileged Access Manager<br>(/iam/docs/pam-overview)|`privilegedaccessma`<br>`nager.googleapis.`<br>`com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Security Command Center|`containerthreatdet`|
||(/security-command-center/docs/security-<br>command-center-overview)|`ection.googleapis.`<br>`com`<br>`securitycenter.`<br>`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Service Directory(/service-directory/docs/overvie|w)`servicedirectory.`<br>`googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Vector Search<br>(/vertex-ai/docs/vector-search/overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Workbench<br>(/vertex-ai/docs/workbench/notebook-solution)|`aiplatform.`<br>`googleapis.com`<br>`notebooks.`<br>`googleapis.com`|
||Vertex AI batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex ML Metadata(/vertex-ai/docs/ml-metadata)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Structured Data<br>(/vertex-ai/generative-ai/docs/multimodal/control-<br>generated-output)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Video Intelligence API(/video-intelligence/docs)|`videointelligence.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for|Access Context Manager|`accesscontextmanag`|
|Impact Level 4 (IL4)|(/access-context-manager/docs/overview)|`er.googleapis.com`|
|(/assured-<br>workloads/docs/control<br>packages/il4)|-<br>AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||Certificate Authority Service<br>(/certificate-authority-service/docs/ca-service-<br>overview)|`privateca.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)<br>[7] (#7)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Identity(/identity)|`cloudidentity.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)|`cloudkms.`|
||(/kms/docs/key-management-service)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`<br>`monitoring.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Kubernetes Engine (GKE) Connect Agent<br>(/kubernetes-engine/fleet-<br>management/docs/connect-agent)|`connectgateway.`<br>`googleapis.com`<br>`gkeconnect.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Google Admin console<br>(https://support.google.com/a/topic/2413312?<br>ref_topic=4388346)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`<br>`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer|`compute.`|
||(/load-balancing/docs/https#regional-td)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer<br>(/load-balancing/docs/l7-internal)|`compute.`<br>`googleapis.com`|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Spanner(/spanner/docs)<br>[3] (#3)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||VPC Service Controls<br>(/vpc-service-controls/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`<br>`servicenetworking.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for|Access Context Manager|`accesscontextmanag`|
|Impact Level 5 (IL5)|(/access-context-manager/docs/overview)|`er.googleapis.com`|
|(/assured-<br>workloads/docs/control<br>packages/il5)|-<br>AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||Certificate Authority Service<br>(/certificate-authority-service/docs/ca-service-<br>overview)|`privateca.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)<br>[7] (#7)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Identity(/identity)|`cloudidentity.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)|`cloudkms.`|
||(/kms/docs/key-management-service)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`us-vision.`<br>`googleapis.com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Kubernetes Engine (GKE) Connect Agent<br>(/kubernetes-engine/fleet-<br>management/docs/connect-agent)|`gkeconnect.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE)|`container.`|
||(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM|`chronicle.`|
||(/security/products/security-information-event-<br>management)|`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Admin console<br>(https://support.google.com/a/topic/2413312?<br>ref_topic=4388346)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc.`<br>`googleapis.com`<br>`dataproc-control.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer|`compute.`|
||(/load-balancing/docs/l7-internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Spanner(/spanner/docs)<br>[3] (#3)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Training|`aiplatform.`|
||(/vertex-ai/docs/training-overview)|`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for<br>International Traffic in<br>Arms Regulations<br>|Access Approval<br>(/assured-workloads/access-<br>approval/docs/overview)|`accessapproval.`<br>`googleapis.com`|
|(ITAR)<br>(/assured-<br>workloads/docs/control|-<br>Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
|packages/itar)|AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee<br>(/apigee/docs/api-platform/get-started/what-<br>apigee)|`apigee.googleapis.`<br>`com`|
||Artifact Analysis<br>(/artifact-analysis/docs/artifact-analysis)|`containeranalysis.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Certificate Authority Service<br>(/certificate-authority-service/docs/ca-service-<br>overview)|`privateca.`<br>`googleapis.com`|
||Certificate Manager(/certificate-manager/docs)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Billing API(/billing/docs/concepts)<br>[11] (#11)|`billingbudgets.`<br>`googleapis.com`<br>`cloudbilling.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)<br>Cloud Service Mesh(/service-mesh/docs/overview)|`sqladmin.`<br>`googleapis.com`<br> `mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`<br>`networkservices.`<br>`googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`datastore.`|
|||`googleapis.com`<br>`firestore.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub (fleets)<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||GKE Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`<br>`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|
||Jurisdictional Google Cloud console<br>(/assured-workloads/docs/jurisdictional-console)|`Not applicable`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Key Access Justifications|`cloudekm.`|
||(/assured-workloads/key-access-<br>justifications/docs/overview)|`googleapis.com`<br>`cloudkms.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer|`compute.`|
||(/load-balancing/docs/l7-internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Security Command Center Premium|`containerthreatdet`|
||(/security-command-center/docs/security-<br>command-center-overview)|`ection.googleapis.`<br>`com`<br>`securitycenter.`<br>`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Service Directory(/service-directory/docs/overview)|`servicedirectory.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`<br>`servicenetworking.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for IRS|AI Protection|`securitycenter.`|
|Publication 1075|(/security-command-center/docs/ai-protection-|`googleapis.com`|
|(/assured-|overview)||
|workloads/docs/control<br>|-<br>Access Context Manager|`accesscontextmanag`|
|packages/irs-1075)|(/access-context-manager/docs/overview)|`er.googleapis.com`|
||Access Transparency|`accessapproval.`|
||(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Application Integration<br>(/application-integration/docs/overview)|`integrations.`<br>`googleapis.com`|
||Artifact Analysis<br>(/artifact-analysis/docs/artifact-analysis)|`containeranalysis.`<br>`googleapis.com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`aiplatform.`<br>`googleapis.com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Connection API<br>(/bigquery/docs/reference/bigqueryconnection/rest<br>[2] (#2)|)<br>`bigqueryconnection`<br>`.googleapis.com`|
||BigQuery Data Transfer Service|`bigquerydatatransf`|
||(/bigquery/docs/dts-introduction)<br>[2] (#2)|`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization|`binaryauthorizatio`|
||(/binary-authorization/docs/overview)|`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory|`cloudasset.`|
||(/asset-inventory/docs/asset-inventory-overview)|`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Google Cloud console(/cloud-console)|`Not applicable`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Run functions(/run/docs/functions-with-run)|`cloudfunctions.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Healthcare API(/healthcare-api/docs)|`healthcare.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler)|`cloudscheduler.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud TPU(/tpu/docs/intro-to-tpu)|`tpu.googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Data Security Posture Management|`securitycenter.`|
||(/security-command-center/docs/dspm-data-<br>security)|`googleapis.com`|
||Database Center(/database-center/docs/overview)|`databasecenter.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Authentication<br>(https://firebase.google.com/docs/auth)|`Not applicable`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs)|`connectors.`<br>`googleapis.com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|
||Jurisdictional Google Cloud console<br>(/assured-workloads/docs/jurisdictional-console)|`Not applicable`|
||Key Access Justifications|`cloudekm.`|
||(/assured-workloads/key-access-<br>justifications/docs/overview)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Looker (Google Cloud core)|`looker.googleapis.`|
||(/looker/docs/looker-core-overview)|`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Memorystore for Redis Cluster<br>(/memorystore/docs/cluster/memorystore-for-redis<br>cluster-overview)|-<br>`redis.googleapis.`<br>`com`|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer|`compute.`|
||(/load-balancing/docs/l7-internal)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Security Command Center Premium<br>(/security-command-center/docs/security-<br>command-center-overview)|`securitycenter.`<br>`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training|`aiplatform.`|
||(/vertex-ai/docs/training-overview)|`googleapis.com`|
||Vertex AI Tuning<br>(/vertex-ai/generative-ai/docs/models/tune-models|)<br>`aiplatform.`<br>`googleapis.com`|
||Vertex AI Workbench<br>(/vertex-ai/docs/workbench/notebook-solution)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workforce Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Australia Data|Access Approval|`accessapproval.`|
|Boundary|(/assured-workloads/access-|`googleapis.com`|
|(/assured-|approval/docs/overview)||
|workloads/docs/control-<br>|Access Context Manager|`accesscontextmanag`|
|packages/australia-<br>data-boundary)|(/access-context-manager/docs/overview)|`er.googleapis.com`|
||Access Transparency|`accessapproval.`|
||(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Run functions(/run/docs/functions-with-run)|`cloudfunctions.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench|`aiplatform.`|
||(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Kubernetes Engine (GKE)|`container.`|
||(/kubernetes-engine/docs/concepts/kubernetes-|`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access|`vpcaccess.`|
||(/vpc/docs/configure-serverless-vpc-access)|`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Australia Data|Access Approval|`accessapproval.`|
|Boundary and Support<br>(/assured-|(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
|workloads/docs/control-<br>packages/australia-<br>data-boundary-support)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency|`accessapproval.`|
||(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench|`aiplatform.`|
||(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes|`netapp.googleapis.`|
||(/netapp/volumes/docs)|`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Kubernetes Engine (GKE)|`container.`|
||(/kubernetes-engine/docs/concepts/kubernetes-|`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access|`vpcaccess.`|
||(/vpc/docs/configure-serverless-vpc-access)|`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Brazil Data Boundary|Access Approval|`accessapproval.`|
|(/assured-|(/assured-workloads/access-|`googleapis.com`|
|workloads/docs/control-|approval/docs/overview)||
|packages/brazil-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors|`connectors.`|
||(/integration-connectors/docs/overview)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Personalized Service Health|`servicehealth.`|
||(/service-health/docs/overview)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Canada Data Boundary|Access Approval|`accessapproval.`|
|(/assured-<br>workloads/docs/control-|(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
|packages/canada-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency|`accessapproval.`|
||(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-|`container.`<br>`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor|`modelarmor.`|
||(/security-command-center/docs/model-armor-<br>overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service|`storagetransfer.`|
||(/storage-transfer/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Canada Data Boundary|Access Approval|`accessapproval.`|
|and Support<br>(/assured-|(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
|workloads/docs/control-<br>packages/canada-data-<br>boundary-support)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-|`container.`<br>`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor|`modelarmor.`|
||(/security-command-center/docs/model-armor-<br>overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service|`storagetransfer.`|
||(/storage-transfer/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training|`aiplatform.`|
||(/vertex-ai/docs/training-overview)|`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for|Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
|Canada Controlled<br>Goods Program (CGP)<br>(/assured-|Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
|workloads/docs/control|-<br>Cloud Key Management Service (Cloud KMS)|`cloudkms.`|
|packages/canada-<br>|(/kms/docs/key-management-service)|`googleapis.com`|
|controlled-goods-<br>program)|Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)|`monitoring.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer<br>(/load-balancing/docs/l7-internal)|`compute.`<br>`googleapis.com`|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Data Boundary for<br>Canada Protected B<br>(/assured-|Access Approval<br>(/assured-workloads/access-<br>approval/docs/overview)|`accessapproval.`<br>`googleapis.com`|
|workloads/docs/control<br>packages/canada-<br>protected-b)|-<br>Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee Hybrid<br>(/apigee/docs/hybrid/latest/what-is-hybrid)|`apigee.googleapis.`<br>`com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service<br>(/certificate-authority-service/docs/ca-service-<br>overview)|`privateca.`<br>`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion<br>(/data-fusion/docs/concepts/overview)|`datafusion.`<br>`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Run functions(/run/docs/functions-with-run)|`cloudfunctions.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)|`cloudkms.`|
||(/kms/docs/key-management-service)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`networkservices.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||External passthrough Network Load Balancer<br>(/load-balancing/docs/passthrough-network-load-<br>balancer)|`compute.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Internal passthrough Network Load Balancer<br>(/load-balancing/docs/internal)|`compute.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health|`servicehealth.`|
||(/service-health/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Regional external Application Load Balancer<br>(/load-balancing/docs/https#regional-td)|`compute.`<br>`googleapis.com`|
||Regional external proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-external-proxy-<br>network-load-balancer)|<br>`compute.`<br>`googleapis.com`|
||Regional internal Application Load Balancer<br>(/load-balancing/docs/l7-internal)|`compute.`<br>`googleapis.com`|
||Regional internal proxy Network Load Balancer<br>(/load-balancing/docs/tcp#regional-internal-proxy-<br>network-load-balancer)|`compute.`<br>`googleapis.com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Service Directory(/service-directory/docs/overview|)`servicedirectory.`<br>`googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Chile Data Boundary|Access Approval|`accessapproval.`|
|(/assured-|(/assured-workloads/access-|`googleapis.com`|
|workloads/docs/control|-<br>approval/docs/overview)||
|packages/chile-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench|`aiplatform.`|
||(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)|`iap.googleapis.com`|
||(/iap/docs/concepts-overview)||

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|EU Data Boundary|AI Protection|`securitycenter.`|
|(/assured-<br>workloads/docs/contr|ol-<br>(/security-command-center/docs/ai-protection-<br>overview)|`googleapis.com`|
|packages/eu-data-<br>boundary)|Access Approval<br>(/assured-workloads/access-<br>approval/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service|`bigquerydatatransf`|
||(/bigquery/docs/dts-introduction)<br>[2] (#2)|`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization|`binaryauthorizatio`|
||(/binary-authorization/docs/overview)|`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`|
|||`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Data Security Posture Management<br>(/security-command-center/docs/dspm-data-<br>security)|`Not applicable`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`|
|||`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Security Command Center|`securitycenter.`|
||(/security-command-center/docs/security-<br>command-center-overview)|`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-batch-predictions)|`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Tuning<br>(/vertex-ai/generative-ai/docs/models/tune-models|)<br>`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|EU Data Boundary and|AI Protection|`securitycenter.`|
|Support|(/security-command-center/docs/ai-protection-|`googleapis.com`|
|(/assured-|overview)||
|workloads/docs/control-<br>|Access Approval|`accessapproval.`|
|packages/eu-data-<br>boundary-support)|(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
||Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service|`bigquerydatatransf`|
||(/bigquery/docs/dts-introduction)<br>[2] (#2)|`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization|`binaryauthorizatio`|
||(/binary-authorization/docs/overview)|`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`|
|||`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Data Security Posture Management<br>(/security-command-center/docs/dspm-data-<br>security)|`Not applicable`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`|
|||`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Security Command Center|`securitycenter.`|
||(/security-command-center/docs/security-<br>command-center-overview)|`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-batch-predictions)|`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Tuning<br>(/vertex-ai/generative-ai/docs/models/tune-models|)<br>`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|EU Data Boundary with|Access Context Manager|`accesscontextmanag`|
|Access Justifications|(/access-context-manager/docs/overview)|`er.googleapis.com`|
|(/assured-<br>workloads/docs/control-|Access Transparency<br>|`accessapproval.`<br>|
|packages/eu-data-<br>boundary-access-|(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
|justifications)|AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`<br>`networkservices.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`<br>`connectgateway.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`<br>`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`<br>`servicenetworking.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Hong Kong Data|Access Approval|`accessapproval.`|
|Boundary|(/assured-workloads/access-|`googleapis.com`|
|(/assured-|approval/docs/overview)||
|workloads/docs/control-<br>k/hk|Access Context Manager|`accesscontextmanag`|
|pacagesong-ong-<br>data-boundary)|(/access-context-manager/docs/overview)|`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench|`aiplatform.`|
||(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)|`iap.googleapis.com`|
||(/iap/docs/concepts-overview)||

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|India Data Boundary|Access Approval|`accessapproval.`|
|(/assured-<br>workloads/docs/control|-<br>(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
|packages/india-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency|`accessapproval.`|
||(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-|`container.`<br>`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor|`modelarmor.`|
||(/security-command-center/docs/model-armor-<br>overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service|`storagetransfer.`|
||(/storage-transfer/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training|`aiplatform.`|
||(/vertex-ai/docs/training-overview)|`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Indonesia Data|Access Approval|`accessapproval.`|
|Boundary|(/assured-workloads/access-|`googleapis.com`|
|(/assured-|approval/docs/overview)||
|workloads/docs/control-<br>k/idi|Access Context Manager|`accesscontextmanag`|
|pacagesnonesa-<br>data-boundary)|(/access-context-manager/docs/overview)|`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer|`networkmanagement.`|
||(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)|`container.`|
||(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`|
|||`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Israel Data Boundary|Access Approval|`accessapproval.`|
|(/assured-<br>workloads/docs/control|-<br>(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
|packages/israel-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency|`accessapproval.`|
||(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`|
|||`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors|`connectors.`|
||(/integration-connectors/docs/overview)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Personalized Service Health|`servicehealth.`|
||(/service-health/docs/overview)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Israel Data Boundary<br>and Support<br>(/assured-|Access Approval<br>(/assured-workloads/access-<br>approval/docs/overview)|`accessapproval.`<br>`googleapis.com`|
|workloads/docs/control<br>packages/israel-data-<br>boundary-support)|-<br>Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors|`connectors.`|
||(/integration-connectors/docs/overview)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Personalized Service Health|`servicehealth.`|
||(/service-health/docs/overview)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Japan Data Boundary|Access Approval|`accessapproval.`|
|(/assured-<br>workloads/docs/control|-<br>(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
|packages/japan-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency|`accessapproval.`|
||(/assured-workloads/access-<br>transparency/docs/overview)|`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`|
|||`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>|`bigquerydatatransf`|
||(/bigquery/docs/dts-introduction)<br>[2] (#2)|`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`|
|||`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization|`binaryauthorizatio`|
||(/binary-authorization/docs/overview)|`n.googleapis.com`|
||Certificate Authority Service<br>i|`privateca.`|
||(/certificate-authority-service/docs)|`googleapis.com`|
||Certificate Manager|`certificatemanager`|
||(/certificate-manager/docs/overview)|`.googleapis.com`|
||Cloud Asset Inventory|`cloudasset.`|
||(/asset-inventory/docs/asset-inventory-overview)|`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`|
|||`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`|
|||`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-|`container.`<br>`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`|
|||`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`|
|||`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Kingdom of Saudi|Access Approval|`accessapproval.`|
|Arabia (KSA) Data|(/assured-workloads/access-|`googleapis.com`|
|Boundary with Access|approval/docs/overview)||
|Justifications<br>|Access Context Manager|`accesscontextmanag`|
|(/assured-<br>workloads/docs/control|-<br>(/access-context-manager/docs/overview)|`er.googleapis.com`|
|packages/ksa-data-<br>boundary-access-<br>i|Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
|justifications)|BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Certificate Authority Service<br>(/certificate-authority-service/docs/ca-service-<br>overview)|`privateca.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)|`cloudkms.`|
||(/kms/docs/key-management-service)|`googleapis.com`|
||Cloud Load Balancing|`compute.`|
||(/load-balancing/docs/load-balancing-overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`trafficdirector.`<br>`googleapis.com`<br>`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`<br>`connectgateway.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`|
||Google Cloud console(/cloud-console)|`Not applicable`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Identity and Access Management (IAM)|`iam.googleapis.com`|
||(/iam/docs/overview)|`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Service Directory(/service-directory/docs/overview|)`servicedirectory.`<br>`googleapis.com`|
||Spanner(/spanner/docs)|`spanner.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`|
|||`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`<br>`servicenetworking.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Qatar Data Boundary|Access Approval|`accessapproval.`|
|(/assured-<br>workloads/docs/control-|(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
|packages/qatar-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors|`connectors.`|
||(/integration-connectors/docs/overview)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Personalized Service Health|`servicehealth.`|
||(/service-health/docs/overview)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Singapore Data|Access Approval|`accessapproval.`|
|Boundary<br>(/assured-|(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
|workloads/docs/control-<br>packages/singapore-<br>data-boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-|`container.`<br>`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor|`modelarmor.`|
||(/security-command-center/docs/model-armor-<br>overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service|`storagetransfer.`|
||(/storage-transfer/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training|`aiplatform.`|
||(/vertex-ai/docs/training-overview)|`googleapis.com`|
||Vertex AI Tuning<br>(/vertex-ai/generative-ai/docs/models/tune-models|)<br>`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|South Africa Data|Access Approval|`accessapproval.`|
|Boundary|(/assured-workloads/access-|`googleapis.com`|
|(/assured-|approval/docs/overview)||
|workloads/docs/control-<br>|Access Context Manager|`accesscontextmanag`|
|packages/south-africa-<br>data-boundary)|(/access-context-manager/docs/overview)|`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors|`connectors.`|
||(/integration-connectors/docs/overview)|`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Personalized Service Health|`servicehealth.`|
||(/service-health/docs/overview)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|South Korea Data|Access Approval|`accessapproval.`|
|Boundary|(/assured-workloads/access-|`googleapis.com`|
|(/assured-|approval/docs/overview)||
|workloads/docs/control-<br>k/thk|Access Context Manager|`accesscontextmanag`|
|pacagessou-orea-<br>data-boundary)|(/access-context-manager/docs/overview)|`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health|`servicehealth.`|
||(/service-health/docs/overview)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection|`dlp.googleapis.com`|
||(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)||
||Serverless VPC Access|`vpcaccess.`|
||(/vpc/docs/configure-serverless-vpc-access)|`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Switzerland Data|Access Approval|`accessapproval.`|
|Boundary|(/assured-workloads/access-|`googleapis.com`|
|(/assured-|approval/docs/overview)||
|workloads/docs/control<br>packages/switzerland-<br>data-boundary)|-<br>Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`<br>`opsconfigmonitorin`<br>`g.googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`aiplatform.`<br>`googleapis.com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`cloudfunctions.`<br>`googleapis.com`<br>`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`|
|||`googleapis.com`|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`connectgateway.`<br>`googleapis.com`<br>`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`databasecenter.`<br>`googleapis.com`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Datastore(/datastore)|`datastore.`|
|||`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`compute.`<br>`googleapis.com`<br>`logging.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor|`compute.`|
||(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Cloud Observability(/stackdriver/docs)|`stackdriver.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)|`iam.googleapis.com`|
||(/iam/docs/overview)|`policytroubleshoot`<br>`er.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)|`looker.googleapis.`|
||(/looker/docs/looker-core-overview)|`com`|
||Managed Service for Apache Airflow|`composer.`|
||(/composer/docs/composer-3/composer-overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection|`dlp.googleapis.com`|
||(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)||

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Serverless VPC Access<br>i|`vpcaccess.`|
||(/vpc/docs/configure-serverless-vpc-access)|`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training|`aiplatform.`|
||(/vertex-ai/docs/training-overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Workbench<br>(/vertex-ai/docs/workbench/notebook-solution)|`notebooks.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`<br>`servicenetworking.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflowexecutions`<br>`.googleapis.com`<br>`workflows.`<br>`googleapis.com`|
||Workload Identity Federation<br>(/iam/docs/workforce-identity-federation)|`iam.googleapis.com`|
|Switzerland Data<br>Boundary with Access<br>Justifications<br>(/assured-|Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`<br>`policytroubleshoot`<br>`er.googleapis.com`|
|workloads/docs/control-<br>packages/switzerland-<br>data-boundary-access-<br>justifications)|Resource Manager<br>(/resource-manager/docs/resource-manager-<br>overview)|`cloudresourcemanag`<br>`er.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|Taiwan Data Boundary|Access Approval|`accessapproval.`|
|(/assured-|(/assured-workloads/access-|`googleapis.com`|
|workloads/docs/control-|approval/docs/overview)||
|packages/taiwan-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect|`compute.`|
||(/network-connectivity/docs/interconnect)|`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules|`firebaserules.`|
||(https://firebase.google.com/docs/rules)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Personalized Service Health|`servicehealth.`|
||(/service-health/docs/overview)|`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager<br>(/secure-source-manager/docs/overview)|`securesourcemanage`<br>`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager|`osconfig.`|
||(/compute/vm-manager/docs/overview)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|
||Vertex AI Model Registry|`aiplatform.`|
||(/vertex-ai/docs/model-registry)|`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|UK Data Boundary|Access Approval|`accessapproval.`|
|(/assured-|(/assured-workloads/access-|`googleapis.com`|
|workloads/docs/control|-<br>approval/docs/overview)||
|packages/uk-data-<br>boundary)|Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|
||Backup for Google Kubernetes Engine (GKE)|`gkebackup.`|
||(/kubernetes-engine/docs/add-on/backup-for-gke)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service<br>(/bigquery/docs/dts-introduction)<br>[2] (#2)|`bigquerydatatransf`<br>`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization<br>(/binary-authorization/docs/overview)|`binaryauthorizatio`<br>`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`<br>`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN|`compute.`|
||(/network-<br>connectivity/docs/vpn/concepts/overview)|`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`<br>`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise Agent Platform Workbench|`aiplatform.`|
||(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Kubernetes Engine (GKE)|`container.`|
||(/kubernetes-engine/docs/concepts/kubernetes-|`googleapis.com`|
||engine-overview)|`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk<br>(/compute/docs/disks/persistent-disks)|`compute.`<br>`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|`networkservices.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access|`vpcaccess.`|
||(/vpc/docs/configure-serverless-vpc-access)|`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction<br>(/vertex-ai/docs/predictions/get-batch-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Monitoring<br>(/vertex-ai/docs/model-monitoring)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|US Data Boundary|AI Protection|`securitycenter.`|
|(/assured-<br>workloads/docs/contr|ol-<br>(/security-command-center/docs/ai-protection-<br>overview)|`googleapis.com`|
|packages/us-data-<br>boundary)|Access Approval<br>(/assured-workloads/access-<br>approval/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service|`bigquerydatatransf`|
||(/bigquery/docs/dts-introduction)<br>[2] (#2)|`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization|`binaryauthorizatio`|
||(/binary-authorization/docs/overview)|`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`|
|||`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Data Security Posture Management<br>(/security-command-center/docs/dspm-data-<br>security)|`Not applicable`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`|
|||`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Security Command Center|`securitycenter.`|
||(/security-command-center/docs/security-<br>command-center-overview)|`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-batch-predictions)|`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Tuning<br>(/vertex-ai/generative-ai/docs/models/tune-models|)<br>`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
|US Data Boundary and|AI Protection|`securitycenter.`|
|Support|(/security-command-center/docs/ai-protection-|`googleapis.com`|
|(/assured-|overview)||
|workloads/docs/control-<br>|Access Approval|`accessapproval.`|
|packages/us-data-<br>boundary-support)|(/assured-workloads/access-<br>approval/docs/overview)|`googleapis.com`|
||Access Context Manager<br>(/access-context-manager/docs/overview)|`accesscontextmanag`<br>`er.googleapis.com`|
||Access Transparency<br>(/assured-workloads/access-<br>transparency/docs/overview)|`accessapproval.`<br>`googleapis.com`|
||Agent Assist(/agent-assist/docs)|`dialogflow.`<br>`googleapis.com`|
||AlloyDB for PostgreSQL(/alloydb/docs/overview)|`alloydb.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`mesh.googleapis.`<br>`com`<br>`meshca.googleapis.`<br>`com`<br>`meshconfig.`<br>`googleapis.com`|
||Apigee(/apigee/docs)|`apigee.googleapis.`<br>`com`|
||App Hub(/app-hub/docs/overview)|`apphub.googleapis.`<br>`com`|
||Artifact Registry(/artifact-registry/docs/overview)|`artifactregistry.`<br>`googleapis.com`|
||Audit Manager(/audit-manager/docs/overview)|`auditmanager.`<br>`googleapis.com`|
||AutoML Tables<br>(/vertex-ai/docs/beginner/beginners-guide)|`automl.googleapis.`<br>`com`|
||Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-<br>dr)|`backupdr.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Backup for Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/add-on/backup-for-gke)|`gkebackup.`<br>`googleapis.com`|
||BigQuery(/bigquery/docs/introduction)<br>[2] (#2)|`bigquery.`<br>`googleapis.com`<br>`bigqueryconnection`<br>`.googleapis.com`<br>`bigquerydatapolicy`<br>`.googleapis.com`<br>`bigquerymigration.`<br>`googleapis.com`<br>`bigqueryreservatio`<br>`n.googleapis.com`<br>`bigquerystorage.`<br>`googleapis.com`|
||BigQuery Data Transfer Service|`bigquerydatatransf`|
||(/bigquery/docs/dts-introduction)<br>[2] (#2)|`er.googleapis.com`|
||Bigtable(/bigtable/docs/overview)|`bigtable.`<br>`googleapis.com`<br>`bigtableadmin.`<br>`googleapis.com`|
||Binary Authorization|`binaryauthorizatio`|
||(/binary-authorization/docs/overview)|`n.googleapis.com`|
||Certificate Authority Service|`privateca.`|
||(/certificate-authority-service/docs/ca-service-<br>overview)|`googleapis.com`|
||Certificate Manager<br>(/certificate-manager/docs/overview)|`certificatemanager`<br>`.googleapis.com`|
||Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-overview)|`cloudasset.`<br>`googleapis.com`|
||Cloud Build(/build/docs/overview)|`cloudbuild.`|
|||`googleapis.com`|
||Cloud DNS(/dns/docs/overview)|`dns.googleapis.com`|
||Cloud Data Fusion|`datafusion.`|
||(/data-fusion/docs/concepts/overview)|`googleapis.com`|
||Cloud Deploy(/deploy/docs/overview)|`clouddeploy.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Domains(/domains/docs/overview)|`domains.`<br>`googleapis.com`|
||Cloud External Key Manager (Cloud EKM)<br>(/kms/docs/ekm)|`cloudkms.`<br>`googleapis.com`|
||Cloud HSM(/kms/docs/hsm)|`cloudkms.`<br>`googleapis.com`|
||Cloud Interconnect<br>(/network-connectivity/docs/interconnect)|`compute.`<br>`googleapis.com`|
||Cloud Key Management Service (Cloud KMS)<br>(/kms/docs/key-management-service)|`cloudkms.`<br>`googleapis.com`|
||Cloud Load Balancing<br>(/load-balancing/docs/load-balancing-overview)|`compute.`<br>`googleapis.com`|
||Cloud Logging(/logging/docs/overview)|`logging.`<br>`googleapis.com`|
||Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>[6] (#6)|`monitoring.`<br>`googleapis.com`|
||Cloud NAT(/nat/docs/overview)|`compute.`<br>`googleapis.com`|
||Cloud OS Login API(/compute/docs/oslogin)|`oslogin.`<br>`googleapis.com`|
||Cloud Router(/network-connectivity/docs/router)|`compute.`<br>`googleapis.com`|
||Cloud Run(/run/docs/overview/what-is-cloud-run)<br>[5] (#5)|`run.googleapis.com`|
||Cloud Run functions(/functions/docs)|`run.googleapis.com`|
||Cloud SQL(/sql/docs/introduction)|`sqladmin.`<br>`googleapis.com`|
||Cloud SQL for PostgreSQL(/sql/docs/postgres)|`sqladmin.`<br>`googleapis.com`|
||Cloud Scheduler(/scheduler/docs/overview)|`cloudscheduler.`<br>`googleapis.com`|
||Cloud Storage(/storage/docs/introduction)|`storage.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Cloud Tasks(/tasks/docs/dual-overview)|`cloudtasks.`<br>`googleapis.com`|
||Cloud Trace(/trace/docs/overview)|`cloudtrace.`<br>`googleapis.com`|
||Cloud VPN<br>(/network-<br>connectivity/docs/vpn/concepts/overview)|`compute.`<br>`googleapis.com`|
||Cloud Vision API(/vision/docs/features-list)|`vision.googleapis.`<br>`com`|
||Cloud Workstations(/workstations/docs/overview)|`workstations.`<br>`googleapis.com`|
||Compliance Manager<br>(/security-command-center/docs/compliance-<br>manager-overview)|`cloudsecuritycompl`<br>`iance.googleapis.`<br>`com`|
||Compute Engine(/compute/docs/overview)|`compute.`<br>`googleapis.com`|
||Config Sync<br>(/kubernetes-engine/config-sync/docs/overview)|`anthosconfigmanage`<br>`ment.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Connect<br>(/anthos/multicluster-management/connect)|`gkeconnect.`<br>`googleapis.com`|
||Dialogflow CX(/dialogflow/cx/docs)|`dialogflow.`<br>`googleapis.com`|
||Customer Experience Insights<br>(/contact-center/insights/docs)|`contactcenterinsig`<br>`hts.googleapis.com`|
||Data Security Posture Management<br>(/security-command-center/docs/dspm-data-<br>security)|`Not applicable`|
||Database Center(/database-center/docs/overview)|`Not applicable`|
||Dataflow(/dataflow/docs/overview)|`dataflow.`|
|||`googleapis.com`<br>`datapipelines.`<br>`googleapis.com`|
||Dataform(/dataform/docs/overview)|`dataform.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Document AI(/document-ai/docs)|`documentai.`<br>`googleapis.com`|
||Essential Contacts<br>(/resource-manager/docs/managing-notification-<br>contacts)|`essentialcontacts.`<br>`googleapis.com`|
||Eventarc(/eventarc/docs/overview)|`eventarc.`<br>`googleapis.com`|
||Filestore(/filestore/docs/overview)|`file.googleapis.`<br>`com`|
||Firebase Security Rules<br>(https://firebase.google.com/docs/rules)|`firebaserules.`<br>`googleapis.com`|
||Firestore(/firestore/native/docs/overview)|`firestore.`<br>`googleapis.com`|
||Flow Analyzer<br>(/network-intelligence-center/docs/flow-<br>analyzer/overview)|`networkmanagement.`<br>`googleapis.com`|
||Google Kubernetes Engine (GKE) Hub<br>(/kubernetes-engine/docs/fleets-overview)|`gkehub.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE) Identity Service<br>(/kubernetes-engine/distributed-<br>cloud/vmware/docs/concepts/authentication)|`anthosidentityserv`<br>`ice.googleapis.com`|
||Google Kubernetes Engine (GKE) Image streaming<br>(/kubernetes-engine/docs/how-to/image-streaming|)<br>`containerfilesyste`<br>`m.googleapis.com`|
||Gemini Enterprise(/gemini/enterprise/docs)<br>[8] (#8|)`discoveryengine.`<br>`googleapis.com`|
||Gemini Enterprise Agent Platform Workbench<br>(/gemini-enterprise-agent-<br>platform/notebooks/workbench/introduction)|`aiplatform.`<br>`googleapis.com`|
||Generative AI on Vertex AI<br>(/vertex-ai/generative-ai/docs/learn/overview)|`aiplatform.`<br>`googleapis.com`|
||Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>[4] (#4)|`compute.`<br>`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Google Cloud Managed Service for Apache Kafka<br>(/managed-service-for-apache-<br>kafka/docs/overview)|`managedkafka.`<br>`googleapis.com`|
||Google Cloud NetApp Volumes<br>(/netapp/volumes/docs)|`netapp.googleapis.`<br>`com`|
||Google Kubernetes Engine (GKE)<br>(/kubernetes-engine/docs/concepts/kubernetes-<br>engine-overview)|`container.`<br>`googleapis.com`<br>`containersecurity.`<br>`googleapis.com`|
||Google Security Operations SIEM<br>(/security/products/security-information-event-<br>management)|`chronicle.`<br>`googleapis.com`<br>`chronicleservicema`<br>`nager.googleapis.`<br>`com`|
||Google Security Operations SOAR<br>(/chronicle/docs/soar)|`Not applicable`|
||Identity and Access Management (IAM)<br>(/iam/docs/overview)|`iam.googleapis.com`|
||Identity-Aware Proxy (IAP)<br>(/iap/docs/concepts-overview)|`iap.googleapis.com`|
||Infrastructure Manager<br>(/infrastructure-manager/docs)|`config.googleapis.`<br>`com`|
||Integration Connectors<br>(/integration-connectors/docs/overview)|`connectors.`<br>`googleapis.com`|
||Knowledge Catalog(/dataplex/docs/introduction)|`dataplex.`<br>`googleapis.com`<br>`datalineage.`<br>`googleapis.com`|
||Looker (Google Cloud core)<br>(/looker/docs/looker-core-overview)|`looker.googleapis.`<br>`com`|
||Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview)|`composer.`<br>`googleapis.com`|
||Managed Service for Apache Spark<br>(/dataproc/docs/concepts/overview)|`dataproc-control.`<br>`googleapis.com`<br>`dataproc.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Memorystore for Redis(/memorystore/docs/redis)|`redis.googleapis.`<br>`com`|
||Migrate to Containers<br>(/migrate/containers/docs/getting-started)|`Not applicable`|
||Model Armor<br>(/security-command-center/docs/model-armor-<br>overview)|`modelarmor.`<br>`googleapis.com`|
||Network Connectivity Center<br>(/network-connectivity/docs/network-connectivity-<br>center/concepts/overview)|`networkconnectivit`<br>`y.googleapis.com`|
||Organization Policy Service<br>(/resource-manager/docs/organization-policy/using<br>constraints)|-<br>`orgpolicy.`<br>`googleapis.com`|
||Persistent Disk|`compute.`|
||(/compute/docs/disks/persistent-disks)|`googleapis.com`|
||Personalized Service Health<br>(/service-health/docs/overview)|`servicehealth.`<br>`googleapis.com`|
||Pub/Sub(/pubsub/docs/overview)|`pubsub.googleapis.`<br>`com`|
||Resource Manager|`cloudresourcemanag`|
||(/resource-manager/docs/resource-manager-<br>overview)|`er.googleapis.com`|
||Secret Manager(/secret-manager/docs/overview)|`secretmanager.`<br>`googleapis.com`|
||Secure Source Manager|`securesourcemanage`|
||(/secure-source-manager/docs/overview)|`r.googleapis.com`|
||Secure Web Proxy|`networkservices.`|
||(/secure-web-proxy/docs/overview)|`googleapis.com`<br>`networksecurity.`<br>`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Security Command Center|`securitycenter.`|
||(/security-command-center/docs/security-<br>command-center-overview)|`googleapis.com`<br>`securitycentermana`<br>`gement.googleapis.`<br>`com`<br>`securityposture.`<br>`googleapis.com`<br>`websecurityscanner`<br>`.googleapis.com`|
||Sensitive Data Protection<br>(/sensitive-data-protection/docs/sensitive-data-<br>protection-overview)|`dlp.googleapis.com`|
||Serverless VPC Access<br>(/vpc/docs/configure-serverless-vpc-access)|`vpcaccess.`<br>`googleapis.com`|
||Spanner(/spanner/docs/editions-overview)|`spanner.`<br>`googleapis.com`|
||Speech-to-Text(/speech-to-text/docs/overview)|`speech.googleapis.`<br>`com`|
||Storage Transfer Service<br>(/storage-transfer/docs/overview)|`storagetransfer.`<br>`googleapis.com`|
||Text-to-Speech(/text-to-speech/docs/basics)|`texttospeech.`<br>`googleapis.com`|
||Cloud Service Mesh(/service-mesh/docs/overview)|`trafficdirector.`<br>`googleapis.com`|
||VM Manager<br>(/compute/vm-manager/docs/overview)|`osconfig.`<br>`googleapis.com`|
||VPC Service Controls|`accesscontextmanag`|
||(/vpc-service-controls/docs/overview)|`er.googleapis.com`<br>`accesscontextintel`<br>`ligence.`<br>`googleapis.com`|
||Vertex AI Batch prediction|`aiplatform.`|
||(/vertex-ai/docs/predictions/get-batch-predictions)|`googleapis.com`|
||Vertex AI Model Monitoring|`aiplatform.`|
||(/vertex-ai/docs/model-monitoring)|`googleapis.com`|

|Control package|Supported products|API services<br>1 (#1)|
|---|---|---|
||Vertex AI Model Registry<br>(/vertex-ai/docs/model-registry)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Online prediction<br>(/vertex-ai/docs/predictions/get-online-predictions)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Pipelines(/vertex-ai/docs/pipelines)|`aiplatform.`<br>`googleapis.com`|
||Agent Search<br>(/gemini-enterprise-agent-platform/models/vertex-<br>ai-search)|`discoveryengine.`<br>`googleapis.com`|
||Vertex AI Training<br>(/vertex-ai/docs/training-overview)|`aiplatform.`<br>`googleapis.com`|
||Vertex AI Tuning<br>(/vertex-ai/generative-ai/docs/models/tune-models|)<br>`aiplatform.`<br>`googleapis.com`|
||Virtual Private Cloud (VPC)(/vpc/docs/overview)|`compute.`<br>`googleapis.com`|
||Web Risk(/web-risk/docs/overview)|`webrisk.`<br>`googleapis.com`|
||Workflows(/workflows/docs/overview)|`workflows.`<br>`googleapis.com`|
||Workload Identity Federation|`iam.googleapis.com`|
||(/iam/docs/workforce-identity-federation)|`sts.googleapis.com`|
