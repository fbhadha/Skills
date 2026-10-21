# Architecture: Well-Architected Framework and reference designs / Google Cloud Well-Architected Framework (overview) to Google Cloud Well-Architected Framework (printable, all pillars): Google Cloud Well-Architected Framework (printable, all pillars) to Continuously improve and innovate: Principle overview
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 2-45, extracted 2026-10-18

Contains:
- Google Cloud Well-Architected Framework (overview) (pages 2-8) https://docs.cloud.google.com/architecture/framework
- Google Cloud Well-Architected Framework (printable, all pillars): Google Cloud Well-Architected Framework (printable, all pillars) to Continuously improve and innovate: Principle overview (pages 9-45) https://docs.cloud.google.com/architecture/framework/printable

## Google Cloud Well-Architected Framework (overview)

URL: https://docs.cloud.google.com/architecture/framework

Last reviewed 2026-10-13 UTC 

To view all of the content in the Well-Architected Framework on a single page or to to get a PDF output of the content, see View on one page (/architecture/framework/printable). 

The Well-Architected Framework provides recommendations to help architects, developers, administrators, and other cloud practitioners design and operate a cloud topology that's secure, efficient, resilient, high-performing, cost-effective, and sustainable. 

A cross-functional team of experts at Google validates the recommendations in the Well-Architected Framework. The team curates the Well-Architected Framework to reflect the expanding capabilities of Google Cloud, industry best practices, community knowledge, and feedback from you. For a summary of the significant changes to the Well-Architected Framework, see What's new 

(/architecture/framework/whats-new). 

The Well-Architected Framework is relevant to applications built for the cloud _and_ for workloads migrated from on-premises to Google Cloud, hybrid cloud deployments, and multi-cloud environments. 

### Well-Architected Framework pillars and perspectives

The recommendations in the Well-Architected Framework are organized into pillars and cross-pillar perspectives, as shown in the following diagram. 

- A _pillar_ in the Well-Architected Framework provides principles and recommendations for a specific non-functional focus area: security, reliability, performance, cost, operations, or sustainability. 

- A _perspective_ in the Well-Architected Framework is a cross-pillar view of recommendations for a specific technology, domain, or sector. The recommendations in a perspective align with the general principles and recommendations in the pillars. 

For example, the financial services (FS) perspective recommends a disaster recovery strategy that meets regulatory requirements for data residency. This FS-specific recommendation aligns with the reliability pillar's principle about realistic targets, because the data residency requirements influence the choice of failover region and, consequently, the recovery objectives. 

#### Pillars

**Operational excellence** (/architecture/framework/operational-excellence) 

Efficiently deploy, operate, monitor, and manage your cloud workloads. 

**Security, privacy, and compliance** (/architecture/framework/security) 

Maximize the security of your data and workloads in the cloud, design for privacy, and align with regulatory requirements and standards. 

**Reliability** (/architecture/framework/reliability) 

Design and operate resilient and highly available workloads in the cloud. 

**Cost optimization** (/architecture/framework/cost-optimization) 

Maximize the business value of your investment in Google Cloud. 

**Performance optimization** (/architecture/framework/performance-optimization) 

Design and tune your cloud resources for optimal performance. 

**Sustainability** (/architecture/framework/sustainability) 

Build and manage cloud workloads that are environmentally sustainable. 

#### Cross-pillar perspectives

**AI and ML** (/architecture/framework/perspectives/ai-ml) 

A cross-pillar view of technology-specific recommendations for AI and ML workloads. 

**Financial services** (/architecture/framework/perspectives/fsi) 

A cross-pillar view of recommendations for FS workloads. 

### Agent skills

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in each pillar of the Well-Architected Framework, use the `googlecloud-waf-*` agent skill s 1 (#fn1) that are available in the Google Agent Skills repository (https://github.com/google/skills) in GitHub. 

To install a specific Well-Architected Framework pillar skill, run the following command in your agent's client or terminal. When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global). 

```
npx skills add google/skills --skill SKILL_NAME
```

In the preceding command, replace _SKILL_NAME_ with the name of the skill that you want to install, from the following table. 

**Note:** If **`npx`** is not available in your environment, install Node.js (https://nodejs.org/en/download), which includes **`npm`** and **`npx`** . 

|Pillar, and link to skill in GitHub|`SKILL_NAME`|
|---|---|
|Operational excellence<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>operational-excellence)|`google-`<br>`cloud-waf-`<br>`operational-`<br>`excellence`|
|Security, privacy, and compliance<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>security)|`google-`<br>`cloud-waf-`<br>`security`|
|Reliability<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>reliability)|`google-`<br>`cloud-waf-`<br>`reliability`|
|Cost optimization<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-cost-<br>optimization)|`google-`<br>`cloud-waf-`<br>`cost-`<br>`optimization`|
|Performance optimization<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>performance-optimization)|`google-`<br>`cloud-waf-`<br>`performance-`<br>`optimization`|
|Sustainability<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>sustainability)|`google-`<br>`cloud-waf-`<br>`sustainabili`<br>`ty`|

**Tip:** To install all of the available Google skills across all your agents and workspaces without being prompted to choose the agents and workspaces, run **`npx skills add google/skills -- all`** 

Each Well-Architected Framework skill includes the following information for a specific pillar: 

- An overview of the pillar, its core principles, and links to AI-friendly documentation for each principle. 

- Examples of Google Cloud products and features that are relevant to the pillar. 

- Assessment questions that agents can ask to understand the requirements of a workload. 

- A validation checklist that agents can use to evaluate an architecture's alignment with the principles and recommendations in the pillar. 

### Core principles

Before you explore the recommendations in each pillar of the Well-Architected Framework, review the following core principles: 

#### Design for change

No system is static. The needs of its users, the goals of the team that builds the system, and the system itself are constantly changing. With the need for change in mind, build a development and production process that enables teams to regularly deliver small changes and get fast feedback on those changes. Consistently demonstrating the ability to deploy changes helps to build trust with stakeholders, including the teams responsible for the system, and the users of the system. Using DORA's software delivery metrics (https://dora.dev/guides/dora-metrics-four-keys/) can help your team monitor the speed, ease, and safety of making changes to the system. 

#### Document your architecture

When you start to move your workloads to the cloud or build your applications, lack of documentation about the system can be a major obstacle. Documentation is especially important for correctly visualizing the architecture of your current deployments. 

Quality documentation isn't achieved by producing a specific amount of documentation, but by how clear content is, how useful it is, and how it's maintained as the system changes. 

A properly documented cloud architecture establishes a common language and standards, which enable cross-functional teams to communicate and collaborate effectively. The documentation also provides the information that's necessary to 

identify and guide future design decisions. Documentation should be written with your use cases in mind, to provide context for the design decisions. 

Over time, your design decisions will evolve and change. The change history provides the context that your teams require to align initiatives, avoid duplication, and measure performance changes effectively over time. Change logs are particularly valuable when you onboard a new cloud architect who is not yet familiar with your current design, strategy, or history. 

