# Architecture: Well-Architected Framework and reference designs / Well-Architected Framework: AI and ML perspective: AI and ML perspective: Reliability: Implement holistic AI and ML observability and reliability practices to AI and ML perspective: Performance optimization
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 312-346, extracted 2026-10-18

## Well-Architected Framework: AI and ML perspective

URL: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable

### Implement holistic AI and ML observability and reliability practices

Holistic observability is essential for managing complex AI and ML systems in production. It's also essential for measuring the reliability of complex AI and ML systems, especially for generative AI, due to its complexity, resource intensity, and potential for unpredictable outputs. Holistic observability involves observing infrastructure, application code, data, and model behavior to gain insights for proactive issue detection, diagnosis, and response. This observability ultimately leads to high-performance, reliable systems. To achieve holistic observability you need to do the following: 

- Adopt SRE principles. 

- Define clear reliability goals. 

- Track metrics across system layers. 

- Use insights from observability for continuous improvement and proactive management. 

To implement holistic observability and reliability practices for AI and ML workloads in Google Cloud, consider the following recommendations. 

#### Establish reliability goals and business metrics

Identify the key performance indicators (KPIs) that your AI and ML system directly affects. The KPIs might include revenue that's influenced by AI recommendations, customer churn that the AI systems predicted or mitigated, and user engagement and conversion rates that are driven by generative AI features. 

For each KPI, define the corresponding technical reliability metrics that affect the KPI. For example, if the KPI is "customer satisfaction with a conversational AI assistant," then the corresponding reliability metrics can include the following: 

- The success rate of user requests. 

- The latency of responses: time to first token (TTFT) and token streaming for LLMs. 

- The rate of irrelevant or harmful responses. 

- The rate of successful task completion by the agent. 

For AI and ML training, reliability metrics can include model FLOPS utilization (MFU), iterations per second, tokens per second, and tokens per device. 

To effectively measure and improve AI and ML reliability, begin by setting clear reliability goals that are aligned with the overarching business objectives. Adopt the SRE approach by defining SLOs that quantify acceptable levels of reliability and performance for your AI and ML services from the users' perspective. Quantify these technical reliability metrics with specific SLO targets. 

The following are examples of SLO targets: 

- 99.9% of API calls must return a successful response. 

- 95th percentile inference latency must be below 300 ms. 

- TTFT must be below 500 ms for 99% of requests. 

- Rate of harmful output must be below 0.1%. 

Aligning SLOs directly with business needs ensures that reliability efforts are focused on the most critical system behavior that affects users and the business. This approach helps to transform reliability into a measurable and actionable engineering property. 

#### Monitor infrastructure and application performance

Track infrastructure metrics across all of the resources that are used by your AI and ML systems. The metrics include processor usage (CPU, GPU, and TPU), memory usage, network throughput and latency, and disk I/O. Track the metrics for managed environments like Gemini Enterprise Agent Platform training and serving and for self-managed resources like GKE nodes and Cloud Run instances. 

Monitor the four golden signals 

