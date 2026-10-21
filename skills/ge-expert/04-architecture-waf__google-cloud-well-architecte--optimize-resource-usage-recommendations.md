# Architecture: Well-Architected Framework and reference designs / Google Cloud Well-Architected Framework (printable, all pillars): Optimize resource usage: Recommendations to Optimize AI and ML workloads for energy efficiency: Principle overview
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 156-193, extracted 2026-10-18

## Google Cloud Well-Architected Framework (printable, all pillars)

URL: https://docs.cloud.google.com/architecture/framework/printable

### Recommendations

To effectively optimize cloud resource usage, consider the following recommendations. 

#### Choose environment-specific resources

Each deployment environment has different requirements for availability, reliability and scalability. For example, developers might prefer an environment that lets them rapidly deploy and run applications for short durations, but might not need high availability. On the other hand, a production environment typically needs high availability. To maximize the utilization of your resources, define environmentspecific requirements based on your business needs. The following table lists examples of environment-specific requirements. 

**Note:** The requirements that are listed in this table are not exhaustive or prescriptive. They're meant to serve as examples to help you understand how requirements can vary based on the environment type. 

|Environment<br>|Requirements|
|---|---|
|Production|High availability|
||Predictable performance|
||Operational stability|
||Security with robust resources|
|Development and testing|Cost efficiency|
||Flexible infrastructure with<br>burstable capacity<br>(/architecture/hybrid-multicloud-patterns-and-practices/cloud-<br>bursting-pattern)|
||Ephemeral infrastructure when data persistence is not necessary|
|Other environments (like<br>staging and QA)|Tailored resource allocation based on environment-specific<br>requirements|

#### Choose workload-specific resources

Each of your cloud workloads might have different requirements for availability, scalability, security, and performance. To optimize costs, you need to align resource choices with the specific requirements of each workload. For example, a stateless application might not require the same level of availability or reliability as a stateful backend. The following table lists more examples of workload-specific requirements. 

**Note:** The requirements that are listed in this table are not exhaustive or prescriptive. They're meant to serve as examples to help you understand how requirements can vary based on the workload type. 

Workload Workload Resource options type requirements 

