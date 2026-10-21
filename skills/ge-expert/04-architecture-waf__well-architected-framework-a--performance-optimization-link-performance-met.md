# Architecture: Well-Architected Framework and reference designs / Well-Architected Framework: AI and ML perspective: AI and ML perspective: Performance optimization: Link performance metrics to design and configuration choices to AI and ML perspective: Performance optimization: Contributors to Agentic AI architecture guides
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 384-423, extracted 2026-10-18

Contains:
- Well-Architected Framework: AI and ML perspective: AI and ML perspective: Performance optimization: Link performance metrics to design and configuration choices to AI and ML perspective: Performance optimization: Contributors (pages 384-391) https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable
- Google Cloud deployment archetypes (pages 392-396) https://docs.cloud.google.com/architecture/deployment-archetypes
- Comparative analysis of Google Cloud deployment archetypes (pages 397-404) https://docs.cloud.google.com/architecture/deployment-archetypes/comparison
- RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform (pages 405-420) https://docs.cloud.google.com/architecture/rag-genai-gemini-enterprise-vertexai
- Agentic AI architecture guides (pages 421-423) https://docs.cloud.google.com/architecture/agentic-ai-overview

## Well-Architected Framework: AI and ML perspective

URL: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable

### Link performance metrics to design and configuration choices

To innovate, troubleshoot, and investigate performance issues, you must establish a clear link between design choices and performance outcomes. You need a reliable record of the lineage of ML assets, deployments, model outputs, and the corresponding configurations and inputs that produced the outputs. 

#### Build a data and model lineage system

To reliably improve performance, you need the ability to trace every model version back to the exact data, code, and configurations that were used to produce the model. As you scale a model, such tracing becomes difficult. You need a lineage system that automates the tracing process and creates a record that's clear and can be queried for every experiment. This system lets your teams efficiently identify and reproduce the choices that lead to the optimally performing models. 

To view and analyze the lineage of pipeline artifacts for workloads in Agent Platform, you can use Agent Platform ML Metadata 

(/gemini-enterprise-agent-platform/machine-learning/ml-metadata/introduction) or Knowledge Catalog (/dataplex/docs/introduction). Both options let you register events or artifacts to meet governance requirements and to query the metadata and retrieve information when needed. This section provides an overview of the two options. For detailed information about the differences between Agent Platform ML Metadata and Knowledge Catalog, see Track the lineage of pipeline artifacts 

(/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage). 

Default implementation: Agent Platform ML Metadata 

Your first pipeline run or _experiment_ in Agent Platform creates a default Agent Platform ML Metadata service. The parameters and artifact metadata that the pipeline consumes and generates are automatically registered to a Agent Platform ML Metadata store. The data model 

(/gemini-enterprise-agent-platform/machine-learning/ml-metadata/data-model) that's used to organize and connect the stored metadata contains the following elements: 

**Context** : A group of artifacts and executions that represents an experimentation run. 

**Execution** : A step in a workflow, like data validation or model training. 

- **Artifact** : An input or output entity, object, or piece of data that a workflow produces and consumes. 

**Event** : A relationship between an artifact and an execution. 

By default, Agent Platform ML Metadata captures and tracks 

(/gemini-enterprise-agent-platform/machine-learning/ml-metadata/tracking) all input and output artifacts of a pipeline run. It integrates these artifacts with Experiments on Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments) , Model Registry 

(/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction), and Agent Platform managed datasets 

(/gemini-enterprise-agent-platform/machine-learning/datasets/overview). 

Autologging 

(/gemini-enterprise-agent-platform/machine-learning/experiments/run-training-jobexperiments) 

is a built-in feature in Agent Platform Managed Training to automatically log data to Experiments on Agent Platform. To efficiently track experiments for optimizing performance, use the built-in integrations between Experiments on Agent Platform and the associated Agent Platform ML Metadata service. 

Agent Platform ML Metadata provides a filtering syntax and operators to run queries about artifacts, executions, and contexts. When required, your teams can efficiently retrieve information about a model's registry link and its dataset or evaluation for a specific experiment run. This metadata can help to accelerate the discovery of choices that optimize performance. For example, you can compare pipeline runs 

(/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-comparepipeline-runs) 

, compare models 

(/gemini-enterprise-agent-platform/machine-learning/experiments/user-journey/uj-comparemodels) 

, and compare experiment runs 

(/gemini-enterprise-agent-platform/machine-learning/experiments/compare-analyze-runs). For more information, including example queries, see Analyze metadata 