(https://sre.google/sre-book/monitoring-distributed-systems/#xref_monitoring_golden-signals) for your AI and ML applications: 

- **Latency** : Time to respond to requests. 

- **Traffic** : Volume of requests or workload. 

- **Error rate** : Rate of failed requests or operations. 

- **Saturation** : Utilization of critical resources like CPU, memory, and GPU or TPU accelerators, which indicates how close your system is to capacity limits. 

Perform monitoring by using the following techniques: 

- Collect, store, and visualize the infrastructure and application metrics by using Cloud Monitoring (/monitoring/docs/monitoring-overview). You can use prebuilt dashboards for Google Cloud services and create custom dashboards that are tailored based on your workload's specific performance indicators and infrastructure health. 

- Collect and integrate metrics from specialized serving frameworks like vLLM (https://docs.vllm.ai/en/latest/design/v1/metrics.html) or NVIDIA Triton Inference Server 

(https://docs.nvidia.com/deeplearning/triton-inference-server/userguide/docs/user_guide/metrics.html) 

into Cloud Monitoring by using Google Cloud Managed Service for Prometheus (/stackdriver/docs/managed-prometheus). 

   - Create dashboards and configure alerts for metrics that are related to custom training, endpoints, and performance, and for metrics that Agent Platform exports to Cloud Monitoring 

   - (/gemini-enterprise-agent-platform/machine-learning/general/monitoring-metrics). 

- Collect detailed logs from your AI and ML applications and the underlying infrastructure by using Cloud Logging (/logging/docs/overview). These logs are essential for troubleshooting and performance analysis. They provide context around events and errors. 

- Pinpoint latency issues and understand request flows across distributed AI and ML microservices by using Cloud Trace (/trace/docs/overview). This capability is crucial for debugging complex Agent Conversation interactions or multicomponent inference pipelines. 

- Identify performance bottlenecks within function blocks in application code by using Cloud Profiler (/profiler/docs/about-profiler). Identifying performance bottlenecks can help you optimize resource usage and execution time. 

- Gather specific accelerator-related metrics like detailed GPU utilization per process, memory usage per process, and temperature, by using tools like NVIDIA Data Center GPU Manager (DCGM) 

- (/monitoring/agent/ops-agent/third-party-nvidia). 

#### Implement data and model observability

Reliable generative AI systems require robust data and model observability, which starts with end-to-end pipeline monitoring. 

- Track data ingestion rates, processed volumes, and transformation latencies by using services like Dataflow (/dataflow/docs/overview). 

- Monitor job success and failure rates within your MLOps pipelines, including pipelines that are managed by Agent Platform Pipelines 

- (/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction). 

Continuous assessment of data quality is crucial. 

- Manage and govern data by using Knowledge Catalog (/dataplex/docs/introduction): 

   - Evaluate accuracy by validating against ground truth or by tracking outlier detection rates. 

   - Monitor freshness based on the age of data and frequency of updates against SLAs. 

   - Assess completeness by tracking null-value percentages and required field-fill rates. 

   - Ensure validity and consistency through checks for schema-adherence and duplication. 

- Proactively detect anomalies by using Cloud Monitoring alerting and through clear data lineage for traceability. 

- For RAG systems, examine the relevance of the retrieved context and the groundedness (attribution to source) of the responses. 

- Monitor the throughput of vector database queries. 

Key model observability metrics include input-output token counts and modelspecific error rates, such as hallucination or query resolution failures. To track these metrics, use Model Monitoring on Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview). 

   - Continuously monitor the toxicity scores of the output and user-feedback ratings. 

   - Automate the assessment of model outputs against defined criteria by using the Gen AI evaluation service 

   - (/gemini-enterprise-agent-platform/models/evaluation-overview). 

   - Ensure sustained performance by systematically monitoring for data and concept drift with comprehensive error-rate metrics. 

To track model metrics, you can use TensorBoard 

(https://www.tensorflow.org/tensorboard) or MLfowl (https://mlflow.org/). For deep analysis and profiling to troubleshoot performance issues, you can use PyTorch XLA profiling (/tpu/docs/pytorch-xla-performance-profiling-tpu-vm) or NVIDIA Nsight (https://developer.nvidia.com/nsight-systems). 

### Contributors

Authors: 

- Rick (Rugui) Chen (https://www.linkedin.com/in/rugui-chen) | AI Infrastructure Field Solutions Architect 

- Stef Ruinard (https://www.linkedin.com/in/stefruinard) | Generative AI Field Solutions Architect 

Other contributors: 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Hossein Sarshar (https://www.linkedin.com/in/hsarshar) | AI Infrastructure Field Solution Architect 

- Jose Andrade (https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Laura Hyatt (https://www.linkedin.com/in/laura-hyatt) | Customer Engineer, FSI 

- Olivier Martin | AI Infrastructure Field Solution Architect 

- Radhika Kanakam (https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework 

## AI and ML perspective: Cost optimization

This document in Well-Architected Framework: AI and ML perspective (/architecture/framework/perspectives/ai-ml) provides an overview of principles and recommendations to optimize the cost of your AI systems throughout the ML lifecycle. By adopting a proactive and informed cost management approach, your organization can realize the full potential of AI and ML systems and also maintain financial discipline. The recommendations in this document align with the cost optimization pillar (/architecture/framework/cost-optimization) of the Google Cloud WellArchitected Framework. 

AI and ML systems can help you unlock valuable insights and predictive capabilities from data. For example, you can reduce friction in internal processes, improve user experiences, and gain deeper customer insights. The cloud offers vast amounts of resources and quick time-to-value without large up-front investments for AI and ML workloads. To maximize business value and to align the spending with your business goals, you need to understand the cost drivers, proactively optimize costs, set up spending controls, and adopt FinOps (https://cloud.google.com/learn/what-is-finops) practices. 

The recommendations in this document are mapped to the following core principles: 

Define and measure costs and returns 

(/architecture/framework/perspectives/ai-ml/costoptimization#define_and_measure_costs_and_returns) 

Optimize resource allocation 

(/architecture/framework/perspectives/ai-ml/costoptimization#optimize_resource_allocation) 

Enforce data management and governance practices 

(/architecture/framework/perspectives/ai-ml/cost- 

optimization#enforce_data_management_and_governance_practices) 

Automate and streamline with MLOps 

(/architecture/framework/perspectives/ai-ml/costoptimization#automate_and_streamline_with_mlops) 

Use managed services and pre-trained models 

(/architecture/framework/perspectives/ai-ml/cost- 

optimization#use_managed_services_and_pre-trained_models) 

### Define and measure costs and returns

To effectively manage AI and ML costs in Google Cloud, you must define and measure the cloud resource costs and the business value of your AI and ML initiatives. To help you track expenses granularly, Google Cloud provides comprehensive billing and cost management tools, such as the following: 

Cloud Billing reports and tables 

- Data Studio dashboards, budgets, and alerts 

- Cloud Monitoring 

- Cloud Logging 

To make informed decisions about resource allocation and optimization, consider the following recommendations. 

#### Establish business goals and KPIs

Align the technical choices in your AI and ML projects with business goals and key performance indicators (KPIs). 

Define strategic objectives and ROI-focused KPIs 

Ensure that AI and ML projects are aligned with strategic objectives like revenue growth, cost reduction, customer satisfaction, and efficiency. Engage stakeholders to understand the business priorities. Define AI and ML objectives that are specific, measurable, attainable, relevant, and time-bound (SMART). For example, a SMART objective is: "Reduce chat handling time for customer support by 15% in 6 months by using an AI chatbot". 

To make progress towards your business goals and to measure the return on investment (ROI), define KPIs for the following categories of metrics: 

- Costs for training, inference, storage, and network resources, including specific unit costs (such as the cost per inference, data point, or task). These metrics help you gain insights into efficiency and cost optimization opportunities. You can track these costs by using Cloud Billing reports (/billing/docs/reports) and Cloud Monitoring dashboards (/monitoring/dashboards). 

- Business value metrics like revenue growth, cost savings, customer satisfaction, efficiency, accuracy, and adoption. You can track these metrics by using BigQuery analytics (/bigquery/docs/query-overview) and Looker dashboards (/looker/docs/dashboards). 

- Industry-specific metrics like the following: 

   - Retail industry: measure revenue lift and churn 

   - Healthcare industry: measure patient time and patient outcomes 

   - Finance industry: measure fraud reduction 

- Project-specific metrics. You can track these metrics by using Experiments on Gemini Enterprise Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-aiexperiments) 

- and evaluation 

- (/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction). 

   - Predictive AI: measure accuracy and precision 

   - Generative AI: measure adoption, satisfaction, and content quality 

   - Computer vision AI: measure accuracy 

Foster a culture of cost awareness and continuous optimization 

Adopt FinOps (https://cloud.google.com/learn/what-is-finops) principles to ensure that each AI and ML project has estimated costs and has ways to measure and track actual costs throughout its lifecycle. Ensure that the costs and business benefits of your projects have assigned owners and clear accountability. 

For more information, see Foster a culture of cost awareness 

- (/architecture/framework/cost-optimization/foster-culture-cost-awareness) in the Cost 

- Optimization pillar of the Google Cloud Well-Architected Framework. 

Drive value and continuous optimization through iteration and feedback 

Map your AI and ML applications directly to your business goals and measure the ROI. 

To validate your ROI hypotheses, start with pilot projects and use the following iterative optimization cycle: 

1. **Monitor continuously and analyze data** : Monitor KPIs and costs to identify deviations and opportunities for optimization. 

2. **Make data-driven adjustments** : Optimize strategies, models, infrastructure, and resource allocation based on data insights. 

3. **Refine iteratively** : Adapt business objectives and KPIs based on the things you learned and the evolving business needs. This iteration helps you maintain relevance and strategic alignment. 

4. **Establish a feedback loop** : Review performance, costs, and value with stakeholders to inform ongoing optimization and future project planning. 

#### Manage billing data with Cloud Billing and labels

Effective cost optimization requires visibility into the source of each cost element. The recommendations in this section can help you use Google Cloud tools to get granular insights into your AI and ML costs. You can also attribute costs to specific AI and ML projects, teams, and activities. These insights lay the groundwork for cost optimization. 

Organize and label Google Cloud resources 

- Structure your projects and resources in a hierarchy that reflects your organizational structure and your AI and ML workflows. To track and analyze costs at different levels, organize your Google Cloud resources by using organizations, folders, and projects. For more information, see Decide a resource hierarchy for your Google Cloud landing zone 

(/architecture/landing-zones/decide-resource-hierarchy). 

- Apply meaningful labels (/resource-manager/docs/labels-overview) to your resources. You can use labels that indicate the project, team, environment, 

model name, dataset, use case, and performance requirements. Labels provide valuable context for your billing data and enable granular cost analysis. 

- Maintain consistency in your labeling conventions across all of your AI and ML projects. Consistent labeling conventions ensure that your billing data is organized and can be readily analyzed. 

Use billing-related tools 

- To facilitate detailed analysis and reporting, export the billing data to BigQuery (/billing/docs/how-to/export-data-bigquery). BigQuery has powerful query capabilities that let you analyze the billing data to help you understand your costs. 

- To aggregate costs by labels, projects, or specific time periods, you can write custom SQL queries in BigQuery. Such queries let you attribute costs to specific AI and ML activities, such as model training, hyperparameter tuning, or inference. 

- To identify cost anomalies or unexpected spending spikes, use the analytic capabilities in BigQuery. This approach can help you detect potential issues or inefficiencies in your AI and ML workloads. 

- To identify and manage unexpected costs, use the anomaly detection dashboard (/billing/docs/how-to/manage-anomalies) in Cloud Billing. 

- To distribute costs across different teams or departments based on resource usage, use Google Cloud's cost allocation (https://services.google.com/fh/files/misc/cloud_finops_shared_services_cost_allocation_ whitepaper.pdf) 

- feature. Cost allocation promotes accountability and transparency. 

- To gain insights into spending patterns, explore the prebuilt Cloud Billing reports (/billing/docs/reports). You can filter and customize these reports to focus on specific AI and ML projects or services. 

#### Monitor resources continuously with dashboards, alerts, and reports

To create a scalable and resilient way to track costs, you need continuous monitoring and reporting. Dashboards, alerts, and reports constitute the foundation for effective cost tracking. This foundation lets you maintain constant access to cost information, identify areas of optimization, and ensure alignment between business goals and costs. 

Create a reporting system 

Create scheduled reports and share them with appropriate stakeholders. 

Use Cloud Monitoring (/monitoring/docs) to collect metrics from various sources, including your applications, infrastructure, and Google Cloud services like Compute Engine, Google Kubernetes Engine (GKE), and Cloud Run functions. To visualize metrics and logs in real time, you can use the prebuilt Cloud Monitoring dashboard or create custom dashboards. Custom dashboards let you define and add metrics to track specific aspects of your systems, like model performance, API calls, or business-level KPIs. 

Use Cloud Logging (/logging/docs) for centralized collection and storage of logs from your applications, systems, and Google Cloud services. Use the logs for the following purposes: 

- Track costs and utilization of resources like CPU, memory, storage, and network. 

- Identify cases of over-provisioning (where resources aren't fully utilized) and under-provisioning (where there are insufficient resources). Over-provisioning results in unnecessary costs. Under-provisioning slows training times and might cause performance issues. 

- Identify idle or underutilized resources, such as VMs and GPUs, and take steps to shut down or rightsize them to optimize costs. 

- Identify cost spikes to detect sudden and unexpected increases in resource usage or costs. 

Use Looker (/looker/docs/intro) or Data Studio (/looker/docs/studio) to create interactive dashboards and reports. Connect the dashboards and reports to various data sources, including BigQuery and Cloud Monitoring. 

Set alert thresholds based on key KPIs 

For your KPIs, determine the thresholds that should trigger alerts. Meaningful alert thresholds can help you avoid alert fatigue. Create alerting policies 

(/monitoring/alerts) in Cloud Monitoring to get notifications related to your KPIs. For example, you can get notifications when accuracy drops below a certain threshold or latency exceeds a defined limit. Alerts based on log data can notify you about potential cost issues in real time. Such alerts let you take corrective actions promptly and prevent further financial loss. 

### Optimize resource allocation

To achieve cost efficiency for your AI and ML workloads in Google Cloud, you must optimize resource allocation. To help you avoid unnecessary expenses and ensure that your workloads have the resources that they need to perform optimally, align resource allocation with the needs of your workloads. 

To optimize the allocation of cloud resources to AI and ML workloads, consider the following recommendations. 

#### Use autoscaling to dynamically adjust resources

Use Google Cloud services that support autoscaling, which automatically adjusts resource allocation to match the current demand. Autoscaling provides the following benefits: 

**Cost and performance optimization** : You avoid paying for idle resources. At the same time, autoscaling ensures that your systems have the necessary resources to perform optimally, even at peak load. 

- **Improved efficiency** : You free up your team to focus on other tasks. 

- **Increased agility** : You can respond quickly to changing demands and maintain high availability for your applications. 

The following table summarizes the techniques that you can use to implement autoscaling for different stages of your AI projects. 

Stage Autoscaling techniques 

- Training Use managed services like Gemini Enterprise Agent Platform 

   - (/gemini-enterprise-agent-platform/machine-learning/training/overview) or GKE (/kubernetes-engine/docs/concepts/cluster-autoscaler), which offer built-in autoscaling capabilities for training jobs. 

   - Configure autoscaling policies to scale the number of training instances based on metrics like CPU utilization, memory usage, and job queue length. 

   - Use custom scaling metrics to fine-tune autoscaling behavior for your specific workloads. 

- Inference Deploy your models on scalable platforms like Gemini Enterprise Agent Platform Inference 

   - (/gemini-enterprise-agent-platform/machine-learning/predictions/overview), GPUs on GKE 

   - (/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling), or TPUs on GKE 

   - (/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscalingtpu) 

   - Use autoscaling features to adjust the number of replicas based on metrics like request rate, latency, and resource utilization. 

   - Implement load balancing to distribute traffic evenly across replicas and ensure high availability. 

#### Start with small models and datasets

To help reduce costs, test ML hypotheses at a small scale when possible and use an iterative approach. This approach, with smaller models and datasets, provides the following benefits: 

- **Reduced costs from the start** : Less compute power, storage, and processing time can result in lower costs during the initial experimentation and development phases. 

- **Faster iteration** : Less training time is required, which lets you iterate faster, explore alternative approaches, and identify promising directions more efficiently. 

   - **Reduced complexity** : Simpler debugging, analysis, and interpretation of results, which leads to faster development cycles. 

   - **Efficient resource utilization** : Reduced chance of over-provisioning resources. You provision only the resources that are necessary for the current workload. 

- Consider the following recommendations: 

   - **Use sample data first** : Train your models on a representative subset of your data. This approach lets you assess the model's performance and identify potential issues without processing the entire dataset. 

   - **Experiment by using notebooks** : Start with smaller instances and scale as needed. You can use Gemini Enterprise Agent Platform Workbench (/gemini-enterprise-agent-platform/notebooks/workbench/introduction), a managed Jupyter notebook environment that's well suited for experimentation with different model architectures and datasets. 

   - **Start with simpler or pre-trained models** : Use Model Garden 

(/gemini-enterprise-agent-platform/models/model-garden/explore-models) to discover and explore the pre-trained models. Such models require fewer computational resources. Gradually increase the complexity as needed based on performance requirements. 

   - Use pre-trained models for tasks like image classification and natural language processing. To save on training costs, you can fine-tune the models on smaller datasets initially. 

   - Use BigQuery ML (/bigquery/docs/bqml-introduction) for structured data. BigQuery ML lets you create and deploy models directly within BigQuery. This approach can be cost-effective for initial experimentation, because you can take advantage of the pay-per-query pricing model for BigQuery. 

- **Scale for resource optimization** : Use Google Cloud's flexible infrastructure to scale resources as needed. Start with smaller instances and adjust their size or number when necessary. 

#### Discover resource requirements through experimentation

Resource requirements for AI and ML workloads can vary significantly. To optimize resource allocation and costs, you must understand the specific needs of your workloads through systematic experimentation. To identify the most efficient configuration for your models, test different configurations and analyze their performance. Then, based on the requirements, right-size the resources that you used for training and serving. 

We recommend the following approach for experimentation: 

1. **Start with a baseline** : Begin with a baseline configuration based on your initial estimates of the workload requirements. To create a baseline, you can use the Pricing Calculator (https://cloud.google.com/products/calculator) for new workloads or use an existing billing report (/billing/docs/how-to/reports). 

2. **Understand your quotas** : Before launching extensive experiments, familiarize yourself with your Google Cloud project quotas (/docs/quotas/overview) for the resources and APIs that you plan to use. The quotas determine the range of configurations that you can realistically test. By becoming familiar with quotas, you can work within the available resource limits during the experimentation phase. 

3. **Experiment systematically** : Adjust parameters like the number of CPUs, amount of memory, number and type of GPUs and TPUs, and storage capacity. Gemini Enterprise Agent Platform Managed Training 

   - (/gemini-enterprise-agent-platform/machine-learning/training-overview) and Agent Platform Inference 

   - (/gemini-enterprise-agent-platform/machine-learning/predictions/overview) let you experiment with different machine types and configurations. 

4. **Monitor utilization, cost, and performance** : Track the resource utilization, cost, and key performance metrics such as training time, inference latency, and model accuracy, for each configuration that you experiment with. 

      - To track resource utilization and performance metrics, you can use the Agent Platform console. 

      - To collect and analyze detailed performance metrics, use Cloud Monitoring. 

      - To view costs, use Cloud Billing reports (/billing/docs/reports) and Cloud Monitoring dashboards (/monitoring/dashboards). 

   - To identify performance bottlenecks in your models and optimize resource utilization, use profiling tools like Agent Platform TensorBoard (/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboardintroduction) 

5. **Analyze costs** : Compare the cost and performance of each configuration to identify the most cost-effective option. 

6. **Establish resource thresholds and improvement targets based on quotas** : Define thresholds for when scaling begins to yield diminishing returns in performance, such as minimal reduction in training time or latency for a significant cost increase. Consider project quotas when setting these thresholds. Determine the point where the cost and potential quota implications of further scaling are no longer justified by performance gains. 

7. **Refine iteratively** : Repeat the experimentation process with refined configurations based on your findings. Always ensure that the resource usage remains within your allocated quotas and aligns with established cost-benefit thresholds. 

#### Use MLOps to reduce inefficiencies

As organizations increasingly use ML to drive innovation and efficiency, managing the ML lifecycle effectively becomes critical. ML operations (MLOps) is a set of practices that automate and streamline the ML lifecycle, from model development to deployment and monitoring. 

Align MLOps with cost drivers 

To take advantage of MLOps for cost efficiency, identify the primary cost drivers in the ML lifecycle. Then, you can adopt and implement MLOps practices that are aligned with the cost drivers. Prioritize and adopt the MLOps features that address the most impactful cost drivers. This approach helps ensure a manageable and successful path to significant cost savings. 

Implement MLOps for cost optimization 

The following are common MLOps practices that help to reduce cost: 

- **Version control** : Tools like Git can help you to track versions of code, data, and models. Version control ensures reproducibility, facilitates collaboration, and prevents costly rework that can be caused by versioning issues. 

- **Continuous integration and continuous delivery (CI/CD)** : Cloud Build (/build/docs/overview) and Artifact Registry (/artifact-registry/docs/overview) let you implement CI/CD pipelines to automate building, testing, and deployment of your ML models. CI/CD pipelines ensure efficient resource utilization and minimize the costs associated with manual interventions. 

- **Observability** : Cloud Monitoring (/monitoring/docs/monitoring-overview) and Cloud Logging (/logging/docs/overview) let you track model performance in production, identify issues, and trigger alerts for proactive intervention. Observability lets you maintain model accuracy, optimize resource allocation, and prevent costly downtime or performance degradation. 

**Model retraining** : Gemini Enterprise Agent Platform Pipelines 

- (/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) simplifies the processes for retraining models periodically or when performance degrades. When you use Agent Platform Pipelines for retraining, it helps ensure that your models remain accurate and efficient, which can prevent unnecessary resource consumption and maintain optimal performance. 

**Automated testing and evaluation** : Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction) helps you accelerate and standardize model evaluation. Implement automated tests throughout the ML lifecycle to ensure the quality and reliability of your models. Such tests can help you catch errors early, prevent costly issues in production, and reduce the need for extensive manual testing. 

For more information, see MLOps: Continuous delivery and automation pipelines in machine learning 

- (/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning). 

### Enforce data management and governance practices

Effective data management and governance practices are critical to cost optimization. Well organized data can encourage teams to reuse datasets, avoid needless duplication, and reduce the effort to obtain high quality data. By 

proactively managing data, you can reduce storage costs, enhance data quality, and ensure that your ML models are trained on the most relevant and valuable data. 

To implement data management and governance practices, consider the following recommendations. 

#### Establish and adopt a data governance framework

The growing prominence of AI and ML has made data the most valuable asset for organizations that are undergoing digital transformation. A robust framework for data governance (https://cloud.google.com/learn/what-is-data-governance) is a crucial requirement for managing AI and ML workloads cost-effectively at scale. A data governance framework with clearly defined policies, procedures, and roles provides a structured approach for managing data throughout its lifecycle. Such a framework helps to improve data quality, enhance security, improve utilization, and reduce redundancy. 

Establish a data governance framework 

There are many pre-existing frameworks for data governance, such as the frameworks published by the EDM Council (https://edmcouncil.org/), with options available for different industries and organization sizes. Choose and adapt a framework that aligns with your specific needs and priorities. 

Implement the data governance framework 

Google Cloud provides the following services and tools to help you implement a robust data governance framework: 

- Knowledge Catalog (/dataplex/docs/introduction) is an intelligent data fabric that helps you unify distributed data and automate data governance without the need to consolidate data sets in one place. This helps to reduce the cost to distribute and maintain data, facilitate data discovery, and promote reuse. 

   - To organize data, use Knowledge Catalog abstractions and set up logical data lakes and zones (/dataplex/docs/create-lake). 

   - To administer access to data lakes and zones, use Google Groups (/iam/docs/groups-in-cloud-console) and Knowledge Catalog roles (/dataplex/docs/lake-security). 

   - To streamline data quality processes, enable auto data quality (/dataplex/docs/auto-data-quality-overview). 

- Knowledge Catalog is also a fully managed and scalable metadata management service. The catalog (/dataplex/docs/catalog-overview) provides a foundation that ensures that data assets are accessible and reusable. 

   - Metadata from the supported Google Cloud sources 

   - (/dataplex/docs/catalog-overview#supported-sources) is automatically ingested into the universal catalog. For data sources outside of Google Cloud, create custom entries 

   - (/dataplex/docs/ingest-custom-sources#create-custom-entry). 

   - To improve the discoverability and management of data assets, enrich technical metadata with business metadata by using aspects 

   - (/dataplex/docs/enrich-entries-metadata#aspects). 

   - Ensure that data scientists and ML practitioners have sufficient permissions (/dataplex/docs/iam-permissions) to access Knowledge Catalog and use the search (/dataplex/docs/search-assets) function. 

- BigQuery sharing (/bigquery/docs/analytics-hub-introduction) lets you efficiently and securely exchange data assets across your organizations to address challenges of data reliability and cost. 

   - Set up data exchanges (/bigquery/docs/analytics-hub-manage-exchanges) and ensure that curated data assets can be viewed as listings (/bigquery/docs/analytics-hub-manage-listings). 

   - Use data clean rooms (/bigquery/docs/data-clean-rooms) to securely manage access to sensitive data and efficiently partner with external teams and organizations on AI and ML projects. 

   - Ensure that data scientists and ML practitioners have sufficient permissions (/bigquery/docs/analytics-hub-grant-roles) to view and publish datasets to BigQuery sharing. 

#### Make datasets and features reusable throughout the ML lifecycle

For significant efficiency and cost benefits, reuse datasets and features across multiple ML projects. When you avoid redundant data engineering and feature development efforts, your organization can accelerate model development, reduce infrastructure costs, and free up valuable resources for other critical tasks. 

Google Cloud provides the following services and tools to help you reuse datasets and features: 

- Data and ML practitioners can publish data products 

- (/architecture/build-data-products-data-mesh) to maximize reuse across teams. The data products can then be discovered and used through Knowledge Catalog and BigQuery sharing. 

- For tabular and structured datasets, you can use Agent Platform Feature Store (/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview) to promote reusability and streamline feature management through BigQuery. 

- You can store unstructured data in Cloud Storage and govern the data by using BigQuery object tables and signed URLs 

- (/bigquery/docs/object-table-introduction). 

- You can manage vector embeddings by including metadata in your Vector Search indexes 

- (/gemini-enterprise-agent-platform/build/vector-search/create-manage-index). 

### Automate and streamline with MLOps

A primary benefit of adopting MLOps practices is a reduction in costs for technology and personnel. Automation helps you avoid the duplication of ML activities and reduce the workload for data scientists and ML engineers. 

To automate and streamline ML development with MLOps, consider the following recommendations. 

#### Automate and standardize data collection and processing

To help reduce ML development effort and time, automate and standardize your data collection and processing technologies. 

Automate data collection and processing 

This section summarizes the products, tools, and techniques that you can use to automate data collection and processing. 

Identify and choose the relevant data sources for your AI and ML tasks: 

- Database options such as Cloud SQL (/sql/docs/introduction), Spanner (/spanner), AlloyDB for PostgreSQL (/alloydb/docs/overview), Firestore (/firestore/native/docs), and BigQuery (/bigquery/docs/introduction). Your choice depends on your requirements, such as latency on write access (static or dynamic), data volume (high or low), and data format (structured, unstructured, or semistructured). For more information, see Google Cloud databases 

- (https://cloud.google.com/products/databases#our-portfolio-of-databases). 

- Data lakes such as Cloud Storage with BigLake (/bigquery/docs/biglake-intro). 

- Knowledge Catalog (/dataplex/docs/introduction) for governing data across sources. 

- Streaming events platforms such as Pub/Sub (/pubsub/docs/overview), Dataflow (/dataflow/docs/overview), or Apache Kafka (https://kafka.apache.org/). 

External APIs. 

For each of your data sources, choose an ingestion tool: 

- Dataflow: For batch and stream processing of data from various sources, with ML-component integration. For an event-driven architecture, you can combine Dataflow with Eventarc (/eventarc/docs) to efficiently process data for ML. To enhance MLOps and ML job efficiency, use GPU and right-fitting capabilities. 

- Cloud Run functions (/run/docs/resource-model#functions): For event-driven data ingestion that gets triggered by changes in data sources for real-time applications. 

- BigQuery: For classical tabular data ingestion with frequent access. 

Choose tools for data transformation and loading: 

- Use tools such as Dataflow (/dataflow/docs/overview) or Dataform (/dataform/docs/overview) to automate data transformations like feature scaling, encoding categorical variables, and creating new features in batch, streaming, 

or real time. The tools that you select depend upon your requirements and chosen services. 

Use Feature Store 

- (/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview) to automate feature creation and management. You can centralize features for reuse across different models and projects. 

Standardize data collection and processing 

To discover, understand, and manage data assets, use metadata management services like Knowledge Catalog (/dataplex/docs/catalog-overview). It helps you standardize data definitions and ensure consistency across your organization. 

To enforce standardization and avoid the cost of maintaining multiple custom implementations, use automated training pipelines and orchestration. For more information, see the next section. 

#### Automate training pipelines and reuse existing assets

To boost efficiency and productivity in MLOps, automated training pipelines are crucial. Google Cloud offers a robust set of tools and services to build and deploy training pipelines, with a strong emphasis on reusing existing assets. Automated training pipelines help to accelerate model development, ensure consistency, and reduce redundant effort. 

Automate training pipelines 

The following table describes the Google Cloud services and features that you can use to automate the different functions of a training pipeline. 

|Function<br>G|oogle Cloud services and features|
|---|---|
|Orchestration:<br>Define<br>complex ML<br>workflows<br>consisting of<br>multiple steps|To create and orchestrate pipelines, use<br>Agent Platform Pipelines<br>(/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) o<br>Kubeflow Pipelines. These tools support simple data transformation, model<br>training, model deployment, and pipeline versioning. They let you define<br>dependencies between steps, manage data flow, and automate the execution<br>the entire workflow.|
|and<br>dependencies.<br>You can define<br>each step as a<br>separate<br>containerized|For complex operational tasks with heavy CI/CD and extract, transform, and lo<br>(ETL) requirements, use<br>Managed Service for Apache Airflow<br>(/composer/docs/composer-3/composer-overview). If you prefer Airflow for dat<br>orchestration, Managed Service for Apache Airflow is a compatible managed<br>service that's built on Airflow.|
|task, which<br>helps you<br>manage and<br>scale<br>individual<br>tasks with<br>ease.|For pipelines that are managed outside of Agent Platform Pipelines, use<br>Workflows(/workflows/docs/choose-orchestration) for infrastructure-focused<br>tasks like starting and stopping VMs or integrating with external systems.<br>To automate your CI/CD process, use<br>Cloud Build(/build/docs/overview) with<br>Pub/Sub(/pubsub/docs/overview). You can set up notifications and automatic<br>triggers for when new code is pushed or when a new model needs to be traine<br>For a fully-managed, scalable solution for pipeline management, use<br>Cloud Da<br>Fusion(/data-fusion/docs/concepts/overview).|

Versioning: Store Kubefow pipeline l (/artifact-registry/docs/kfp) templates in a Kubeflow Track and Pipelines repository in Artifact Registry (/artifact-registry/docs/overview). control different versions of pipelines and components to ensure reproducibility and auditability. 

Function Google Cloud services and features Reusability: Store your pipeline templates in Cloud Storage (/storage/docs/introduction) and Reuse existingshare them across your organization. pipeline components and artifacts, such as prepared datasets and trained models, to accelerate development. Monitoring: Use Cloud Logging and Cloud Monitoring. For more information, see Monitor Monitor resources continuously with dashboards, alerts, and reports pipeline (/architecture/framework/perspectives/ai-ml/costexecution to optimization#monitor_resources_continuously_with_dashboards_alerts_and_repor identify and . address any issues. 

Expand reusability beyond pipelines 

Look for opportunities to expand reusability beyond training pipelines. The following are examples of Google Cloud capabilities that let you reuse ML features, datasets, models, and code. 

Feature Store 

(/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview) provides a centralized repository for organizing, storing, and serving ML features. It lets you reuse features across different projects and models, which can improve consistency and reduce feature engineering effort. You can store, share, and access features for both online and offline use cases. 

Agent Platform datasets 

(/gemini-enterprise-agent-platform/machine-learning/datasets/overview) enable teams to create and manage datasets centrally, so your organization can maximize reusability and reduce data duplication. Your teams can search and discover the datasets by using Knowledge Catalog (/dataplex/docs/catalog-overview). 

Model Registry on Gemini Enterprise Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction) lets you store, manage, and deploy your trained models. Model Registry lets you reuse the models in subsequent pipelines or for online prediction, which helps you take advantage of previous training efforts. 

Custom containers 

- (/gemini-enterprise-agent-platform/machine-learning/training/containers-overview) let you package your training code and dependencies into containers and store the containers in Artifact Registry. Custom containers let you provide consistent and reproducible training environments across different pipelines and projects. 

#### Use Google Cloud services for model evaluation and tuning

Google Cloud offers a powerful suite of tools and services to streamline and automate model evaluation and tuning. These tools and services can help you reduce your time to production and reduce the resources required for continuous training and monitoring. By using these services, your AI and ML teams can enhance model performance with fewer expensive iterations, achieve faster results, and minimize wasted compute resources. 

Use resource-efficient model evaluation and experimentation 

Begin an AI project with experiments before you scale up your solution. In your experiments, track various metadata such as dataset version, model parameters, and model type. For further reproducibility and comparison of the results, use metadata tracking in addition to code versioning, similar to the capabilities in Git. To avoid missing information or deploying the wrong version in production, use Experiments on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments) before you implement full-scale deployment or training jobs. 

Experiments on Agent Platform lets you do the following: 

- Streamline and automate metadata tracking and discovery through a user friendly UI and API for production-ready workloads. 

- Analyze the model's performance metrics and compare metrics across multiple models. 

After the model is trained, continuously monitor the performance and data drift over time for incoming data. To streamline this process, use Model Monitoring on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) to directly access the created models in Model Registry 

(/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction). Model Monitoring on Agent Platform also automates monitoring for data and results through online and batch predictions. You can export the results to BigQuery for further analysis and tracking. 

Choose optimal strategies to automate training 

For hyperparameter tuning, we recommend the following approaches: 

   - To automate the process of finding the optimal hyperparameters for your models, use Agent Platform hyperparameter tuning 

   - (/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuningoverview) 

   - . Agent Platform uses advanced algorithms to explore the hyperparameter space and identify the best configuration. 

   - For efficient hyperparameter tuning, consider using Bayesian optimization (/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuningoverview#understanding-trials) 

   - techniques, especially when you deal with complex models and large datasets. 

- For distributed training, we recommend the following approaches: 

   - For large datasets and complex models, use the distributed training infrastructure of Agent Platform. This approach lets you train your models on multiple machines, which helps to significantly reduce training time and associated costs. Use tools like the following: 

      - Agent Platform tuning (/gemini-enterprise-agent-platform/models/tuning) to perform supervised fine-tuning of Gemini, Imagen, and other models. 

Agent Platform Managed Training 

- (/gemini-enterprise-agent-platform/machine-learning/training-overview) or Ray on Gemini Enterprise Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/open-source/ray) for custom distributed training. 

Choose optimized ML frameworks, like Keras and PyTorch, that support distributed training and efficient resource utilization. 

Use explainable AI 

It's crucial to understand why a model makes certain decisions and to identify potential biases or areas for improvement. Use explainability techniques to gain insights into your model's predictions. 

- **Feature-based** : To understand which features are most influential in your model's predictions, analyze feature attributions 

- (/gemini-enterprise-agent-platform/machine-learning/tabular-data/classificationexplanations) 

- . This understanding can guide feature-engineering efforts and improve model interpretability. 

- **Example-based** : To return a list of examples (typically from the training set) that are most similar to the input, use nearest-neighbor search. Because similar inputs generally yield similar predictions, you can use these explanations to explore and explain a model's behavior. 

### Use managed services and pre-trained models

Adopt an incremental approach to model selection and model development. This approach helps you avoid excessive costs that are associated with starting afresh every time. To control costs, use ML frameworks, managed services, and pretrained models. 

To get the maximum value from managed services and pre-trained models, consider the following recommendations. 

#### Use notebooks for exploration and experiments

Notebook (https://en.wikipedia.org/wiki/Notebook_interface) environments are crucial for cost-effective ML experimentation. A notebook provides an interactive and collaborative space for data scientists and engineers to explore data, develop models, share knowledge, and iterate efficiently. Collaboration and knowledge sharing through notebooks significantly accelerates development, code reviews, and knowledge transfer. Notebooks help streamline workflows and reduce duplicated effort. 

Instead of procuring and managing expensive hardware for your development environment, you can use the scalable and on-demand infrastructure of Gemini Enterprise Agent Platform Workbench and Colab Enterprise. 

Agent Platform Workbench 

- (/gemini-enterprise-agent-platform/notebooks/workbench/introduction) is a Jupyter notebook development environment for the entire data science workflow. You can interact with Agent Platform and other Google Cloud services from within an instance's Jupyter notebook. Agent Platform Workbench integrations and features help you do the following: 

   - Access and explore data from a Jupyter notebook by using BigQuery and Cloud Storage integrations. 

   - Automate recurring updates to a model by using scheduled executions of code that runs on Agent Platform. 

   - Process data quickly by running a notebook on a Managed Service for Apache Spark cluster. 

   - Run a notebook as a step in a pipeline by using Agent Platform Pipelines. 

- Colab Enterprise (/colab/docs/introduction) is a collaborative, managed notebook environment that has the security and compliance capabilities of Google Cloud. Colab Enterprise is ideal if your project's priorities include collaborative development and reducing the effort to manage infrastructure. Colab Enterprise integrates with Google Cloud services and AI-powered assistance that uses Gemini. Colab Enterprise lets you do the following: 

   - Work in notebooks without the need to manage infrastructure. 

   - Share a notebook with a single user, Google group, or Google Workspace domain. You can control notebook access through Identity and Access Management (IAM). 

Interact with features built into Agent Platform and BigQuery. 

To track changes and revert to previous versions when necessary, you can integrate your notebooks with version control tools like Git. 

#### Start with existing and pre-trained models

Training complex models from scratch, especially deep-learning models, requires significant computational resources and time. To accelerate your model selection and development process, start with existing and pre-trained models. These models, which are trained on vast datasets, eliminate the need to train models from scratch and significantly reduce cost and development time. 

Reduce training and development costs 

Select an appropriate model or API for each ML task and combine them to create an end-to-end ML development process. 

Model Garden (/gemini-enterprise-agent-platform/models/model-garden/explore-models) offers a vast collection of pre-trained models for tasks such as image classification, object detection, and natural language processing. The models are grouped into the following categories: 

- Google models like the Gemini family of models and Imagen for image generation. 

- Open models like Gemma and Llama. 

- Third-party models from partners like Anthropic. 

Google Cloud provides AI and ML APIs (https://cloud.google.com/ai/apis) that let developers integrate powerful AI capabilities into applications without the need to build models from scratch. 

- Cloud Vision API (/vision/docs/apis) lets you derive insights from images. This API is valuable for applications like image analysis, content moderation, and automated data entry. 

- Cloud Natural Language API (/natural-language/docs/apis) lets you analyze text to understand its structure and meaning. This API is useful for tasks like 

customer feedback analysis, content categorization, and understanding social media trends. 

- Speech-to-Text API (/speech-to-text/docs/apis) converts audio to text. This API supports a wide range of languages and dialects. 

- Video Intelligence API (/video-intelligence/docs/apis) analyzes video content to identify objects, scenes, and actions. Use this API for video content analysis, content moderation, and video search. 

- Document AI API (/document-ai/docs/reference) processes documents to extract, classify, and understand data. This API helps you automate document processing workflows. 

- Dialogflow API (/dialogflow/cx/docs/reference) enables the creation of conversational interfaces, such as chatbots and voice assistants. You can use this API to create customer service bots and virtual assistants. 

- Gemini API (/gemini-enterprise-agent-platform/reference/models/inference) provides access to Google's most capable and general-purpose AI model. 

Reduce tuning costs 

To help reduce the need for extensive data and compute time, fine-tune your pretrained models on specific datasets. We recommend the following approaches: 

- **Learning transfer** : Use the knowledge from a pre-trained model for a new task, instead of starting from scratch. This approach requires less data and compute time, which helps to reduce costs. 

**Adapter tuning (parameter-efcient tuningfi** 

(/gemini-enterprise-agent-platform/models/tuning#parameter-tuning) **)** : Adapt models to new tasks or domains without full fine-tuning. This approach requires significantly lower computational resources and a smaller dataset. 

**Supervised fine tuning** 

(/gemini-enterprise-agent-platform/models/tuning/supervised-tuning): Adapt model behavior with a labeled dataset. This approach simplifies the management of the underlying infrastructure and the development effort that's required for a custom training job. 

Explore and experiment by using Agent Studio on Gemini Enterprise Agent Platform 

Agent Studio (/gemini-enterprise-agent-platform/agent-studio) lets you rapidly test, prototype, and deploy generative AI applications. 

- **Integration with Model Garden** : Provides quick access to the latest models and lets you efficiently deploy the models to save time and costs. 

- **Unified access to specialized models** : Consolidates access to a wide range of pre-trained models and APIs, including those for chat, text, media, translation, and speech. This unified access can help you reduce the time spent searching for and integrating individual services. 

#### Use managed services to train or serve models

Managed services can help reduce the cost of model training and simplify the infrastructure management, which lets you focus on model development and optimization. This approach can result in significant cost benefits and increased efficiency. 

Reduce operational overhead 

To reduce the complexity and cost of infrastructure management, use managed services such as the following: 

Agent Platform Managed Training 

- (/gemini-enterprise-agent-platform/machine-learning/training-overview) provides a fully managed environment for training your models at scale. You can choose from various prebuilt containers with popular ML frameworks or use your own custom containers. Google Cloud handles infrastructure provisioning, scaling, and maintenance, so you incur lower operational overhead. 

Agent Platform Inference 

- (/gemini-enterprise-agent-platform/machine-learning/predictions/overview) handles infrastructure scaling, load balancing, and request routing. You get high availability and performance without manual intervention. 

Ray on Gemini Enterprise Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/open-source/ray) provides a fully 

managed Ray cluster. You can use the cluster to run complex custom AI workloads that perform many computations (hyperparameter tuning, model fine-tuning, distributed model training, and reinforcement learning from human feedback) without the need to manage your own infrastructure. 

Use managed services to optimize resource utilization 

For details about efficient resource utilization, see Optimize resource utilization (/architecture/framework/perspectives/ai-ml/cost-optimization#optimize_resource_allocation). 

### Contributors

Authors: 

- Isaac Lo (https://www.linkedin.com/in/isaac-l-25525440) | AI Business Development Manager 

- Anastasia Prokaeva (https://www.linkedin.com/in/anastasiia-prokaieva) | Field Solutions Architect, Generative AI 

- Amy Southwood (https://www.linkedin.com/in/amycsouthwood) | Technical Solutions Consultant, Data Analytics, and AI 

Other contributors: 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

- Nicolas Pintaux (https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist 

## AI and ML perspective: Performance optimization

This document in the Google Cloud Well-Architected Framework: AI and ML perspective (/architecture/framework/perspectives/ai-ml) provides principles and recommendations to help you optimize the performance of your AI and ML workloads on Google Cloud. The recommendations in this document align with the performance optimization pillar (/architecture/framework/performance-optimization) of the Well-Architected Framework. 

AI and ML systems enable advanced automation and decision-making capabilities for your organization. The performance of these systems can directly affect important business drivers like revenue, costs, and customer satisfaction. To realize the full potential of AI and ML systems, you must optimize their performance based on your business goals and technical requirements. The performance optimization process often involves trade-offs. For example, a design choice that provides the required performance might lead to higher costs. The recommendations in this document prioritize performance over other considerations. 

To optimize AI and ML performance, you need to make decisions regarding factors like the model architecture, parameters, and training strategy. When you make these decisions, consider the entire lifecycle of the AI and ML systems and their deployment environment. For example, very large LLMs can be highly performant on massive training infrastructure, but might not perform well in capacityconstrained environments like mobile devices. 

The recommendations in this document are mapped to the following core principles: 

- Establish performance objectives and evaluation methods (#performance-objectives-evaluation-methods) 

Run and track frequent experiments (#run-track-exp) 

- Build and automate training and serving infrastructure 

- (#build-automate-training-serving) 

Match design choices to performance requirements (#match-design-performance) 

- Link performance metrics to design and configuration choices (#link-perf-design)
