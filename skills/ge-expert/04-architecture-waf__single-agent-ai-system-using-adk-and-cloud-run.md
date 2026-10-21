# Architecture: Well-Architected Framework and reference designs / Single-agent AI system using ADK and Cloud Run to Enterprise foundations blueprint
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 496-538, extracted 2026-10-18

Contains:
- Single-agent AI system using ADK and Cloud Run (pages 496-523) https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run
- Landing zone design in Google Cloud (pages 524-533) https://docs.cloud.google.com/architecture/landing-zones
- Enterprise foundations blueprint (pages 534-538) https://docs.cloud.google.com/architecture/blueprints/security-foundations

## Single-agent AI system using ADK and Cloud Run

URL: https://docs.cloud.google.com/architecture/single-agent-ai-system-adk-cloud-run

Last reviewed 2025-12-09 UTC 

This document provides a reference architecture to help you design a single-agent AI system on Google Cloud. The single-agent system in this architecture is built by using Agent Development Kit (ADK) and it's deployed on Cloud Run. You can also deploy the agent on Agent Runtime on Gemini Enterprise Agent Platform or Google Kubernetes Engine (GKE). The architecture uses Model Context Protocol (MCP) (https://modelcontextprotocol.io/docs/getting-started/intro), which enables the agent to access and process information from multiple sources so that it can provide context-rich insights. 

This document is intended for architects, developers, and administrators of AI applications. It assumes that you have a basic understanding of AI, machine learning (ML), and large language model (LLM) concepts. The document also assumes that you have a foundational understanding of AI agents and models. It doesn't provide specific guidance for designing and coding AI agents. 