Analysis by DORA (https://dora.dev/capabilities/documentation-quality/) has found a clear link between documentation quality and organizational performance — the organization's ability to meet their performance and profitability goals. 

#### Simplify your design and use fully managed services

Simplicity is crucial for design. If your architecture is too complex to understand, it will be difficult to implement the design and manage it over time. Where feasible, use fully managed services to minimize the risks, time, and effort associated with managing and maintaining baseline systems. 

If you're already running your workloads in production, test with managed services to see how they might help to reduce operational complexities. If you're developing new workloads, then start simple, establish a minimal viable product (MVP), and resist the urge to over-engineer. You can identify exceptional use cases, iterate, and improve your systems incrementally over time. 

#### Decouple your architecture

Research from DORA (https://dora.dev/capabilities/loosely-coupled-teams/) shows that architecture is an important predictor for achieving continuous delivery. Decoupling is a technique that's used to separate your applications and service components into smaller components that can operate independently. For example, you might separate a monolithic application stack into individual service components. In a loosely coupled architecture, an application can run its functions independently, regardless of the various dependencies. 

A decoupled architecture gives you increased flexibility to do the following: 

Apply independent upgrades. 

- Enforce specific security controls. 

- Establish reliability goals for each subsystem. 

- Monitor health. 

- Granularly control performance and cost parameters. 

You can start the decoupling process early in your design phase or incorporate it as part of your system upgrades as you scale. 

#### Use a stateless architecture

A stateless architecture can increase both the reliability and scalability of your applications. 

Stateful applications rely on various dependencies to perform tasks, such as local caching of data. Stateful applications often require additional mechanisms to capture progress and restart gracefully. Stateless applications can perform tasks without significant local dependencies by using shared storage or cached services. A stateless architecture enables your applications to scale up quickly with minimum boot dependencies. The applications can withstand hard restarts, have lower downtime, and provide better performance for end users. 

1. For more information about agent skills standard, see Agent Skills Overview (https://agentskills.io/home). ↩ (#fnref1) 

Last updated 2026-10-13 UTC. 



## Google Cloud Well-Architected Framework (printable, all pillars)

URL: https://docs.cloud.google.com/architecture/framework/printable

Last reviewed 2026-01-28 UTC 

The Well-Architected Framework provides recommendations to help architects, developers, administrators, and other cloud practitioners design and operate a cloud topology that's secure, efficient, resilient, high-performing, cost-effective, and sustainable. 

A cross-functional team of experts at Google validates the recommendations in the Well-Architected Framework. The team curates the Well-Architected Framework to reflect the expanding capabilities of Google Cloud, industry best practices, community knowledge, and feedback from you. For a summary of the significant changes to the Well-Architected Framework, see What's new 

(/architecture/framework/whats-new). 

The Well-Architected Framework is relevant to applications built for the cloud _and_ for workloads migrated from on-premises to Google Cloud, hybrid cloud deployments, and multi-cloud environments. 

### Well-Architected Framework pillars and perspectives

The recommendations in the Well-Architected Framework are organized into pillars and cross-pillar perspectives, as shown in the following diagram. 

A _pillar_ in the Well-Architected Framework provides principles and recommendations for a specific non-functional focus area: security, reliability, performance, cost, operations, or sustainability. 

- A _perspective_ in the Well-Architected Framework is a cross-pillar view of recommendations for a specific technology, domain, or sector. The recommendations in a perspective align with the general principles and recommendations in the pillars. 

For example, the financial services (FS) perspective recommends a disaster recovery strategy that meets regulatory requirements for data residency. This FS-specific recommendation aligns with the reliability pillar's principle about realistic targets, because the data residency requirements influence the choice of failover region and, consequently, the recovery objectives. 

#### Pillars

**Operational excellence** (/architecture/framework/operational-excellence) 

Efficiently deploy, operate, monitor, and manage your cloud workloads. 

**Security, privacy, and compliance** (/architecture/framework/security) 

Maximize the security of your data and workloads in the cloud, design for privacy, and align with regulatory requirements and standards. 

**Reliability** (/architecture/framework/reliability) 

Design and operate resilient and highly available workloads in the cloud. 

**Cost optimization** (/architecture/framework/cost-optimization) 

Maximize the business value of your investment in Google Cloud. 

**Performance optimization** (/architecture/framework/performance-optimization) 

Design and tune your cloud resources for optimal performance. 

**Sustainability** (/architecture/framework/sustainability) 

Build and manage cloud workloads that are environmentally sustainable. 

#### Cross-pillar perspectives

**AI and ML** (/architecture/framework/perspectives/ai-ml) 

A cross-pillar view of technology-specific recommendations for AI and ML workloads. 

**Financial services** (/architecture/framework/perspectives/fsi) 

A cross-pillar view of recommendations for FS workloads. 

### Agent skills

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in each pillar of the Well-Architected Framework, use the `googlecloud-waf-*` agent skill s 1 (#fn1) that are available in the Google Agent Skills repository (https://github.com/google/skills) in GitHub. 

To install a specific Well-Architected Framework pillar skill, run the following command in your agent's client or terminal. When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global). 

```
npx skills add google/skills --skill SKILL_NAME
```

In the preceding command, replace _SKILL_NAME_ with the name of the skill that you want to install, from the following table. 

**Note:** If **`npx`** is not available in your environment, install Node.js (https://nodejs.org/en/download), which includes **`npm`** and **`npx`** . 

Pillar, and link to skill in GitHub `SKILL_NAME` 

Operational excellence `google-` (https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf- `cloud-waf-` operational-excellence) `operationalexcellence` 

|Pillar, and link to skill in GitHub|`SKILL_NAME`|
|---|---|
|Security, privacy, and compliance<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>security)|`google-`<br>`cloud-waf-`<br>`security`|
|Reliability<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>reliability)|`google-`<br>`cloud-waf-`<br>`reliability`|
|Cost optimization<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-cost-<br>optimization)|`google-`<br>`cloud-waf-`<br>`cost-`<br>`optimization`|
|Performance optimization<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>performance-optimization)|`google-`<br>`cloud-waf-`<br>`performance-`<br>`optimization`|
|Sustainability<br>(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-<br>sustainability)|`google-`<br>`cloud-waf-`<br>`sustainabili`<br>`ty`|

**Tip:** To install all of the available Google skills across all your agents and workspaces without being prompted to choose the agents and workspaces, run **`npx skills add google/skills -- all`** 

Each Well-Architected Framework skill includes the following information for a specific pillar: 

- An overview of the pillar, its core principles, and links to AI-friendly documentation for each principle. 

- Examples of Google Cloud products and features that are relevant to the pillar. 

- Assessment questions that agents can ask to understand the requirements of a workload. 

- A validation checklist that agents can use to evaluate an architecture's alignment with the principles and recommendations in the pillar. 

### Core principles

Before you explore the recommendations in each pillar of the Well-Architected Framework, review the following core principles: 

#### Design for change

No system is static. The needs of its users, the goals of the team that builds the system, and the system itself are constantly changing. With the need for change in mind, build a development and production process that enables teams to regularly deliver small changes and get fast feedback on those changes. Consistently demonstrating the ability to deploy changes helps to build trust with stakeholders, including the teams responsible for the system, and the users of the system. Using DORA's software delivery metrics (https://dora.dev/guides/dora-metrics-four-keys/) can help your team monitor the speed, ease, and safety of making changes to the system. 

#### Document your architecture

When you start to move your workloads to the cloud or build your applications, lack of documentation about the system can be a major obstacle. Documentation is especially important for correctly visualizing the architecture of your current deployments. 

Quality documentation isn't achieved by producing a specific amount of documentation, but by how clear content is, how useful it is, and how it's maintained as the system changes. 

A properly documented cloud architecture establishes a common language and standards, which enable cross-functional teams to communicate and collaborate effectively. The documentation also provides the information that's necessary to identify and guide future design decisions. Documentation should be written with your use cases in mind, to provide context for the design decisions. 

Over time, your design decisions will evolve and change. The change history provides the context that your teams require to align initiatives, avoid duplication, and measure performance changes effectively over time. Change logs are 

particularly valuable when you onboard a new cloud architect who is not yet familiar with your current design, strategy, or history. 

Analysis by DORA (https://dora.dev/capabilities/documentation-quality/) has found a clear link between documentation quality and organizational performance — the organization's ability to meet their performance and profitability goals. 

#### Simplify your design and use fully managed services

Simplicity is crucial for design. If your architecture is too complex to understand, it will be difficult to implement the design and manage it over time. Where feasible, use fully managed services to minimize the risks, time, and effort associated with managing and maintaining baseline systems. 

If you're already running your workloads in production, test with managed services to see how they might help to reduce operational complexities. If you're developing new workloads, then start simple, establish a minimal viable product (MVP), and resist the urge to over-engineer. You can identify exceptional use cases, iterate, and improve your systems incrementally over time. 

#### Decouple your architecture

Research from DORA (https://dora.dev/capabilities/loosely-coupled-teams/) shows that architecture is an important predictor for achieving continuous delivery. Decoupling is a technique that's used to separate your applications and service components into smaller components that can operate independently. For example, you might separate a monolithic application stack into individual service components. In a loosely coupled architecture, an application can run its functions independently, regardless of the various dependencies. 

A decoupled architecture gives you increased flexibility to do the following: 

- Apply independent upgrades. 

- Enforce specific security controls. 

- Establish reliability goals for each subsystem. 

- Monitor health. 

- Granularly control performance and cost parameters. 

You can start the decoupling process early in your design phase or incorporate it as part of your system upgrades as you scale. 

#### Use a stateless architecture

A stateless architecture can increase both the reliability and scalability of your applications. 

Stateful applications rely on various dependencies to perform tasks, such as local caching of data. Stateful applications often require additional mechanisms to capture progress and restart gracefully. Stateless applications can perform tasks without significant local dependencies by using shared storage or cached services. A stateless architecture enables your applications to scale up quickly with minimum boot dependencies. The applications can withstand hard restarts, have lower downtime, and provide better performance for end users. 

## Well-Architected Framework: Operational excellence pillar

The operational excellence pillar in the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to operate workloads efficiently on Google Cloud. Operational excellence in the cloud involves designing, implementing, and managing cloud solutions that provide value, performance, security, and reliability. The recommendations in this pillar help you to continuously improve and adapt workloads to meet the dynamic and ever-evolving needs in the cloud. 

The operational excellence pillar is relevant to the following audiences: 

- **Managers and leaders** : A framework to establish and maintain operational excellence in the cloud and to ensure that cloud investments deliver value and support business objectives. 

- **Cloud operations teams** : Guidance to manage incidents and problems, plan capacity, optimize performance, and manage change. 

- **Site reliability engineers (SREs)** : Best practices that help you to achieve high levels of service reliability, including monitoring, incident response, and 

automation. 

**Cloud architects and engineers** : Operational requirements and best practices for the design and implementation phases, to help ensure that solutions are designed for operational efficiency and scalability. 

**DevOps teams** : Guidance about automation, CI/CD pipelines, and change management, to help enable faster and more reliable software delivery. 

To achieve operational excellence, you should embrace automation, orchestration, and data-driven insights. Automation helps to eliminate toil. It also streamlines and builds guardrails around repetitive tasks. Orchestration helps to coordinate complex processes. Data-driven insights enable evidence-based decision-making. By using these practices, you can optimize cloud operations, reduce costs, improve service availability, and enhance security. 

Operational excellence in the cloud goes beyond technical proficiency in cloud operations. It includes a cultural shift that encourages continuous learning and experimentation. Teams must be empowered to innovate, iterate, and adopt a growth mindset. A culture of operational excellence fosters a collaborative environment where individuals are encouraged to share ideas, challenge assumptions, and drive improvement. 

For operational excellence principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Operational excellence 

(/architecture/framework/perspectives/ai-ml/operational-excellence) in the Well-Architected Framework. 

### Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the `google-cloud-waf-operational-excellence` (https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-operationalexcellence) 

skill, which is available in the Google Agent Skills repository in GitHub. 

To install the skill, run the following command in your agent's client or terminal: 

```
npx skills add google/skills --skill google-cloud-waf-operational-excellence
```

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global). 

**Note:** If **`npx`** is not available in your environment, install Node.js (https://nodejs.org/en/download), which includes **`npm`** and **`npx`** . 

### Core principles

The recommendations in the operational excellence pillar of the Well-Architected Framework are mapped to the following core principles: 

Ensure operational readiness and performance using CloudOps 

- (/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops) 

- : Ensure that cloud solutions meet operational and performance requirements by defining service level objectives (SLOs) and by performing comprehensive monitoring, performance testing, and capacity planning. 

Manage incidents and problems 

- (/architecture/framework/operational-excellence/manage-incidents-and-problems): Minimize the impact of cloud incidents and prevent recurrence through comprehensive observability, clear incident response procedures, thorough retrospectives, and preventive measures. 

Manage and optimize cloud resources 

- (/architecture/framework/operational-excellence/manage-and-optimize-cloud-resources): Optimize and manage cloud resources through strategies like right-sizing, autoscaling, and by using effective cost monitoring tools. 

Automate and manage change 

- (/architecture/framework/operational-excellence/automate-and-manage-change): Automate processes, streamline change management, and alleviate the burden of manual labor. 

- Continuously improve and innovate 

- (/architecture/framework/operational-excellence/continuously-improve-and-innovate): Focus on ongoing enhancements and the introduction of new solutions to stay competitive. 

### Contributors

Authors: 

- Alex Stepney (https://www.linkedin.com/in/alexstepney/) | Lead Principal Architect Ryan Cox (https://www.linkedin.com/in/ryanlcox) | Principal Architect 

- Hadrian Knotz (https://www.linkedin.com/in/hadrianknotz) | Enterprise Architect 

Other contributors: 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Gary Harmson (https://www.linkedin.com/in/garyharmson) | Principal Architect 

- Jose Andrade (https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Nicolas Pintaux (https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist 

- Radhika Kanakam (https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework 

- Samantha He (https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer 

- Zach Seils (https://www.linkedin.com/in/zachseils) | Networking Specialist 

- Wade Holmes (https://www.linkedin.com/in/wholmes) | Global Solutions Director 

## Ensure operational readiness and performance using CloudOps

This principle in the operational excellence pillar of the Google Cloud WellArchitected Framework (/architecture/framework) helps you to ensure operational readiness and performance of your cloud workloads. It emphasizes establishing clear expectations and commitments for service performance, implementing robust monitoring and alerting, conducting performance testing, and proactively planning for capacity needs. 

### Principle overview

Different organizations might interpret operational readiness differently. Operational readiness is how _your_ organization prepares to successfully operate workloads on Google Cloud. Preparing to operate a complex, multilayered cloud workload requires careful planning for both go-live and day-2 (https://discuss.google.dev/t/simplify-day-2-cloud-operations-with-google-cloud-solutions-andarchitectural-design-best-practices/98008) 

operations. These operations are often called _CloudOps_ . 

### Focus areas of operational readiness

Operational readiness consists of four focus areas. Each focus area consists of a set of activities and components that are necessary to prepare to operate a complex application or environment in Google Cloud. The following table lists the components and activities of each focus area: 

**Note:** The recommendations in the operational excellence pillar of the Well-Architected Framework are relevant to one or more of these operational-readiness focus areas. 

|Focus area of operational<br>readiness|Activities and components|
|---|---|
|Workforce|Defining clear roles and responsibilities for the teams that<br>manage and operate the cloud resources.<br>Ensuring that team members have appropriate skills.<br>Developing a learning program.<br>Establishing a clear team structure.<br>Hiring the required talent.|
|Processes|Observability.<br>Managing service disruptions.<br>Cloud delivery.<br>Core cloud operations.|
|Tooling|Tools that are required to support CloudOps processes.|
|Governance|Service levels and reporting.<br>Cloud financials.<br>Cloud operating model.<br>Architectural review and governance boards.<br>Cloud architecture and compliance.|

### Recommendations

To ensure operational readiness and performance by using CloudOps, consider the recommendations in the following sections. Each recommendation in this document is relevant to one or more of the focus areas of operational readiness (#focus-areas-of-operational-readiness). 

#### Define SLOs and SLAs

A core responsibility of the cloud operations team is to define service level objectives (SLOs) and service level agreements (SLAs) for all of the critical 

workloads. This recommendation is relevant to the _governance_ focus area of operational readiness (#focus-areas-of-operational-readiness). 

**Define SLOs** : 

SLOs must be specific, measurable, achievable, relevant, and time-bound (SMART), and they must reflect the level of service and performance that you want. 

- **Specific** : Clearly articulates the required level of service and performance. 

- **Measurable** : Quantifiable and trackable. 

- **Achievable** : Attainable within the limits of your organization's capabilities and resources. 

- **Relevant** : Aligned with business goals and priorities. 

- **Time-bound** : Has a defined timeframe for measurement and evaluation. 

For example, an SLO for a web application might be "99.9% availability" or "average response time less than 200 ms." Such SLOs clearly define the required level of service and performance for the web application, and the SLOs can be measured and tracked over time. 

**Define SLAs** : 

SLAs outline the commitments to customers regarding service availability, performance, and support, including any penalties or remedies for noncompliance. SLAs must include specific details about the services that are provided, the level of service that can be expected, the responsibilities of both the service provider and the customer, and any penalties or remedies for noncompliance. SLAs serve as a contractual agreement between the two parties, ensuring that both have a clear understanding of the expectations and obligations that are associated with the cloud service. 

**Track SLOs** : 

Use Cloud Monitoring (/monitoring) and service level indicators (SLIs) to track SLOs. Cloud Monitoring provides comprehensive monitoring and observability capabilities that enable your organization to collect and analyze metrics that are related to the availability, performance, and latency of cloud-based 

applications and services. SLIs are specific metrics that you can use to measure and track SLOs over time. By utilizing these tools, you can effectively monitor and manage cloud services, and ensure that they meet the SLOs and SLAs. 

Clearly defining, communicating, and tracking SLOs and SLAs for all of your critical cloud services helps to ensure reliability and performance of your deployed applications and services. 

#### Implement comprehensive observability

To get real-time visibility into the health and performance of your cloud environment, we recommend that you use a combination of Google Cloud Observability tools (https://cloud.google.com/products/observability) and third-party solutions. This recommendation is relevant to the _processes_ and _tooling_ focus areas of operational readiness (#focus-areas-of-operational-readiness). 

Implementing a combination of observability solutions provides you with a comprehensive observability strategy that covers various aspects of your cloud infrastructure and applications. Google Cloud Observability is a unified platform for collecting, analyzing, and visualizing metrics, logs, and traces from various Google Cloud services, applications, and external sources. By using Cloud Monitoring, you can gain insights into resource utilization, performance characteristics, and overall health of your resources. 

To ensure comprehensive monitoring, monitor important metrics that align with system health indicators such as CPU utilization, memory usage, network traffic, disk I/O, and application response times. You must also consider business-specific metrics. By tracking these metrics, you can identify potential bottlenecks, performance issues, and resource constraints. Additionally, you can set up alerts to notify relevant teams proactively about potential issues or anomalies. 

To enhance your monitoring capabilities further, you can integrate third-party solutions with Google Cloud Observability. These solutions can provide additional functionality, such as advanced analytics, machine learning-powered anomaly detection, and incident management capabilities. This combination of Google Cloud Observability tools and third-party solutions lets you create a robust and customizable monitoring ecosystem that's tailored to your specific needs. By using this combination approach, you can proactively identify and address issues, 

optimize resource utilization, and ensure the overall reliability and availability of your cloud applications and services. 

#### Implement performance and load testing

Performing regular performance testing helps you to ensure that your cloud-based applications and infrastructure can handle peak loads and maintain optimal performance. Load testing simulates realistic traffic patterns. Stress testing pushes the system to its limits to identify potential bottlenecks and performance limitations. This recommendation is relevant to the _processes_ and _tooling_ focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

- **Test performance** : Use Cloud Load Balancing (/load-balancing) and load testing services (/load-balancing/docs/backend-service-load-testing) to simulate realworld traffic patterns and stress-test your applications. These tools provide valuable insights into how your system behaves under various load conditions, and can help you to identify areas that require optimization. 

- **Optimize performance** : Based on the results of performance testing, you can make decisions to optimize your cloud infrastructure and applications for optimal performance and scalability. This optimization might involve adjusting resource allocation, tuning configurations, or implementing caching mechanisms. 

For example, if you find that your application is experiencing slowdowns during periods of high traffic, you might need to increase the number of virtual machines or containers that are allocated to the application. Alternatively, you might need to adjust the configuration of your web server or database to improve performance. 

By regularly conducting performance testing and implementing the necessary optimizations, you can ensure that your cloud-based applications and infrastructure always run at peak performance, and deliver a seamless and responsive experience for your users. Doing so can help you to maintain a competitive advantage and build trust with your customers. 

#### Plan and manage capacity

To keep your cloud systems running and scaling in response to changes in demand, you need to actively plan and manage capacity for the cloud resources. This recommendation supports the _processes_ and _tooling_ focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

- **Consider service limits and manage resource quotas** : To plan capacity for your cloud resources, start with the hard limits (the fixed constraints) for the services that you plan to use. 

   - Estimate the quota (/docs/quotas/view-manage) requirements for compute, storage, API limits and other resources that you need. Request suitable quota adjustments before you need the resources. 

   - Load metrics from Cloud Monitoring (/monitoring/docs/monitoring-overview) into BigQuery (/bigquery/docs/loading-data), and use the metrics to identify traffic patterns and track the system load over time. 

   - Forecast the demand for resources based on upcoming marketing campaigns, user signups, and feature rollouts. Also consider your current and planned SLA commitments. 

- **Design for flexibility and efficiency** : When you plan capacity for your cloud deployments, decouple application components from specific machine types. When you pin a workload to a single machine type, you can't take advantage of newer cloud hardware or changes in regional capacity. 

   - For workloads that need specialized hardware, such as high-memory instances or GPUs, ensure that you can obtain resources when required. Use future reservations (/compute/docs/instances/future-reservations-overview) to get an assurance of capacity for critical machine types up to a year ahead. 

   - For batch-processing or model-training workloads that can tolerate variable start times, schedule capacity dynamically by using Flex-start VMs (/compute/docs/instances/about-flex-start-vms). These VMs use Dynamic 

Workload Scheduling (DWS) to queue requests and reduce compute costs. 

- Avoid reserving older machine families or resources for transient development environments. 

- Plan for resources in secondary regions so that you can fail over efficiently for disaster recovery (DR). 

**Implement automatic scaling** : To dynamically adapt your cloud resources to real-time workload fluctuations, implement autoscaling policies. Autoscaling algorithms evaluate metrics such as CPU utilization, memory pressure, and queue depth. Based on the evaluation, resources are scaled out during peak traffic periods and scaled in during low-utilization windows, which helps to optimize the cost of your cloud resources. 

- Configure managed instance groups (MIGs) 

- (/compute/docs/instance-groups/about-instance-flexibility) with mixed instance templates that combine current and newer generations of machine types. 

- Ensure that your MIG configurations include both instance flexibility (specifying multiple compatible machine types) and location flexibility (spreading targets across multiple zones in a region). Depending on the current capacity requirements, your system automatically provisions the next preferred machine type from your fallback list without dropping requests or limiting compute resources. 

#### Continuously monitor and optimize

To manage and optimize cloud workloads, you must establish a process for continuously monitoring and analyzing performance metrics. This recommendation is relevant to the _processes_ and _tooling_ focus areas of operational readiness (/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

**Track and gather data** : 

To establish a process for continuous monitoring and analysis, you need to track, collect, and evaluate data that's related to various aspects of your cloud 

environment. By using this data, you can proactively identify areas for improvement, optimize resource utilization, and ensure that your cloud infrastructure consistently meets or exceeds your performance expectations. 

**Review logs and traces** : 

Logs provide valuable insights into system events, errors, and warnings. Traces provide detailed information about the flow of requests through your application. By analyzing logs and traces, you can identify potential issues, identify the root causes of problems, and get a better understanding of how your applications behave under different conditions. Metrics like the round-trip time between services can help you to identify and understand bottlenecks that are in your workloads. 

**Tune for performance** : 

Use performance-tuning techniques to significantly optimize application response times and overall efficiency. The following are examples of techniques that you can use: 

- **Caching** : Store frequently accessed data in memory to reduce the need for repeated database queries or API calls. 

- **Database optimization** : Use techniques like indexing and query optimization to improve the performance of database operations. 

- **Code profiling** : Identify areas of your code that consume excessive resources or cause performance issues. 

## Manage incidents and problems

This principle in the operational excellence pillar of the Google Cloud WellArchitected Framework (/architecture/framework) provides recommendations to help you manage incidents and problems related to your cloud workloads. It involves implementing comprehensive monitoring and observability, establishing clear incident response procedures, conducting thorough root cause analysis, and implementing preventive measures. Many of the topics that are discussed in this principle are covered in detail in the Reliability (/architecture/framework/reliability) pillar. 

### Principle overview

Incident management and problem management are important components of a functional operations environment. How you respond to, categorize, and solve incidents of differing severity can significantly affect your operations. You must also proactively and continuously make adjustments to optimize reliability and performance. An efficient process for incident and problem management relies on the following foundational elements: 

- **Continuous monitoring** : Identify and resolve issues quickly. 

- **Automation** : Streamline tasks and improve efficiency. 

- **Orchestration** : Coordinate and manage cloud resources effectively. 

- **Data-driven insights** : Optimize cloud operations and make informed decisions. 

These elements help you to build a resilient cloud environment that can handle a wide range of challenges and disruptions. These elements can also help to reduce the risk of costly incidents and downtime, and they can help you to achieve greater business agility and success. These foundational elements are spread across the four focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) : Workforce, Processes, Tooling, and Governance. 

**Note:** The Google SRE Book (https://sre.google/workbook/table-of-contents/) defines many of the terms and concepts that are described in this document. We recommend the Google SRE Book as supplemental reading to support the recommendations that are described in this document. 

### Recommendations

To manage incidents and problems effectively, consider the recommendations in the following sections. Each recommendation in this document is relevant to one or more of the focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

#### Establish clear incident response procedures

Clear roles and responsibilities are essential to ensure effective and coordinated response to incidents. Additionally, clear communication protocols and escalation paths help to ensure that information is shared promptly and effectively during an incident. This recommendation is relevant to these focus areas of operational 

readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

: workforce, processes, and tooling. 

To establish incident response procedures, you need to define the roles and expectations of each team member, such as incident commanders, investigators, communicators, and technical experts. Establishing communication and escalation paths includes identifying important contacts, setting up communication channels, and defining the process for escalating incidents to higher levels of management when necessary. Regular training and preparation helps to ensure that teams are equipped with the knowledge and skills to respond to incidents effectively. 

By documenting incident response procedures in a runbook or playbook, you can provide a standardized reference guide for teams to follow during an incident. The runbook must outline the steps to be taken at each stage of the incident response process, including communication, triage, investigation, and resolution. It must also include information about relevant tools and resources and contact information for important personnel. You must regularly review and update the runbook to ensure that it remains current and effective. 

#### Centralize incident management

For effective tracking and management throughout the incident lifecycle, consider using a centralized incident management system. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) : processes and tooling. 

- A centralized incident management system provides the following advantages: 

   - **Improved visibility** : By consolidating all incident-related data in a single location, you eliminate the need for teams to search in various channels or systems for context. This approach saves time and reduces confusion, and it gives stakeholders a comprehensive view of the incident, including its status, impact, and progress. 

   - **Better coordination and collaboration** : A centralized system provides a unified platform for communication and task management. It promotes seamless collaboration between the different departments and functions that are involved in incident response. This approach ensures that everyone has access to up-to-date information and it reduces the risk of miscommunication and misalignment. 

   - **Enhanced accountability and ownership** : A centralized incident management system enables your organization to allocate tasks to specific individuals or teams and it ensures that responsibilities are clearly defined and tracked. This approach promotes accountability and encourages proactive problem-solving because team members can easily monitor their progress and contributions. 

A centralized incident management system must offer robust features for incident tracking, task assignment, and communication management. These features let you customize workflows, set priorities, and integrate with other systems, such as monitoring tools and ticketing systems. 

By implementing a centralized incident management system, you can optimize your organization's incident response processes, improve collaboration, and enhance visibility. Doing so leads to faster incident resolution times, reduced downtime, and improved customer satisfaction. It also helps foster a culture of continuous improvement because you can learn from past incidents and identify areas for improvement. 

#### Conduct thorough post-incident reviews

After an incident occurs, you must conduct a detailed post-incident review (PIR), which is also known as a postmortem (https://sre.google/workbook/postmortem-culture/), to identify the root cause, contributing factors, and lessons learned. This thorough 

review helps you to prevent similar incidents in the future. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

: processes and governance. 

The PIR process must involve a multidisciplinary team that has expertise in various aspects of the incident. The team must gather all of the relevant information through interviews, documentation review, and site inspections. A timeline of events must be created to establish the sequence of actions that led up to the incident. 

After the team gathers the required information, they must conduct a root cause analysis to determine the factors that led to the incident. This analysis must identify both the immediate cause and the systemic issues that contributed to the incident. 

Along with identifying the root cause, the PIR team must identify any other contributing factors that might have caused the incident. These factors could include human error, equipment failure, or organizational factors like communication breakdowns and lack of training. 

The PIR report must document the findings of the investigation, including the timeline of events, root cause analysis, and recommended actions. The report is a valuable resource for implementing corrective actions and preventing recurrence. The report must be shared with all of the relevant stakeholders and it must be used to develop safety training and procedures. 

To ensure a successful PIR process, your organization must foster a blameless culture that focuses on learning and improvement rather than assigning blame. This culture encourages individuals to report incidents without fear of retribution, and it lets you address systemic issues and make meaningful improvements. 

By conducting thorough PIRs and implementing corrective measures based on the findings, you can significantly reduce the risk of similar incidents occurring in the future. This proactive approach to incident investigation and prevention helps to create a safer and more efficient work environment for everyone involved. 

#### Maintain a knowledge base

A knowledge base of known issues, solutions, and troubleshooting guides is essential for incident management and resolution. Team members can use the knowledge base to quickly identify and address common problems. Implementing a knowledge base helps to reduce the need for escalation and it improves overall efficiency. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) : workforce and processes. 

A primary benefit of a knowledge base is that it lets teams learn from past experiences and avoid repeating mistakes. By capturing and sharing solutions to known issues, teams can build a collective understanding of how to resolve common problems and best practices for incident management. Use of a knowledge base saves time and effort, and helps to standardize processes and ensure consistency in incident resolution. 

Along with helping to improve incident resolution times, a knowledge base promotes knowledge sharing and collaboration across teams. With a central repository of information, teams can easily access and contribute to the knowledge base, which promotes a culture of continuous learning and improvement. This culture encourages teams to share their expertise and experiences, leading to a more comprehensive and valuable knowledge base. 

To create and manage a knowledge base effectively, use appropriate tools and technologies. Collaboration platforms like Google Workspace (https://workspace.google.com/) are well-suited for this purpose because they let you easily create, edit, and share documents collaboratively. These tools also support version control and change tracking, which ensures that the knowledge base remains up-to-date and accurate. 

Make the knowledge base easily accessible to all relevant teams. You can achieve this by integrating the knowledge base with existing incident management systems or by providing a dedicated portal or intranet site. A knowledge base that's readily available lets teams quickly access the information that they need to resolve incidents efficiently. This availability helps to reduce downtime and minimize the impact on business operations. 

Regularly review and update the knowledge base to ensure that it remains relevant and useful. Monitor incident reports, identify common issues and trends, and incorporate new solutions and troubleshooting guides into the knowledge base. An up-to-date knowledge base helps your teams resolve incidents faster and more effectively. 

#### Automate incident response

Automation helps to streamline your incident response and remediation processes. It lets you address security breaches and system failures promptly and efficiently. By using Google Cloud products like Cloud Run functions (/functions) or Cloud Run (/run), you can automate various tasks that are typically manual and timeconsuming. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) : processes and tooling. 

Automated incident response provides the following benefits: 

**Reduction in incident detection and resolution times** : Automated tools can continuously monitor systems and applications, detect suspicious or anomalous activities in real time, and notify stakeholders or respond without intervention. This automation lets you identify potential threats or issues before they escalate into major incidents. When an incident is detected, automated tools can trigger predefined remediation actions, such as isolating affected systems, quarantining malicious files, or rolling back changes to restore the system to a known good state. 

**Reduced burden on security and operations teams** : Automated incident response lets the security and operations teams focus on more strategic tasks. By automating routine and repetitive tasks, such as collecting diagnostic information or triggering alerts, your organization can free up personnel to handle more complex and critical incidents. This automation can lead to improved overall incident response effectiveness and efficiency. 

**Enhanced consistency and accuracy of the remediation process** : Automated tools can ensure that remediation actions are applied uniformly across all affected systems, minimizing the risk of human error or 

inconsistency. This standardization of the remediation process helps to minimize the impact of incidents on users and the business. 

## Manage and optimize cloud resources

This principle in the operational excellence pillar of the Google Cloud WellArchitected Framework (/architecture/framework) provides recommendations to help you manage and optimize the resources that are used by your cloud workloads. It involves right-sizing resources based on actual usage and demand, using autoscaling for dynamic resource allocation, implementing cost optimization strategies, and regularly reviewing resource utilization and costs. Many of the topics that are discussed in this principle are covered in detail in the Cost optimization (/architecture/framework/cost-optimization) pillar. 

### Principle overview

Cloud resource management and optimization play a vital role in optimizing cloud spending, resource usage, and infrastructure efficiency. It includes various strategies and best practices aimed at maximizing the value and return from your cloud spending. 

This pillar's focus on optimization extends beyond cost reduction. It emphasizes the following goals: 

- **Efficiency** : Using automation and data analytics to achieve peak performance and cost savings. 

- **Performance** (/architecture/framework/performance-optimization): Scaling resources effortlessly to meet fluctuating demands and deliver optimal results. 

- **Scalability** : Adapting infrastructure and processes to accommodate rapid growth and diverse workloads. 

By focusing on these goals, you achieve a balance between cost and functionality. You can make informed decisions regarding resource provisioning, scaling, and migration. Additionally, you gain valuable insights into resource consumption patterns, which lets you proactively identify and address potential issues before they escalate. 

### Recommendations

To manage and optimize resources, consider the recommendations in the following sections. Each recommendation in this document is relevant to one or more of the focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

#### Right-size resources

Continuously monitoring resource utilization and adjusting resource allocation to match actual demand are essential for efficient cloud resource management. Overprovisioning resources can lead to unnecessary costs, and under-provisioning can cause performance bottlenecks that affect application performance and user experience. To achieve an optimal balance, you must adopt a proactive approach to right-sizing cloud resources. This recommendation is relevant to the governance focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

Cloud Monitoring (https://cloud.google.com/monitoring) and Recommender 

(https://cloud.google.com/recommender) can help you to identify opportunities for right-sizing. Cloud Monitoring provides real-time visibility into resource utilization metrics. This visibility lets you track resource usage patterns and identify potential inefficiencies. Recommender analyzes resource utilization data to make intelligent recommendations for optimizing resource allocation. By using these tools, you can gain insights into resource usage and make informed decisions about right-sizing the resources. 

In addition to Cloud Monitoring and Recommender, consider using custom metrics to trigger automated right-sizing actions. Custom metrics let you track specific resource utilization metrics that are relevant to your applications and workloads. You can also configure alerts to notify administrators when predefined thresholds are met. The administrators can then take necessary actions to adjust resource allocation. This proactive approach ensures that resources are scaled in a timely manner, which helps to optimize cloud costs and prevent performance issues. 

#### Use autoscaling

Autoscaling compute and other resources helps to ensure optimal performance and cost efficiency of your cloud-based applications. Autoscaling lets you dynamically adjust the capacity of your resources based on workload fluctuations, so that you have the resources that you need when you need them and you can avoid overprovisioning and unnecessary costs. This recommendation is relevant to the processes focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

To meet the diverse needs of different applications and workloads, Google Cloud offers various autoscaling options, including the following: 

Compute Engine managed instance groups (MIGs) 

(/compute/docs/instance-groups#managed_instance_groups) are groups of VMs that are managed and scaled as a single entity. With MIGs, you can define autoscaling policies that specify the minimum and maximum number of VMs to maintain in the group, and the conditions that trigger autoscaling. For example, you can configure a policy to add VMs in a MIG when the CPU utilization reaches a certain threshold and to remove VMs when the utilization drops below a different threshold. 

Google Kubernetes Engine (GKE) autoscaling 

- (/kubernetes-engine/docs/concepts/cluster-autoscaler) dynamically adjusts your cluster resources to match your application's needs. It offers the following tools: 

   - Cluster Autoscaler adds or removes nodes based on Pod resource demands. 

- Horizontal Pod Autoscaler changes the number of Pod replicas based on CPU, memory, or custom metrics. 

- Vertical Pod Autoscaler fine-tunes Pod resource requests and limits based on usage patterns. 

- Node Auto-Provisioning automatically creates optimized node pools for your workloads. 

These tools work together to optimize resource utilization, ensure application performance, and simplify cluster management. 

- Cloud Run (https://cloud.google.com/run) is a serverless platform that lets you run code without having to manage infrastructure. Cloud Run offers built-in autoscaling, which automatically adjusts the number of instances based on the incoming traffic. When the volume of traffic increases, Cloud Run scales up the number of instances to handle the load. When traffic decreases, Cloud Run scales down the number of instances to reduce costs. 

By using these autoscaling options, you can ensure that your cloud-based applications have the resources that they need to handle varying workloads, while avoiding overprovisioning and unnecessary costs. Using autoscaling can lead to improved performance, cost savings, and more efficient use of cloud resources. 

#### Leverage cost optimization strategies

Optimizing cloud spending helps you to effectively manage your organization's IT budgets. This recommendation is relevant to the governance focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

Google Cloud offers several tools and techniques to help you optimize cloud costs. By using these tools and techniques, you can get the best value from your cloud spending. These tools and techniques help you to identify areas where costs can be reduced, such as identifying underutilized resources or recommending more costeffective instance types. Google Cloud options to help optimize cloud costs include the following: 

- Committed use discounts (CUDs) (/docs/cuds) are discounts for committing to a certain level of usage over a period of time. 

- Sustained use discounts (/compute/docs/sustained-use-discounts) in Compute Engine provide discounts for consistent usage of a service. 

Spot VMs (/compute/docs/instances/spot) provide access to unused VM capacity at a lower cost compared to regular VMs. 

Pricing models might change over time, and new features might be introduced that offer better performance or lower cost compared to existing options. Therefore, you should regularly review pricing models and consider alternative features. By staying informed about the latest pricing models and features, you can make informed decisions about your cloud architecture to minimize costs. 

Google Cloud's Cost Management (https://cloud.google.com/cost-management) tools, such as budgets and alerts, provide valuable insights into cloud spending. Budgets and alerts let users set budgets and receive alerts when the budgets are exceeded. These tools help users track their cloud spending and identify areas where costs can be reduced. 

#### Track resource usage and costs

You can use tagging and labeling to track resource usage and costs. By assigning tags and labels to your cloud resources like projects, departments, or other relevant dimensions, you can categorize and organize the resources. This lets you monitor and analyze spending patterns for specific resources and identify areas of high usage or potential cost savings. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) : governance and tooling. 

Tools like Cloud Billing and Cost Management help you to get a comprehensive understanding of your spending patterns. These tools provide detailed insights into your cloud usage and they let you identify trends, forecast costs, and make informed decisions. By analyzing historical data and current spending patterns, you can identify the focus areas for your cost-optimization efforts. 

Custom dashboards and reports help you to visualize cost data and gain deeper insights into spending trends. By customizing dashboards with relevant metrics and dimensions, you can monitor key performance indicators (KPIs) and track progress towards your cost optimization goals. Reports offer deeper analyses of cost data. Reports let you filter the data by specific time periods or resource types to understand the underlying factors that contribute to your cloud spending. 

Regularly review and update your tags, labels, and cost analysis tools to ensure that you have the most up-to-date information on your cloud usage and costs. By staying informed and conducting cost postmortems or proactive cost reviews, you can promptly identify any unexpected increases in spending. Doing so lets you make proactive decisions to optimize cloud resources and control costs. 

#### Establish cost allocation and budgeting

Accountability and transparency in cloud cost management are crucial for optimizing resource utilization and ensuring financial control. This recommendation is relevant to the governance focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

To ensure accountability and transparency, you need to have clear mechanisms for cost allocation and chargeback. By allocating costs to specific teams, projects, or individuals, your organization can ensure that each of these entities is responsible for its cloud usage. This practice fosters a sense of ownership and encourages responsible resource management. Additionally, chargeback mechanisms enable your organization to recover cloud costs from internal customers, align incentives with performance, and promote fiscal discipline. 

Establishing budgets for different teams or projects is another essential aspect of cloud cost management. Budgets enable your organization to define spending limits and track actual expenses against those limits. This approach lets you make proactive decisions to prevent uncontrolled spending. By setting realistic and achievable budgets, you can ensure that cloud resources are used efficiently and aligned with business objectives. Regular monitoring of actual spending against budgets helps you to identify variances and address potential overruns promptly. 

To monitor budgets, you can use tools like Cloud Billing budgets and alerts (/billing/docs/how-to/budgets). These tools provide real-time insights into cloud spending and they notify stakeholders of potential overruns. By using these capabilities, you can track cloud costs and take corrective actions before significant deviations occur. This proactive approach helps to prevent financial surprises and ensures that cloud resources are used responsibly. 

## Automate and manage change

This principle in the operational excellence pillar of the Google Cloud WellArchitected Framework (/architecture/framework) provides recommendations to help you automate and manage change for your cloud workloads. It involves implementing infrastructure as code (IaC), establishing standard operating procedures, implementing a structured change management process, and using automation and orchestration. 

### Principle overview

Change management and automation play a crucial role in ensuring smooth and controlled transitions within cloud environments. For effective change management, you need to use strategies and best practices that minimize disruptions and ensure that changes are integrated seamlessly with existing systems. 

Effective change management and automation include the following foundational elements: 

- **Change governance** : Establish clear policies and procedures for change management, including approval processes and communication plans. 

- **Risk assessment** : Identify potential risks associated with changes and mitigate them through risk management techniques. 

- **Testing and validation** : Thoroughly test changes to ensure that they meet functional and performance requirements and mitigate potential regressions. 

**Controlled deployment** : Implement changes in a controlled manner, ensuring that users are seamlessly transitioned to the new environment, with mechanisms to seamlessly roll back if needed. 

These foundational elements help to minimize the impact of changes and ensure that changes have a positive effect on business operations. These elements are represented by the processes, tooling, and governance focus areas of operational 

readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

### Recommendations

To automate and manage change, consider the recommendations in the following sections. Each recommendation in this document is relevant to one or more of the focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

#### Adopt IaC

Infrastructure as code (IaC) is a transformative approach for managing cloud infrastructure. You can define and manage cloud infrastructure declaratively by using tools like Terraform (/docs/terraform/iac-overview). IaC helps you achieve consistency, repeatability, and simplified change management. It also enables faster and more reliable deployments. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

: processes and tooling. 

The following are the main benefits of adopting the IaC approach for your cloud deployments: 

**Human-readable resource configurations** : With the IaC approach, you can declare your cloud infrastructure resources in a human-readable format, like 

JSON or YAML. Infrastructure administrators and operators can easily understand and modify the infrastructure and collaborate with others. 

- **Consistency and repeatability** : IaC enables consistency and repeatability in your infrastructure deployments. You can ensure that your infrastructure is provisioned and configured the same way every time, regardless of who is performing the deployment. This approach helps to reduce errors and ensures that your infrastructure is always in a known state. 

- **Accountability and simplified troubleshooting** : The IaC approach helps to improve accountability and makes it easier to troubleshoot issues. By storing your IaC code in a version control system, you can track changes, and identify when changes were made and by whom. If necessary, you can easily roll back to previous versions. 

#### Implement version control

A version control system like Git is a key component of the IaC process. It provides robust change management and risk mitigation capabilities, which is why it's widely adopted, either through in-house development or SaaS solutions. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) : governance and tooling. 

By tracking changes to IaC code and configurations, version control provides visibility into the evolution of the code, making it easier to understand the impact of changes and identify potential issues. This enhanced visibility fosters collaboration among team members who work on the same IaC project. 

Most version control systems let you easily roll back changes if needed. This capability helps to mitigate the risk of unintended consequences or errors. By using tools like Git in your IaC workflow, you can significantly improve change management processes, foster collaboration, and mitigate risks, which leads to a more efficient and reliable IaC implementation. 

#### Build CI/CD pipelines

Continuous integration and continuous delivery (CI/CD) pipelines streamline the process of developing and deploying cloud applications. CI/CD pipelines automate the building, testing, and deployment stages, which enables faster and more frequent releases with improved quality control. This recommendation is relevant to the tooling focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

CI/CD pipelines ensure that code changes are continuously integrated into a central repository, typically a version control system like Git. Continuous integration facilitates early detection and resolution of issues, and it reduces the likelihood of bugs or compatibility problems. 

To create and manage CI/CD pipelines for cloud applications, you can use tools like Cloud Build (/build)and Cloud Deploy (/deploy). 

- **Cloud Build** is a fully managed build service that lets developers define and execute build steps in a declarative manner. It integrates seamlessly with popular source-code management platforms and it can be triggered by events like code pushes and pull requests. 

- **Cloud Deploy** is a serverless deployment service that automates the process of deploying applications to various environments, such as testing, staging, and production. It provides features like blue-green deployments, traffic splitting, and rollback capabilities, making it easier to manage and monitor application deployments. 

Integrating CI/CD pipelines with version control systems and testing frameworks helps to ensure the quality and reliability of your cloud applications. By running automated tests as part of the CI/CD process, development teams can quickly identify and fix any issues before the code is deployed to the production environment. This integration helps to improve the overall stability and performance of your cloud applications. 

#### Use configuration management tools

Tools like Puppet, Chef, Ansible, and VM Manager (/compute/docs/vm-manager) help you to automate the configuration and management of cloud resources. Using 

these tools, you can ensure resource consistency and compliance across your cloud environments. This recommendation is relevant to the tooling focus area of 

operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

Automating the configuration and management of cloud resources provides the following benefits: 

- **Significant reduction in the risk of manual errors** : When manual processes are involved, there is a higher likelihood of mistakes due to human error. Configuration management tools reduce this risk by automating processes, so that configurations are applied consistently and accurately across all cloud resources. This automation can lead to improved reliability and stability of the cloud environment. 

- **Improvement in operational efficiency** : By automating repetitive tasks, your organization can free up IT staff to focus on more strategic initiatives. This automation can lead to increased productivity and cost savings and improved responsiveness to changing business needs. 

- **Simplified management of complex cloud infrastructure** : As cloud environments grow in size and complexity, managing the resources can become increasingly difficult. Configuration management tools provide a centralized platform for managing cloud resources. The tools make it easier to track configurations, identify issues, and implement changes. Using these tools can lead to improved visibility, control, and security of your cloud environment. 

#### Automate testing

Integrating automated testing into your CI/CD pipelines helps to ensure the quality and reliability of your cloud applications. By validating changes before deployment, you can significantly reduce the risk of errors and regressions, which leads to a more stable and robust software system. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) : processes and tooling. 

The following are the main benefits of incorporating automated testing into your CI/CD pipelines: 

- **Early detection of bugs and defects** : Automated testing helps to detect bugs and defects early in the development process, before they can cause major problems in production. This capability saves time and resources by preventing the need for costly rework and bug fixes at later stages in the development process. 

- **High quality and standards-based code** : Automated testing can help improve the overall quality of your code by ensuring that the code meets certain standards and best practices. This capability leads to more maintainable and reliable applications that are less prone to errors. 

You can use various types of testing techniques in CI/CD pipelines. Each test type serves a specific purpose. 

- **Unit testing** focuses on testing individual units of code, such as functions or methods, to ensure that they work as expected. 

- **Integration testing** tests the interactions between different components or modules of your application to verify that they work properly together. 

- **End-to-end testing** is often used along with unit and integration testing. End-to-end testing simulates real-world scenarios to test the application as a whole, and helps to ensure that the application meets the requirements of your end users. 

To effectively integrate automated testing into your CI/CD pipelines, you must choose appropriate testing tools and frameworks. There are many different options, each with its own strengths and weaknesses. You must also establish a clear testing strategy that outlines the types of tests to be performed, the frequency of testing, and the criteria for passing or failing a test. By following these recommendations, you can ensure that your automated testing process is efficient and effective. Such a process provides valuable insights into the quality and reliability of your cloud applications. 

## Continuously improve and innovate

This principle in the operational excellence pillar of the Google Cloud WellArchitected Framework (/architecture/framework) provides recommendations to help you continuously optimize cloud operations and drive innovation. 

### Principle overview

To continuously improve and innovate in the cloud, you need to focus on continuous learning, experimentation, and adaptation. This helps you to explore new technologies and optimize existing processes and it promotes a culture of excellence that enables your organization to achieve and maintain industry leadership. 

Through continuous improvement and innovation, you can achieve the following goals: 

- **Accelerate innovation** : Explore new technologies and services to enhance capabilities and drive differentiation. 

- **Reduce costs** : Identify and eliminate inefficiencies through processimprovement initiatives. 

- **Enhance agility** : Adapt rapidly to changing market demands and customer needs. 

- **Improve decision making** : Gain valuable insights from data and analytics to make data-driven decisions. 

Organizations that embrace the continuous improvement and innovation principle can unlock the full potential of the cloud environment and achieve sustainable growth. This principle maps primarily to the Workforce focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

. A culture of innovation lets teams experiment with new tools and technologies to expand capabilities and reduce costs.
