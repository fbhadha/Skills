# Architecture: Well-Architected Framework and reference designs / Google Cloud Well-Architected Framework (printable, all pillars): Shared responsibilities and shared fate on Google Cloud: What's next to Optimize resource usage: Principle overview
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 117-156, extracted 2026-10-18

## Google Cloud Well-Architected Framework (printable, all pillars)

URL: https://docs.cloud.google.com/architecture/framework/printable

### What's next

- Review the core security principles 

- (/architecture/framework/security#core_principles). 

- Familiarize yourself with available blueprints (https://cloud.google.com/security/best-practices#deployable-security-blueprints-andlanding-zones) 

- , including the security foundations blueprint and workload examples like the secured data warehouse. 

- Read more about shared fate (https://cloud.google.com/security/shared-fate). 

- Read about our underlying secure infrastructure in the Google infrastructure security design overview (/docs/security/infrastructure/design). 

- Review the Google Cloud controls that are aligned with the NIST Cybersecurity Framework requirements 

(/security-command-center/docs/compliance-manager-frameworks#nist-csf-v1-1). 

## Well-Architected Framework: Reliability pillar

The reliability pillar in the Google Cloud Well-Architected Framework (/architecture/framework) provides principles and recommendations to help you design, deploy, and manage reliable workloads in Google Cloud. 

This document is intended for cloud architects, developers, platform engineers, administrators, and site reliability engineers. 

_Reliability_ is a system's ability to consistently perform its intended functions within the defined conditions and maintain uninterrupted service. Best practices for reliability include redundancy, fault-tolerant design, monitoring, and automated recovery processes. 

As a part of reliability, _resilience_ is the system's ability to withstand and recover from failures or unexpected disruptions, while maintaining performance. Google Cloud features, like multi-regional deployments 

(/architecture/deployment-archetypes/multiregional), automated backups, and disaster recovery solutions, can help you improve your system's resilience. 

Reliability is important to your cloud strategy for many reasons, including the following: 

- **Minimal downtime** : Downtime can lead to lost revenue, decreased productivity, and damage to reputation. Resilient architectures can help ensure that systems can continue to function during failures or recover efficiently from failures. 

- **Enhanced user experience** : Users expect seamless interactions with technology. Resilient systems can help maintain consistent performance and 

availability, and they provide reliable service even during high demand or unexpected issues. 

- **Data integrity** : Failures can cause data loss or data corruption. Resilient systems implement mechanisms such as backups, redundancy, and replication to protect data and ensure that it remains accurate and accessible. 

- **Business continuity** : Your business relies on technology for critical operations. Resilient architectures can help ensure continuity after a catastrophic failure, which enables business functions to continue without significant interruptions and supports a swift recovery. 

- **Compliance** : Many industries have regulatory requirements for system availability and data protection. Resilient architectures can help you to meet these standards by ensuring systems remain operational and secure. 

- **Lower long-term costs** : Resilient architectures require upfront investment, but resiliency can help to reduce costs over time by preventing expensive downtime, avoiding reactive fixes, and enabling more efficient resource use. 

### Organizational mindset

To make your systems reliable, you need a plan and an established strategy. This strategy must include education and the authority to prioritize reliability alongside other initiatives. 

Set a clear expectation that the entire organization is responsible for reliability, including development, product management, operations, platform engineering, and site reliability engineering (SRE) (https://cloud.google.com/sre). Even the businessfocused groups, like marketing and sales, can influence reliability. 

Every team must understand the reliability targets and risks of their applications. The teams must be accountable to these requirements. Conflicts between reliability and regular product feature development must be prioritized and escalated accordingly. 

Plan and manage reliability holistically, across all your functions and teams. Consider setting up a Cloud Centre of Excellence (CCoE) that includes a reliability pillar. For more information, see Optimize your organization's cloud journey with a 

Cloud Center of Excellence 

(https://cloud.google.com/blog/topics/training-certifications/optimize-your-organizations-cloudjourney-with-a-cloud-center-of-excellence) 

### Focus areas for reliability

The activities that you perform to design, deploy, and manage a reliable system can be categorized in the following focus areas. Each of the reliability principles and recommendations in this pillar is relevant to one of these focus areas. 

- **Scoping** : To understand your system, conduct a detailed analysis of its architecture. You need to understand the components, how they work and interact, how data and actions flow through the system, and what could go wrong. Identify potential failures, bottlenecks, and risks, which helps you to take actions to mitigate those issues. 

- **Observation** : To help prevent system failures, implement comprehensive and continuous observation and monitoring. Through this observation, you can understand trends and identify potential problems proactively. 

- **Response** : To reduce the impact of failures, respond appropriately and recover efficiently. Automated responses can also help reduce the impact of failures. Even with planning and controls, failures can still occur. 

- **Learning** : To help prevent failures from recurring, learn from each experience, and take appropriate actions. 

### Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the `google-cloud-waf-reliability` 

(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-reliability) skill, which is available in the Google Agent Skills repository in GitHub. 

To install the skill, run the following command in your agent's client or terminal: 

```
npx skills add google/skills --skill google-cloud-waf-reliability
```

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global). 

**Note:** If **`npx`** is not available in your environment, install Node.js (https://nodejs.org/en/download), which includes **`npm`** and **`npx`** . 

### Core principles

The recommendations in the reliability pillar of the Well-Architected Framework are mapped to the following core principles: 

- Define reliability based on user-experience goals 

- (/architecture/framework/reliability/define-reliability-based-on-user-experience-goals) 

- Set realistic targets for reliability (/architecture/framework/reliability/set-targets) 

- Build highly available systems through resource redundancy 

- (/architecture/framework/reliability/build-highly-available-systems) 

- Take advantage of horizontal scalability 

- (/architecture/framework/reliability/horizontal-scalability) 

- Detect potential failures by using observability 

- (/architecture/framework/reliability/observability) 

- Design for graceful degradation 

- (/architecture/framework/reliability/graceful-degradation) 

- Perform testing for recovery from failures 

- (/architecture/framework/reliability/perform-testing-for-recovery-from-failures) 

- Perform testing for recovery from data loss 

- (/architecture/framework/reliability/perform-testing-for-recovery-from-data-loss) 

- Conduct thorough postmortems 

(/architecture/framework/reliability/conduct-postmortems) 

**Note:** To learn about the building blocks of infrastructure reliability in Google Cloud, see Google Cloud infrastructure reliability guide (/architecture/infra-reliability-guide). 

### Contributors

Authors: 

- Laura Hyatt (https://www.linkedin.com/in/laura-hyatt) | Customer Engineer, FSI Jose Andrade (https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist 

- Gino Pelliccia (https://www.linkedin.com/in/gino-pelliccia-13637025) | Principal Architect 

Other contributors: 

- Andrés-Leonardo Martínez-Ortiz (https://www.linkedin.com/in/almo) | Technical Program Manager 

- Brian Kudzia (https://www.linkedin.com/in/brian-kudzia-3061558) | Enterprise Infrastructure Customer Engineer 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Gary Harmson (https://www.linkedin.com/in/garyharmson) | Principal Architect 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

- Nicolas Pintaux (https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist 

- Radhika Kanakam (https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework 

- Ryan Cox (https://www.linkedin.com/in/ryanlcox) | Principal Architect 

- Samantha He (https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer 

- Wade Holmes (https://www.linkedin.com/in/wholmes) | Global Solutions Director 

- Zach Seils (https://www.linkedin.com/in/zachseils) | Networking Specialist 

## Define reliability based on userexperience goals

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) helps you to assess your users' experience, and then map the findings to reliability goals and metrics. 

This principle is relevant to the _scoping_ focus area 

(/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

Observability tools provide large amounts of data, but not all of the data directly relates to the impacts on the users. For example, you might observe high CPU usage, slow server operations, or even crashed tasks. However, if these issues don't affect the user experience, then they don't constitute an outage. 

To measure the user experience, you need to distinguish between internal system behavior and user-facing problems. Focus on metrics like the success ratio of user requests. Don't rely solely on server-centric metrics, like CPU usage, which can lead to misleading conclusions about your service's reliability. True reliability means that users can consistently and effectively use your application or service. 

### Recommendations

To help you measure user experience effectively, consider the recommendations in the following sections. 

#### Measure user experience

To truly understand your service's reliability, prioritize metrics that reflect your users' actual experience. For example, measure the users' query success ratio, application latency, and error rates. 

Ideally, collect this data directly from the user's device or browser. If this direct data collection isn't feasible, shift your measurement point progressively further away from the user in the system. For example, you can use the load balancer or frontend service as the measurement point. This approach helps you identify and address issues before those issues can significantly impact your users. 

#### Analyze user journeys

To understand how users interact with your system, you can use tracing tools like Cloud Trace (/trace/docs/overview). By following a user's journey through your application, you can find bottlenecks and latency issues that might degrade the user's experience. Cloud Trace captures detailed performance data for each _hop_ in your service architecture. This data helps you identify and address performance issues more efficiently, which can lead to a more reliable and satisfying user experience. 

## Set realistic targets for reliability

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) helps you define reliability goals that are technically feasible for your workloads in Google Cloud. 

This principle is relevant to the _scoping_ focus area (/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

Design your systems to be just reliable enough for user happiness. It might seem counterintuitive, but a goal of 100% reliability is often not the most effective strategy. Higher reliability might result in a significantly higher cost, both in terms of financial investment and potential limitations on innovation. If users are already happy with the current level of service, then efforts to further increase happiness might yield a low return on investment. Instead, you can better spend resources elsewhere. 

You need to determine the level of reliability at which your users are happy, and determine the point where the cost of incremental improvements begin to outweigh the benefits. When you determine this level of _sufficient reliability_ , you can allocate resources strategically and focus on features and improvements that deliver greater value to your users. 

### Recommendations

To set realistic reliability targets, consider the recommendations in the following subsections. 

#### Accept some failure and prioritize components

Aim for high availability such as 99.99% uptime, but don't set a target of 100% uptime. Acknowledge that some failures are inevitable. 

The gap between 100% uptime and a 99.99% target is the allowance for failure. This gap is often called the _error budget_ . The error budget can help you take risks and innovate, which is fundamental to any business to stay competitive. 

Prioritize the reliability of the most critical components in the system. Accept that less critical components can have a higher tolerance for failure. 

#### Balance reliability and cost

To determine the optimal reliability level for your system, conduct thorough costbenefit analyses. 

Consider factors like system requirements, the consequences of failures, and your organization's risk tolerance for the specific application. Remember to consider your disaster recovery metrics 

(/architecture/dr-scenarios-planning-guide#basics_of_dr_planning), such as the recovery time objective (RTO) and recovery point objective (RPO). Decide what level of reliability is acceptable within the budget and other constraints. 

Look for ways to improve efficiency and reduce costs without compromising essential reliability features. 

## Build highly available systems through resource redundancy

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to plan, build, and manage resource redundancy, which can help you to avoid failures. 

This principle is relevant to the _scoping_ focus area (/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

After you decide the level of reliability (/architecture/framework/reliability/set-targets) that you need, you must design your systems to avoid any single points of failure (/architecture/infra-reliability-guide/design#avoid_single_points_of_failure). Every critical component in the system must be replicated across multiple machines, zones, and regions (/docs/geography-and-regions#regions_and_zones). For example, a critical database can't be located in only one region, and a metadata server can't be deployed in only one single zone or region. In those examples, if the sole zone or region has an outage, the system has a global outage. 

### Recommendations

To build redundant systems, consider the recommendations in the following subsections. 

#### Identify failure domains and replicate services

Map out your system's failure domains 

(/architecture/infra-reliability-guide/building-blocks), from individual VMs to regions, and design for redundancy across the failure domains. 

To ensure high availability, distribute and replicate your services and applications across multiple zones and regions. Configure the system for automatic failover to make sure that the services and applications continue to be available in the event of zone or region outages. 

For examples of multi-zone and multi-region architectures, see Design reliable infrastructure for your workloads in Google Cloud 

(/architecture/infra-reliability-guide/design#deployment_architectures). 

#### Detect and address issues promptly

Continuously track the status of your failure domains to detect and address issues promptly. 

You can monitor the current status of Google Cloud services in all regions by using the Google Cloud Service Health dashboard (https://status.cloud.google.com/). You can also view incidents relevant to your project by using Personalized Service Health 

(https://cloud.google.com/service-health). You can use load balancers to detect resource health and automatically route traffic to healthy backends. For more information, see Health checks overview (/load-balancing/docs/health-check-concepts). 

#### Test failover scenarios

Like a fire drill, regularly simulate failures to validate the effectiveness of your replication and failover strategies. 

For more information, see Simulate a zone outage for a regional MIG 

(/compute/docs/instance-groups/regional-mig-simulate-zonal-outage) and Simulate a zone failure in GKE regional clusters (/kubernetes-engine/docs/tutorials/simulate-zone-failure). 

## Take advantage of horizontal scalability

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you use horizontal scalability. By using horizontal scalability, you can help ensure that your workloads in Google Cloud can scale efficiently and maintain performance. 

This principle is relevant to the _scoping_ focus area (/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

Re-architect your system to a horizontal architecture. To accommodate growth in traffic or data, you can add more resources. You can also remove resources when they're not in use. 

To understand the value of horizontal scaling, consider the limitations of vertical scaling. 

A common scenario for vertical scaling is to use a MySQL database as the primary database with critical data. As database usage increases, more RAM and CPU is required. Eventually, the database reaches the memory limit on the host machine, and needs to be upgraded. This process might need to be repeated several times. The problem is that there are hard limits on how much a database can grow. VM sizes are not unlimited. The database can reach a point when it's no longer possible to add more resources. 

Even if resources were unlimited, a large VM can become a single point of failure. Any problem with the primary database VM can cause error responses or cause a system-wide outage that affects all users. Avoid single points of failure, as described in Build highly available systems through resource redundancy (/architecture/framework/reliability/build-highly-available-systems). 

Besides these scaling limits, vertical scaling tends to be more expensive. The cost can increase exponentially as machines with greater amounts of compute power 

and memory are acquired. 

Horizontal scaling, by contrast, can cost less. The potential for horizontal scaling is virtually unlimited in a system that's designed to scale. 

### Recommendations

To transition from a single VM architecture to a horizontal multiple-machine architecture, you need to plan carefully and use the right tools. To help you achieve horizontal scaling, consider the recommendations in the following subsections. 

#### Use managed services

Managed services remove the need to manually manage horizontal scaling. For example, with Compute Engine managed instance groups (MIGs), you can add or remove VMs to scale your application horizontally. For containerized applications, Cloud Run is a serverless platform that can automatically scale your stateless containers based on incoming traffic. 

#### Promote modular design

Modular components and clear interfaces help you scale individual components as needed, instead of scaling the entire application. For more information, see Promote modular design 

(/architecture/framework/performance-optimization/promote-modular-design) in the performance optimization pillar. 

#### Implement a stateless design

Design applications to be stateless, meaning no locally stored data. This lets you add or remove instances without worrying about data consistency. 

## Detect potential failures by using observability

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you proactively identify areas where errors and failures might occur. 

This principle is relevant to the _observation_ focus area (/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

To maintain and improve the reliability of your workloads in Google Cloud, you need to implement effective observability by using metrics, logs, and traces. 

- Metrics are numerical measurements of activities that you want to track for your application at specific time intervals. For example, you might want to track technical metrics like request rate and error rate, which can be used as service-level indicators (SLIs). You might also need to track applicationspecific business metrics like orders placed and payments received. 

- Logs are time-stamped records of discrete events that occur within an application or system. The event could be a failure, an error, or a change in state. Logs might include metrics, and you can also use logs for SLIs. 

- A trace represents the journey of a single user or transaction through a number of separate applications or the components of an application. For example, these components could be microservices. Traces help you to track what components were used in the journeys, where bottlenecks exist, and how long the journeys took. 

Metrics, logs, and traces help you monitor your system continuously. Comprehensive monitoring helps you find out where and why errors occurred. You can also detect potential failures before errors occur. 

### Recommendations

To detect potential failures efficiently, consider the recommendations in the following subsections. 

#### Gain comprehensive insights

To track key metrics like response times and error rates, use Cloud Monitoring (/monitoring/docs/monitoring-overview) and Cloud Logging (/logging/docs/overview). These tools also help you to ensure that the metrics consistently meet the needs of your workload. 

To make data-driven decisions, analyze default service metrics to understand component dependencies and their impact on overall workload performance. 

To customize your monitoring strategy, create and publish your own metrics by using the Google Cloud SDK. 

#### Perform proactive troubleshooting

Implement robust error handling and enable logging across all of the components of your workloads in Google Cloud. Activate logs like Cloud Storage access logs (/storage/docs/access-logs) and VPC Flow Logs (/vpc/docs/flow-logs). 

When you configure logging, consider the associated costs 

(https://cloud.google.com/products/observability/pricing#logging-pricing-summary). To control logging costs, you can configure exclusion filters 

(/logging/docs/routing/overview#exclusions) on the log sinks to exclude certain logs from being stored. 

#### Optimize resource utilization

Monitor CPU consumption, network I/O metrics, and disk I/O metrics to detect under-provisioned and over-provisioned resources in services like GKE, Compute Engine, and Managed Service for Apache Spark. For a complete list of supported services, see Cloud Monitoring overview (/monitoring/docs/monitoring-overview). 

#### Prioritize alerts

For alerts, focus on critical metrics, set appropriate thresholds to minimize alert fatigue, and ensure timely responses to significant issues. This targeted approach lets you proactively maintain workload reliability. For more information, see Alerting overview (/monitoring/alerts). 

## Design for graceful degradation

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you to design your Google Cloud workloads to fail gracefully. 

This principle is relevant to the _response_ focus area (/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

Graceful degradation is a design approach where a system that experiences a high load continues to function, possibly with reduced performance or accuracy. Graceful degradation ensures continued availability of the system and prevents complete failure, even if the system's work isn't optimal. When the load returns to a manageable level, the system resumes full functionality. 

For example, during periods of high load, Google Search prioritizes results from higher-ranked web pages, potentially sacrificing some accuracy. When the load decreases, Google Search recomputes the search results. 

### Recommendations

To design your systems for graceful degradation, consider the recommendations in the following subsections. 

#### Implement throttling

Ensure that your replicas can independently handle overloads and can throttle incoming requests during high-traffic scenarios. This approach helps you to prevent cascading failures that are caused by shifts in excess traffic between zones. 

Use tools like Apigee (/apigee/docs/api-platform/get-started/what-apigee) to control the rate of API requests during high-traffic times. You can configure policy rules to reflect how you want to scale back requests. 

#### Drop excess requests early

Configure your systems to drop excess requests at the frontend layer to protect backend components. Dropping some requests prevents global failures and enables the system to recover more gracefully.With this approach, some users might experience errors. However, you can minimize the impact of outages, in contrast to an approach like _circuit-breaking_ , where _all_ traffic is dropped during an overload. 

#### Handle partial errors and retries

Build your applications to handle partial errors and retries seamlessly. This design helps to ensure that as much traffic as possible is served during high-load scenarios. 

#### Test overload scenarios

To validate that the throttle and request-drop mechanisms work effectively, regularly simulate overload conditions in your system. Testing helps ensure that your system is prepared for real-world traffic surges. 

#### Monitor traffic spikes

Use analytics and monitoring tools to predict and respond to traffic surges before they escalate into overloads. Early detection and response can help maintain service availability during high-demand periods. 

## Perform testing for recovery from failures

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you design and run tests for recovery in the event of failures. 

This principle is relevant to the _learning_ focus area (/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

To be sure that your system can recover from failures, you must periodically run tests that include regional failovers, release rollbacks, and data restoration from backups. 

This testing helps you to practice responses to events that pose major risks to reliability, such as the outage of an entire region 

(/docs/geography-and-regions#regions_and_zones). This testing also helps you verify that your system behaves as intended during a disruption. 

In the unlikely event of an entire region going down, you need to fail over all traffic to another region. During normal operation of your workload, when data is modified, it needs to be synchronized from the primary region to the failover region. You need to verify that the replicated data is always very recent, so that users don't experience data loss or session breakage. The load balancing system must also be able to shift traffic to the failover region at any time without service interruptions. To minimize downtime after a regional outage, operations engineers also need to be able to manually and efficiently shift user traffic away from a region, in as less time as possible. This operation is sometimes called _draining a region_ , which means you stop the inbound traffic to the region and move all the traffic elsewhere. 

### Recommendations

When you design and run tests for failure recovery, consider the recommendations in the following subsections. 

#### Define the testing objectives and scope

Clearly define what you want to achieve from the testing. For example, your objectives can include the following: 

- Validate the recovery time objective (RTO) and the recovery point objective (RPO). For details, see Basics of DR planning 

- (/architecture/dr-scenarios-planning-guide#basics_of_dr_planning). 

- Assess system resilience and fault tolerance under various failure scenarios. Test the effectiveness of automated failover mechanisms. 

Decide which components, services, or regions are in the testing scope. The scope can include specific application tiers like the frontend, backend, and database, or it can include specific Google Cloud resources like Cloud SQL instances or GKE clusters. The scope must also specify any external dependencies, such as thirdparty APIs or cloud interconnections. 

#### Prepare the environment for testing

Choose an appropriate environment, preferably a staging or sandbox environment that replicates your production setup. If you conduct the test in production, ensure that you have safety measures ready, like automated monitoring and manual rollback procedures. 

Create a backup plan. Take snapshots or backups of critical databases and services to prevent data loss during the test. Ensure that your team is prepared to do manual interventions if the automated failover mechanisms fail. 

To prevent test disruptions, ensure that your IAM roles, policies, and failover configurations are correctly set up. Verify that the necessary permissions are in place for the test tools and scripts. 

Inform stakeholders, including operations, DevOps, and application owners, about the test schedule, scope, and potential impact. Provide stakeholders with an estimated timeline and the expected behaviors during the test. 

#### Simulate failure scenarios

Plan and execute failures by using tools like Chaos Monkey 

(https://netflix.github.io/chaosmonkey/). You can use custom scripts to simulate failures of critical services such as a shutdown of a primary node in a multi-zone GKE cluster or a disabled Cloud SQL instance. You can also use scripts to simulate a region-wide network outage by using firewall rules or API restrictions based on your scope of test. Gradually escalate the failure scenarios to observe system behavior under various conditions. 

Introduce load testing alongside failure scenarios to replicate real-world usage during outages. Test cascading failure impacts, such as how frontend systems behave when backend services are unavailable. 

To validate configuration changes and to assess the system's resilience against human errors, test scenarios that involve misconfigurations. For example, run tests with incorrect DNS failover settings or incorrect IAM permissions. 

Zone and region disconnect testing in production 

To aim for the highest levels of service continuity, Google Cloud conducts rigorous resilience testing in a dedicated, production-equivalent environment. Unlike standard simulations, this testing uses an internal-only Google Cloud region that is architecturally identical to our customer-facing regions. The region's network connectivity is then physically disconnected to validate precisely how our products behave during a total zonal or regional failure. 

The goal is to ensure that while local services within the affected area might go offline as expected, control planes and services that operate in other zones and regions remain unaffected. 

Validation occurs on a consistent, periodic schedule, ensuring a repeatable feedback loop. This ongoing validation ensures our global infrastructure remains resilient against large-scale outages. 

For guidance on how to implement testing for your services running on Google Cloud, see Fault Injection Testing (/fault-injection-testing). 

#### Monitor system behavior

Monitor how load balancers, health checks, and other mechanisms reroute traffic. Use Google Cloud tools like Cloud Monitoring and Cloud Logging to capture metrics and events during the test. 

Observe changes in latency, error rates, and throughput during and after the failure simulation, and monitor the overall performance impact. Identify any degradation or inconsistencies in the user experience. 

Ensure that logs are generated and alerts are triggered for key events, such as service outages or failovers. Use this data to verify the effectiveness of your alerting and incident response systems. 

#### Verify recovery against your RTO and RPO

Measure how long it takes for the system to resume normal operations after a failure, and then compare this data with the defined RTO and document any gaps. 

Ensure that data integrity and availability align with the RPO. To test database consistency, compare snapshots or backups of the database before and after a failure. 

Evaluate service restoration and confirm that all services are restored to a functional state with minimal user disruption. 

#### Document and analyze results

Document each test step, failure scenario, and corresponding system behavior. Include timestamps, logs, and metrics for detailed analyses. 

Highlight bottlenecks, single points of failure, or unexpected behaviors observed during the test. To help prioritize fixes, categorize issues by severity and impact. 

Suggest improvements to the system architecture, failover mechanisms, or monitoring setups. Based on test findings, update any relevant failover policies and playbooks. Present a postmortem report to stakeholders. The report should summarize the outcomes, lessons learned, and next steps. For more information, see Conduct thorough postmortems 

(/architecture/framework/reliability/conduct-postmortems). 

#### Iterate and improve

To validate ongoing reliability and resilience, plan periodic testing (for example, quarterly). 

Run tests under different scenarios, including infrastructure changes, software updates, and increased traffic loads. 

Automate failover tests by using CI/CD pipelines to integrate reliability testing into your development lifecycle. 

During the postmortem, use feedback from stakeholders and end users to improve the test process and system resilience. 

## Perform testing for recovery from data loss

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you design and run tests for recovery from data loss. 

This principle is relevant to the _learning_ focus area (/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

To ensure that your system can recover from situations where data is lost or corrupted, you need to run tests for those scenarios. Instances of data loss might be caused by a software bug or some type of natural disaster. After such events, you need to restore data from backups and bring all of the services back up again by using the freshly restored data. 

We recommend that you use three criteria to judge the success or failure of this type of recovery test: data integrity, recovery time objective (RTO), and recovery 

point objective (RPO). For details about the RTO and RPO metrics, see Basics of DR planning (/architecture/dr-scenarios-planning-guide#basics_of_dr_planning). 

The goal of data restoration testing is to periodically verify that your organization can continue to meet business continuity requirements. Besides measuring RTO and RPO, a data restoration test must include testing of the entire application stack and all the critical infrastructure services with the restored data. This is necessary to confirm that the entire deployed application works correctly in the test environment. 

### Recommendations

When you design and run tests for recovering from data loss, consider the recommendations in the following subsections. 

#### Verify backup consistency and test restoration processes

You need to verify that your backups contain consistent and usable snapshots of data that you can restore to immediately bring applications back into service. To validate data integrity, set up automated consistency checks to run after each backup. 

To test backups, restore them in a non-production environment. To ensure your backups can be restored efficiently and that the restored data meets application requirements, regularly simulate data recovery scenarios. Document the steps for data restoration, and train your teams to execute the steps effectively during a failure. 

#### Schedule regular and frequent backups

To minimize data loss during restoration and to meet RPO targets, it's essential to have regularly scheduled backups. Establish a backup frequency that aligns with your RPO. For example, if your RPO is 15 minutes, schedule backups to run at least every 15 minutes. Optimize the backup intervals to reduce the risk of data loss. 

Use Google Cloud tools like Cloud Storage, Cloud SQL automated backups, or Spanner backups to schedule and manage backups. For critical applications, use 

near-continuous backup solutions like point-in-time recovery (PITR) for Cloud SQL (/sql/docs/postgres/backup-recovery/pitr) or incremental backups for large datasets. 

#### Define and monitor RPO

Set a clear RPO based on your business needs, and monitor adherence to the RPO. If backup intervals exceed the defined RPO, use Cloud Monitoring to set up alerts. 

#### Monitor backup health

Use Google Cloud Backup and DR service 

(/backup-disaster-recovery/docs/concepts/backup-dr) or similar tools to track the health of your backups and confirm that they are stored in secure and reliable locations. Ensure that the backups are replicated across multiple regions 

(/docs/geography-and-regions#regions_and_zones) for added resilience. 

#### Plan for scenarios beyond backup

Combine backups with disaster recovery strategies like active-active failover setups or cross-region replication for improved recovery time in extreme cases. For more information, see Disaster recovery planning guide 

(/architecture/dr-scenarios-planning-guide). 

## Conduct thorough postmortems

This principle in the reliability pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you conduct effective postmortems after failures and incidents. 

This principle is relevant to the _learning_ focus area 

(/architecture/framework/reliability#focus-areas) of reliability. 

### Principle overview

A postmortem is a written record of an incident, its impact, the actions taken to mitigate or resolve the incident, the root causes, and the follow-up actions to prevent the incident from recurring. The goal of a postmortem is to learn from mistakes and not assign blame. 

The following diagram shows the workflow of a postmortem: 

The workflow of a postmortem includes the following steps: 

- Create postmortem 

- Capture the facts 

- Identify and analyze the root causes 

- Plan for the future 

- Execute the plan 

Conduct postmortem analyses after major events and non-major events like the following: 

- User-visible downtimes or degradations beyond a certain threshold. 

- Data losses of any kind. 

- Interventions from on-call engineers, such as a release rollback or rerouting of traffic. 

- Resolution times above a defined threshold. 

Monitoring failures, which usually imply manual incident discovery. 

### Recommendations

Define postmortem criteria before an incident occurs so that everyone knows when a post mortem is necessary. 

To conduct effective postmortems, consider the recommendations in the following subsections. 

#### Conduct blameless postmortems

Effective postmortems focus on processes, tools, and technologies, and don't place blame on individuals or teams. The purpose of a postmortem analysis is to improve your technology and future, not to find who is guilty. Everyone makes mistakes. The goal should be to analyze the mistakes and learn from them. 

The following examples show the difference between feedback that assigns blame and blameless feedback: 

**Feedback that assigns blame** : "We need to rewrite the entire complicated backend system! It's been breaking weekly for the last three quarters and I'm sure we're all tired of fixing things piecemeal. Seriously, if I get paged one more time I'll rewrite it myself…" 

- **Blameless feedback** : "An action item to rewrite the entire backend system might actually prevent these pages from continuing to happen. The maintenance manual for this version is quite long and really difficult to be fully trained up on. I'm sure our future on-call engineers will thank us!" 

#### Make the postmortem report readable by all the intended audiences

For each piece of information that you plan to include in the report, assess whether that information is important and necessary to help the audience understand what happened. You can move supplementary data and explanations to an appendix of the report. Reviewers who need more information can request it. 

#### Avoid complex or over-engineered solutions

Before you start to explore solutions for a problem, evaluate the importance of the problem and the likelihood of a recurrence. Adding complexity to the system to solve problems that are unlikely to occur again can lead to increased instability. 

#### Share the postmortem as widely as possible

To ensure that issues don't remain unresolved, publish the outcome of the postmortem to a wide audience and get support from management. The value of a postmortem is proportional to the learning that occurs after the postmortem. When more people learn from incidents, the likelihood of similar failures recurring is reduced. 

## Well-Architected Framework: Cost optimization pillar

The cost optimization pillar in the Google Cloud Well-Architected Framework (/architecture/framework) describes principles and recommendations to optimize the cost of your workloads in Google Cloud. 

The intended audience includes the following: 

- CTOs, CIOs, CFOs, and other executives who are responsible for strategic cost management. 

- Architects, developers, administrators, and operators who make decisions that affect cost at all the stages of an organization's cloud journey. 

The cost models for on-premises and cloud workloads differ significantly. Onpremises IT costs include capital expenditure (CapEx) and operational expenditure (OpEx). On-premises hardware and software assets are acquired and the acquisition costs are depreciated (https://en.wikipedia.org/wiki/Depreciation) over the operating life of the assets. In the cloud, the costs for most cloud resources are treated as OpEx, where costs are incurred when the cloud resources are consumed. 

This fundamental difference underscores the importance of the following core principles of cost optimization. 

**Note:** You might be able to classify the cost of some Google Cloud services (like Compute Engine sole-tenant nodes) as capital expenditure. For more information, see Sole-tenancy accounting FAQ (/compute/docs/nodes/sole-tenancy-accounting-faq). 

For cost optimization principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Cost optimization 

(/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

### Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the `google-cloud-waf-cost-optimization` 

(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-cost-optimization) skill, which is available in the Google Agent Skills repository in GitHub. 

To install the skill, run the following command in your agent's client or terminal: 

```
npx skills add google/skills --skill google-cloud-waf-cost-optimization
```

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global). 

**Note:** If **`npx`** is not available in your environment, install Node.js (https://nodejs.org/en/download), which includes **`npm`** and **`npx`** . 

### Core principles

The recommendations in the cost optimization pillar of the Well-Architected Framework are mapped to the following core principles: 

**Align cloud spending with business value** 

(/architecture/framework/cost-optimization/align-cloud-spending-business-value): Ensure that your cloud resources deliver measurable business value by aligning IT spending with business objectives. 

**Foster a culture of cost awareness** 

(/architecture/framework/cost-optimization/foster-culture-cost-awareness): Ensure that people across your organization consider the cost impact of their decisions and activities, and ensure that they have access to the cost information required to make informed decisions. 

**Optimize resource usage** 

(/architecture/framework/cost-optimization/optimize-resource-usage): Provision only the resources that you need, and pay only for the resources that you consume. 

**Optimize continuously** 

(/architecture/framework/cost-optimization/optimize-continuously): Continuously monitor your cloud resource usage and costs, and proactively make adjustments as needed to optimize your spending. This approach involves identifying and addressing potential cost inefficiencies before they become significant problems. 

These principles are closely aligned with the core tenets of cloud FinOps (https://cloud.google.com/learn/what-is-finops). FinOps is relevant to any organization, regardless of its size or maturity in the cloud. By adopting these principles and following the related recommendations, you can control and optimize costs throughout your journey in the cloud. 

### Contributors

Author: Nicolas Pintaux (https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist 

Other contributors: 

- Anuradha Bajpai (https://www.linkedin.com/in/anuradhabajpai) | Solutions Architect 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect 

- Eric Lam (https://www.linkedin.com/in/ericlam) | Head of Google Cloud FinOps 

- Fernando Rubbo (https://www.linkedin.com/in/fernandorubbo) | Cloud Solutions Architect 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Gary Harmson (https://www.linkedin.com/in/garyharmson) | Principal Architect 

- Jose Andrade (https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist 

- Kent Hua (https://www.linkedin.com/in/kenthua) | Solutions Manager 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

- Radhika Kanakam (https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework 

- Samantha He (https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer 

- Steve McGhee (https://www.linkedin.com/in/stevemcghee) | Reliability Advocate 

- Sergei Lilichenko (https://www.linkedin.com/in/sergei-lilichenko) | Solutions Architect 

- Wade Holmes (https://www.linkedin.com/in/wholmes) | Global Solutions Director 

- Zach Seils (https://www.linkedin.com/in/zachseils) | Networking Specialist 

## Align cloud spending with business value

This principle in the cost optimization pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to align your use of Google Cloud resources with your organization's business goals. 

### Principle overview

To effectively manage cloud costs, you need to maximize the business value that the cloud resources provide and minimize the total cost of ownership (TCO) 

(https://www.finops.org/assets/terminology/#total-cost-of-ownership). When you evaluate the resource options for your cloud workloads, consider not only the cost of provisioning and using the resources, but also the cost of managing them. For example, virtual machines (VMs) on Compute Engine 

(https://cloud.google.com/products/compute) might be a cost-effective option for hosting applications. However, when you consider the overhead to maintain, patch, and scale the VMs, the TCO can increase. On the other hand, serverless services like Cloud Run (/run/docs) can offer greater business value. The lower operational overhead lets your team focus on core activities and helps to increase agility. 

To ensure that your cloud resources deliver optimal value, evaluate the following factors: 

- **Provisioning and usage costs** : The expenses incurred when you purchase, provision, or consume resources. 

- **Management costs** : The recurring expenses for operating and maintaining resources, including tasks like patching, monitoring and scaling. 

- **Indirect costs** : The costs that you might incur to manage issues like downtime, data loss, or security breaches. 

- **Business impact** : The potential benefits from the resources, like increased revenue, improved customer satisfaction, and faster time to market. 

By aligning cloud spending with business value, you get the following benefits: 

- **Value-driven decisions** : Your teams are encouraged to prioritize solutions that deliver the greatest business value and to consider both short-term and long-term cost implications. 

- **Informed resource choice** : Your teams have the information and knowledge that they need to assess the business value and TCO of various deployment options, so they choose resources that are cost-effective. 

- **Cross-team alignment** : Cross-functional collaboration between business, finance, and technical teams ensures that cloud decisions are aligned with the overall objectives of the organization. 

### Recommendations

To align cloud spending with business objectives, consider the following recommendations. 

#### Prioritize managed services and serverless products

Whenever possible, choose managed services and serverless products (/serverless) to reduce operational overhead and maintenance costs. This choice lets your teams concentrate on their core business activities. They can accelerate the delivery of new features and functionalities, and help drive innovation and value. 

The following are examples of how you can implement this recommendation: 

- To run PostgreSQL, MySQL, or Microsoft SQL Server server databases, use Cloud SQL (/sql) instead of deploying those databases on VMs. 

- To run and manage Kubernetes clusters, use Google Kubernetes Engine (GKE) Autopilot (/kubernetes-engine/docs/concepts/autopilot-overview) instead of deploying containers on VMs. 

- For your Apache Hadoop or Apache Spark processing needs, use Managed Service for Apache Spark (/dataproc) and Managed Service for Apache Spark Serverless (/dataproc-serverless/docs). Per-second billing can help to achieve significantly lower TCO 

- (https://cloud.google.com/resources/analyzing-economic-benefits-of-dataprocwhitepaper) 

when compared to on-premises data lakes. 

#### Balance cost efficiency with business agility

Controlling costs and optimizing resource utilization are important goals. However, you must balance these goals with the need for flexible infrastructure that lets you innovate rapidly, respond quickly to changes, and deliver value faster. The following are examples of how you can achieve this balance: 

- Adopt DORA metrics (https://dora.dev) for software delivery performance. Metrics like change failure rate (CFR), time to detect (TTD), and time to restore (TTR) can help to identify and fix bottlenecks in your development and deployment processes. By reducing downtime and accelerating delivery, you can achieve both operational efficiency and business agility. 

- Follow Site Reliability Engineering (SRE) (https://sre.google) practices to improve operational reliability. SRE's focus on automation, observability, and incident response can lead to reduced downtime, lower recovery time, and higher customer satisfaction. By minimizing downtime and improving operational reliability, you can prevent revenue loss and avoid the need to overprovision resources as a safety net to handle outages. 

#### Enable self-service optimization

Encourage a culture of experimentation and exploration by providing your teams with self-service cost optimization tools, observability tools, and resource management platforms. Enable them to provision, manage, and optimize their cloud resources autonomously. This approach helps to foster a sense of ownership, accelerate innovation, and ensure that teams can respond quickly to changing needs while being mindful of cost efficiency. 

#### Adopt and implement FinOps

Adopt FinOps to establish a collaborative environment where everyone is empowered to make informed decisions that balance cost and value. FinOps fosters financial accountability and promotes effective cost optimization in the cloud. 

#### Promote a value-driven and TCO-aware mindset

Encourage your team members to adopt a holistic attitude toward cloud spending, with an emphasis on TCO and not just upfront costs. Use techniques like value stream mapping (https://en.wikipedia.org/wiki/Value-stream_mapping) to visualize and 

analyze the flow of value through your software delivery process and to identify areas for improvement. 

Gain a granular understanding of cost drivers by using unit costing for your applications and services. Adopt unit economics 

(https://www.finops.org/framework/capabilities/unit-economics/) to balance costs against revenue or business metrics. By correlating cloud spending with business units of measure, such as revenue per customer or transaction volume, you can measure unit margins and verify that increasing spend is driven by profitable growth. When you balance cost against revenue, your organization can distinguish between operational inefficiency and healthy scaling. This helps you identify when further cloud investments are justified. For more information, see Maximize business value with cloud FinOps (https://cloud.google.com/resources/cloud-finops-whitepaper). 

## Foster a culture of cost awareness

This principle in the cost optimization pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to promote cost awareness across your organization and ensure that team members have the cost information that they need to make informed decisions. 

Conventionally, the responsibility for cost management might be centralized to a few select stakeholders and primarily focused on initial project architecture decisions. However, team members across all cloud user roles (analyst, architect, developer, or administrator) can help to reduce the cost of your resources in Google Cloud. By sharing cost data appropriately, you can empower team members to make cost-effective decisions throughout their development and deployment processes. 

### Principle overview

Stakeholders across various roles – product owners, developers, deployment engineers, administrators, and financial analysts – need visibility into relevant cost data and its relationship to business value. When provisioning and managing cloud resources, they need the following data: 

- **Projected resource costs** : Cost estimates at the time of design and deployment. 

- **Real-time resource usage costs** : Up-to-date cost data that can be used for ongoing monitoring and budget validation. 

- **Costs mapped to business metrics** : Insights into how cloud spending affects key performance indicators (KPIs), to enable teams to identify costeffective strategies. 

Every individual might not need access to raw cost data. However, promoting cost awareness across all roles is crucial because individual decisions can affect costs. 

By promoting cost visibility and ensuring clear ownership of cost management practices, you ensure that everyone is aware of the financial implications of their choices and everyone actively contributes to the organization's cost optimization goals. Whether through a centralized FinOps team or a distributed model, establishing accountability is crucial for effective cost optimization efforts. 

### Recommendations

To promote cost awareness and ensure that your team members have the cost information that they need to make informed decisions, consider the following recommendations. 

#### Provide organization-wide cost visibility

To achieve organization-wide cost visibility, the teams that are responsible for cost management can take the following actions: 

- **Standardize cost calculation and budgeting** : Use a consistent method to determine the full costs of cloud resources, after factoring in discounts and shared costs. Establish clear and standardized budgeting processes that align with your organization's goals and enable proactive cost management. 

- **Use standardized cost management and visibility tools** : Use appropriate tools that provide real-time insights into cloud spending and generate regular (for example, weekly) cost progression snapshots. These tools enable proactive budgeting, forecasting, and identification of 

optimization opportunities. The tools could be cloud provider tools (like the Google Cloud Billing dashboard (/billing/docs/how-to/reports)), third-party solutions, or open-source solutions like the Cost Attribution solution (https://github.com/google/cost-attribution-solution). 

- **Implement a cost allocation system** : Allocate a portion of the overall cloud budget to each team or project. Such an allocation gives the teams a sense of ownership over cloud spending and encourages them to make cost-effective decisions within their allocated budget. 

- **Promote transparency** : Encourage teams to discuss cost implications during the design and decision-making processes. Create a safe and supportive environment for sharing ideas and concerns related to cost optimization. Some organizations use positive reinforcement mechanisms like leaderboards or recognition programs. If your organization has restrictions on sharing raw cost data due to business concerns, explore alternative approaches for sharing cost information and insights. For example, consider sharing aggregated metrics (like the total cost for an environment or feature) or relative metrics (like the average cost per transaction or user). 

#### Understand how cloud resources are billed

Pricing for Google Cloud resources might vary across regions 

(/docs/geography-and-regions#regions_and_zones). Some resources are billed monthly at a fixed price, and others might be billed based on usage. To understand how Google Cloud resources are billed, use the Google Cloud pricing calculator (https://cloud.google.com/products/calculator) and product-specific pricing information (for example, Google Kubernetes Engine (GKE) pricing (https://cloud.google.com/kubernetes-engine/pricing)). 

#### Understand resource-based cost optimization options

For each type of cloud resource that you plan to use, explore strategies to optimize utilization and efficiency. The strategies include rightsizing, autoscaling, and adopting serverless technologies where appropriate. The following are examples of cost optimization options for a few Google Cloud products: 

- Cloud Run lets you configure always-allocated CPUs 

- (/run/docs/configuring/cpu-allocation) to handle predictable traffic loads at a 

fraction of the price of the default allocation method (that is, CPUs allocated only during request processing). 

- You can purchase BigQuery slot commitments 

- (/bigquery/docs/reservations-commitments) to save money on data analysis. 

- GKE (/kubernetes-engine/docs/how-to/cost-optimization-metrics) provides detailed metrics to help you understand cost optimization options. 

- Understand how network pricing (https://cloud.google.com/vpc/network-pricing) can affect the cost of data transfers and how you can optimize costs for specific networking services. For example, you can reduce the data transfer costs for external Application Load Balancers by using Cloud CDN or Google Cloud Armor. For more information, see Ways to lower external Application Load Balancer costs 

- (/vpc/network-pricing#ways-to-lower-external-application-load-balancer-costs). 

#### Understand discount-based cost optimization options

Familiarize yourself with the discount programs that Google Cloud offers, such as the following examples: 

- **Committed use discounts (CUDs)** (/docs/cuds): CUDs are suitable for resources that have predictable and steady usage. CUDs let you get significant reductions in price in exchange for committing to specific resource usage over a period (typically one to three years). You can also use CUD autorenewal (/compute/docs/instances/renew-commitments-automatically) to avoid having to manually repurchase commitments when they expire. 

- **Sustained use discounts** (/compute/docs/sustained-use-discounts): For certain Google Cloud products like Compute Engine and GKE, you can get automatic discount credits after continuous resource usage beyond specific duration thresholds. 

- **Spot VMs** (https://cloud.google.com/solutions/spot-vms): For fault-tolerant and flexible workloads, Spot VMs can help to reduce your Compute Engine costs. The cost of Spot VMs is significantly lower than regular VMs. However, Compute Engine might preemptively stop or delete Spot VMs to reclaim capacity. Spot VMs are suitable for batch jobs that can tolerate preemption and don't have high availability requirements. 

**Discounts for specific product options** : Some managed services like BigQuery offer discounts (/bigquery/docs/reservations-intro) when you purchase dedicated or autoscaling query processing capacity. 

Evaluate and choose the discounts options that align with your workload characteristics and usage patterns. 

#### Incorporate cost estimates into architecture blueprints

Encourage teams to develop architecture blueprints that include cost estimates for different deployment options and configurations. This practice empowers teams to compare costs proactively and make informed decisions that align with both technical and financial objectives. 

#### Use a consistent and standard set of labels for all your resources

You can use labels (/resource-manager/docs/best-practices-labels) to track costs and to identify and classify resources. Specifically, you can use labels to allocate costs to different projects, departments, or cost centers. Defining a formal labeling policy 

(/resource-manager/docs/best-practices-labels#example_labels_table) that aligns with the needs of the main stakeholders in your organization helps to make costs visible more widely. You can also use labels to filter resource cost and usage data based on target audience. 

Use automation tools like Terraform to enforce labeling on every resource that is created. To enhance cost visibility and attribution further, you can use the tools provided by the open-source cost attribution solution 

(https://github.com/google/cost-attribution-solution). 

#### Share cost reports with team members

By sharing cost reports with your team members, you empower them to take ownership of their cloud spending. This practice enables cost-effective decision making, continuous cost optimization, and systematic improvements to your cost allocation model. 

Cost reports can be of several types, including the following: 

- **Periodic cost reports** : Regular reports inform teams about their current cloud spending. Conventionally, these reports might be spreadsheet exports. More effective methods include automated emails and specialized dashboards. To ensure that cost reports provide relevant and actionable information without overwhelming recipients with unnecessary detail, the reports must be tailored to the target audiences. Setting up tailored reports is a foundational step toward more real-time and interactive cost visibility and management. 

- **Automated notifications** : You can configure cost reports to proactively notify relevant stakeholders (for example, through email or chat) about cost anomalies, budget thresholds, or opportunities for cost optimization. By providing timely information directly to those who can act on it, automated alerts encourage prompt action and foster a proactive approach to cost optimization. 

- **Google Cloud dashboards** : You can use the built-in billing dashboards (/billing/docs/how-to/reports) in Google Cloud to get insights into cost breakdowns and to identify opportunities for cost optimization. Google Cloud also provides FinOps hub (/billing/docs/how-to/finops-hub) to help you monitor savings and get recommendations for cost optimization. An AI engine powers the FinOps hub to recommend cost optimization opportunities for all the resources that are currently deployed. To control access to these recommendations, you can implement role-based access control (RBAC). 

- **Custom dashboards** : You can create custom dashboards by exporting cost data to an analytics database, like BigQuery 

- (/billing/docs/how-to/export-data-bigquery). Use a visualization tool like Data Studio (https://cloud.google.com/data-studio) to connect to the analytics database to build interactive reports and enable fine-grained access control through role-based permissions. 

- **Multicloud cost reports** : For multicloud deployments, you need a unified view of costs across all the cloud providers to ensure comprehensive analysis, budgeting, and optimization. Use tools like BigQuery to centralize and analyze cost data from multiple cloud providers, and use Data Studio to build teamspecific interactive reports. 

## Optimize resource usage

This principle in the cost optimization pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you plan and provision resources to match the requirements and consumption patterns of your cloud workloads. 

### Principle overview

To optimize the cost of your cloud resources, you need to thoroughly understand your workloads resource requirements and load patterns. This understanding is the basis for a well defined cost model that lets you forecast the total cost of ownership (TCO) and identify cost drivers throughout your cloud adoption journey. By proactively analyzing and forecasting cloud spending, you can make informed choices about resource provisioning, utilization, and cost optimization. This approach lets you control cloud spending, avoid overprovisioning, and ensure that cloud resources are aligned with the dynamic needs of your workloads and environments.