(/gemini-enterprise-agent-platform/machine-learning/ml-metadata/analyzing#inputs-andoutputs) 

Alternative implementation: Knowledge Catalog 

Knowledge Catalog discovers metadata from Google Cloud resources (/dataplex/docs/catalog-overview#supported-sources), including Agent Platform artifacts. You can also integrate a custom data source (/dataplex/docs/ingest-custom-sources). 

Knowledge Catalog can read metadata across multiple regions and organizationwide stores, whereas Agent Platform ML Metadata is a project-specific resource. When compared to Agent Platform ML Metadata, Knowledge Catalog involves more setup effort. However, Knowledge Catalog might be appropriate when you need integration with your wider data portfolio in Google Cloud and with organizationwide stores. 

Knowledge Catalog discovers and harvests metadata for projects where the Data Lineage API is enabled. The metadata in the catalog is organized by using a data model (/dataplex/docs/catalog-overview#supported-sources) that consists of projects, entry groups, entries, and aspects. Knowledge Catalog provides a specific syntax (/dataplex/docs/search-syntax) that you can use to discover artifacts. If required, you can map metadata artifacts 

(/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage#map_artifacts_to_fqn) to Knowledge Catalog. 

#### Use explainability tools

The behavior of an AI model is based on data that was used to train the model. This behavior is encoded as parameters 

(https://developers.google.com/machine-learning/glossary#parameter) in mathematical functions. Understanding exactly _why_ a model performs in a certain way can be difficult. However, this knowledge is critical for performance optimization. 

For example, consider an image classification model where the training data contains images of only red cars. The model might learn to identify the "car" label based on the color of the object rather than the object's spatial and shape attributes. When the model is tested with images that show cars of different colors, the performance of the model might degrade. The following sections describe tools that you can use to identify and diagnose such problems. 

Detect data biases 

In the exploratory data analysis (EDA) phase of an ML project, you identify issues with the data, such as class-imbalanced datasets 

(https://developers.google.com/machine- 

learning/glossary/fundamentals#class_imbalanced_data_set) and biases 

(https://developers.google.com/machine-learning/glossary/fundamentals#bias-ethicsfairness). 

In production systems, you often retrain models and run experiments with different datasets. To standardize data and compare across experiments, we recommend a systematic approach to EDA that includes the following characteristics: 

- **Automation** : As a training set grows in size, the EDA process must run automatically in the background. 

**Wide coverage** : When you add new features, the EDA must reveal insights about the new features. 

Many EDA tasks are specific to the data type and the business context. To automate the EDA process, use BigQuery or a managed data processing service like Dataflow. For more information, see Classifcation on imbalanced datai (https://www.tensorflow.org/tutorials/structured_data/imbalanced_data) and Data bias metrics for Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/evaluation/data-bias-metrics). 

Understand model characteristics and behavior 

In addition to understanding the distribution of data in the training and validation sets and their biases, you need to understand a model's characteristics and behavior at prediction time. To understand model behavior, use the following tools: 

|Tool|Description<br>|Purposes|
|---|---|---|
|Example-based<br>explanations|You can use example-based explanations<br>or nearest-neighbor search to understand<br>a prediction by finding the most similar<br>examples from the training data. This<br>approach is based on the principle that<br>similar inputs yield similar outputs.|Identify and fix gaps in the<br>training data by finding similar<br>examples for an incorrect<br>prediction.<br>Classify inputs that the model<br>was not originally trained to<br>recognize, by using<br>neighbors<br>(https://en.wikipedia.org/wiki/K<br>nearest_neighbors_algorithm)<br>from a reference set.|
|||Identify anomalies by finding<br>inputs that are significantly<br>different from all of the known<br>training examples.|
|||Make data collection more<br>efficient by identifying<br>ambiguous cases, like when<br>neighbors have mixed labels.<br>Prioritize such cases for human<br>review.|

|Tool|Description<br>|Purposes|
|---|---|---|
|Feature-based<br>explanations|For predictions that are based on tabular<br>data or images, feature-based<br>explanations show how much each<br>feature<br>(https://developers.google.com/machine-<br>learning/glossary/fundamentals#feature)<br>affects a prediction when it's compared<br>to a baseline.<br>Explainability techniques and<br>tabular<br>explanations<br>(/gemini-enterprise-agent-<br>platform/machine-learning/tabular-<br>data/classification-explanations)<br>provide feature attribution methods<br>depending on the model type and task.<br>The methods typically rely on sampling<br>and sensitivity analysis to measure how<br>much the output changes in response to<br>changes in an input feature.|Identify biases that a validation<br>step might miss.<br>Optimize performance by<br>identifying the features that ar<br>most important for a prediction<br>To increase a model's quality<br>and performance, ML engineer<br>can intentionally add, remove,<br>or engineer features.|
|What-If Tool<br>(https://pair-<br>code.github.io/wh<br>if-tool)|at-<br>The What-If Tool was developed by<br>Google's<br>People + AI Research (PAIR)<br>initiative(https://pair.withgoogle.com/) to<br>help you understand and visualize the<br>behavior of image and tabular models.<br>For examples of using the tool, see<br>What-<br>If Tool Web Demos<br>(https://pair-code.github.io/what-if-<br>tool/explore/)<br>.|Debug and find the root cause<br>of incorrect predictions.<br>Investigate how a model<br>performs across different<br>subsets of data by identifying<br>biases through a fairness<br>analysis.<br>Understand a model's behavio<br>particularly the relationship<br>between a model's predictions<br>and input features.<br>Compare predictions by using<br>visual comparison tool that<br>requires either two models or a<br>ground truth baseline.|

### Contributors

Authors: 

- Benjamin Sadik (https://www.linkedin.com/in/benjaminhaimsadik) | AI and ML Specialist Customer Engineer 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

Other contributors: 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

Last updated 2025-02-14 UTC. 



## Google Cloud deployment archetypes

URL: https://docs.cloud.google.com/architecture/deployment-archetypes

Last reviewed 2026-09-09 UTC 

As a cloud architect or decision maker, when you plan to deploy an application in Google Cloud, you need to choose a _deployment archetyp_ _e_ 1 (#fn1) that's suitable for your application. This guide describes six deployment archetypes—zonal, regional, multi-regional, global, hybrid, and multicloud—and presents use cases and design considerations for each deployment archetype. The guide also provides a comparative analysis to help you choose the deployment archetypes that meet your requirements for availability, cost, performance, and operational efficiency. 

### What is a deployment archetype?

A deployment archetype is an abstract, provider-independent model that you use as the foundation to build application-specific _deployment architectures_ that meet your business and technical requirements. Each deployment archetype specifies a combination of failure domains where an application can run. These failure domains can be one or more Google Cloud zones or regions 

(/architecture/infra-reliability-guide/building-blocks#regions_and_zones), and they can extend to include your on-premises data centers or failure domains in other cloud providers. 

The following diagram shows six applications deployed in Google Cloud. Each application uses a deployment archetype that meets its specific requirements. 

As the preceding diagram shows, in an architecture that uses the hybrid or multicloud deployment archetype, the cloud topology is based on one of the _basic_ archetypes: zonal, regional, multi-regional, or global. In this sense, the hybrid and multicloud deployment archetypes can be considered as _composite_ deployment archetypes that include one of the basic archetypes. 

**Note:** Deployment archetypes are different from location scopes (/architecture/infra-reliability-guide/building-blocks#location_scopes). The location scope of a Google Cloud resource defines its availability boundary. For example, the location scope of a Compute Engine VM is _zonal_ . This means that if the Google Cloud zone in which a VM is provisioned has an outage, the availability of the VM is affected. However, by distributing VMs across multiple zones, you can build a highly available architecture that's based on the _regional_ deployment archetype. 

Choosing a deployment archetype helps to simplify subsequent decisions regarding the Google Cloud products and features that you should use. For example, for a highly available containerized application, if you choose the regional deployment archetype, then regional Google Kubernetes Engine (GKE) clusters are more appropriate than zonal GKE clusters. 

When you choose a deployment archetype for an application, you need to consider tradeoffs between factors like availability, cost, and operational complexity. For example, if an application serves users in multiple countries and needs high 

availability, you might choose the multi-regional deployment archetype. But for an internal application that's used by employees in a single geographical region, you might prioritize cost over availability and, therefore, choose the regional deployment archetype. 

### Overview of the deployment archetypes

The following tabs provide definitions for the deployment archetypes and a summary of the use cases and design considerations for each. 

<!-- Start of picture text -->
ZonalRegional (#regional)Multi-regional… Global (#global)Hybrid (#hybrid)Multiclo<br> (#zonal)<br>Your application runs within a single Google Cloud zone, as shown in the<br>following diagram:<br>Use cases Development and test environments.<br>Applications that don't need high availability.<br>Low-latency networking between application components.<br>Migrating commodity workloads.<br>Applications that use license-restricted software.<br><!-- End of picture text -->

<!-- Start of picture text -->
Design Downtime during zone outages.<br>considerations<br>For business continuity, you can provision a passive replica of the<br>application in another zone in the same region. If a zone outage occurs,<br>you can restore the application to production by using the passive replica.<br>More See the following sections:<br>information<br>Zonal deployment archetype (/architecture/deployment-archetypes/zonal)<br>Comparative analysis of all the deployment archetypes<br> (/architecture/deployment-archetypes/comparison)<br><!-- End of picture text -->

### Contributors

Author: Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | CrossProduct Solution Developer 

Other contributors: 

   - Anna Berenberg (https://www.linkedin.com/in/annaberenberg) | Engineering Fellow 

   - Anshu Kak (https://www.linkedin.com/in/anshu-kak-26654a) | Distinguished Engineer 

   - Jeff Welsch (https://www.linkedin.com/in/jeffwelsch) | Director, Product Management 

   - Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

   - Sekou Page (https://www.linkedin.com/in/sekoupage) | Outbound Product Manager 

   - Steve McGhee (https://www.linkedin.com/in/stevemcghee) | Reliability Advocate Victor Moreno (https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking 

1. Anna Berenberg and Brad Calder, Deployment Archetypes for Cloud Applications (https://dl.acm.org/doi/10.1145/3498336), ACM Computing Surveys, Volume 55, Issue 3, Article No.: 61, pp 1-48 ↩ (#fnref1) 

Next 

Last updated 2026-09-09 UTC. 



## Comparative analysis of Google Cloud deployment archetypes

URL: https://docs.cloud.google.com/architecture/deployment-archetypes/comparison

Last reviewed 2026-09-09 UTC 

This section of the Google Cloud deployment archetypes 

(/architecture/deployment-archetypes) guide compares the deployment archetypes in terms of availability, robustness against outages, cost, and operational complexity. 

The following table summarizes the comparative analysis for the basic deployment archetypes: zonal, regional, multi-regional, and global. For the hybrid and multicloud topologies, the deployment archetype that's used for the Google Cloud part of the topology influences the availability, robustness against outages, cost, and operational complexity. 

|Design consideration|Zonal|Regional|Multi-regional|Global|
|---|---|---|---|---|
|Infrastructure availability<br>(/architecture/deployment-<br>archetypes/comparison#availability)|99.9% (3<br>nines)|99.99% (4<br>nines)|99.999% (5<br>nines)|99.999% (5<br>nines)|
|Robustness of infrastructure against<br>zone outages<br>(/architecture/deployment-<br>archetypes/comparison#robustness)|RTO of hours<br>or days|Near-zero<br>RTO if<br>replication is<br>synchronous|Near-zero<br>RTO if<br>replication is<br>synchronous|Near-zero<br>RTO if<br>replication is<br>synchronous|
|Robustness of infrastructure against<br>region outages<br>(/architecture/deployment-<br>archetypes/comparison#robustness)|RTO of hours<br>or days|RTO of hours<br>or days|Near-zero<br>RTO if<br>replication is<br>synchronous|Near-zero<br>RTO if<br>replication is<br>synchronous|
|Cost of Google Cloud resources<br>(/architecture/deployment-<br>archetypes/comparison#cost)|Low|Medium|High|Medium|
|Operational complexity<br>(/architecture/deployment-<br>archetypes/comparison#operations)|Simpler than<br>the other<br>deployment<br>archetypes|More<br>complex than<br>zonal|<br>More<br>complex than<br>regional|<br>Potentially<br>simpler than<br>multi-regional|

**Note:** For more information about region-specific considerations, see Geography and regions (/docs/geography-and-regions#regions_and_zones). 

The following sections describe the comparative analysis that's summarized in the preceding table. 

### Infrastructure availability

The following sections describe the differences in infrastructure availability between the deployment archetypes. 

#### Zonal, regional, multi-regional, and global deployment archetypes

Google Cloud infrastructure is built to support a target availability of 99.9% for your workload when you use the zonal deployment archetype, 99.99% for regional deployments, and 99.999% for multi-regional and global deployments. These availability numbers are targets for the platform-level infrastructure. 

The availability that you can expect from an application that's deployed in Google Cloud depends on the following factors besides the deployment archetype: 

- Design of the application 

- Number of interdependent tiers in the application stack 

- Uptime Service Level Agreements (SLAs) (https://cloud.google.com/terms/sla) for the Google Cloud services used 

- Amount of redundant resources 

- Location scopes (/architecture/infra-reliability-guide/building-blocks#location_scopes) of the resources 

For more information, see Building blocks of reliability in Google Cloud (/architecture/infra-reliability-guide/building-blocks). 

#### Hybrid and multicloud deployment archetypes

For a hybrid or multicloud topology, the overall availability depends on the infrastructure in each environment and the interdependencies between the environments. 

- If critical interdependencies exist between components in Google Cloud and components outside Google Cloud, the overall availability is lower than the availability of the component that provides the least availability across all the environments. 

- If every component of the application is deployed redundantly across Google Cloud and on-premises or in other cloud platforms, the redundancy helps to ensure high availability. 

### Robustness of infrastructure against zone and region outages

The following sections describe the differences between the deployment archetypes in terms of the ability of the infrastructure to continue to support your workloads in the event of Google Cloud zone and region outages. 

#### Zonal deployment archetype

An architecture that uses the basic single-zone deployment archetype isn't robust against zone outages. You must plan for recovering from zone outages based on your recovery point objective (RPO) and recovery time objective (RTO). For example, you can maintain a passive or scaled-down replica of the infrastructure in another (failover) zone. If an outage occurs in the primary zone, you can promote the database in the failover zone to be the primary database and update the load balancer to send traffic to the frontend in the failover zone. 

#### Regional deployment archetype

An architecture that uses the regional deployment archetype is robust against zone outages. A failure in one zone is unlikely to affect infrastructure in other zones. The RTO is near zero if data is replicated synchronously. However, when an outage affects an entire Google Cloud region, the application becomes unavailable. Plan 

for recovering from outages according to your RPO and RTO for the application. For example, you can provision a passive replica of the infrastructure in a different region, and activate the replica during region outages. 

#### Multi-regional and global deployment archetypes

An architecture that uses the multi-regional or global deployment archetype is robust against zone and region outages. The RTO is near zero if data is replicated synchronously. An architecture where the application runs as a globally distributed location-unaware stack provides the highest level of robustness against region outages. 

#### Hybrid and multicloud deployment archetypes

The robustness of a hybrid and multicloud architecture depends on the robustness of each environment (Google Cloud, on-premises, and other cloud platforms), and the interdependencies between the environments. 

For example, if every component of an application runs redundantly across both Google Cloud and another environment (on-premises or another cloud platform), then the application is robust against _any_ Google Cloud outages. If critical interdependencies exist between components in Google Cloud and components that are deployed on-premises or on other cloud platforms, the robustness against Google Cloud outages depends on the robustness of the deployment archetype that you use for the Google Cloud part of the architecture. 

### Cost of Google Cloud resources

The cost of the Google Cloud resources that are required for an application depends on the Google Cloud services that you use, the number of resources that you provision, the period for which you retain or use resources, and the deployment archetype that you choose. To estimate the cost of Google Cloud resources in an architecture based on any deployment archetype, you can use the Google Cloud Pricing Calculator (https://cloud.google.com/products/calculator). 

The following sections describe the differences in the cost of the Google Cloud resources between the various deployment archetypes. 

#### Zonal versus regional and multi-regional deployment archetypes

When compared with an architecture that uses the zonal deployment archetype, an architecture that uses the multi-regional deployment archetype might incur extra costs for redundant storage. Also, for any network traffic that crosses region boundaries, you need to consider the cross-region data transfer costs. 

#### Global deployment archetype

With this archetype, you have the opportunity to use highly available global resources, like a global load balancer. The cost of setting up and operating the cloud resources can be lower than a multi-regional deployment where you provision and configure multiple instances of regional resources. However, global resources might entail higher costs in some cases. For example, the global load balancer requires Premium Tier (/network-tiers/docs/overview#premium_tier) networking, but for regional load balancers, you can choose Standard Tier (/network-tiers/docs/overview#standard_tier). 

#### Hybrid and multicloud deployment archetypes

In a hybrid or multicloud deployment architecture, you need to consider additional costs along with the cost of the resources that you provision. For example, consider costs like hybrid or cross-cloud networking, and the cost of monitoring and managing the resources across multiple environments. 

#### Considerations for all the deployment archetypes

When you assess the cost of running a cloud workload, you need to consider additional costs along with the cost of the Google Cloud resources that you provision. For example, consider personnel expenses and the overhead costs to design, build, and maintain your cloud deployment. 

To compare the cost of Google Cloud resources across the deployment archetypes, also consider the cost per _unit of work_ that the application performs. Identify units of work that reflect the business drivers of the application, like the number of users the application serves or the number of requests processed. 

By carefully managing the utilization of your Google Cloud resources and adopting Google-recommended best practices, you can optimize the cost of your cloud deployments. For more information, see Google Cloud Well-Architected Framework: Cost optimization (/architecture/framework/cost-optimization). 

### Operational complexity

The following sections describe the differences in operational complexity between the deployment archetypes, which depends on the number of infrastructure resources, features, and application stacks that you need to operate. 

#### Zonal versus regional and multi-regional deployment archetypes

An architecture that's based on the zonal deployment archetype is easier to set up and operate when compared with the other deployment architectures. An application that runs redundantly in multiple zones or regions requires higher operational effort, due to the following reasons: 

- The status of the application stacks in multiple locations must be monitored, both at the stack level and for each component of the application. 

- If a component becomes unavailable in any location, in-process requests must be handled gracefully. 

- Application changes must be rolled out carefully. 

- The databases must be synchronized across all the locations. 

#### Global deployment archetype

The global deployment archetype lets you use highly available global resources like a global load balancer and a global database. The effort to set up and operate cloud resources can be lower than a multi-regional deployment where you need to manage multiple instances of regional resources. However, you must carefully manage changes to global resources 

(/architecture/infra-reliability-guide/buildingblocks#careful_management_of_changes_to_global_resources) 

The effort to operate an architecture that uses the global deployment archetype also depends on whether you deploy a distributed location-unaware stack or multiple regionally isolated stacks: 

- A distributed, location-unaware application can be expanded and scaled with greater flexibility. For example, if certain components have critical end-user latency requirements in only specific locations, you can deploy these components in the required locations and operate the remainder of the stack in other locations. 

- An application that's deployed as multiple regionally isolated stacks requires higher effort to operate and maintain, due to the following factors: 

   - The status of the application stacks in multiple locations must be monitored, both at the stack level and for each component. 

   - If a component becomes unavailable in any location, in-process requests must be handled gracefully. 

   - Application changes must be rolled out carefully. 

   - The databases must be synchronized across all the locations. 

#### Hybrid and multicloud deployment archetypes

Hybrid or multicloud topologies require more effort to set up and operate than an architecture that uses only Google Cloud. 

- Resources must be managed consistently across the on-premises and Google Cloud topologies. 

- You need a way to efficiently provision and manage resources across multiple platforms. Tools like Terraform can help to reduce the provisioning effort. 

- Security features and tools aren't standard across cloud platforms. Your security administrators need to acquire skills and expertise to manage the security of resources distributed across all the cloud platforms that you use. 

Previous 

##### Multicloud (/architecture/deployment-archetypes/multicloud)

Next 

Last updated 2026-09-09 UTC. 



## RAG infrastructure for generative AI using Gemini Enterprise and Agent Platform

URL: https://docs.cloud.google.com/architecture/rag-genai-gemini-enterprise-vertexai

Last reviewed 2025-11-10 UTC 

This document provides a reference architecture that you can use to design the infrastructure for a generative AI application with retrieval-augmented generation (RAG) 

(https://developers.google.com/machine-learning/glossary#retrieval-augmented_generation) by using Gemini Enterprise (https://cloud.google.com/gemini-enterprise) and Agent Platform (/gemini-enterprise-agent-platform). This reference architecture demonstrates how to use managed services and deploy a single AI agent 

(/docs/generative-ai/glossary#ai-agents) to facilitate an end-to-end RAG dataflow. Gemini Enterprise serves as the unified platform for agent orchestration across the enterprise. Agent Platform accelerates the development and deployment of custom agents and provides managed datastores to facilitate efficient retrieval for RAG. 

The intended audience for this document includes architects, developers, and administrators of generative AI applications. The document assumes that you have a basic understanding of AI, machine learning (ML), and large language model (LLM) concepts. This document doesn't provide guidance about how to design and develop a generative AI application. For information about how to design an application, see Develop a generative AI application 

(/docs/ai-ml/generative-ai/develop-generative-ai-application). 

**Note:** To meet your requirements, you can consider other architectural approaches for your RAG-capable generative AI application. For more information, see the design alternatives (#design_alternatives) section later in this document. 

### Architecture

The following diagram shows a high-level view of the architecture that this document presents: 

The architecture in the preceding diagram has two subsystems: data ingestion and serving. 

- The **data ingestion subsystem** ingests and prepares data from external sources for use in RAG. The subsystem generates embeddings 

- (/gemini-enterprise-agent-platform/machine-learning/glossary#embedding) for the ingested data and uses them to build and maintain a searchable vector index (/gemini-enterprise-agent-platform/machine-learning/glossary#index) in a managed datastore. 

- The **serving subsystem** contains the generative AI application's frontend and backend services. 

   - The frontend service handles the query-response flow with application users and forwards queries to the backend service. 

   - The backend service uses Gemini Enterprise and Agent Platform to build and deploy your AI agent to orchestrate the RAG process. This process uses the indexed vector data to generate responses that are contextually 

grounded and adhere to Responsible AI 

- (/gemini-enterprise-agent-platform/models/responsible-ai) safety filters. 

The following diagram shows a detailed view of the architecture: 

The following sections describe the data flow within each subsystem of the preceding architecture diagram. 

#### Data ingestion subsystem

The data ingestion subsystem ingests data from external sources and prepares the data for RAG. The following are the steps in the data-ingestion and preparation flow: 

- A. Data engineers upload data from external sources to a Cloud Storage bucket (/storage/docs/buckets). The external sources might be applications, databases, or streaming services. 

- B. Upon completion, Cloud Storage publishes a message to a Pub/Sub topic. 

- C. The Pub/Sub topic triggers a processing job to run in Cloud Run functions (/functions/docs/concepts/overview). 

- D. Cloud Run functions processes the raw data by generating and storing the metadata as JSON Lines (JSONL) 

   - (/generative-ai-app-builder/docs/prepare-data#storage-unstructured) files. The JSONL files are stored into a separate Cloud Storage bucket. 

- E. Upon completion, Cloud Run functions publishes a message to a Pub/Sub topic. 

- F. The Pub/Sub topic triggers a processing job to run in the managed datastore (/gemini/enterprise/docs/introduction-to-connectors-and-data-stores) within Gemini Enterprise. The processing job pulls the raw ingested data and metadata from the Cloud Storage buckets, then parses and chunks the data 

   - (/gemini/enterprise/docs/parse-chunk-documents#parse-chunk-rag) for efficient retrieval during serving. Gemini Enterprise automatically generates vector embeddings without any configuration necessary. 

#### Serving subsystem

The serving subsystem handles the query-response flow between the generative AI application and its users. The following are the steps in the serving flow: 

1. An application user sends a query through one of the Cloud Run frontend services (/run/docs/resource-model#services). You can customize these services for different experiences, such as a chatbot UI, a search page, or a mobile application. 

2. The frontend service receives the query, and then forwards the query to a centralized Cloud Run backend service. This backend provides a single, unified endpoint to support all of the different frontend clients. The backend service also performs necessary preprocessing, which can include constructing filters for the search query. This approach keeps the logic transparent to the frontends. 

3. The backend service sends the prepared request to Gemini Enterprise by using the Gemini Enterprise API endpoint to initiate the RAG workflow. 

4. To process the query, Gemini Enterprise uses the enterprise search and custom agent to perform the following tasks: 

   - a. Create an embedding of the user's query. 

   - b. Perform a semantic search on the indexed data in the Managed datastore to find the most relevant information. 

   - c. Augment the original query with the retrieved data from the managed datastore to create a detailed, contextual prompt. 

   - d. Generate a final response that's based on the augmented prompt. 

5. Gemini Enterprise sends the generated response to the Cloud Run backend service. 

6. The backend service returns the final response to the frontend service that sent the original request. The frontend service presents the answer to the application user. 

### Products used

This reference architecture uses the following Google Cloud products: 

- Gemini Enterprise (https://cloud.google.com/gemini-enterprise): A fully-managed secure platform to deploy and manage AI agents within an enterprise. 

- Gemini Enterprise Agent Platform (/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 

   - Agent Runtime on Gemini Enterprise Agent Platform 

   - (/gemini-enterprise-agent-platform/build/runtime): A platform that lets you run, manage, and scale AI agents in production. 

- Cloud Run (https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure. 

- Pub/Sub (https://cloud.google.com/pubsub): An asynchronous and scalable messaging service that decouples services that produce messages from services that process those messages. 

- Cloud Storage (https://cloud.google.com/storage): A low-cost, no-limit object store for diverse data types. Data can be accessed from within and outside Google Cloud, and it's replicated across locations for redundancy. 

### Use cases

This architecture is designed for enterprise scenarios where your generative AI application needs access to the most current information and requires deep, contextual understanding to provide accurate responses. 

The architecture includes a custom data ingestion subsystem to address two key enterprise requirements: 

- **Real-time data availability:** The event-driven pipeline processes new data as soon as it's available in your organization—for example, a new product guide or an updated report. The pipeline also makes the information available in your managed datastore. This design helps to mitigate information staleness because it ensures that there's a minimal delay between data availability and use. 

- **Enriched contextual search:** The custom processing job allows your organization to apply its own business logic to enrich data with valuable metadata. The Cloud Run function can tag each document with specific attributes like product line, author, location, or document type. This rich metadata helps the agent to narrow down its search and deliver more precise, context-aware answers. 

RAG is an effective technique to improve the quality of output that's generated from an LLM. This section provides examples of use cases for which you can use RAG-capable generative AI applications. 

#### Personalized product recommendations

An online shopping site might use an LLM-powered chatbot to assist customers with finding products or getting shopping-related help. The questions from a user can be augmented by using historical data about the user's buying behavior and website interaction patterns. The data might include user reviews and feedback that's stored in an unstructured datastore or search-related metrics that are stored in a web analytics data warehouse. The augmented question can then be processed by the LLM to generate personalized responses that the user might find more appealing and compelling. 

#### Clinical assistance systems

Doctors in hospitals need to quickly analyze and diagnose a patient's health condition to make decisions about appropriate care and medication. A generative AI application that uses a medical LLM like Med-PaLM 

(https://sites.research.google/med-palm/) can be used to assist doctors in their clinical diagnosis process. The responses that the application generates can be grounded in historical patient records by contextualizing the doctors' prompts with data from the hospital's electronic health record (EHR) database or from an external knowledge base like PubMed (https://pubmed.ncbi.nlm.nih.gov/). 

#### Efficient legal research

Generative AI-powered legal research lets lawyers quickly query large volumes of statutes and case laws to identify relevant legal precedents or summarize complex legal concepts. The output of such research can be enhanced by augmenting a lawyer's prompts with data that's retrieved from the law firm's proprietary corpus of contracts, past legal communication, and internal case records. This design approach ensures that the generated responses are relevant to the legal domain that the lawyer specializes in. 

### Design alternatives

This section presents alternative design approaches that you can consider for your RAG-capable generative AI application in Google Cloud. 

#### AI infrastructure alternatives

For a list of architecture guides to design and deploy generative AI applications with RAG in Google Cloud, see Generative AI with RAG 

(/architecture/rag-reference-architectures). 

#### Application hosting options

In the architecture that's shown in this document, Cloud Run is the host for the generative AI application and data processing. Cloud Run is an application that is 

developer-focused and fully managed. You can also deploy your application to Agent Runtime on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/scale), GKE clusters (/kubernetes-engine/docs), or to Compute Engine (/compute) VMs. 

To choose an application host, consider the following trade-offs between configuration flexibility and management effort: 

- With the serverless Cloud Run option, you deploy your custom services to a preconfigured, managed environment. To host the frontend services and the custom backend logic for request pre-processing, this architecture requires the ability to deploy custom applications. 

- With the Agent Runtime option, you use a fully managed platform that's designed for agent serving. Agent Runtime reduces management overhead and ensures tight integration with Gemini Enterprise. 

- With Compute Engine VMs and GKE containers, you're responsible for managing the underlying compute resources, but you have greater configuration flexibility and control. 

For more information about choosing an appropriate application hosting service, see the following documents: 

- Is my app a good fit for Cloud Run? (/run/docs/fit-for-run) 

- Select a managed container runtime environment 

- (/architecture/select-managed-container-runtime-environment) 

- Hosting Applications on Google Cloud (https://cloud.google.com/hosting-options) 

#### Other infrastructure options

For information about other infrastructure options, supported models, and grounding techniques that you can use for generative AI applications in Google Cloud, see Choose models and infrastructure for your generative AI application (/docs/generative-ai/choose-models-infra-for-ai). 

### Design considerations

This section provides guidance to help you develop a RAG-capable generative AI architecture in Google Cloud that meets your specific requirements for security and compliance, reliability, cost, and performance. The guidance in this section isn't exhaustive. Depending on the specific requirements of your generative AI application and the Google Cloud products and features that you use, you might need to consider additional design factors and trade-offs. 

For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the AI and ML perspective 

(/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 

#### Security, privacy, and compliance

This section describes design considerations and recommendations to design a topology in Google Cloud that meets your workload's security and compliance requirements. 

For security principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Security 

(/architecture/framework/perspectives/ai-ml/security) in the Well-Architected Framework. 

Agent Platform 

Agent Platform supports Google Cloud security controls that you can use to meet your requirements for data residency, data encryption, network security, and access transparency. For more information, see the following documentation: 

Security controls for machine learning services 

- (/gemini-enterprise-agent-platform/machine-learning/security-controls) 

- Security controls for Generative AI 

- (/gemini-enterprise-agent-platform/models/security-controls) 

- Agent Platform and zero data retention 

- (/gemini-enterprise-agent-platform/resources/zero-data-retention) 

- Enable access transparency for Gemini Enterprise 

- (/gemini/enterprise/docs/access-transparency) 

Compliance and security controls for Gemini Enterprise 

(/gemini/enterprise/docs/compliance-security-controls) 

Gemini Enterprise deletes user-requested data within 60 days. For more information, see Data deletion on Google Cloud (/docs/security/deletion). 

Generative AI models might produce harmful responses, especially when they are explicitly prompted for such responses. To enhance safety and mitigate potential misuse, you can configure content filters to act as barriers to harmful responses. For more information, see Safety and content filters 

(/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters). 

Cloud Run 

By default, Cloud Run encrypts data by using Google-owned and Google-managed encryption keys. To protect your containers by using keys that you control, you can use customer-managed encryption keys (CMEKs). For more information, see Using customer managed encryption keys (/run/docs/securing/using-cmek). 

To ensure that only authorized container images are deployed to Cloud Run, you can use Binary Authorization (/binary-authorization/docs/overview). 

Cloud Run helps you meet data residency requirements. Your Cloud Run functions run within the selected region (/docs/geography-and-regions#regions_and_zones). 

Cloud Storage 

By default, Cloud Storage encrypts the data that it stores by using Google-owned and Google-managed encryption keys. If required, you can use CMEKs or your own keys that you manage by using an external management method like customersupplied encryption keys (CSEKs). For more information, see Data encryption options (/storage/docs/encryption). 

Cloud Storage supports two methods to grant users access to your buckets and objects: Identity and Access Management (IAM) and access control lists (ACLs). In most cases, we recommend that you use IAM, which lets you grant permissions at the bucket and project levels. For more information, see Overview of access control (/storage/docs/access-control). 

The data that you load into the data ingestion subsystem through Cloud Storage might include sensitive data. You can use Sensitive Data Protection to discover, classify, and de-identify sensitive data. For more information, see Using Sensitive Data Protection with Cloud Storage (/sensitive-data-protection/docs/dlp-gcs). 

Cloud Storage helps you meet data residency requirements. Cloud Storage stores or replicates data within the region that you specify. 

Pub/Sub 

By default, Pub/Sub encrypts all of the messages, which includes at rest and in transit messages, by using Google-owned and Google-managed encryption keys. Pub/Sub supports the use of CMEKs for message encryption at the application layer. For more information, see Configure message encryption 

(/pubsub/docs/encryption). 

If you have data residency requirements, to ensure that message data is stored in specific locations, you can configure message storage policies 

(/pubsub/docs/resource-location-restriction). 

#### Reliability

This section describes design considerations and recommendations to build and operate reliable infrastructure for your deployment in Google Cloud. 

For reliability principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Reliability 

(/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

Agent Platform 

Agent Platform ensures data residency at rest. Agent Platform stores your source data, which includes data for RAG in the managed datastore, within the Google Cloud location (https://cloud.google.com/about/locations) that you have selected. This separation of processing from storage is a fundamental aspect of how the platform provides both high reliability and compliance. 

Cloud Run 

Cloud Run is a regional service that stores data synchronously across multiple zones within a region. The service automatically load-balances the traffic across the zones. If a zone outage occurs, Cloud Run jobs continue to run and data isn't lost. If a region outage occurs, the Cloud Run jobs stop running until Google resolves the outage. 

Individual Cloud Run jobs or tasks might fail. To handle such failures, you can use task retries (/run/docs/configuring/max-retries) and checkpointing. For more information, see Jobs retries and checkpoints best practices (/run/docs/jobs-retries). 

Cloud Storage 

You can create Cloud Storage buckets in one of three location types (/storage/docs/locations): regional, dual-region, or multi-region. For data in regional buckets, Cloud Storage synchronously replicates that data across multiple zones within a region. For higher availability, you can use dual-region or multi-region buckets, where Cloud Storage replicates data asynchronously across regions. Ensure that your choice aligns with your compliance requirements. 

#### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build by using this reference architecture. 

For cost optimization principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Cost optimization 

(/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

Agent Platform 

The underlying AI model that the agent invokes can directly influence the cost to use that agent. Pricing is calculated based on the number of input and output tokens for each request. For more information, see Generative AI on Agent Platform quotas and system limits (/gemini-enterprise-agent-platform/models/quotas) and the Google Cloud pricing calculator (https://cloud.google.com/products/calculator). 

For information about how to minimize token count to reduce cost, see the Context caching overview 

(/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview). 

Cloud Run functions 

When you create Cloud Run jobs, you specify the amount of memory and CPU to be allocated to the container instance. To control costs, start with the default CPU and memory allocations. To improve performance, you can increase the allocation by configuring the CPU limit (/run/docs/configuring/jobs/cpu) and memory limit 

(/run/docs/configuring/jobs/memory-limits). 

If you can predict the CPU and memory requirements of your Cloud Run jobs, then you can save money with discounts for committed usage. For more information, see Cloud Run committed use discounts (/run/cud). 

Cloud Storage 

For the Cloud Storage bucket that you use to load data into the data ingestion subsystem, choose an appropriate storage class (/storage/docs/storage-classes) based on the data-retention and access-frequency requirements of your workloads. For example, you can choose the Standard storage class, and use Object Lifecycle Management (/storage/docs/lifecycle) to control storage costs. Object Lifecycle Management automatically downgrades objects to a lower-cost storage class or deletes objects based on conditions that you set. 

#### Performance optimization

This section describes design considerations and recommendations to design a topology in Google Cloud that meets the performance requirements of your workloads. 

For performance optimization principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Performance optimization (/architecture/framework/perspectives/ai-ml/performance-optimization) in the WellArchitected Framework. 

Gemini Enterprise 

To reduce latency during serving, stream responses by sending model responses before the agent generates the complete output. This enables real-time processing of the output, and you can immediately update your user interface and perform other concurrent tasks. Streaming enhances perceived responsiveness and creates a more interactive user experience. For more information, see Stream answers (/gemini/enterprise/docs/stream-answer). 

Cloud Run 

Adjust the memory and CPU allocation for the Cloud Run instances based on performance requirements. For more information, see Configure CPU limits for jobs (/run/docs/configuring/jobs/cpu) and Configure memory limits for services (/run/docs/configuring/services/memory-limits). 

Cloud Storage 

To upload large files, you can use a method called parallel composite uploads (/storage/docs/parallel-composite-uploads). With this strategy, the large file is split into chunks. You upload the chunks to Cloud Storage in parallel, and Cloud Storage then reassembles the data in Google Cloud. Parallel composite uploads can be faster than regular upload operations if you have sufficient network bandwidth and disk speed. However, this strategy has some limitations and cost implications. For more information, see Parallel composite uploads (/storage/docs/parallel-composite-uploads). 

### Deployment

To deploy this reference architecture, use the Terraform example that's available in GitHub. For more information, see RAG Infrastructure for Generative AI Applications using Gemini Enterprise and Agent Platform 

(https://github.com/yelshater/rag-infrastructure-for-gemini-enterprise). 

### What's next

Learn how Gemini Enterprise chunks documents for RAG (/gemini/enterprise/docs/parse-chunk-documents#parse-chunk-rag). 

- Learn how to host AI apps and agents on Cloud Run (/run/docs/ai-agents). 

- Learn about responsible AI best practices and Agent Platform safety filters (/gemini-enterprise-agent-platform/models/responsible-ai). 

- Learn about prompting strategies for LLMs 

- (/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies). 

- For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the AI and ML perspective (/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 

- For more reference architectures, diagrams, and best practices, explore the Cloud Architecture Center (/architecture). 

### Contributors

Author: Samantha He (https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer 

Other contributors: 

- Deepak Michael | Networking Specialist Customer Engineer 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Mark Schlagenhauf (https://www.linkedin.com/in/mark-schlagenhauf-63b98) | Technical Writer, Networking 

- Victor Moreno (https://www.linkedin.com/in/vimoreno) | Product Manager, Cloud Networking 

- Yehia Elshater (https://www.linkedin.com/in/yehiaz/) | Field Solutions Architect, Generative AI, Google Cloud 

- Paarth Mahajan (https://www.linkedin.com/in/paarthmahajan/) | Network Specialist, Google Cloud 

Last updated 2025-11-10 UTC. 



## Agentic AI architecture guides

URL: https://docs.cloud.google.com/architecture/agentic-ai-overview

Last reviewed 2025-11-25 UTC 

This document in the Architecture Center provides links to architecture guides that you can use to build and deploy agentic AI applications in Google Cloud. 

To filter the list, type a keyword 

|Architecture guide|Description|
|---|---|
|Administer interactive learning<br>(/architecture/agentic-ai-interactive-learning)|A high-level architecture to design a single-agent<br>AI system that assesses a user's knowledge on a<br>specific topic and generates a personalized<br>learning experience.|
|Automate data science workflows<br>(/architecture/agentic-ai-data-science)|A high-level architecture to design a multi-agent<br>AI system that automates complex data analytics<br>and machine learning tasks.|
|Build a borderless open data lakehouse<br>(/architecture/agentic-ai-build-multicloud-<br>open-data-lakehouse)|A high-level architecture to build a borderless<br>open data lakehouse that establishes a highly<br>governed, secure pipeline from raw borderless<br>silos to AI and agentic driven actions.|
|Build a trusted agentic system with Google<br>Maps Platform<br>(/architecture/agentic-ai-system-with-<br>grounding-using-maps)|A high-level architecture to build trustworthy and<br>effective AI agents by grounding them in real-<br>world maps and calendar data.|
|Classify multimodal data<br>(/architecture/agentic-ai-classify-multimodal-<br>data)|A high-level architecture to design a multi-agent<br>AI system that analyzes disparate multimodal<br>data and produces a high-confidence<br>classification.|
|Guide technical workflows with bidirectional<br>multimodal streaming<br>(/architecture/agentic-ai-bidirectional-<br>multimodal-streaming)|A high-level architecture to build and deploy a<br>multi-agent AI system that provides technical<br>guidance and automated safety monitoring<br>through a continuous, bidirectional stream of<br>multimodal data.|

|Architecture guide|Description|
|---|---|
|Implement agentic analytics workflows for<br>distributed data<br>(/architecture/agentic-ai-cross-cloud-<br>analytics)|A high-level architecture for implementing cross-<br>cloud analytics workflows that use AI agents.|
|Multimodal GraphRAG resource orchestration<br>(/architecture/agentic-ai-multimodal-graph-<br>rag-resource-orchestration)|A high-level architecture to build and deploy a<br>multi-agent AI system that consolidates<br>fragmented multimodal data into a searchable<br>knowledge graph.|
|Orchestrate access to disparate enterprise<br>systems<br>(/architecture/agenticai-orchestrate-access-<br>disparate-systems)|A high-level architecture to design an agentic AI<br>system that orchestrates interactions with<br>disparate enterprise systems.|
|Orchestrate security operations workflows<br>(/architecture/agentic-ai-orchestrate-<br>security-ops-workflows)|A high-level architecture to build a multi-agent AI<br>system that orchestrates complex investigation<br>and triage processes in a security operations<br>center (SOC).|
|Choose a design pattern for your agentic AI<br>system<br>(/architecture/choose-design-pattern-<br>agentic-ai-system)|A design guide to help you choose a design<br>pattern for your agentic AI system.|
|Choose your agentic AI architecture<br>components<br>(/architecture/choose-agentic-ai-<br>architecture-components)|A design guide to help you choose architectural<br>components for your agentic AI applications in<br>Google Cloud.|
|Multi-agent AI system<br>(/architecture/multiagent-ai-system)|A reference architecture to help you design a<br>robust multi-agent AI system in Google Cloud.|
|Multi-tenant agentic AI system<br>(/architecture/multi-tenant-agentic-ai-<br>system)|A reference architecture to help you design a<br>robust multi-tenant agentic AI system in Google<br>Cloud.|
|Single-agent AI system using ADK and Cloud<br>Run<br>(/architecture/single-agent-ai-system-adk-<br>cloud-run)|A reference architecture to help you design a<br>single-agent AI system by using Agent<br>Development Kit (ADK) and Cloud Run with<br>Gemini and Model Context Protocol (MCP).|

licensed under the Apache 2.0 License (https://www.apache.org/licenses/LICENSE-2.0). For details, see the Google Developers Site Policies (https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. 

Last updated 2025-11-25 UTC.
