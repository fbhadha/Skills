# Architecture: Well-Architected Framework and reference designs / Well-Architected Framework: AI and ML perspective: Well-Architected Framework: AI and ML perspective to AI and ML perspective: Security: Deploy on secure systems with secure tools and artifacts
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 234-273, extracted 2026-10-18

## Well-Architected Framework: AI and ML perspective

URL: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable

Last reviewed 2025-02-14 UTC 

This document in the Google Cloud Well-Architected Framework 

(/architecture/framework) describes principles and recommendations to help you to design, build, and manage AI and ML workloads in Google Cloud that meet your operational, security, reliability, cost, and performance goals. 

The target audience for this document includes decision makers, architects, administrators, developers, and operators who design, build, deploy, and maintain AI and ML workloads in Google Cloud. 

The following pages describe principles and recommendations that are specific to AI and ML, for each pillar of the Well-Architected Framework: 

AI and ML perspective: Operational excellence 

- (/architecture/framework/perspectives/ai-ml/operational-excellence) 

- AI and ML perspective: Security 

- (/architecture/framework/perspectives/ai-ml/security) 

- AI and ML perspective: Reliability 

- (/architecture/framework/perspectives/ai-ml/reliability) 

- AI and ML perspective: Cost optimization 

- (/architecture/framework/perspectives/ai-ml/cost-optimization) 

- AI and ML perspective: Performance optimization 

- (/architecture/framework/perspectives/ai-ml/performance-optimization) 

### Contributors

Authors: 

