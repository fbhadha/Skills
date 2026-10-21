# Gemini Enterprise: platform, security, agents, cost, monitoring / Use customer-managed encryption keys to View costs
Source: 01-Gemini-Enterprise-Platform-security-agents-cost-monitoring.pdf, pages 272-311, extracted 2026-10-18

Contains:
- Use customer-managed encryption keys (pages 272-297) https://docs.cloud.google.com/gemini/enterprise/docs/cmek
- Turn off Gemini Enterprise (pages 298-298) https://docs.cloud.google.com/gemini/enterprise/docs/turn-off-gemini-enterprise
- Manage costs: overview (pages 299-301) https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview
- View feature usage (pages 302-304) https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage
- Configure overages (pages 305-308) https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages
- View costs (pages 309-311) https://docs.cloud.google.com/gemini/enterprise/docs/view-costs

## Use customer-managed encryption keys

URL: https://docs.cloud.google.com/gemini/enterprise/docs/cmek

**Warning:** CMEK settings apply only after the CMEK key is registered. Any app or data connector created prior to that will remain unprotected. 

In order to ensure that your CmekConfig is applied when creating an app or data connector, you need to either set the CmekConfig as default or provide the CmekConfig explicitly as part of resource creation. 

**Key Term:** In Gemini Enterprise, the term _data store_ can be used interchangeably with the term _connector_ or _data connector_ . 

By default, Gemini Enterprise encrypts customer content at rest. Gemini Enterprise handles encryption for you without any additional actions on your part. This option is called _Google default encryption_ . 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in Cloud KMS (/kms/docs) with CMEK-integrated services including Gemini Enterprise. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you track key usage 

(/kms/docs/view-key-usage), view audit logs, and control key lifecycles. Instead of Google owning and managing the symmetric key encryption keys (KEKs) 