The Deployment (#deployment) section of this document lists code samples that you can use to learn how to build and deploy single-agent AI systems. 

### Architecture

The following diagram shows an architecture for a single-agent AI system that's deployed on Cloud Run: 

#### Architecture components

The example architecture consists of the following components: 

|Component|Description|
|---|---|
|Frontend|Users interact with the agent through a frontend, such as a chat interface, that<br>runs as a serverless<br>Cloud Run(/run/docs/overview/what-is-cloud-run) service.|
|Agent|The agent receives user requests, interprets user intent, selects the appropriate<br>tools, and then it synthesizes information to answer queries.|

Component Description 

|Agent runtime|The agent is built by using<br>ADK(https://google.github.io/adk-docs/) and it's<br>deployed as a<br>serverless Cloud Run service(/run/docs/ai-agents). You can also<br>deploy the agent on<br>Agent Runtime on Gemini Enterprise Agent Platform<br>(/gemini-enterprise-agent-platform/scale) or as a containerized app on<br>GKE<br>(/kubernetes-engine/docs/tutorials/agentic-adk-vertex). For information about<br>how to choose an agent runtime, see<br>Choose your agentic AI architecture<br>components<br>(/architecture/choose-agentic-ai-architecture-components#agent_runtime).|
|---|---|
|ADK|ADK provides tools and a framework to develop, test, and deploy agents. ADK<br>abstracts the complexity of agent creation and lets AI developers focus on the<br>agent's logic and capabilities. When you develop agents by using ADK, you can<br>configure the agents to access and use<br>built-in tools<br>(https://google.github.io/adk-docs/tools/built-in-tools/) like Google Search.|
|AI model and<br>model<br>runtime|For inference serving, the agent in this example architecture uses the Gemini AI<br>model on<br>Gemini Enterprise Agent Platform<br>(/gemini-enterprise-agent-platform/models/start).|
|MCP Toolbox|MCP Toolbox for Databases(https://mcp-toolbox.dev/) provides database-specific<br>tools for the agent. It can handle complexities such as connection pooling and<br>authentication.|
|MCP clients,<br>servers, and<br>tools|MCP(https://modelcontextprotocol.io/docs/getting-started/intro) facilitates<br>access to tools by standardizing the interaction between agents and tools. For<br>each agent-tool pair, an MCP client sends requests to an MCP server through<br>which the agent accesses a tool such as a file system or an API. For example,<br>external tools like the StackOverflow LangChain Tool and the Google Search tool<br>can provide data and grounding.|
|Observability|The agent is monitored by using Google Cloud Observability for logging,<br>monitoring, and tracing.|

#### Agentic flow

The example single-agent system in the preceding architecture has the following flow: 

1. A user enters a prompt through a frontend, such as a chat interface, which runs as a serverless Cloud Run service. 

2. The frontend forwards the prompt to the agent. 

3. The agent uses the AI model to reason about the user's prompt and synthesize a response: 

   - The AI model determines which tools to use to gather contextual information or to perform a task. 

   - The agent performs tool calls and it adds the response to its context. 

   - The agent performs grounding and intermediate validation. 

### Products used

This reference architecture uses the following Google Cloud and open-source products and tools: 

- Cloud Run (https://cloud.google.com/run): A serverless compute platform that lets you run containers directly on top of Google's scalable infrastructure. 

- Gemini (https://ai.google.dev/gemini-api/docs/models): A family of multimodal AI models developed by Google. 

- Gemini Enterprise Agent Platform (/gemini-enterprise-agent-platform/overview): A comprehensive platform that lets you build, scale, govern, and optimize enterprise‑grade AI agents. 

- Model Context Protocol (MCP) 

- (https://modelcontextprotocol.io/docs/getting-started/intro): An open-source standard for connecting AI applications to external systems. 

- MCP Toolbox for Databases (https://mcp-toolbox.dev/documentation/introduction/): An open-source Model Context Protocol (MCP) 

- (https://modelcontextprotocol.io/docs/getting-started/intro) server that lets AI agents securely connect to databases by managing database complexities like connection pooling, authentication, and observability. 

- Google Cloud Observability (/stackdriver/docs): Observability services including Cloud Monitoring, Cloud Logging, and Cloud Trace to help you understand the behavior, health, and performance of your applications. 

### Use cases

This section describes possible use cases for the architecture that's described in this document. 

#### Automated bug report triage

You can adapt this reference architecture to automate triage for incoming bug reports: understanding the issue, searching for duplicates, gathering relevant technical context, and then creating a bug in the system. An AI-powered agent can act as an intelligent assistant that can perform the initial investigation, which lets human experts focus on more complex problem-solving. 

For this use case, the architecture provides the following benefits: 

- **Faster resolution times** : The agent automates the initial research and context-gathering, which can significantly reduce the time that it takes to assign and resolve bug tickets. 

- **Improved accuracy and consistency** : The agent can systematically search across multiple data sources (internal databases, code repositories, and the public web). This capability provides a more comprehensive and consistent analysis than manual triage might allow. 

- **Reduced manual workload** : The agent can offload repetitive triage tasks from IT support and engineering teams, which lets them focus on higher-value work. 

This architecture is ideal for any organization that develops software and that wants to improve the efficiency and effectiveness of its bug resolution process. For more information and deployment options, see Software Bug Assistant - ADK Python Sample Agent 

(https://github.com/google/adk-samples/tree/main/python/agents/software-bug-assistant) and Tools Make an Agent: From Zero to Assistant with ADK 

(https://cloud.google.com/blog/topics/developers-practitioners/tools-make-an-agent-from-zeroto-assistant-with-adk) 

#### Customer service

You can adapt this reference architecture to help provide a seamless and personalized shopping experience for customers. An AI-powered agent can provide customer service, recommend products, manage orders, and schedule services, which lets human representatives focus on other tasks. 

For this use case, the architecture provides the following benefits: 

- **Upselling and promotions** : The agent can help increase sales by suggesting products, services, and promotions. The agent's suggestions are based on the customer's current order and relevant sales, the customer's order history, and the items that are in their cart. 

- **Order management and scheduling** : The agent can increase efficiency and reduce customer friction by managing the contents of a customer's shopping cart and facilitating self-scheduling for services. 

- **Reduced manual workload** : The agent handles general inquiries, orders, and scheduling, which enables human customer service agents to focus on more complex customer issues. 

This architecture is ideal for any retail organization that wants to improve their customer experience, increase sales, and simplify their order management and scheduling. For more information and deployment options, see Cymbal Home & Garden Customer Service Agent 

(https://github.com/google/adk-samples/tree/main/python/agents/customer-service). 

#### Time-series forecasting

You can adapt this reference architecture to help predict outcomes, such as demand forecasting, traffic patterns prediction, or machine failure analysis and prediction. An AI-powered agent can analyze real-time data, historical trends, and upcoming events. The agent can use these analyses to forecast outcomes for a specified period of time. These forecasts can help you plan and help reduce the time spent by human data analysts. 

This use case can benefit organizations in many scenarios, such as the following: 

- **Inventory management** : By using advanced analytics combined with historical sales data and market trends, the agent can help you plan restock orders so that you can prepare for surges or lulls in customer demand. 

- **Travel routes** : The agent can help save time and reduce travel costs for delivery and service providers by analyzing real-time and historical traffic patterns along with events like construction or road closures. 

- **Avoid outages** : The agent can help you avoid potential service interruptions by helping to identify the root cause for historical outages. It can also help predict future potential failure states so that you can mitigate an issue before it becomes a problem. 

This architecture is ideal for any organization that needs to adapt to changing patterns based on established trends. It's also ideal for organizations whose customers can benefit from proactive insights that help them plan for the future. For more information and deployment options, see Time Series Forecasting Agent with Google's ADK and MCP Toolbox 

(https://github.com/google/adk-samples/tree/main/java/agents/time-series-forecasting). 

#### Document retrieval

You can adapt this reference architecture to use RAG Engine on Gemini Enterprise Agent Platform (/gemini-enterprise-agent-platform/build/rag-engine/rag-overview) and create an agent to manage contextual data retrieval. A document-retrieval agent can fetch relevant data from a curated set of documents to provide factual answers with citations to the source material. 

With a document-retrieval agent, you can help ensure that customers and internal users get informed and context-aware responses to their queries. This implementation can help reduce mistakes and inaccuracies by helping to ensure that answers are based on the information that you validated. 

A document-retrieval architecture is ideal for knowledge bases about policy and process, technical infrastructure, product capabilities, and other fact-based documentation. For information about how to develop a retrieval-augmented generation (RAG)-powered document retrieval agent, see Documentation Retrieval Agent (https://github.com/google/adk-samples/tree/main/python/agents/RAG). 

### Design alternatives

This section presents alternative design approaches that you can consider for your AI agent deployment in Google Cloud. 

#### Agent runtime

In the architecture that this document describes, the agent and its tools are deployed on Cloud Run. You can also use GKE or Agent Runtime as an alternative runtime. For information about how to choose an agent runtime, see Agent runtime (/architecture/choose-agentic-ai-architecture-components#agent_runtime) in "Choose your agentic AI architecture components". 

#### AI model runtime

In the architecture that this document describes, the AI model runtime is Agent Platform. You can also use Cloud Run or GKE as an alternative runtime. For information about how to choose a model runtime, see Model runtime 

(/architecture/choose-agentic-ai-architecture-components#model-runtime) in "Choose your agentic AI architecture components". 

### Design considerations

This section provides guidance to help you use this reference architecture to develop an architecture that meets your specific requirements for security, reliability, cost, operational efficiency, and performance. 

#### System design

This section provides guidance to help you choose Google Cloud regions for your deployment and to select appropriate Google Cloud products and tools. 

Region selection 

When you select Google Cloud regions for your AI applications, consider the following factors: 

- Availability of Google Cloud services 

(https://cloud.google.com/about/locations#products-available-by-location) in each region. 

- End-user latency 

- (/network-intelligence-center/docs/performance-dashboard/how-to/view-google-cloudlatency#global-latency) 

- requirements. 

- Cost (https://cloud.google.com/products/calculator) of Google Cloud resources. Regulatory requirements. 

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

Memory and session storage 

The example architecture that's shown in this document doesn't include memory or session storage. In a production environment, you can improve the responses and add personalization by integrating state and memory into your agent. 

- **Session** (https://google.github.io/adk-docs/sessions/session/): A session is the conversational thread between a user and the agent, from the initial interaction to the end of the dialogue. 

- **State** (https://google.github.io/adk-docs/sessions/state/): State is the data that the agent uses and collects within a specific session. The state data that's collected includes the history of messages that the user and agent exchanged, the results of any tool calls, and other variables that the agent needs in order to understand the context of the conversation. 

ADK can track sessions in short-term memory by using the `Session` object and `state` attributes. ADK also supports long-term memory 

(https://google.github.io/adk-docs/sessions/memory/) across sessions with the same user, including through Memory Bank (/agent-builder/agent-engine/memory-bank/overview). To store session state, you can also use services like Memorystore for Redis 

(/memorystore/docs/redis/memorystore-for-redis-overview). 

For information about agent memory options, see Choose your agentic AI architecture components 

(/architecture/choose-agentic-ai-architecture-components#agent-memory). 

#### Security

This section describes design considerations and recommendations to design a topology in Google Cloud that meets your workload's security requirements. 

Security considerations for agents 

AI agents introduce certain unique and critical security risks that conventional, deterministic security practices might not be able to mitigate adequately. Google recommends an approach 

(https://research.google/pubs/an-introduction-to-googles-approach-for-secure-ai-agents/) that combines the strengths of deterministic security controls with dynamic, reasoningbased defenses. This approach is grounded in three core principles: human oversight, carefully defined agent autonomy, and observability. The following are specific recommendations that are aligned with these core principles. 

- **Human oversight** : An agentic AI system might sometimes fail or not perform as expected. For example, the model might generate inaccurate content or an agent might select inappropriate tools. In business-critical agentic AI systems, incorporate a human-in-the-loop flow to let human supervisors monitor, override, and pause agents. For example, human users can review the output of agents, approve or reject the outputs, and provide further guidance to correct errors or to make strategic decisions. This approach combines the efficiency of agentic AI systems with the critical thinking and domain expertise of human users. 

- **Agent identity and least-privilege access** : 

   - Provide each agent a workload-bound, SPIFFE 

   - (https://spiffe.io/docs/latest/spiffe-about/overview)-based identity by using 

Agent Identity 

(/gemini-enterprise-agent-platform/govern/agent-identity-overview). You can use Agent Identity when you deploy agents to Agent Runtime 

   - (/gemini-enterprise-agent-platform/scale/runtime/agent-identity) or to Cloud Run 

   - (/run/docs/ai/agent-platform-features). 

   - Configure per-agent permissions by using Identity and Access Management (IAM) access policies 

   - (/gemini-enterprise-agent-platform/govern/policies/iam-overview-uap) and Agent Platform access control with IAM 

   - (/gemini-enterprise-agent-platform/machine-learning/general/access-control). Grant each agent only the permissions that it needs to perform its tasks and to communicate with tools and with other agents. To further isolate each agent and limit the potential impact of a security breach, bind Principal Access Boundary (PAB) (/iam/docs/principal-access-boundary-policies) policies to the agent identity. 

   - When agents need to authenticate to external tools or to third-party APIs, use the Agent Identity auth manager (/iam/docs/auth-manager-overview). With this approach, you can centrally control OAuth tokens and API keys instead of having to embed credentials within agent code or prompts. 

- **Ingress and egress traffic governance** : Route agent traffic through Agent Gateway (/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) to enforce runtime security policies at both the ingress and egress boundaries. For information about the runtime platforms that support Agent Gateway, see Supported agent runtimes 

(/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview#agentruntimes) 

**Client-to-Agent (ingress)** : Deploy Agent Gateway 

- (/gemini-enterprise-agent-platform/scale/runtime/agent-gateway-runtime-deploy) in front of your agent runtime. The gateway helps to authenticate callers and inspect inbound prompts in real time by using Model Armor 

(/gemini-enterprise-agent-platform/govern/configure-model-armor). 

**Agent-to-Anywhere (egress)** : 

Route outbound agent-to-agent (A2A) and agent-to-tool (MCP) requests through Agent Gateway in egress mode. 

   - Enforce default-deny access policies by using IAM access policies and Identity-Aware Proxy (IAP) (/iap/docs/agent-overview). 

   - Verify that target agents and tools are registered in Agent Registry (/agent-registry/overview). 

   - Inspect outbound tool invocations and responses with Model Armor to help prevent data exfiltration, indirect prompt injection, and tool misuse. 

- **Monitoring** : Monitor agent behavior by using comprehensive tracing capabilities that give you visibility into every action that an agent takes, including its reasoning process, tool selection, and execution paths. For more information, see Logging an agent in Agent Runtime 

- (/gemini-enterprise-agent-platform/scale/runtime/logging) and Logging in ADK (https://google.github.io/adk-docs/observability/logging/). 

For more information about securing AI agents, see Safety and Security for AI Agents (https://google.github.io/adk-docs/safety/). 

Agent Platform security considerations 

To help ensure that your Agent Platform configurations and usage meet your security requirements, consider the following recommendations: 

- **Shared responsibility** : Security is a shared responsibility. Agent Platform secures the underlying infrastructure and provides tools and security controls to help you protect your data, code, and models. You are responsible for properly configuring your services, managing access controls, and securing your applications. For more information, see Agent Platform shared responsibility 

- (/gemini-enterprise-agent-platform/machine-learning/shared-responsibility). 

- **Security controls** : Agent Platform supports Google Cloud security controls that you can use to meet your requirements for data residency, customermanaged encryption keys (CMEK) 

- (/gemini-enterprise-agent-platform/machine-learning/general/cmek), network security using VPC Service Controls 

- (/gemini-enterprise-agent-platform/machine-learning/general/vpc-service-controls), and 

Access Transparency (/assured-workloads/access-transparency/docs/overview). For more information, see the following documentation: 

   - Security controls for Agent Platform 

   - (/gemini-enterprise-agent-platform/machine-learning/security-controls) 

   - Security controls for Generative AI 

   - (/gemini-enterprise-agent-platform/models/security-controls) 

   - Agent Platform and zero data retention 

   - (/gemini-enterprise-agent-platform/resources/zero-data-retention) 

- **Safety** : AI models might produce harmful responses, sometimes in response to malicious prompts. 

   - To enhance safety and mitigate potential misuse of the agentic AI system, you can configure content filters to act as barriers to harmful inputs and responses. For more information, see Safety and content filters 

   - (/gemini-enterprise-agent-platform/models/capabilities/configure-safety-filters). 

   - To inspect and sanitize inference requests, agent prompts, tool calls, and responses for threats like prompt injection and harmful content, you can use Model Armor (/model-armor/overview) for direct model API calls _and_ for requests that are routed through Agent Gateway 

   - (/gemini-enterprise-agent-platform/govern/configure-model-armor). Model Armor helps you prevent malicious input, verify content safety, protect sensitive data, maintain compliance, and enforce safety and security policies consistently. 

- **Model access** : You can set up organization policies to limit the type and versions of AI models that can be used in a Google Cloud project. For more information, see Control access to Model Garden models 

- (/gemini-enterprise-agent-platform/models/control-model-access). 

- **Data protection** : To discover and de-identify sensitive data in the prompts and responses and in log data, use the Cloud Data Loss Prevention API (/sensitive-data-protection/docs/apis). For more information, see this video: Protecting sensitive data in AI apps 

(https://www.youtube.com/watch?v=ct1nuLS-wlA). 

MCP security considerations 

To help ensure that your MCP implementation meets your security requirements, consider the following recommendations: 

- **Tool registration and discovery** : Register MCP servers and tools in Agent Registry (/agent-registry/register-mcp-servers) so that agents only connect to inventoried, administrator-approved MCP endpoints. 

- **Access control and traffic inspection** : Route agent-to-MCP traffic through Agent Gateway in **Agent-to-Anywhere (egress)** mode and protect MCP servers (such as MCP servers hosted on Cloud Run) by using IAP 

- (/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp) and IAM access policies. Configure Model Armor or semantic governance policies on Agent Gateway to inspect MCP tool inputs and outputs for sensitive data exposure and indirect prompt injection. 

- **General MCP security** : When you configure your agents to use MCP, ensure that access to external data and tools is authorized, implement privacy controls like encryption, apply filters to protect sensitive data, and monitor agent interactions. For more information, see MCP and security 

- (https://cloud.google.com/discover/what-is-model-context-protocol#mcp-and-security). 

A2A security considerations 

To help ensure that your A2A implementation meets your security requirements, consider the following recommendations: 

- **Transport security** : The A2A protocol mandates HTTPS for all A2A communication in production environments and it recommends Transport Layer Security (TLS) 

(https://a2a-protocol.org/latest/topics/enterprise-ready/#transport-level-security-tls) versions 1.2 or higher. 

- **Authentication** : The A2A protocol delegates authentication to standard web mechanisms like HTTP headers and to standards like OAuth2 and OpenID Connect. Each agent advertises the authentication requirements in its Agent Card. For more information, see A2A authentication 

(https://a2a-protocol.org/latest/topics/enterprise-ready/#authentication). 

- **Inter-agent governance** : Register A2A agents in Agent Registry (/agent-registry/register-agents) and route inter-agent requests through Agent Gateway. By combining Agent Gateway with Agent Identity, IAP, and IAM access policies, you can cryptographically verify the calling agent's identity, enforce fine-grained authorization between coordinator agents and subagents, and inspect inter-agent payloads with Model Armor. 

Cloud Run security considerations 

To help ensure that your Cloud Run implementation meets your security requirements, consider the following recommendations: 

- **Ingress security (for the frontend service)** : To control access to the application, disable the default `run.app` URL 

- (/run/docs/securing/ingress#disable-url) of the frontend Cloud Run service and set up a regional external Application Load Balancer 

(/load-balancing/docs/https/setting-up-reg-ext-https-serverless). In addition to loadbalancing incoming traffic to the application, the load balancer handles SSL certificate management. For added protection, you can use Google Cloud Armor security policies (/armor/docs/integrating-cloud-armor#serverless) to provide request filtering, DDoS protection, and rate limiting for the service. 

**User authentication** : 

- **Users inside your organization** : To authenticate internal user access to the frontend Cloud Run service, use IAP. When a user tries to access an IAP-secured resource, IAP performs authentication and authorization checks. 

- **Users outside your organization** : To authenticate external user access to the frontend service, use Identity Platform (/identity-platform/docs) or Firebase Authentication 

- (https://firebase.google.com/docs/auth). To manage external user access, configure your application to handle a sign-in flow and to make authenticated API calls to the Cloud Run service. 

For more information, see Authenticating users 

(/run/docs/authenticating/end-users). 

- **Agent and MCP server security** : When you host agents or MCP servers on Cloud Run, configure Agent Platform features for Cloud Run 

- (/run/docs/ai/agent-platform-features) to assign a managed agent identity to the service, and use IAP 

- (/gemini-enterprise-agent-platform/govern/policies/iap-cloud-run-mcp) with Agent Gateway to authenticate and authorize inbound agent and tool requests. 

- **Container image security** : To ensure that only authorized container images are deployed to Cloud Run, you can use Binary Authorization 

- (/binary-authorization/docs/run/overview). To identify and mitigate security risks in the container images, use Artifact Analysis to automatically run vulnerability scans. For more information, see Container scanning overview 

- (/artifact-analysis/docs/container-scanning-overview). 

- **Data residency** : Cloud Run helps you meet data residency requirements. Your Cloud Run services run within the selected region 

- (/docs/geography-and-regions#regions_and_zones). 

For more guidance about container security, see General Cloud Run development tips (/run/docs/tips/general#container-security). 

Security considerations for all of the Google Cloud products in the architecture 

To help ensure that your architecture meets your security requirements, consider the following general recommendations: 

- **Data encryption** : By default, Google Cloud encrypts data at rest by using Google-owned and Google-managed encryption keys. To protect your agents' data by using encryption keys that you control, you can use CMEKs (/kms/docs/cmek) that you create and manage in Cloud KMS. For information about Google Cloud services that are compatible with Cloud KMS, see Compatible services (/kms/docs/compatible-services). 

- **Mitigate data exfiltration risk** : To reduce the risk of data exfiltration, create a VPC Service Controls (/vpc-service-controls/docs/overview) perimeter around the infrastructure. VPC Service Controls supports all of the Google Cloud services that this reference architecture uses. 

- **Access control** : When you configure permissions for the resources in your topology, follow the principle of least privilege 

(/iam/docs/using-iam-securely#least_privilege). 

**Cloud environment security** : Use the tools in Security Command Center (/security-command-center/docs/security-command-center-overview) to detect vulnerabilities, identify and mitigate threats, define and deploy a security posture, and export data for further analysis. 

**Post-deployment optimization** : After you deploy your application in Google Cloud, get recommendations to further optimize security by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see Find recommendations in Active Assist (/recommender/docs/active-assist/find-recommendations). 

More security recommendations 

- Well-Architected Framework AI and ML perspective: Security (/architecture/framework/perspectives/ai-ml/security) 

- Google's Approach for Secure AI Agents: An Introduction (https://storage.googleapis.com/gweb-research2023-media/pubtools/1018686.pdf) 

#### Reliability

This section describes design considerations and recommendations to build and operate reliable infrastructure for your deployment in Google Cloud. 

Component Design considerations and recommendations Agent Simulate failures: Before you deploy the agentic AI system to production, validate it by simulating a production environment. Identify and fix issues and unexpected behaviors. 

Scale horizontally: To help ensure high availability and fault tolerance, run multiple instances of your agent application behind a load balancer. This approach can also help reduce latency and timeouts by distributing requests across instances. Some agent runtimes handle load balancing for you automatically, such as with instance autoscaling in Cloud Run services (/run/docs/about-instance-autoscaling). Recover from outages: To help ensure that the agent can gracefully handle restarts and maintain context, decouple state from runtime. To implement such a stateless agent application, use an external datastore like a database or a distributed cache. For example, you can use Memory Bank (/agent-builder/agent-engine/memory-bank/overview), Memorystore for Redis (/memorystore/docs/redis/memorystore-for-redis-overview), or a database service like Cloud SQL (/sql/docs/introduction). 

Handle errors: To enable diagnosis and troubleshooting of errors, implement logging, exception handling, and retry mechanisms. Agent Capacity planning: If the number of your requests exceeds the allocated Platform capacity, then error code 429 (/gemini-enterprise-agent-platform/models/standard-paygo#resourceexhausted-429-errors) is returned. For workloads that are business critical and consistently require high throughput, you can reserve throughput by using Provisioned Throughput (/gemini-enterprise-agent-platform/models/provisioned-throughput). Model endpoint availability: If data can be shared across multiple regions or countries, you can use a global endpoint (/gemini-enterprise-agent-platform/resources/locations#global-endpoint) for the model. 

|Component|Design considerations and recommendations|
|---|---|
|Cloud Run|Robustness to infrastructure outages: Cloud Run is a regional service. It stores<br>data synchronously across multiple zones within a region and it automatically<br>load-balances traffic across the zones. If a zone outage occurs, Cloud Run<br>continues to run and data isn't lost. If a region outage occurs, the service stops<br>running until Google resolves the outage.|
||Horizontal scaling: Cloud Run services handle<br>instance autoscaling<br>(/run/docs/about-instance-autoscaling) for you. Autoscaling helps ensure that<br>instances can handle all of the incoming requests, events, and CPU utilization<br>that's needed to ensure high availability.|
|All of the<br>products in<br>the<br>architecture|Post-deployment optimization: After you deploy your application in Google Cloud,<br>get recommendations to further optimize security by using Active Assist. Review<br>the recommendations and apply them as appropriate for your environment. For<br>more information, see<br>Find recommendations in Active Assist<br>(/recommender/docs/active-assist/find-recommendations).|

For reliability principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Reliability 

(/architecture/framework/perspectives/ai-ml/reliability) in the Well-Architected Framework. 

#### Operations

This section describes the factors to consider when you use this reference architecture to design a Google Cloud topology that you can operate efficiently. 

|Component|Design considerations and recommendations|
|---|---|
|Agent|Debugging and analysis: Implement structured logging within your agent<br>application. Logging and tracing lets you capture key information in a structured<br>format, such as which tools were called, the inputs and outputs of the agent, and<br>the latency of each step.|

|Component|Design considerations and recommendations|
|---|---|
|Agent<br>Platform|Monitoring using logs: By default, agent logs that are written to the`stdout`and<br>`stderr`streams are routed to Cloud Logging. For advanced logging, you can<br>integrate the Python logger with Logging. If you need full control over logging<br>and structured logs, use the Logging client. For more information, see<br>Logging<br>an agent(/gemini-enterprise-agent-platform/scale/runtime/logging) and<br>Logging<br>in ADK(https://google.github.io/adk-docs/observability/logging/).<br>Continuous evaluation: Regularly perform a qualitative evaluation of the output<br>of the agents and the trajectory or steps taken by the agents to produce the<br>output. To implement agent evaluation, you can use the<br>Gen AI evaluation<br>service<br>(/gemini-enterprise-agent-platform/optimize/evaluation/agent-evaluation) or the<br>evaluation methods that ADK supports<br>(https://google.github.io/adk-docs/evaluate/#how-evaluation-works-with-the-<br>adk)<br>.|
|Cloud Run|Health and performance: Monitor your Cloud Run services by using Google Cloud<br>Observability. Set up alerts in Cloud Monitoring to notify you of potential issues,<br>such as an increase in error rates, high latency, or abnormal resource utilization.|
|Databases|Health and performance: Monitor your database by using Google Cloud<br>Observability. Set up alerts in Monitoring to notify you of potential issues, such<br>as an increase in error rates, high latency, or abnormal resource utilization.|

Component Design considerations and recommendations MCP Database tools: To efficiently manage database tools for your AI agents and to ensure that the agents securely handle complexities like connection pooling and authentication, use the MCP Toolbox for Databases (https://mcp-toolbox.dev/dev/documentation/introduction/). It provides a centralized location to store and update database tools. You can share the tools across agents and update the tools without redeploying agents. The toolbox includes a wide range of tools for Google Cloud databases like AlloyDB for PostgreSQL and for third-party databases like MongoDB. Generative AI models: To enable AI agents to use Google generative AI models like Imagen and Veo, you can use MCP Servers for Google Cloud generative media APIs (https://github.com/GoogleCloudPlatform/vertex-ai-creativestudio/tree/main/experiments/mcp-genmedia) . Google security products and tools: To enable your AI agents to access Google security products and tools like Google Security Operations, Google Threat Intelligence, and Security Command Center, use MCP servers for Google security products (https://google.github.io/mcp-security/). All of the Tracing: Continuously gather and analyze trace data by using Trace. Trace data Google Cloud lets you rapidly identify and diagnose latency issues within complex agent products in workflows. You can perform in-depth analysis through visualizations in the the Google Cloud console Trace explorer page. For more information, see Trace an architecture agent (/gemini-enterprise-agent-platform/optimize/observability/traces). 

For operational excellence principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Operational excellence 

(/architecture/framework/perspectives/ai-ml/operational-excellence) in the Well-Architected Framework. 

#### Cost optimization

This section provides guidance to optimize the cost of setting up and operating a Google Cloud topology that you build by using this reference architecture. 

Agent Platform cost considerations 

To help ensure that your Agent Platform configurations and usage meet your cost requirements, consider the following recommendations: 

**Cost analysis and management** : To analyze and manage Agent Platform costs, we recommend that you create baseline metrics for queries per second (QPS) and tokens per second (TPS). Then, monitor these metrics after deployment. The baseline also helps with capacity planning. For example, the baseline helps you determine when Provisioned Throughput 

(/gemini-enterprise-agent-platform/models/provisioned-throughput) might be necessary. 

**Model selection** : The model 

(/gemini-enterprise-agent-platform/models/google-models) that you select for your AI application directly affects both costs and performance. To identify the model that provides an optimal balance between performance and cost for your specific use case, test models iteratively. We recommend that you start with the most cost-efficient model and progress gradually to more powerful options. 

**Cost-effective prompting** : The length of your prompts (input) and the generated responses (output) directly affect performance and cost. Write prompts that are short, direct, and provide sufficient context. Design your prompts to get concise responses from the model. For example, include phrases such as "summarize in 2 sentences" or "list 3 key points". For more information, see the best practices for prompt design 

(/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies#bestpractices) 

- **Context caching** : To reduce the cost of requests that contain repeated content with high input token counts, use context caching 

- (/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview). 

**Batch requests** : When relevant, consider batch prediction 

- (/gemini-enterprise-agent-platform/models/capabilities/batch-inference). Batched requests incur a lower cost than standard requests. 

Cloud Run cost considerations 

To help ensure that your Cloud Run implementation meets your cost requirements, consider the following recommendations: 

- **Resource allocation** : When you create a Cloud Run service, you can specify the amount of memory and CPU to be allocated. Start with the default CPU and memory allocations. Observe the resource usage and cost over time, and adjust the allocation as necessary. For more information, see Configure memory limits for services (/run/docs/configuring/services/memory-limits) and Configure CPU limits for services (/run/docs/configuring/services/cpu) 

- **Rate optimization** : If you can predict the CPU and memory requirements, you can save money with committed use discounts (CUDs) (/run/cud). 

Cost considerations for all of the Google Cloud products in the architecture 

After you deploy your application in Google Cloud, get recommendations to further optimize cost by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see Find recommendations in Active Assist 

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

- (/gemini-enterprise-agent-platform/models/prompts/prompt-optimizer). The optimizer helps you efficiently adapt prompts across different models. 

Agent Platform performance considerations 

To help ensure that your Agent Platform configurations and usage meet your performance requirements, consider the following recommendations: 

- **Model selection** : The model 

- (/gemini-enterprise-agent-platform/models/google-models) that you select for your AI application directly affects both costs and performance. To identify the model that provides an optimal balance between performance and cost for your specific use case, test models iteratively. We recommend that you start with the most cost-efficient model and progress gradually to more powerful options. 

- **Prompt engineering** : The length of your prompts (input) and the generated responses (output) directly affect performance and cost. Write prompts that are short, direct, and provide sufficient context. Design your prompts to get concise responses from the model. For example, include phrases such as "summarize in 2 sentences" or "list 3 key points". For more information, see the best practices for prompt design 

- (/gemini-enterprise-agent-platform/models/prompts/prompt-design-strategies#bestpractices) 

- **Context caching** : To reduce latency for requests that contain repeated content with high input token counts, use context caching 

- (/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview). 

Cloud Run performance considerations 

Depending on your performance requirements, configure the memory and CPU to be allocated to the Cloud Run service. For more information, see Configure memory limits for services (/run/docs/configuring/services/memory-limits) and Configure CPU limits for services (/run/docs/configuring/services/cpu) 

For more performance optimization guidance, see General Cloud Run development tips (/run/docs/tips/general#optimize_performance). 

Performance considerations for all of the Google Cloud products in the architecture After you deploy your application in Google Cloud, get recommendations to further optimize performance by using Active Assist. Review the recommendations and apply them as appropriate for your environment. For more information, see Find recommendations in Active Assist 

(/recommender/docs/active-assist/find-recommendations). 

For performance optimization principles and recommendations that are specific to AI and ML workloads, see AI and ML perspective: Performance optimization (/architecture/framework/perspectives/ai-ml/performance-optimization) in the WellArchitected Framework. 

### Deployment

Automated deployment for this reference architecture isn't available. Use the following code samples to help you build a single-agent architecture: 

- Deploy a similar architecture by deploying the Software Bug Assistant - ADK Python Sample Agent 

(https://github.com/google/adk-samples/tree/main/python/agents/software-bugassistant) 

- Learn more about memory and state with Python Tutor - ADK State and Memory Example 

- (https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/python-tutor). 

For code samples to get started with using ADK together with MCP servers, see MCP Tools (https://google.github.io/adk-docs/tools/mcp-tools/). 

For examples of additional single-agent AI systems, you can use the following code samples. These code samples are fully functional starting points for learning and experimentation. For optimal operation in production environments, you must customize the code based on your specific business and technical requirements. 

Personalized shopping 

(https://github.com/google/adk-samples/tree/main/python/agents/personalized-shopping) : Provide personalized product recommendations for a specific brand, merchant, or online marketplace. 

Incident management 

(https://github.com/google/adk-samples/tree/main/python/agents/incident-management) : Validate end-user token and identity on a per-request basis by using dynamic identity propagation. 

Order processing 

(https://github.com/google/adk-samples/tree/main/python/agents/order-processing): Process and store orders and orchestrate email confirmation with a conditional human review for specified order quantities. 

Data engineering 

(https://github.com/google/adk-samples/tree/main/python/agents/data-engineering): Develop Dataform pipelines, troubleshoot pipeline issues, and manage data engineering from complex SQL queries to data transformations and data dependencies. 

Documentation retrieval 

(https://github.com/google/adk-samples/tree/main/python/agents/RAG): Use RAG to query documents that you upload to RAG Engine on Gemini Enterprise Agent Platform and get answers with citations to documentation and code. 

### What's next

Explore sample agents and tools in Agent Garden 

(https://console.cloud.google.com/agent-platform/agent-garden). 

Build agents using ADK (https://google.github.io/adk-docs/agents/). 

Deploy agents to Google Cloud (https://google.github.io/adk-docs/deploy/). 

- Host MCP servers on Cloud Run (/run/docs/host-mcp-servers). 

- Host AI apps and agents on Cloud Run (/run/docs/ai-agents). 

- Learn how to implement a RAG infrastructure for generative AI applications in Google Cloud (/architecture/rag-reference-architectures). 

- For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the AI and ML perspective (/architecture/framework/perspectives/ai-ml) in the Well-Architected Framework. 

- For more reference architectures, diagrams, and best practices, explore the Cloud Architecture Center (/architecture). 

### Contributors

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Megan O'Keefe (https://www.linkedin.com/in/askmeegs) | Developer Advocate 

- Shir Meir Lador (https://www.linkedin.com/in/shirmeirlador) | Developer Relations Engineering Manager 

Last updated 2025-12-09 UTC. 



## Landing zone design in Google Cloud

URL: https://docs.cloud.google.com/architecture/landing-zones

Last reviewed 2026-01-02 UTC 

This document provides an overview on how to design landing zones in Google Cloud. A landing zone, also called a _cloud foundation_ , is a modular and scalable configuration that enables organizations to adopt Google Cloud for their business needs. A landing zone is often a prerequisite to deploying enterprise workloads in a cloud environment. 

A _landing zone_ is not a zone 

(https://cloud.google.com/docs/geography-and-regions#regions_and_zones) or zonal resources (https://cloud.google.com/docs/geography-and-regions#zonal_resources). 

This document is aimed at solutions architects, technical practitioners, and executive stakeholders who want an overview of the following: 

- Typical elements of landing zones in Google Cloud 

- Where to find detailed information on landing zone design 

- How to deploy a landing zone for your enterprise, including options to deploy pre-built solutions 

This document is part of a series that helps you understand how to design and build a landing zone. The other documents in this series help guide you through the high-level decisions that you need to make when you design your organization's landing zone. In this series, you learn about the following: 

- Landing zone design in Google Cloud (this document) 

- Decide how to onboard identities to Google Cloud 

- (/architecture/landing-zones/decide-how-to-onboard-identities) 

- Decide the resource hierarchy for your Google Cloud landing zone 

- (/architecture/landing-zones/decide-resource-hierarchy) 

- Decide the network design for your Google Cloud landing zone 

- (/architecture/landing-zones/decide-network-design) 

- Decide the security for your Google Cloud landing zone 

- (/architecture/landing-zones/decide-security) 

This series does not specifically address compliance requirements from regulated industries such as financial services or healthcare. 

### What is a Google Cloud landing zone?

Landing zones help your enterprise deploy, use, and scale Google Cloud services more securely. Landing zones are dynamic and grow as your enterprise adopts more cloud-based workloads over time. 

To deploy a landing zone, you must first create an organization resource (/resource-manager/docs/creating-managing-organization) and create a billing account (/billing/docs/how-to/manage-billing-account), either online or invoiced. 

A landing zone spans multiple areas and includes different elements, such as identities, resource management, security, and networking. Many other elements can also be part of a landing zone, as described in Elements of a landing zone (#elements). 

The following diagram shows a sample implementation of a landing zone. It shows an Infrastructure as a Service (IaaS) use case with hybrid cloud and on-premises connectivity in Google Cloud: 

The example architecture in the preceding diagram shows a Google Cloud landing zone that includes the following Google Cloud services and features: 

- Resource Manager defines a resource hierarchy 

- (/resource-manager/docs/cloud-platform-resource-hierarchy) with organizational policies. (/resource-manager/docs/organization-policy/overview) 

- A Cloud Identity (/identity/docs/overview) account synchronizes with an onpremises identity provider and Identity and Access Management (IAM) (/iam/docs/overview) providing granular access to Google Cloud resources. 

- A network deployment that includes the following: 

   - A Shared VPC (/vpc/docs/shared-vpc) network for each environment (production, development, and testing) connects resources from multiple 

projects to the VPC network. 

   - Virtual Private Cloud (VPC) firewall rules (/vpc/docs/firewalls) control connectivity to and from workloads in the Shared VPC (/vpc/docs/shared-vpc) networks. 

   - A Cloud NAT (/nat/docs/overview) gateway allows outbound connections to the internet from resources in these networks without external IP addresses. 

   - Cloud Interconnect (/network-connectivity/docs/interconnect/concepts/overview) connects on-premises applications and users. (You can choose between different Cloud Interconnect options, including Dedicated Interconnect 

   - (/network-connectivity/docs/interconnect/concepts/dedicated-overview) or Partner Interconnect 

   - (/network-connectivity/docs/interconnect/concepts/partner-overview).) 

   - Cross-Cloud Interconnect 

   - (/network-connectivity/docs/interconnect/concepts/cci-overview) (or Cloud VPN 

   - (/network-connectivity/docs/vpn)) connects to other cloud service providers. 

   - A Cloud DNS (/dns/docs/overview) private zone hosts DNS records for your deployments in Google Cloud. 

- Multiple service projects are configured to use the Shared VPC (/vpc/docs/shared-vpc) networks. These service projects host your application resources. 

- Google Cloud Observability (/stackdriver/docs) includes Cloud Monitoring (/monitoring/docs) for monitoring and Cloud Logging (/logging/docs) for logging. Cloud Audit Logs (/logging/docs/audit), Firewall Rules Logging 

- (/vpc/docs/firewall-rules-logging) and VPC Flow Logs (/vpc/docs/flow-logs) help ensure all necessary data is logged and available for analysis. 

- A VPC Service Controls (/vpc-service-controls/docs/overview) perimeter isolates service and resources, which helps to mitigate the risk of data egress to Google Cloud services outside the perimeter. Traffic from hybrid environments is configured with authorized private access to communicate with services inside the perimeter. 

The diagram above is only an example, because there is no single or standard implementation of a landing zone. Your business must make many design choices, 

depending on different factors, including the following: 

- Your industry 

- Your organizational structure and processes 

- Your security and compliance requirements 

- The workloads that you want to move to Google Cloud 

- Your existing IT infrastructure and other cloud environments 

- The location of your business and customers 

### When to build a landing zone

We recommend that you build a landing zone before you deploy your first enterprise workload on Google Cloud, because a landing zone provides the following: 

- A foundation that's designed to be secure 

- The network for enterprise workloads 

- The tools that you require to govern your internal cost distribution 

However, because a landing zone is modular, your first iteration of a landing zone is often not your final version. Therefore, we recommend that you design a landing zone with scalability and growth in mind. For example, if your first workload does not require access to on-premises network resources, you could build connectivity to your on-premises environment later. 

Depending on your organization and the type of workloads that you plan to run on Google Cloud, some workloads might have very different requirements. For example, some workloads might have unique scalability or compliance requirements. In these cases, you might require more than one landing zone for your organization: one landing zone to host most of the workloads and a separate landing zone to host the unique workloads. You can share some elements such as identities, billing, and the organization resource across your landing zones. However, other elements, such as the network setup, deployment mechanisms, and folder-level policies, might vary. 

### Elements of a landing zone

A landing zone requires you to design the following core elements on Google Cloud: 

- Identity provisioning (/architecture/landing-zones/decide-how-to-onboard-identities) Resource hierarchy (/architecture/landing-zones/decide-resource-hierarchy) 

- Network (/architecture/landing-zones/decide-network-design) 

- Security controls (/architecture/landing-zones/decide-security) 

In addition to these core elements, your business might have additional requirements. The following table describes these elements and where you can find more information about them. 

|Landing zone<br>element|Description|
|---|---|
|Monitoring and<br>logging|Design a monitoring and logging strategy that helps ensure all relevant data<br>is logged and that you have dashboards that visualize the data and alerts<br>that notify you of any actionable exceptions.<br>For more information, see the<br>Monitoring, logging, and alerting<br>(/docs/security/gcmvsp/monitoring-logging-alerting) section of the Google<br>Cloud minimum viable secure platform.|
|Backup and<br>disaster recover|y<br>Design a strategy for backups and disaster recovery.<br>For more information, see the following:<br>Disaster recovery planning guide<br>(/architecture/dr-scenarios-planning-guide)<br>Backup and DR Service<br>(/backup-disaster-recovery/docs/concepts/backup-dr)|
|Compliance|Follow the compliance frameworks that are relevant to your organization.<br>For more information, see the<br>Compliance resource center<br>(https://cloud.google.com/compliance).|

|Landing zone<br>element|Description|
|---|---|
|Cost efficiency<br>and control|Design capabilities to monitor and optimize cost for workloads in your landing<br>zone.<br>For more information, see the following:<br>Overview of cloud billing concepts(/billing/docs/concepts)<br>Google Cloud Well-Architected Framework: Cost optimization<br>(/architecture/framework/cost-optimization)<br>Cost management(https://cloud.google.com/cost-management)|
|API managemen|tDesign a scalable solution for APIs that you develop. For more information,<br>see<br>Apigee API Management(/apigee).|
|Cluster<br>management|Design Google Kubernetes Engine (GKE) clusters that follow best practices to<br>build scalable, resilient, and observable services.|
||For more information, see the following:|

- GKE best practices (/kubernetes-engine/docs/best-practices) GKE Autopilot mode (/kubernetes-engine/docs/concepts/autopilot-overview) 

Multi-cluster Services 

- (/kubernetes-engine/docs/concepts/multi-cluster-services) 

About Cloud Service Mesh (/service-mesh/docs/overview) 

### Best practices for designing and deploying a landing zone

Designing and deploying a landing zone requires planning. You must have the right team to perform the tasks, and use a project management process. We also recommend that you follow the technical best practices that are described in this series. 

#### Build a team

Bring together a team that includes people from multiple technical functions across the organization. The team must include people who can build all landing zone elements, including security, identity, networks, and operations. Identify a cloud practitioner who understands Google Cloud to lead the team. Your team should include members who manage the project and track achievements, and members who collaborate with application or business owners. 

Make sure that all stakeholders are involved early in the process. Your stakeholders must come to a common understanding of the scope of the process and make high-level decisions when the project gets kicked off. 

#### Apply project management to your landing zone deployment

Designing and deploying your landing zone can take multiple weeks, so project management is essential. Ensure that project goals are clearly defined and communicated to all stakeholders and that all parties receive updates on any project changes. Define regular checkpoints and agree on milestones with realistic timelines that take operational processes and unexpected delays into account. 

To best align with business requirements, plan the initial landing zone deployment around the use cases that you want to deploy first in Google Cloud. We recommend that you first deploy workloads that can most easily run on Google Cloud, such as horizontally scaling multi-tier web applications. These workloads might be new or existing workloads. To assess existing workloads for migration readiness, see Migration to Google Cloud: Getting started 

(/architecture/migration-to-gcp-getting-started). 

Because landing zones are modular, center the initial design around the elements that are required to migrate your first workloads and plan to add other elements later. 

#### Follow technical best practices

Consider using Infrastructure as Code (IaC) 

(https://en.wikipedia.org/wiki/Infrastructure_as_code), with, for example, Terraform (/docs/terraform). IaC helps you make your deployment repeatable and modular. Having a CI/CD pipeline that deploys cloud infrastructure changes 

(/docs/terraform/resource-management/managing-infrastructure-as-code) using GitOps 

helps you ensure that you follow internal guidelines and put the right controls in place. 

When you design your landing zone, ensure that you and your team take technical best practices into consideration. For more information on decisions to make in your landing zone, see the other guides in this series. 

In addition to this series, the following table describes frameworks, guides, and blueprints that can also help you follow best practices, depending on your use cases. 

|Related documentation|Description|
|---|---|
|Google Cloud Setup<br>(/docs/enterprise/cloud-setup)|A high-level guided flow to help you set up Google<br>Cloud for scalable, production-ready, enterprise<br>workloads.|
|Enterprise foundation blueprint<br>(/architecture/security-foundations)|An opinionated view of Google Cloud security best<br>practices, aimed at CISO, security practitioners, risk<br>managers, or compliance officers.|
|Google Cloud Well-Architected Framework<br>(/architecture/framework)|Recommendations and best practices to help<br>architects, developers, administrators, and other<br>cloud practitioners design and operate a cloud<br>topology that's secure, efficient, resilient, high-<br>performing, and cost-effective.|
|Terraform blueprints<br>(/docs/terraform/blueprints/terraform-<br>blueprints)|A list of blueprints and modules that are packaged<br>as Terraform modules and that you can use to<br>create resources for Google Cloud.|

### Identify resources to help implement your landing zone

Google Cloud offers the following options to help you set up your landing zone: 

- Design and deploy a landing zone that is customized to your requirements with Google Cloud partners (https://cloud.google.com/partners) or Google Cloud professional services (https://cloud.google.com/consulting). 

- Onboard a workload with the Google Cloud Customer Onboarding program (http://cloud.google.com/onboarding). 

- Deploy a generic landing zone with the setup guide in the Google Cloud console (https://console.cloud.google.com/cloud-setup/overview). 

- Deploy a highly opinionated landing zone by using the Terraform example foundation 

(https://github.com/terraform-google-modules/terraform-example-foundation). 

All these offerings have approaches that are designed specifically to meet the needs of different industries and business sizes, across the globe. To help you make the best selection for your use case, we recommend that you work with your Google Cloud account team to make the selection and help to ensure a successful project. 

### What's next

- Decide how to onboard identities to Google Cloud 

- (/architecture/landing-zones/decide-how-to-onboard-identities) (next document in this series). 

- Decide the resource hierarchy for your Google Cloud landing zone 

- (/architecture/landing-zones/decide-resource-hierarchy). 

- Decide the network design for your Google Cloud landing zone 

- (/architecture/landing-zones/decide-network-design). 

- Decide the security for your Google Cloud landing zone 

- (/architecture/landing-zones/decide-security). 

Last updated 2026-01-02 UTC. 



## Enterprise foundations blueprint

URL: https://docs.cloud.google.com/architecture/blueprints/security-foundations

Last reviewed 2025-05-15 UTC 

This document describes the best practices that let you deploy a foundational set of resources in Google Cloud. A cloud foundation is the baseline of resources, configurations, and capabilities that enable companies to adopt Google Cloud for their business needs. A well-designed foundation enables consistent governance, security controls, scale, visibility, and access to shared services across all workloads in your Google Cloud environment. After you deploy the controls and governance that are described in this document, you can deploy workloads to Google Cloud. 

The _enterprise foundations blueprint_ (formerly known as the _security foundations blueprint_ ) is intended for architects, security practitioners, and platform engineering teams who are responsible for designing an enterprise-ready environment on Google Cloud. This blueprint consists of the following: 

A terraform-example-foundation GitHub repository 

- (https://github.com/terraform-google-modules/terraform-example-foundation) that contains the deployable Terraform assets. 

- A guide that describes the architecture, design, and controls that you implement with the blueprint (this document). 

You can use this guide in one of two ways: 

- To create a complete foundation based on Google's best practices. You can deploy all the recommendations from this guide as a starting point, and then customize the environment to address your business' specific requirements. 

- To review an existing environment on Google Cloud. You can compare specific components of your design against Google-recommended best practices. 

### Supported use cases

The enterprise foundation blueprint provides a baseline layer of resources and configurations that help enable all types of workloads on Google Cloud. Whether 

you're migrating existing compute workloads to Google Cloud, building containerized web applications, or creating big data and machine learning workloads, the enterprise foundation blueprint helps you build your environment to support enterprise workloads at scale. 

After you deploy the enterprise foundation blueprint, you can deploy workloads directly or deploy additional blueprints to support complex workloads that require additional capabilities. 

### A defense-in-depth security model

Google Cloud services benefit from the underlying Google infrastructure security design (/docs/security/infrastructure/design). It is your responsibility to design security into the systems that you build on top of Google Cloud. The enterprise foundation blueprint helps you to implement a defense-in-depth security model for your Google Cloud services and workloads. 

The following diagram shows a defense-in-depth security model for your Google Cloud organization that combines architecture controls, policy controls, and detective controls. 

The diagram describes the following controls: 

**Policy controls** are programmatic constraints that enforce acceptable resource configurations and prevent risky configurations. The blueprint uses a 

combination of policy controls including infrastructure-as-code (IaC) validation in your pipeline and organization policy constraints. 

- **Architecture controls** are the configuration of Google Cloud resources like networks and resource hierarchy. The blueprint architecture is based on security best practices. 

- **Detective controls** let you detect anomalous or malicious behavior within the organization. The blueprint uses platform features such as Security Command Center, integrates with your existing detective controls and workflows such as a security operations center (SOC), and provides capabilities to enforce custom detective controls. 

### Key decisions

This section summarizes the high-level architectural decisions of the blueprint. 

The diagram describes how Google Cloud services contribute to key architectural decisions: 

- **Cloud Build:** Infrastructure resources are managed using a GitOps model. Declarative IaC is written in Terraform and managed in a version control system for review and approval, and resources are deployed using Cloud Build as the continuous integration and continuous deployment (CI/CD) automation tool. The pipeline also enforces policy-as-code checks to validate that resources meet expected configurations before deployment. 

- **Cloud Identity:** Users and group membership are synchronized from your existing identity provider. Controls for user account lifecycle management and single sign-on (SSO) rely on the existing controls and processes of your identity provider. 

- **Identity and Access Management (IAM):** Allow policies (formerly known as IAM policies) allow access to resources and are applied to groups based on job function. Users are added to the appropriate groups to receive view-only access to foundation resources. All changes to foundation resources are deployed through the CI/CD pipeline which uses privileged service account identities. 

- **Resource Manager:** All resources are managed under a single organization, with a resource hierarchy of folders that organizes projects by environments. Projects are labeled with metadata for governance including cost attribution. 

- **Networking** : Network topologies use Shared VPC to provide network resources for workloads across multiple regions 

- (/docs/geography-and-regions#regions_and_zones) and zones, separated by environment, and managed centrally. All network paths between on-premises hosts, Google Cloud resources in the VPC networks, and Google Cloud services are private. No outbound traffic to or inbound traffic from the public internet is permitted by default. 

- **Cloud Logging** : Aggregated log sinks are configured to collect logs relevant for security and auditing into a centralized project for long-term retention, analysis, and export to external systems. 

- **Organization Policy Service:** Organization policy constraints are configured to prevent various high-risk configurations. 

- **Secret Manager:** Centralized projects are created for a team responsible for managing and auditing the use of sensitive application secrets to help meet compliance requirements. 

- **Cloud Key Management Service (Cloud KMS):** Centralized projects are created for a team responsible for managing and auditing encryption keys to help meet compliance requirements. 

- **Security Command Center:** Threat detection and monitoring capabilities are provided using a combination of built-in security controls from Security Command Center and custom solutions that let you detect and respond to security events. 

For alternatives to these key decisions, see alternatives (/architecture/blueprints/security-foundations/summary#alternatives). 

### What's next

- Read about authentication and authorization 

- (/architecture/blueprints/security-foundations/authentication-authorization) (next document in this series). 

Last updated 2025-05-15 UTC.
