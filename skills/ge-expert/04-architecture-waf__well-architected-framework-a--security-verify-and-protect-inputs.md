# Architecture: Well-Architected Framework and reference designs / Well-Architected Framework: AI and ML perspective: AI and ML perspective: Security: Verify and protect inputs to AI and ML perspective: Reliability: Maintain trust and control through data and model governance
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 273-312, extracted 2026-10-18

## Well-Architected Framework: AI and ML perspective

URL: https://docs.cloud.google.com/architecture/framework/perspectives/ai-ml/printable

### Verify and protect inputs

Treat all of the inputs to your AI systems as untrusted, regardless of whether the inputs are from end users or other automated systems. To help keep your AI systems secure and to ensure that they operate as intended, you must detect and sanitize potential attack vectors early. 

To verify and protect your inputs, consider the following recommendations. 

#### Implement practices that help secure generative AI systems

Treat prompts as a critical application component that has the same importance to security as code does. Implement a defense-in-depth 

(https://en.wikipedia.org/wiki/Defense_in_depth_(computing)) strategy that combines proactive design, automated screening, and disciplined lifecycle management. 

To help secure your generative AI prompts, you must design them for security, screen them before use, and manage them throughout their lifecycle. 

To improve the security of your prompt design and engineering, consider the following practices: 

**Structure prompts for clarity** : Design and test all of your prompts by using Agent Studio on Gemini Enterprise Agent Platform prompt management capabilities (/gemini-enterprise-agent-platform/reference/models/prompt-classes). Prompts need to have a clear, unambiguous structure. Define a role, include few-shot examples 

(/gemini-enterprise-agent-platform/models/prompts/few-shot-examples), and give specific, bounded instructions. These methods reduce the risk that the model might misinterpret a user's input in a way that creates a security loophole. 

- **Test the inputs for robustness and grounding** : Test all of your systems proactively against unexpected, malformed, and malicious inputs in order to prevent crashes or insecure outputs. Use red team testing to simulate realworld attacks. As a standard step in your Agent Platform Pipelines, automate your robustness tests. You can use the following testing techniques: 

   - Fuzz testing. 

   - Test directly against PII, sensitive inputs, and SQL injections. 

   - Scan multimodal inputs that can contain malware or violate prompt policies. 

- **Implement a layered defense** : Use multiple defenses and never rely on a single defensive measure. For example, for an application based on retrievalaugmented generation (RAG), use a separate LLM to classify incoming user intent and check for malicious patterns. Then, that LLM can pass the request to the more-powerful primary LLM that generates the final response. 

- **Sanitize and validate inputs** : Before you incorporate external input or userprovided input into a prompt, filter and validate all of the input in your 

application code. This validation is important to help you prevent indirect prompt injection. 

- For automated prompt and response screening, consider the following practices: 

   - **Use comprehensive security services** : Implement a dedicated, modelagnostic security service like Model Armor as a mandatory protection layer for your LLMs. Model Armor inspects prompts and responses for threats like prompt injection, jailbreak attempts 

   - (https://en.wikipedia.org/wiki/Privilege_escalation#Jailbreaking), and harmful content. To help ensure that your models don't leak sensitive training data or intellectual property in their responses, use the Sensitive Data Protection integration with Model Armor. For details, see Model Armor filters 

(/security-command-center/docs/model-armor-overview#ma-filters). 

   - **Monitor and log interactions** : Maintain detailed logs for all of the prompts and responses for your model endpoints. Use Logging (/logging) to audit these interactions, identify patterns of misuse, and detect attack vectors that might emerge against your deployed models. 

- To help secure prompt lifecycle management, consider the following practices: 

   - **Implement versioning for prompts** : Treat all of your production prompts like application code. Use a version control system like Git to create a complete history of changes, enforce collaboration standards, and enable rollbacks to previous versions. This core MLOps practice can help you to maintain stable and secure AI systems. 

   - **Centralize prompt management** : Use a central repository to store, manage, and deploy all of your versioned prompts. This strategy enforces consistency across environments and it enables runtime updates without the need for a full application redeployment. 

   - **Conduct regular audits and red team testing** : Test your system's defenses continuously against known vulnerabilities, such as those listed in the OWASP Top 10 for LLM Applications 

   - (https://owasp.org/www-project-top-10-for-large-language-model-applications/). As an AI engineer, you must be proactive and red-team test your own application to discover and remediate weaknesses before an attacker can exploit them. 

#### Prevent malicious queries to your AI systems

Along with authentication and authorization, which this document discussed earlier, you can take further measures to help secure your AI systems against malicious inputs. You need to prepare your AI systems for _post-authentication_ scenarios in which attackers bypass both the authentication and authorization protocols, and then attempt to attack the system internally. 

To implement a comprehensive strategy that can help protect your system from post-authentication attacks, apply the following requirements: 

- **Secure network and application layers** : Establish a multi-layered defense for all of your AI assets. 

   - To create a security perimeter that prevents data exfiltration of models from Model Registry or of sensitive data from BigQuery, use VPC Service Controls (/vpc-service-controls/docs/overview). Always use dry run mode (/vpc-service-controls/docs/dry-run-mode) to validate the impact of a perimeter before you enforce it. 

   - To help protect web-based tools such as notebooks, use IAP (/iap/docs/concepts-overview). 

   - To help secure all of the inference endpoints, use Apigee (/apigee) for enterprise-grade security and governance. You can also use API Gateway for straightforward authentication. 

**Watch for query pattern anomalies** : For example, an attacker that probes a system for vulnerabilities might send thousands of slightly different, sequential queries. Flag abnormal query patterns that don't reflect normal user behavior. 

**Monitor the volume of requests** : A sudden spike in query volume strongly indicates a denial-of-service (DoS) attack or a model theft attack, which is an attempt to reverse-engineer the model. Use rate limiting and throttling to control the volume of requests from a single IP address or user. 

**Monitor and set alerts for geographic and temporal anomalies** : Establish a baseline for normal access patterns. Generate alerts for sudden activity from unusual geographic locations or at odd hours. For example, a massive spike in logins from a new country at 3 AM. 

### Monitor, evaluate, and prepare to respond to outputs

AI systems deliver value because they produce outputs that augment, optimize, or automate human decision-making. To maintain the integrity and trustworthiness of your AI systems and applications, ensure that the outputs are secure and within the expected parameters. You also need a plan to respond to incidents. 

To maintain your outputs, consider the following recommendations. 

#### Evaluate model performance with metrics and security measures

To ensure that your AI models meet performance benchmarks, meet security requirements, and adhere to fairness and compliance standards, thoroughly evaluate the models. Conduct evaluations before deployment, and then continue to evaluate the models in production on a regular basis. To minimize risks and build trustworthy AI systems, implement a comprehensive evaluation strategy that combines performance metrics with specific AI security assessments. 

To evaluate model robustness and security posture, consider the following recommendations: 

Implement model signing and verification in your MLOps pipeline. 

- For containerized models, use Binary Authorization 

- (/binary-authorization/docs/cloud-build) to verify signatures. 

- For models that are deployed directly to Agent Platform endpoints, use custom checks in your deployment scripts for verification. 

- For any model, use Cloud Build for model signing. 

Assess your model's resilience to unexpected or adversarial inputs. 

- For all of your models, test your model for common data corruptions and any potentially malicious data modifications. To orchestrate these tests, you can use Gemini Enterprise Agent Platform Managed Training or Agent Platform Pipelines. 

- For security-critical models, conduct adversarial attack simulations to understand the potential vulnerabilities. 

   - For models that are deployed in containers, use Artifact Analysis in Artifact Registry to scan the base images for vulnerabilities. 

- Use Model Monitoring on Gemini Enterprise Agent Platform to detect drift and skew for deployed models. Then, feed these insights back into the reevaluation or retraining cycles. 

- Use model evaluations from Agent Platform as a pipeline component with Agent Platform Pipelines. You can run the model evaluation component by itself or with other pipeline components. Compare the model versions against your defined metrics and datasets. Log the evaluation results to Agent Platform ML Metadata for lineage and tracking. 

- Use or build upon the Gen AI evaluation service 

- (/gemini-enterprise-agent-platform/models/evaluation-overview) to evaluate your chosen models or to implement custom human-evaluation workflows. 

To assess fairness, bias, explainability, and factuality, consider the following recommendations: 

- Define fairness measures 

- (/gemini-enterprise-agent-platform/machine-learning/evaluation/intro-evaluationfairness) 

that match your use cases, and then evaluate your models for potential biases across different data slices. 

- Understand which features drive model predictions in order to ensure that the features, and the predictions that result, align with domain knowledge and ethical guidelines. 

- Use explainability techniques to get feature attributions for your models. 

- Use the Gen AI evaluation service to compute metrics. During the source verification phase of testing, the service's grounding metric checks for factuality against the source text that's provided. 

- Enable grounding (/gemini-enterprise-agent-platform/models/grounding/overview) for your model's output in order to facilitate a second layer of source verification at the user level. 

- Review our AI principles (https://ai.google/principles/) and adapt them for your AI applications. 

#### Monitor AI and ML model outputs in production

Continuously monitor your AI and ML models and their supporting infrastructure in production. It's important to promptly identify and diagnose degradations in model output quality or performance, security vulnerabilities that emerge, and deviations from compliance mandates. This monitoring helps you sustain system safety, reliability, and trustworthiness. 

To monitor AI system outputs for anomalies, threats, and quality degradation, consider the following recommendations: 

- Use Model Monitoring on Agent Platform for your model outputs to track unexpected shifts in prediction distributions or spikes in low-confidence model predictions. Actively monitor your generative AI model outputs for generated content that's unsafe, biased, off-topic, or malicious. You can also use Model Armor to screen all of your model outputs. 

- Identify specific error patterns, capture quality indicators, or detect harmful or non-compliant outputs at the application level. To find these issues, use custom monitoring in Monitoring dashboards and use log-based metrics from Logging. 

To monitor outputs for security-specific signals and unauthorized changes, consider the following recommendations: 

- Identify unauthorized access attempts to AI models, datasets in Cloud Storage or BigQuery, or MLOps pipeline components. In particular, identify unexpected or unauthorized changes in IAM permissions for AI resources. To track these activities and review them for suspicious patterns, use the Admin Activity audit logs and Data Access audit logs in Cloud Audit Logs. Integrate the findings from Security Command Center, which can flag security misconfigurations and flag potential threats that are relevant to your AI assets. 

- Monitor outputs for high volumes of requests or requests from suspicious sources, which might indicate attempts to reverse engineer models or exfiltrate data. You can also use Sensitive Data Protection to monitor for the exfiltration of potentially sensitive data. 

- Integrate logs into your security operations. Use Google Security Operations to help you detect, orchestrate, and respond to any cyber threats from your AI 

systems. 

To track the operational health and performance of the infrastructure that serves your AI models, consider the following recommendations: 

- Identify operational issues that can impact service delivery or model performance. 

- Monitor Agent Platform endpoints for latency, error rates, and traffic patterns. Monitor MLOps pipelines for execution status and errors. 

- Use Monitoring, which provides ready-made metrics. You can also create custom dashboards to help you identify issues like endpoint outages or pipeline failures. 

#### Implement alerting and incident response procedures

When you identify any potential performance, security, or compliance issues, an effective response is critical. To ensure timely notifications to the appropriate teams, implement robust alerting mechanisms. Establish and operationalize comprehensive, AI-aware incident response procedures to manage, contain, and remediate these issues efficiently. 

To establish robust alerting mechanisms for AI issues that you identify, consider the following recommendations: 

- Configure actionable alerts to notify the relevant teams, based on the monitoring activities of your platform. For example, configure alerts to trigger when Model Monitoring on Agent Platform detects significant drift, skew, or prediction anomalies. Or, configure alerts to trigger when Model Armor or custom Monitoring rules flag malicious inputs or unsafe outputs. 

- Define clear notification channels, which can include Slack, email, or SMS through Pub/Sub integrations. Customize the notification channels for your alert severities and the responsible teams. 

Develop and operationalize an AI-aware incident response plan. A structured incident response plan is vital to minimize any potential impacts and ensure recovery. Customize this plan to address AI-specific risks such as model tampering, 

incorrect predictions due to drift, prompt injection, or unsafe outputs from generative models. To create an effective plan, include the following key phases: 

- **Preparation** : Identify assets and their vulnerabilities, develop playbooks, and ensure that your teams have appropriate privileges. This phase includes the following tasks: 

   - Identify critical AI assets, such as models, datasets, and specific Agent Platform resources like endpoints or Feature Store instances. 

   - Identify the assets' potential failure modes or attack vectors. 

   - Develop AI-specific playbooks for incidents that match your organization's threat model. For example, playbooks might include the following: 

      - A model rollback that uses versioning in Model Registry. 

      - An emergency retraining pipeline on Gemini Enterprise Agent Platform Managed Training. 

      - The isolation of a compromised data source in BigQuery or Cloud Storage. 

   - Use IAM to ensure that response teams have the necessary leastprivilege access to tools that are required during an incident. 

- **Identification and triage** : Use configured alerts to detect and validate potential incidents. Establish clear criteria and thresholds for how your organization investigates or declares an AI-related incident. For detailed investigation and evidence collection, use Logging for application logs and service logs, and use Cloud Audit Logs for administrative activities and data access patterns. Security teams can use Google SecOps for deeper analyses of security telemetry. 

- **Containment** : Isolate affected AI systems or components to prevent further impact or data exfiltration. This phase might include the following tasks: 

   - Disable a problematic Agent Platform endpoint. 

   - Revoke specific IAM permissions. 

   - Update firewall rules or Cloud Armor policies. 

   - Pause a Agent Platform pipeline that's misbehaving. 

- **Eradication** : Identify and remove the root cause of the incident. This phase might include the following tasks: 

   - Patch the vulnerable code in a custom model container. 

   - Remove the identified malicious backdoors from a model. 

   - Sanitize the poisoned data before you initiate a secure retraining job on Gemini Enterprise Agent Platform Managed Training. 

   - Update any insecure configurations. 

   - Refine the input validation logic to block specific prompt-injection techniques. 

- **Recovery and secure redeployment** : Restore the affected AI systems to a known good and secure operational state. This phase might include the following tasks: 

   - Deploy a previously validated and trusted model version from Model Registry. 

   - Ensure that you find and apply all of the security patches for vulnerabilities that might be present in your code or system. 

   - Reset the IAM permissions to the principle of least privilege. 

- **Post-incident activity and lessons learned** : After you resolve the significant AI incidents, conduct a thorough post-incident review. This review involves all of the relevant teams, such as the AI and ML, MLOps, security, and data science teams. Understand the full lifecycle of the incident. Use these insights to refine the AI system design, update security controls, improve Monitoring configurations, and enhance the AI incident response plan and playbooks. 

Integrate the AI incident response with the broader organizational frameworks, such as IT and security incident management, for a coordinated effort. To align your AI-specific incident response with your organizational frameworks, consider the following: 

- **Escalation** : Define clear paths for how you escalate significant AI incidents to central SOC, IT, legal, or relevant business units. 

- **Communication** : Use established organizational channels for all internal and external incident reports and updates. 

- **Tooling and processes** : Use existing enterprise incident management and ticketing systems for AI incidents to ensure consistent tracking and visibility. 

- **Collaboration** : Pre-define collaboration protocols between AI and ML, MLOps, data science, security, legal, and compliance teams for effective AI incident responses. 

### Contributors

Authors: 

- Kamilla Kurta (https://www.linkedin.com/in/kamillakurta) | GenAI/ML Specialist Customer Engineer 

- Vidhi Jain (https://www.linkedin.com/in/vidhi-jain-jpm) | Cloud Engineer, Analytics and AI 

- Mohamed Fawzi (https://www.linkedin.com/in/fawzii) | Benelux Security and Compliance Lead 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

Other contributors: 

- Lauren Anthony (https://www.linkedin.com/in/lauren-a-5a778a44) | Customer Engineer, Security Specialist 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect 

- John Bacon (https://www.linkedin.com/in/johnbac/) | Partner Solutions Architect 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

- Mónica Carranza (https://www.linkedin.com/in/monicaecp/) | Senior Generative AI Threat Analyst 

- Tarun Sharma (https://www.linkedin.com/in/tarun27in) | Principal Architect 

- Wade Holmes (https://www.linkedin.com/in/wholmes) | Global Solutions Director 

## AI and ML perspective: Reliability

This document in the Google Cloud Well-Architected Framework: AI and ML perspective (/architecture/framework/perspectives/ai-ml) provides an overview of the principles and recommendations to design and operate reliable AI and ML systems on Google Cloud. It explores how to integrate advanced reliability practices and observability into your architectural blueprints. The recommendations in this document align with the reliability pillar (/architecture/framework/reliability) of the Google Cloud Well-Architected Framework. 

In the fast-evolving AI and ML landscape, reliable systems are essential in order to ensure customer satisfaction and achieve business goals. To meet the unique demands of both predictive ML and generative AI, you need AI and ML systems that are robust, reliable, and adaptable. To handle the complexities of MLOps (/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning)— from development to deployment and continuous improvement—you need to use a reliability-first approach. Google Cloud offers a purpose-built AI infrastructure that's aligned with site reliability engineering (SRE) (https://sre.google/) principles and that provides a powerful foundation for reliable AI and ML systems. 

The recommendations in this document are mapped to the following core principles: 

- Ensure that infrastructure is scalable and highly available (#scalable-highly-available-infrastructure) 

- Use a modular and loosely coupled architecture (#modular-loosely-coupled-architecture) 

- Build an automated end-to-end MLOps platform 

- (#automated-end-to-end-mlops-platform) 

Maintain trust and control through data and model governance 

- (#trust-control-through-governance) 

Implement holistic observability and reliability practices 

- (#holistic-observability-reliability-practices) 

### Ensure that ML infrastructure is scalable and highly available

Reliable AI and ML systems in the cloud require scalable and highly available infrastructure. These systems have dynamic demands, diverse resource needs, and critical dependencies on model availability. Scalable architectures adapt to fluctuating loads and variations in data volume or inference requests. High availability (HA) helps to ensure resilience against failures at the component, zone, or region level. 

To build scalable and highly available ML infrastructure, consider the following recommendations. 

#### Implement automatic and dynamic scaling capabilities

AI and ML workloads are dynamic, with demand that fluctuates based on data arrival rates, training frequency, and the volume of inference traffic. Automatic and dynamic scaling adapts infrastructure resources seamlessly to demand fluctuations. Scaling your workloads effectively helps to prevent downtime, maintain performance, and optimize costs. 

To autoscale your AI and ML workloads, use the following products and features in Google Cloud: 

**Data processing pipelines** : Create data pipelines in Dataflow 

(/dataflow/docs/overview). Configure the pipelines to use Dataflow's horizontal autoscaling (/dataflow/docs/horizontal-autoscaling) feature, which dynamically adjusts the number of worker instances based on CPU utilization, pipeline parallelism, and pending data. You can configure autoscaling parameters through pipeline options when you launch jobs. 

**Training jobs** : Automate the scaling of training jobs by using Gemini Enterprise Agent Platform custom training 

(/gemini-enterprise-agent-platform/machine-learning/training/configure-compute). You can define worker pool specifications such as the machine type, the type and number of accelerators, and the number of worker pools. For jobs that can tolerate interruptions and for jobs where the training code implements checkpointing, you can reduce costs by using Spot VMs 

- (/gemini-enterprise-agent-platform/machine-learning/training/use-spot-vms). 

**Online inference** : For online inference, use Agent Platform endpoints 

(/gemini-enterprise-agent-platform/machine-learning/general/deployment). To enable autoscaling, configure the minimum and maximum replica count. Specify a minimum of two replicas for HA. Agent Platform automatically adjusts the number of replicas based on traffic and the configured autoscaling metrics, such as CPU utilization and replica utilization. 

**Containerized workloads in** **Google Kubernetes Engine** 

(/kubernetes-engine/docs/concepts/kubernetes-engine-overview): Configure autoscaling at the node and Pod levels. Configure the cluster autoscaler (/kubernetes-engine/docs/concepts/cluster-autoscaler) and node auto-provisioning (/kubernetes-engine/docs/how-to/node-auto-provisioning) to adjust the node count based on pending Pod resource requests like CPU, memory, GPU, and TPU. Use Horizontal Pod Autoscaler (HPA) 

- (/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling) for deployments to define scaling policies based on metrics like CPU and memory utilization. You can also scale based on custom AI and ML metrics, such as GPU or TPU utilization and prediction requests per second. 

**Serverless containerized services** : Deploy the services in Cloud Run (/run/docs/configuring/services/gpu#gps-max-instances) and configure autoscaling by specifying the minimum and maximum number of container instances. Use best practices (/run/docs/configuring/services/gpu-best-practices#autoscaling-and-gpu) to autoscale GPU-enabled instances by specifying the accelerator type. Cloud Run automatically scales instances between the configured minimum and maximum limits based on incoming requests. When there are no requests, it scales efficiently to zero instances. You can leverage the automatic, requestdriven scaling of Cloud Run to deploy agents (/run/docs/ai-agents) and to deploy third-party workloads like quantized models using Ollama 

(/run/docs/tutorials/gpu-gemma-with-ollama) and LLM model inference using vLLM (/run/docs/tutorials/gpu-gemma2-with-vllm). 

#### Design for HA and fault tolerance

For production-grade AI and ML workloads, it's crucial that you ensure continuous operation and resilience against failures. To implement HA and fault tolerance, you need to build redundancy and replication into your architecture on Google Cloud. This approach helps to ensure that a failure of an individual component doesn't cause a failure of the complete system. 

- For HA and low latency in model serving, particularly for real-time inference and generative AI models, distribute your deployments across multiple locations. 

- For global availability and resilience, deploy the models to multiple Agent Platform endpoints 

- (/gemini-enterprise-agent-platform/machine-learning/general/deployment) across Google Cloud regions or use the global endpoint 

- (/gemini-enterprise-agent-platform/resources/locations#global-endpoint). 

- Use global load balancing to route traffic. 

- For training on GKE or Compute Engine MIGs, implement monitoring for Xid errors (/compute/docs/troubleshooting/troubleshooting-gpus#xid_messages). When you identify Xid errors, take appropriate remedial action. For example, reset GPUs (/compute/docs/troubleshooting/troubleshooting-gpus#reset-gpus), reset Compute Engine instances (/compute/docs/instances/reset-instance#reset-instance), or trigger hardware replacement by using the gcloud CLI report faulty host 

- (/ai-hypercomputer/docs/manage/report-faulty-host#report-a-faulty-host) command. 

- Explore fault-tolerant or elastic and resilient training solutions like recipes to use the Google Resiliency Library 

(https://github.com/AI-Hypercomputer/gpu- 

recipes/tree/main/training/a3mega/llama3_70b) 

or integration of the Resilient training with Pathways 

- (/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training) logic for TPU workloads. 

Implement redundancy for critical AI and ML components in Google Cloud. The following are examples of products and features that let you implement resource redundancy: 

- Deploy GKE regional clusters (/kubernetes-engine/docs/concepts/regional-clusters) across multiple zones. 

- Ensure data redundancy for datasets and checkpoints by using Cloud Storage (/storage/docs/storage-classes#standard-availability) multi-regional or dual-region buckets. 

- Use Spanner for globally consistent, highly available storage of metadata. 

- Configure Cloud SQL read replicas (/sql/docs/mysql/replication/create-replica) for operational databases. 

- Ensure that vector databases 

- (/gemini-enterprise-agent-platform/build/rag-engine/vector-db-choices) for retrieval augmented generation (RAG) are highly available and multi-zonal or multiregional. 

#### Manage resources proactively and anticipate requirements

Effective resource management is important to help you optimize costs, performance, and reliability. AI and ML workloads are dynamic and there's high demand for specialized hardware like GPUs and TPUs. Therefore, it's crucial that you apply proactive resource management and ensure resource availability. 

Plan for capacity based on historical monitoring data, such as GPU or TPU utilization and throughput rates, from Cloud Monitoring 

(/monitoring/docs/monitoring-overview) and logs in Cloud Logging 

(/logging/docs/overview). Analyze this telemetry data by using BigQuery (/bigquery/docs/introduction) or Data Studio (/looker/docs/studio) and forecast future demand for GPUs based on growth or new models. Analysis of resource usage patterns and trends helps you to predict when and where you need critical specialized accelerators. 

- Validate capacity estimates through rigorous load testing. Simulate traffic on AI and ML services like serving and pipelines by using tools like Apache JMeter (https://jmeter.apache.org/) or LoadView (https://www.loadview-testing.com). 

- Analyze system behavior under stress. 

   - To anticipate and meet increased workload demands in production, proactively identify resource requirements. Monitor latency, throughput, errors, and resource utilization, especially GPU and TPU utilization. Increase resource quotas as necessary. 

   - For generative AI serving, test under high concurrent loads and identify the level at which accelerator availability limits performance. 

- Perform continuous monitoring for model queries and set up proactive alerts (/gemini-enterprise-agent-platform/optimize/evaluation/quality-alerts) for agents. 

   - Use the model observability dashboard 

   - (/gemini-enterprise-agent-platform/models/model-observability#view) to view metrics that are collected by Cloud Monitoring, such as model queries per second (QPS), token throughput, and first token latencies. 

#### Optimize resource availability and obtainability

Optimize costs and ensure resource availability by strategically selecting appropriate compute resources based on workload requirements. 

- For stable 24x7 inference or for training workloads with fixed or predictable capacity requirements, use committed use discounts (CUDs) 

- (/compute/docs/instances/committed-use-discounts-overview) for VMs and accelerators. 

- For GKE nodes and Compute Engine VMs, use Spot VMs and Dynamic Workload Scheduler (DWS) capabilities: 

   - For fault-tolerant tasks such as evaluation and experimentation workloads, use Spot VMs (/kubernetes-engine/docs/concepts/spot-vms). Spot VMs can be preempted, but they can help reduce your overall costs. 

   - To manage preemption risk for high-demand accelerators, you can ensure better obtainability by using DWS 

   - (/kubernetes-engine/docs/how-to/provisioningrequest). 

      - For complex batch training that needs high-end GPUs to run up to seven days, use the DWS Flex-Start mode. 

      - For longer running workloads that run up to three months, use the Calendar mode to reserve specific GPUs (H100 and H200) and TPUs (Trillium). 

- To optimize AI inference on GKE, you can run a vLLM (https://docs.vllm.ai/en/stable/) engine that dynamically uses TPUs and GPUs to address fluctuating capacity and performance needs. For more information, see vLLM GPU/TPU Fungibility 

- (https://gke-ai-labs.dev/docs/tutorials/gpu-tpu/fungibility-recipes/). 

- For advanced scenarios with complex resource and topology needs that involve accelerators, use tools to abstract resource management. 

   - Cluster Director (/ai-hypercomputer/docs/cluster-director) lets you deploy and manage accelerator groups with colocation and scheduling for multi-GPU training (A3 Ultra H200 and A4 B200). Cluster Director supports GKE and Slurm clusters. 

   - Ray on Gemini Enterprise Agent Platform 

   - (/gemini-enterprise-agent-platform/machine-learning/open-source/ray) abstracts distributed computing infrastructure. It enables applications to request resources for training and serving without the need for direct management of VMs and containers. 

#### Distribute incoming traffic across multiple instances

Effective load balancing is crucial for AI applications that have fluctuating demands. Load balancing distributes traffic, optimizes resource utilization, provides HA and low latency, and helps to ensure a seamless user experience. 

- **Inference with varying resource needs** : Implement load balancing based on model metrics. GKE Inference Gateway 

- (/kubernetes-engine/docs/concepts/about-gke-inference-gateway) lets you deploy models behind a load balancer with model-aware routing. The gateway prioritizes instances with GPU and TPU accelerators for compute-intensive tasks like generative AI and LLM inference. Configure detailed health checks to assess model status. Use serving frameworks like vLLM or Triton for LLM metrics and integrate the metrics into Cloud Monitoring 

- (/monitoring/docs/monitoring-overview) by using Google Cloud Managed Service for Prometheus (/stackdriver/docs/managed-prometheus). 

- **Inference workloads that need GPUs or TPUs** : To ensure that critical AI and ML inference workloads consistently run on machines that are suitable to the workloads' requirements, particularly when GPU and TPU availability is constrained, use GKE custom compute classes 

- (/kubernetes-engine/docs/concepts/about-custom-compute-classes). You can define specific compute _profiles_ with fallback policies for autoscaling. For example, you can define a profile that specifies a higher priority for reserved GPU or TPU instances. The profile can include a fallback to use cost-efficient Spot VMs if the reserved resources are temporarily unavailable. 

- **Generative AI on diverse orchestration platforms** : Use a centralized load balancer. For example, for cost and management efficiency, you can route requests that have low GPU needs to Cloud Run and route more complex, GPU-intensive tasks to GKE. For inter-service communication and policy management, implement a service mesh by using Cloud Service Mesh (/service-mesh/docs/onboarding/provision-control-plane). Ensure consistent logging and monitoring by using Cloud Logging and Cloud Monitoring. 

- **Global load distribution** : To load balance traffic from global users who need low latency, use a global external Application Load Balancer (/load-balancing/docs/https). Configure geolocation routing to the closest region and implement failover. Establish regional endpoint replication in Agent Platform or GKE. Configure Cloud CDN for static assets. Monitor global traffic and latency by using Cloud Monitoring. 

- **Granular traffic management** : For requests that have diverse data types or complexity and long-running requests, implement granular traffic management. 

   - Configure content-based routing 

   - (/load-balancing/docs/url-map#traffic-management-guides) to direct requests to specialized backends based on attributes like URL paths and headers. For example, direct requests to GPU-enabled backends for image or video models and to CPU-optimized backends for text-based models. 

   - For long-running generative AI requests or batch workloads, use WebSockets or gRPC. Implement traffic management to handle timeouts and buffering. Configure request timeouts and retries and implement rate limiting and quotas by using API Gateway or Apigee. 

### Use a modular and loosely coupled architecture

In a modular, loosely coupled AI and ML architecture, complex systems are divided into smaller, self-contained components that interact through well-defined interfaces. This architecture minimizes module dependencies, simplifies development and testing, enhances reproducibility, and improves fault tolerance by containing failures. The modular approach is crucial for managing complexity, accelerating innovation, and ensuring long-term maintainability. 

To design a modular and loosely coupled architecture for AI and ML workloads, consider the following recommendations. 

#### Implement small self-contained modules or components

Separate your end-to-end AI and ML system into small, self-contained modules or components. Each module or component is responsible for a specific function, such as data ingestion, feature transformation, model training, inference serving, or evaluation. A modular design provides several key benefits for AI and ML systems: improved maintainability, increased scalability, reusability, and greater flexibility and agility. 

The following sections describe Google Cloud products, features, and tools that you can use to design a modular architecture for your AI and ML systems. 

Containerized microservices on GKE 

For complex AI and ML systems or intricate generative AI pipelines that need finegrained orchestration, implement modules as microservices that are orchestrated by using GKE. Package each distinct stage as an individual microservice within Docker containers. These distinct stages include data ingestion that's tailored for diverse formats, specialized data preprocessing or feature engineering, distributed model training or fine tuning of large foundation models, evaluation, or serving. 

Deploy the containerized microservices on GKE and leverage automated scaling based on CPU and memory utilization or custom metrics like GPU utilization, rolling updates, and reproducible configurations in YAML manifests. Ensure efficient communication between the microservices by using GKE service discovery. For 

asynchronous patterns, use message queues like Pub/Sub 

(/pubsub/docs/pubsub-basics). 

The microservices-on-GKE approach helps you build scalable, resilient platforms for tasks like complex RAG applications where the stages can be designed as distinct services. 

Serverless event-driven services 

For event-driven tasks that can benefit from serverless, automatic scaling, use Cloud Run (/run/docs/overview/what-is-cloud-run) or Cloud Run functions 

(/functions/docs/concepts/overview). These services are ideal for asynchronous tasks like preprocessing or for smaller inference jobs. Trigger Cloud Run functions on events, such as a new data file that's created in Cloud Storage or model updates in Artifact Registry. For web-hook tasks or services that need a container environment, use Cloud Run. 

Cloud Run services and Cloud Run functions can scale up rapidly and scale down to zero, which helps to ensure cost efficiency for fluctuating workloads. These services are suitable for modular components in Agent Conversation workflows. You can orchestrate component sequences with Workflows (/workflows/docs/overview) or Application Integration (/application-integration/docs/overview). 

Agent Platform managed services 

Agent Platform services support modularity and help you simplify the development and deployment of your AI and ML systems. The services abstract the infrastructure complexities so that you can focus on the application logic. 

- To orchestrate workflows that are built from modular steps, use Gemini Enterprise Agent Platform Pipelines. 

- To run custom AI and ML code, package the code in Docker containers that can run on managed services like Agent Platform custom training and Agent Platform prediction. 

- For modular feature engineering pipelines, use Agent Platform Feature Store (/gemini-enterprise-agent-platform/machine-learning/featurestore/latest/overview). 

- For modular exploration and prototyping, use notebook environments like Gemini Enterprise Agent Platform Workbench 

(/gemini-enterprise-agent-platform/notebooks/workbench/introduction) or Colab Enterprise (/colab/docs/introduction). Organize your code into reusable functions, classes, and scripts. 

Agentic applications 

For AI agents, Agent Development Kit (ADK) (https://adk.dev/) provides modular capabilities like Tools (https://adk.dev/tools/) and State (https://adk.dev/sessions/state/). To enable interoperability between frameworks like LangChain 

(https://python.langchain.com/docs/tutorials), LangGraph 

(https://langchain-ai.github.io/langgraph), LlamaIndex (https://www.llamaindex.ai/), and Agent Platform, you can combine ADK with the Agent2Agent (A2A) protocol (https://a2a-protocol.org/latest/) and the Model Context Protocol (MCP) (https://github.com/modelcontextprotocol). This interoperability lets you compose agentic workflows by using diverse components. 

You can deploy agents on Agent Runtime on Gemini Enterprise Agent Platform, which is a managed runtime that's optimized for scalable agent deployment. To run containerized agents, you can leverage the autoscaling capabilities in Cloud Run. 

#### Design well-defined interfaces

To build robust and maintainable software systems, it's crucial to ensure that the components of a system are loosely coupled and modularized. This approach offers significant advantages, because it minimizes the dependencies between different parts of the system. When modules are loosely coupled, changes in one module have minimal impact on other modules. This isolation enables independent updates and development workflows for individual modules. 

The following sections provide guidance to help ensure seamless communication and integration between the modules of your AI and ML systems. 

Protocol choice 

- For universal access, use HTTP APIs, adhere to RESTful principles, and use JSON for language-agnostic data exchange. Design the API endpoints to 

represent actions on resources. 

- For high-performance internal communication among microservices, use gRPC (https://grpc.io/docs/) with Protocol Buffers (ProtoBuf) 

- (https://developers.google.com/protocol-buffers/docs/overview) for efficient serialization and strict typing. Define data structures like ModelInput, PredictionResult, or ADK Tool data by using `.proto` files, and then generate language bindings. 

- For use cases where performance is critical, leverage gRPC streaming for large datasets or for continuous flows such as live text-to-speech or video applications. Deploy the gRPC services on GKE. 

Standardized and comprehensive documentation 

Regardless of the interface protocol that you choose, standardized documentation is crucial. The OpenAPI Specification (https://swagger.io/specification/) describes RESTful APIs. Use OpenAPI to document your AI and ML APIs: paths, methods, parameters, request-response formats that are linked to JSON schemas, and security. Comprehensive API documentation helps to improve discoverability and client integration. For API authoring and visualization, use UI tools like Swagger Editor (https://swagger.io/tools/swagger-editor/). To accelerate development and ensure consistency, you can generate client SDKs and server stubs by using AI-assisted coding tools like Gemini Code Assist (https://codeassist.google/). Integrate OpenAPI documentation into your CI/CD flow. 

Interaction with Google Cloud managed services like Agent Platform 

Choose between the higher abstraction of the Agent Platform SDK, which is preferred for development productivity, and the granular control that the REST API provides. 

- The Agent Platform SDK simplifies tasks and authentication. Use the SDK when you need to interact with Agent Platform. 

- The REST API is a powerful alternative especially when interoperability is required between layers of your system. It's useful for tools in languages that don't have an SDK or when you need fine-grained control. 

#### Use APIs to isolate modules and abstract implementation details

For security, scalability, and visibility, it's crucial that you implement robust API management for your AI and ML services. To implement API management for your defined interfaces, use the following products: 

- **API Gateway** (/api-gateway/docs/about-api-gateway): For APIs that are externally exposed and managed, API Gateway provides a centralized, secure entry point. It simplifies access to serverless backend services, such as prediction, training, and data APIs. API Gateway helps to consolidate access points, enforce API contracts, and manage security capabilities like API keys and OAuth 2.0. To protect backends from overload and ensure reliability, implement rate limiting and usage quotas in API Gateway. 

- **Cloud Endpoints** (/endpoints/docs): To streamline API development and deployment on GKE and Cloud Run, use Cloud Endpoints, which offers a developer-friendly solution for generating API keys. It also provides integrated monitoring and tracing for API calls and it automates the generation of OpenAPI specs, which simplifies documentation and client integration. You can use Cloud Endpoints to manage access to internal or controlled AI and ML APIs, such as to trigger training and manage feature stores. 

- **Apigee** (/apigee/docs/api-platform/get-started/what-apigee): For enterprise-scale AI and ML, especially sophisticated generative AI APIs, Apigee provides advanced, comprehensive API management. Use Apigee for advanced security like threat protection and OAuth 2.0, for traffic management like caching, quotas, and mediation, and for analytics. Apigee can help you to gain deep insights into API usage patterns, performance, and engagement, which are crucial for understanding generative AI API usage. 

#### Plan for graceful degradation

In production AI and ML systems, component failures are unavoidable, just like in other systems. Graceful degradation ensures that essential functions continue to operate, potentially with reduced performance. This approach prevents complete outages and improves overall availability. Graceful degradation is critical for latency-sensitive inference, distributed training, and generative AI. 

The following sections describe techniques that you use to plan and implement graceful degradation. 

Fault isolation 

- To isolate faulty components in distributed architectures, implement the circuit breaker pattern (https://martinfowler.com/bliki/CircuitBreaker.html) by using resilience libraries, such as Resilience4j (https://resilience4j.readme.io/) in Java and CircuitBreaker (https://pypi.org/project/circuitbreaker/) in Python. 

- To prevent cascading failures, configure thresholds based on AI and ML workload metrics like error rates and latency and define fallbacks like simpler models and cached data. 

Component redundancy 

For critical components, implement redundancy and automatic failover. For example, use GKE multi-zone clusters or regional clusters and deploy Cloud Run services redundantly across different regions. To route traffic to healthy instances when unhealthy instances are detected, use Cloud Load Balancing. 

Ensure data redundancy by using Cloud Storage multi-regional buckets. For distributed training, implement asynchronous checkpointing to resume after failures. For resilient and elastic training, use Pathways 

(/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training). 

Proactive monitoring 

Graceful degradation helps to ensure system availability during failure, but you must also implement proactive measures for continuous health checks and comprehensive monitoring. Collect metrics that are specific to AI and ML, such as latency, throughput, and GPU utilization. Also, collect model performance degradation metrics like model and data drift by using Cloud Monitoring and Model Monitoring on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview). 

Health checks can trigger the need to replace faulty nodes, deploy more capacity, or automatically trigger continuous retraining or fine-tuning of pipelines that use updated data. This proactive approach helps to prevent both accuracy-based 

degradation and system-level graceful degradation and it helps to enhance overall reliability. 

SRE practices 

To monitor the health of your systems, consider adopting SRE practices to implement service level objectives (SLOs) 

(https://sre.google/sre-book/service-level-objectives/). Alerts on error budget loss and burn rate can be early indicators of reliability problems with the system. For more information about SRE practices, see the Google SRE book 

(https://sre.google/sre-book/table-of-contents/). 

### Build an automated end-to-end MLOps platform

A robust, scalable, and reliable AI and ML system on Google Cloud requires an automated end-to-end MLOps platform for the model development lifecycle. The development lifecycle includes initial data handling, continuous model training, deployment, and monitoring in production. By automating these stages on Google Cloud, you establish repeatable processes, reduce manual toil, minimize errors, and accelerate the pace of innovation. 

An automated MLOps platform is essential for establishing production-grade reliability for your applications. Automation helps to ensure model quality, guarantee reproducibility, and enable continuous integration and delivery of AI and ML artifacts. 

To build an automated end-to-end MLOps platform, consider the following recommendations. 

#### Automate the model development lifecycle

A core element of an automated MLOps platform is the orchestration of the entire AI and ML workflow as a series of connected, automated steps: from data preparation and validation to model training, evaluation, deployment, and monitoring. 

- Use Agent Platform Pipelines 

- (/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction) as your central orchestrator: 

   - Define end-to-end workflows with modular components for data processing, training, evaluation, and deployment. 

   - Automate pipeline runs by using schedules or triggers like new data or code changes. 

   - Implement automated parameterization and versioning for each pipeline run and create a version history. 

   - Monitor pipeline progress and resource usage by using built-in logging and tracing, and integrate with Cloud Monitoring alerts (/monitoring/alerts). 

- Define your ML pipelines programmatically by using the Kubeflow Pipelines (KFP) SDK or TensorFlow Extended SDK. For more information, see Interfaces for Agent Platform Pipelines 

- (/gemini-enterprise-agent-platform/machine-learning/pipelines/interfaces). 

- Orchestrate operations by using Google Cloud services like Dataflow 

- (/dataflow/docs/overview), Agent Platform custom training 

- (/gemini-enterprise-agent-platform/machine-learning/training/create-custom-job), Model Registry on Gemini Enterprise Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction), and Agent Platform endpoints. 

- For generative AI workflows, orchestrate the steps for prompt management, batched inference, human-in-the-loop (HITL) evaluation, and coordinating ADK components. 

#### Manage infrastructure as code

Infrastructure as code (IaC) is crucial for managing AI and ML system infrastructure and for enabling reproducible, scalable, and maintainable deployments. The infrastructure needs of AI and ML systems are dynamic and complex. The systems often require specialized hardware like GPUs and TPUs. IaC helps to mitigate the risks of manual infrastructure management by ensuring consistency, enabling rollbacks, and making deployments repeatable. 

To effectively manage your infrastructure resources as code, use the following techniques. 

Automate resource provisioning 

To effectively manage IaC on Google Cloud, define and provision your AI and ML infrastructure resources by using Terraform (https://developer.hashicorp.com/terraform). The infrastructure might include resources such as the following: 

- GKE clusters that are configured with node pools. The node pools can be optimized based on workload requirements. For example, you can use A100, H100, H200, or B200 GPUs for training, and use L4 GPUs for inference. 

- Agent Platform endpoints 

- (/gemini-enterprise-agent-platform/machine-learning/general/deployment) that are configured for model serving, with defined machine types and scaling policies. 

Cloud Storage buckets (/storage/docs/buckets) for data and artifacts. 

Use configuration templates 

Organize your Terraform configurations as modular templates. To accelerate the provisioning of AI and ML resources, you can use Cluster Toolkit 

(/cluster-toolkit/docs/overview). The toolkit provides example blueprints (https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples), which are Google-curated Terraform templates that you can use to deploy ready-to-use HPC, AI, and ML clusters in Slurm or GKE. You can customize the Terraform code and manage it in your version control system. To automate the resource provisioning and update workflow, you can integrate the code into your CI/CD pipelines by using Cloud Build (/build/docs/overview). 

Automate configuration changes 

After you provision your infrastructure, manage the ongoing configuration changes declaratively: 

- In Kubernetes-centric environments, manage your Google Cloud resources as Kubernetes objects by using Config Connector (/config-connector/docs/overview). 

- Define and manage Agent Platform resources like datasets, models, and endpoints, Cloud SQL instances, Pub/Sub topics, and Cloud Storage buckets by using YAML manifests. 

- Deploy the manifests to your GKE cluster in order to integrate the application and infrastructure configuration. 

- Automate configuration updates by using CI/CD pipelines and use templating to handle environment differences. 

- Implement configurations for Identity and Access Management (IAM) policies and service accounts by using IaC. 

Integrate with CI/CD 

- Automate the lifecycle of the Google Cloud infrastructure resources by integrating IaC into CI/CD pipelines by using tools like Cloud Build (/build/docs/overview) and Infrastructure Manager 

- (/infrastructure-manager/docs/overview). 

- Define triggers for automatic updates on code commits. 

- Implement automated testing and validation within the pipeline. For example, you can create a script to automatically run the Terraform `validate` and `plan` commands. 

- Store the configurations as artifacts and enable versioning. 

- Define separate environments, such as dev, staging, and prod, with distinct configurations in version control and automate environment promotion. 

#### Validate model behavior

To maintain model accuracy and relevance over time, automate the training and evaluation process within your MLOps platform. This automation, coupled with rigorous validation, helps to ensure that the models behave as expected with relevant data before they're deployed to production. 

- Set up continuous training pipelines, which are either triggered by new data and monitoring signals like data drift or that run on a schedule. 

   - To manage automated training jobs, such as hyperparameter tuning trials and distributed training configurations for larger models, use Agent Platform custom training 

   - (/gemini-enterprise-agent-platform/machine-learning/training/create-custom-job). 

   - For fine-tuning foundation models, automate the fine-tuning process and integrate the jobs into your pipelines. 

- Implement automated model versioning and securely store trained model artifacts after each successful training run. You can store the artifacts in Cloud Storage or register them in Model Registry 

- (/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction). 

- Define evaluation metrics and set clear thresholds, such as minimum accuracy, maximum error rate, and minimum F1 score. 

   - Ensure that a model meets the thresholds to automatically pass the evaluation and be considered for deployment. 

   - Automate evaluation by using services like model evaluation in Agent Platform 

   - (/gemini-enterprise-agent-platform/machine-learning/evaluation/introduction). 

   - Ensure that the evaluation includes metrics that are specific to the quality of generated output, factual accuracy, safety attributes, and adherence to specified style or format. 

- To automatically log and track the parameters, code versions, dataset versions, and results of each training and evaluation run, use Experiments on Gemini Enterprise Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/experiments/intro-vertex-aiexperiments) 

- . This approach provides a history that's useful for comparison, debugging, and reproducibility. 

- To optimize hyperparameter tuning 

- (/gemini-enterprise-agent-platform/machine-learning/training/hyperparameter-tuningoverview) 

and automate searching for optimal model configurations based on your defined objective, use Agent Platform Vizier 

(/gemini-enterprise-agent-platform/machine-learning/vizier/overview). 

- To visualize training metrics and to debug during development, use Agent Platform TensorBoard 

- (/gemini-enterprise-agent-platform/machine-learning/experiments/tensorboardintroduction) 

#### Validate inputs and outputs of AI and ML pipelines

To ensure the reliability and integrity of your AI and ML systems, you must validate data when it enters the systems and moves through the pipelines. You must also verify the inputs and outputs at the component boundaries. Robust validation of all inputs and outputs—raw data, processed data, configurations, arguments, and files —helps to prevent unexpected behavior and maintain model quality throughout the MLOps lifecycle. When you integrate this proactive approach into your MLOps platform, it helps detect errors before they are propagated throughout a system and it saves time and resources. 

To effectively validate the inputs and outputs of your AI and ML pipelines, use the following techniques. 

Automate data validation 

- Implement automated data validation in your data ingestion and preprocessing pipelines by using TensorFlow Data Validation (TFDV) (https://www.tensorflow.org/tfx/data_validation). 

   - For large-scale, SQL-based data quality checks, leverage scalable processing services like BigQuery (/bigquery/docs/introduction). 

   - For complex, programmatic validation on streaming or batch data, use Dataflow (/dataflow/docs/overview). 

- Monitor data distributions over time with TFDV capabilities. 

   - Visualize trends by using tools that are integrated with Cloud Monitoring (/monitoring/docs/monitoring-overview) to detect data drift. You can automatically trigger model retraining pipelines when data patterns change significantly. 

- Store validation results and metrics in BigQuery for analysis and historical tracking and archive validation artifacts in Cloud Storage. 

Validate pipeline configurations and input data 

To prevent pipeline failures or unexpected behavior caused by incorrect settings, implement strict validation for all pipeline configurations and command-line arguments: 

- Define clear schemas for your configuration files like YAML or JSON by using schema validation libraries like jsonschema 

- (https://github.com/python-jsonschema/jsonschema) for Python. Validate configuration objects against these schemas before a pipeline run starts and before a component executes. 

- Implement input validation for all command-line arguments and pipeline parameters by using argument-parsing libraries like `argparse` (https://docs.python.org/3/library/argparse.html). Validation should check for correct data types, valid values, and required arguments. 

Within Agent Platform Pipelines 

- (/gemini-enterprise-agent-platform/machine-learning/pipelines/introduction), define the expected types and properties of component parameters by using the built-in component input validation features. 

- To ensure reproducibility of pipeline runs and to maintain an audit trail, store validated, versioned configuration files in Cloud Storage or Artifact Registry. 

Validate input and output files 

Validate input and output files such as datasets, model artifacts, and evaluation reports for integrity and format correctness: 

- Validate file formats like CSV, Parquet (https://parquet.apache.org/docs/overview/), and image types by using libraries. 

- For large files or critical artifacts, validate file sizes and checksums to detect corruption or incomplete transfers by using Cloud Storage data validation and change detection (/storage/docs/data-validation). 

- Perform file validation by using Cloud Run functions 

- (/functions/docs/concepts/overview) (for example, based on file upload events) or within Dataflow (/dataflow/docs/overview) pipelines. 

- Store validation results in BigQuery (/bigquery/docs/introduction) for easier retrieval and analysis. 

#### Automate deployment and implement continuous monitoring

Automated deployment and continuous monitoring of models in production helps to ensure reliability, perform rapid updates, and detect issues promptly. This involves managing model versions, controlled deployment, automated deployment using CI/CD, and comprehensive monitoring as described in the following sections. 

Manage model versions 

Manage model iterations and associated artifacts by using versioning tools: 

- To track model versions and metadata and to link to underlying model artifacts, use Model Registry 

- (/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction). 

- Implement a clear versioning scheme (such as, semantic versioning). For each model version, attach comprehensive metadata such as training parameters, evaluation metrics from validation pipelines, and dataset version. 

- Store model artifacts such as model files, pretrained weights, and serving container images in Artifact Registry (/artifact-registry/docs/overview) and use its versioning and tagging features. 

- To meet security and governance requirements, define stringent accesscontrol policies for Model Registry and Artifact Registry. 

- To programmatically register and manage versions and to integrate versions into automated CI/CD pipelines, use the Agent Platform SDK or API. 

Perform controlled deployment 

Control the deployment of model versions to endpoints by using your serving platform's traffic management capabilities. 

- Implement a rolling deployment 

- (/gemini-enterprise-agent-platform/machine-learning/predictions/rolling-deployment) by using the traffic splitting feature of Agent Platform endpoints. 

- If you deploy your model to GKE, use advanced traffic management techniques like canary deployment (/deploy/docs/deployment-strategies/canary): 

   1. Route a small subset of the production traffic to a new model version. 

   2. Continuously monitor performance and error rates through metrics. 

   3. Establish that the model is reliable. 

   4. Roll out the version to all traffic. 

- Perform A/B testing (https://en.wikipedia.org/wiki/A/B_testing) of AI agents: 

   1. Deploy two different model-agent versions or entirely different models to the same endpoint. 

   2. Split traffic across the deployments. 

   3. Analyze the results against business objectives. 

- Implement automated rollback mechanisms that can quickly revert endpoint traffic to a previous stable model version if monitoring alerts are triggered or performance thresholds are missed. 

- Configure traffic splitting and deployment settings programmatically by using the Agent Platform SDK or API. 

- Use Cloud Monitoring (/monitoring/docs/monitoring-overview) to track performance and traffic across versions. 

- Automate deployment with CI/CD pipelines. You can use Cloud Build (/build/docs/overview) to build containers, version artifacts, and trigger deployment to Agent Platform endpoints. 

- Ensure that the CI/CD pipelines manage versions and pull from Artifact Registry. 

- Before you shift traffic, perform automated endpoint testing for prediction correctness, latency, throughput, and API function. 

- Store all configurations in version control. 

Monitor continuously 

- Use Model Monitoring on Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/model-monitoring/overview) to automatically detect performance degradation, data drift (changes in input distribution compared to training), and prediction drift (changes in model outputs). 

   - Configure drift detection jobs with thresholds and alerts. 

   - Monitor real-time performance: prediction latency, throughput, error rates. 

- Define custom metrics in Cloud Monitoring (/monitoring/docs/monitoring-overview) for business KPIs. 

- Integrate Model Monitoring on Agent Platform results and custom metrics with Cloud Monitoring for alerts and dashboards. 

- Configure notification channels like email, Slack, or PagerDuty and configure automated remediation. 

- To debug prediction logs, use Cloud Logging (/logging/docs/overview). 

- Integrate monitoring with incident management. 

For generative AI endpoints, monitor output characteristics like toxicity and coherence: 

- Monitor feature serving for drift. 

- Implement granular prediction validation: validate outputs against expected ranges and formats by using custom logic. 

- Monitor prediction distributions for shifts. 

- Validate output schema. 

- Configure alerts for unexpected outputs and shifts. 

- Track and respond to real-time validation events by using Pub/Sub (/pubsub/docs/overview). 

Ensure that the output of comprehensive monitoring feeds back into continuous training. 

### Maintain trust and control through data and model governance

AI and ML reliability extends beyond technical uptime. It includes trust and robust data and model governance. AI outputs might be inaccurate, biased, or outdated. Such issues erode trust and can cause harm. Comprehensive traceability, strong access control, automated validation, and transparent practices help to ensure that AI outputs are reliable, trustworthy, and meet ethics standards. 

To maintain trust and control through data and model governance, consider the following recommendations. 

#### Establish data and model catalogs for traceability

To facilitate comprehensive tracing, auditing, and understanding the lineage of your AI and ML assets, maintain a robust, centralized record of data and model versions throughout their lifecycle. A reliable data and model catalog serves as the single source of truth for all of the artifacts that are used and produced by your AI and ML pipelines–from raw data sources and processed datasets to trained model versions and deployed endpoints. 

Use the following products, tools, and techniques to create and maintain catalogs for your data assets: 

- Build an enterprise-wide catalog of your data assets by using Knowledge Catalog (/dataplex/docs/catalog-overview). To automatically discover and build inventories of the data assets, integrate Knowledge Catalog with your storage systems, such as BigQuery (/bigquery/docs/introduction), Cloud Storage (/storage/docs/introduction), and Pub/Sub (/pubsub/docs/overview). 

- Ensure that your data is highly available and durable by storing it in Cloud Storage multi-region or dual-region buckets 

- (/storage/docs/locations#considerations). Data that you upload to these buckets is stored redundantly across at least two separate geographic locations. This redundancy provides built-in resilience against regional outages and it helps to ensure data integrity. 

- Tag and annotate your datasets with relevant business metadata, ownership information, sensitivity levels, and lineage details. For example, link a 

processed dataset to its raw source and to the pipeline that created the dataset. 

- Create a central repository for model versions by using Model Registry (/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction). Register each trained model version and link it to the associated metadata. The metadata can include the following: 

   - Training parameters. 

   - Evaluation metrics from validation pipelines. 

   - Dataset version that was used for training, with lineage traced back to the relevant Knowledge Catalog entry. 

   - Code version that produced the dataset. 

   - Details about the framework or foundation model that was used. 

- Before you import a model into Model Registry, store model artifacts like model files and pretrained weights in a service like Cloud Storage. Store custom container images for serving or custom training jobs in a secure repository like Artifact Registry (/artifact-registry/docs/overview). 

- To ensure that data and model assets are automatically registered and updated in the respective catalogs upon creation or modification, implement automated processes within your MLOps pipelines. This comprehensive cataloging provides end-to-end traceability from raw data to prediction, which lets you audit the inputs and processes that led to a specific model version or prediction. The auditing capability is vital for debugging unexpected behavior, ensuring compliance with data usage policies, and understanding the impact of data or model changes over time. 

- For Generative AI and foundation models, your catalog must also track details about the specific foundation model used, fine-tuning parameters, and evaluation results that are specific to the quality and safety of the generated output. 

#### Implement robust access controls and audit trails

To maintain trust and control in your AI and ML systems, it's essential that you protect sensitive data and models from unauthorized access and ensure 

accountability for all changes. 

- Implement strict access controls and maintain detailed audit trails across all components of your AI and ML systems in Google Cloud. 

- Define granular permissions in IAM for users, groups, and service accounts that interact with your AI and ML resources. 

- Follow the principle of least privilege rigorously. 

- Grant only the minimum necessary permissions for specific tasks. For example, a training service account needs read access to training data and write access for model artifacts, but the service might not need write access to production serving endpoints. 

Apply IAM policies consistently across all relevant assets and resources in your AI and ML systems, including the following: 

- Cloud Storage buckets that contain sensitive data or model artifacts. BigQuery datasets. 

- Agent Platform resources, such as model repositories, endpoints, pipelines, and Feature Store resources. 

- Compute resources, such as GKE clusters and Cloud Run services. 

Use auditing and logs to capture, monitor, and analyze access activity: 

- Enable Cloud Audit Logs (/logging/docs/audit) for all of the Google Cloud services that are used by your AI and ML system. 

- Configure audit logs to capture detailed information about API calls, data access events, and configuration changes made to your resources. Monitor the logs for suspicious activity, unauthorized access attempts, or unexpected modifications to critical data or model assets. 

- For real-time analysis, alerting, and visualization, stream the audit logs to Cloud Logging (/logging/docs/overview). 

- For cost-effective long-term storage and retrospective security analysis or compliance audits, export the logs to BigQuery. 

- For centralized security monitoring, integrate audit logs with your security information and event management (SIEM) systems. Regularly review access policies and audit trails to ensure they align with your governance requirements and detect potential policy violations. 

- For applications that handle sensitive data, such as personally identifiable information (PII) for training or inference, use Sensitive Data Protection (/sensitive-data-protection/docs/sensitive-data-protection-overview) checks within pipelines or on data storage. 

- For generative AI and agentic solutions, use audit trails to help track who accessed specific models or tools, what data was used for fine-tuning or prompting, and what queries were sent to production endpoints. The audit trails help you to ensure accountability and they provide crucial data for you to investigate misuse of data or policy violations. 

#### Address bias, transparency, and explainability

To build trustworthy AI and ML systems, you need to address potential biases that are inherent in data and models, strive for transparency in system behavior, and provide explainability for model outputs. It's especially crucial to build trustworthy systems in sensitive domains or when you use complex models like those that are typically used for generative AI applications. 

- Implement proactive practices to identify and mitigate bias throughout the MLOps lifecycle. 

- Analyze training data for bias by using tools that detect skew in feature distributions across different demographic groups or sensitive attributes. 

- Evaluate the overall model performance and the performance across predefined slices of data. Such evaluation helps you to identify disparate performance or bias that affects specific subgroups. 

For model transparency and explainability, use tools that help users and developers understand why a model made a particular prediction or produced a specific output. 

- For tabular models that are deployed on Agent Platform endpoints, generate feature attributions 

(/gemini-enterprise-agent-platform/machine-learning/tabular-data/classificationexplanations) 

- , which indicate the input features that contributed most to the prediction. 

- Interactively explore model behavior and potential biases on a dataset by using model-agnostic tools like the What-If Tool 

- (https://pair-code.github.io/what-if-tool/), which integrates with TensorBoard. 

- Integrate explainability into your monitoring dashboards. In situations where understanding the model's reasoning is important for trust or decisionmaking, provide explainability data directly to end users through your application interfaces. 

- For complex models like LLMs that are used for generative AI models, explain the _process_ that an agent followed, such as by using trace logs 

- (/gemini-enterprise-agent-platform/scale/runtime/tracing). Explainability is relatively challenging for such models, but it's still vital. 

- In RAG applications, provide citations for retrieved information. You can also use techniques like prompt engineering to guide the model to provide explanations or show its reasoning steps. 

- Detect shifts in model behavior or outputs that might indicate emerging bias or unfairness by implementing continuous monitoring in production. Document model limitations, intended use cases, and known potential biases as part of the model's metadata in the Model Registry 

- (/gemini-enterprise-agent-platform/machine-learning/model-registry/introduction).
