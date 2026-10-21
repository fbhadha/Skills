# Canada Protected B, Assured Workloads and access controls / Restrict resource locations
Source: 05-Canada-Protected-B-Assured-Workloads-and-access-controls.pdf, pages 390-421, extracted 2026-10-18

## Restrict resource locations

URL: https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations

**Important:** The information on this page does _not_ describe Google Cloud Platform's data location commitments for Customer Data (as defined in the agreement under which Google has agreed to provide Google Cloud Platform services and as described in the Google Cloud Platform Services Summary (https://cloud.google.com/terms/services)) to its customers. For the list of Google Cloud Platform services for which Customer Data location may be selected by customers, see Google Cloud Platform Services with Data Residency 

(https://cloud.google.com/terms/data-residency). 

### Overview

This guide describes how to set an organization policy (/organization-policy/overview) that includes the resource locations constraint. 

You can limit the physical location of a new resource with the Organization Policy Service resource locations constraint. You can use the location property of a resource to identify where it is deployed and maintained by the service. For datacontaining resources of some Google Cloud services, this property also reflects the location where data is stored. This constraint lets you define the allowed Google Cloud locations where the resources for supported services in your hierarchy can be created. 

After you define resource locations, this limitation will apply only to newly-created resources. Resources you created before setting the resource locations constraint will continue to exist and perform their function. 

A policy that includes this constraint won't be enforced on sub-resource creation for certain services, such as Cloud Storage and Managed Service for Apache Spark. 

**Warning:** An organization policy that includes this constraint will prevent services from creating new resources that violate the constraint, which can stop those services from working correctly. Some services interact with and implement the resource location constraint in different ways. For details and examples of these special cases, see the 

Services that support restricting resource locations 

(/organization-policy/reference/restrict-locations-supported-services) page. 

### Limitations

The resource locations Organization Policy Service constraint controls the ability to create resources for which a location can be selected. This constraint does not affect where global resources, such as Compute Engine global addresses, or resources that don't support selecting a location are created. 

To avoid breaking existing serving infrastructure, you should test any new policy on non-production projects and folders, then apply the policy gradually within your organization. 

**Note:** The resource locations constraint controls only where resources are created. Some Google Cloud services might not store or process data contained by a resource in the same location where that resource was created. 

For data storage commitments, see the Google Cloud Terms of Service (https://cloud.google.com/terms) and the Service Specific Terms (https://cloud.google.com/terms/service-terms). Organization policies that contain the resource locations constraint aren't data storage commitments. 

This constraint applies to a specific subset of products and resource types. For a list of supported services and details on the behavior of each service, see the Services that support restricting resource locations 

(/organization-policy/reference/restrict-locations-supported-services) page. 

### Location types

You can deploy Google Cloud resources in location (https://cloud.google.com/about/locations) types that represent different size categories. The largest location type is the `multi-region` , which includes more than one `region` . Each `region` is further subdivided into `zones` . For more information 

about regions and zones, see the Regions and Zones overview (/compute/docs/regions-zones). 

- `Multi-region` locations are backed by physical resources in more than one `region` and are typically only used by storage-based resources. Some examples include `us` , `asia` , `europe` , and `global` . 

- `Region` locations are geographically isolated from each other. Some examples include `us-west1` (Oregon), `asia-northeast1` (Tokyo), and `europe-west1` (Belgium). 

- `Zone` locations are the most granular and isolated location type used for deploying resources. A `zone` is an independent failure domain within a `region` . Some examples are `us-east1-b` , `us-west1-b` , and `asia-northeast1-a` . Google Cloud also offers specialized AI zones (/compute/docs/regions-zones/ai-zones) that are tailored for AI and ML workloads—for example, `us-central1-ai1a` . 

When setting up locations, you should use the `in:` prefix and a Value Group (#value_groups). Using a Value Group curated by Google Cloud lets you choose geographic location(s), without having to specify current or future Cloud locations. 

The `in:` prefix to a Value Group specifies that all values that exist within the value group are considered to be part of the policy. If you enter a group value or a Google Cloud region without the prefix, the `in:` prefix will be automatically added, per these rules: 

- If you enter a location that uses the `in:` prefix, and it contains any invalid group, the policy change will fail. 

- If you enter a location that is a region, such as `us-east1` , it will have the `in:` prefix prepended, to `in:us-east1-locations` in this example. 

- If you enter a region or multi-region value group such as `us-locations` , it will have the `in:` prefix prepended, to `in:us-locations` in this example. 

- If you enter a zone or multi-region such as `us-east1-b` or `us` , the values won't be changed. 

### Setting the organization policy

The resource locations constraint is a type of legacy managed constraint with list rules (/organization-policy/create-organization-policies#list-constraint). You can add and remove locations from the `allowed_values` or `denied_values` lists of a resource locations constraint. To prevent organization policies from unexpectedly restricting service behavior as new locations are added to the available list, use a value group (#value_groups), or a list of `allowed_values` that represents the entire geographic boundary you want to define. 

To set an organization policy (/resource-manager/reference/rest/v1/Policy) including a resource locations constraint: 

Consolegcloud (#gcloud)API (#api) (#console) 

1. In the Google Cloud console, go to the **Organization policies** page. 

Go to Organization policies (https://console.cloud.google.com/iam-admin/orgpolicies) 

2. From the project picker, select the organization, folder, or project for which you want to set the organization policy. 

3. Select the **Google Cloud Platform - Resource Location Restriction** constraint to open its **Policy details** page. 

4. Click **Manage policy** . 

5. On the **Edit policy** page, select **Override parent's policy** . 

6. Under **Policy enforcement** , select **Replace** . 

7. Click **Add rule** . 

8. Under **Policy values** , select **Custom** . 

9. Under **Policy type** , select **Allow** to create a list of allowed locations, or select **Deny** to create a list of denied locations. 

10. In the **Policy value** box, enter the `in` prefix and a value group (#value_groups) location string, then press **Enter** . 

For example, `in:us-locations` or `in:us-west1-locations` . You can enter multiple location strings by clicking **Add value** . 

You can also enter specific zone, region, or multi-region locations as location strings. For a list of available locations, see the Services that support restricting resource locations 

(/organization-policy/reference/restrict-locations-supported-services) page. 

11. To enforce the policy, click **Set policy** . 

To learn about using constraints in organization policies, see Create organization policies (/organization-policy/create-organization-policies#list-constraint). 

#### Using inheritance in organization policy

You can refine your organization policy to inherit the organization policy from the resource's parent nodes. Inheritance (/organization-policy/hierarchy-evaluation) gives you granular control over the organization policies used throughout your resource hierarchy. 

To enable inheritance on a resource node, set `inheritFromParent = true` in the organization policy YAML file. For example: 

```
name: organizations/01234567890/policies/gcp.resourceLocations
spec:
 inheritFromParent: true
 rules:
 - values:
     deniedValues:
     - in:us-west1
```

### Allow or deny VM creation in AI zones

You can allow or deny VMs from being created in AI zones by creating and enforcing a custom constraint in a custom organization policy. 

An AI zone is identified with the string `ai` in its name. For example, `us-west4-ai2b` is an AI zone in the `us-west4` region, and `us-west4-b` is the parent zone. When 

creating a custom constraint, use the string `-ai` in your condition. For more information about AI zones, see About AI zones (/compute/docs/regions-zones/ai-zones). 

**Note:** Conditions can only evaluate individual values, as custom organization policy doesn't support value groups (#value_groups). The custom constraint described in this section applies only to VMs and not to other resources, such as disks. 

For permissions required to manage organization policies, see Required roles (/organization-policy/create-custom-constraints#required-roles) in the _Creating and managing custom constraints_ page. 

To set a custom organization policy to allow or deny VMs from being created in AI zones, complete the following steps: 

1. **Create a custom constraint for AI zones** 

Depending on whether you want to allow or deny VMs from being created in AI zones, create a YAML file with one of the following constraints. 

To allow VMs to be created in AI zones only, use the following constraint: 

```
name:
organizations/ORGANIZATION_ID/customConstraints/custom.allowOnlyAiZone
s
resource_types:
- compute.googleapis.com/Instance
method_types:
- CREATE
- UPDATE
actionType: ALLOW
condition: "resource.zone.contains('-ai')"
displayName: allowOnlyAiZones
description: Allow VMs to be created in AI zones only.
```

To deny VMs from being created in AI zones, use the following constraint: 

```
name:
organizations/ORGANIZATION_ID/customConstraints/custom.denyAiZones
resource_types:
- compute.googleapis.com/Instance
method_types:
- CREATE
- UPDATE
actionType: DENY
condition: "resource.zone.contains('-ai')"
displayName: denyAiZones
description: Deny VMs from being created in AI zones.
```

Replace _`ORGANIZATION_ID`_ 

(/organization-policy/restrict-domains#retrieving_customer_id) with your organization ID—for example, `01234567890` . 

2. **Set the custom constraint** 

After you've created the YAML file for the custom constraint, you must set the custom constraint to make it available for organization policies. 

To set the custom constraint, use the `gcloud org-policies set-customconstraint` command: 

```
gcloud org-policies set-custom-constraint CONSTRAINT_PATH
```

Replace _`CONSTRAINT_PATH`_ with the full path to your custom constraint YAML file —for example, `/home/user/customconstraint.yaml` . 

3. **Create an organization policy** 

To create an organization policy that enforces the custom constraint, create a policy YAML file that references the constraint: 

```
name: projects/PROJECT_ID/policies/CONSTRAINT_NAME
spec:
 rules:
```

- `enforce: true` 

Replace the following: 

- _`PROJECT_ID`_ : the project that you want to enforce your constraint on. 

- _`CONSTRAINT_NAME`_ : the name of your custom constraint 

- `custom.allowOnlyAiZones` or `custom.denyAiZones` . 

4. **Enforce the custom organization policy on your project** 

To enforce the organization policy containing the custom constraint, run the following command: 

```
gcloud org-policies set-policy POLICY_PATH
```

Replace _`POLICY_PATH`_ with the full path to your organization policy YAML file. Changes to organization policies can take up to 15 minutes to be fully enforced. 

For more information about custom constraints, see Create custom constraints (/organization-policy/create-custom-constraints). For troubleshooting, see Troubleshooting custom constraints 

- (/organization-policy/create-custom-constraints#troubleshooting_constraints). 

### Example error message

Services that support the resource location constraint are prevented from creating new resources in locations that would violate the constraint. If a service attempts to create a resource in a location that violates the constraint, the attempt will fail and an error message will be generated. 

This error message will have this format: _`LOCATION_IN_REQUEST`_ `violates constraint constraints/gcp.resourceLocations on the resource` _`RESOURCE_TESTED`_ `.` 

In the following example, a Compute Engine resource fails to create a new instance (/compute/docs/instances) due to policy enforcement: 

```
Location ZONE:us-east1-b violates constraint constraints/gcp.resourceLocations
on the resource
projects/policy-violation-test/zones/us-east1-b/instances/instance-3.
```

Google Cloud Observability and Cloud Audit Logs log entry: 

```
{
insertId: "5u759gdngec"
logName: "projects/policy-violation-
test/logs/cloudaudit.googleapis.com%2Factivity"
protoPayload: {
 @type: "type.googleapis.com/google.cloud.audit.AuditLog"
 authenticationInfo: {…}
 authorizationInfo: [6]
 methodName: "beta.compute.instances.insert"
 request: {…}
 requestMetadata: {…}
 resourceLocation: {…}
 resourceName: "projects/policy-violation-test/zones/us-east1-
b/instances/instance-3"
 response: {
  @type: "type.googleapis.com/error"
  error: {
   code: 412
   errors: [
    0: {
     domain: "global"
     location: "If-Match"
     locationType: "header"
     message: "Location ZONE:us-east1-b violates constraint
constraints/gcp.resourceLocations on the resource projects/policy-violation-
test/zones/us-east1-b/instances/instance-3."
     reason: "conditionNotMet"
    }
   ]
   message: "Location ZONE:us-east1-b violates constraint
constraints/gcp.resourceLocations on the resource projects/policy-violation-
test/zones/us-east1-b/instances/instance-3."
  }
 }
 serviceName: "compute.googleapis.com"
 status: {
  code: 3
  message: "INVALID_ARGUMENT"
 }
}
receiveTimestamp: "2019-06-14T03:04:23.660988360Z"
resource: {
 labels: {…}
 type: "gce_instance"
}
severity: "ERROR"
timestamp: "2019-06-14T03:04:22.783Z"
}
```

### Vulnerability findings and remediation

The resource location constraint restricts the creation of resources at runtime. This feature helps to prevent location violations from occurring, but does not identify or remediate existing violations. You can use Security Health Analytics, a built-in service of Security Command Center, to discover location violations in your resource hierarchy. For more information, see Organization Policy vulnerability findings (/security-command-center/docs/concepts-vulnerabilities-findings#org-findings). 

If there are Security Health Analytics findings of location violations, see Remediating Security Health Analytics findings 

(/security-command-center/docs/how-to-remediate-security-health-analyticsfindings#org_policy_location_restriction) 

for steps to remediate those findings. 

### Value groups

Value groups are collections of groups and locations that are curated by Google to provide a simple way to define your resource locations. Value groups include many related locations and are expanded over time by Google without needing to change your organization policy to accommodate the new locations. 

To use value groups in your organization policy, prefix your entries with the string `in:` . For more information on using value prefixes, see Create organization policies (/organization-policy/create-organization-policies#hierarchy_subtree). Group names are validated on the call to set the organization policy. Using an invalid group name will cause the policy setting to fail. 

**Note:** The **`global`** location is considered a multi-region (/organization-policy/restrict-locations#location_types). Its datacenters are spread throughout the world. It is not possible to predict or control exactly which datacenters are selected or where they are located. Depending on the service, there is a distinction between "US" and "us","EU" and "eu". For the list of services and the corresponding values, see the multi-regional locations (https://cloud.google.com/about/locations#multi-region). 

The following table contains the current list of available groups: 

|Group|Details|Direct members|
|---|---|---|
|Johannesburg|All locations within|_Values:_|
||Johannesburg:<br>`in:africa-south1-locations`|`africa-south1`|
|||`africa-south1-a`|
|||`africa-south1-b`|
|||`africa-south1-c`|

|Group|Details|Direct members|
|---|---|---|
|Asia|All locations within Asia:<br>`in:asia-locations`|_Groups:_<br>`asia-east2-locations`<br>`id-locations`|
|||`il-locations`<br>`in-locations`|
|||`jp-locations`|
|||`kr-locations`|
|||`me-central1-locations`|
|||`sa-locations`|
|||`sg-locations`|
|||`tw-locations`|
|||_Values:_|
|||`asia`|
|||`asia1`|
|||`aws-ap-northeast-2`|
|Hong Kong|All locations within Hong Kong:<br>`in:asia-east2-locations`|_Values:_<br>`asia-east2`|
|||`asia-east2-a`|
|||`asia-east2-b`|
|||`asia-east2-c`|
|Indonesia|All locations within Indonesia:<br>`in:id-locations`|_Groups:_<br>`asia-southeast2-`<br>`locations`|
|||_Values:_<br>`id`|

|Group|Details|Direct members|
|---|---|---|
|Jakarta|All locations within Jakarta:<br>`in:asia-southeast2-`<br>`locations`|_Values:_<br>`asia-southeast2`<br>`asia-southeast2-a`<br>`asia-southeast2-b`<br>`asia-southeast2-c`|
|Israel|All locations within Israel:<br>`in:il-locations`|_Groups:_<br>`me-west1-locations`|
|||_Values:_|
|||`il`|
|Israel|All locations within Israel:<br>`in:me-west1-locations`|_Values:_<br>`me-west1`<br>`me-west1-a`|
|||`me-west1-b`|
|||`me-west1-c`|
|India|All locations within India:<br>`in:in-locations`|_Groups:_<br>`asia-south1-locations`<br>`asia-south2-locations`|
|||_Values:_<br>`in`|
|Mumbai|All locations within Mumbai:<br>`in:asia-south1-locations`|_Values:_<br>`asia-south1`<br>`asia-south1-a`<br>`asia-south1-b`<br>`asia-south1-c`|

|Group|Details|Direct members|
|---|---|---|
|Delhi|All locations within Delhi:<br>`in:asia-south2-locations`|_Values:_<br>`asia-south2`<br>`asia-south2-a`<br>`asia-south2-b`<br>`asia-south2-c`|
|Japan|All locations within Japan:<br>`in:jp-locations`|_Groups:_<br>`asia-northeast1-`<br>`locations`<br>`asia-northeast2-`<br>`locations`|
|||_Values:_|
|||`jp`|
|Tokyo|All locations within Tokyo:<br>`in:asia-northeast1-`<br>`locations`|_Values:_<br>`asia-northeast1`<br>`asia-northeast1-a`|
|||`asia-northeast1-b`|
|||`asia-northeast1-c`|
|Osaka|All locations within Osaka:<br>`in:asia-northeast2-`<br>`locations`|_Values:_<br>`asia-northeast2`<br>`asia-northeast2-a`|
|||`asia-northeast2-b`<br>`asia-northeast2-c`|

|Group|Details|Direct members|
|---|---|---|
|South Korea|All locations within South<br>Korea:<br>`in:kr-locations`|_Groups:_<br>`asia-northeast3-`<br>`locations`|
|||_Values:_<br>`kr`|
|Seoul|All locations within Seoul:<br>`in:asia-northeast3-`<br>`locations`|_Values:_<br>`asia-northeast3`<br>`asia-northeast3-a`<br>`asia-northeast3-b`<br>`asia-northeast3-c`|
|Doha|All locations within Doha:<br>`in:me-central1-locations`|_Values:_<br>`me-central1`<br>`me-central1-a`<br>`me-central1-b`|
|||`me-central1-c`|
|Saudi Arabia|All locations within Saudi<br>Arabia:<br>`in:sa-locations`|_Groups:_<br>`me-central2-locations`|
|||_Values:_<br>`sa`|
|Dammam|All locations within Dammam:<br>`in:me-central2-locations`|_Values:_<br>`me-central2`<br>`me-central2-a`<br>`me-central2-b`<br>`me-central2-c`|

|Group|Details|Direct members|
|---|---|---|
|Singapore|All locations within Singapore:<br>`in:sg-locations`|_Groups:_<br>`asia-southeast1-`<br>`locations`|
|||_Values:_|
|||`sg`|
|Singapore|All locations within Singapore:<br>`in:asia-southeast1-`<br>`locations`|_Values:_<br>`asia-southeast1`<br>`asia-southeast1-a`<br>`asia-southeast1-b`<br>`asia-southeast1-c`|
|Taiwan|All locations within Taiwan:<br>`in:tw-locations`|_Groups:_<br>`asia-east1-locations`|
|||_Values:_<br>`tw`|
|Taiwan|All locations within Taiwan:<br>`in:asia-east1-locations`|_Values:_<br>`asia-east1`<br>`asia-east1-a`<br>`asia-east1-b`<br>`asia-east1-c`|

|Group|Details|Direct members|
|---|---|---|
|Australia|All locations within Australia:<br>`in:australia-locations`|_Groups:_<br>`australia-southeast1-`<br>`locations`<br>`australia-southeast2-`<br>`locations`|
|||_Values:_|
|||`au`|
|Sydney|All locations within Sydney:<br>`in:australia-southeast1-`<br>`locations`|_Values:_<br>`australia-southeast1`<br>`australia-southeast1-a`|
|||`australia-southeast1-b`<br>`australia-southeast1-c`|
|Melbourne|All locations within Melbourne:<br>`in:australia-southeast2-`<br>`locations`|_Values:_<br>`australia-southeast2`<br>`australia-southeast2-a`|
|||`australia-southeast2-b`|
|||`australia-southeast2-c`|
|AWS|All AWS locations:<br>`in:aws-locations`|_Values:_<br>`aws-ap-northeast-2`<br>`aws-ap-southeast-2`<br>`aws-eu-central-1`<br>`aws-us-east-1`|
|Azure|All Azure locations:<br>`in:azure-locations`|_Values:_<br>`azure-eastus2`<br>`azure-westus2`|

|Group|Details|Direct members|
|---|---|---|
|European Union|All locations within European<br>Union:<br>`in:eu-locations`|_Groups:_<br>`de-locations`<br>`europe-central2-`<br>`locations`|
|||`europe-north1-locations`|
|||`europe-north2-locations`|
|||`europe-southwest1-`<br>`locations`|
|||`europe-west1-locations`|
|||`europe-west4-locations`|
|||`europe-west9-locations`|
|||`it-locations`|
|||_Values:_|
|||`EU`|
|||`eu`|
|||`eur3`|
|||`eur4`|
|||`eur8`|
|||`europe-west`|
|Germany|All locations within Germany:<br>`in:de-locations`|_Groups:_<br>`europe-west10-locations`|
|||`europe-west3-locations`|
|||_Values:_<br>`de`|

|Group|Details|Direct members|
|---|---|---|
|Berlin|All locations within Berlin:<br>`in:europe-west10-locations`|_Values:_<br>`europe-west10`<br>`europe-west10-a`<br>`europe-west10-b`<br>`europe-west10-c`|
|Frankfurt|All locations within Frankfurt:<br>`in:europe-west3-locations`|_Values:_<br>`europe-west3`<br>`europe-west3-a`<br>`europe-west3-b`|
|||`europe-west3-c`|
|Warsaw|All locations within Warsaw:<br>`in:europe-central2-`<br>`locations`|_Values:_<br>`europe-central2`<br>`europe-central2-a`|
|||`europe-central2-b`<br>`europe-central2-c`|
|Finland|All locations within Finland:<br>`in:europe-north1-locations`|_Values:_<br>`europe-north1`<br>`europe-north1-a`<br>`europe-north1-b`|
|||`europe-north1-c`|
|Stockholm|All locations within Stockholm:<br>`in:europe-north2-locations`|_Values:_<br>`europe-north2`<br>`europe-north2-a`<br>`europe-north2-b`|
|||`europe-north2-c`|

|Group|Details|Direct members|
|---|---|---|
|Madrid|All locations within Madrid:<br>`in:europe-southwest1-`<br>`locations`|_Values:_<br>`europe-southwest1`<br>`europe-southwest1-a`<br>`europe-southwest1-b`<br>`europe-southwest1-c`|
|Belgium|All locations within Belgium:<br>`in:europe-west1-locations`|_Values:_<br>`europe-west1`<br>`europe-west1-b`<br>`europe-west1-c`<br>`europe-west1-d`|
|Netherlands|All locations within<br>Netherlands:<br>`in:europe-west4-locations`|_Values:_<br>`europe-west4`<br>`europe-west4-a`<br>`europe-west4-b`<br>`europe-west4-c`|
|Paris|All locations within Paris:<br>`in:europe-west9-locations`|_Values:_<br>`europe-west9`<br>`europe-west9-a`<br>`europe-west9-b`<br>`europe-west9-c`|
|Italy|All locations within Italy:<br>`in:it-locations`|_Groups:_<br>`europe-west12-locations`<br>`europe-west8-locations`|
|||_Values:_<br>`it`|

|Group|Details|Direct members|
|---|---|---|
|Turin|All locations within Turin:<br>`in:europe-west12-locations`|_Values:_<br>`europe-west12`|
|||`europe-west12-a`|
|||`europe-west12-b`<br>`europe-west12-c`|
|Milan|All locations within Milan:<br>`in:europe-west8-locations`|_Values:_<br>`europe-west8`|
|||`europe-west8-a`|
|||`europe-west8-b`|
|||`europe-west8-c`|

|Group|Details|Direct members|
|---|---|---|
|Europe|All locations within Europe:<br>`in:europe-locations`|_Groups:_<br>`ch-locations`|
|||`de-locations`|
|||`europe-central2-`<br>`locations`|
|||`europe-north1-locations`|
|||`europe-north2-locations`|
|||`europe-southwest1-`<br>`locations`|
|||`europe-west1-locations`|
|||`europe-west4-locations`|
|||`europe-west9-locations`|
|||`gb-locations`|
|||`it-locations`|
|||_Values:_|
|||`EU`|
|||`eu`|
|||`eur3`|
|||`eur4`|
|||`eur5`|
|||`eur7`|
|||`eur8`|
|||`europe`|
|||`europe-west`|

|Group|Details|Direct members|
|---|---|---|
|Switzerland|All locations within Switzerland<br>`in:ch-locations`|:<br>_Groups:_<br>`europe-west6-locations`|
|||_Values:_<br>`ch`|
|Zurich|All locations within Zurich:<br>`in:europe-west6-locations`|_Values:_<br>`europe-west6`<br>`europe-west6-a`<br>`europe-west6-b`<br>`europe-west6-c`|
|United Kingdom|All locations within United<br>Kingdom:<br>`in:gb-locations`|_Groups:_<br>`europe-west2-locations`|
|||_Values:_<br>`gb`|
|London|All locations within London:<br>`in:europe-west2-locations`|_Values:_<br>`europe-west2`<br>`europe-west2-a`<br>`europe-west2-b`<br>`europe-west2-c`|

|Group|Details|Direct members|
|---|---|---|
|Low carbon locations|All locations with low carbon<br>impact:<br>`in:low-carbon-locations`|_Groups:_<br>`canada-low-carbon-`<br>`locations`<br>`eu-low-carbon-locations`<br>`europe-low-carbon-`<br>`locations`<br>`northamerica-low-carbon-`<br>`locations`<br>`southamerica-low-carbon-`<br>`locations`<br>`us-low-carbon-locations`|
|Low carbon Canada|All locations within Canada wit<br>low carbon impact:<br>`in:canada-low-carbon-`<br>`locations`|h<br>_Groups:_<br>`northamerica-northeast1-`<br>`locations`<br>`northamerica-northeast2-`<br>`locations`|
|Montréal|All locations within Montréal:<br>`in:northamerica-`<br>`northeast1-locations`|_Values:_<br>`northamerica-northeast1`<br>`northamerica-northeast1-`<br>`a`<br>`northamerica-northeast1-`<br>`b`<br>`northamerica-northeast1-`<br>`c`|

|Group|Details|Direct members|
|---|---|---|
|Toronto|All locations within Toronto:<br>`in:northamerica-`<br>`northeast2-locations`|_Values:_<br>`northamerica-northeast2`<br>`northamerica-northeast2-`<br>`a`<br>`northamerica-northeast2-`<br>`b`<br>`northamerica-northeast2-`<br>`c`|
|Low carbon European Union|All locations within European<br>Union with low carbon impact:<br>`in:eu-low-carbon-locations`|_Groups:_<br>`europe-north1-locations`<br>`europe-southwest1-`<br>`locations`<br>`europe-west1-locations`<br>`europe-west9-locations`|
|Low carbon Europe|All locations within Europe with<br>low carbon impact:<br>`in:europe-low-carbon-`<br>`locations`|_Groups:_<br>`europe-north1-locations`<br>`europe-southwest1-`<br>`locations`|
|||`europe-west1-locations`<br>`europe-west6-locations`<br>`europe-west9-locations`|
|Low carbon North America|All locations within North<br>America with low carbon<br>impact:<br>`in:northamerica-low-`<br>`carbon-locations`|_Groups:_<br>`northamerica-northeast1-`<br>`locations`<br>`northamerica-northeast2-`<br>`locations`|
|||`us-central1-locations`<br>`us-west1-locations`|

|Group|Details|Direct members|
|---|---|---|
|Iowa|All locations within Iowa:<br>`in:us-central1-locations`|_Values:_<br>`us-central1`<br>`us-central1-a`<br>`us-central1-b`<br>`us-central1-c`<br>`us-central1-f`|
|Oregon|All locations within Oregon:<br>`in:us-west1-locations`|_Values:_<br>`us-west1`|
|||`us-west1-a`<br>`us-west1-b`<br>`us-west1-c`|
|Low carbon South America|All locations within South<br>America with low carbon<br>impact:<br>`in:southamerica-low-`<br>`carbon-locations`|_Groups:_<br>`southamerica-east1-`<br>`locations`|
|São Paulo|All locations within São Paulo:<br>`in:southamerica-east1-`<br>`locations`|_Values:_<br>`southamerica-east1`<br>`southamerica-east1-a`<br>`southamerica-east1-b`<br>`southamerica-east1-c`|
|Low carbon United States|All locations within United<br>States with low carbon impact:<br>`in:us-low-carbon-locations`|_Groups:_<br>`us-central1-locations`<br>`us-west1-locations`|

|Group|Details|Direct members|
|---|---|---|
|North America|All locations within North<br>America:<br>`in:northamerica-locations`|_Groups:_<br>`canada-locations`<br>`northamerica-south1-`<br>`locations`<br>`us-locations`|
|||_Values:_|
|||`nam14`|
|Canada|All locations within Canada.<br>`in:canada-locations`|_Groups:_<br>`northamerica-northeast1-`<br>`locations`<br>`northamerica-northeast2-`<br>`locations`|
|||_Values:_|
|||`ca`|
|Mexico|All locations within Mexico:<br>`in:northamerica-south1-`<br>`locations`|_Values:_<br>`northamerica-south1`<br>`northamerica-south1-a`<br>`northamerica-south1-b`<br>`northamerica-south1-c`|

|Group|Details|Direct members|
|---|---|---|
|United States|All locations within the United<br>States:<br>`in:us-locations`|_Groups:_<br>`us-central1-locations`<br>`us-central2-locations`<br>`us-east1-locations`|
|||`us-east4-locations`|
|||`us-east5-locations`<br>`us-south1-locations`|
|||`us-west1-locations`|
|||`us-west2-locations`|
|||`us-west3-locations`|
|||`us-west4-locations`|
|||_Values:_|
|||`US`|
|||`aws-us-east-1`|
|||`azure-eastus2`|
|||`nam10`|
|||`nam11`|
|||`nam12`|
|||`nam13`|
|||`nam15`|
|||`nam3`|
|||`nam4`|
|||`nam5`|
|||`nam6`|
|||`nam7`<br>`nam8`|

|Group|Details|Direct members|
|---|---|---|
|||`nam9`<br>`us`<br>`us-central`|
|Oklahoma|All locations within Oklahoma:<br>`in:us-central2-locations`|_Values:_<br>`us-central2`|
|||`us-central2-a`|
|||`us-central2-b`|
|||`us-central2-c`|
|||`us-central2-d`|
|South Carolina|All zones within South Carolina<br>|:<br>_Values:_|
||`in:us-east1-locations`|`us-east1`|
|||`us-east1-a`|
|||`us-east1-b`|
|||`us-east1-c`|
|||`us-east1-d`|
|Northern Virginia|All locations within Northern<br>Virginia:<br>`in:us-east4-locations`|_Values:_<br>`us-east4`|
|||`us-east4-a`|
|||`us-east4-b`|
|||`us-east4-c`|
|Columbus|All locations within Columbus:<br>`in:us-east5-locations`|_Values:_<br>`us-east5`|
|||`us-east5-a`|
|||`us-east5-b`|
|||`us-east5-c`|

|Group|Details|Direct members|
|---|---|---|
|Dallas|All locations within Dallas:<br>`in:us-south1-locations`|_Values:_<br>`us-south1`<br>`us-south1-a`<br>`us-south1-b`|
|||`us-south1-c`|
|Los Angeles|All locations within Los<br>Angeles:<br>`in:us-west2-locations`|_Values:_<br>`us-west2`<br>`us-west2-a`<br>`us-west2-b`<br>`us-west2-c`|
|Salt Lake City|All locations within Salt Lake<br>City:<br>`in:us-west3-locations`|_Values:_<br>`us-west3`<br>`us-west3-a`<br>`us-west3-b`<br>`us-west3-c`|
|Las Vegas|All locations within Las Vegas:<br>`in:us-west4-locations`|_Values:_<br>`us-west4`<br>`us-west4-a`<br>`us-west4-b`<br>`us-west4-c`|
|South America|All locations within South<br>America:<br>`in:southamerica-locations`|_Groups:_<br>`br-locations`<br>`cl-locations`|

|Group|Details|Direct members|
|---|---|---|
|Brazil|All locations within Brazil:<br>`in:br-locations`|_Groups:_<br>`southamerica-east1-`<br>`locations`|
|||_Values:_<br>`br`|
|Chile|All locations within Chile:<br>`in:cl-locations`|_Groups:_<br>`southamerica-west1-`<br>`locations`|
|||_Values:_|
|||`cl`|
|Santiago|All locations within Santiago:<br>`in:southamerica-west1-`<br>`locations`|_Values:_<br>`southamerica-west1`<br>`southamerica-west1-a`<br>`southamerica-west1-b`<br>`southamerica-west1-c`|
|Thailand|All locations within Thailand:<br>`in:th-locations`|_Groups:_<br>`asia-southeast3-`<br>`locations`|
|||_Values:_<br>`th`|
|Bangkok|All locations within Bangkok:<br>`in:asia-southeast3-`<br>`locations`|_Values:_<br>`asia-southeast3`<br>`asia-southeast3-a`<br>`asia-southeast3-b`<br>`asia-southeast3-c`|

### Authentication

Organization Policy Service uses OAuth 2.0 (http://tools.ietf.org/html/rfc6749) for API authentication and authorization. To get an OAuth 2.0 bearer token: 

1. Go to the OAuth 2.0 Playground page (https://developers.google.com/oauthplayground/). 

2. In the **Step 1** list of scopes, select the **Cloud Resource Manager API v2** > **https://www.googleapis.com/auth/cloud-platform** , and then click **Authorize APIs** . 

3. On the **Sign in with Google** page that appears, select your account and sign in. 

4. To provide access to **Google OAuth 2.0 Playground** , click **Allow** on the prompt that appears. 

5. In **Step 2** , click **Exchange authorization code for tokens** . 

6. At the bottom of the **Request / Response** pane on the right, your access token string is displayed: 

```
{
 "access_token": "ACCESS_TOKEN",
 "token_type": "Bearer",
 "expires_in": 3600
}
```

Where _ACCESS_TOKEN_ is the OAuth 2.0 bearer token string that you can use for API authorization. 

Last updated 2026-10-13 UTC.
