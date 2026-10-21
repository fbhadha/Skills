# Canada Protected B, Assured Workloads and access controls / Supported products by control package: Footnotes to Overview of VPC Service Controls
Source: 05-Canada-Protected-B-Assured-Workloads-and-access-controls.pdf, pages 350-389, extracted 2026-10-18

Contains:
- Supported products by control package: Footnotes (pages 350-352) https://docs.cloud.google.com/assured-workloads/docs/supported-products
- Introduction to Access Approval (pages 353-353) https://docs.cloud.google.com/assured-workloads/docs/access-approval
- Introduction to Access Transparency (pages 354-354) https://docs.cloud.google.com/assured-workloads/docs/access-transparency
- Overview of Key Access Justifications (pages 355-360) https://docs.cloud.google.com/assured-workloads/key-access-justifications
- Cloud External Key Manager (pages 361-376) https://docs.cloud.google.com/kms/docs/ekm
- Overview of VPC Service Controls (pages 377-389) https://docs.cloud.google.com/vpc-service-controls/docs/overview

## Supported products by control package

URL: https://docs.cloud.google.com/assured-workloads/docs/supported-products

### Footnotes

1. Depending on the data boundary that you choose, different API endpoint types (/docs/security/compliance/endpoints) may be available. The API endpoints listed on this 

page are global API endpoints, but regional or locational API endpoints may be available or required for a given data boundary. 

2. BigQuery is supported, but it isn't automatically enabled when you create a new Assured Workloads folder due to an internal configuration process. This process normally finishes in ten minutes, but can take much longer in some circumstances. To check whether the process is finished and to enable BigQuery, complete the following steps: 

1. In the Google Cloud console, go to the **Assured Workloads** page. 