(/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS. 

After you set up your resources with CMEKs, the experience of accessing your Gemini Enterprise resources is similar to using Google default encryption. For more information about your encryption options, see Customer-managed encryption keys (CMEK) (/kms/docs/cmek). 

When a CMEK key is registered, Gemini Enterprise calls Cloud KMS periodically to maintain a logically isolated instance of your data. This happens even if the CMEK config isn't set as the default and there are no apps or data connectors using it. The usage comes from setting up and running the instance, not from the volume of 

data or number of users accessing it. See Cloud Key Management Service pricing (/kms/pricing). 

To completely shut off all Cloud KMS usage, you must unregister your Cloud KMS key (#key-unregistration), disable the key, or revoke its permissions. Disabling the Gemini Enterprise API doesn't delete your CmekConfig or your data, and you continue to be billed for CMEK usage. 

**Note:** Apps or data stores in US or EU regions require data encryption. 

**Note:** Gemini Enterprise data at rest uses Google-owned and Google-managed encryption key (GMEK) by default 

(https://docs.cloud.google.com/docs/security/encryption/default-encryption). CMEK, as described on this page, lets you use your own keys instead of the GMEK keys. 

**Note:** If you want to ensure that your Gemini Enterprise resources are always protected by CMEK, we strongly recommend that you configure a CMEK organization policy. For more information, see Organization policy constraints (/kms/docs/org-policy-constraints). 

### Limitations of Cloud KMS in Gemini Enterprise

The following limitations apply to CMEK (Cloud KMS) keys in Gemini Enterprise: 

- Keys that are already applied to an app or data connector can't be changed, although key versions can be rotated. 

- End-user data is an exception to the preceding limitation. Unlike apps and data connectors, which keep the key that they were created with, end-user data always follows the current default CmekConfig. For more information, see End-user data and the default Cloud KMS configuration (#end-user-data). 

- CMEK-protection with Gemini Enterprise is not integrated with Cloud Asset Inventory (/asset-inventory/docs/asset-inventory-overview) search. 

- You must use US or EU multi-region apps or data stores (not global ones). For more information about multi-regions and data residency, including limits associated with using non-global locations, see locations 

- (/gemini/enterprise/docs/locations). 

- If you need to register more than one key for a project, contact your Google account team to request a quota increase for CMEK configurations, providing a justification for why you need more than one key. 

- The following limitations apply to EKM or HSM with CMEK: 

   - Your EKM and HSM quota for encrypt and decrypt calls should have at least 1,000 QPM of headroom. For how to check your quotas, see Check your Cloud KMS quotas (/kms/docs/monitor-adjust-quotas#check_your_quotas). 

   - If using EKM, the key must be reachable for more than 90% of any time window of longer than 30 seconds. If the key isn't reachable for this amount of time, it can negatively impact indexing and search freshness. 

   - If there are billing issues, persistent out-of-quota issues, or persistent unreachability issues for more than 12 hours, the service automatically turns down the CmekConfig associated with the EKM or HSM key. 

- Apps or data connectors created before a key is registered to the project can't be protected by the key. 

- For apps with multiple data connectors, if one data connector uses a CMEK configuration, all other data connectors must also use the same CMEK configuration. 

- First-party connectors (/gemini/enterprise/docs/connectors/create-data-store) are not CMEK-compliant except for the "import-once" and "periodic" apps and data connectors for BigQuery and Cloud Storage. 

- For Gemini Notebook Enterprise, additional Cloud KMS restrictions apply. See Limitations of Cloud KMS in Gemini Notebook Enterprise 

- (/gemini/enterprise/notebooklm-enterprise/docs/cmek#limitations). 

- You can use Terraform to configure CMEK for Gemini Enterprise. See google_discovery_engine_cmek_confgi 

- (https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_ engine_cmek_config) 

### Before you begin

Make sure you satisfy the following prerequisites: 

- Create a multi-region symmetric Cloud KMS key. See Create a key ring (/kms/docs/create-key-ring) and Create a key (/kms/docs/create-key) in the Cloud KMS documentation. 

   - Set the rotation period to **Never (Manual rotation)** . 

   - For **Location** , select **Multi-region** , and select **europe** or **us** from the drop-down. 

- If you use third-party connectors, create three single-region symmetric Cloud KMS keys. It is optional otherwise. 

   - Set the rotation period to **Never (Manual rotation)** . 

   - For **Location** , select **region** . 

   - Select the single-regions in the following table from the location dropdown. You need to have all three keys with you when you Register your Cloud KMS keys for third-party connectors 

   - (#third-party-connectors-key-registration). 

|`us single-regions`|`europe single-regions`|
|---|---|
|`us-east1`|`europe-west1`|
|`us-central1`|`europe-west4`|
|`us-west1`|`europe-north1`|

- The CryptoKey Encrypter/Decrypter IAM role 

- ( `roles/cloudkms.cryptoKeyEncrypterDecrypter` ) on the key has been granted to the Discovery Engine service agent. The service agent account has an email address that uses the following format: `service-` _`PROJECT_NUMBER`_ `@gcp-sadiscoveryengine.iam.gserviceaccount.com` . For general instructions on how to add a role to a service agent, see Grant or revoke a single role 

- (/iam/docs/manage-access-service-accounts). 

- The CryptoKey Encrypter/Decrypter IAM role ( `roles/cloudkms.cryptoKeyEncrypterDecrypter` ) on the key has been granted to the Cloud Storage service agent. If this role is not granted, data import for CMEK-protected apps and data connectors will fail because Discovery Engine is not able to make the CMEK-protected, temporary bucket and directory that is required for importing. 

- Don't create any apps or data connectors that you want managed by your key until after you have completed the key registration (#key-registration) instructions on this page. 

- Set your key as the default before your end users start using Gemini Enterprise. End-user data that is created before the default is set isn't migrated to the key. For more information, see End-user data and the default Cloud KMS configuration (#end-user-data). 

### Register your Cloud KMS key

To encrypt data using CMEK, you must register your multi-region key. Optionally, if your data needs single-region keys, for example, when using third-party connectors, you also need to register your single-region keys. 

#### Register your multi-region Cloud KMS key

Before you begin 

Make sure of the following: 

- The region isn't already protected by a key. The procedure below fails if a key is already registered for the region through the REST command. To determine if there is an active key in Gemini Enterprise for a location, see View Cloud KMS keys (#view-key). 

- You have the Gemini Enterprise Admin 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) 

- ( `roles/discoveryengine.agentspaceAdmin` ) role. 

Procedure 

RESTConsole (#console) (#rest) 

To register your own key for Gemini Enterprise, follow these steps: 

1. Call the `UpdateCmekConfig` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs/patch) method with the key that you want to register. 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-d
'{"kmsKey":"projects/KMS_PROJECT_ID/locations/KMS_LOCATION/keyRings/
KEY_RING/cryptoKeys/KEY_NAME"}' \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/
LOCATION/cmekConfigs/CMEK_CONFIG_ID?set_default=SET_DEFAULT"
```

Replace the following: 

- _`KMS_PROJECT_ID`_ : the ID of your project that contains the key. The project number won't work. 

- _`KMS_LOCATION`_ : the multi-region of your key: `us` or `europe` . 

- _`KEY_RING`_ : the name of the key ring that holds the key. 

- _`KEY_NAME`_ : the name of the key. 

- _`PROJECT_ID`_ : the ID of your project that contains the app or data connector. 

- _`LOCATION`_ : the multi-region of your app or data connector: `us` or `eu` . 

- _`CMEK_CONFIG_ID`_ : set a unique ID for the CmekConfig resource, for example, `default_cmek_config` . 

- _`SET_DEFAULT`_ : set to `true` to use the key as the default key for subsequent apps and data connectors created in the multi-region. 

**Important:** **_SET_DEFAULT_** is required to automatically apply the CmekConfig on subsequent resources. 

**Note:** The default CmekConfig also protects end-user data. Unlike apps and data connectors, end-user data follows the default CmekConfig when you change it. For more information, see End-user data and the default Cloud KMS configuration (#end-user-data). 

<sup>Example command and result</sup> 

```
$ curl -X PATCH
-H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
-d '{"kmsKey":"projects/key-project-456/locations/us/keyRings/my-key-
ring/cryptoKeys/my-key"}'
"https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-
project-123/locations/us/cmekConfigs/default_cmek_config?
set_default=true"
{
"name": "projects/my-ai-app-project-
123/locations/us/operations/update-cmek-config-56789",
"metadata": {
 "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.UpdateCmekConfig
Metadata"
}
}
```

2. Verify that your key is ready to use before you create any apps or data connectors. A registered key can't protect resources until it's ready. It typically takes a few minutes to register a key. See Verify that your Cloud KMS key is ready to use (#verify-key-ready). 

To track the registration operation, you can record the `name` value returned by the method and follow Get details about a long-running operation (/gemini/enterprise/docs/long-running-operations#get-details). 

After the key is ready, new apps and data connectors in that multiregion are protected by the key. For general information about creating apps, see About apps and data stores 

(/gemini/enterprise/docs/apps-data-stores). 

3. Create the app. For instructions, see Create an app 

   - (/gemini/enterprise/docs/create-app) and About apps and data stores 

   - (/gemini/enterprise/docs/apps-data-stores). 

It can take several hours for the ingested data to show up in search results. 

**Note:** After you create the app or data stores, verify that they are protected by the keys. For more information, see verify that an app or data connector is protected by a Cloud KMS key (#verify-cmek). 

#### Register single-region Cloud KMS keys for third-party connectors

RESTConsole (#console) (#rest) 

To register your own key for Gemini Enterprise, follow these steps: 

1. Call the `UpdateCmekConfig` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations/updateCmekConfig) method with the key that you want to register. 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-d
'{"kmsKey":"projects/KMS_PROJECT_ID/locations/KMS_LOCATION/keyRings/
KEY_RING/cryptoKeys/KEY_NAME"}' \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/
```

Replace the following: 

- _`KMS_PROJECT_ID`_ : the ID of your project that contains the key. The project number won't work. 

- _`KMS_LOCATION`_ : the multi-region of your key: `us` or `europe` . 

- _`KEY_RING`_ : the name of the key ring that holds the key. 

- _`KEY_NAME`_ : the name of the key. 

- _`PROJECT_ID`_ : the ID of your project that contains the app or data connector. 

- _`LOCATION`_ : the multi-region of your app or data connector: `us` or `eu` . 

- _`CMEK_CONFIG_ID`_ : Set a unique ID for the CmekConfig resource, for example, `default_cmek_config` . 

- _`SET_DEFAULT`_ : set to `true` to use the key as the default key for subsequent apps and data connectors created in the multi-region. 

**Important:** **_SET_DEFAULT_** is required to automatically apply the CmekConfig on subsequent resources. 

**Note:** The default CmekConfig also protects end-user data. Unlike apps and data connectors, end-user data follows the default CmekConfig when you change it. For more information, see End-user data and the default Cloud KMS configuration (#end-user-data). 

<sup>Example command and result</sup> 

- `$ curl -X PATCH` 

- `-H "Authorization: Bearer $(gcloud auth print-access-token)"` 

- `-H "Content-Type: application/json"` 

- `-d '{"kmsKey":"projects/key-project-456/locations/us/keyRings/my-key-` 

```
ring/cryptoKeys/my-key"}'
"https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-
project-123/locations/us/cmekConfigs/default_cmek_config?
set_default=true"
{
"name": "projects/my-ai-app-project-
123/locations/us/operations/update-cmek-config-56789",
"metadata": {
 "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.UpdateCmekConfig
Metadata"
}
}
```

2. Optional: Record the `name` value returned by the method and follow the instructions in Get details about a long-running operation 

(/gemini/enterprise/docs/long-running-operations#get-details) to see when the operation is complete. 

It typically takes a few minutes to register a key. 

After the operation completes, new apps and data connectors in that multi-region are protected by the key. For general information about creating apps, see About apps and data stores 

(/gemini/enterprise/docs/apps-data-stores). 

3. If you use third-party connectors 

(/gemini/enterprise/docs/connect-third-party-data-source) and want to protect your third-party data with your own key, then create three additional single-region keys as follows: 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-d '{
"kmsKey":"projects/KMS_PROJECT_ID/locations/KMS_LOCATION/keyRings/KEY
_RING/cryptoKeys/KEY_NAME",
 "singleRegionKeys": [ \
   {"kmsKey":
"projects/KMS_PROJECT_ID/locations/REGION_1/keyRings/KEY_RING_1/crypt
oKeys/KEY_NAME_1"}, \
   {"kmsKey":
"projects/KMS_PROJECT_ID/locations/REGION_2/keyRings/KEY_RING_2/crypt
oKeys/KEY_NAME_2"}, \
   {"kmsKey":
"projects/KMS_PROJECT_ID/locations/REGION_3/keyRings/KEY_RING_3/crypt
oKeys/KEY_NAME_3"} \
 ] \
}' \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/
LOCATION/cmekConfigs/CMEK_CONFIG_ID?set_default=SET_DEFAULT"
```

- Replace the following: 

   - _`KMS_PROJECT_ID`_ : the ID of your project that contains the key. The project number won't work. 

   - Set the `REGION` values: 

      - _`REGION_1`_ : for the `eu` location, set this to `europe-west1` , and for the `us` location, set this to `us-east1` . 

      - _`REGION_2`_ : for the `eu` location, set this to `europe-west4` , and for the `us` location, set this to `us-central1` . 

      - _`REGION_3`_ : for the `eu` location, set this to `europe-north1` , and for the `us` location, set this to `us-west1` . 

   - _`KEY_RING`_ : the name of the key ring that holds the key. 

   - _`KEY_NAME`_ : the name of the multi-region key. 

   - _`LOCATION`_ : the multi-region of your app or data connector: `us` or `eu` . 

   - _`PROJECT_ID`_ : the ID of your project that contains the app or data connector. 

   - _`CMEK_CONFIG_ID`_ : Set to the ID for the CmekConfig resource. Use the same value as in Step 1, for example, `default_cmek_config` . 

- _`SET_DEFAULT`_ : set to `true` to use the key as the default key for subsequent apps and data connectors created in the multi-region. 

- <sup>Example command and result</sup> 

```
$ curl -X PATCH
-H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
-d '{
"kmsKey":"projects/key-project-456/locations/us/keyRings/my-key-
ring/cryptoKeys/my-key",
"singleRegionKeys": [
 {"kms_key": "projects/key-project-456/locations/us-
east1/keyRings/my-key-ring/cryptoKeys/my-key"},
 {"kms_key": "projects/key-project-456/locations/us-
central1/keyRings/my-key-ring/cryptoKeys/my-key"},
 {"kms_key": "projects/key-project-456/locations/us-
west1/keyRings/my-key-ring/cryptoKeys/my-key"}
]
}'
"https://us-discoveryengine.googleapis.com/v1/projects/my-ai-
app-project-123/locations/us/cmekConfigs/default_cmek_config?
set_default=true"
{
"name": "projects/my-ai-app-project-
123/locations/us/operations/update-cmek-config-56789",
"metadata": {
"@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.UpdateCmekC
onfigMetadata"
}
}
```

4. Verify that your key is ready to use before you create any apps or data connectors. A registered key can't protect resources until it's ready. See Verify that your Cloud KMS key is ready to use (#verify-key-ready). 

5. Create the app. For instructions, see Create an app (/gemini/enterprise/docs/create-app) and About apps and data stores 

(/gemini/enterprise/docs/apps-data-stores). 

It can take several hours for the ingested data to show up in search results. 

**Note:** After you create the app or data stores, verify that they are protected by the keys. For more information, see verify that an app or data connector is protected by a key (#verify-cmek). 

### View Cloud KMS keys

To view a registered key for Gemini Enterprise, do one of the following: 

- If you have the CmekConfig resource name, call the `GetCmekConfig` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs/get) method: 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/c
mekConfigs/CMEK_CONFIG_ID"
```

Replace the following: 

- _`LOCATION`_ : the multi-region of your app or data connector: `us` or `eu` . 

- _`PROJECT_ID`_ : the ID of your project that contains the data. 

- _`CMEK_CONFIG_ID`_ : the ID of the CmekConfig resource. If you registered your key using the console, the ID is `default_cmek_config` . 

An example curl call and response looks like this: 

```
$ curl -X GET
-H "Authorization: Bearer $(gcloud auth print-access-token)"
"https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-
123/locations/us/cmekConfigs/default_cmek_config"
{
 "name":
 "projects/my-ai-app-project-
123/locations/us/cmekConfigs/default_cmek_config",
```

- `"kmsKey": "projects/key-project-456/locations/us/keyRings/my-key-` 

- `ring/cryptoKeys/my-key",` 

- `"kmsKeyVersion": "projects/key-project-456/locations/us/keyRings/my-key-` 

- `ring/cryptoKeys/my-key/cryptoKeyVersions/2",` 

- `"state": "ACTIVE",` 

- `"isDefault": true,` 

- `"lastRotationTimestampMicros": "1788220800000000"` 

```
}
```

- If you don't have the CmekConfig resource name, call the `ListCmekConfigs` (/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs/list) method: 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/c
mekConfigs"
```

Replace the following: 

- _`LOCATION`_ : the multi-region of your app or data connector: `us` or `eu` . 

- _`PROJECT_ID`_ : the ID of your project that contains the data. 

An example curl call and response looks like this: 

```
$ curl -X GET
-H "Authorization: Bearer $(gcloud auth print-access-token)"
"https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-
123/locations/us/cmekConfigs"
{
 "cmek_configs": [
   {
     "name":
     "projects/my-ai-app-project-
123/locations/us/cmekConfigs/default_cmek_config",
     "kmsKey": "projects/key-project-456/locations/us/keyRings/my-key-
ring/cryptoKeys/my-key",
     "kmsKeyVersion": "projects/key-project-456/locations/us/keyRings/my-
key-ring/cryptoKeys/my-key/cryptoKeyVersions/2",
     "state": "ACTIVE",
     "isDefault": true,
     "lastRotationTimestampMicros": "1788220800000000"
   }
 ]
}
```

### Verify that your Cloud KMS key is ready to use

After you register a key, you must verify that it's ready to use before it can protect any resources: 

1. View your registered Cloud KMS keys. See View Cloud KMS keys (#view-key). 

2. Review the output from the command. The CmekConfig is ready for use if all of the following values are in the output: 

   - `"state": "ACTIVE"` 

```
"isDefault": true
```

If `"isDefault": true` , then the key is automatically applied to protect new apps and data connectors. 

You can also check that a default CMEK configuration is set (that is, `"isDefault": true` ) using the Google Cloud console: 

1. In the Google Cloud console, go to the **Gemini Enterprise** page. 

2. Click **Settings** , and select the **CMEK** tab. 

3. Check that the configuration status for your location shows your registered key. 

### Unset the default Cloud KMS configuration

Unsetting the default stops new apps and data connectors from being automatically protected by the key, and removes CMEK protection from end-user data. Existing apps and data connectors keep the key that they were created with. 

To unset the default, call the `UpdateCmekConfig` 

(/gemini/enterprise/docs/reference/rest/v1/projects.locations.cmekConfigs/patch) method with `set_default` set to `false` : 

```
curl -X PATCH \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/cmekCo
nfigs/CMEK_CONFIG_ID?set_default=false"
```

Replace the following: 

- _`LOCATION`_ : the multi-region of your app or data connector: `us` or `eu` . 

- _`PROJECT_ID`_ : the ID of your project that contains the app or data connector. 

- _`CMEK_CONFIG_ID`_ : the ID of the CmekConfig resource. If you registered your key using the console, the ID is `default_cmek_config` . 

**Caution:** Unsetting the default removes CMEK protection from end-user data. For more information about the effect on your end users, see End-user data and the default Cloud KMS 

Unsetting the default doesn't delete the CmekConfig or your key, and Cloud KMS usage continues. To stop Cloud KMS usage, unregister your key (#key-unregistration). 

### Unregister your Cloud KMS key

To unregister your key from Gemini Enterprise, follow these steps: 

1. Call the `DeleteCmekConfig` method with the CmekConfig resource name that you want to unregister. 

```
curl -X DELETE \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/c
mekConfigs/CMEK_CONFIG_ID"
```

Replace the following: 

- _`LOCATION`_ : the multi-region of your app or data connector: `us` or `eu` . 

- _`PROJECT_ID`_ : the ID of your project that contains the app or data connector. 

- _`CMEK_CONFIG_ID`_ : the ID of the CmekConfig resource. If you registered your key using the console, the ID is `default_cmek_config` . 

An example curl call and response looks like this: 

```
$ curl -X DELETE
-H "Authorization: Bearer $(gcloud auth print-access-token)"
"https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-
123/locations/us/cmekConfigs/default_cmek_config"
{
"name": "projects/my-ai-app-project-123/locations/us/operations/delete-
cmek-config-56789",
"metadata": {
 "@type":
"type.googleapis.com/google.cloud.discoveryengine.v1.DeleteCmekConfigMetad
ata"
}
}
```

2. Optional: Record the `name` value returned by the method and follow the instructions in Get details about a long-running operation (/gemini/enterprise/docs/long-running-operations#get-details) to see when the operation is complete. 

Deleting a CmekConfig is a long-running operation that can take up to a couple of days to complete. This is because the underlying encrypted resources are fully deprovisioned before the CmekConfig is removed. 

**Note:** A CmekConfig resource can only be deleted if no Gemini Enterprise resources are being protected by that CmekConfig resource. 

If end-user data is still protected by the CmekConfig, the request fails with a `FAILED_PRECONDITION` error similar to the following: 

```
The default user store is currently protected by this CmekConfig. Please unset
the default CmekConfig (UpdateCmekConfig with set_default set to false) before
trying to delete the CmekConfig.
```

To resolve this error, unset the default Cloud KMS configuration (#unset-default), and then retry the delete request. Unsetting the default removes CMEK protection from end-user data. For more information, see End-user data and the default Cloud KMS configuration (#end-user-data). 

### Verify that an app or data connector is protected by a key

Apps and data connectors that are created after your key is registered are protected by the key. If you want to confirm that a particular app or data connector is protected by your key, follow these steps: 

#### Verify using the Google Cloud console

1. To verify whether an app is protected by a key: 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

   - b. Click **Apps** , and select your app. 

   - c. Click **Security** , and find the **CMEK configuration** section. 

   - d. Check that the **KMS key** field shows your registered key. 

1. To verify whether a data connector is protected by a key: 

   - a. In the Google Cloud console, go to the **Gemini Enterprise** page. 

   - b. Click **Data stores** , and select your data connector. 

   - c. Check that the **KMS key** field shows your registered key. 

#### Verify using the CLI / API

1. To verify for a data store: 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "x-goog-user-project: PROJECT_ID" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/c
ollections/default_collection/dataStores/DATA_STORE_ID"
```

Replace the following: 

_`LOCATION`_ : the multi-region of your project: `us` or `eu` . 

- _`PROJECT_ID`_ : the ID of your project that contains the app or data connector. 

- _`DATA_STORE_ID`_ : the ID of the data store associated with your app or data connector. 

An example curl call looks like this: 

```
curl -X GET
-H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
-H "x-goog-user-project: my-ai-app-project-123"
"https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-
123/locations/us/collections/default_collection/dataStores/my-data-store-
1"
```

2. To verify for an app: 

```
curl -X GET \
-H "Authorization: Bearer $(gcloud auth print-access-token)" \
-H "Content-Type: application/json" \
-H "x-goog-user-project: PROJECT_ID" \
"https://LOCATION-
discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/c
ollections/default_collection/engines/ENGINE_ID"
```

Replace the following: 

- _`LOCATION`_ : the multi-region of your project: `us` or `eu` . 

- _`PROJECT_ID`_ : the ID of your project that contains the app. 

- _`ENGINE_ID`_ : the ID of your app. 

An example curl call looks like this: 

```
curl -X GET
-H "Authorization: Bearer $(gcloud auth print-access-token)"
-H "Content-Type: application/json"
-H "x-goog-user-project: my-ai-app-project-123"
"https://us-discoveryengine.googleapis.com/v1/projects/my-ai-app-project-
123/locations/us/collections/default_collection/engines/my-app"
```

3. Review the output from the command: If the `cmekConfig` field is in the output and the `kmsKey` field shows the key that you registered, then the app or data connector is protected by the key. 

An example response for a data store looks like this: 

```
{
"name":
"projects/969795412903/locations/us/collections/default_collection/dataSto
res/my-data-store-1",
"displayName": "my-data-store-1",
"industryVertical": "GENERIC",
"createTime": "2023-09-05T21:20:21.520552Z",
"solutionTypes": [
  "SOLUTION_TYPE_SEARCH"
],
"defaultSchemaId": "default_schema",
"cmekConfig": {
  "name":
"projects/969795412903/locations/us/collections/default_collection/dataSto
res/my-data-store-1/cmekConfigs/default_cmek_config",
  "kmsKey": "projects/my-ai-app-project-123/locations/us/keyRings/my-key-
ring/cryptoKeys/my-key"
}
}
```

An example response for an app looks like this: 

```
{
 "name":
"projects/969795412903/locations/us/collections/default_collection/engines
/my-app",
 "displayName": "my-app",
 "dataStoreIds": [
   "my-data-store-1"
 ],
 "solutionType": "SOLUTION_TYPE_SEARCH",
 "searchEngineConfig": {
   "searchTier": "SEARCH_TIER_STANDARD"
 },
 "industryVertical": "GENERIC",
 "appType": "APP_TYPE_INTRANET",
 "cmekConfig": {
  "name":
"projects/969795412903/locations/us/collections/default_collection/dataSto
res/my-data-store-1/cmekConfigs/default_cmek_config",
  "kmsKey": "projects/my-ai-app-project-123/locations/us/keyRings/my-key-
ring/cryptoKeys/my-key"
}
}
```

### Other data protected by the Cloud KMS key

In addition to data in the apps and data connectors, your keys can protect other types of app-owned core information held by Gemini Enterprise, such as the session data generated during search with follow-ups 

(/gemini/enterprise/docs/answer#commands_for_follow-up_questions). This kind of core information is CMEK-protected if the apps and data connectors are CMEK-protected. 

Although you can't run a specific command to verify that sessions are protected, you can verify if the app is protected. Run the Verify that an app or data connector is protected by a key (#verify-cmek) command for the app to see the key in the cmekConfig resource. Then you'll know that the session data is protected. 

#### End-user data and the default Cloud KMS configuration

Gemini Enterprise stores data about your end users, such as their personalization settings, their UI preferences, and the credentials that authorize your data connectors on their behalf. Gemini Enterprise provisions this storage for your project automatically. You don't create or delete it, and you can't assign a key to it directly. 

Instead, end-user data is protected by whichever CmekConfig is the default for the location. Its protection therefore changes when the default changes: 

|Action|Effect on end-user data|
|---|---|
|You set a CmekConfig as<br>the default (`set_`<br>`default=true`)|End-user data is protected by that key.|
|You set a different|End-user data is protected by the new key. Data that is stored under|
|CmekConfig as the<br>default|the previous key isn't migrated and becomes inaccessible.|
|You unset the default|End-user data is no longer CMEK-protected and reverts to Google-|
|(`set_default=false`)|owned and Google-managed encryption key. Data that is stored<br>under the previous key isn't migrated and becomes inaccessible.|

**Caution:** Changing or unsetting the default CmekConfig takes effect immediately, and enduser data that is stored under the previous key isn't migrated. Your end users might need to authorize their data connectors again, and their personalization settings and UI preferences might be reset. Plan these changes accordingly. 

Because end-user data follows the default CmekConfig, you can't delete a CmekConfig while it still protects end-user data. To delete it, first unset the default Cloud KMS configuration (#unset-default). For more information, see Unregister your Cloud KMS key (#key-unregistration). 

### Rotate Cloud KMS keys

You can't change which key protects an existing app or data connector, but you can rotate that key to a new key version. When you make a new version of a registered key the primary version, Gemini Enterprise detects the change and reencrypts your data with the new key version automatically. You don't need to call a Gemini Enterprise method to start a rotation. 

For general information about rotating keys, see Key rotation (/kms/docs/key-rotation) in the Cloud KMS guide. 

**Important:** Do not rotate keys on apps or data connectors associated with recommendations or with any apps that need analytics, and don't rotate the singleregion keys used for third-party connectors. See Limitations of Cloud KMS in Gemini Enterprise (#limitations). 

To rotate a key, follow these steps: 

1. Create a new key version and make it the primary version. For instructions, see Rotate a key (/kms/docs/rotate-key) in the Cloud KMS guide. 

Leave the previous key version enabled. Re-encryption starts automatically after Gemini Enterprise detects the new primary version. 

2. Confirm that Gemini Enterprise detected the new key version. To view your CmekConfig, see View Cloud KMS keys (#view-key). Check the following fields in the output: 

   - `kmsKeyVersion` shows the new key version. 

   - `state` is `ACTIVE` . 

   - `lastRotationTimestampMicros` shows when the rotation started. 

3. Keep the previous key version enabled for at least 30 days after `kmsKeyVersion` shows the new key version. 

**Caution:** Gemini Enterprise doesn't report when the re-encryption of all underlying storage is complete. If you disable or destroy the previous key version before the reencryption is complete, the data that is still encrypted under that version becomes inaccessible. 

4. Disable the previous key version, and make sure that everything is working as before. See Enable and disable key versions (/kms/docs/enable-disable) in the Cloud KMS guide. 

5. When you are certain that no problems were caused by disabling the previous key version, destroy it. See Destroy and restore key versions (/kms/docs/destroy-restore) in the Cloud KMS guide. 

**Tip:** Destruction is scheduled rather than immediate. While a key version is scheduled for destruction, it behaves as if it were disabled, and you can restore it to cancel the 

### If a Cloud KMS key is disabled or revoked

If a key is disabled (/kms/docs/enable-disable) or permissions for the key are revoked, the app or data connector stops ingesting data and stops serving data within 15 minutes. You may re-enable your key within 30 days to resume operations before the CMEK config expires and any associated data is permanently deleted. However, re-enabling a key or restoring permissions takes a long time. It can take up to 24 hours before the app or data connector can resume serving data. 

Therefore, don't disable a key unless necessary. Disabling and enabling a key on an app or data connector is a time-consuming operation. For example, repeatedly switching a key between disabled and enabled means it will take a long time for the app or data connector to reach a protected state. Disabling a key and reenabling it immediately afterward could result in days of downtime because the key is first disabled from the app or data connector and subsequently re-enabled. 

### Troubleshoot: KMS key projects not found error

**Symptom:** When you try to create an app or data connector using a KMS key, you receive an error similar to the following: 

```
KMS key projects/[...] not found for location: [...] and project number:
[...]
```

**Issue:** This error message can be misleading. It doesn't necessarily mean that the key doesn't exist. Instead, it might indicate that the KMS key hasn't been registered for use with Gemini Enterprise in the specified location. 

**Solution:** To resolve this issue, register your key by following the steps in Register your Cloud KMS key (#key-registration). After the registration is complete, you can create apps or data connectors protected by that key. 

Last updated 2026-10-15 UTC. 



## Turn off Gemini Enterprise

URL: https://docs.cloud.google.com/gemini/enterprise/docs/turn-off-gemini-enterprise

You can turn off Gemini Enterprise by disabling the Discovery Engine API. Disabling the Discovery Engine API has the following effects: 

All Gemini Enterprise and Agent Search resources might be deleted 

Charges might continue to appear for up to a day after disabling the API 

Because Gemini Enterprise and Agent Search are based on the Discovery Engine API, disabling the Discovery Engine API turns off all these products and any code that calls the Discovery Engine API fails. 

To turn off Gemini Enterprise, follow these steps: 

1. In the Google Cloud console, go to the **Discovery Engine API Service Details** (https://console.cloud.google.com/apis/api/discoveryengine.googleapis.com) page. 

2. Click **Disable API** . 

3. In the **Disable Discovery Engine API?** box, click **Disable** . 

Last updated 2026-10-14 UTC. 



## Manage costs: overview

URL: https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview

**Note:** To use this feature, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

In Gemini Enterprise, your subscription entitles your users to specific feature quotas. When your project reaches its pooled quota for a feature, feature usage stops unless you enable overages. 

How overages work depends on your product edition: 

|Product edition|Overages support|
|---|---|
|All Gemini<br>Enterprise editions<br>(Gemini Enterprise<br>Standard, Plus,|Supported. You can enable overages to let users exceed included quotas at<br>pay-as-you-go rates. For more information about how pooled quotas work,<br>see<br>Quotas and overages(/gemini/enterprise/docs/quotas-and-overages).|
|Frontline, EDU, and<br>Emerging Market<br>editions)|Overages and spend controls are available only if your project has an<br>invoiced Cloud Billing account<br>(/billing/docs/concepts#billing_account_types) and at least one active,<br>non-free-trial subscription. To verify your account type, see<br>Find out your<br>Cloud Billing account type and charging cycle<br>(/billing/docs/how-to/billing-cycle#view-your-charging-cycle).|
|Gemini Enterprise<br>Pay-as-you-go|Not applicable. You pay for all usage on a pay-as-you-go basis without<br>pooled quota limits.|

**Note:** Gemini Enterprise Emerging Market editions are available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility. 

For more information, see the following resources: 

- View feature usage (/gemini/enterprise/docs/feature-usage) Configure overages (/gemini/enterprise/docs/configure-overages) 

### Cap costs with a project spend limit

To prevent unexpected charges when you enable overages, you can configure a monthly spend limit on your total spend in Cloud Billing. When defining a budget for your project, you select **Vertex AI (aiplatform.googleapis.com)** as the service scope. This sets a project-level spend cap that applies across all of the following areas: 

- Gemini Enterprise app 

Gemini Enterprise Agent Platform 

AI coding and developer tools (such as Google Antigravity) 

When your project reaches this spend limit, overage usage is automatically stopped. To configure a monthly spend limit for your project, see Set a monthly spend limit (/gemini/enterprise/docs/configure-overages#set-spend-limit). 

**Note:** Because stopping usage can take a few minutes to take effect, you might incur charges that exceed your limit. 

### End-user experience when limits are reached

When your project reaches a usage or spending limit, Gemini Enterprise restricts further usage. Feature access resumes automatically when the quota resets or at the start of the next billing cycle. 

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

Your project reached its monthly spend cap. 

- Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 

This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

### Budget alert notifications

The Gemini Enterprise app doesn't send automated email alerts or push notifications when your project reaches its pooled feature quotas or starts incurring overage charges. When your project reaches a pooled quota and you haven't enabled overages, end users see the **Usage limit reached** error message in the app. 

When you configure a monthly spend limit in Cloud Billing, you can set alert threshold rules to monitor your costs. Cloud Billing automatically sends email notifications when your spend reaches specified percentages of your budget, such as 50%, 80%, and 100% of the budget amount. 

The following principals receive budget alert notifications: 

- **Default recipients:** Cloud Billing sends email alerts to users who have the **Billing Account Administrator** or **Billing Account User** IAM roles on the target billing account. 

- **Custom recipients:** You can configure custom email recipients, such as specific project administrators, team distribution lists, or Pub/Sub channels, in your budget alert rules. 

For more information, see the following resources: 

- Create, edit, or delete budgets and budget alerts (/billing/docs/how-to/budgets) Manage budget alert recipients (/billing/docs/how-to/budgets-notification-recipients) 

- View costs and cost trends (/gemini/enterprise/docs/view-costs) 

Last updated 2026-10-14 UTC. 



## View feature usage

URL: https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage

When you view feature usage in Gemini Enterprise, the usage details depend on your product edition: 

- **Gemini Enterprise Pay-as-you-go:** You see only the usage amount for each feature. 

- **License-based editions (such as Gemini Enterprise Standard, Plus, Frontline, EDU, and Emerging Market editions):** You see pooled quotas based on the number of licenses per subscription. 

### Pooled quotas overview

In Gemini Enterprise, for editions with license-based subscriptions (such as Gemini Enterprise Standard, Plus, Frontline, EDU, and Emerging Market editions), all users in a Google Cloud project share resource quotas. For more information about the quotas for each edition, see Quotas and overages (/gemini/enterprise/docs/quotas-and-overages). To enable overages when your project reaches a pooled quota, see Configure overages (/gemini/enterprise/docs/configure-overages). 

#### Quota reset times

Your subscription entitles you to certain quotas across product features. Except for storage and data indexing, feature quotas are pooled across users in the same edition within a project and location. For more information, see Feature and edition-based quotas (/gemini/enterprise/docs/quotas-and-overages#feature-quotas). 

Pooled quotas reset on the following schedule: 

|Feature|Reset schedule|
|---|---|
|All features except AI developer tools|Daily at midnight Pacific Time (PT)|
|AI developer tools|Every seven days, starting from when a prompt or request is first|
|(/gemini/enterprise/docs/ai-<br>developer-tools-overview)|sent to an AI developer tool.<br>For example, if a user in your project sends the first prompt using<br>Antigravity on Wednesday at 2 PM Pacific Time (PT), the seven-<br>day quota cycle starts at that time, and the AI developer tools<br>quota resets the following Wednesday at 2 PM PT.|

### Pay-as-you-go usage overview

For the Gemini Enterprise Pay-as-you-go edition, Gemini Enterprise does not pool usage based on user licenses. Instead, when you view feature usage in the dashboard, you see the actual usage amount consumed by your project. 

**Note:** To subscribe to the Gemini Enterprise Pay-as-you-go edition, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

### Before you begin

Gemini EnterpriseAgentspace (#agentspace) (#gemini-enterprise) 

You can view the usage dashboard only if the following are true: 

- You're a Gemini Enterprise Administrator 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin). 

You have at least one active Gemini Enterprise subscription 

- (/gemini/enterprise/docs/licenses#about-subscriptions) (such as Gemini Enterprise Standard, Plus, Frontline, EDU, Emerging Market editions, or Pay-as-you-go). 

To view quota usage on the **Usage** tab of the **Usage & Spending** page, you need the following IAM permissions: 

```
monitoring.timeSeries.list
```

Included by default in the Gemini Enterprise Administrator 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) 

- ( `roles/discoveryengine.agentspaceAdmin` ) role. 

Without this permission, quota usage displays as `0` . 

```
serviceconsumermanagement.quota.get
```

Without this permission, the quota limit displays as `Unknown` . 

If you use user roles that don't include these permissions, you must add the required permissions to the role (/iam/docs/creating-custom-roles#edit-role). 

### View the usage dashboard

To view feature usage and quota details in your project, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page. 

Go to Usage & Spending (https://console.cloud.google.com/gemini-enterprise/usage-and-spending) 

2. Select the **location** of the licenses or subscription. 

3. In the **Usage details** section, from the **Subscription tier** list, select the product edition for which you want to view details. 

The dashboard shows the features and usage details for your selected edition: 

- For **Pay-as-you-go** , it displays the usage amount. 

- For Gemini Enterprise editions, such as Standard, Plus, Frontline, EDU, and Emerging Market editions, it displays the absolute and percentage usage of each pooled quota. 

### What's next

- Learn how to confgure overages and spend limitsi (/gemini/enterprise/docs/configure-overages). 

Learn how to view costs (/gemini/enterprise/docs/view-costs). 

Last updated 2026-10-14 UTC. 



## Configure overages

URL: https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages

**Note:** To use this feature, your project must be linked to an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) that receives an active monthly invoice. 

When your project reaches its pooled quota for a feature in Gemini Enterprise, feature usage stops unless you enable overages. Enabling overages lets users in your project continue using features beyond the included pooled quota limits at pay-as-you-go overage rates. 

You can enable overages only if your project has an invoiced Cloud Billing account (/billing/docs/concepts#billing_account_types) and at least one active, non-free-trial subscription, and uses one of the following license-based product editions: 

- Gemini Enterprise Standard 

- Gemini Enterprise Plus 

- Gemini Enterprise Frontline Starter and Frontline Worker 

- Gemini Enterprise EDU and EDU Pro 

- Gemini Enterprise Standard Emerging Market, Emerging Market EDU, Emerging Market governments. Emerging market editions are available only to eligible customers. Your Google account team assesses the requirements to determine your eligibility. 

**Note:** Overages don't apply to the **Gemini Enterprise Pay-as-you-go** edition because you pay for all feature usage on a pay-as-you-go basis. 

To learn how overage pricing works and view the pricing tables for each feature, see Quotas and overages (/gemini/enterprise/docs/quotas-and-overages#overages). 

**Caution:** If you enable overages without setting a monthly spend limit, feature usage continues without restriction after your project exceeds its pooled quota, and you pay for all excess usage at pay-as-you-go overage rates. To prevent unexpected charges, set a monthly spend limit (#set-spend-limit). 

### Before you begin

You can enable overages and set spend limits if you meet the following requirements: 

- You are a Gemini Enterprise Administrator 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin). 

- You have at least one active, non-free-trial Gemini Enterprise subscription (/gemini/enterprise/docs/licenses#about-subscriptions) for a license-based edition (such as Gemini Enterprise Standard, Plus, Frontline, EDU, or Emerging Market editions). 

- Your project has an invoiced Cloud Billing account 

- (/billing/docs/concepts#billing_account_types). To check your billing account type, see Find out your Cloud Billing account type and charging cycle 

- (/billing/docs/how-to/billing-cycle#view-your-charging-cycle). 

### Enable overages

To enable overages for your project, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page. 

Go to Usage & Spending (https://console.cloud.google.com/gemini-enterprise/usage-and-spending) 

2. Select the **Usage** tab. 

3. In the tier selector banner, select the edition you want to configure from the **Choose another tier** drop-down menu. Each edition must be configured separately. 

4. Under **Feature usage** > **Pay-as-you-go usage above quota** , turn the toggle to **Enabled** . 

5. Click **Save changes** . 

6. In the **Pay-as-you-go usage above quota enabled** dialog, click **Got it** . 

### Set a monthly spend limit

You can set a monthly spend limit on overages and the Pay-as-you-go edition usage for your project. When your project reaches this limit, Gemini Enterprise automatically stops overage usage to prevent unexpected charges. 

**Note:** Because stopping usage can take a few minutes to take effect, you might incur charges that exceed your limit. 

The budget you set applies to the following product areas: 

- Gemini Enterprise app 

Gemini Enterprise Agent Platform 

AI coding tools such as Google Antigravity 

To configure a monthly spend limit, do the following: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page. 

Go to Usage & Spending (https://console.cloud.google.com/gemini-enterprise/usage-and-spending) 

2. Select the **Usage** tab. 

3. In the **Project monthly spend limit** section, click **Set limit** . 

4. In Cloud Billing, configure your budget and spend cap actions. When defining the scope of your budget, select **Vertex AI (aiplatform.googleapis.com)** from the **Services** list. Cloud Billing bills overages for Gemini Enterprise and AI developer tools under Vertex AI API. 

For more information about creating budgets and configuring spend limits, see Set budget spend caps (/billing/docs/how-to/budgets-spend-caps). 

### Turn off overages

When you turn off overages, feature usage stops after your project reaches its pooled quota limits. 

Because overages are configured per edition, you turn off overages individually for each edition where you previously enabled them. 

To turn off overages for an edition, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page. 

Go to Usage & Spending (https://console.cloud.google.com/gemini-enterprise/usage-and-spending) 

2. Select the **Usage** tab. 

3. In the tier selector banner, select the edition you want to configure from the **Choose another tier** drop-down menu. Each edition must be configured separately. 

4. Under **Feature usage** > **Pay-as-you-go usage above quota** , turn the toggle to **Disabled** . 

5. Click **Save changes** . 

6. In the **Disable pay-as-you-go usage above quota?** dialog, click **Disable** . 

### What's next

- Learn how to view feature usage (/gemini/enterprise/docs/feature-usage). 

- Learn how to view costs (/gemini/enterprise/docs/view-costs). 

Last updated 2026-10-14 UTC. 



## View costs

URL: https://docs.cloud.google.com/gemini/enterprise/docs/view-costs

In Gemini Enterprise, the **Billing** tab on the **Usage & Spending** page displays a summary of your overage and Pay-as-you-go usage costs over the last 30 days across your enabled features and tools. 

**Note:** The **Usage & Spending** page displays overages and Pay-as-you-go edition usage costs. It doesn't include license-based Gemini Enterprise subscription costs. 

The **Billing** tab displays total overage and Pay-as-you-go usage costs that include charges for: 

- Gemini Enterprise app 

- Gemini Enterprise Agent Platform 

- AI developer tools (such as Google Antigravity) 

### Before you begin

To view cost details on the **Usage & Spending** page, you need the following IAM roles and permissions: 

**Required roles** : 

- Gemini Enterprise Administrator 

- (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) 

- ( `roles/discoveryengine.agentspaceAdmin` ) on the project 

- Billing Account Viewer (/iam/docs/roles-permissions/billing#billing.viewer) 

- ( `roles/billing.viewer` ) or Billing Account Administrator 

- (/iam/docs/roles-permissions/billing#billing.admin) ( `roles/billing.admin` ) on the target billing account 

**Required permissions** : 

- `monitoring.timeSeries.list` (included by default in the Gemini Enterprise 

- Administrator (/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role) 

```
serviceconsumermanagement.quota.get
```

Without these permissions, the **Billing** tab isn't visible. If you use custom roles that don't include these permissions, you must add the required permissions to the role (/iam/docs/creating-custom-roles#edit-role). 

### View costs and cost trends

To view your project's overages and Pay-as-you-go edition usage costs, follow these steps: 

1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page. 

Go to Usage & Spending (https://console.cloud.google.com/gemini-enterprise/usage-and-spending) 

2. Select the **Billing** tab. 

The **Gemini Enterprise costs (Last 30 days)** section displays the following cost breakdown: 

|Cost item|Description|
|---|---|
|Gemini Enterprise app|Charges for Gemini Enterprise feature usages.|
|Gemini Enterprise Agent<br>Platform|Charges for building and deploying AI models and agents.|
|AI developer tools (such as<br>Antigravity)|Charges for AI coding and developer tool usage, including Antigravity.|
|Total cost|The combined sum of these overage and Pay-as-you-go usage costs,<br>along with a 30-day cost trend chart.|

3. To inspect detailed cost breakdowns, invoices, or reports in the Cloud Billing console, click **View details in Billing** . 

For more information on billing reports and cost analysis in Cloud Billing, see View your billing reports and cost trends (/billing/docs/how-to/reports/gemini-enterprise-costs). 

### What's next

Learn how to view feature usage (/gemini/enterprise/docs/feature-usage). 

- Learn how to confgure overages and spend limitsi (/gemini/enterprise/docs/configure-overages). 

Last updated 2026-10-14 UTC.
