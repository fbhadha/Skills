# Architecture: Well-Architected Framework and reference designs / Multi-agent AI system in Google Cloud
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 469-495, extracted 2026-10-18

## Multi-agent AI system in Google Cloud

URL: https://docs.cloud.google.com/architecture/multiagent-ai-system

Last reviewed 2026-10-09 UTC 

This document provides a reference architecture to help you design robust multiagent AI systems in Google Cloud. A multi-agent AI system optimizes complex and dynamic processes by segmenting them into discrete tasks that multiple specialized AI agents collaboratively execute. 

The intended audience for this document includes architects, developers, and administrators who build and manage AI infrastructure and applications in the cloud. This document assumes a foundational understanding of AI agents and models. The document doesn't provide specific guidance for designing and coding AI agents. 

The Deployment (#deployment) section of this document lists code samples that you can use to learn how to build and deploy multi-agent AI systems. 

### Architecture

The following diagram shows an architecture for an example of a multi-agent AI system that's deployed in Google Cloud. 

#### Architecture components

The example architecture in the preceding section contains the following components: 

**Frontend** 

Users interact with the multi-agent system through a frontend, such as a chat interface, that runs as a serverless Cloud Run 

(/run/docs/overview/what-is-cloud-run) service. 

**Agents** 

A coordinator agent controls the agentic AI system in this example. The coordinator agent invokes an appropriate subagent to trigger the agentic flow. The agents can communicate with each other by using the Agent2Agent (A2A) protocol (https://a2a-protocol.org/latest/), which enables interoperability between agents regardless of their programming language and runtime. The example architecture shows agents in a sequential pattern 

(/architecture/choose-design-pattern-agentic-ai-system#sequential-pattern) and an iterative refinement pattern 

(/architecture/choose-design-pattern-agentic-ai-system#iterative-refinement-pattern). 

For more information about the subagents in this example, see the Agentic flow (#agentic-flow) section. 

**Agents runtime** 

AI agents can be deployed as serverless Cloud Run services (/run/docs/ai-agents) , as containerized apps on Google Kubernetes Engine (GKE) 

(/kubernetes-engine/docs/tutorials/agentic-adk-vertex), or on Agent Runtime on Gemini Enterprise Agent Platform (/gemini-enterprise-agent-platform/build/runtime). 

**ADK** 

Agent Development Kit (ADK) (https://google.github.io/adk-docs/) provides tools and a framework to develop, test, and deploy agents. ADK abstracts the complexity of agent creation and lets AI developers focus on the agent's logic and capabilities. 

**AI model and model runtimes** 

For inference serving, the agents in this example architecture use an AI model on Gemini Enterprise Agent Platform 

(/gemini-enterprise-agent-platform/agents/quickstart-adk). The architecture shows Cloud Run (/run/docs/configuring/services/gpu-best-practices) and GKE (/kubernetes-engine/docs/concepts/machine-learning/inference) as alternative runtimes for the AI model that you choose to use. 

**Model Armor** 

Model Armor enables inspection and sanitization of inputs and responses for models that are deployed in Agent Platform and GKE. Model Armor can also be used for agent and tool traffic that is routed through Agent Gateway (/gemini-enterprise-agent-platform/govern/configure-model-armor). For more information, see Model Armor integration with Google Cloud services (/model-armor/integrations). 

**MCP clients, servers, and tools** 

The Model Context Protocol (MCP) 

(https://modelcontextprotocol.io/docs/getting-started/intro) facilitates access to tools by standardizing the interaction between agents and tools. For each agenttool pair, an MCP client sends requests to an MCP server through which the agent accesses a tool such as a database, a file system, or an API. 

#### Agentic flow

The example multi-agent system in the preceding architecture has the following flow: 

1. A user enters a prompt through a frontend, such as a chat interface, which runs as a serverless Cloud Run service. 

2. The frontend forwards the prompt to a coordinator agent. 

3. The coordinator agent starts one of the following agentic flows based on the intent that's expressed in the prompt. 

**Sequential** : 

- a. The task-A subagent performs a task. 

- b. The task-A subagent invokes the task-A.1 subagent. 

**Iterative refinement** : 

- a. The task-B subagent performs a task. 

- b. The quality evaluator subagent reviews the output of the task-B subagent. 

- c. If the output is unsatisfactory, the quality evaluator invokes the prompt enhancer subagent to refine the prompt. 

- d. The task-B subagent performs its task again by using the enhanced prompt. 

This cycle continues until the output is satisfactory or the maximum number of iterations is reached. 

The example architecture includes a human-in-the-loop 

(/architecture/choose-design-pattern-agentic-ai-system#human-in-the-loop-pattern) path to let human users intervene in the agentic flow when necessary. 

4. The task-A.1 subagent and quality evaluator subagent independently invoke the response generator subagent. 

5. The response generator subagent generates a response, performs validation and grounding checks, and then it sends the final response to the user through the coordinator agent. 

### Products and tools used

This reference architecture uses the following Google Cloud and third-party products and tools: 

- Cloud Run (https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure. 

- Gemini Enterprise Agent Platform (/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 

- Google Kubernetes Engine (GKE) (https://cloud.google.com/kubernetes-engine): A Kubernetes service that you can use to deploy and operate containerized applications at scale using Google's infrastructure. 

- Model Armor (https://cloud.google.com/security/products/model-armor): A service that provides protection for your generative and agentic AI resources against prompt injection, sensitive data leaks, and harmful content. 

- Agent Development Kit (ADK) (https://adk.dev/): A set of tools and libraries to develop, test, and deploy AI agents. 

- Agent2Agent (A2A) protocol (https://a2a-protocol.org/latest/): An open protocol that enables communication and interoperability between agents regardless of their programming language and runtime. 

- Model Context Protocol (MCP) 

(https://modelcontextprotocol.io/docs/getting-started/intro): An open-source standard for connecting AI applications to external systems. 

### Use cases

Multi-agent AI systems are suitable for complex use cases that require collaboration and coordination across multiple specialized skill sets to achieve a business goal. To identify use cases that multi-agent AI systems are suitable for, analyze your business processes and identify specific tasks that AI can augment. Focus on tangible business outcomes, like cost reduction and accelerated processing. This approach helps align your investments in AI with business value. 

The following are examples of use cases for multi-agent AI systems. 

#### Financial advisor

Provide personalized stock trading recommendations and execute trades. The following diagram shows an example of an agentic flow for this use case. This example uses a sequential pattern. 

The diagram shows the following flow: 

1. A data retriever agent retrieves real-time and historical stock prices, company financial reports, and other relevant data from reliable sources. 

2. A financial analyzer agent applies appropriate analytics and charting techniques to the data, identifies price movement patterns, and makes predictions. 

3. A stock recommender agent uses the analysis and charts to generate personalized recommendations to buy and sell specific stocks based on the user's risk profile and investment goals. 

4. A trade executor agent buys and sells stocks on behalf of the user. 

#### Research assistant

Create a research plan, gather information, evaluate and refine the research, and then compose a report. The following diagram shows an example of an agentic flow for this use case. The main flow in this example uses a sequential pattern. The example also includes an iterative refinement pattern. 

The diagram shows the following flow: 

1. A planner agent creates a detailed research plan. 

2. A researcher agent completes the following tasks: 

   - a. Uses the research plan to identify appropriate internal and external data sources. 

   - b. Gathers and analyzes the required data. 

   - c. Prepares a research summary and provides the summary to an evaluator agent. 

The researcher agent repeats these tasks until the evaluator agent approves the research. 

3. A report composer agent creates the final research report. 

#### Supply chain optimizer

Optimize inventory, track shipments, and communicate with supply chain partners. The following diagram shows an example of an agentic flow for this use case. This example uses a sequential pattern. 

1. A warehouse manager agent ensures optimal stock levels by creating re-stock orders based on inventory, demand forecasts, and supplier lead times. 

   - The agent interacts with the shipment tracker agent to track deliveries. The agent interacts with the supplier communicator agent to notify suppliers about changes in orders. 

2. A shipment tracker agent ensures timely and efficient fulfillment of orders by integrating with suppliers' logistics platforms and carrier systems. 

3. A supplier communicator agent communicates with external suppliers on behalf of the other agents in the system. 

### Design alternatives

Depending on your requirements for manageability, control, and flexibility, you can choose from a range of runtime options in Google Cloud for your AI agents and model. For more information, see Choose your agentic AI architecture components (/architecture/choose-agentic-ai-architecture-components). 

### Design considerations

This section describes design factors, best practices, and recommendations to consider when you use this reference architecture to develop a topology that meets your specific requirements for security, reliability, cost, and performance. 

The guidance in this section isn't exhaustive. Depending on your workload's requirements and the Google Cloud and third-party products and features that you 

use, there might be additional design factors and trade-offs that you should consider. 

#### System design

This section provides guidance to help you choose Google Cloud regions for your deployment and to select appropriate Google Cloud products and tools. 

Region selection 

When you select Google Cloud regions for your AI applications, consider the following factors: 

Availability of Google Cloud services 

(https://cloud.google.com/about/locations#products-available-by-location) in each region. 

End-user latency 

- (/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloudlatency#global-latency) 

requirements. 

Cost (https://cloud.google.com/products/calculator) of Google Cloud resources. 

- Regulatory requirements. 

To select appropriate Google Cloud locations for your applications, use the following tools: 

- Google Cloud Region Picker (https://cloud.withgoogle.com/region-picker/): An interactive web-based tool to select the optimal Google Cloud region for your applications and data based on factors like carbon footprint, cost, and latency. 

- Cloud Location Finder API (/location-finder/docs/overview): A public API that provides a programmatic way to find deployment locations in Google Cloud, Google Distributed Cloud, and other cloud providers. 

Agent design 

This section provides general recommendations for designing AI agents. Detailed guidance about writing agent code and logic is outside the scope of this document. 

**Agent definition and design** : 

- Clearly define the business goal of the agentic AI system and the task that each agent performs. 

- Choose an agent design pattern 

- (/architecture/choose-design-pattern-agentic-ai-system) that best meets your requirements. 

- Use ADK to efficiently create, deploy, and manage your agentic architecture. 

**Agent interactions** : 

- Design the human-facing agents in the architecture to support natural language interactions. 

- Ensure that each agent clearly communicates its actions and status to its dependent clients. 

- Design the agents to detect and handle ambiguous queries and nuanced interactions. 

**Context, tools, and data** : 

- Ensure that the agents have sufficient context 

- (https://google.github.io/adk-docs/context/) to track multi-turn interactions and session parameters. 

- Clearly describe the purpose, arguments, and usage of the tools that the agents can use. 

- Ensure that the agents' responses are grounded in reliable data sources to reduce hallucinations. 

- Implement logic to handle no-match situations, such as when a prompt is off-topic. 

#### Security

This section describes design considerations and recommendations to design a topology in Google Cloud that meets your workload's security requirements. 

Security considerations for agents 

AI agents introduce certain unique and critical security risks that conventional, deterministic security practices might not be able to mitigate adequately. Google recommends an approach 

(https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) that combines the strengths of deterministic security controls with dynamic, reasoningbased defenses. This approach is grounded in three core principles: human oversight, carefully defined agent autonomy, and observability. The following are specific recommendations that are aligned with these core principles. 

- **Human oversight** : An agentic AI system might sometimes fail or not perform as expected. For example, the model might generate inaccurate content or an agent might select inappropriate tools. In business-critical agentic AI systems, incorporate a human-in-the-loop flow to let human supervisors monitor, override, and pause agents. For example, human users can review the output of agents, approve or reject the outputs, and provide further guidance to correct errors or to make strategic decisions. This approach combines the efficiency of agentic AI systems with the critical thinking and domain expertise of human users. 

**Agent identity and least-privilege access** : 

- Provide each agent a workload-bound, SPIFFE 

- (https://spiffe.io/docs/latest/spiffe-about/overview)-based identity by using Agent Identity 

- (/gemini-enterprise-agent-platform/govern/agent-identity-overview). You can use Agent Identity when you deploy agents to Agent Runtime 

- (/gemini-enterprise-agent-platform/scale/runtime/agent-identity) or to Cloud Run 

- (/run/docs/ai/agent-platform-features). 

- Configure per-agent permissions by using Identity and Access Management (IAM) access policies 

- (/gemini-enterprise-agent-platform/govern/policies/iam-overview-uap) and Agent Platform access control with IAM 

- (/gemini-enterprise-agent-platform/machine-learning/general/access-control). Grant each agent only the permissions that it needs to perform its tasks and to communicate with tools and with other agents. To further isolate each agent and limit the potential impact of a security breach, bind 

Principal Access Boundary (PAB) (/iam/docs/principal-access-boundary-policies) policies to the agent identity. 

   - When agents need to authenticate to external tools or to third-party APIs, use the Agent Identity auth manager (/iam/docs/auth-manager-overview). With this approach, you can centrally control OAuth tokens and API keys instead of having to embed credentials within agent code or prompts. 

- **Ingress and egress traffic governance** : Route agent traffic through Agent Gateway (/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) to enforce runtime security policies at both the ingress and egress boundaries. For information about the runtime platforms that support Agent Gateway, see 

Supported agent runtimes 

(/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview#agentruntimes) 

**Client-to-Agent (ingress)** : Deploy Agent Gateway 

- (/gemini-enterprise-agent-platform/scale/runtime/agent-gateway-runtime-deploy) in front of your agent runtime. The gateway helps to authenticate callers and inspect inbound prompts in real time by using Model Armor 

- (/gemini-enterprise-agent-platform/govern/configure-model-armor). 

**Agent-to-Anywhere (egress)** : 

   - Route outbound agent-to-agent (A2A) and agent-to-tool (MCP) requests through Agent Gateway in egress mode. 

   - Enforce default-deny access policies by using IAM access policies and Identity-Aware Proxy (IAP) (/iap/docs/agent-overview). 

   - Verify that target agents and tools are registered in Agent Registry (/agent-registry/overview). 

   - Inspect outbound tool invocations and responses with Model Armor to help prevent data exfiltration, indirect prompt injection, and tool misuse. 

- **Monitoring** : Monitor agent behavior by using comprehensive tracing capabilities that give you visibility into every action that an agent takes, including its reasoning process, tool selection, and execution paths. For more information, see Logging an agent in Agent Runtime 

(/gemini-enterprise-agent-platform/scale/runtime/logging) and Logging in ADK (https://google.github.io/adk-docs/observability/logging/). 

For more information about securing AI agents, see Safety and Security for AI Agents (https://google.github.io/adk-docs/safety/). 

Agent Platform security considerations 

To help ensure that your Agent Platform configurations and usage meet your security requirements, consider the following recommendations: 

- **Shared responsibility** : Security is a shared responsibility. Agent Platform secures the underlying infrastructure and provides tools and security controls to help you protect your data, code, and models. You are responsible for properly configuring your services, managing access controls, and securing your applications. For more information, see Agent Platform shared responsibility 

(/gemini-enterprise-agent-platform/machine-learning/shared-responsibility). 

- **Security controls** : Agent Platform supports Google Cloud security controls that you can use to meet your requirements for data residency, customermanaged encryption keys (CMEK) 

- (/gemini-enterprise-agent-platform/machine-learning/general/cmek), network security using VPC Service Controls 

(/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls), and Access Transparency (/assured-workloads/access-transparency/docs/overview). For more information, see the following documentation: 

Security controls for Agent Platform 

- (/gemini-enterprise-agent-platform/machine-learning/security-controls) 

- Security controls for Generative AI 

- (/gemini-enterprise-agent-platform/models/security-controls) 

Agent Platform and zero data retention 

   - (/gemini-enterprise-agent-platform/resources/zero-data-retention) 

- **Safety** : AI models might produce harmful responses, sometimes in response to malicious prompts. 

   - To enhance safety and mitigate potential misuse of the agentic AI system, you can configure content filters to act as barriers to harmful inputs and responses. For more information, see Safety and content filters 

   - (/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters). 

   - To inspect and sanitize inference requests, agent prompts, tool calls, and responses for threats like prompt injection and harmful content, you can use Model Armor (/model-armor/overview) for direct model API calls _and_ for requests that are routed through Agent Gateway 

   - (/gemini-enterprise-agent-platform/govern/configure-model-armor). Model Armor helps you prevent malicious input, verify content safety, protect sensitive data, maintain compliance, and enforce safety and security policies consistently. 

- **Model access** : You can set up organization policies to limit the type and versions of AI models that can be used in a Google Cloud project. For more information, see Control access to Model Garden models 

- (/gemini-enterprise-agent-platform/models/control-model-access). 

- **Data protection** : To discover and de-identify sensitive data in the prompts and responses and in log data, use the Cloud Data Loss Prevention API (/sensitive-data-protection/docs/apis). For more information, see this video: Protecting sensitive data in AI apps 

- (https://www.youtube.com/watch?v=ct1nuLS-wlA). 

MCP security considerations 

To help ensure that your MCP implementation meets your security requirements, consider the following recommendations: 

- **Tool registration and discovery** : Register MCP servers and tools in Agent Registry (/agent-registry/register-mcp-servers) so that agents only connect to inventoried, administrator-approved MCP endpoints. 

- **Access control and traffic inspection** : Route agent-to-MCP traffic through Agent Gateway in **Agent-to-Anywhere (egress)** mode and protect MCP servers (such as MCP servers hosted on Cloud Run) by using IAP (/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp) and IAM access policies. Configure Model Armor or semantic governance policies on Agent 

Gateway to inspect MCP tool inputs and outputs for sensitive data exposure and indirect prompt injection. 

- **General MCP security** : When you configure your agents to use MCP, ensure that access to external data and tools is authorized, implement privacy controls like encryption, apply filters to protect sensitive data, and monitor agent interactions. For more information, see MCP and security 

(https://cloud.google.com/discover/what-is-model-context-protocol#mcp-and-security). 

A2A security considerations 

To help ensure that your A2A implementation meets your security requirements, consider the following recommendations: 

- **Transport security** : The A2A protocol mandates HTTPS for all A2A communication in production environments and it recommends Transport Layer Security (TLS) 

- (https://a2a-protocol.org/latest/topics/enterprise-ready/#transport-level-security-tls) versions 1.2 or higher. 

- **Authentication** : The A2A protocol delegates authentication to standard web mechanisms like HTTP headers and to standards like OAuth2 and OpenID Connect. Each agent advertises the authentication requirements in its Agent Card. For more information, see A2A authentication 

(https://a2a-protocol.org/latest/topics/enterprise-ready/#authentication). 

**Inter-agent governance** : Register A2A agents in Agent Registry 

(/agent-registry/register-agents) and route inter-agent requests through Agent Gateway. By combining Agent Gateway with Agent Identity, IAP, and IAM access policies, you can cryptographically verify the calling agent's identity, enforce fine-grained authorization between coordinator agents and subagents, and inspect inter-agent payloads with Model Armor. 

Cloud Run security considerations 

To help ensure that your Cloud Run implementation meets your security requirements, consider the following recommendations: 

**Ingress security (for the frontend service)** : To control access to the application, disable the default `run.app` URL 

(/run/docs/securing/ingress#disable-url) of the frontend Cloud Run service and set up a regional external Application Load Balancer 

(/load-balancing/docs/https/setting-up-reg-ext-https-serverless). In addition to loadbalancing incoming traffic to the application, the load balancer handles SSL certificate management. For added protection, you can use Google Cloud Armor security policies (/armor/docs/integrating-cloud-armor#serverless) to provide request filtering, DDoS protection, and rate limiting for the service. 

**User authentication** : 

- **Users inside your organization** : To authenticate internal user access to the frontend Cloud Run service, use IAP. When a user tries to access an IAP-secured resource, IAP performs authentication and authorization checks. 

- **Users outside your organization** : To authenticate external user access to the frontend service, use Identity Platform 

- (/identity-platform/docs) or Firebase Authentication 

- (https://firebase.google.com/docs/auth). To manage external user access, configure your application to handle a sign-in flow and to make authenticated API calls to the Cloud Run service. 

For more information, see Authenticating users 

- (/run/docs/authenticating/end-users). 

- **Agent and MCP server security** : When you host agents or MCP servers on Cloud Run, configure Agent Platform features for Cloud Run 

- (/run/docs/ai/agent-platform-features) to assign a managed agent identity to the service, and use IAP 

- (/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp) with Agent Gateway to authenticate and authorize inbound agent and tool requests. 

- **Container image security** : To ensure that only authorized container images are deployed to Cloud Run, you can use Binary Authorization 

- (/binary-authorization/docs/run/overview). To identify and mitigate security risks in the container images, use Artifact Analysis to automatically run vulnerability scans. For more information, see Container scanning overview 

- (/artifact-analysis/docs/container-scanning-overview). 

- **Data residency** : Cloud Run helps you meet data residency requirements. Your Cloud Run services run within the selected region 

(/docs/geography-and-regions#regions_and_zones). 

For more guidance about container security, see General Cloud Run development tips (/run/docs/tips/general#container-security). 

Security considerations for all of the Google Cloud products in the architecture 

To help ensure that your architecture meets your security requirements, consider the following general recommendations: 

- **Data encryption** : By default, Google Cloud encrypts data at rest by using Google-owned and Google-managed encryption keys. To protect your agents' data by using encryption keys that you control, you can use CMEKs (/kms/docs/cmek) that you create and manage in Cloud KMS. For information about Google Cloud services that are compatible with Cloud KMS, see Compatible services (/kms/docs/compatible-services). 

- **Mitigate data exfiltration risk** : To reduce the risk of data exfiltration, create a VPC Service Controls (/vpc-service-controls/docs/overview) perimeter around the infrastructure. VPC Service Controls supports all of the Google Cloud services that this reference architecture uses. 

- **Access control** : When you configure permissions for the resources in your topology, follow the principle of least privilege 

- (/iam/docs/using-iam-securely#least_privilege). 

- **Cloud environment security** : Use the tools in Security Command Center (/security-command-center/docs/security-command-center-overview) to detect vulnerabilities, identify and mitigate threats, define and deploy a security posture, and export data for further analysis. 

- **Post-deployment optimization** : After you deploy your application in Google Cloud, get recommendations to further optimize security by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see Find recommendations in Active Assist (/recommender/docs/active-assist/find-recommendations). 

More security recommendations 

- Google Cloud Well-Architected Framework AI and ML perspective: Security (/architecture/framework/perspectives/ai-ml/security) 

- Google's Approach for Secure AI Agents: An Introduction (https://storage.googleapis.com/gweb-research2023-media/pubtools/1018686.pdf) 

#### Reliability

This section describes design considerations and recommendations to build and operate reliable infrastructure for your deployment in Google Cloud. 

Reliability considerations for agents 

To help ensure that your agent configurations meet your reliability requirements, consider the following recommendations: 

- **Fault tolerance** : Design the agentic system to tolerate or handle agent-level failures. Where feasible, use a decentralized approach where agents can operate independently. 

- **Simulate failures** : Before deploying the agentic AI system to production, validate it by simulating a production environment. Identify and fix inter-agent coordination issues and unexpected behaviors. 

- **Error handling** : To enable diagnosis and troubleshooting of errors, implement logging, exception handling, and retry mechanisms. 

Agent Platform reliability considerations 

To help ensure that your Agent Platform configurations and usage meet your reliability requirements, consider the following recommendations: 

- **Capacity planning** : If the number of your requests exceeds the allocated capacity, then error code 429 

(/gemini-enterprise-agent-platform/models/standard-paygo#resource-exhausted-429errors) 

is returned. For workloads that are business critical and consistently require high throughput, you can reserve throughput by using Provisioned Throughput (/gemini-enterprise-agent-platform/models/provisioned-throughput). 

- **Model endpoint availability** : If data can be shared across multiple regions or countries, you can use a global endpoint 

(/gemini-enterprise-agent-platform/resources/locations#global-endpoint) for the model. 

Cloud Run robustness to zone and region outages 

Cloud Run is a regional service. It stores data synchronously across multiple zones within a region and it automatically load-balances traffic across the zones. If a zone outage occurs, Cloud Run continues to run and data isn't lost. If a region outage occurs, the service stops running until Google resolves the outage. 

Reliability considerations for all of the Google Cloud products in the architecture 

After you deploy your application in Google Cloud, get recommendations to further optimize reliability by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see Find recommendations in Active Assist 

(/recommender/docs/active-assist/find-recommendations). 

For reliability principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Reliability 

(/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

#### Operations

This section describes the factors to consider when you use this reference architecture to design a Google Cloud topology that you can operate efficiently. 

Agent Platform operations considerations 

To help ensure that your Agent Platform configurations and usage meet your operational requirements, consider the following recommendations: 

**Monitoring using logs** : By default, agent logs that are written to the `stdout` and `stderr` streams are routed to Cloud Logging. For advanced logging, you can integrate the Python logger with Cloud Logging. If you need full control 

over logging and structured logs, use the Cloud Logging client. For more information, see Logging an agent 

- (/gemini-enterprise-agent-platform/scale/runtime/logging) and Logging in ADK (https://google.github.io/adk-docs/observability/logging/). 

- **Continuous evaluation** : Regularly perform a qualitative evaluation of the output of the agents and the _trajectory_ or steps taken by the agents to produce the output. To implement agent evaluation, you can use the Gen AI evaluation service 

- (/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation) or the evaluation methods that ADK supports 

(https://google.github.io/adk-docs/evaluate/#how-evaluation-works-with-adk). 

MCP operations considerations 

To help ensure that your MCP implementation meets your operational requirements, consider the following recommendations: 

- **Database tools** : To efficiently manage database tools for your AI agents and to ensure that the agents securely handle complexities like connection pooling and authentication, use the MCP Toolbox for Databases 

- (https://mcp-toolbox.dev/documentation/introduction/). It provides a centralized location to store and update database tools. You can share the tools across agents and update the tools without redeploying agents. The toolbox includes a wide range of tools for Google Cloud databases like AlloyDB for PostgreSQL and for third-party databases like MongoDB. 

- **Generative AI models** : To enable AI agents to use Google generative AI models like Imagen and Veo, you can use MCP Servers for Google Cloud generative media APIs 

(https://github.com/GoogleCloudPlatform/genmedia-creativestudio/tree/main/experiments/mcp-genmedia) 

- **Google security products and tools** : To enable your AI agents to access Google security products and tools like Google Security Operations, Google Threat Intelligence, and Security Command Center, use MCP servers for Google security products (https://google.github.io/mcp-security/). 

Operations considerations for all of the Google Cloud products in the architecture 

Continuously gather and analyze trace data by using Cloud Trace. Trace data lets you rapidly identify and diagnose errors within complex agent workflows. You can perform in-depth analysis through visualizations in the Trace Explorer tool. For more information, see View agent traces 

(/gemini-enterprise-agent-platform/optimize/observability/traces). 

For operational excellence principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Operational excellence 

(/architecture/framework/perspectives/ai-ml/operational-excellence) in the Well-Architected Framework. 

#### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build by using this reference architecture. 

Agent Platform cost considerations 

To help ensure that your Agent Platform configurations and usage meet your cost requirements, consider the following recommendations: 

- **Cost analysis and management** : To analyze and manage Agent Platform costs, we recommend that you create baseline metrics for queries per second (QPS) and tokens per second (TPS). Then, monitor these metrics after deployment. The baseline also helps with capacity planning. For example, the baseline helps you determine when Provisioned Throughput 

(/gemini-enterprise-agent-platform/models/provisioned-throughput) might be necessary. 

**Model selection** : The model 

(/gemini-enterprise-agent-platform/models/google-models) that you select for your AI application directly affects both costs and performance. To identify the model that provides an optimal balance between performance and cost for your specific use case, test models iteratively. We recommend that you start with the most cost-efficient model and progress gradually to more powerful options. 

- **Cost-effective prompting** : The length of your prompts (input) and the generated responses (output) directly affect performance and cost. Write prompts that are short, direct, and provide sufficient context. Design your prompts to get concise responses from the model. For example, include phrases such as "summarize in 2 sentences" or "list 3 key points". For more information, see the best practices for prompt design 

- (/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies#bestpractices) 

- **Context caching** : To reduce the cost of requests that contain repeated content with high input token counts, use context caching 

- (/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview). 

- **Batch requests** : When relevant, consider batch prediction 

- (/gemini-enterprise-agent-platform/models/capabilities/batch-inference). Batched requests incur a lower cost than standard requests. 

Cloud Run cost considerations 

To help ensure that your Cloud Run implementation meets your cost requirements, consider the following recommendations: 

- **Resource allocation** : When you create a Cloud Run service, you can specify the amount of memory and CPU to be allocated. Start with the default CPU and memory allocations. Observe the resource usage and cost over time, and adjust the allocation as necessary. For more information, see Configure memory limits for services (/run/docs/configuring/services/memory-limits) and Configure CPU limits for services (/run/docs/configuring/services/cpu) 

- **Rate optimization** : If you can predict the CPU and memory requirements, you can save money with committed use discounts (CUDs) (/run/cud). 

Cost considerations for all of the Google Cloud products in the architecture 

After you deploy your application in Google Cloud, get recommendations to further optimize cost by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see Find 

recommendations in Active Assist 

(/recommender/docs/active-assist/find-recommendations). 

To estimate the cost of your Google Cloud resources, use the Google Cloud Pricing Calculator (https://cloud.google.com/products/calculator). 

For cost optimization principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Cost optimization 

(/architecture/framework/perspectives/ai-ml/cost-optimization) in the Well-Architected Framework. 

#### Performance optimization

This section describes design considerations and recommendations to design a topology in Google Cloud that meets the performance requirements of your workloads. 

Performance considerations for agents 

To help ensure that your agent configurations meet your performance requirements, consider the following recommendations: 

- **Model selection** : When you select models for your agentic AI system, consider the capabilities that are required for the tasks that the agents need to perform. 

- **Prompt optimization** : To rapidly improve and optimize prompt performance at scale and to eliminate the need for manual rewriting, use the Agent Platform prompt optimizer 

(/gemini-enterprise-agent-platform/models/prompts/prompt-optimizer). The optimizer helps you efficiently adapt prompts across different models. 

Agent Platform performance considerations 

To help ensure that your Agent Platform configurations and usage meet your performance requirements, consider the following recommendations: 

- **Model selection** : The model 

- (/gemini-enterprise-agent-platform/models/google-models) that you select for your AI application directly affects both costs and performance. To identify the model that provides an optimal balance between performance and cost for your specific use case, test models iteratively. We recommend that you start with 

the most cost-efficient model and progress gradually to more powerful options. 

- **Prompt engineering** : The length of your prompts (input) and the generated responses (output) directly affect performance and cost. Write prompts that are short, direct, and provide sufficient context. Design your prompts to get concise responses from the model. For example, include phrases such as "summarize in 2 sentences" or "list 3 key points". For more information, see the best practices for prompt design 

- (/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies#bestpractices) 

- **Context caching** : To reduce latency for requests that contain repeated content with high input token counts, use context caching 

- (/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview). 

Cloud Run performance considerations 

Depending on your performance requirements, configure the memory and CPU to be allocated to the Cloud Run service. For more information, see Configure memory limits for services (/run/docs/configuring/services/memory-limits) and Configure CPU limits for services (/run/docs/configuring/services/cpu) 

For more performance optimization guidance, see General Cloud Run development tips (/run/docs/tips/general#optimize_performance). 

Performance considerations for all of the Google Cloud products in the architecture 

After you deploy your application in Google Cloud, get recommendations to further optimize performance by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see Find recommendations in Active Assist 

(/recommender/docs/active-assist/find-recommendations). 

For performance optimization principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Performance optimization 

(/architecture/framework/perspectives/ai-ml/performance-optimization) in the WellArchitected Framework. 

### Deployment

To learn how to build and deploy multi-agent AI systems, use the following code samples. These code samples are fully functional starting points for learning and experimentation. For optimal operation in production environments, you must customize the code based on your specific business and technical requirements. 

**Course creator** : Build structured educational courses. 

- Using Gemini and Gemma models 

(https://codelabs.developers.google.com/next26/multi-agent-system#0) 

Using a Gemini model 

(https://codelabs.developers.google.com/codelabs/production-ready-ai-roadshow/1building-a-multi-agent-system/building-a-multi-agent-system#0) 

**Financial advisor** 

(https://github.com/google/adk-recipes/tree/main/contrib/python/financial-advisor): Analyze stock market data, create trading strategies, define execution plans, and evaluate risks. 

**Research assistant** 

(https://github.com/google/adk-recipes/tree/main/core/python/deep-search): Plan and conduct research, evaluate the findings, and compose a research report. 

**Search optimizer** 

(https://github.com/google/adk-recipes/tree/main/contrib/python/brand-searchoptimization) 

: Find search keywords, analyze web pages, and provide suggestions to optimize search. 

**Airbnb planner** 

(https://github.com/a2aproject/a2asamples/tree/main/samples/python/agents/airbnb_planner_multiagent) 

( _with A2A and MCP_ ): For a given location and time, find Airbnb listings and get weather information. 

### What's next

- Choose a design pattern for your agentic AI system 

- (/architecture/choose-design-pattern-agentic-ai-system). 

- Explore sample agents and tools in Agent Garden 

- (https://console.cloud.google.com/agent-platform/agent-garden). 

- Build agents using ADK (https://google.github.io/adk-docs/agents/). 

- Deploy agents to Google Cloud (https://google.github.io/adk-docs/deploy/). 

- Host A2A agents on Cloud Run (/run/docs/ai/a2a-agents). 

- Host MCP servers on Cloud Run (/run/docs/host-mcp-servers). 

- For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the AI and ML perspective (/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 

- For more reference architectures, diagrams, and best practices, explore the Cloud Architecture Center (/architecture). 

### Contributors

Author: Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | CrossProduct Solution Developer 

Other contributors: 

- Alan Blount (https://www.linkedin.com/in/alanblount) | Product Manager 

- Ali Arsanjani, PhD (https://www.linkedin.com/in/ali-arsanjani) | Director, Applied AI Engineering 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Holt Skinner (https://www.linkedin.com/in/holt) | Developer Advocate 

- Jack Wotherspoon (https://www.linkedin.com/in/jack-wotherspoon) | Developer Advocate 

- Joe Shirey (https://www.linkedin.com/in/jshirey) | Cloud Developer Relations Manager 

- Megan O'Keefe (https://www.linkedin.com/in/askmeegs) | Developer Advocate 

- Samantha He (https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer 

- Sara Ford (https://www.linkedin.com/in/sarasford/) | Senior Developer Relations Engineer 

- Shir Meir Lador (https://www.linkedin.com/in/shirmeirlador) | Developer Relations Engineering Manager 

- Victor Dantas (https://www.linkedin.com/in/vicdan) | Gen AI Field Solutions Architect 

- Vlad Kolesnikov (https://www.linkedin.com/in/vkolesnikov) | Developer Relations Engineer 

Last updated 2026-10-09 UTC.