|Mission-<br>critical|Continuous<br>availability,<br>robust security,<br>and high<br>performance|Premium resources and managed services like<br>Spanner<br>(/spanner) for high availability and global consistency of data.|
|---|---|---|
|Non-critical|Cost-efficient<br>and autoscaling<br>infrastructure|Resources with basic features and ephemeral resources like<br>Spot VMs(/compute/docs/instances/spot).|
|Event-driven|Dynamic scaling<br>based on the<br>current demand<br>for capacity and<br>performance|Serverless services like<br>Cloud Run(/run) and<br>Cloud Run<br>functions<br>(https://cloud.google.com/blog/products/serverless/google-<br>cloud-functions-is-now-cloud-run-functions?e=48754805)<br>.|
|Experimental<br>workloads|Low cost and<br>flexible<br>environment for<br>rapid<br>development,<br>iteration,<br>testing, and<br>innovation|Resources with basic features, ephemeral resources like<br>Spot<br>VMs(/compute/docs/instances/spot), and sandbox environments<br>with defined spending limits.|

A benefit of the cloud is the opportunity to take advantage of the most appropriate computing power for a given workload. Some workloads are developed to take advantage of processor instruction sets, and others might not be designed in this way. Benchmark and profile your workloads accordingly. Categorize your workloads and make workload-specific resource choices (for example, choose appropriate machine families (/compute/docs/machine-resource#recommendations_for_machine_types) for Compute Engine VMs). This practice helps to optimize costs, enable innovation, and maintain the level of availability and performance that your workloads need. 

The following are examples of how you can implement this recommendation: 

- For mission-critical workloads that serve globally distributed users, consider using Spanner (/spanner). Spanner removes the need for complex database deployments by ensuring reliability and consistency of data in all regions (/docs/geography-and-regions#regions_and_zones). 

- For workloads with fluctuating load levels, use autoscaling to ensure that you don't incur costs when the load is low and yet maintain sufficient capacity to 

meet the current load. You can configure autoscaling for many Google Cloud services, including Compute Engine VMs (/compute/docs/autoscaler), Google Kubernetes Engine (GKE) clusters 

(/kubernetes-engine/docs/concepts/cluster-autoscaler), and Cloud Run (/run/docs/about-instance-autoscaling). When you set up autoscaling, you can configure maximum scaling limits to ensure that costs remain within specified budgets. 

#### Select regions based on cost requirements

For your cloud workloads, carefully evaluate the available Google Cloud regions and choose regions that align with your cost objectives. The region with lowest cost might not offer optimal latency or it might not meet your sustainability requirements. Make informed decisions about where to deploy your workloads to achieve the desired balance. You can use the Google Cloud Region Picker (https://cloud.withgoogle.com/region-picker/) to understand the trade-offs between cost, sustainability, latency, and other factors. 

#### Use built-in cost optimization options

Google Cloud products provide built-in features to help you optimize resource usage and control costs. The following table lists examples of cost optimization features that you can use in some Google Cloud products: 

- Product Cost optimization feature Compute Automatically add or remove VMs based on the current load by using autoscaling Engine (/compute/docs/autoscaler). Avoid overprovisioning by creating and using custom machine types (/compute/docs/instances/creating-instance-with-custom-machine-type) that match your workload's requirements. 

   - For non-critical or fault-tolerant workloads, reduce costs by using Spot VMs (/compute/docs/instances/spot). 

   - In development environments, reduce costs by limiting the run time (/compute/docs/instances/limit-vm-runtime) of VMs or by suspending (/compute/docs/instances/suspend-resume-instance) or stopping (/compute/docs/instances/stop-start-instance) VMs when you don't need them. 

- GKE Automatically adjust the size of GKE clusters based on the current load by using cluster autoscaler (/kubernetes-engine/docs/concepts/cluster-autoscaler). 

   - Automatically create and manage node pools based on workload requirements and ensure optimal resource utilization by using node auto-provisioning (/kubernetes-engine/docs/how-to/node-auto-provisioning). 

Cloud Automatically transition data to lower-cost storage classes based on the age of Storage data or based on access patterns by using Object Lifecycle Management (/storage/docs/lifecycle). 

   - Dynamically move data to the most cost-effective storage class based on usage patterns by using Autoclass (/storage/docs/autoclass). 

- BigQuery Reduce query processing costs for steady-state workloads by using capacity-based pricing. (https://cloud.google.com/bigquery/pricing#capacity_compute_analysis_pricing) Optimize query performance and costs by using partitioning and clustering techniques. 

Google Reduce VMware costs by using cost-optimization strategies Cloud (/vmware-engine/docs/best-practices-costs) like CUDs, optimizing storage VMware consumption, and rightsizing ESXi clusters. Engine 

#### Optimize resource sharing

To maximize the utilization of cloud resources, you can deploy multiple applications or services on the same infrastructure, while still meeting the security and other requirements of the applications. For example, in development and testing environments, you can use the same cloud infrastructure to test all the components of an application. For the production environment, you can deploy each component on a separate set of resources to limit the extent of impact in case of incidents. 

The following are examples of how you can implement this recommendation: 

- Use a single Cloud SQL (/sql) instance for multiple non-production environments. 

- Enable multiple development teams to share a GKE cluster by using the fleet team management (/kubernetes-engine/fleet-management/docs/team-management) feature in GKE with appropriate access controls. 

- Use GKE Autopilot (/kubernetes-engine/docs/concepts/autopilot-overview) to take advantage of cost-optimization techniques like bin packing and autoscaling that GKE implements by default. 

- For AI and ML workloads, save GPU costs by using GPU-sharing strategies (/kubernetes-engine/docs/concepts/timesharing-gpus#what-is-gpu-sharing) like multiinstance GPUs, time-sharing GPUs, and NVIDIA MPS. 

#### Develop and maintain reference architectures

Create and maintain a repository of reference architectures that are tailored to meet the requirements of different deployment environments and workload types. To streamline the design and implementation process for individual projects, the blueprints can be centrally managed by a team like a Cloud Center of Excellence 

(https://cloud.google.com/resources/cloud-teams) (CCoE). Project teams can choose suitable blueprints based on clearly defined criteria, to ensure architectural consistency and adoption of best practices. For requirements that are unique to a project, the project team and the central architecture team should collaborate to design new reference architectures. You can share the reference architectures across the organization to foster knowledge sharing and expand the repository of available solutions. This approach ensures consistency, accelerates development, simplifies decision-making, and promotes efficient resource utilization. 

Review the reference architectures (/architecture/all-reference-architectures) provided by Google for various use cases and technologies. These reference architectures incorporate best practices for resource selection, sizing, configuration, and deployment. By using these reference architectures, you can accelerate your development process and achieve cost savings from the start. 

#### Enforce cost discipline by using organization policies

Consider using organization policies 

(/resource-manager/docs/organization-policy/overview) to limit the available Google Cloud locations and products that team members can use. These policies help to ensure that teams adhere to cost-effective solutions and provision resources in locations that are aligned with your cost optimization goals. 

#### Estimate realistic budgets and set financial boundaries

Develop detailed budgets for each project, workload, and deployment environment. Make sure that the budgets cover all aspects of cloud operations, including infrastructure costs, software licenses, personnel, and anticipated growth. To prevent overspending and ensure alignment with your financial goals, establish clear spending limits or thresholds for projects, services, or specific resources. Monitor cloud spending regularly against these limits. You can use proactive quota alerts (/docs/quotas/set-up-quota-alerts) to identify potential cost overruns early and take timely corrective action. 

In addition to setting budgets, you can use quotas (/docs/quotas/view-manage) and limits to help enforce cost discipline and prevent unexpected spikes in spending. You can exercise granular control over resource consumption by setting quotas at various levels, including projects, services, and even specific resource types. 

The following are examples of how you can implement this recommendation: 

- **Project-level quotas** : Set spending limits or resource quotas at the project level to establish overall financial boundaries and control resource consumption across all the services within the project. 

- **Service-specific quotas** : Configure quotas for specific Google Cloud services like Compute Engine or BigQuery to limit the number of instances, CPUs, or storage capacity that can be provisioned. 

- **Resource type-specific quotas** : Apply quotas to individual resource types like Compute Engine VMs, Cloud Storage buckets, Cloud Run instances, or GKE nodes to restrict their usage and prevent unexpected cost overruns. 

- **Quota alerts** : Get notifications when your quota usage (at the project level) reaches a percentage of the maximum value. 

By using quotas and limits in conjunction with budgeting and monitoring, you can create a proactive and multi-layered approach to cost control. This approach helps to ensure that your cloud spending remains within defined boundaries and aligns with your business objectives. Remember, these cost controls are not permanent or rigid. To ensure that the cost controls remain aligned with current industry standards and reflect your evolving business needs, you must review the controls regularly and adjust them to include new technologies and best practices. 

## Optimize continuously

This principle in the cost optimization pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you optimize the cost of your cloud deployments based on constantly changing and evolving business goals. 

As your business grows and evolves, your cloud workloads need to adapt to changes in resource requirements and usage patterns. To derive maximum value from your cloud spending, you must maintain cost-efficiency while continuing to support business objectives. This requires a proactive and adaptive approach that focuses on continuous improvement and optimization. 

### Principle overview

To optimize cost continuously, you must proactively monitor and analyze your cloud environment and make suitable adjustments to meet current requirements. Focus your monitoring efforts on key performance indicators (KPIs) that directly affect your end users' experience, align with your business goals, and provide insights for continuous improvement. This approach lets you identify and address inefficiencies, adapt to changing needs, and continuously align cloud spending with strategic business goals. To balance comprehensive observability with cost effectiveness, understand the costs and benefits of monitoring resource usage and use appropriate process-improvement and optimization strategies. 

### Recommendations

To effectively monitor your Google Cloud environment and optimize cost continuously, consider the following recommendations. 

#### Focus on business-relevant metrics

Effective monitoring starts with identifying the metrics that are most important for your business and customers. These metrics include the following: 

- **User experience metrics** : Latency, error rates, throughput, and customer satisfaction metrics are useful for understanding your end users' experience when using your applications. 

- **Business outcome metrics** : Revenue, customer growth, and engagement can be correlated with resource usage to identify opportunities for cost optimization. 

- **DevOps Research & Assessment (DORA)** (https://dora.dev) **metrics** : Metrics like deployment frequency, lead time for changes, change failure rate, and time to restore provide insights into the efficiency and reliability of your software delivery process. By improving these metrics, you can increase productivity, reduce downtime, and optimize cost. 

- **Site Reliability Engineering (SRE)** (https://sre.google) **metrics** : Error budgets help teams to quantify and manage the acceptable level of service disruption. By establishing clear expectations for reliability, error budgets empower teams to innovate and deploy changes more confidently, knowing their safety margin. This proactive approach promotes a balance between innovation and stability, helping prevent excessive operational costs associated with major outages or prolonged downtime. 

#### Use observability for resource optimization

The following are recommendations to use observability to identify resource bottlenecks and underutilized resources in your cloud deployments: 

- **Monitor resource utilization** : Use resource utilization metrics to identify Google Cloud resources that are underutilized. For example, use metrics like CPU and memory utilization to identify idle VM resources 

(/monitoring/agent/process-metrics#view_performance_metrics_for_top_resourceconsuming_vms) . For Google Kubernetes Engine (GKE), you can view a detailed breakdown of costs (/kubernetes-engine/docs/how-to/cost-allocations) and cost-related optimization metrics (/kubernetes-engine/docs/how-to/cost-optimization-metrics). For Google Cloud VMware Engine, review resource utilization 

- (https://cloud.google.com/blog/topics/cost-management/cost-optimization-of-googlecloud-vmware-engine-deployments) 

to optimize CUDs, storage consumption, and ESXi right-sizing. 

- **Use cloud recommendations** : Active Assist (/solutions/active-assist) is a portfolio of intelligent tools that help you optimize your cloud operations. These tools provide actionable recommendations to reduce costs, increase performance, improve security and even make sustainability-focused decisions. For example, VM rightsizing insights (/compute/docs/instance-groups/apply-machine-type-recommendations-managedinstance-groups) 

can help to optimize resource allocation and avoid unnecessary spending. 

- **Correlate resource utilization with performance** : Analyze the relationship between resource utilization and application performance to determine whether you can downgrade to less expensive resources without affecting the user experience. 

#### Balance troubleshooting needs with cost

Detailed observability data can help with diagnosing and troubleshooting issues. However, storing excessive amounts of observability data or exporting unnecessary data to external monitoring tools can lead to unnecessary costs. For efficient troubleshooting, consider the following recommendations: 

- **Collect sufficient data for troubleshooting** : Ensure that your monitoring solution captures enough data to efficiently diagnose and resolve issues when they arise. This data might include logs, traces, and metrics at various levels of granularity. 

- **Use sampling and aggregation** : Balance the need for detailed data with cost considerations by using sampling and aggregation techniques. This approach lets you collect representative data without incurring excessive storage costs. 

- **Understand the pricing models of your monitoring tools and services** : Evaluate different monitoring solutions and choose options that align with your project's specific needs, budget, and usage patterns. Consider factors like data volume, retention requirements, and the required features when making your selection. 

- **Regularly review your monitoring configuration** : Avoid collecting excessive data by removing unnecessary metrics or logs. 

#### Tailor data collection to roles and set role-specific retention policies

Consider the specific data needs of different roles. For example, developers might primarily need access to traces and application-level logs, whereas IT administrators might focus on system logs and infrastructure metrics. By tailoring data collection, you can reduce unnecessary storage costs and avoid overwhelming users with irrelevant information. 

Additionally, you can define retention policies based on the needs of each role and any regulatory requirements. For example, developers might need access to detailed logs for a shorter period, while financial analysts might require longer-term data. 

#### Consider regulatory and compliance requirements

In certain industries, regulatory requirements mandate data retention. To avoid legal and financial risks, you need to ensure that your monitoring and data retention practices help you adhere to relevant regulations. At the same time, you need to maintain cost efficiency. Consider the following recommendations: 

- Determine the specific data retention requirements for your industry or region, and ensure that your monitoring strategy meets the requirements of those requirements. 

- Implement appropriate data archival and retrieval mechanisms to meet audit and compliance needs while minimizing storage costs. 

#### Implement smart alerting

Alerting helps to detect and resolve issues in a timely manner. However, a balance is necessary between an approach that keeps you informed, and one that overwhelms you with notifications. By designing intelligent alerting systems, you can prioritize critical issues that have higher business impact. Consider the following recommendations: 

**Prioritize issues that affect customers** : Design alerts that trigger rapidly for issues that directly affect the customer experience, like website outages, slow response times, or transaction failures. 

- **Tune for temporary problems** : Use appropriate thresholds and delay mechanisms to avoid unnecessary alerts for temporary problems or selfhealing system issues that don't affect customers. 

- **Customize alert severity** : Ensure that the most urgent issues receive immediate attention by differentiating between critical and noncritical alerts. 

- **Use notification channels wisely** : Choose appropriate channels for alert notifications (email, SMS, or paging) based on the severity and urgency of the alerts. 

## Well-Architected Framework: Performance optimization pillar

This pillar in the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to optimize the performance of workloads in Google Cloud. 

This document is intended for architects, developers, and administrators who plan, design, deploy, and manage workloads in Google Cloud. 

The recommendations in this pillar can help your organization to operate efficiently, improve customer satisfaction, increase revenue, and reduce cost. For example, when the backend processing time of an application decreases, users experience faster response times, which can lead to higher user retention and more revenue. 

The performance optimization process can involve a trade-off between performance and cost. However, optimizing performance can sometimes help you reduce costs.  For example, when the load increases, autoscaling can help to provide predictable performance by ensuring that the system resources aren't overloaded. Autoscaling also helps you to reduce costs by removing unused resources during periods of low load. 

Performance optimization is a continuous process, not a one-time activity. The following diagram shows the stages in the performance optimization process: 

The performance optimization process is an ongoing cycle that includes the following stages: 

1. **Define requirements** : Define granular performance requirements for each layer of the application stack before you design and develop your applications. To plan resource allocation, consider the key workload characteristics and performance expectations. 

2. **Design and deploy** : Use elastic and scalable design patterns that can help you meet your performance requirements. 

3. **Monitor and analyze** : Monitor performance continually by using logs, tracing, metrics, and alerts. 

4. **Optimize** : Consider potential redesigns as your applications evolve. Rightsize cloud resources and use new features to meet changing performance requirements. 

As shown in the preceding diagram, continue the cycle of monitoring, reassessing requirements, and adjusting the cloud resources. 

For performance optimization principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Performance optimization 

(/architecture/framework/perspectives/ai-ml/performance-optimization) in the WellArchitected Framework. 

### Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the `google-cloud-waf-performance-` 

```
optimization
```

(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-performanceoptimization) 

skill, which is available in the Google Agent Skills repository in GitHub. 

To install the skill, run the following command in your agent's client or terminal: 

```
npx skills add google/skills --skill google-cloud-waf-performance-optimization
```

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global). 

**Note:** If **`npx`** is not available in your environment, install Node.js (https://nodejs.org/en/download), which includes **`npm`** and **`npx`** . 

### Core principles

The recommendations in the performance optimization pillar of the WellArchitected Framework are mapped to the following core principles: 

Plan resource allocation 

- (/architecture/framework/performance-optimization/plan-resource-allocation) 

- Take advantage of elasticity 

- (/architecture/framework/performance-optimization/elasticity) 

- Promote modular design 

- (/architecture/framework/performance-optimization/promote-modular-design) 

Continuously monitor and improve performance 

- (/architecture/framework/performance-optimization/continuously-monitor-and-improveperformance) 

### Contributors

Authors: 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect 

- Gary Harmson (https://www.linkedin.com/in/garyharmson) | Principal Architect 

- Luis Urena (https://www.linkedin.com/in/urena-luis) | Developer Relations Engineer 

- Zach Seils (https://www.linkedin.com/in/zachseils) | Networking Specialist 

Other contributors: 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Jose Andrade (https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

- Nicolas Pintaux (https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist 

- Ryan Cox (https://www.linkedin.com/in/ryanlcox) | Principal Architect 

- Radhika Kanakam (https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework 

- Samantha He (https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer 

- Wade Holmes (https://www.linkedin.com/in/wholmes) | Global Solutions Director 

## Plan resource allocation

This principle in the performance optimization pillar of the Google Cloud WellArchitected Framework (/architecture/framework) provides recommendations to help you plan resources for your workloads in Google Cloud. It emphasizes the importance of defining granular requirements before you design and develop applications for cloud deployment or migration. 

### Principle overview

To meet your business requirements, it's important that you define the performance requirements for your applications, before design and development. Define these requirements as granularly as possible for the application as a whole and for each layer of the application stack. For example, in the storage layer, you must consider the throughput and I/O operations per second (IOPS) that the applications need. 

From the beginning, plan application designs with performance and scalability in mind. Consider factors such as the number of users, data volume, and potential growth over time. 

Performance requirements for each workload vary and depend on the type of workload. Each workload can contain a mix of component systems and services that have unique sets of performance characteristics. For example, a system that's responsible for periodic batch processing of large datasets has different performance demands than an interactive virtual desktop solution. Your optimization strategies must address the specific needs of each workload. 

Select services and features that align with the performance goals of each workload. For performance optimization, there's no one-size-fits-all solution. When you optimize each workload, the entire system can achieve optimal performance and efficiency. 

Consider the following workload characteristics that can influence your performance requirements: 

- **Deployment archetype** : The deployment archetype (/architecture/deployment-archetypes) that you select for an application can influence your choice of products and features, which then determine the performance that you can expect from your application. 

- **Resource placement** : When you select a Google Cloud region 

- (/docs/geography-and-regions) for your application resources, we recommend that you prioritize low latency for end users, adhere to data-locality regulations, and ensure the availability of required Google Cloud products and services. 

- **Network connectivity** : Choose networking services that optimize data access and content delivery. Take advantage of Google Cloud's global network, high-speed backbones, interconnect locations, and caching services. 

- **Application hosting options** : When you select a hosting platform, you must evaluate the performance advantages and disadvantages of each option. For example, consider bare metal, virtual machines, containers, and serverless platforms. 

**Storage strategy** : Choose an optimal storage strategy 

- (/architecture/storage-advisor) that's based on your performance requirements. 

- **Resource configurations** : The machine type, IOPS, and throughput can have a significant impact on performance. Additionally, early in the design phase, you must consider appropriate security capabilities and their impact on resources. When you plan security features, be prepared to accommodate the necessary performance trade-offs to avoid any unforeseen effects. 

### Recommendations

To ensure optimal resource allocation, consider the recommendations in the following sections. 

#### Configure and manage quotas

Ensure that your application uses only the necessary resources, such as memory, storage, and processing power. Over-allocation can lead to unnecessary expenses, while under-allocation might result in performance degradation. 

To accommodate elastic scaling and to ensure that adequate resources are available, regularly monitor the capacity of your quotas. Additionally, track quota usage to identify potential scaling constraints or over-allocation issues, and then make informed decisions about resource allocation. 

#### Educate and promote awareness

Inform your users about the performance requirements and provide educational resources (https://www.cloudskillsboost.google/course_templates/734) about effective performance management techniques. 

To evaluate progress and to identify areas for improvement, regularly document the target performance and the actual performance. Load test your application to find potential breakpoints and to understand how you can scale the application. 

#### Monitor performance metrics

Use Cloud Monitoring (/monitoring/docs/monitoring-overview) to analyze trends in performance metrics, to analyze the effects of experiments, to define alerts for critical metrics, and to perform retrospective analyses. 

Active Assist (/recommender/docs/whatis-activeassist) is a set of tools that can provide insights and recommendations to help optimize resource utilization. These recommendations can help you to adjust resource allocation and improve performance. 

## Take advantage of elasticity

This principle in the performance optimization pillar of the Google Cloud WellArchitected Framework (/architecture/framework) provides recommendations to help you incorporate elasticity, which is the ability to adjust resources dynamically based on changes in workload requirements. 

Elasticity allows different components of a system to scale independently. This targeted scaling can help improve performance and cost efficiency by allocating resources precisely where they're needed, without over provisioning or under provisioning your resources. 

### Principle overview

The performance requirements of a system directly influence when and how the system scales vertically or scales horizontally. You need to evaluate the system's capacity and determine the load that the system is expected to handle at baseline. Then, you need to determine how you want the system to respond to increases and decreases in the load. 

When the load increases, the system must scale out horizontally, scale up vertically, or both. For horizontal scaling, add replica nodes to ensure that the system has sufficient overall capacity to fulfill the increased demand. For vertical scaling, replace the application's existing components with components that contain more capacity, more memory, and more storage. 

When the load decreases, the system must scale down (horizontally, vertically, or both). 

Define the _circumstances_ in which the system scales up or scales down. Plan to manually scale up systems for known periods of high traffic. Use tools like autoscaling, which responds to increases or decreases in the load. 

### Recommendations

To take advantage of elasticity, consider the recommendations in the following sections. 

#### Plan for peak load periods

You need to plan an efficient scaling path for known events, such as expected periods of increased customer demand. 

Consider scaling up your system ahead of known periods of high traffic. For example, if you're a retail organization, you expect demand to increase during seasonal sales. We recommend that you manually scale up or scale out your systems before those sales to ensure that your system can immediately handle the increased load or immediately adjust existing limits. Otherwise, the system might take several minutes to add resources in response to real-time changes. Your application's capacity might not increase quickly enough and cause some users to experience delays. 

For unknown or unexpected events, such as a sudden surge in demand or traffic, you can use autoscaling features to trigger elastic scaling that's based on metrics. These metrics can include CPU utilization, load balancer serving capacity, latency, and even custom metrics that you define in Cloud Monitoring 

(/monitoring/docs/monitoring-overview). 

For example, consider an application that runs on a Compute Engine (/compute/docs/overview) managed instance group (MIG). This application has a requirement that each instance performs optimally until the average CPU utilization reaches 75%. In this example, you might define an autoscaling policy 

(/compute/docs/autoscaler#autoscaling_policy) that creates more instances when the CPU utilization reaches the threshold. These newly-created instances help absorb the load, which helps ensure that the average CPU utilization remains at an optimal rate until the maximum number of instances that you've configured for the MIG is reached. When the demand decreases, the autoscaling policy removes the instances that are no longer needed. 

Plan resource slot reservations in BigQuery 

(/bigquery/docs/reservations-intro#reservations) or adjust the limits for autoscaling configurations in Spanner by using the managed autoscaler 

(/spanner/docs/managed-autoscaler). 

#### Use predictive scaling

If your system components include Compute Engine, you must evaluate whether predictive autoscaling (/compute/docs/autoscaler#predictive_mode) is suitable for your workload. Predictive autoscaling forecasts the future load based on your metrics' historical trends—for example, CPU utilization. Forecasts are recomputed every few minutes, so the autoscaler rapidly adapts its forecast to very recent changes in load. Without predictive autoscaling, an autoscaler can only scale a group reactively, based on observed real-time changes in load. Predictive autoscaling works with both real-time data and historical data to respond to both the current and the forecasted load. 

#### Implement serverless architectures

Consider implementing a serverless architecture with serverless services that are inherently elastic, such as the following: 

- Cloud Run (/run/docs) 

- Cloud Run functions (/functions/docs) 

- BigQuery (/bigquery/docs) 

- Spanner (/spanner/docs) 

- Eventarc (/eventarc/docs) 

- Workflows (/workflows/docs) 

- Pub/Sub (/pubsub/docs) 

Unlike autoscaling in other services that require fine-tuning rules (for example, Compute Engine), serverless autoscaling is instant and can scale down to zero resources. 

#### Use Autopilot mode for Kubernetes

For complex applications that require greater control over Kubernetes, consider Autopilot mode in Google Kubernetes Engine (GKE) 

(/kubernetes-engine/docs/concepts/autopilot-overview). Autopilot mode provides automation and scalability by default. GKE automatically scales nodes and resources based on traffic. GKE manages nodes, creates new nodes for your applications, and configures automatic upgrades and repairs. 

## Promote modular design

This principle in the performance optimization pillar of the Google Cloud WellArchitected Framework (/architecture/framework) provides recommendations to help you promote a modular design. Modular components and clear interfaces can enable flexible scaling, independent updates, and future component separation. 

### Principle overview

Understand the dependencies between the application components and the system components to design a scalable system. 

Modular design enables flexibility and resilience, regardless of whether a monolithic or microservices architecture was initially deployed. By decomposing the system into well-defined, independent modules with clear interfaces, you can scale individual components to meet specific demands. 

Targeted scaling can help optimize resource utilization and reduce costs in the following ways: 

- Provisions only the necessary resources to each component, and allocates fewer resources to less-demanding components. 

- Adds more resources during high-traffic periods to maintain the user experience. 

Removes under-utilized resources without compromising performance. 

Modularity also enhances maintainability. Smaller, self-contained units are easier to understand, debug, and update, which can lead to faster development cycles and reduced risk. 

While modularity offers significant advantages, you must evaluate the potential performance trade-offs. The increased communication between modules can introduce latency and overhead. Strive for a balance between modularity and performance. A highly modular design might not be universally suitable. When performance is critical, a more tightly coupled approach might be appropriate. 

System design is an iterative process (/architecture/framework/performance-optimization) , in which you continuously review and refine your modular design. 

### Recommendations

To promote modular designs, consider the recommendations in the following sections. 

#### Design for loose coupling

Design a loosely coupled architecture 

(/architecture/microservices-architecture-refactoring-monoliths). Independent components with minimal dependencies can help you build scalable and resilient applications 

(/architecture/scalable-and-resilient-apps). As you plan the boundaries for your services, you must consider the availability and scalability requirements. For example, if one component has requirements that are different from your other components, you can design the component as a standalone service. Implement a plan for graceful failures for less-important subprocesses or services that don't impact the response time of the primary services. 

#### Design for concurrency and parallelism

Design your application to support multiple tasks concurrently, like processing multiple user requests or running background jobs while users interact with your system. Break large tasks into smaller chunks that can be processed at the same time by multiple service instances. Task concurrency lets you use features like autoscaling to increase the resource allocation in products like the following: 

- Compute Engine (/compute/docs/autoscaler) 

- GKE (/spanner/docs/autoscaling-overview) 

- BigQuery (/bigquery/docs/slots-autoscaling-intro) 

- Spanner (/spanner/docs/autoscaling-overview) 

#### Balance modularity for flexible resource allocation

Where possible, ensure that each component uses only the necessary resources (like memory, storage, and processing power) for specific operations. Resource over-allocation can result in unnecessary costs, while resource under-allocation can compromise performance. 

#### Use well-defined interfaces

Ensure modular components communicate effectively through clear, standardized interfaces (like APIs and message queues) to reduce overhead from translation layers or from extraneous traffic. 

#### Use stateless models

A stateless model can help ensure that you can handle each request or interaction with the service independently from previous requests. This model facilitates scalability and recoverability, because you can grow, shrink, or restart the service without losing the data necessary for in-progress requests or processes. 

#### Choose complementary technologies

Choose technologies that complement the modular design. Evaluate programming languages, frameworks, and databases for their modularity support. 

For more information, see the following resources: 

Re-architecting to cloud native 

- (https://cloud.google.com/resources/rearchitecting-to-cloud-native) 

- Introduction to microservices (/architecture/microservices-architecture-introduction) 

## Continuously monitor and improve performance

This principle in the performance optimization pillar of the Google Cloud WellArchitected Framework (/architecture/framework) provides recommendations to help you continuously monitor and improve performance. 

After you deploy applications, continuously monitor their performance by using logs, tracing, metrics, and alerts. As your applications grow and evolve, you can use the trends in these data points to re-assess your performance requirements. You might eventually need to redesign parts of your applications to maintain or improve their performance. 

### Principle overview

The process of continuous performance improvement requires robust monitoring tools and strategies. Cloud observability tools can help you to collect key performance indicators (KPIs) such as latency, throughput, error rates, and resource utilization. Cloud environments offer a variety of methods to conduct granular performance assessments across the application, the network, and the end-user experience. 

Improving performance is an ongoing effort that requires a multi-faceted approach. The following key mechanisms and processes can help you to boost performance: 

- To provide clear direction and help track progress, define performance objectives that align with your business goals. Set SMART goals: specific, measurable, achievable, relevant, and time-bound. 

- To measure performance and identify areas for improvement, gather KPI metrics. 

- To continuously monitor your systems for issues, use visualized workflows in monitoring tools. Use architecture process mapping techniques to identify redundancies and inefficiencies. 

- To create a culture of ongoing improvement, provide training and programs that support your employees' growth. 

- To encourage proactive and continuous improvement, incentivize your employees and customers to provide ongoing feedback about your application's performance. 

### Recommendations

To promote modular designs, consider the recommendations in the following sections. 

#### Define clear performance goals and metrics

Define clear performance objectives that align with your business goals. This requires a deep understanding of your application's architecture and the performance requirements of each application component. 

As a priority, optimize the most critical components that directly influence your core business functions and user experience. To help ensure that these components continue to run efficiently and meet your business needs, set specific and measurable performance targets. These targets can include response times, error rates, and resource utilization thresholds. 

This proactive approach can help you to identify and address potential bottlenecks, optimize resource allocation, and ultimately deliver a seamless and highperforming experience for your users. 

#### Monitor performance

Continuously monitor your cloud systems for performance issues and set up alerts for any potential problems. Monitoring and alerts can help you to catch and fix issues before they affect users. Application profiling can help to identify bottlenecks and can help to optimize resource use. 

You can use tools that facilitate effective troubleshooting and network optimization. Use Google Cloud Observability (/stackdriver/docs) to identify areas that have high CPU consumption, memory consumption, or network consumption. These capabilities can help developers improve efficiency, reduce costs, and enhance the user experience. Network Intelligence Center 

(/network-intelligence-center/docs/overview) shows visualizations of the topology of your network infrastructure, and can help you to identify high-latency paths. 

#### Incentivize continuous improvement

Create a culture of ongoing improvement that can benefit both the application and the user experience. 

Provide your employees with training and development opportunities that enhance their skills and knowledge in performance techniques across cloud services. Establish a community of practice (CoP) and offer mentorship and coaching programs to support employee growth. 

To prevent _reactive_ performance management and encourage proactive performance management, encourage ongoing feedback from your employees, your customers, and your stakeholders. You can consider gamifying the process by tracking KPIs on performance and presenting those metrics to teams on a frequent basis in the form of a league table. 

To understand your performance and user happiness over time, we recommend that you measure user feedback quantitatively and qualitatively. The HEART (https://dl.acm.org/doi/10.1145/1753326.1753687) framework can help you capture user feedback across five categories: 

- Happiness 

- Engagement 

- Adoption 

- Retention 

- Task success 

By using such a framework, you can incentivize engineers with data-driven feedback, user-centered metrics, actionable insights, and a clear understanding of goals. 

## Well-Architected Framework: Sustainability pillar

The sustainability pillar in the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to design, build, and manage workloads in Google Cloud that are energy-efficient and carbon-aware. 

The target audience for this document includes decision-makers, architects, administrators, developers, and operators who design, build, deploy, and maintain 

workloads in Google Cloud. 

Architectural and operational decisions have a significant impact on the energy usage, water impact, and carbon footprint that's driven by your workloads in the cloud. Every workload, whether it's a small website or a large-scale ML model, consumes energy and contributes to carbon emissions and water resource intensity. When you integrate sustainability into your cloud architecture and design process, you build systems that are efficient, cost-effective, _and_ environmentally sustainable. A sustainable architecture is resilient and optimized, which creates a positive feedback loop of higher efficiency, lower cost, and lower environmental impact. 

### Sustainable by design: Holistic business outcomes

Sustainability isn't a trade-off against other core business objectives; sustainability practices help to accelerate your other business objectives. Architecture choices that prioritize low-carbon resources and operations help you build systems that are also faster, cheaper, and more secure. Such systems are considered to be _sustainable by design_ , where optimizing for sustainability leads to overall positive outcomes for performance, cost, security, resilience, and user experience. 

#### Performance optimization

Systems that are optimized for performance 

(/architecture/framework/performance-optimization) inherently use fewer resources. An efficient application that completes a task faster requires compute resources for a shorter duration. Therefore, the underlying hardware consumes less kilowatt-hours (kWh) of energy. Optimized performance also leads to lower latency and better user experience. Time and energy aren't wasted by resources waiting on inefficient processes. When you use specialized hardware (for example, GPUs and TPUs), adopt efficient algorithms, and maximize parallel processing, you improve performance _and_ reduce the carbon footprint of your cloud workload. 

#### Cost optimization

Cloud operational expenditure depends on resource usage. Due to this direct correlation, when you continuously optimize cost 

(/architecture/framework/cost-optimization), you also reduce energy consumption and carbon emissions. When you right-size VMs, implement aggressive autoscaling, archive old data, and eliminate idle resources, you reduce resource usage and cloud costs. You also reduce the carbon footprint of your systems, because the data centers consume less energy to run your workloads. 

#### Security and resilience

Security (/architecture/framework/security) and reliability 

(/architecture/framework/reliability) are prerequisites for a sustainable cloud environment. A compromised system—for example, a system that's affected by a denial of service (DoS) attack or an unauthorized data breach—can dramatically increase resource consumption. These incidents can trigger massive spikes in traffic, create runaway compute cycles for mitigation, and necessitate lengthy, high-energy operations for forensic analysis, cleanup, and data restoration. Strong security measures can help to prevent unnecessary spikes in resource usage, so that your operations remain stable, predictable, and energy-efficient. 

#### User experience

Systems that prioritize efficiency, performance, accessibility, and minimal use of data can help to reduce energy usage by end users. An application that loads a smaller model or processes less data to deliver results faster helps to reduce the energy that's consumed by network devices and end-user devices. This reduction in energy usage particularly benefits users who have limited bandwidth or who use older devices. Further, sustainable architecture helps to minimize planetary harm and demonstrates your commitment to socially responsible technology. 

### Sustainability value of migrating to the cloud

Migrating on-premises workloads to the cloud can help to reduce your organization's environmental footprint. The transition to cloud infrastructure can reduce energy usage and associated emissions by 1.4 to 2 times 

(https://research.google/blog/good-news-about-the-carbon-footprint-of-machine-learningtraining/) 

when compared to typical on-premises deployments. Cloud data centers are modern, custom-designed facilities that are built for high power usage effectiveness (PUE) (https://en.wikipedia.org/wiki/Power_usage_effectiveness). Older onpremises data centers often lack the scale that's necessary to justify investments in advanced cooling and power distribution systems. 

### Shared responsibility and shared fate

Shared responsibilities and shared fate on Google Cloud 

(/architecture/framework/security/shared-responsibility-shared-fate) describes how security for cloud workloads is a shared responsibility between Google and you, the customer. This shared responsibility model also applies to sustainability. 

Google is responsible for the sustainability _of_ Google Cloud, which means the energy efficiency and water stewardship of our data centers, infrastructure, and core services. We invest continuously in renewable energy, climate-conscious cooling, and hardware optimization. For more information about Google's sustainability strategy and progress, see Google Sustainability 2025 Environmental Report (https://sustainability.google/google-2025-environmental-report/). 

You, the customer, are responsible for sustainability _in_ the cloud, which means optimizing your workloads to be energy efficient. For example, you can right-size resources, use serverless services that scale to zero, and manage data lifecycles effectively. 

We also advocate a shared fate model: sustainability isn't just a division of tasks but a collaborative partnership between you and Google to reduce the environmental footprint for the entire ecosystem. 

### Use AI for business impact

The sustainability pillar of the Well-Architected Framework (this document) includes guidance to help you design sustainable AI systems. However, a comprehensive sustainability strategy extends beyond the environmental impact of AI workloads. 

The strategy should include ways to use AI to optimize operations and create new business value. 

AI serves as a catalyst for sustainability by transforming vast datasets into actionable insights. It enables organizations to transition from reactive compliance to proactive optimization, such as in the following areas: 

- **Operational efficiency** : Streamline operations through improved inventory management, supply chain optimization, and intelligent energy management. 

- **Transparency and risk** : Use data for granular supply chain transparency, regulatory compliance, and climate risk modeling. 

**Value and growth** : Develop new revenue streams in sustainable finance and recommerce (https://en.wikipedia.org/wiki/Recommerce). 

Google offers the following products and features to help you derive insights from data and build capabilities for a sustainable future: 

- Google Earth AI (https://ai.google/earth-ai/): Uses planetary-scale geospatial data to analyze environmental changes and monitor supply chain impacts. 

- WeatherNext (https://deepmind.google/science/weathernext/): Provides advanced weather forecasting and climate risk analytics to help you build resilience against climate volatility. 

- Geospatial insights with Google Earth 

- (https://mapsplatform.google.com/solutions/visualize-data/): Uses geospatial data to add rich contextual data to locations, which enables smarter site selection, resource planning, and operations. 

- Google Maps routes optimization 

- (https://mapsplatform.google.com/maps-products/#routes-section): Optimizes logistics and delivery routes to increase efficiency and reduce fuel consumption and transportation emissions. 

### Collaborations with partners and customers

Google Cloud and TELUS (https://www.telus.com) have partnered to advance cloud sustainability by migrating workloads to Google's carbon-neutral infrastructure and 

leveraging data analytics to optimize operations. This collaboration provides social and environmental benefits through initiatives like smart-city technology, which uses real-time data to reduce traffic congestion and carbon emissions across municipalities in Canada. For more information about this collaboration, see Google Cloud and TELUS collaborate for sustainability 

(https://cloud.google.com/blog/topics/sustainability/google-cloud-and-telus-collaborate-forsustainability) 

### Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the `google-cloud-waf-sustainability` 

(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-sustainability) skill, which is available in the Google Agent Skills repository in GitHub. 

To install the skill, run the following command in your agent's client or terminal: 

```
npx skills add google/skills --skill google-cloud-waf-sustainability
```

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global). 

**Note:** If **`npx`** is not available in your environment, install Node.js (https://nodejs.org/en/download), which includes **`npm`** and **`npx`** . 

### Core principles

The recommendations in the sustainability pillar of the Well-Architected Framework are mapped to the following core principles: 

Use regions that consume low-carbon energy 

(/architecture/framework/sustainability/low-carbon-regions) 

- Optimize AI and ML workloads for energy efficiency 

- (/architecture/framework/sustainability/ai-ml-energy-efficiency) 

- Optimize resource usage for sustainability 

- (/architecture/framework/sustainability/optimize-resource-usage) 

- Develop energy-efficient software 

- (/architecture/framework/sustainability/energy-efficient-software) 

- Optimize data and storage for sustainability 

- (/architecture/framework/sustainability/optimize-storage) 

- Continuously measure and improve sustainability 

- (/architecture/framework/sustainability/continuously-measure-improve) 

- Promote a culture of sustainability (/architecture/framework/sustainability/culture) 

- Align sustainability practices with industry guidelines 

- (/architecture/framework/sustainability/industry-guidelines) 

### Contributors

Author: Brett Tackaberry (https://www.linkedin.com/in/tackaberry) | Principal Architect 

Other contributors: 

- Adrien Feudjio (https://www.linkedin.com/in/adrienfeudjio) | | Product Manager, Carbon Footprint 

- Alex Stepney (https://www.linkedin.com/in/alexstepney/) | Lead Principal Architect 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect 

- Denise Pearl (https://www.linkedin.com/in/denise-pearl) | Global Marketing Lead, Sustainability 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Laura Hyatt (https://www.linkedin.com/in/laura-hyatt) | Customer Engineer, FSI 

- Nicolas Pintaux (https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist 

- Radhika Kanakam (https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework 

## Use regions that consume lowcarbon energy

This principle in the sustainability pillar of the Google Cloud Well-Architected Framework (/architecture/framework/sustainability) provides recommendations to help you select low-carbon regions for your workloads in Google Cloud. 

### Principle overview

When you plan to deploy a workload in Google Cloud, an important architectural decision is the choice of Google Cloud region for the workload. This decision affects the carbon footprint of your workload. To minimize the carbon footprint, your region-selection strategy must include the following elements: 

- **Data-driven selection** : To identify and prioritize regions, consider the 

- Low CO 2<sup>(https://cloud.google.com/sustainability/region-carbon#region-picker)</sup> indicator and the carbon-free energy (CFE) 

(https://cloud.google.com/sustainability/region-carbon) metric. 

- **Policy-based governance** : Restrict resource creation to environmentally optimal locations by using the resource locations 

- (/resource-manager/docs/organization-policy/defining-locations) constraint in Organization Policy Service. 

- **Operational flexibility** : Use techniques like time-shifting and carbon-aware scheduling to run batch workloads during hours when the carbon intensity of the electrical grid (https://en.wikipedia.org/wiki/Electrical_grid) is the lowest. 

The electricity that's used to power your application and workloads in the cloud is an important factor that affects your choice of Google Cloud regions. In addition, consider the following factors: 

- **Data residency and sovereignty** : The location where you need to store your data is a foundational factor that dictates your choice of Google Cloud region. This choice affects compliance with local data residency 

- (/assured-workloads/docs/data-residency) requirements. 

- **Latency for end users** : The geographical distance between your end users and the regions where you deploy applications affects user experience and application performance. 

**Cost** : The pricing for Google Cloud resources can be different across regions. 

The Google Cloud Region Picker (https://cloud.withgoogle.com/region-picker/) tool helps you select optimal Google Cloud regions based on your requirements for carbon footprint, cost, and latency. You can also use Cloud Location Finder 

(/location-finder/docs/overview) to find cloud locations in Google Cloud and other providers based on your requirements for proximity, carbon-free energy (CFE) usage, and other parameters. 

### Recommendations

To deploy your cloud workloads in low-carbon regions, consider the recommendations in the following sections. These recommendations are based on the guidance in Carbon-free energy for Google Cloud regions 

(https://cloud.google.com/sustainability/region-carbon). 

#### Understand the carbon intensity of cloud regions

Google Cloud data centers in a region use energy from the electrical grid where the region is located. Google measures the carbon impact of a region by using the CFE metric, which is calculated every hour. CFE indicates the percentage of carbon-free energy out of the total energy that's consumed during an hour. The CFE metric depends on two factors: 

- The type of power-generation plants that supply the grid during a given period. 

- Google-attributed (https://sustainability.google/progress/projects/ppa/) clean energy that's supplied to the grid during that time. 

For information about the aggregated average hourly CFE% for each Google Cloud region, see Carbon-free energy for Google Cloud regions 

(https://cloud.google.com/sustainability/region-carbon). You can also get this data in a machine-readable format from the Carbon free energy for Google Cloud regions (https://github.com/GoogleCloudPlatform/region-carbon-info) repository in GitHub and a BigQuery public dataset 

(https://console.cloud.google.com/marketplace/product/bigquery-public-datasets/regional-cfe). 

#### Incorporate CFE in your location-selection strategy

Consider the following recommendations: 

- Select the cleanest region for your applications. If you plan to run an application for a long period, run it in the region that has the highest CFE%. For batch workloads, you have greater flexibility in choosing a region because you can predict when the workload must run. 

- Select low-carbon regions. Certain pages in the Google Cloud website and location selectors in the Google Cloud console show the 

- Low CO 2<sup>(https://cloud.google.com/sustainability/region-carbon#region-picker)</sup> indicator for regions that have the lowest carbon impact. 

- Restrict the creation of resources to specific low-carbon Google Cloud regions by using the resource locations 

- (/resource-manager/docs/organization-policy/defining-locations) Organization Policy constraint. For example, to allow the creation of resources in only US-based low-carbon regions, create a constraint that specifies the `in:us-low-carbonlocations` value group. 

When you select locations for your Google Cloud resources, also consider best practices for region selection 

(https://cloud.google.com/solutions/best-practices-compute-engine-region-selection), including factors like data residency requirements, latency to end users, redundancy of the application, availability of services, and pricing. 

#### Use time-of-day scheduling

The carbon intensity of an electrical grid can vary significantly throughout the day. The variation depends on the mix of energy sources that supply the grid. You can schedule workloads, particularly those that are flexible or non-urgent, to run when the grid is supplied by a higher proportion of CFE. 

For example, many grids have higher CFE percentages during off-peak hours or when renewable sources like solar and wind supply more power to the grid. By scheduling compute-intensive tasks such as model training and large-scale batch inference during higher-CFE hours, you can significantly reduce the associated carbon emissions without affecting performance or cost. This approach is known as _time-shifting_ , where you use the dynamic nature of a grid's carbon intensity to optimize your workloads for sustainability. 

## Optimize AI and ML workloads for energy efficiency

This principle in the sustainability pillar of the Google Cloud Well-Architected Framework (/architecture/framework/sustainability) provides recommendations for optimizing AI and ML workloads to reduce their energy usage and carbon footprint. 

### Principle overview

To optimize AI and ML workloads for sustainability, you need to adopt a holistic approach to designing, deploying, and operating the workloads. Select appropriate models and specialized hardware like Tensor Processing Units (TPUs), run the workloads in low-carbon regions, optimize to reduce resource usage, and apply operational best practices. 

Architectural and operational practices that optimize the cost and performance of AI and ML workloads inherently lead to reduced energy consumption and lower carbon footprint. The AI and ML perspective (/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework describes principles and recommendations to design, build, and manage AI and ML workloads that meet your operational, security, reliability, cost, and performance goals. In addition, the Cloud Architecture 

Center (/architecture/ai-ml) provides detailed reference architectures and design guides for AI and ML workloads in Google Cloud.