Go to Assured Workloads (https://console.cloud.google.com/compliance/assuredworkloads) 

2. Select your new Assured Workloads folder from the list. 

3. On the **Folder Details** page in the **Allowed services** section, click **Review Available Updates** . 

4. In the **Allowed services** pane, review the services to be added to the Resource Usage Restriction 

(/resource-manager/docs/organization-policy/restricting-resources) organization policy for the folder. If BigQuery services are listed, click **Allow Services** to add them. 

If BigQuery services are not listed, wait for the internal process to complete. If the services are not listed within 12 hours of folder creation, contact Cloud Customer Care (/support). 

After the enablement process is completed, you can use BigQuery in your Assured Workloads folder. 

Gemini in BigQuery is not supported by Assured Workloads. 

3. Spanner Vertex AI integration (/spanner/docs/ml) is not supported. 

4. See Google Cloud Armor compliance (/armor/docs/compliance) for supported configurations. 

5. Unless otherwise noted, the following Cloud Run features aren't supported: 

   - Cloud Trace integration (/run/docs/trace) 

   - Cloud Run functions (/functions/docs/concepts/overview) 

   - Eventarc triggers (/functions/docs/calling/eventarc) 

6. Cloud Monitoring's Synthetic monitoring (/monitoring/uptime-checks/introduction) and Uptime checks (/monitoring/uptime-checks) features are not supported in Assured Workloads. 

7. It is your responsibility not to use the following Cloud Build features because they are not compliant with Data Boundary for IL5: 

Generate and validate build provenance 

(/build/docs/securing-builds/generate-validate-build-provenance) 

Build repositories from GitHub Enterprise in a private network 

(/build/docs/automating-builds/github/build-repos-from-github-enterprise-privatenetwork?generation=2nd-gen) 

8. Gemini Enterprise includes support for the Web Grounding for Enterprise feature. For FedRAMP High and Department of Defense (DoD) Impact Level 4 (IL4) users, see the Deployment guidance for Gemini for Government 

(/docs/security/compliance/deploy-gemini-gov) page. 

9. The following Knowledge Catalog features are not supported: 

Lakes, zones, and tasks (/dataplex/docs/metadata) 

10. Cloud Shell doesn't meet NIST SP 800-53 Control SA-9(5) data residency requirements for FedRAMP High workloads. If you choose to use Cloud Shell for FedRAMP High workloads, you are also choosing to accept the associated risks under the Assured Workloads shared responsibility model 

(/assured-workloads/docs/shared-responsibility). 

11. Cloud Billing Support cases are not in scope for FedRAMP Moderate or Assured Workloads; only tech support cases for Cloud Billing or the Cloud Billing API are in scope. 

Last updated 2026-10-13 UTC. 



## Introduction to Access Approval

URL: https://docs.cloud.google.com/assured-workloads/docs/access-approval

Google Cloud aims to ensure that limits on administrative access are an integral part of how the products are designed to work. Access Approval lets you decide if and when Google personnel can access your customer content stored on Google Cloud. When Google personnel require access to customer data to fulfill a contractual obligation, they must submit a detailed approval request with a valid business justification. 

For more information, see Overview of Access Approval 

(/assured-workloads/access-approval/docs/overview). 

For the list of services that Access Approval supports, see Supported services (/assured-workloads/access-approval/docs/supported-services). 

For information about what an access request looks like, see Anatomy of an access request (/assured-workloads/access-approval/docs/approval-request-details). 

### Get started with using Access Approval

To get started using the Google-managed signing key, see Review and approve access requests using the Google-managed signing key 

(/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys). 

To get started using a custom signing key, see Review and approve access requests using a custom signing key 

(/assured-workloads/access-approval/docs/review-approve-access-requests-google-keys). 

Last updated 2026-10-13 UTC. 



## Introduction to Access Transparency

URL: https://docs.cloud.google.com/assured-workloads/docs/access-transparency

As a part of Google's long-term commitment to security and transparency, Access Transparency lets you review logs of actions that Google personnel take when accessing certain Customer Data to fulfill their contractual obligations. 

Access Transparency logs include information about Google personnel activity, including the following: 

- Actions taken by the Cloud Customer Care team to resolve a support ticket that you filed. 

- Investigation of an outage. 

For more information, see Overview of Access Transparency 

(/assured-workloads/access-transparency/docs/overview). 

For the list of services that Access Transparency supports, see Supported services (/assured-workloads/access-transparency/docs/supported-services). 

For information about Google Cloud's approach to privileged access management, see Privileged access at Google Cloud 

(/assured-workloads/access-transparency/docs/privileged-access). 

### Get started with using Access Transparency

Learn how to enable Access Transparency 

(/assured-workloads/access-transparency/docs/enable). Then, understand and use Access Transparency logs (/assured-workloads/access-transparency/docs/reading-logs). 

Last updated 2026-10-13 UTC. 



## Overview of Key Access Justifications

URL: https://docs.cloud.google.com/assured-workloads/key-access-justifications

This page provides an overview of Key Access Justifications. Key Access Justifications is a part of Google's long-term commitment to transparency, user trust, and customer ownership of their data. Key Access Justifications directs Google systems to generate access justifcation codesi 

(/assured-workloads/key-access-justifications/docs/justification-codes) for each cryptographic operation involving enrolled Cloud Key Management Service (Cloud KMS) keys. 

Key Access Justifications works alongside Access Approval 

(/assured-workloads/access-approval/docs/overview) and Access Transparency (/assured-workloads/access-transparency/docs/overview) in the following way: Access Approval lets you authorize requests from Google personnel to access Customer Data (https://cloud.google.com/terms/data-processing-addendum), Access Transparency helps you discover information about when Customer Data is accessed, and Key Access Justifications provides key access control for all interactions with at-rest Customer Data that is encrypted by a customer-managed key. Together, each of these products provide access management capabilities that give you control over and context for administrative requests to access Customer Data. 

### Overview

Key Access Justifications lets you set a policy on Cloud Key Management Service (Cloud KMS) keys to view, approve, and deny key access requests depending on the provided justification code 

(/assured-workloads/key-access-justifications/docs/justification-codes). For select external key management partners, you can configure Key Access Justifications policies outside of Google Cloud to be exclusively enforced by the external key manager rather than by Cloud KMS. 

Depending on the Assured Workloads control package 

(/assured-workloads/docs/control-packages) you choose, the following Key Access Justifications features are available: 

- For select regional control packages (/assured-workloads/docs/control-packages#regional-controls), _Key Access Transparency_ logs these justification codes in your Cloud KMS audit logs (/kms/docs/audit-logging). 

- For select regional, regulatory 

- (/assured-workloads/docs/control-packages#regulatory-controls), or sovereign (/assured-workloads/docs/control-packages#sovereign-controls) control packages, Key Access Justifications lets you set a policy on your keys to approve or deny key access requests depending on the provided justification code. Some regional data boundaries provide this feature in addition to Key Access Transparency. 

- For select sovereign control packages, you can use a supported external key management partners to configure Key Access Justifications policies outside of Google Cloud. These policies are exclusively enforced by the external key manager rather than by Cloud KMS. 

In addition to these features, the Assured Workloads control package you choose will also determine which of the following Cloud KMS key types are available: 

- Cloud EKM keys (/kms/docs/ekm#overview) 

- Cloud HSM keys (/assured-workloads/key-access-justifications/docs/configure-kaj) 

- Cloud KMS software keys 

- (/assured-workloads/key-access-justifications/docs/configure-kaj) 

### How encryption at rest works

Google Cloud encryption at rest works by encrypting your data stored on Google Cloud with an encryption key that lives outside the service where the data is stored. For example, if you encrypt data in Cloud Storage, the service only stores the encrypted information you have stored, whereas the key used to encrypt that data is stored in Cloud KMS (if you are using customer-managed encryption keys (CMEK)) or in your external key manager (if you are using Cloud EKM). 

When you use a Google Cloud service, you want your applications to continue working as described, and this will require your data to be decrypted. For example, 

if you run a query using BigQuery, the BigQuery service needs to decrypt your data to be able to analyze it. BigQuery accomplishes this by making a decryption request to the key manager to get the required data. 

### Why would my keys be accessed?

Your encryption keys are most often accessed by automated systems while servicing your own requests and workloads on Google Cloud. 

In addition to customer-initiated accesses and automated system accesses, a Google employee might need to initiate operations which use your encryption keys for the following reasons: 

- **Back up your data** : Google might need to access your encryption keys to back up your data for disaster recovery reasons. 

- **Resolve a support request** : A Google employee might need to decrypt your data to fulfill the contractual obligation of providing support. 

- **Manage and troubleshoot systems** : Google personnel can initiate operations which use your encryption keys to perform technical debugging needed for a complex support request or investigation. Access might also be needed to remediate storage failure or data corruption. 

- **Ensure data integrity and compliance, and protect against fraud and abuse** : Google might need to decrypt data for the following reasons: 

   - To ensure the safety and security of your data and accounts. 

   - To make sure that you are using Google services in compliance with the Google Cloud Terms of Service (https://cloud.google.com/terms). 

   - To investigate complaints by other users and customers, or other signals of abusive activity. 

   - To verify that Google Cloud services are being used in accordance with applicable regulatory requirements, such as anti-money laundering regulations. 

- **Maintain system reliability** : Google personnel can request access to investigate that a suspected service outage doesn't affect you. Also, access 

might be requested to ensure backup and recovery from outages or system failures. 

For the list of justification codes, see justifcation reason codes for Key Accessi Justifications (/assured-workloads/key-access-justifications/docs/justification-codes). 

### Managing access to your keys

Key Access Justifications provides a reason every time your Cloud KMS-managed keys or externally managed keys are accessed. When your key is used for any cryptographic operation, you receive a justification for both service-based access (for supported services) and direct API access. 

After your key projects are enrolled in Key Access Justifications, you immediately begin receiving justifications for every key access for new keys. For previously existing keys, you will begin receiving justifications for every key access within 24 hours. 

### Enabling Key Access Justifications

Key Access Justifications can only be used with Assured Workloads, and is enabled by default when you create a new Assured Workloads folder configured for a control package that includes Key Access Justifications. See the Assured Workloads overview (/assured-workloads/docs/overview) for more information. 

**Note:** It can take up to 24 hours to enable Key Access Justifications with external key managers after you've created your Assured Workloads folder. Therefore, we recommend that you don't reject key access requests in production environments during this time. There is no delay when using non-external Cloud KMS keys. 

### Key Access Justifications exclusions

Key Access Justifications only applies to the following situations: 

- **Operations on encrypted data** : For the fields within a given service that are encrypted by a customer-managed key, refer to the service's documentation. 

- **The transition from data-at-rest to data-in-use** : While Google continues to apply protections to your data-in-use, Key Access Justifications only governs the transition from data-at-rest to data-in-use. 

The following Compute Engine and Persistent Disk features are exempted when used with CMEK: 

- Local SSDs (/compute/docs/disks#localssds) 

- Automatic restart (/compute/docs/instances/setting-vm-host-options) 

- Machine image operations (/compute/docs/machine-images/create-machine-images) 

### Key Access Justifications with Access Approval

For workloads with Access Approval enabled with a custom signing key, Key Access Justifications will also apply to processing signed access approval requests. Access Approval requests can only be processed if the associated justification for the key access associated is also permitted by the key's Key Access Justifications policy. When a customer signs an Access Approval request, the associated justification is reflected in the signing request for the approval. 

All Customer Data accesses that occur from an approved, signed access approval request will appear in Access Transparency logs linked to the approval request. 

### What's next

- See which services (/assured-workloads/docs/supported-products) are supported by Assured Workloads for Sovereign Controls for EU 

- (/assured-workloads/docs/control-packages#eu-sovereignty-controls) and the list of additional KAJ-supported services 

- (/assured-workloads/key-access-justifications/docs/supported-services). 

- Read how to view and act on justifications 

- (/assured-workloads/key-access-justifications/docs/view-justifications). 

- Read where you can get support for Key Access Justifications 

- (/assured-workloads/key-access-justifications/docs/getting-support). 

- Learn what an Access Approval request looks like 

- (/assured-workloads/access-approval/docs/approval-request-details). 

- Learn about the core principles upon which controls that prevent unauthorized administrative access are based 

- (/assured-workloads/cloud-provider-access-management/docs/administrative-access). 

Last updated 2026-10-13 UTC. 



## Cloud External Key Manager

URL: https://docs.cloud.google.com/kms/docs/ekm

This page provides an overview of Cloud External Key Manager (Cloud EKM). 

### Terminology

**External key manager (EKM)** 

The key manager used outside of Google Cloud to manage your keys. 

**Cloud External Key Manager (Cloud EKM)** 

A Google Cloud service for using your external keys that are managed within a supported EKM. 

**Cloud EKM through the internet** 

A version of Cloud EKM where Google Cloud communicates with your external key manager over the internet. 

**Cloud EKM through a VPC** 

A version of Cloud EKM where Google Cloud communicates with your external key manager over a Virtual Private Cloud (VPC). For more information, see VPC network overview (/vpc/docs/vpc). 

**EKM key management from Cloud KMS** 

When using Cloud EKM through a VPC with an external key management partner that supports the Cloud EKM control plane, you can use the **Cloud KMS** EKM management mode to simplify the process of maintaining external keys in your external key management partner and in Cloud EKM. For more information, see Coordinated external keys (#how-coordinated) and EKM key management from Cloud KMS (#ekm-management-mode) on this page. 

**Crypto space** 

A container for your resources within your external key management partner. Your crypto space is identified by a unique crypto space path. The format of the crypto space path varies by external key management partner—for example, `v0/cryptospaces/` _`YOUR_UNIQUE_PATH`_ . 

**Partner-managed EKM** 

An arrangement where your EKM is managed for you by a trusted partner. For more information, see Partner-managed EKM (#partner-managed) on this page. 

**Key Access Justifications** 

When you use Cloud EKM with Key Access Justifications, each request to your external key management partner includes a field that identifies the reason for each request. You can configure your external key management partner to allow or deny requests based on the Key Access Justifications code provided. For more information about Key Access Justifications, see Key Access Justifications overview (/assured-workloads/key-access-justifications/docs/overview). 

### Overview

With Cloud EKM, you can use keys that you manage within a supported external key management partner (#supported_partners) to protect data within Google Cloud. You can protect data at rest in supported CMEK integration services 

(#supported_services), or by calling the Cloud Key Management Service API directly. 

Cloud EKM provides several benefits: 

- **Key provenance:** You control the location and distribution of your externally managed keys. Externally managed keys are never cached or stored within Google Cloud. Instead, Cloud EKM communicates directly with the external key management partner for each request. 

- **Access control:** You manage access to your externally managed keys in your external key manager. You can't use an externally managed key in Google Cloud without first granting the Google Cloud project access to the key in your external key manager. You can revoke this access at any time. 

- **Centralized key management:** You can manage your keys and access policies from a single user interface, whether the data they protect resides in the cloud or on your premises. 

**Migrate between Cloud EKM protection levels with zero downtime** 

- **(Preview** (https://cloud.google.com/products#product-launch-stages) **):** If you have Cloud EKM keys that you're already using, you can migrate existing key 

versions between the `EXTERNAL` and `EXTERNAL_VPC` protection levels. This lets you switch between Cloud EKM over the internet and Cloud EKM over a VPC for the same key material, without needing to re-encrypt your data. For more information, see Migrate external keys (/kms/docs/migrate-external-keys). 

In all cases, the key resides on the external system, and is never sent to Google. 

You can communicate with your external key manager over the internet (/kms/docs/set-up-ekm-internet) or over a Virtual Private Cloud (VPC) (/kms/docs/create-ekm-connection). 

### How Cloud EKM works

Cloud EKM key versions consist of these parts: 

- **External key material** : The external key material of a Cloud EKM key is cryptographic material created and stored in your EKM. This material does not leave your EKM and it is never shared with Google. 

- **Key reference** : Each Cloud EKM key version contains either a key URI or a key path. This is a unique identifier for the external key material that Cloud EKM uses when requesting cryptographic operations using the key. 

- **Internal key material** : When a symmetric Cloud EKM key is created, Cloud KMS creates additional key material in Cloud KMS, which never leaves Cloud KMS. This key material is used as an extra layer of encryption when communicating with your EKM. This internal key material does not apply to asymmetric signing keys. 

To use your Cloud EKM keys, Cloud EKM sends requests for cryptographic operations to your EKM. For example, to encrypt data with a symmetric encryption key, Cloud EKM first encrypts the data using the internal key material. The encrypted data is included in a request to the EKM. The EKM wraps the encrypted data in another layer of encryption using the external key material, and then returns the resulting ciphertext. Data encrypted using a Cloud EKM key can't be decrypted without both the external key material and the internal key material. 

If your organization has enabled Key Access Justifications, your external key management partner records the provided access justification and completes the 

request only for justification reason codes 

(/assured-workloads/key-access-justifications/docs/overview#reasons) that are allowed by your Key Access Justifications policy on the external key management partner. 

Creating and managing Cloud EKM keys requires corresponding changes in both Cloud KMS and the EKM. These corresponding changes are handled differently for _manually managed external keys_ and for _coordinated external keys_ . All external keys accessed over the internet are manually managed. External keys accessed over a VPC network can be manually managed or coordinated, depending on the EKM management mode of the EKM connection. The **Manual** EKM management mode is used for manually managed keys. The **Cloud KMS** EKM management mode is used for coordinated external keys. For more information about EKM management modes, see Manually managed external keys (#how-manually-managed) and Coordinated external keys (#how-coordinated) on this page. 

The following diagram shows how Cloud KMS fits into the key management model. This diagram uses Compute Engine and BigQuery as two examples; you can also see the full list of services that support Cloud EKM keys (#supported_services). 

**Caution:** Both the Cloud EKM key version and the external key are required for each encryption and decryption request. If you lose access to either key, your data cannot be recovered. It is not possible to re-create an identical Cloud EKM key version by using the same external key URI or key path. 

You can learn about the considerations (#considerations) and restrictions (#restrictions) when using Cloud EKM. 

#### Manually managed external keys

This section provides a broad overview of how Cloud EKM works with a manually managed external key. 

1. You create or use an existing key in a supported external key management partner system (#supported_partners). This key has a unique URI or key path. 

2. You grant your Google Cloud project access to use the key, in the external key management partner system. 

3. In your Google Cloud project, you create a Cloud EKM key version, using the URI or key path for the externally managed key. 

4. Maintenance operations like key rotation must be manually managed between your EKM and Cloud EKM. For example, key version rotation or key version destruction operations need to be completed both directly in your EKM and in Cloud KMS. 

Within Google Cloud, the key appears alongside your other Cloud KMS and Cloud HSM keys, with protection level `EXTERNAL` or `EXTERNAL_VPC` . The Cloud EKM key and the external key management partner key work together to protect your data. The external key material is never exposed to Google. 

#### Coordinated external keys

This section provides an overview of how Cloud EKM works with coordinated external keys. 

1. You set up an EKM connection (/kms/docs/create-ekm-connection), setting the **EKM management mode** to **Cloud KMS** . During setup, you must authorize your EKM to access your VPC network and authorize your Google Cloud project service account to access your _crypto space_ in your EKM. Your EKM connection uses the hostname of your EKM and a _crypto space path_ that identifies your resources within your EKM. 

2. You create an external key (/kms/docs/create-key) in Cloud KMS. When you create a Cloud EKM key using an EKM over VPC connection with the **Cloud KMS** EKM management mode enabled, the following steps take place automatically: 

   - a. Cloud EKM sends a key creation request to your EKM. 

   - b. Your EKM creates the requested key material. This external key material remains in the EKM and is never sent to Google. 

   - c. Your EKM returns a key path to Cloud EKM. 

   - d. Cloud EKM creates your Cloud EKM key version using the key path provided by your EKM. 

3. Maintenance operations on coordinated external keys can be initiated from Cloud KMS. For example, coordinated external keys used for symmetric encryption can be automatically rotated on a set schedule. The creation of new key versions is coordinated in your EKM by Cloud EKM. You can also trigger the creation or destruction of key versions in your EKM from Cloud KMS using the Google Cloud console, the gcloud CLI, the Cloud KMS API, or Cloud KMS client libraries. 

Within Google Cloud, the key appears alongside your other Cloud KMS and Cloud HSM keys, with protection level `EXTERNAL_VPC` . The Cloud EKM key and the external key management partner key work together to protect your data. The external key material is never exposed to Google. 

EKM key management from Cloud KMS 

Coordinated external keys are made possible by EKM connections that use EKM key management from Cloud KMS. If your EKM supports the Cloud EKM control plane, then you can enable EKM key management from Cloud KMS for your EKM connections to create coordinated external keys. With EKM key management from Cloud KMS enabled, Cloud EKM can request the following changes in your EKM: 

- Create a key: When you create an externally managed key in Cloud KMS using a compatible EKM connection, Cloud EKM sends your key creation request to your EKM. When successful, your EKM creates the new key and key material and returns the key path for Cloud EKM to use to access the key. 

- Rotate a key: When you rotate an externally-managed key in Cloud KMS using a compatible EKM connection, Cloud EKM sends your rotation request to your EKM. When successful, your EKM creates new key material and returns the key path for Cloud EKM to use to access the new key version. 

- Destroy a key: When you destroy a key version for an externally-managed key in Cloud KMS using a compatible EKM connection, Cloud KMS schedules the 

key version for destruction in Cloud KMS. If the key version is not restored before the _scheduled for destruction_ period ends, Cloud EKM destroys its part of the key's cryptographic material and sends a destruction request to your EKM. 

Data encrypted with this key version cannot be decrypted after the key version is destroyed in Cloud KMS, even if the EKM has not yet destroyed the key version. You can see whether the EKM has successfully destroyed the key version by viewing the key's details in Cloud KMS. 

When keys in your EKM are managed from Cloud KMS, the key material still resides in your EKM. Google can't make any key management requests to your EKM without explicit permission. Google can't change permissions or Key Access Justifications policies in your external key management partner system. If you revoke Google's permissions in your EKM, key management operations attempted in Cloud KMS fail. 

### Compatibility

#### Supported key managers

You can store external keys in the following external key management partner systems: 

Supported today: 

- Fortanix (https://fortanix.com/solutions/use-case/ekm-for-gcp/) 

- Futurex (https://www.futurex.com/solutions/google-cloud-ekm-integration) 

Thales 

- (https://thalesdocs.com/dpod/services/key_management_services/cdsp/index.html ) 

#### Services that support CMEK with Cloud EKM

The following services support integration with Cloud KMS for external (Cloud EKM) keys: 

- Agent Assist (/agent-assist/docs/cmek) 

- Agent Retrieval (/gemini-enterprise-agent-platform/build/vector-search-2/cmek) 

- AlloyDB for PostgreSQL (/alloydb/docs/cmek) 

- Apigee API hub (/apigee/docs/apihub/provision#step-encryption) 

- Application Integration (/application-integration/docs/cmek) 

- Artifact Registry (/artifact-registry/docs/cmek) 

- Backup and DR Service: Backup Vault Container 

- (/backup-disaster-recovery/docs/concepts/cmek#backup-vault-container) and Backups at rest (/backup-disaster-recovery/docs/concepts/cmek#backups-at-rest) 

- Backup for GKE (/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-cmek) 

- BigQuery (/bigquery/docs/customer-managed-encryption) 

- Bigtable (/bigtable/docs/cmek) 

- Cloud Data Fusion (/data-fusion/docs/how-to/customer-managed-encryption-keys) 

- Cloud Healthcare API (/healthcare-api/docs/cmek) 

- Cloud Logging: Data in the Log Router (/logging/docs/routing/managed-encryption) and Data in Logging storage (/logging/docs/routing/managed-encryption-storage) 

- Cloud Run (/run/docs/securing/using-cmek) 

- Cloud Run functions (/functions/docs/securing/cmek) 

- Cloud SQL: Data written to databases (/sql/docs/mysql/configure-cmek) and Standard and enhanced backups (/sql/docs/mysql/backup-recovery/backups) 

- Cloud Storage (/storage/docs/encryption/using-customer-managed-keys) 

- Cloud Tasks (/tasks/docs/use-cmek) 

- Cloud Workstations (/workstations/docs/encrypt-workstation-resources) 

- Compute Engine: Persistent disks 

- (/compute/docs/disks/customer-managed- 

- encryption#encrypt_a_new_persistent_disk_with_cmek) 

- , Snapshots (/compute/docs/disks/customer-managed-encryption#create_snapshot), Custom images 

(/compute/docs/disks/customer-managed-encryption#encrypt_an_imported_image), and Machine images 

(/compute/docs/machine-images/create-machine-images#create-image-from-instance) 

- Customer Experience Insights (/contact-center/insights/docs/cmek) 

- Data Studio (/data-studio/cmek) 

- Database Migration Service: MySQL migrations - data written to databases (/sql/docs/mysql/configure-cmek), PostgreSQL migrations - Data written to databases (/sql/docs/postgres/configure-cmek), PostgreSQL to AlloyDB migrations - Data written to databases (/alloydb/docs/use-cmek), SQL Server migrations - Data written to databases (/sql/docs/sqlserver/configure-cmek), and Oracle to PostgreSQL data at rest 

- (/database-migration/docs/oracle-to-postgresql/cmek-for-migration-jobs) 

- Dataflow (/dataflow/docs/guides/customer-managed-encryption-keys) 

- Dataform (/dataform/docs/cmek) 

- Dataproc Metastore (/dataproc-metastore/docs/cmek) 

- Datastream (/datastream/docs/use-cmek) 

- Dialogflow CX (/dialogflow/cx/docs/concept/cmek) 

- Document AI (/document-ai/docs/cmek) 

- Eventarc Advanced (/eventarc/advanced/docs/use-cmek) (Preview (https://cloud.google.com/products/#product-launch-stages)) 

- Eventarc Standard (/eventarc/docs/use-cmek) 

- Filestore (/filestore/docs/cmek) 

- Firestore (/firestore/docs/use-cmek) 

- Google Cloud Managed Lustre (/managed-lustre/docs/cmek) 

- Google Cloud Managed Service for Apache Kafka 

- (/managed-service-for-apache-kafka/docs/encryption) 

- Google Cloud NetApp Volumes 

- (/netapp/volumes/docs/configure-and-use/cmek/create-cmek-policy) 

- Google Cloud Observability 

- (/stackdriver/docs/observability/set-defaults-for-observability-buckets) (Preview (https://cloud.google.com/products/#product-launch-stages)) 

- Google Distributed Cloud (/distributed-cloud/edge/latest/docs/security#storage) 

- Google Kubernetes Engine: Data on VM disks 

- (/kubernetes-engine/docs/how-to/using-cmek) and Application-layer secrets 

- (/kubernetes-engine/docs/how-to/encrypting-secrets) 

- Integration Connectors (/integration-connectors/docs/encryption) 

- Knowledge Catalog (/dataplex/docs/cmek) 

- Looker (Google Cloud core) (/looker/docs/looker-core-cmek) 

- Managed Service for Apache Airflow (/composer/docs/cmek) 

- Managed Service for Apache Spark: Cluster data on VM disks (/dataproc/docs/concepts/configuring-clusters/customer-managed-encryption) and Serverless data on VM disks (/dataproc-serverless/docs/guides/cmek-serverless) 

- Memorystore for Redis (/memorystore/docs/redis/cmek) 

- Memorystore for Redis Cluster (/memorystore/docs/cluster/use-cmek) 

- Memorystore for Valkey (/memorystore/docs/valkey/use-cmek) 

- Migrate to Virtual Machines: Data migrated from VMware, AWS, and Azure VM sources (/migrate/virtual-machines/docs/5.0/migrate/cmek#migration-data) and Data migrated from disk and machine image sources 

- (/migrate/virtual-machines/docs/5.0/migrate/cmek#target-disk-machine-images) 

- Parameter Manager (/secret-manager/parameter-manager/docs/cmek) 

- Pub/Sub (/pubsub/docs/cmek) 

- Secret Manager (/secret-manager/docs/cmek) 

- Secure Source Manager (/secure-source-manager/docs/cmek) 

- Security Command Center (/security-command-center/docs/cmek) 

- Spanner (/spanner/docs/cmek) 

- Speech-to-Text (/speech-to-text/v2/docs/encryption) 

- Vertex AI (/vertex-ai/docs/general/cmek) 

- Vertex AI Workbench instances (/vertex-ai/docs/workbench/instances/cmek) 

- Workflows (/workflows/docs/use-cmek) 

- Workload Manager (/workload-manager/docs/evaluate/custom-rules/enable-cmek) 

**Important:** All other services are not compatible with Cloud External Key Manager for CMEK. 

**Note:** If your Cloud EKM key is not listed in the Google Cloud console when setting up CMEK services, first copy the resource name 

(/kms/docs/getting-resource-ids#getting_the_id_for_a_key_and_version). Then select **Don't see your key? Enter key resource name.** and enter the key resource name captured earlier. 

### Considerations

- When you use a Cloud EKM key, Google has no control over the availability of your externally managed key in the external key management partner system. If you lose keys that you manage outside of Google Cloud, Google can't recover your data. 

- Review the guidelines about external key management partners and regions (#regions) when choosing the locations for your Cloud EKM keys. 

- Review the Cloud EKM Service Level Agreement (SLA) (https://cloud.google.com/ekm/sla). 

- Communicating with an external service over the internet can lead to problems with reliability, availability, and latency. For applications with low tolerance for these types of risks, consider using Cloud HSM or Cloud KMS to store your key material. 

   - If an external key is unavailable, Cloud KMS returns a `FAILED_PRECONDITION` error and provides details in the `PreconditionFailure` (/kms/docs/reference/ekm_errors#input_errors) error detail. 

Enable data audit logging (/kms/docs/audit-logging#enabling_audit_logging) to maintain a record of all errors related to Cloud EKM. Error messages contain detailed information to help pinpoint the source of the error. An example of a common error is when an external key management partner does not respond to a request within a reasonable timeframe. 

   - You need a support contract with the external key management partner. Google Cloud support can only help with issues in Google Cloud services and cannot directly assist with issues on external systems. Sometimes, you must work with support on both sides to troubleshoot interoperability issues. 

- Cloud EKM can be used with Bare Metal Rack HSM (/kms/docs/bare-metal-rack-hsm) to create a standalone HSM solution integrated with Cloud KMS. To learn more, choose a Cloud EKM partner that supports single-tenant HSMs and review the requirements for Bare Metal Rack HSMs (/kms/docs/bare-metal-rack-hsm#requirements). This is different from Single-tenant Cloud HSM (/kms/docs/single-tenant-hsm), and you should carefully consider which solution better meets your requirements. 

- Enable audit logging in your external key manager to capture access to and usage of your EKM keys. 

**Caution:** When you use Cloud EKM keys, there's a risk that the key can become unavailable. Depending on which services you're using, this can cause fatal errors or inaccessible data. For example, if you use an external CMEK key to encrypt Google Kubernetes Engine application-layer secrets, your nodes can become unavailable if they can't decrypt the secrets. Inability to access the external key can also cause permanent data loss. For example, if the CMEK key used to encrypt a Spanner database remains unavailable for more than 30 consecutive days, Spanner automatically deletes the database. When the current key version is not available, you cannot recover the data by rotating to a new key version. For better availability, consider using Cloud EKM over VPC or Cloud HSM keys. 

### Restrictions

- When you create a Cloud EKM key using the API or the Google Cloud CLI, it must not have an initial key version. This does not apply to Cloud EKM keys 

created using the Google Cloud console. 

- Automatic rotation is not supported for manually-managed external keys. 

- Cloud EKM operations are subject to specific quotas 

- (/kms/quotas#cloud_ekm_quotas) in addition to the quotas on Cloud KMS operations. 

#### Symmetric encryption keys

- Symmetric encryption keys are only supported for the following: 

   - Customer managed encryption keys (CMEK) in supported integration services (#supported_services). 

   - Symmetric encryption and decryption using Cloud KMS directly (/kms/docs/encrypt-decrypt). 

- Data that is encrypted by Cloud EKM using an externally managed key cannot be decrypted without using Cloud EKM. 

#### Asymmetric signing keys

- Asymmetric signing keys are limited to a subset of Cloud KMS algorithms. 

- Asymmetric signing keys are only supported for the following use cases: 

   - Asymmetric signing using Cloud KMS directly 

   - (/kms/docs/create-validate-signatures). 

   - Custom signing key with Access Approval 

   - (/assured-workloads/access-approval/docs/review-approve-access-requestscustom-keys) 

- Once an asymmetric signing algorithm is set on a Cloud EKM key, it cannot be modified. 

- Signing must be done on the `data` field. 

### External key managers and regions

Cloud EKM needs to be able to reach your keys quickly to avoid an error. When creating a Cloud EKM key, choose a Google Cloud location that is geographically near the location of the external key management partner key. See your external key management partner's documentation to determine which locations they support. 

- Cloud EKM over the internet: available in most Google Cloud locations where Cloud KMS is available, including regional and multi-regional locations. 

- Cloud EKM over a VPC: available in most regional locations (/kms/docs/locations#regional) where Cloud KMS is available. Cloud EKM over a VPC isn't available in multi-regional locations. 

Some locations including `global` and `nam-eur-asia1` aren't available for Cloud EKM. To learn which locations support Cloud EKM, see Cloud KMS locations (/kms/docs/locations). 

#### Multi-region use

When you use an externally managed key with a multi-region, the metadata of the key is available in multiple data centers within the multi-region. This metadata includes the information needed to communicate with the external key management partner. If your application fails over from one data center to another within the multi-region, the new data center initiates key requests. The new data center may have different network characteristics from the previous data center, including distance from the external key management partner and the likelihood of timeouts. We recommend only using a multi-region with Cloud EKM if your chosen external key manager provides low latency to all areas of that multi-region. 

### Partner-managed EKM

Partner-managed EKM lets you use Cloud EKM through a trusted sovereign partner that manages your EKM system for you. With partner-managed EKM, your partner creates and manages the keys that you use in Cloud EKM. The partner ensures that your EKM complies with sovereignty requirements. 

When you onboard with your sovereign partner, the partner provisions resources in the Google Cloud and your EKM. These resources include a Cloud KMS project to 

manage your Cloud EKM keys and an EKM connection configured for EKM key management from Cloud KMS. Your partner creates resources in Google Cloud locations according to your data residency requirements. 

Each Cloud EKM key includes Cloud KMS metadata, which lets Cloud EKM send requests to your EKM to perform cryptographic operations using the external key material that never leaves your EKM. Symmetric Cloud EKM keys also include Cloud KMS internal key material that never leaves Google Cloud. For more information about the internal and external sides of Cloud EKM keys, see How Cloud EKM works (#how_it_works) on this page. 

For more information about partner-managed EKM, see Configure partner-managed Cloud KMS (/sovereign-controls-by-partners/docs/configure-kms). 

### Monitor Cloud EKM usage

**Preview** 

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the Service Specific Terms (/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the launch stage descriptions (https://cloud.google.com/products/#product-launch-stages). 

You can use Cloud Monitoring to monitor your EKM connection. The following metrics can help you understand your EKM usage: 

```
cloudkms.googleapis.com/ekm/external/request_latencies
cloudkms.googleapis.com/ekm/external/request_count
```

For more information about these metrics, see cloudkms metrics (/monitoring/api/metrics_gcp_c#gcp-cloudkms). You can create a dashboard to track these metrics. To learn how to set up a dashboard to monitor your EKM connection, see Monitor EKM usage (/kms/docs/monitor-ekm-usage). 

### Getting support

If you experience an issue with Cloud EKM, contact Support (/kms/docs/support). 

### What's next

- Start using the API (/kms/docs/accessing-the-api). 

- Set up Cloud EKM over the internet (/kms/docs/set-up-ekm-internet). 

- Create an EKM connection (/kms/docs/create-ekm-connection) to use EKM over VPC. 

- Read through the Cloud KMS API Reference (/kms/docs/reference/rest). 

- Learn about Logging (/kms/docs/audit-logging#enabling_audit_logging) in Cloud KMS. Logging is based on operations, and applies to keys with both HSM and software protection levels. 

- See Reference architectures for reliable deployment of Cloud EKM services (/docs/security/reliable-ekm-architectures) for recommendations on configuring an External Key Manager (EKM) service deployment integrated with Cloud EKM. 

Last updated 2026-10-16 UTC. 



## Overview of VPC Service Controls

URL: https://docs.cloud.google.com/vpc-service-controls/docs/overview

This topic provides an overview of VPC Service Controls and describes its advantages and capabilities. 

### Who should use VPC Service Controls

Your organization might own intellectual property in the form of highly sensitive data, or your organization might handle sensitive data that is subject to additional data protection regulations, such as PCI DSS. Unintended loss or disclosure of sensitive data can lead to significant negative business implications. 

If you are migrating from on-premises to the cloud, one of your goals might be to replicate your on-premises network based security architecture as you move your data to Google Cloud. To protect your highly sensitive data, you might want to ensure that your resources can only be accessed from trusted networks. Some organizations might allow public access to resources as long as the request originates from a trusted network, which can be identified based on the IP address of the request. 

To mitigate data exfiltration risks, your organization might also want to ensure secure data exchange across organizational boundaries with fine-grained controls. As an administrator, you might want to ensure the following: 

- Clients with privileged access don't also have access to partner resources. 

- Clients with access to sensitive data can only read public data sets but not write to them. 

### How VPC Service Controls reduces data exfiltration risks

VPC Service Controls helps protect against accidental or targeted action by external entities or insider entities, which helps to minimize unwarranted data exfiltration risks from Google Cloud services such as Cloud Storage and BigQuery. 

You can use VPC Service Controls to create perimeters that protect the resources and data of services that you explicitly specify. 

VPC Service Controls secures your Google Cloud services by defining the following controls: 

- Clients within a perimeter that have private access to resources do not have access to unauthorized (potentially public) resources outside the perimeter. 

- Data cannot be copied to unauthorized resources outside the perimeter using service operations such as `gcloud storage cp` (/sdk/gcloud/reference/storage/cp) or `bq mk` (/bigquery/docs/reference/bq-cli-reference#bq_mk). 

- Data exchange between clients and resources separated by perimeters is secured by using ingress and egress rules 

- (/vpc-service-controls/docs/ingress-egress-rules). 

- Context-aware access to resources is based on client attributes, such as identity type (service account or user), identity, device data, and network origin (IP address or VPC network). The following are examples of contextaware access: 

   - Clients outside the perimeter that are on Google Cloud or on-premises are within authorized VPC resources and use Private Google Access to access resources within a perimeter. 

   - Internet access to resources within a perimeter is restricted to a range of IPv4 and IPv6 addresses. 

For more information, see Context-aware access using ingress rules (/vpc-service-controls/docs/context-aware-access). 

- Access to Google services not fully integrated with VPC Service Controls on private network paths can be controlled by using VPC Service Controls service patterns (/vpc-service-controls/docs/vpc-accessible-services#service-patterns). Administrators can permit access only to specific unsupported API URL patterns, which mitigates risks associated with overly broad access. 

VPC Service Controls provides an extra layer of security defense for Google Cloud services that is independent of Identity and Access Management (IAM). While IAM enables granular _identity-based access control_ , VPC Service Controls enables broader _context-based perimeter security_ , including controlling data egress across 

the perimeter. We recommend using both VPC Service Controls and IAM for defense in depth. 

VPC Service Controls lets you monitor resource access patterns across your service perimeters using Cloud Audit Logs. For more information, see VPC Service Controls audit logging (/vpc-service-controls/docs/audit-logging). 

### Security benefits of VPC Service Controls

VPC Service Controls helps mitigate the following security risks without sacrificing the performance advantages of direct private access to Google Cloud resources: 

- **Access from unauthorized networks using stolen credentials** : By allowing private access only from authorized VPC networks, VPC Service Controls helps protect against the risk of data exfiltration presented by clients using stolen OAuth or service account credentials. 

- **Data exfiltration by malicious insiders or compromised code:** VPC Service Controls complements network egress controls by preventing clients within those networks from accessing the resources of Google-managed services outside the perimeter. 

VPC Service Controls also prevents reading data from or copying data to a resource outside the perimeter. VPC Service Controls prevents service operations such as a `gcloud storage cp` command copying to a public Cloud Storage bucket or a `bq mk` command copying to a permanent external BigQuery table. 

Google Cloud also provides a restricted virtual IP that is integrated with VPC Service Controls. The restricted VIP also allows requests to be made to services supported by VPC Service Controls 

(/vpc-service-controls/docs/supported-products) without exposing those requests to the internet. 

**Public exposure of private data caused by misconfigured IAM** 

**policies** : VPC Service Controls provides an extra layer of security by denying access from unauthorized networks, even if the data is exposed by misconfigured IAM policies. 

**Monitoring access to services** : Use VPC Service Controls in dry run mode (/vpc-service-controls/docs/dry-run-mode) to monitor requests to protected services without preventing access and to understand traffic requests to your projects. You can also create honeypot perimeters to identify unexpected or malicious attempts to probe accessible services. 

You can use an organization access policy and configure VPC Service Controls for your entire Google Cloud organization, or use scoped policies 

(/access-context-manager/docs/scoped-policies) and configure VPC Service Controls for a folder or project in the organization. You retain the flexibility to process, transform, and copy data within the perimeter. 

VPC Service Controls configurations are managed at the organization level by default, but scoped access policies for folders or projects can be used to delegate administration of service perimeters further down the resource hierarchy. 

#### VPC Service Controls and metadata

VPC Service Controls is not designed to enforce comprehensive controls on metadata movement. 

In this context, _data_ is defined as content stored in a Google Cloud resource. For example, the contents of a Cloud Storage object. _Metadata_ is defined as the attributes of the resource or its parent. For example, Cloud Storage bucket names. 

The primary goal of VPC Service Controls is to control the movement of data, rather than metadata, across a service perimeter through supported services. VPC Service Controls also manages access to metadata, but there might be scenarios in which metadata can be copied and accessed without VPC Service Controls policy checks. 

We recommend that you rely on IAM, including the use of custom roles (/iam/docs/understanding-custom-roles), to ensure appropriate control over access to metadata. 

### Capabilities

VPC Service Controls lets you define security policies that prevent access to Google-managed services outside of a trusted perimeter, block access to data from untrusted locations, and mitigate data exfiltration risks. 

You can use VPC Service Controls for the following use cases: 

- Isolate Google Cloud resources and VPC networks (#isolate) into service perimeters 

- Extend perimeters to on-premises networks (#hybrid_access) using authorized VPN or Cloud Interconnect landing zone VPC networks. 

- Control access to Google Cloud resources (#internet) from the internet 

- Protect data exchange across perimeters and organizations 

- (/vpc-service-controls/docs/secure-data-exchange) by using ingress and egress rules 

- Allow context-aware access to resources 

- (/vpc-service-controls/docs/context-aware-access) based on client attributes by using ingress rules 

#### Isolate Google Cloud resources into service perimeters

A **service perimeter** creates a security boundary around Google Cloud resources. A service perimeter allows free communication within the perimeter but, by default, blocks communication to Google Cloud services across the perimeter. 

The perimeter works specifically with Google Cloud managed services. The perimeter doesn't block access to any third-party APIs or services on the internet. 

You can configure a perimeter to control the following types of communications: 

- From public internet to customer resources within managed services 

- From virtual machines (VMs) to a Google Cloud service (API) 

- Between Google Cloud services 

VPC Service Controls doesn't require you to have a Virtual Private Cloud (VPC) network. To use VPC Service Controls without having any resources on a VPC network, you can allow traffic from external IP ranges or certain IAM (/iam/docs) 

principals. For more information, see Create and manage access levels 

(/vpc-service-controls/docs/use-access-levels#create_and_manage_access_levels). 

Here are some examples of VPC Service Controls creating a security boundary: 

- A VM within a VPC network (/vpc/docs/vpc) that is part of a service perimeter can read from or write to a Cloud Storage bucket in the same perimeter. However, VPC Service Controls doesn't allow VMs within VPC networks that are outside the perimeter to access Cloud Storage buckets that are inside the perimeter. You must specify an ingress policy to allow VMs within VPC networks that are outside the perimeter to access Cloud Storage buckets that are inside the perimeter. 

- A host project that contains multiple VPC networks has a different perimeter policy for each VPC network in the host project. 

- A copy operation between two Cloud Storage buckets succeeds if both buckets are in the same service perimeter, but if one of the buckets is outside the perimeter, the copy operation fails. 

- VPC Service Controls doesn't allow a VM within a VPC network that is inside a service perimeter to access Cloud Storage buckets that are outside the perimeter. 

The following diagram shows a service perimeter that allows communication between a VPC project and Cloud Storage bucket inside the perimeter but blocks all communication across the perimeter: 

#### Extend perimeters to an authorized VPN or Cloud Interconnect

You can configure private communication to Google Cloud resources from VPC networks that span hybrid environments with Private Google Access on-premises extensions (/vpc-service-controls/docs/private-connectivity). To privately access Google Cloud resources within a perimeter, the VPC network that contains the landing zone from on-premises must be a part of the perimeter for resources in the onpremises network. 

VMs with private IP addresses in a VPC network secured by a service perimeter cannot access managed resources outside the service perimeter. If necessary, you can continue to enable inspected and audited access to all Google APIs (for example, Gmail) over the internet. 

The following diagram shows a service perimeter that extends to hybrid environments with Private Google Access: 

#### Control access to Google Cloud resources from the internet

Access from the internet to managed resources within a service perimeter is denied by default. Optionally, you can enable access based on the context of the request. To do so, you can create ingress rules or access levels to permit access based on various attributes, such as the source IP address, identity, or source 

Google Cloud project. If requests made from the internet don't meet the criteria defined in the ingress rule or access level, the requests are denied. 

To use the Google Cloud console to access resources within a perimeter, you must configure an access level that allows access from one or more IPv4 and IPv6 ranges, or to specific user accounts. 

The following diagram shows a service perimeter that allows access from the internet to protected resources based on the configured access levels, such as IP address or device policy: 

### Other controls to mitigate data exfiltration risks

- **Domain restricted sharing** : You can consider setting up an organizational policy to limit resource sharing to identities that belong to a particular organization resource. For more information, see Restricting identities by domain (/resource-manager/docs/organization-policy/restricting-domains). 

- **Uniform bucket-level access** : To uniformly control access to your Cloud Storage buckets, consider setting up bucket-level IAM permissions. Using uniform bucket-level access lets you use other Google Cloud security features such as domain restricted sharing, Workforce Identity Federation 

- (/iam/docs/workforce-identity-federation), and IAM conditions 

- (/iam/docs/conditions-overview). 

- **Multi-factor authentication** : We recommend using multi-factor authentication to access your Google Cloud resources 

(/identity/solutions/enforce-mfa). 

**Post-deployment scans** : You can consider using the following postdeployment scanning tools to scan for open Cloud Storage buckets: 

   1. Security Command Center 

      - (/security-command-center/docs/security-command-center-overview) 

   2. Cloud Asset Inventory (/asset-inventory/docs/overview) to search asset metadata history and analyse IAM policy to understand who has access to what. 

   3. Third-party tools like Palo Alto PrismaCloud 

- **De-identification of sensitive data** : You can consider using Sensitive Data Protection (/sensitive-data-protection/docs/sensitive-data-protection-overview) to discover, classify, and de-identify sensitive data inside and outside Google Cloud. De-identification of sensitive data can be done by redaction, tokenization, or encryption. 

- **Automation using infrastructure-as-code tools** : We recommend that you deploy Cloud Storage buckets using an automation tool to control access to the buckets. Pass the infrastructure-as-code through human or automated reviews before deployment. 

### Unsupported Services

For more information on products and services that are supported by VPC Service Controls, refer to the Supported products (/vpc-service-controls/docs/supported-products) page. 

**Warning:** While it may be possible to enable unsupported services to access the data of supported products and services, we recommend that you do not. Unexpected issues might occur when attempting to access a supported service using an unsupported service, especially within the same project. 

Unsupported services may not function at all when enabled in a project protected by VPC Service Controls, especially when low-level storage services like Cloud Storage or Pub/Sub are restricted. We recommend deploying unsupported services in projects outside perimeters. To allow these services to access data in resources within a perimeter, create an access level (/vpc-service-controls/docs/use-access-levels) that includes the service account for that service and apply it to perimeters as needed 

(/vpc-service-controls/docs/manage-service-perimeters#add-access-level). 

Attempting to restrict an unsupported service using the `gcloud` command-line tool or the Access Context Manager API will result in an error. 

Cross-project access to data of supported services will be blocked by VPC Service Controls. Additionally, the restricted VIP can be used to block the ability of workloads to call unsupported services. 

### Known limitations

There are some known limitations with certain Google Cloud services, products, and interfaces when you use VPC Service Controls. For example, VPC Service Controls doesn't support all Google Cloud services. Therefore, don't enable unsupported Google Cloud services in the perimeter. For more information, see the VPC Service Controls supported products list 

(/vpc-service-controls/docs/supported-products#supported_products). If you need to use a service that VPC Service Controls doesn't support, enable the service in a project that is outside the perimeter. 

We recommend that you review known limitations before you include Google Cloud services in the perimeter. For more information, see the VPC Service Controls service limitations (/vpc-service-controls/docs/supported-products#service-limitations). 

### Glossary

In this topic, you have learned about several new concepts introduced by VPC Service Controls: 

**VPC Service Controls** 

Technology that enables you to define a service perimeter around resources of Google-managed services to control communication to and between those services. 

**service perimeter** 

A service perimeter around Google-managed resources. Allows free communication within the perimeter but, by default, blocks all communication across the perimeter. 

**ingress rule** 

A rule that allows an API client that is outside the perimeter to access resources within a perimeter. For more information, see Ingress and egress rules (/vpc-service-controls/docs/ingress-egress-rules). 

**egress rule** 

A rule that allows an API client or resource that is inside the perimeter to access Google Cloud resources outside the perimeter. The perimeter does not block access to any third-party API or services on the internet. 

**service perimeter bridge** 

A perimeter bridge allows projects in different service perimeters to communicate. Perimeter bridges are bidirectional, allowing projects from each service perimeter equal access within the scope of the bridge. 

**Note:** Instead of using a perimeter bridge, we recommend using ingress and egress rules that provide more granular controls. 

**Access Context Manager** 

A context-aware request classification service that can map a request to an access level based on specified attributes of the client, such as the source IP address. For more information, see Overview of Access Context Manager (/access-context-manager/docs/overview). 

**access level** 

A classification of requests over the internet based on several attributes, such as source IP range, client device, geolocation, and others. Just like an ingress rule, you can use an access level to configure a service perimeter to grant access from the internet based on the access level associated with a request. You can create an access level using Access Context Manager (/access-context-manager/docs/create-basic-access-level). 

**access policy** 

A Google Cloud resource object that defines service perimeters. You can create access policies that are scoped to specific folders or projects alongside an access policy that can apply to the entire organization. An organization can have only one organization-level access policy. 

**scoped policy** 

A scoped policy is an access policy that is scoped to specific folders or projects alongside an access policy that applies to the entire organization. For more information, see Overview of scoped policies 

(/access-context-manager/docs/scoped-policies). 

**restricted VIP** 

The restricted VIP provides a private network route for products and APIs supported by VPC Service Controls in order to make data and resources used by those products inaccessible from the internet. `restricted.googleapis.com` resolves to `199.36.153.4/30` . This IP address range is not announced to the internet. 

### What's next

- Learn about service perimeter configuration 

- (/vpc-service-controls/docs/service-perimeters). 

- Understand how to manage VPC networks in service perimeters 

- (/vpc-service-controls/docs/vpc-perimeters-management) 

- Review the known service limitations 

- (/vpc-service-controls/docs/supported-products#service-limitations). 

Last updated 2026-10-13 UTC.