- Benjamin Sadik (https://www.linkedin.com/in/benjaminhaimsadik) | AI and ML Specialist Customer Engineer 

- Charlotte Gistelinck, PhD (https://www.linkedin.com/in/charlottegistelinck) | Partner Engineer 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Isaac Lo (https://www.linkedin.com/in/isaac-l-25525440) | AI Business Development Manager 

- Kamilla Kurta (https://www.linkedin.com/in/kamillakurta) | GenAI/ML Specialist Customer Engineer 

- Mohamed Fawzi (https://www.linkedin.com/in/fawzii) | Benelux Security and Compliance Lead 

- Rick (Rugui) Chen (https://www.linkedin.com/in/rugui-chen) | AI Infrastructure Field Solutions Architect 

- Sannya Dang (https://www.linkedin.com/in/thugiangdang) | AI Solution Architect 

Other contributors: 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect 

- Gary Harmson (https://www.linkedin.com/in/garyharmson) | Principal Architect 

- Jose Andrade (https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

- Nicolas Pintaux (https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist 

- Radhika Kanakam (https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework 

- Ryan Cox (https://www.linkedin.com/in/ryanlcox) | Principal Architect 

- Samantha He (https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer 

- Stef Ruinard (https://www.linkedin.com/in/stefruinard) | Generative AI Field Solutions Architect 

- Wade Holmes (https://www.linkedin.com/in/wholmes) | Global Solutions Director Zach Seils (https://www.linkedin.com/in/zachseils) | Networking Specialist 

## AI and ML perspective: Operational excellence

This document in the Well-Architected Framework: AI and ML perspective (/architecture/framework/perspectives/ai-ml) provides an overview of the principles and recommendations to build and operate robust AI and ML systems on Google Cloud. These recommendations help you set up foundational elements like observability, automation, and scalability. The recommendations in this document align with the operational excellence pillar (/architecture/framework/operational-excellence) of the Google Cloud Well-Architected Framework. 

Operational excellence within the AI and ML domain is the ability to seamlessly deploy, manage, and govern the AI and ML systems and pipelines that help drive your organization's strategic objectives. Operational excellence lets you respond efficiently to changes, reduce operational complexity, and ensure that your operations remain aligned with business goals. 

The recommendations in this document are mapped to the following core principles: 

- Build a robust foundation for model development 

- (#build_a_robust_foundation_for_model_development) 

- Automate the model development lifecycle (#automate_the_model-development_lifecycle) 

- Implement observability (#implement_observability) 

- Build a culture of operational excellence (#build_a_culture_of_operational_excellence) 

- Design for scalability (#design_for_scalability) 

### Build a robust foundation for model development

To develop and deploy scalable, reliable AI systems that help you achieve your business goals, a robust model-development foundation is essential. Such a foundation enables consistent workflows, automates critical steps in order to reduce errors, and ensures that the models can scale with demand. A strong model-development foundation ensures that your ML systems can be updated, improved, and retrained seamlessly. The foundation also helps you to align your models' performance with business needs, deploy impactful AI solutions quickly, and adapt to changing requirements. 

To build a robust foundation to develop your AI models, consider the following recommendations. 

#### Define the problems and the required outcomes

Before you start any AI or ML project, you must have a clear understanding of the business problems to be solved and the required outcomes. Start with an outline of the business objectives and break the objectives down into measurable key performance indicators (KPIs). To organize and document your problem definitions and hypotheses in a Jupyter notebook environment, use tools like Gemini Enterprise Agent Platform Workbench 

(/gemini-enterprise-agent-platform/notebooks/workbench/introduction). To implement versioning for code and documents and to document your projects, goals, and assumptions, use tools like Git. To develop and manage prompts for generative AI applications, you can use Agent Studio on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/agent-studio/quickstart). 

#### Collect and preprocess the necessary data

To implement data preprocessing and transformation, you can use Dataflow (/dataflow/docs/overview) (for Apache Beam), Managed Service for Apache Spark (/dataproc-serverless/docs/overview) (for Apache Spark), or BigQuery 

(/bigquery/docs/introduction) if an SQL-based process is appropriate. To validate schemas and detect anomalies, use TensorFlow Data Validation (TFDV) (https://www.tensorflow.org/tfx/data_validation/get_started) and take advantage of 

automated data quality scans (/bigquery/docs/data-quality-scan) in BigQuery where applicable. 

For generative AI, data quality includes accuracy, relevance, diversity, and alignment with the required output characteristics. In cases where real-world data is insufficient or imbalanced, you can generate synthetic data to help improve model robustness and generalization. To create synthetic datasets based on existing patterns or to augment training data for better model performance, use BigQuery DataFrames (/bigquery/docs/bigquery-dataframes-introduction). Synthetic data is particularly valuable for generative AI because it can help improve prompt diversity and overall model robustness. When you build datasets for fine-tuning generative AI models, consider using the synthetic data generation capabilities in Gemini Enterprise Agent Platform. 

For generative AI tasks like fine-tuning or reinforcement learning from human feedback (RLHF), ensure that labels accurately reflect the quality, relevance, and safety of the generated outputs. 

#### Select an appropriate ML approach

When you design your model and parameters, consider the model's complexity and computational needs. Depending on the task (such as classification, regression, or generation), consider using Agent Platform custom training 

(/gemini-enterprise-agent-platform/machine-learning/training/overview) for custom model building or AutoML for simpler ML tasks. For common applications, you can also access pretrained models through Model Garden 

(/gemini-enterprise-agent-platform/models/model-garden/explore-models). You can experiment with a variety of state-of-the-art foundation models for various use cases, such as generating text, images, and code. 

You might want to fine-tune a pretrained foundation model to achieve optimal performance for your specific use case. For high-performance requirements in custom training, configure Cloud Tensor Processing Units (TPUs) (/tpu) or GPU resources (/compute/docs/gpus) to accelerate the training and inference of deeplearning models, like large language models (LLMs) and diffusion models. 

#### Set up version control for code, models, and data

To manage and deploy code versions effectively, use tools like GitHub or GitLab. These tools provide robust collaboration features, branching strategies, and integration with CI/CD pipelines to ensure a streamlined development process. 

Use appropriate solutions to manage each artifact of your ML system, like the following examples: 

- For code artifacts like container images and pipeline components, Artifact Registry (/artifact-registry/docs/overview) provides a scalable storage solution that can help improve security. Artifact Registry also includes versioning and can integrate with Cloud Build (/build/docs/overview) and Cloud Deploy (/deploy/docs/overview). 

- To manage data artifacts, like datasets used for training and evaluation, use solutions like BigQuery or Cloud Storage (/storage/docs/introduction) for storage and versioning. 

- To store metadata and pointers to data locations, use your version control system or a separate data catalog. 

To maintain the consistency and versioning of your feature data, use Agent Platform Feature Store 

(/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview). To track and manage model artifacts, including binaries and metadata, use Model Registry on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction), which lets you store, organize, and deploy model versions seamlessly. 

To ensure model reliability, implement Model Monitoring on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview). Detect data drift, track performance, and identify anomalies in production. For generative AI systems, monitor shifts in output quality and safety compliance. 

### Automate the model-development lifecycle

Automation helps you to streamline every stage of the AI and ML lifecycle. Automation reduces manual effort and standardizes processes, which leads to enhanced operational efficiency and a lower risk of errors. Automated workflows 

enable faster iteration, consistent deployment across environments, and more reliable outcomes, so your systems can scale and adapt seamlessly. 

To automate the development lifecycle of your AI and ML systems, consider the following recommendations. 

#### Use a managed pipeline orchestration system

Use Gemini Enterprise Agent Platform Pipelines 

(/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) to automate every step of the ML lifecycle—from data preparation to model training, evaluation, and deployment. To accelerate deployment and promote consistency across projects, automate recurring tasks with scheduled pipeline runs 

(/gemini-enterprise-agent-platform/machine-learning/pipelines/schedule-pipeline-run), monitor workflows with execution metrics 

(/gemini-enterprise-agent-platform/machine-learning/pipelines/metrics), and develop reusable pipeline templates 

(/gemini-enterprise-agent-platform/machine-learning/pipelines/create-pipeline-template) for standardized workflows. These capabilities extend to generative AI models, which often require specialized steps like prompt engineering 

(/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies), response filtering, and human-in-the-loop (https://cloud.google.com/discover/human-in-the-loop) evaluation. For generative AI, Agent Platform Pipelines can automate these steps, including the evaluation of generated outputs against quality metrics and safety guidelines. To improve prompt diversity and model robustness, automated workflows can also include data augmentation techniques. 

#### Implement CI/CD pipelines

To automate the building, testing, and deployment of ML models, use Cloud Build. This service is particularly effective when you run test suites for application code, which ensures that the infrastructure, dependencies, and model packaging meet your deployment requirements. 

ML systems often need additional steps beyond code testing. For example, you need to stress test the models under varying loads, perform bulk evaluations to assess model performance across diverse datasets, and validate data integrity before retraining. To simulate realistic workloads for stress tests, you can use tools 

like Locust (https://locust.io/), Grafana k6 (https://grafana.com/docs/k6/latest/), or Apache JMeter (https://jmeter.apache.org/). To identify bottlenecks, monitor key metrics like latency, error rate, and resource utilization through Cloud Monitoring 

(/monitoring/docs/monitoring-overview). For generative AI, the testing must also include evaluations that are specific to the type of generated content, such as text quality, image fidelity, or code functionality. These evaluations can involve automated metrics like perplexity 

(https://developers.google.com/machine-learning/glossary#perplexity) for language models or human-in-the-loop evaluation for more nuanced aspects like creativity and safety. 

To implement testing and evaluation tasks, you can integrate Cloud Build with other Google Cloud services. For example, you can use Agent Platform Pipelines for automated model evaluation, BigQuery (/bigquery/docs/introduction) for large-scale data analysis, and Dataflow pipeline validation for feature validation. 

You can further enhance your CI/CD pipeline by using Agent Platform for continuous training 

(/gemini-enterprise-agent-platform/machine-learning/pipelines/continuous-training-tutorial) to enable automated retraining of models on new data. Specifically for generative AI, to keep the generated outputs relevant and diverse, the retraining might involve automatically updating the models with new training data or prompts. You can use Agent Platform Model Garden 

(/gemini-enterprise-agent-platform/models/model-garden/explore-models) to select the latest base models that are available for tuning. This practice ensures that the models remain current and optimized for your evolving business needs. 

#### Implement safe and controlled model releases

To minimize risks and ensure reliable deployments, implement a model release approach that lets you detect issues early, validate performance, and roll back quickly when required. 

To package your ML models and applications into container images and deploy them, use Cloud Deploy (/deploy/docs/overview). You can deploy your models to Agent Platform endpoints 

(/gemini-enterprise-agent-platform/machine-learning/general/deployment). 

Implement controlled releases for your AI applications and systems by using strategies like canary releases (https://en.wikipedia.org/wiki/Canary_release). For applications that use managed models like Gemini, we recommend that you gradually release new application versions to a subset of users before the full deployment. This approach lets you detect potential issues early, especially when you use generative AI models where outputs can vary. 

To release fine-tuned models, you can use Cloud Deploy to manage the deployment of the model versions, and use the canary release strategy to minimize risk. With managed models and fine-tuned models, the goal of controlled releases is to test changes with a limited audience before you release the applications and models to all users. 

For robust validation, use Experiments on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-ai-experiments) to compare new models against existing ones, and use Agent Platform model evaluation (/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction) to assess model performance. Specifically for generative AI, define evaluation metrics that align with the intended use case and the potential risks. You can use the Gen AI evaluation service in Agent Platform to assess metrics like toxicity, coherence, factual accuracy, and adherence to safety guidelines. 

To ensure deployment reliability, you need a robust rollback plan. For traditional ML systems, use Model Monitoring on Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) to detect data drift and performance degradation. For generative AI models, you can track relevant metrics and set up alerts for shifts in output quality or the emergence of harmful content by using Agent Platform model evaluation along with Cloud Logging and Cloud Monitoring. Configure alerts based on generative AI-specific metrics to trigger rollback procedures when necessary. To track model lineage and revert to the most recent stable version, use insights from Model Registry 

(/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction). 

### Implement observability

The behavior of AI and ML systems can change over time due to changes in the data or environment and updates to the models. This dynamic nature makes 

observability crucial to detect performance issues, biases, or unexpected behavior. This is especially true for generative AI models because the outputs can be highly variable and subjective. Observability lets you proactively address unexpected behavior and ensure that your AI and ML systems remain reliable, accurate, and fair. 

To implement observability for your AI and ML systems, consider the following recommendations. 

#### Monitor performance continuously

Use metrics and success criteria for ongoing evaluation of models after deployment. 

You can use Model Monitoring on Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) to proactively track model performance, identify training-serving skew and prediction drift, and receive alerts to trigger necessary model retraining or other interventions. To effectively monitor for training-serving skew, construct a golden dataset (https://developers.google.com/machine-learning/glossary#golden-dataset) that represents the ideal data distribution, and use TFDV 

(https://www.tensorflow.org/tfx/data_validation/get_started) to analyze your training data and establish a baseline schema. 

Configure Model Monitoring on Agent Platform to compare the distribution of input data against the golden dataset for automatic skew detection. For traditional ML models, focus on metrics 

(https://developers.google.com/machine-learning/crash-course/classification/accuracyprecision-recall) 

like accuracy, precision, recall, F1-score, AUC-ROC, and log loss. Define custom thresholds for alerts in Model Monitoring on Agent Platform. For generative AI, use the Gen AI evaluation service 

(/gemini-enterprise-agent-platform/models/evaluation-overview) to continuously monitor model output in production. You can also enable automatic evaluation metrics for response quality, safety, instruction adherence, grounding, writing style, and verbosity. To assess the generated outputs for quality, relevance, safety, and adherence to guidelines, you can incorporate human-in-the-loop 

(https://cloud.google.com/discover/human-in-the-loop) evaluation. 

Create feedback loops to automatically retrain models with Agent Platform Pipelines when Model Monitoring on Agent Platform triggers an alert. Use these insights to improve your models continuously. 

#### Evaluate models during development

Before you deploy your LLMs and other generative AI models, thoroughly evaluate them during the development phase. Use Agent Platform model evaluation to achieve optimal performance and to mitigate risk. Use Agent Platform rapid evaluation (/gemini-enterprise-agent-platform/models/run-evaluation) to let Google Cloud automatically run evaluations based on the dataset and prompts that you provide. 

You can also define and integrate custom metrics that are specific to your use case. For feedback on generated content, integrate human-in-the-loop workflows by using Agent Platform Model Evaluation. 

Use adversarial testing 

(https://developers.google.com/machine-learning/guides/adv-testing) to identify vulnerabilities and potential failure modes. To identify and mitigate potential biases, use techniques like subgroup analysis and counterfactual generation. Use the insights gathered from the evaluations that were completed during the development phase to define your model monitoring strategy in production. Prepare your solution for continuous monitoring as described in the Monitor performance continuously (#automated-performance-monitoring) section of this document. 

#### Monitor for availability

To gain visibility into the health and performance of your deployed endpoints and infrastructure, use Cloud Monitoring (/monitoring/docs/monitoring-overview). For your Agent Platform endpoints, track key metrics like request rate, error rate, latency, and resource utilization, and set up alerts for anomalies. For more information, see Cloud Monitoring metrics for Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/general/monitoring-metrics). 

Monitor the health of the underlying infrastructure, which can include Compute Engine instances, Google Kubernetes Engine (GKE) clusters, and TPUs and GPUs. Get automated optimization recommendations from Active Assist 

(/recommender/docs/whatis-activeassist). If you use autoscaling, monitor the scaling behavior to ensure that autoscaling responds appropriately to changes in traffic patterns. 

Track the status of model deployments, including canary releases and rollbacks, by integrating Cloud Deploy with Cloud Monitoring. In addition, monitor for potential security threats and vulnerabilities by using Security Command Center 

(/security-command-center/docs/security-command-center-overview). 

#### Set up custom alerts for business-specific thresholds

For timely identification and rectification of anomalies and issues, set up custom alerting based on thresholds that are specific to your business objectives. Examples of Google Cloud products that you can use to implement a custom alerting system include the following: 

- Cloud Logging (/logging/docs/overview): Collect, store, and analyze logs from all components of your AI and ML system. 

- Cloud Monitoring: Create custom dashboards to visualize key metrics and trends, and define custom metrics based on your needs. Configure alerts to get notifications about critical issues, and integrate the alerts with your incident management tools like PagerDuty or Slack. 

- Error Reporting (/error-reporting/docs/grouping-errors): Automatically capture and analyze errors and exceptions. 

- Cloud Trace (/trace/docs/overview): Analyze the performance of distributed systems and identify bottlenecks. Tracing is particularly useful for understanding latency between different components of your AI and ML pipeline. 

- Cloud Profiler (/profiler/docs/about-profiler): Continuously analyze the performance of your code in production and identify performance bottlenecks in CPU or memory usage. 

### Build a culture of operational excellence

Shift the focus from just building models to building sustainable, reliable, and impactful AI solutions. Empower teams to continuously learn, innovate, and improve, which leads to faster development cycles, reduced errors, and increased efficiency. By prioritizing automation, standardization, and ethical considerations, you can ensure that your AI and ML initiatives consistently deliver value, mitigate risks, and promote responsible AI development. 

To build a culture of operational excellence for your AI and ML systems, consider the following recommendations. 

#### Champion automation and standardization

To emphasize efficiency and consistency, embed automation and standardized practices into every stage of the AI and ML lifecycle. Automation reduces manual errors and frees teams to focus on innovation. Standardization ensures that processes are repeatable and scalable across teams and projects. 

#### Prioritize continuous learning and improvement

Foster an environment where ongoing education and experimentation are core principles. Encourage teams to stay up-to-date with AI and ML advancements, and provide opportunities to learn from past projects. A culture of curiosity and adaptation drives innovation and ensures that teams are equipped to meet new challenges. 

#### Cultivate accountability and ownership

Build trust and alignment with clearly defined roles, responsibilities, and metrics for success. Empower teams to make informed decisions within these boundaries, and establish transparent ways to measure progress. A sense of ownership motivates teams and ensures collective responsibility for outcomes. 

#### Embed AI ethics and safety considerations

Prioritize considerations for ethics in every stage of development. Encourage teams to think critically about the impact of their AI solutions, and foster discussions on fairness, bias, and societal impact. Clear principles and 

accountability mechanisms ensure that your AI systems align with organizational values and promote trust. 

### Design for scalability

To accommodate growing data volumes and user demands and to maximize the value of AI investments, your AI and ML systems need to be scalable. The systems must adapt and perform optimally to avoid performance bottlenecks that hinder effectiveness. When you design for scalability, you ensure that the AI infrastructure can handle growth and maintain responsiveness. Use scalable infrastructure, plan for capacity, and employ strategies like horizontal scaling and managed services. 

To design your AI and ML systems for scalability, consider the following recommendations. 

#### Plan for capacity and quotas

Assess future growth, and plan your infrastructure capacity and resource quotas accordingly. Work with business stakeholders to understand the projected growth and then define the infrastructure requirements accordingly. 

Use Cloud Monitoring (/monitoring/docs/monitoring-overview) to analyze historical resource utilization, identify trends, and project future needs. Conduct regular load testing to simulate workloads and identify bottlenecks. 

Familiarize yourself with Google Cloud quotas (/docs/quotas/view-manage) for the services that you use, such as Compute Engine, Agent Platform, and Cloud Storage. Proactively request quota increases through the Google Cloud console, and justify the increases with data from forecasting and load testing. Monitor quota usage (/monitoring/alerts/using-quota-metrics) and set up alerts to get notifications when the usage approaches the quota limits. 

To optimize resource usage based on demand, rightsize your resources, use Spot VMs (/kubernetes-engine/docs/concepts/spot-vms) for fault-tolerant batch workloads, and implement autoscaling. 

#### Prepare for peak events

Ensure that your system can handle sudden spikes in traffic or workload during peak events. Document your peak event strategy and conduct regular drills to test your system's ability to handle increased load. 

To aggressively scale up resources when the demand spikes, configure autoscaling policies in Compute Engine (/compute/docs/autoscaler) and GKE 

(/kubernetes-engine/docs/concepts/cluster-autoscaler). For predictable peak patterns, consider using predictive autoscaling (/compute/docs/autoscaler/predictive-autoscaling). To trigger autoscaling based on application-specific signals, use custom metrics in Cloud Monitoring. 

Distribute traffic across multiple application instances by using Cloud Load Balancing (/load-balancing/docs/load-balancing-overview). Choose an appropriate load balancer type based on your application's needs. For geographically distributed users, you can use global load balancing to route traffic to the nearest available instance. For complex microservices-based architectures, consider using Cloud Service Mesh (/service-mesh/docs/overview). 

Cache static content at the edge of Google's network by using Cloud CDN (/cdn/docs/overview). 

To cache frequently accessed data, use one of the following fully managed inmemory datastore services: 

- Memorystore for Valkey (/memorystore/docs/valkey/product-overview) 

- Memorystore for Redis (/memorystore/docs/redis/memorystore-for-redis-overview) 

- Memorystore for Redis Cluster 

- (/memorystore/docs/cluster/memorystore-for-redis-cluster-overview) 

Decouple the components of your system by using Pub/Sub (/pubsub/docs/overview) for real-time messaging and Cloud Tasks for asynchronous task execution 

#### Scale applications for production

To ensure scalable serving in production, you can use managed services like Agent Platform distributed training 

(/gemini-enterprise-agent-platform/machine-learning/training/distributed-training) and Gemini Enterprise Agent Platform Inference 

(/gemini-enterprise-agent-platform/machine-learning/predictions/overview). Agent Platform Inference lets you configure the machine types 

(/gemini-enterprise-agent-platform/machine-learning/predictions/configurecompute#machine-types) 

for your prediction nodes when you deploy a model to an endpoint or request batch predictions. For some configurations, you can add GPUs. Choose the appropriate machine type and accelerators to optimize latency, throughput, and cost. 

To scale complex AI and Python applications and custom workloads across distributed computing resources, you can use Ray on Gemini Enterprise Agent Platform (/gemini-enterprise-agent-platform/machine-learning/open-source/ray). This feature can help optimize performance and enables seamless integration with Google Cloud services. Ray on Gemini Enterprise Agent Platform simplifies distributed computing by handling cluster management, task scheduling, and data transfer. It integrates with other Agent Platform services like training, prediction, and pipelines. Ray provides fault tolerance and autoscaling, and helps you adapt the infrastructure to changing workloads. It offers a unified framework for distributed training, hyperparameter tuning, reinforcement learning, and model serving. Use Ray for distributed data preprocessing with Datafowl 

(/dataflow/docs/overview) or Managed Service for Apache Spark (/dataproc/docs/concepts/overview), accelerated model training, scalable hyperparameter tuning, reinforcement learning, and parallelized batch prediction. 

### Contributors

Authors: 

- Charlotte Gistelinck, PhD (https://www.linkedin.com/in/charlottegistelinck) | Partner Engineer 

- Sannya Dang (https://www.linkedin.com/in/thugiangdang) | AI Solution Architect 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

Other contributors: 

- Gary Harmson (https://www.linkedin.com/in/garyharmson) | Principal Architect 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

- Ryan Cox (https://www.linkedin.com/in/ryanlcox) | Principal Architect 

- Stef Ruinard (https://www.linkedin.com/in/stefruinard) | Generative AI Field Solutions Architect 

## AI and ML perspective: Security

This document in the Well-Architected Framework: AI and ML perspective (/architecture/framework/perspectives/ai-ml) provides an overview of principles and recommendations to ensure that your AI and ML deployments meet the security and compliance requirements of your organization. The recommendations in this document align with the security pillar (/architecture/framework/security) of the Google Cloud Well-Architected Framework. 

Secure deployment of AI and ML workloads is a critical requirement, particularly in enterprise environments. To meet this requirement, you need to adopt a holistic security approach that starts from the initial conceptualization of your AI and ML solutions and extends to development, deployment, and ongoing operations. Google Cloud offers robust tools and services that are designed to help secure your AI and ML workloads. 

The recommendations in this document are mapped to the following core principles: 

- Define clear goals and requirements (#define_clear_goals_and_requirements) 

- Keep data secure and prevent loss or mishandling (#keep_data_secure_and_prevent_loss_or_mishandling) 

- Keep AI pipelines secure and robust against tampering (#keep_ai_pipelines_secure_and_robust_against_tampering) 

- Deploy on secure systems with secure tools and artifacts (#deploy_on_secure_systems_with_secure_tools_and_artifacts) 

- Verify and protect inputs (#verify_and_protect_inputs) 

- Monitor, evaluate, and prepare to respond to outputs 

- (#monitor_evaluate_and_prepare_to_respond_to_outputs) 

For more information about AI security, you can also review the following resources: 

- Google Cloud's Secure AI Framework (SAIF) (https://safety.google/cybersecurity-advancements/saif/) provides a comprehensive guide for building secure and responsible AI systems. It outlines key principles and best practices for addressing security and compliance considerations throughout the AI lifecycle. 

- To learn more about Google Cloud's approach to trust in AI, see our compliance resource center (https://cloud.google.com/compliance). 

### Define clear goals and requirements

Effective AI and ML security is a core component of your overarching business strategy. It's easier to integrate the required security and compliance controls early in your design and development process, instead of adding controls after development. 

From the start of your design and development process, make decisions that are appropriate for your specific risk environment and your specific business priorities. For example, overly restrictive security measures might protect data but also impede innovation and slow down development cycles. However, a lack of security can lead to data breaches, reputational damage, and financial losses, which are detrimental to business goals. 

To define clear goals and requirements, consider the following recommendations. 

#### Align AI and ML security with business goals

To align your AI and ML security efforts with your business goals, use a strategic approach that integrates security into every stage of the AI lifecycle. To follow this approach, do the following: 

1. **Define clear business objectives and security requirements** : 

- **Identify key business goals** : Define clear business objectives that your AI and ML initiatives are designed to achieve. For example, your objectives might be to improve customer experience, optimize operations, or develop new products. 

- **Translate goals into security requirements** : When you clarify your business goals, define specific security requirements to support those goals. For example, your goal might be to use AI to personalize customer recommendations. To support that goal, your security requirements might be to protect customer data privacy and prevent unauthorized access to recommendation algorithms. 

2. **Balance security with business needs** : 

- **Conduct risk assessments** : Identify potential security threats and vulnerabilities in your AI systems. 

- **Prioritize security measures** : Base the priority of these security measures upon their potential impact on your business goals. 

- **Analyze the costs and benefits** : Ensure that you invest in the most effective solutions. Consider the costs and benefits of different security measures. 

- **Shift left on security** : Implement security best practices early in the design phase, and adapt your safety measures as business needs change and threats emerge. 

#### Identify potential attack vectors and risks

Consider potential attack vectors that could affect your AI systems, such as data poisoning, model inversion, or adversarial attacks. Continuously monitor and assess the evolving attack surface as your AI system develops, and keep track of new threats and vulnerabilities. Remember that changes in your AI systems can also introduce changes to their attack surface. 

To mitigate potential legal and reputational risks, you also need to address compliance requirements related to data privacy, algorithmic bias, and other relevant regulations. 

To anticipate potential threats and vulnerabilities early and make design choices that mitigate risks, adopt a _secure by design_ approach. 

Google Cloud provides a comprehensive suite of tools and services to help you implement a secure by design approach: 

**Cloud posture management** 

(/security-command-center/docs/security-command-center-overview): Use Security Command Center to identify potential vulnerabilities and misconfigurations in your AI infrastructure. 

**Attack exposure scores and attack paths** 

(/security-command-center/docs/attack-exposure-learn): Refine and use the attack exposure scores and attack paths that Security Command Center generates. 

**Google Threat Intelligence** 

(https://cloud.google.com/security/products/threat-intelligence): Stay informed about new threats and attack techniques that emerge to target AI systems. 

**Logging and Monitoring** (/stackdriver/docs): Track the performance and security of your AI systems, and detect any anomalies or suspicious activities. Conduct regular security audits to identify and address potential vulnerabilities in your AI infrastructure and models. 

**Vulnerability management** 

(https://cloud.google.com/security/resources/datasheets/consulting-services-threat-andvulnerability-management) 

: Implement a vulnerability management process to track and remediate security vulnerabilities in your AI systems. 

For more information, see Secure by Design at Google 

(https://research.google/pubs/secure-by-design-at-google/) and Implement security by design (/architecture/framework/security/implement-security-by-design). 

### Keep data secure and prevent loss or mishandling

Data is a valuable and sensitive asset that must be kept secure. Data security helps you to maintain user trust, support your business objectives, and meet your compliance requirements. 

To help keep your data secure, consider the following recommendations. 

#### Adhere to data minimization principles

To ensure data privacy, adhere to the principle of data minimization. To minimize data, don't collect, keep, or use data that's not strictly necessary for your business goals. Where possible, use synthetic or fully anonymized data. 

Data collection can help drive business insights and analytics, but it's crucial to exercise discretion in the data collection process. If you collect personally identifiable information (PII) about your customer, reveal sensitive information, or create bias or controversy, then you might build biased ML models. 

You can use Google Cloud features to help you improve data minimization and data privacy for various use cases: 

- To de-identify your data and also preserve its utility, apply transformation methods like pseudonymization, de-identification, and generalization such as bucketing. To implement these methods, you can use Sensitive Data Protection (/architecture/de-identification-re-identification-pii-using-cloud-dlp). 

- To enrich data and mitigate potential bias, you can use an Agent Platform data labeling job 

- (/gemini-enterprise-agent-platform/machine-learning/datasets/label-using-console). The data labeling process adds informative and meaningful tags to raw data, which transforms it into structured training data for ML models. Data labeling adds specificity to the data and reduces ambiguity. 

- To help protect resources from prolonged access or manipulation, use Cloud Storage features to control data lifecycles (/storage/docs/control-data-lifecycles). 

For best practices about how to implement data encryption, see data encryption at rest and in transit 

(/architecture/framework/security/implement-security-bydesign#encrypt_data_at_rest_and_in_transit) in the Well-Architected Framework. 

#### Monitor data collection, storage, and transformation

Your AI application's training data poses the largest risks for the introduction of bias and data leakage. To stay compliant and manage data across different teams, establish a data governance layer to monitor data flows, transformations, and access. Maintain logs for data access and manipulation activities. The logs help you audit data access, detect unauthorized access attempts, and prevent unwanted access. 

You can use Google Cloud features to help you implement data governance strategies: 

- To establish an organization-wide or department-wide data governance platform, use Knowledge Catalog (/dataplex/docs). A data governance platform can help you to centrally discover, manage, monitor, and govern data and AI artifacts across your data platforms. The data governance platform also provides access to trusted users. You can perform the following tasks with Knowledge Catalog: 

   - Manage data lineage. BigQuery can also provide column-level lineage. 

   - Manage data quality checks and data profiles. 

   - Manage data discovery, exploration, and processing across different data marts. 

   - Manage feature metadata and model artifacts. 

   - Create a business glossary to manage metadata and establish a standardized vocabulary. 

   - Enrich the metadata (/dataplex/docs/enrich-entries-metadata) with context through aspects and aspect types. 

   - Unify data governance across BigLake and open-format tables like Iceberg and Delta. 

   - Build a data mesh (/architecture/data-mesh) to decentralize data ownership among data owners from different teams or domains. This practice adheres to data security principles and it can help improve data accessibility and operational efficiency. 

   - Inspect and send sensitive data results 

   - (/sensitive-data-protection/docs/add-aspects-inspection-job) from BigQuery to Knowledge Catalog. 

- To build a unified open lakehouse 

- (https://cloud.google.com/discover/what-is-a-data-lakehouse) that is well-governed, integrate your data lakes and warehouses with managed metastore services like Dataproc Metastore (/dataproc-metastore/docs/overview) and Lakehouse runtime catalog (/biglake/docs/about-blms). An open lakehouse uses open table formats that are compatible with different data processing engines. 

- To schedule the monitoring of features and feature groups, use Agent Platform Feature Store 

(/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/monitorfeatures#create-feature-monitor) 

- To scan your Agent Platform datasets at the organization, folder, or project level, use Sensitive data discovery for Agent Platform 

- (/sensitive-data-protection/docs/data-profiles). You can also analyze the data profiles (/sensitive-data-protection/docs/analyze-data-profiles) that are stored in BigQuery. 

- To capture real-time logs and collect metrics related to data pipelines, use Cloud Logging (/logging/docs/view/streaming-live-tailing) and Cloud Monitoring (/logging/docs/alerting/monitoring-logs). To collect audit trails of API calls, use Cloud Audit Logs (/logging/docs/audit). Don't log PII or confidential data in experiments or in different log servers. 

#### Implement role-based access controls with least privilege principles

Implement role-based access controls (RBAC) to assign different levels of access based on user roles. Users must have only the minimum permissions that are necessary to let them perform their role activities. Assign permissions based on the principle of least privilege (/iam/docs/using-iam-securely#least_privilege) so that users have only the access that they need, such as no-access, read-only, or write. 

RBAC with least privilege is important for security when your organization uses sensitive data that resides in data lakes, in feature stores, or in hyperparameters for model training. This practice helps you to prevent data theft, preserve model integrity, and limit the surface area for accidents or attacks. 

To help you implement these access strategies, you can use the following Google Cloud features: 

- To implement access granularity, consider the following options: 

   - Map the IAM roles of different products to a user, group, or service account to allow granular access. Map these roles based on your project needs, access patterns, or tags (/resource-manager/docs/tags/tags-overview). 

   - Set IAM policies with conditions (/iam/docs/conditions-overview) to manage granular access to your data, model, and model configurations, such as code, resource settings, and hyperparameters. 

   - Explore application-level granular access that helps you secure sensitive data that you audit and share outside of your team. 

      - **Cloud Storage** : Set IAM policies on buckets and managed folders (/storage/docs/access-control/iam). 

      - **BigQuery** : Use IAM roles and permissions (/bigquery/docs/access-control) for datasets and resources within datasets. Also, restrict access at the row-level 

      - (/bigquery/docs/managing-row-level-security) and column-level 

      - (/bigquery/docs/column-level-security-intro) in BigQuery. 

- To limit access to certain resources, you can use principal access boundary (PAB) policies (/iam/docs/principal-access-boundary-policies-create). You can also use Privileged Access Manager (/iam/docs/temporary-elevated-access) to control justin-time, temporary privilege elevation for select principals. Later, you can view the audit logs for this Privileged Access Manager activity. 

- To restrict access to resources based on the IP address and end user device attributes, you can extend Identity-Aware Proxy (IAP) access policies (/iap/docs/cloud-iap-context-aware-access-howto). 

- To create access patterns for different user groups, you can use Agent Platform access control with IAM 

- (/gemini-enterprise-agent-platform/machine-learning/general/access-control) to combine the predefined or custom roles. 

- To protect Gemini Enterprise Agent Platform Workbench instances by using context-aware access controls, use Access Context Manager 

(/access-context-manager/docs) and Chrome Enterprise Premium 

(/chrome-enterprise-premium/docs/access-levels). With this approach, access is evaluated each time a user authenticates to the instance. 

#### Implement security measures for data movement

Implement secure perimeters and other measures like encryption and restrictions on data movement. These measures help you to prevent data exfiltration and data loss, which can cause financial losses, reputational damage, legal liabilities, and a disruption to business operations. 

To help prevent data exfiltration and loss on Google Cloud, you can use a combination of security tools and services. 

To implement encryption, consider the following: 

- To gain more control over encryption keys, use customer-managed encryption keys (CMEKs) in Cloud KMS. When you use CMEKs, the following CMEKintegrated services encrypt data at rest for you: 

Agent Platform 

   - (/gemini-enterprise-agent-platform/machine-learning/general/cmek) 

   - Cloud Storage (/storage/docs/encryption/customer-managed-keys) 

   - Cloud SQL (/sql/docs/sqlserver/cmek) 

   - Spanner (/spanner/docs/cmek) 

   - BigQuery (/bigquery/docs/customer-managed-encryption) 

- To help protect your data in Cloud Storage, use server-side encryption to store your CMEKs. If you manage CMEKs on your own servers, server-side encryption can help protect your CMEKs and associated data, even if your CMEK storage system is compromised. 

- To encrypt data in transit, use HTTPS for all of your API calls to AI and ML services. To enforce HTTPS for your applications and APIs, use HTTPS load balancers (/load-balancing/docs/https). 

For more best practices about how to encrypt data, see Encrypt data at rest and in transit 

(/architecture/framework/security/implement-security-bydesign#encrypt_data_at_rest_and_in_transit) 

in the security pillar of the Well-Architected Framework. 

To implement perimeters, consider the following: 

- To create a security boundary around your AI and ML resources and prevent data exfiltration from your Virtual Private Cloud (VPC), use VPC Service Controls 

- (/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls) to define a service perimeter. Include your AI and ML resources and sensitive data in the perimeter. To control data flow, configure ingress and egress rules for your perimeter. 

- To restrict inbound and outbound traffic to your AI and ML resources, configure firewall rules (/firewall/docs/firewall-policies-overview). Implement policies that deny all traffic by default and explicitly allow only the traffic that meets your criteria. For a policy example, see Example: Deny all external connections except to specific ports 

- (/firewall/docs/network-firewall-policy-examples#deny-all-external-connections-exceptto-specific-ports) 

To implement restrictions on data movement, consider the following: 

- To share data and to scale across privacy boundaries in a secure environment, use BigQuery sharing (/bigquery/docs/analytics-hub-introduction) and BigQuery data clean rooms (/bigquery/docs/data-clean-rooms), which provide a robust security and privacy framework. 

- To share data directly into built-in destinations from business intelligence dashboards, use Looker Action Hub (/looker/docs/action-hub), which provides a secure cloud environment. 

#### Guard against data poisoning

_Data poisoning_ is a type of cyberattack in which attackers inject malicious data into training datasets to manipulate model behavior or to degrade performance. This cyberattack can be a serious threat to ML training systems. To protect the validity and quality of the data, maintain practices that guard your data. This 

approach is crucial for consistent unbiasedness, reliability, and integrity of your model. 

To track inconsistent behavior, transformation, or unexpected access to your data, set up comprehensive monitoring and alerting 

- (#monitor-data-collection-storage-and-transformation) for data pipelines and ML 

- pipelines. 

Google Cloud features can help you implement more protections against data poisoning: 

- To validate data integrity, consider the following: 

   - Implement robust data validation checks before you use the data for training. Verify data formats, ranges, and distributions. You can use the automatic data quality capabilities in Knowledge Catalog 

   - (/dataplex/docs/auto-data-quality-overview). 

   - Use Sensitive Data Protection with Model Armor to take advantage of comprehensive data loss prevention capabilities. For more information, see Model Armor key concepts 

   - (/security-command-center/docs/key-concepts-model-armor). Sensitive Data Protection with Model Armor lets you discover, classify, and protect sensitive data such as intellectual property. These capabilities can help you prevent the unauthorized exposure of sensitive data in LLM interactions. 

   - To detect anomalies in your training data that might indicate data poisoning, use anomaly detection in BigQuery 

   - (/bigquery/docs/anomaly-detection-overview) with statistical methods or ML models. 

- To prepare for robust training, do the following: 

   - Employ ensemble methods (https://en.wikipedia.org/wiki/Ensemble_learning) to reduce the impact of poisoned data points. Train multiple models on different subsets of the data with hyperparameter tuning 

   - (/gemini-enterprise-agent-platform/machine-learning/training/hyperparametertuning-overview) 

   - Use data augmentation techniques to balance the distribution of data across datasets. This approach can reduce the impact of data poisoning and lets you add adversarial examples. 

- To incorporate human review for training data or model outputs, do the following: 

   - Analyze model evaluation metrics to detect potential biases, anomalies, or unexpected behavior that might indicate data poisoning. For details, see Model evaluation in Agent Platform 

   - (/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction). 

   - Take advantage of domain expertise to evaluate the model or application and identify suspicious patterns or data points that automated methods might not detect. For details, see Gen AI evaluation service overview (/gemini-enterprise-agent-platform/models/evaluation-overview). 

For best practices about how to create data platforms that focus on infrastructure and data security, see the Implement security by design 

(/architecture/framework/security/data-security) principle in the Well-Architected Framework. 

### Keep AI pipelines secure and robust against tampering

Your AI and ML code and the code-defined pipelines are critical assets. Code that isn't secured can be tampered with, which can lead to data leaks, compliance failure, and disruption of critical business activities. Keeping your AI and ML code secure helps to ensure the integrity and value of your models and model outputs. 

To keep AI code and pipelines secure, consider the following recommendations. 

#### Use secure coding practices

To prevent vulnerabilities, use secure coding practices when you develop your models. We recommend that you implement AI-specific input and output validation, manage all of your software dependencies, and consistently embed secure coding principles into your development. Embed security into every stage of the AI lifecycle, from data preprocessing to your final application code. 

To implement rigorous validation, consider the following: 

- To prevent model manipulation or system exploits, validate and sanitize inputs and outputs in your code. 

   - Use Model Armor or fine-tuned LLMs to automatically screen prompts and responses for common risks. 

   - Implement data validation within your data ingestion and preprocessing scripts for data types, formats, and ranges. For Gemini Enterprise Agent Platform Pipelines 

   - (/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) or BigQuery, you can use Python to implement this data validation. 

   - Use coding assistant LLM agents, like CodeMender 

   - (https://cloud.google.com/security/codemender), to improve code security. Keep a human in the loop to validate its proposed changes. 

- To manage and secure your AI model API endpoints, use Apigee (/apigee/docs/api-platform/get-started/what-apigee), which includes configurable features like request validation, traffic control, and authentication. 

- To help mitigate risk throughout the AI lifecycle, you can use AI Protection (/security-command-center/docs/ai-protection-overview) to do the following: 

   - Discover AI inventory in your environment. 

   - Assess the inventory for potential vulnerabilities. 

   - Secure AI assets with controls, policies, and protections. 

   - Manage AI systems with detection, investigation, and response capabilities. 

To help secure the code and artifact dependencies in your CI/CD pipeline, consider the following: 

- To address the risks that open-source library dependencies can introduce to your project, use Artifact Analysis (/artifact-analysis/docs/artifact-analysis) with Artifact Registry (/artifact-registry/docs) to detect known vulnerabilities. Use and maintain the approved versions of libraries. Store your custom ML packages and vetted dependencies in a private Artifact Registry repository. 

- To embed dependency scanning into your Cloud Build MLOps pipelines, use Binary Authorization (/build/docs/securing-builds/secure-deployments-to-run-gke). Enforce policies that allow deployments only if your code's container images pass the security checks. 

- To get security information about your software supply chain, use dashboards (/monitoring/dashboards) in the Google Cloud console that provide details about sources, builds, artifacts, deployments, and runtimes. This information includes vulnerabilities in build artifacts, build provenance, and Software Bill of Materials (SBOM) dependency lists. 

- To assess the maturity level of your software supply chain security, use the Supply chain Levels for Software Artifacts (SLSA) framework (https://slsa.dev/spec/v1.0/levels). 

To consistently embed secure coding principles into every stage of development, consider the following: 

- To prevent the exposure of sensitive data from model interactions, use Logging with Sensitive Data Protection. When you use these products together, you can control what data your AI applications and pipeline components log, and hide sensitive data. 

- To implement the principle of least privilege, ensure that the service accounts that you use for your Agent Platform custom jobs, pipelines, and deployed models have only the minimum required IAM permissions. For more information, see Implement role-based access controls with least privilege principles (#implement_role_based_access_controls_with_least_privilege_principles). 

- To help secure and protect your pipelines and build artifacts, understand the security configurations (VPC and VPC Service Controls) in the environment your code runs in. 

#### Protect pipelines and model artifacts from unauthorized access

Your model artifacts and pipelines are intellectual property, and their training data also contains proprietary information. To protect model weights, files, and deployment configurations from tampering and vulnerabilities, store and access these artifacts with improved security. Implement different access levels for each artifact based on user roles and needs. 

To help secure your model artifacts, consider the following: 

- To protect model artifacts and other sensitive files, encrypt them with Cloud KMS. This encryption helps to protect data at rest and in transit, even if the underlying storage becomes compromised. 

- To help secure access to your files, store them in Cloud Storage and configure access controls. 

- To track any incorrect or inadequate configurations and any drift from your defined standards, use Security Command Center to configure security postures (/security-command-center/docs/security-posture-overview). 

- To enable fine-grained access control and encryption at rest, store your model artifacts in Model Registry on Gemini Enterprise Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction). For additional security, create a digital signature for packages and containers that are produced during the approved build processes. 

- To benefit from Google Cloud's enterprise-grade security, use models that are available in Model Garden. Model Garden provides Google's proprietary models and it offers third-party models 

- (/gemini-enterprise-agent-platform/models/model-garden/exploremodels#model_security_scanning) 

- from featured partners. 

- To enforce central management for all user and group lifecycles and to enforce the principle of least privilege, use IAM. 

   - Create and use dedicated, least-privilege service accounts for your MLOps pipelines. For example, a training pipeline's service account has the permissions to read data from only a specific Cloud Storage bucket and to write model artifacts to Model Registry. 

   - Use IAM Conditions to enforce conditional, attribute-based access control. For example, a condition allows a service account to trigger a Agent Platform pipeline only if the request originates from a trusted Cloud Build trigger. 

To help secure your deployment pipelines, consider the following: 

- To manage MLOps stages on Google Cloud services and resources, use Agent Platform Pipelines, which can integrate with other services and provide lowlevel access control. When you re-execute the pipelines, ensure that you perform explainability evaluations (such as feature attributions) and responsible AI (/gemini-enterprise-agent-platform/models/responsible-ai) checks before you deploy the model artifacts. These checks can help you detect or prevent the following security issues: 

   - Unauthorized changes, which can indicate model tampering. 

   - Cross-site scripting (XSS), which can indicate compromised container images or dependencies. 

   - Insecure endpoints, which can indicate misconfigured serving infrastructure. 

- To help secure model interactions during inference, use private endpoints based on Private Service Connect 

- (/gemini-enterprise-agent-platform/machine-learning/predictions/private-serviceconnect) 

with prebuilt containers 

- (/gemini-enterprise-agent-platform/machine-learning/predictions/pre-built-containers) or custom containers 

- (/gemini-enterprise-agent-platform/machine-learning/predictions/use-custom-container). Create model signatures with a predefined input and output schema. 

- To automate code change tracking, use Git for source code management, and integrate version control with robust CI/CD pipelines. 

For more information, see Secure AI Framework (SAIF) 

(https://cloud.google.com/use-cases/secure-ai-framework). 

#### Enforce lineage and tracking

To help meet the regulatory compliance requirements that you might have, enforce lineage and tracking of your AI and ML assets. Data lineage and tracking provides extensive change records for data, models, and code. Model provenance provides transparency and accountability throughout the AI and ML lifecycle. 

To effectively enforce lineage and tracking in Google Cloud, consider the following tools and services: 

- To track the lineage of models, datasets, and artifacts that are automatically encrypted at rest, use Agent Platform ML Metadata 

- (/gemini-enterprise-agent-platform/machine-learning/mlmetadata/introduction#ml_artifact_lineage) 

- . Log metadata about data sources, transformations, model parameters, and experiment results. 

- To track the lineage of pipeline artifacts 

- (/gemini-enterprise-agent-platform/machine-learning/pipelines/lineage) from Agent Platform Pipelines, and to search for model and dataset resources, you can use Knowledge Catalog. Track individual pipeline artifacts when you want to perform debugging, troubleshooting, or a root cause analysis. To track your entire MLOps pipeline, which includes the lineage of pipeline artifacts, use Agent Platform ML Metadata 

- (/gemini-enterprise-agent-platform/machine-learning/ml-metadata/analyzing). Agent Platform ML Metadata also lets you analyze the resources and runs. Model Registry applies and manages the versions of each model that you store. 

- To track API calls and administrative actions, enable audit logs for Agent Platform (/gemini-enterprise-agent-platform/machine-learning/general/audit-logging). Analyze audit logs (/logging/docs/analyze/query-and-view) with Observability Analytics to understand who accessed or modified data and models, and when. You can also route logs to third-party destinations 

- (/logging/docs/export/pubsub#integrate-thru-pubsub). 

### Deploy on secure systems with secure tools and artifacts

Ensure that your code and models run in a secure environment. This environment must have a robust access control system and provide security assurances for the tools and artifacts that you deploy. 

To deploy your code on secure systems, consider the following recommendations. 

#### Train and deploy models in a secure environment

To maintain system integrity, confidentiality, and availability for your AI and ML systems, implement stringent access controls that prevent unauthorized resource manipulation. This defense helps you to do the following: 

- Mitigate model tampering that could produce unexpected or conflicting results. 

- Protect your training data from privacy violations. 

- Maintain service uptime. 

- Maintain regulatory compliance. 

- Build user trust. 

To train your ML models in an environment with improved security, use managed services in Google Cloud like Cloud Run, GKE, and Managed Service for Apache Spark. You can also use Agent Platform serverless training 

- (/gemini-enterprise-agent-platform/machine-learning/training/overview). 

This section provides recommendations to help you further help secure your training and deployment environment. 

To help secure your environment and perimeters, consider the following: 

- When you implement security measures 

- (#implement_security_measures_for_data_movement), as described earlier, consider the following: 

   - To isolate training environments and limit access, use dedicated projects or VPCs (/architecture/best-practices-vpc-design) for training. 

   - To protect sensitive data and code during execution, use Shielded VMs (/compute/shielded-vm/docs/shielded-vm) or confidential computing (/confidential-computing/confidential-vm/docs/confidential-vm-overview) for training workloads. 

   - To help secure your network infrastructure and to control access to your deployed models, use VPCs, firewalls, and security perimeters. 

- When you use Gemini Enterprise Agent Platform Managed Training, you can use the following methods to help secure your compute infrastructure: 

      - To train custom jobs that privately communicate with other authorized Google Cloud services and that aren't exposed to public traffic, set up a Private Service Connect interface 

      - (/gemini-enterprise-agent-platform/machine-learning/general/vpc-psc-i-setup). 

      - For increased network security and lower network latency than what you get with a public IP address, use a private IP address to connect to your training jobs. For details, see Use a private IP for custom training (/gemini-enterprise-agent-platform/machine-learning/training/using-private-ip). 

   - When you use GKE or Cloud Run to set up a custom environment, consider the following options: 

      - To secure your GKE cluster, use the appropriate network policies, pod security policies, and access controls. Use trusted and verified container images (/kubernetes-engine/docs/how-to/hardening-your-cluster#containerd) for your training workloads. To scan container images 

      - (/artifact-analysis/docs/scan-os-automatically) for vulnerabilities, use Artifact Analysis. 

      - To protect your environment from container escapes 

      - (/security-command-center/docs/findings/threats/agent-engine-container-escape) and other attacks, implement runtime security measures 

      - (/functions/docs/securing/execution-environment-security) for Cloud Run functions. To further protect your environment, use GKE Sandbox (/kubernetes-engine/docs/concepts/sandbox-pods) and workload isolation (/kubernetes-engine/docs/how-to/workload-separation). 

      - To help secure your GKE workloads, follow the best practices in the GKE security overview (/kubernetes-engine/docs/concepts/security-overview). 

      - To help meet your security requirements in Cloud Run, see the security design overview} (/run/docs/securing/security). 

   - When you use Managed Service for Apache Spark for model training, follow the Managed Service for Apache Spark security best practices (/dataproc/docs/concepts/security-best-practices). 

- To help secure your deployment, consider the following: 

   - When you deploy models, use Model Registry. If you deploy models in containers, use GKE Sandbox and Container-Optimized OS 

(/container-optimized-os/docs) to enhance security and isolate workloads. Restrict access to models 

- (/gemini-enterprise-agent-platform/models/control-model-access) from Model Garden according to user roles and responsibilities. 

- To help secure your model APIs, use Apigee or API Gateway (/api-gateway/docs). To prevent abuse, implement API keys, authentication, authorization, and rate limiting. To control access to model APIs, use API keys and authentication mechanisms. 

- To help secure access to models during prediction, use Gemini Enterprise Agent Platform Inference 

- (/gemini-enterprise-agent-platform/machine-learning/predictions/overview). To prevent data exfiltration, use VPC Service Controls perimeters to protect private endpoints 

- (/gemini-enterprise-agent-platform/machine-learning/predictions/using-privateendpoints) 

and govern access to the underlying models. You use private endpoints to enable access to the models within a VPC network. IAM isn't directly applied (/gemini-enterprise-agent-platform/machine-learning/general/endpoint-access-control) to the private endpoint, but the target service uses IAM to manage access to the models. For online prediction, we recommend that you use Private Service Connect. 

- To track API calls that are related to model deployment, enable Cloud Audit Logs for Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/general/audit-logging). Relevant API calls include activities such as endpoint creation, model deployment, and configuration updates. 

- To extend Google Cloud infrastructure to edge locations, consider Google Distributed Cloud (/distributed-cloud/docs/overview) solutions. For a fully disconnected solution, you can use Distributed Cloud air-gapped 

- (/distributed-cloud/hosted/docs/latest/gdch/overview), which doesn't require connectivity to Google Cloud. 

- To help standardize deployments and to help ensure compliance with regulatory and security needs, use Assured Workloads (/assured-workloads/docs/overview). 

#### Follow SLSA guidelines for AI artifacts

Follow the standard Supply-chain Levels for Software Artifacts (SLSA) (https://slsa.dev/) guidelines for your AI-specific artifacts, like models and software packages. 

SLSA is a security framework that's designed to help you improve the integrity of software artifacts and help prevent tampering. When you adhere to the SLSA guidelines, you can enhance the security of your AI and ML pipeline and the artifacts that the pipeline produces. SLSA adherence can provide the following benefits: 

**Increased trust in your AI and ML artifacts** : SLSA helps to ensure that tampering doesn't occur to your models and software packages. Users can also trace models and software packages back to their source, which increases users' confidence in the integrity and reliability of the artifacts. 

- **Reduced risk of supply chain attacks** : SLSA helps to mitigate the risk of attacks that exploit vulnerabilities in the software supply chain, like attacks that inject malicious code or that compromise build processes. 

- **Enhanced security posture** : SLSA helps you to strengthen the overall security posture of your AI and ML systems. This implementation can help reduce the risk of attacks and protect your valuable assets. 

To implement SLSA for your AI and ML artifacts on Google Cloud, do the following: 

1. **Understand SLSA levels** : Familiarize yourself with the different SLSA levels (https://slsa.dev/spec/v1.0/levels) and their requirements. As the levels increase, the integrity that they provide also increases. 

2. **Assess your current level** : Evaluate your current practices against the SLSA framework to determine your current level and to identify areas for improvement. 

3. **Set your target level** : Determine the appropriate SLSA level to target based on your risk tolerance, security requirements, and the criticality of your AI and ML systems. 

4. **Implement SLSA requirements** : To meet your target SLSA level, implement the necessary controls and practices 

   - (/software-supply-chain-security/docs/overview), which could include the following: 

   - **Source control** : Use a version control system like Git to track changes to your code and configurations. 

   - **Build process** : Use a service that helps to secure your builds, like Cloud Build (/build), and ensure that your build process is scripted or automated. 

   - **Provenance generation** : Generate provenance metadata that captures details about how your artifacts were built, including the build process, source code, and dependencies. For details, see Track metadata 

   - (/gemini-enterprise-agent-platform/machine-learning/ml-metadata/tracking) and Track executions and artifacts 

   - (/gemini-enterprise-agent-platform/machine-learning/experiments/trackexecutions-artifacts) 

   - **Artifact signing** : Sign your artifacts to verify their authenticity and integrity. 

   - **Vulnerability management** : Scan your artifacts and dependencies for vulnerabilities on a regular basis. Use tools like Artifact Analysis. (/artifact-registry/docs/analysis) 

   - **Deployment security** : Implement deployment practices that help to secure your systems, such as the practices that are described in this document. 

5. **Continuous improvement** : Monitor and improve your SLSA implementation to address new threats and vulnerabilities, and strive for higher SLSA levels. 

#### Use validated prebuilt container images

To prevent a single point of failure for your MLOps stages, isolate the tasks that require different dependency management into different containers. For example, use separate containers for feature engineering, training or fine-tuning, and inference tasks. This approach also gives ML engineers the flexibility to control and customize their environment. 

To promote MLOps consistency across your organization, use prebuilt containers. Maintain a central repository of verified and trusted base platform images with the following best practices: 

- Maintain a centralized platform team in your organization that builds and manages standardized base containers. 

- Extend the prebuilt container images that Agent Platform provides specifically for AI and ML. Manage the container images in a central repository within your organization. 

Agent Platform provides a variety of prebuilt containers 

(/gemini-enterprise-agent-platform/machine-learning/training/pre-built-containers) for training and inference, and it also lets you use custom containers 

(/gemini-enterprise-agent-platform/machine-learning/training/containers-overview). For smaller models, you can reduce latency for inference if you load models in containers (/run/docs/configuring/services/gpu-best-practices#model-container). 

To improve the security of your container management, consider the following recommendations: 

- Use Artifact Registry (/artifact-registry/docs) to create, store, and manage repositories of container images with different formats. Artifact Registry handles access control with IAM, and it has integrated observability and vulnerability assessment 

- (/security-command-center/docs/concepts-security-sources#ar-vuln-assessment) features. Artifact Registry lets you enable container security features, scan container images, and investigate vulnerabilities. 

- Run continuous integration 

- (/architecture/app-development-and-delivery-with-cloud-code-gcb-cd-and-gke) steps and build container images (/build/docs/building/build-containers) with Cloud Build. Dependency issues can be highlighted at this stage. If you want to deploy only the images that are built by Cloud Build, you can use Binary Authorization (/binary-authorization/docs/cloud-build). To help prevent supply chain attacks, deploy the images built by Cloud Build in Artifact Registry. Integrate automated testing tools such as SonarQube, PyLint, or OWASP ZAP. 

- Use a container platform like GKE or Cloud Run, which are optimized for GPU or TPU for AI and ML workloads. Consider the vulnerability scanning options 

- (/artifact-analysis/docs/container-scanning-overview) for containers in GKE clusters. 

#### Consider Confidential Computing for GPUs

To protect _data in use_ (https://en.wikipedia.org/wiki/Digital_data#Data_in_use), you can use Confidential Computing. Conventional security measures protect data at rest and in transit, but Confidential Computing encrypts data during processing. When you use Confidential Computing for GPUs, you help to protect sensitive training data and model parameters from unauthorized access. You can also help to prevent unauthorized access from privileged cloud users or potential attackers who might gain access to the underlying infrastructure. 

To determine whether you need Confidential Computing for GPUs, consider the sensitivity of the data, regulatory requirements, and potential risks. 

If you set up Confidential Computing, consider the following options: 

- For general-purpose AI and ML workloads, use Confidential VM instances (/confidential-computing/confidential-vm/docs/confidential-vm-overview) with NVIDIA T4 GPUs. These VM instances offer hardware-based encryption of data in use. 

- For containerized workloads, use Confidential GKE Nodes 

- (/kubernetes-engine/docs/how-to/gpus-confidential-nodes). These nodes provide a secure and isolated environment for your pods. 

- To ensure that your workload is running in a genuine and secure enclave, verify the attestation (/confidential-computing/confidential-vm/docs/attestation) reports that Confidential VM provides. 

- To track performance, resource utilization, and security events, monitor your Confidential Computing resources and your Confidential GKE Nodes by using Monitoring and Logging.
