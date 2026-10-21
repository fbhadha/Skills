# Canada Protected B, Assured Workloads and access controls / Regions and zones: Regions and zones to Available regions and zones
Source: 05-Canada-Protected-B-Assured-Workloads-and-access-controls.pdf, pages 422-505, extracted 2026-10-18

## Regions and zones

URL: https://docs.cloud.google.com/compute/docs/regions-zones

Compute Engine resources are hosted in multiple locations worldwide. These locations are composed of regions and zones. 

_Regions_ are independent geographic areas that consist of _zones_ . Zones and regions are logical abstractions of underlying physical resources. For more information about region-specific considerations, see Geography and regions (/docs/geography-and-regions#regions_and_zones). 

Resources that live in a zone, such as Compute Engine instances 

(/compute/docs/instances) or zonal disks (/compute/docs/disks), are referred to as zonal resources. Other resources, like static external IP addresses 

(/compute/docs/ip-addresses#reservedaddress), are regional. Regional resources can be used by any resource in that region, regardless of zone, while zonal resources can only be used by other resources in the same zone. For example, to attach a zonal persistent disk to an instance, both resources must be in the same zone. Similarly, if you want to assign a static IP address to an instance, the instance must be in the same region as the static IP address. 

Putting resources in different zones in a region reduces the risk of an infrastructure outage affecting all resources simultaneously. Putting resources in different regions provides an even higher degree of failure independence. This lets you design robust systems with resources spread across different failure domains. 

Only certain resources are region- or zone-specific. Other resources, such as images, are global resources that can be used by any other resources across any location. For information on global, regional, and zonal Compute Engine resources, see Global, Regional, and Zonal Resources 

(/compute/docs/regions-zones/global-regional-zonal-resources). 

Google Cloud also offers specialized AI zones that provide high-capacity GPUs and TPUs for AI and ML workloads. These zones have unique characteristics, including specific network latency requirements and shared fate with a parent zone. For more information, see AI zones (/compute/docs/regions-zones/ai-zones). 

### Identifying a region or zone

Each region in Compute Engine contains a number of zones. Each zone name contains two parts that describe each zone in detail. The first part of the zone name is the **region** and the second part of the name describes the **zone** in the region: 

**Region** 

_Regions_ are collections of zones. Zones have high-bandwidth, low-latency network connections to other zones in the same region. In order to deploy fault-tolerant applications that have high availability, Google recommends deploying applications across multiple zones and multiple regions. This helps protect against unexpected failures of components, up to and including a single zone or region. 

Choose regions that make sense for your scenario. For example, if you only have customers in the US, or if you have specific needs that require your data to live in the US, it makes sense to store your resources in zones in the `uscentral1` region or zones in the `us-east1` region. 

**Zone** 

A _zone_ is a deployment area within a region. Zones which are specialized for AI and ML workloads are called AI zones. Non-AI zones are referred to as _standard zones_ or just _zones_ . Depending on how widely you want to distribute your resources, create compute instances across multiple zones in multiple regions for redundancy. 

**Standard zone** 

A standard zone name contains two parts: the **region** and the **zone** in the region. For example, the fully qualified name for zone `a` in region `uscentral1` is `us-central1-a` . 

**AI zone** 

AI zones follow an extended naming convention to differentiate them from non-AI zones. For an AI zone, the `<zone>` variable consists of three parts: the string ai (to identify it as an AI zone), a number (indicating its deployment group), and a letter (indicating the shared software update schedule). For example, the fully qualified name for AI zone `ai2b` in region `us-west4` is `us-west4-ai2b` . This AI zone shares its deployment rollout wave with the standard `us-west4-b` zone. 

### Resource quotas

Certain resources, such as static IPs, images, firewall rules, and VPC networks, have defined project-wide quota limits and per-region quota limits. When you create these resources, it counts towards your total project-wide quota or your perregion quota, if applicable. If any of the affected quota limits are exceeded, you won't be able to add more resources of the same type in that project or region. 

To see a comprehensive list of quotas that apply to your project, visit the Quotas (https://console.cloud.google.com/iam-admin/quotas) page in the Google Cloud console. 

For example, if your global target pools quota is 50 and you create 25 target pools in example-region-1 and 25 target pools in example-region-2, you reach your project-wide quota and won't be able to create more target pools in any region within your project until you free up space. Similarly, if you have a per-region quota of 7 reserved IP addresses, you can only reserve up to 7 IP addresses in a single region. After you reach that limit, you will either need to reserve IP addresses in a new region or release some IP addresses. 

### Transparent maintenance

Google regularly maintains its infrastructure by patching systems with the latest software, performing routine tests and preventative maintenance, and generally ensuring that Google infrastructure is as fast and efficient as Google knows how to make it. 

By default, all compute instances are configured so that these maintenance events are transparent to your applications and workloads. Google uses a combination of datacenter innovations, operational best practices, and live migration technology to move running virtual machine instances out of the way of maintenance that is being performed. Your instance continues to run within the same zone with no action on your part. 

By default, most virtual machines are set to live migrate, but you can also set your virtual machines to stop and reboot. Some machine series support only stop and reboot for maintenance operations. The two options differ in the following ways: 

**Live migrate** 

Compute Engine automatically migrates your running instance. The migration process will impact guest performance to some degree but your instance remains online throughout the migration process. The exact guest performance impact and duration depends on many factors, but it is expected most applications and workloads will not notice. For more information, see Live Migration (/compute/docs/instances/live-migration-process). 

**Stop and reboot** 

Compute Engine automatically signals your instance to shut down, waits a short time for it to shut down cleanly, and then restarts it away from the maintenance event. 

For more information on how to set the options above for your instances, see Set VM host maintenance policy (/compute/docs/instances/setting-vm-host-options). 

### Choosing a region and zone

You choose which region or zone hosts your resources, which controls where your data is stored and used. Choosing a region and zone is important for several reasons: 

**Handling failures** 

Distribute your resources across multiple zones and regions to tolerate outages. Google designs zones to minimize the risk of correlated failures caused by physical infrastructure outages like power, cooling, or networking. Thus, if a zone becomes unavailable, you can transfer traffic to another zone in the same region to keep your services running. Similarly, you can mitigate the impact of a region outage on your application by running backup services in a different region. For more information about distributing your resources and designing a robust system, see Designing resilient systems (/compute/docs/tutorials/robustsystems). 

**Decreased network latency** 

To decrease network latency, you might want to choose a region or zone that is close to your point of service. For example, if you mostly have customers on the East coast of the United States of America, then you might want to choose 

a primary region and zone that is close to that area and a backup region and zone that is also close by. 

**Optimized AI and ML acceleration** 

For workloads that require high-capacity AI accelerators, AI zones are available in select regions. These specialized zones provide GPU and TPU resources for AI and ML training and inference. You can select an AI zone to use infrastructure that is optimized for maximizing AI and ML throughput. See the AI zones (/compute/docs/regions-zones/ai-zones) section for details. 

For more information about how to choose a region and zone for your Compute Engine resources, see Best practices for Compute Engine regions selection 

(https://cloud.google.com/solutions/best-practices-compute-engine-region-selection). 

### Location selection tips

During compute instance creation, Compute Engine can automatically select zones for your instances based on capacity and availability using the following methods: 

- The bulk instance creation API 

- (/compute/docs/instances/multiple/about-bulk-creation) can automatically choose the zone in which to create instances. 

- A regional managed instance group (MIG) can be configured with a target distribution shape 

- (/compute/docs/instance-groups/regional-mig-set-target-distribution-shape), which can automatically create instances in zones where resources are available. 

- If you are creating an instance in the Google Cloud console and you know the machine type and region that you want but you aren't sure which zone to select, you can select **Any** and Google will choose a zone for you based on the machine type and availability. 

When selecting zones yourself, here are some things to keep in mind: 

**Communication within and across regions will incur different costs.** 

Generally, communication within regions will always be cheaper and faster than communication across different regions. 

**Design important systems with redundancy across multiple zones or regions.** 

At some point in time, your instances might experience an unexpected failure. To mitigate the effects of these possible events, you should duplicate important systems in multiple zones and regions. 

For example, by hosting instances in zones `europe-west1-b` and `europe-west1-` `c` , if `europe-west1-b` fails unexpectedly, your instances in zone `europe-west1-c` will still be available. However, if you host all your instances in `europe-west1-` `b` , you will not be able to access any instances if `europe-west1-b` goes offline. Also, consider hosting your resources across regions. For example, to plan for continued availability of your workload in the unlikely scenario that the `europe-west1` region experiences a failure, consider deploying the workload on backup instances in the `europe-west3` region. For more tips on how to design systems for availability, see Designing resilient systems 

(/compute/docs/tutorials/robustsystems). 

### Available regions and zones

You can use the Google Cloud console, the Google Cloud CLI, or REST to see available regions and zones (/compute/docs/regions-zones/viewing-regions-zones). You can also get the complete list of available machine types in all regions and zones by using the `gcloud compute machine-types list` command 

(/sdk/gcloud/reference/compute/machine-types/list). For example, running the following command displays all the regions and zones where you can use `c4d-standard-4` machine types. 

```
gcloud compute machine-types list --filter="name=c4d-standard-4"
```

Each zone offers a variety of processors. When you create an instance in a zone, your instance uses the default processor supported in that zone. For example, if you create an instance in the `us-central1-a` zone, your instance by default uses an Intel Haswell processor, unless you specify another option. 

Alternatively, you can choose your desired CPU platform. For more information, read Specifying a minimum CPU platform for VM instances 

(/compute/docs/instances/specify-min-cpu-platform). 

Consider the following information about resource availability before you select the regions and zones where you create your instances: 

- Local SSD and Titanium SSD storage is available in all regions and zones for supported machine series and machine types. See About Local SSD disks (/compute/docs/disks/local-ssd) to learn more. 

- GPUs (/compute/docs/regions-zones/gpu-regions-zones) and TPUs 

- (/compute/docs/regions-zones/tpu-regions-zones) are available only in specific zones. 

- Sole-tenancy (/compute/docs/nodes/sole-tenant-nodes) is available in regions and zones where machine series with sole-tenant node types 

- (/compute/docs/nodes/sole-tenant-nodes#node_types) are available. 

- Confidential VM 

- (/confidential-computing/confidential-vm/docs/supported-configurations) is available only with certain machine series in specific zones. 

For information about hardware and feature support for all machine series, see Machine series comparison (/compute/docs/machine-resource#machine_type_comparison). For example, to see which machine series support both Intel TDX and sole tenancy, in the **Choose instance properties to compare** field, select both **Confidential Computing** and **Sole tenancy** . 

For zonal availability of bare metal machine types, see Regional availability of bare metal instances (/compute/docs/instances/bare-metal-instances#regions-zones). 

|ZonesLocation<br>|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`afric`<br>Johannesburg|,<br>E2, N4 ,|Intel|AMD SEV||
|`a-`<br>`south`<br>`1-a`<br>South Africa|N2 , N2D<br>C4 , C4A,<br>C4D,<br>T2D, M3,<br>C2D|,<br> <br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`afric`<br>Johannesburg|,<br>E2, N4 ,|Intel|AMD SEV||
|`a-`<br>`south`<br>South Africa|N2 , N2D<br>C4 , T2D,|,<br>Cascade<br>Lake, Ice|(/confidential-<br>computing/confidential||
|`1-b`|C2D|Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`afric`<br>`a-`<br>`south`<br>`1-c`<br>Johannesburg<br>South Africa|,<br>E2, N4 ,<br>N2 , N2D<br>C4 , C4D,<br>T2D, M3,<br>C2D|,<br> <br> <br>Intel<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`east1`<br>`-a`<br>Changhua<br>County,<br>Taiwan, APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>C3D,<br>T2D, Z3-<br>metal,<br>M1, C2 ,<br>C2D, G4,<br>G2|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`east1`<br>`-b`<br>Changhua<br>County,<br>Taiwan, APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>C3D,<br>T2D, M3,<br>M1, C2 ,<br>C2D, G2|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`east1`<br>`-c`<br>Changhua<br>County,<br>Taiwan, APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>C3D,<br>T2D, Z3-<br>metal,<br>M3, M1,<br>C2 , C2D,|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice|,<br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
||A3, G2|Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|<br>||
|`asia-`<br>`east2`<br>`-a`<br>Hong Kong,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C3 , T2D,<br>C2|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`east2`<br>`-b`<br>Hong Kong,<br>APAC|E2, N2 ,<br>N2D, N1<br>T2D, C4 ,<br>C2|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`asia-`<br>`east2`<br>`-c`<br>Hong Kong,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, T2D,<br>C4 , C2 ,<br>C2D|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`north`<br>`east1`<br>`-a`<br>Tokyo, Japan,<br>APAC|E2, C4A,<br>N4 , N2 ,<br>N2D, N1,<br>T2D, Z3,<br>M4N,<br>M4, M3,<br>M2, M1,<br>C2 , A2,<br>G2|<br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`asia-`<br>`north`<br>`east1`<br>`-b`<br>Tokyo, Japan,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A,<br>C4D, C3 ,<br>T2D, Z3,<br>M3, M2,<br>M1, C2 ,<br>C2D, A4 ,<br>A3, G4,<br>G2|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`north`<br>`east1`<br>`-c`<br>Tokyo, Japan,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A,<br>C4D, C3 ,<br>T2D, Z3,<br>M3, M1,<br>C2 , A2,<br>G2|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`asia-`<br>`north`<br>`east2`<br>`-a`<br>Osaka, Japan,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C3 , T2D,<br>M3, M1,<br>C2 , C2D|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`north`<br>`east2`<br>`-b`<br>Osaka, Japan,<br>APAC|E2, N2 ,<br>N2D, N1,<br>T2D, M3,<br>M2, M1,<br>C2|<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>AMD EPYC<br>Milan|<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`asia-`<br>`north`<br>`east2`<br>`-c`<br>Osaka, Japan,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C3 , T2D,<br>M3, M2,<br>M1, C2 ,<br>C2D|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Mac<br>typ|hine<br>es|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`asia-`<br>`north`<br>Seoul, South<br>Korea, APAC|E2,<br>N2 ,|N4 ,<br>N2D|,<br>Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-||
|`east3`<br>`-a`|N1,<br>C3 ,<br>M2,<br>C2 ,|C4 ,<br>M3,<br>M1,<br>C2D,|<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell|,<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
||G2||Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|||
|`asia-`<br>`north`<br>Seoul, South<br>Korea, APAC|E2,<br>N2 ,|N4 ,<br>N2D|,<br>Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-||
|`east3`<br>`-b`|N1,<br>C3 ,<br>M2,<br>C2 ,<br>A2,|C4 ,<br>M3,<br>M1,<br>C2D,<br>G2|<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`north`<br>`east3`<br>`-c`<br>Seoul, South<br>Korea, APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>M3, C2 ,<br>C2D, A3|,<br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`asia-`<br>`south`<br>Mumbai,<br>India, APAC|E2, N4 ,<br>N4D, N2|,<br>Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-||
|`1-a`|N2D, C4<br>C4A, C3 ,<br>C3D,<br>T2D, N1,<br>M2, M1,<br>C2 , C2D,|,<br> <br> <br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade|,<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
||G2|Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,|<br> <br>||
|||Google<br>Axion|||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`south`<br>`1-b`<br>Mumbai,<br>India, APAC|E2, N4 ,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, Z3,<br>X4, M4N,<br>M4 , M3,<br>M2, M1,<br>C2 , C2D,<br>G2, A3|,<br> <br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`south`<br>`1-c`<br>Mumbai,<br>India, APAC|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, Z3,<br>H4D, X4,<br>M4N,<br>M4 , M3,<br>M1, C2 ,<br>C2D, A3,<br>G4, G2|,<br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`south`<br>Delhi, India,<br>APAC|E2, N4 ,<br>N2 , N2D,|<br>Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-||
|`2-a`|N1, C4 ,<br>C3, T2D,<br>X4, M4N,|<br>Haswell,<br>Broadwell<br>Skylake,|,<br>computing/confidential<br>-vm/docs/supported-<br>configurations?||
||M4 , M3,<br>M2, M1,<br>C2 , C2D,|<br>Cascade<br>Lake, Ice<br>Lake,|tab=amd-sev)||
||G4|Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|<br>||
|`asia-`<br>`south`<br>Delhi, India,<br>APAC|E2, N4 ,<br>N2 , N2D,|<br>Intel Ivy<br>Bridge,|AMD SEV<br>(/confidential-||
|`2-b`|N1, C4 ,<br>C3 ,T2D,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>C2 , C2D|Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`south`<br>`2-c`<br>Delhi, India,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C3 , T2D,<br>C2 , A3,<br>G4|,<br> <br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`asia-`<br>`south`<br>`east1`<br>`-a`<br>Jurong West,<br>Singapore,<br>APAC|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D, C2 ,<br>C2D,<br>T2D, Z3,<br>H4D,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>A2, G4,<br>G2|,<br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`south`<br>`east1`<br>`-b`<br>Jurong West,<br>Singapore,<br>APAC|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D, C2 ,<br>C2D,<br>T2D,<br>T2A, Z3,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>A4 , A3,<br>G4, G2|,<br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Ampere<br>Altra Arm,<br>Google<br>Axion|,<br> <br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`south`<br>`east1`<br>`-c`<br>Jurong West,<br>Singapore,<br>APAC|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell|,<br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
||C3D,<br>T2D,<br>T2A, Z3,<br>M1, C2 ,<br>C2D, A2,<br>A3, G2|Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Ampere<br>Altra Arm,<br>Google<br>Axion|<br> <br> <br> <br>,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`south`<br>`east2`<br>`-a`<br>Jakarta,<br>Indonesia,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>T2D, M1|,<br> <br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|<br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`asia-`<br>`south`<br>`east2`<br>`-b`<br>Jakarta,<br>Indonesia,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A,<br>T2D, G4|,<br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion<br>AMD EPYC<br>Turin|<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`asia-`<br>`south`<br>`east2`<br>`-c`<br>Jakarta,<br>Indonesia,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A,<br>T2D, M1,<br>G4|,<br> <br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`asia-`<br>`south`<br>`east3`<br>`-a`<br>Bangkok,<br>Thailand,<br>APAC|N4 , C4 ,<br>C3D,<br>M4N,<br>M4 , M3|Intel<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|||
|`asia-`<br>`south`<br>`east3`<br>`-b`<br>Bangkok,<br>Thailand,<br>APAC|N4 , C4 ,<br>C3D,<br>M4N,<br>M4 , M3|Intel<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|||
|`asia-`<br>`south`<br>`east3`<br>`-c`<br>Bangkok,<br>Thailand,<br>APAC|N4 , C4 ,<br>C3D,<br>M4N,<br>M4 , M3|Intel<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`austr`<br>`alia-`<br>`south`<br>`east1`<br>`-a`<br>Sydney,<br>Australia,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C3 ,<br>T2D, C2 ,<br>M3, M2,<br>M1|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`austr`<br>`alia-`<br>`south`<br>`east1`<br>`-b`<br>Sydney,<br>Australia,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4,<br>C3 , C3D,<br>T2D, Z3,<br>C2 , M2,<br>M1|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`austr`<br>`alia-`<br>`south`<br>`east1`<br>`-c`<br>Sydney,<br>Australia,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, C2 ,<br>M4N,<br>M4 , M3,<br>M1, A3,<br>Z3|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`austr`<br>`alia-`<br>`south`<br>`east2`<br>`-a`<br>Melbourne,<br>Australia,<br>APAC|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>C3D,<br>T2D, Z3-<br>metal,<br>C2D|,<br> <br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`austr`<br>Melbourne,|E2, N4 ,|Intel Ivy|GPUs||
|`alia-`<br>`south`<br>Australia,<br>APAC|N2 , N2D<br>N1, C4 ,|,<br>Bridge,<br>Haswell,|||
|`east2`|C4A,|Broadwell,|||
|`-b`|T2D, C3 ,|<br>Skylake,|||
||Z3-|Cascade|||
||metal,<br>M3, M1,|Lake, Ice<br>Lake,|||
||A3|Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|||
|`austr`<br>`alia-`<br>`south`<br>Melbourne,<br>Australia,<br>APAC|E2, N4 ,<br>N2 , N2D<br>C4 , C4A,|,<br> <br>Intel Ivy<br>Bridge,<br>Haswell,|AMD SEV<br>(/confidential-<br>computing/confidential||
|`east2`|T2D, N1,|<br>Broadwell,|-vm/docs/supported-||
|`-c`|M3, M1|Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`centr`<br>`al2-a`<br>Warsaw,<br>Poland,<br>Europe|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A,<br>T2D,<br>M4N,<br>M4 , M3,<br>M1, C2D|,<br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`centr`<br>`al2-b`<br>Warsaw,<br>Poland,<br>Europe|E2, N2 ,<br>N2D, N1<br>T2D, M1,<br>C2D|,<br> <br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`centr`<br>`al2-c`<br>Warsaw,<br>Poland,<br>Europe|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>T2D|,<br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`north`<br>`1-a`<br>Hamina,<br>Finland,<br>Europe|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A,<br>C3D,<br>T2D, C2 ,<br>M3, G4|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`north`<br>`1-b`<br>Hamina,<br>Finland,<br>Europe|E2, N4 ,<br>N2 , N2D<br>N1, C4A,<br>C4 , C3 ,<br>T2D, C2 ,|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Broadwell|,<br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
||G4|Skylake,<br>Cascade<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|<br> <br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`north`<br>`1-c`<br>Hamina,<br>Finland,<br>Europe|E2, N4 ,<br>N2 , N2D<br>N1, T2D,<br>C4 , C4A,<br>C2 , M3,<br>A4 , G4|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`north`<br>`2-a`<br>Stockholm,<br>Sweden,<br>Europe|E2, N4 ,<br>C4 , C4A,<br>C3 , C3D<br>Z3|<br>,<br>Intel Ivy<br>Bridge,<br>Broadwell<br>Haswell,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|,<br> <br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`north`<br>`2-b`<br>Stockholm,<br>Sweden,<br>Europe|E2, N4 ,<br>C4 , C4A,<br>C3 , C3D<br>Z3, C2D|<br>,<br>Intel Ivy<br>Bridge,<br>Broadwell,<br>Haswell,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|<br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`north`<br>`2-c`<br>Stockholm,<br>Sweden,<br>Europe|E2, N4 ,<br>C4|Intel Ivy<br>Bridge,<br>Broadwell,<br>Haswell,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`south`<br>`west1`<br>`-a`<br>Madrid,<br>Spain, Euro|pe<br>E2, N4 ,<br>N2 , N2D<br>C4 , C4A,<br>T2D,<br>M4N,<br>M4 , M3,<br>M2, M1|,<br> <br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`south`<br>`west1`<br>`-b`<br>Madrid,<br>Spain, Euro|pe<br>E2, N4 ,<br>N2 , N2D<br>C4 , C4A,<br>T2D,<br>C2D|,<br> <br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`south`<br>`west1`<br>`-c`<br>Madrid,<br>Spain, Euro|pe<br>E2, N4 ,<br>N2 , N2D<br>C4 , C4A,<br>T2D,<br>M4N,<br>M4 , M3,<br>M2, M1|,<br> <br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west1`<br>`-b`<br>St. Ghislain,<br>Belgium,<br>Europe|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1<br>C4 , C4A,<br>C4D, C3<br>C3D,<br>T2D, Z3,<br>X4, M4N<br>M4 , M3,<br>M2, M1,<br>C2 , C2D<br>A4 , A3,<br>G4, G2|,<br>,<br> <br>,<br> <br>,<br>,<br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west1`<br>`-c`<br>St. Ghislain,<br>Belgium,<br>Europe|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1<br>C4 , C4A,<br>C4D, C3<br>C3D,<br>T2D, Z3,<br>X4, M4N<br>M4 , M2,<br>C2 , C2D<br>A3, G4,<br>G2|,<br>,<br> <br>,<br>,<br>,<br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west1`<br>`-d`<br>St. Ghislain,<br>Belgium,<br>Europe|E2, N4 ,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, Z3,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>C2 , C2D|,<br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west2`<br>`-a`<br>London,<br>England,<br>Europe|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1<br>C4 , C4A,<br>C4D,<br>C4N, C3<br>C3D, C2<br>C2D,<br>T2D, Z3,<br>M3, M2,<br>M1, G2|,<br>,<br> <br>,<br>,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west2`<br>`-b`<br>London,<br>England,<br>Europe|E2, N4 ,<br>N4A, N2<br>N2D, N1<br>C4 , C4A,<br>C4D, C3<br>C3D, C2<br>C2D,<br>T2D, Z3,<br>M3, M2,<br>M1, G4,<br>G2|,<br>,<br> <br>,<br>,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west2`<br>`-c`<br>London,<br>England,<br>Europe|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1<br>C4 , C4A,<br>C4D, C3<br>C2 , C2D<br>T2D, Z3,<br>M4N,<br>M4 , M3,<br>M1, G4|,<br>,<br> <br>,<br>,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west3`<br>`-a`<br>Frankfurt,<br>Germany,<br>Europe|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
||C3D,<br>T2D, Z3,<br>X4, M4N,<br>M4 , M3,<br>M2, M1,<br>C2 , C2D,|<br> <br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,|,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)||
||G2|Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west3`<br>`-b`<br>Frankfurt,<br>Germany,<br>Europe|E2, N4 ,<br>N4A, N2 ,<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, Z3,<br>X4, M4N,<br>M4 , M3,<br>M2, M1,<br>C2 , C2D,|<br> <br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?||
||G2|Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|tab=amd-sev-snp)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west3`<br>`-c`<br>Frankfurt,<br>Germany,<br>Europe|E2, N4 ,<br>N4A, N2 ,<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, Z3,<br>M3, M1,<br>C2 , C2D,<br>A3|<br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west4`<br>`-a`<br>Eemshaven,<br>Netherlands,<br>Europe|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,|,<br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell|,<br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
||C3D,|Skylake,|,<br>AMD SEV-SNP||
||T2D,<br>T2A, Z3,<br>X4, M4N<br>M4 , M3,<br>M2, M1,<br>C2 , C2D,<br>A3, A2,<br>G4, G2|,<br> <br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Ampere<br>Altra Arm,<br>Google<br>Axion|<br> <br> <br> <br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west4`<br>`-b`<br>Eemshaven,<br>Netherlands,<br>Europe|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,|,<br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell|,<br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
||C3D,<br>T2D,<br>T2A, Z3,<br>X4, M4N<br>M4 , M3,<br>M2, M1,<br>H4D, H3<br>C2 , C2D,<br>A4X , A4 ,<br>A3, A2,<br>G4, G2|,<br>,<br> <br> <br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Ampere<br>Altra Arm,<br>Google<br>Axion|<br> <br> <br> <br>,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west4`<br>`-c`<br>Eemshaven,<br>Netherlands,<br>Europe|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1<br>C4 , C4A,<br>C4D, C3<br>C3D,<br>T2D,<br>T2A, Z3,<br>X4, M2,<br>M1, H4D<br>H3, C2 ,<br>C2D, A3,<br>G4, G2|,<br>,<br> <br>,<br>,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Ampere<br>Altra Arm,<br>Google<br>Axion|,<br> <br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)<br>,<br>NVIDIA Confidential<br>Computing<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=nvidia-<br>confidential-<br>computing)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`west6`<br>`-a`<br>Zurich,<br>Switzerland,<br>Europe|E2, N4 ,<br>N2 , N2D<br>N1, C2 ,<br>T2D|,<br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|,<br>|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west6`<br>`-b`<br>Zurich,<br>Switzerland,<br>Europe|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A,<br>T2D, M3,<br>M1, C2 ,<br>G2, Z3|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`west6`<br>`-c`<br>Zurich,<br>Switzerland,<br>Europe|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>T2D, M3,<br>M1, C2 ,<br>G2|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west8`<br>`-a`<br>Milan, Italy,<br>Europe|E2, N4 ,<br>N2 , N2D<br>T2D, X4,<br>M3, M2,<br>M1|,<br> <br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`west8`<br>`-b`<br>Milan, Italy,<br>Europe|E2, N4 ,<br>N2 , N2D<br>C4 , T2D,<br>Z3-<br>metal,<br>M2, G4|,<br> <br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west8`<br>`-c`<br>Milan, Italy,<br>Europe|E2, N4 ,<br>N2 , N2D<br>C4 , C2D,<br>T2D, Z3-<br>metal,<br>X4, M3,<br>M2, M1,<br>G4|,<br> <br>Intel<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`west9`<br>`-a`<br>Paris, France,<br>Europe|E2, N4 ,<br>N2 , N2D<br>C4 , C3 ,<br>T2D, M3|,<br>Intel<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west9`<br>`-b`<br>Paris, France,<br>Europe|E2, N4 ,<br>N2 , N2D<br>C4 , C4D<br>C3 , T2D,<br>M3, M1|,<br>,<br> <br>Intel<br>Broadwell,<br>Haswell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`west9`<br>`-c`<br>Paris, France,<br>Europe|E2, N4 ,<br>N2 , N2D<br>C4 , C3 ,<br>T2D, M1,<br>A3|,<br> <br>Intel<br>Broadwell,<br>Haswell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west1`<br>`0-a`<br>Berlin,<br>Germany,<br>Europe|E2, N4 ,<br>N2 , N2D<br>C4D, C3 ,<br>T2D, Z3|,<br> <br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`europ`<br>`e-`<br>`west1`<br>`0-b`<br>Berlin,<br>Germany,<br>Europe|E2, N2 ,<br>N2D,<br>C4D, Z3,<br>G4|<br>Intel<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`europ`<br>`e-`<br>`west1`<br>`0-c`<br>Berlin,<br>Germany,<br>Europe|E2, N4 ,<br>N2 , N2D<br>C4 , C4D,<br>T2D, Z3|,<br> <br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`europ`<br>`e-`<br>`west1`<br>`2-a`<br>Turin, Italy,<br>Europe|E2, N2 ,<br>N2D,<br>T2D,<br>M4N,<br>M4 , M3|Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`west1`<br>`2-b`<br>Turin, Italy,<br>Europe|E2, N2 ,<br>N2D,<br>T2D, M3,<br>C2D|<br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>AMD EPYC<br>Milan|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`europ`<br>`e-`<br>`west1`<br>`2-c`<br>Turin, Italy,<br>Europe|E2, N4 ,<br>N2 , N2D<br>C4 , T2D|,<br>Intel<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`me-`<br>`centr`<br>`al1-a`<br>Doha, Qatar,<br>Middle East|E2, N2 ,<br>N2D, C4<br>C3 , T2D<br>Z3-meta|,<br>,<br>l<br>Intel<br>Broadwell,<br>Haswell,<br>Ivy|||
|||Bridge,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>AMD EPYC<br>Milan|||
|`me-`<br>`centr`<br>Doha, Qatar,<br>Middle East|E2, N4 ,<br>N2 , N2D|,<br>Intel<br>Broadwell,|AMD SEV<br>(/confidential-||
|`al1-b`|C4 , T2D<br>M3|,<br>Haswell,<br>Ivy<br>Bridge,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`me-`<br>`centr`<br>`al1-c`<br>Doha, Qatar,<br>Middle East|E2, N4 ,<br>N2 , N2D<br>C4 , C4A,<br>C3 , T2D,<br>Z3-<br>metal,<br>M3|,<br> <br> <br>Intel<br>Broadwell,<br>Haswell,<br>Ivy<br>Bridge,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`me-`<br>`centr`<br>`al2-a`<br>Dammam,<br>Saudi Arabia,<br>Middle East|E2, N4 ,<br>N2 , N2D<br>C4 , C4A,<br>C3 , C3D,<br>T2D, C2 ,<br>M3, M2,<br>G4, G2|,<br> <br> <br> <br>Intel<br>Broadwell,<br>Haswell,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`me-`<br>`centr`<br>`al2-b`<br>Dammam,<br>Saudi Arabia,<br>Middle East|E2, N2 ,<br>N2D, C3<br>T2D, M3,<br>M2, C2|,<br> <br>Intel<br>Broadwell,<br>Haswell,<br>Ivy<br>Bridge,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>AMD EPYC<br>Milan|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`me-`<br>`centr`<br>`al2-c`<br>Dammam,<br>Saudi Arabia,<br>Middle East|E2, N4 ,<br>N2 , N2D<br>C4 , C3 ,<br>C3D,<br>T2D,<br>M4N,<br>M4 , M3,<br>M2, C2 ,<br>G2|,<br>Intel<br>Broadwell,<br>Haswell,<br>Ivy<br>Bridge,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`me-`<br>`west`<br>`-a`|`1`<br>Tel Aviv,<br>Israel, Middle<br>East|E2, N4 ,<br>N2 , N2D<br>C4 , C3 ,<br>T2D, M3,<br>M1, C2 ,<br>A2|,<br> <br>Intel<br>Broadwell,<br>Haswell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`me-`<br>`west`|`1`<br>Tel Aviv,<br>Israel, Middle|E2, N4 ,<br>N2 , N2D|,<br>Intel<br>Broadwell,|GPUs,<br>AMD SEV<br>(/confidential-||
|`-b`|East|N1<br>GPU<br>required<br>(#n1-<br>footnote<br>, C4 ,<br>C4A, C3 ,<br>C3D,<br>T2D, C2|)<br> <br>Haswell,<br>Ivy<br>Bridge,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|i<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`me-`<br>`west1`<br>`-c`<br>Tel Aviv,<br>Israel, Middle<br>East|E2, N2 ,<br>N2D,<br>N1<br>GPU<br>required<br>(#n1-<br>footnote<br>, C3 ,<br>T2D, M3,<br>M1, C2 ,<br>C2D, A2|)<br> <br>Intel<br>Broadwell<br>Haswell,<br>Ivy<br>Bridge,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`north`<br>`ameri`<br>`ca-`<br>`north`<br>`east1`<br>`-a`<br>Montréal,<br>Québec,<br>North<br>America|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>T2D,<br>M4N,<br>M4 , C2 ,<br>C2D|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`north`<br>`ameri`<br>`ca-`<br>`north`<br>`east1`<br>`-b`<br>Montréal,<br>Québec,<br>North<br>America|E2, N4 ,<br>C4 , C4A,<br>C4D, C3<br>N2 , N2D<br>N1, T2D,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>H3, C2 ,<br>G2|<br>,<br>,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`north`<br>`ameri`<br>`ca-`<br>`north`<br>`east1`<br>`-c`<br>Montréal,<br>Québec,<br>North<br>America|E2, N2 ,<br>N2D, N1<br>T2D, M3,<br>M2, M1,<br>C2 , G2|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`north`<br>`ameri`<br>`ca-`<br>`north`<br>`east2`<br>`-a`<br>Toronto,<br>Ontario, No<br>America|rth<br>E2, N2 ,<br>N2D, N1<br>C4 , T2D,<br>M3, M2,<br>M1, G2|,<br> <br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`north`<br>`ameri`<br>Toronto,<br>Ontario, No|rth<br>E2, N4 ,<br>N2 , N2D|,<br>Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-|Low CO<br>2|
|`ca-`<br>`north`<br>`east2`<br>`-b`<br>America|N1, C4 ,<br>C4A,<br>C4D,<br>C2D,<br>T2D, Z3-<br>metal,<br>M3, M2,<br>M1, G2|<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`north`<br>`ameri`<br>Toronto,<br>Ontario, Nor|th<br>E2, N4 ,<br>N2 , N2D|,<br>Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-|Low CO<br>2|
|`ca-`<br>`north`<br>`east2`<br>`-c`<br>America|N1, C4 ,<br>C2D,<br>T2D, Z3-<br>metal,<br>M4N,<br>M4 , M3,<br>M2, A3|Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|(https://cloud.google.com/susta<br>carbon#region-picker)|
|`north`<br>`ameri`<br>`ca-`<br>`south`<br>`1-a`<br>Queretaro,<br>Mexico, Nort<br>America|h<br>E2, N4 ,<br>C4 , C4A,<br>C3D, Z3|<br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|,<br> <br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`north`<br>`ameri`<br>`ca-`<br>`south`<br>`1-b`<br>Queretaro,<br>Mexico, North<br>America|E2, N4 ,<br>C4 , C4A,<br>C3D, Z3|<br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`north`<br>`ameri`<br>`ca-`<br>`south`<br>Queretaro,<br>Mexico, North<br>America|E2, N4 ,<br>C4 , C4A,<br>C3D, Z3|<br>Intel Ivy<br>Bridge,<br>Haswell,<br>Broadwell,|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-||
|`1-c`||Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|configurations?<br>tab=amd-sev)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`south`<br>`ameri`<br>`ca-`<br>`east1`<br>`-a`<br>Osasco, São<br>Paulo, Brazil,<br>South<br>America|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C3 , T2D,<br>Z3-<br>metal,<br>C2 , C2D,<br>G4|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`south`<br>`ameri`<br>`ca-`<br>`east1`<br>`-b`<br>Osasco, São<br>Paulo, Brazil,<br>South<br>America|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C3 , T2D,<br>M3, M2,<br>M1, C2 ,<br>C2D, G4|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`south`<br>`ameri`<br>`ca-`<br>`east1`<br>`-c`<br>Osasco, São<br>Paulo, Brazil,<br>South<br>America|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>T2D,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>C2 , C2D|,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`south`<br>`ameri`<br>Santiago,<br>Chile, South|E2, N4 ,<br>N2 , N2D|,<br>Intel<br>Broadwell|,|Low CO<br>2|
|`ca-`<br>`west1`<br>America|C4 , C4A,<br>C2 , T2D,|<br> <br>Haswell,<br>Skylake,||(https://cloud.google.com/susta<br>carbon#region-picker)|
|`-a`|Z3|Cascade<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`south`<br>`ameri`<br>`ca-`<br>`west1`<br>`-b`<br>Santiago,<br>Chile, South<br>America|E2, N4 ,<br>N2 , N2D<br>C4 , C4A,<br>C2 , T2D,<br>M4N,<br>M4 , M3,<br>M2, M1|,<br> <br> <br>Intel<br>Broadwell,<br>Haswell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`south`<br>`ameri`<br>Santiago,<br>Chile, South|E2, N4 ,<br>N2 , N2D|,<br>Intel<br>Broadwell,||Low CO<br>2|
|`ca-`<br>`west1`<br>`-c`<br>America|C4 , T2D,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>C2|<br>Haswell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan||(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`centr`<br>`al1-a`<br>Council Bluffs<br>Iowa, North<br>America|f,<br>E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D,<br>C4N, C3 ,|,<br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,|,<br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>AMD SEV-SNP|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
||C3D,<br>T2D,<br>T2A,<br>Z4D,<br>Z4M, Z3,<br>X5, X4,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>H4D, H3,<br>C2 , C2D,<br>A4X , A3,<br>A2, G2|<br> <br> <br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Ampere<br>Altra Arm,<br>Google<br>Axion,<br>NVIDIA<br>Grace|<br> <br> <br> <br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)<br>,<br>NVIDIA Confidential<br>Computing<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=nvidia-<br>confidential-<br>computing)||

Machine ZonesLocation CPUs Options CO2 emissions types `us-` Council Bluffs,E2, N4 , Intel Ivy GPUs, AMD SEV `centr` Iowa, North N4D, Bridge, (/confidential- Low CO 2 `al1-b` America N4A, N2 , Sandy computing/confidential (https://cloud.google.com/susta N2D, N1, Bridge, -vm/docs/supportedcarbon#region-picker) C4 , C4A, Haswell, configurations? C4D, Broadwell,tab=amd-sev) C4N, C3 , Skylake, , AMD SEV-SNP C3D, Cascade (/confidentialT2D, Lake, Ice computing/confidential T2A, Lake, -vm/docs/supportedZ4M, Sapphire configurations? Z4D, Z3, Rapids, tab=amd-sev-snp) X4, M4N,Emerald , Intel TDX M4 , M3, Rapids, (/confidentialM2, M1, Granite computing/confidential C2 , C2D, Rapids, -vm/docs/supportedA4X AMD EPYC configurations? Max, Milan, tab=intel-tdx) A4X , A4 , AMD EPYC A3, A2, Genoa, G4, G2, AMD EPYC H4D Turin, Ampere Altra Arm, Google Axion, NVIDIA Grace 

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`centr`<br>`al1-c`<br>Council Bluffs<br>Iowa, North<br>America|f,<br>E2, N4 ,<br>N4D,<br>N4A, N2 ,<br>N2D, N1,<br>C4 , C4A,<br>C4D,<br>C4N, C3 ,<br>C3D,<br>T2D,<br>Z4M,<br>Z4D, Z3,<br>X5, X4,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>C2 , C2D,<br>A3, A2,<br>G2|<br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>AMD SEV-SNP<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev-snp)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`centr`<br>`al1-f`<br>Council Bluffs<br>Iowa, North<br>America|f,<br>E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,|,<br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell|,<br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
||C3D,|Skylake,|||
||T2D,|Cascade|||
||T2A,<br>Z4D, Z3,<br>M1, C2 ,<br>C2D, A2,|Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,|||
||G4|Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Ampere<br>Altra Arm,<br>Google<br>Axion|<br> <br> <br>||

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`us-`<br>`east`<br>`-b`|`1`<br>Moncks<br>Corner, Sou<br>Carolina,<br>North<br>America|th<br>E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, Z3,<br>M4N,<br>M4 , M3,<br>M1, H4D<br>C2 , C2D,<br>A4 , A2,<br>G4, G2|,<br> <br> <br> <br>,<br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`us-`<br>`east`<br>`-c`|`1`<br>Moncks<br>Corner, Sou<br>Carolina,<br>North<br>America|th<br>E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D,<br>C4N, C3 ,<br>C3D,<br>T2D, Z3,<br>M1, C2 ,<br>C2D, G2|,<br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`us-`<br>`east`<br>`-d`|`1`<br>Moncks<br>Corner, Sou<br>Carolina,<br>North<br>America|th<br>E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, Z3,<br>M4N,<br>M4 , M3,<br>M1, C2 ,<br>C2D,<br>A4X , A4 ,<br>G4|,<br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`east4`<br>`-a`<br>Ashburn,<br>Virginia,<br>North<br>America|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
||C3D,|Skylake,|,<br>Intel TDX||
||T2D,<br>Z4M, Z3,<br>X5, X4,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>C2 , C2D,<br>A4X<br>Max, A3,<br>G2|<br> <br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|<br> <br> <br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`east4`<br>Ashburn,<br>Virginia,|E2, N4 ,<br>N4A,|Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-||
|`-b`<br>North<br>America|N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,|,<br> <br> <br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell|,<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
||C3D,|Skylake,|||
||T2D,|Cascade|||
||Z4D, Z3,<br>X4, M4N,|<br>Lake, Ice<br>Lake,|||
||M4 , M3,<br>M2, M1,<br>C2 , C2D,|<br>Sapphire<br>Rapids,<br>Emerald|||
||A4X|Rapids,|||
||Max,<br>A4X , A4 ,|<br>Granite<br>Rapids,|||
||A3, G4|AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion,<br>NVIDIA<br>Grace|<br> <br>||

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`east4`<br>`-c`<br>Ashburn,<br>Virginia,<br>North<br>America|E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,|,<br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell,|GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
||C3D,|Skylake,|,<br>Intel TDX||
||T2D,<br>Z4D, Z3,<br>X5, X4,<br>M4N,<br>M4 , M3,<br>M1, C2 ,<br>C2D, A3,<br>A2, G4,<br>G2|Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|<br> <br> <br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||

Machine ZonesLocation CPUs Options CO2 emissions types `us-` Columbus, E2, N4 , Intel GPUs, AMD SEV `east5` Ohio, North N4D, N2 ,Broadwell, (/confidential- `-a` America N2D, C4 ,Haswell, computing/confidential C4A, Skylake, -vm/docs/supportedC4D, C3 , Cascade configurations? C3D, Lake, Ice tab=amd-sev) T2D, Lake, , NVIDIA Confidential Z4D, Z3, Sapphire Computing M4N, Rapids, (/confidentialM4 , C2 , Emerald computing/confidential A3, A2, Rapids, -vm/docs/supportedG4 Granite configurations? Rapids, tab=nvidiaAMD EPYC confidentialMilan, computing) AMD EPYC Turin, Google Axion `us-` Columbus, E2, N4 , Intel GPUs, AMD SEV `east5` Ohio, North N4D , Broadwell, (/confidential- `-b` America N2 , N2D,Haswell, computing/confidential C4 , C4A, Skylake, -vm/docs/supportedC4D, Cascade configurations? C4N, C3 , Lake, tab=amd-sev) C3D, Sapphire , Intel TDX T2D, Rapids, (/confidentialZ4D, Z3, Emerald computing/confidential M4N, Rapids, -vm/docs/supportedM4 , C2 , Granite configurations? A4X Rapids, tab=intel-tdx) Max, G4 AMD EPYC Milan, AMD EPYC Genoa, AMD EPYC Turin, Google Axion 

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`east5`<br>`-c`<br>Columbus,<br>Ohio, North<br>America|E2, N4 ,<br>N4D ,<br>N2 , N2D<br>C4 , C4A,<br>C4D,<br>C4N, C3 ,<br>C3D,<br>T2D,<br>M4N,<br>M4 ,<br>Z4D, Z3,<br>C2 , A4X<br>Max, G4|,<br> <br> <br> <br>Intel<br>Broadwell<br>Haswell,<br>Skylake,<br>Cascade<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>NVIDIA<br>Grace,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)||
|`us-`<br>`south`<br>`1-a`<br>Dallas, Texas,<br>North<br>America|E2, N4 ,<br>N2 , N2D<br>C4 , C4A,<br>C3 , T2D,<br>Z3, G4|,<br> <br> <br>Intel<br>Broadwell<br>Haswell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`us-`<br>`sout`<br>`1-b`|`h`<br>Dallas, Texas,<br>North<br>America|E2, N4 ,<br>N2 , N2D<br>C4 , C4A,<br>C3 , T2D,<br>A4 , A3,<br>Z3, G4|,<br> <br> <br>Intel<br>Broadwell<br>Haswell,<br>Skylake,<br>Cascade<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|
|`us-`<br>`sout`<br>`1-c`|`h`<br>Dallas, Texas,<br>North<br>America|E2, N2 ,<br>N2D, C3<br>T2D, Z3|,<br>Intel<br>Broadwell<br>Haswell,<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>AMD EPYC<br>Milan|,<br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`west1`<br>`-a`<br>The Dalles,<br>Oregon, Nort<br>America|h<br>E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, Z3,<br>M4N,<br>M4 , M3,<br>M1, C2 ,<br>C2D, A3,<br>G4, G2|,<br> <br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`west1`<br>`-b`<br>The Dalles,<br>Oregon, Nort<br>America|h<br>E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1<br>C4 , C4D<br>C4N, C3<br>C3D,<br>T2D, Z3,<br>C2 , C2D<br>M4N,<br>M4 , M3,<br>M1, A3,<br>A2, G4,<br>G2|,<br>,<br>,<br>,<br>,<br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)<br>,<br>Intel TDX<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=intel-tdx)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|ZonesLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|
|`us-`<br>`west1`<br>`-c`<br>The Dalles,<br>Oregon, Nort<br>America|h<br>E2, N4 ,<br>N4A,<br>N4D, N2<br>N2D, N1<br>C4 , C4A,<br>C4D,<br>C3D,<br>T2D, C3 ,<br>C2 , C2D<br>M4N,<br>M4 , M3,<br>A3, G4|,<br>,<br> <br> <br>,<br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)|Low CO<br>2<br>(https://cloud.google.com/susta<br>carbon#region-picker)|

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`us-`<br>`west`<br>`-a`|`2`<br>Los Angeles,<br>California,<br>North<br>America|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>C3D,<br>T2D, C2 ,<br>C2D, Z3|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>Google<br>Axion|,<br> <br> <br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`us-`<br>`west`<br>`-b`|`2`<br>Los Angeles,<br>California,<br>North<br>America|E2, N4 ,<br>N2 , N2D<br>N1, C4 ,<br>C4A, C3 ,<br>C3D,<br>T2D, M1,<br>C2|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`us-`<br>`west`<br>`-c`|`2`<br>Los Angeles,<br>California,<br>North<br>America|E2, N4 ,<br>N2 , N2D<br>N1, T2D,<br>C4 , C4A,<br>C3 , C3D,<br>M1, C2 ,<br>C2D, A4|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Haswell,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>Google<br>Axion|,<br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`us-`<br>`west`<br>`-a`|`3`<br>Salt Lake City<br>Utah, North<br>America|,<br>E2, N4 ,<br>N4D ,<br>N2 , N2D<br>N1, C4 ,<br>C4D, C3 ,<br>T2D, C2 ,<br>M3, G4|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Sandy<br>Bridge,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|Zone|sLocation|Ma<br>typ|chine<br>es|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|---|
|`us-`<br>`west`|`3`<br>Salt Lake Cit<br>Utah, North|y,<br>E2,<br>N2 ,|N4 ,<br>N2D|,<br>Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-||
|`-b`|America|N1,<br>C3 ,<br>C2 ,|C4 ,<br>T2D,<br>A4 ,|<br>Sandy<br>Bridge,<br>Broadwell|,<br>computing/confidential<br>-vm/docs/supported-<br>configurations?||
|||A2||Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|<br>tab=amd-sev)||
|`us-`|Salt Lake Cit|y,<br>E2,|N4 ,|Intel Ivy|GPUs,<br>AMD SEV||
|`west`|`3`<br>Utah, North|N2 ,|N2D|,<br>Bridge,|(/confidential-||
|`-c`|America|N1,<br>C3 ,<br>C2 ,|C4 ,<br>T2D,<br>C2D,|<br> <br>Sandy<br>Bridge,<br>Broadwell|,<br>computing/confidential<br>-vm/docs/supported-<br>configurations?||
|||A4||Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan|<br>tab=amd-sev)||

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`us-`<br>`west`<br>`-a`|`4`<br>Las Vegas,<br>Nevada,<br>North<br>America|E2, N4 ,<br>N4D, N2<br>N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, C2 ,<br>C2D, X4,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>A3, G4,<br>G2, H4D|,<br> <br> <br>Intel Ivy<br>Bridge,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Genoa,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||
|`us-`<br>`west`|`4`<br>Las Vegas,<br>Nevada,|E2, N4 ,<br>N4D, N2|,<br>Intel Ivy<br>Bridge,|GPUs,<br>AMD SEV<br>(/confidential-||
|`-b`|North<br>America|N2D, N1,<br>C4 , C4A,<br>C4D, C3 ,<br>C3D,<br>T2D, C2 ,<br>C2D, X4,<br>M4N,<br>M4 , M3,<br>M2, M1,<br>A2, G4|<br> <br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

|Zone|sLocation|Machine<br>types|CPUs|Options|CO2emissions|
|---|---|---|---|---|---|
|`us-`<br>`west`<br>`-c`|`4`<br>Las Vegas,<br>Nevada,<br>North<br>America|E2, N4 ,<br>N4D, N2<br>N2D, N1,<br>C4A, C4 ,<br>C4D, C3 ,<br>T2D, C2 ,<br>C2D, G4,<br>G2|,<br> <br> <br> <br>Intel Ivy<br>Bridge,<br>Broadwell<br>Skylake,<br>Cascade<br>Lake, Ice<br>Lake,<br>Sapphire<br>Rapids,<br>Emerald<br>Rapids,<br>Granite<br>Rapids,<br>AMD EPYC<br>Milan,<br>AMD EPYC<br>Turin,<br>Google<br>Axion|,<br> <br> <br>GPUs,<br>AMD SEV<br>(/confidential-<br>computing/confidential<br>-vm/docs/supported-<br>configurations?<br>tab=amd-sev)||

* **GPU required** : To use an N1 machine type in any of the supported `me-west1` zones, you must attach at least one NVIDIA T4 GPU to the VM.
