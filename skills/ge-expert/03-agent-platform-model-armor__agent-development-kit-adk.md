# Agent Platform, Model Armor and data governance / Agent Development Kit (ADK) to A2A key concepts
Source: 03-Agent-Platform-Model-Armor-and-data-governance.pdf, pages 152-170, extracted 2026-10-18

Contains:
- Agent Development Kit (ADK) (pages 152-165) https://adk.dev/
- A2A key concepts (pages 166-170) https://a2a-protocol.org/latest/topics/key-concepts/

## Agent Development Kit (ADK)

URL: https://adk.dev/

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **Build production agents,** **not prototypes.** 

ADK is the open-source agent development framework that lets you build, debug, and deploy reliable AI agents at enterprise scale. Available in Python, TypeScript, Go, Java, and Kotlin. **Start building** Python TypeScript Go Java Kotlin `from google.adk import Agent from google.adk.tools import google_search agent = Agent( name="researcher", model="gemini-flash-latest", instruction="You help users research topics thoroughly.", tools=[google_search],` **Cookie consent** `)` We use cookies to recognize repeated visits and preferences, as well as to measure the efectiveness of our documentation andf whether users find the information they need. With your consent, `pip install google-adk` you're helping us to make our documentation better. **Manage settings** 

### **Agents CLI** 

### **Build agents** **_with_ agents.** 

Go from idea to coded ADK agent in minutes. Use your favorite AI-enabled developer environment to scaffold, build, test, evaluate, and deploy with Agents CLI. 

**Learn more** 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **Graph Workflows** 

### **Reliable logic. Intelligent reasoning.** 

Weave deterministic code with adaptive AI reasoning. Orchestrate complex tasks through structured, graph-based architectures, with explicit execution paths and predictable outcomes. New in ADK 2.0! 

### **Learn more** 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **Framework** 

### **Powerful simplicity. Built for scale.** 

Start building ADK agents with prompts and tool calls, then grow to multi-agent orchestration, graph-based workflows, performance evaluation, and deployment to world class enterprise services for scalability, reliability, and throughput. 

### **Learn more** 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **Ecosystem** 

### **Open ecosystem. Connect everything.** 

ADK's open integration partners connect your agents with existing apps, a wide range of AI models, and extend agent capabilities to access data, add resilience, and evaluate performance. 

### **Learn more** 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **Ready to build agents?** 

### We think one of the best ways to learn is by building, so **Cookie consent** 

We use cookies to recognize repeated visits and preferences, aswe've created guides that help you get your development environment set up and run an ADK agentwell as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, in minutes. you're helping us to make our documentation better. 

**Manage settings** 

### **Start building** 

### **Developer Community** 

Build alongside a growing community of developers engineering the next generation of production-ready AI agents. Whether you want to troubleshoot a graph workflow, share a custom Agent Skill, or shape the future of the framework, we want you involved. 

### **Community call** 

Join the ADK core engineering team for live demos, technical deep dives, roadmap updates, and Q&A. **Learn more →** 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Developer resources Manage settings** 

Skip the learning curve with comprehensive training, videos, and deep-dives from community members like you. **Learn more →** 

### **Frequently Asked Questions** 

Still have questions about ADK? Here are some answers: 

### **Can I vibe code agents with ADK?** 

Yes! ADK is designed to be written by both humans and AI. Connect your favorite coding assistant to our ADK developer Skills and AI-aware developer resources, and generate agents in seconds. Find out more about AI-powered coding of agents in our Coding with AI guide. 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **What AI models can I use with ADK?** 

ADK can work with almost any generative AI model. The framework provides easy access to Gemini as well as other leading models, and we provide adapters that let you connect with many other models and model providers, including locally running models. For enterprises, ADK can connect to models on hosted services, including Google Cloud which provides a wide range of models and lets you closely manage performance, reliability, security, access, safety, and costs. 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **What makes ADK different?** 

With ADK, we are focused on building an open development framework that lets you build professional, production grade agents, without requiring a pile of code to get started. Our goal is to get you building agents quickly, and let you add functionality and complexity as you need it. ADK provides a basic structure for agents that is easy to build, and that structure is designed with the flexibility to let you extend, expand, and build complex, robust, useful agentic systems. We've put a lot of effort into providing you with development tools for interacting with agents you build, and providing ways to use AI-powered tools for building ADK agents. We are also quite proud of our approach to agent context management and how we manage context to keep it efficient, and also let you tune context management to your needs. We could go on, and if you are interested, you can find more details in our developer docs. 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **How does ADK handle context management?** 

Unlike tools that simply paste strings together until the context window overflows, ADK **manages** your context. We treat context like source code— sessions, memory, tool outputs, and artifacts are assembled into a structured view where every token earns its place. ADK automatically filters irrelevant events, summarizes older conversational turns, lazy-loads artifacts, and tracks token usage. This approach keeps your agents fast, efficient, and reliable by default, while giving you the controls to fully customize how context is managed for complex tasks. 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 

### **How does ADK deploy to production?** 

ADK is built for _deploy anywhere_ flexibility. You can containerize and run ADK on your own infrastructure, or take advantage of our native, one-command deployment to Google Cloud. When deploying to Google Cloud via Agent Runtime (Agent Platform), Cloud Run, or GKE, your agents instantly inherit managed infrastructure, built-in authentication, Cloud Trace observability, and enterprise-grade security—all without requiring you to change a single line of your agent code. Develop locally, scale globally. 

**When should I use an agent framework to work with generative AI?** 

AI chat conversations can accomplish many tasks, but when you need to accomplish complex, multistep processes, an agent framework lets you create a managed, repeatable task structure that 

### can run _hands-off_ with minimal human input. **Cookie consent** 

Agent frameworks like ADK can automatically We use cookies to recognize repeated visits and preferences, as initiate tasks, make multiple iterative AI model well as to measure the effectiveness of our documentation and requests, managwhether users find th information they need. With your consent, **e** context, handle tool calls, record you're helping us to make our documentation better. data, run parallel jobs, handle failures, and resume 

tasks if they get stopped. **Manage settings** 

### **Cookie consent** 

We use cookies to recognize repeated visits and preferences, as well as to measure the effectiveness of our documentation and whether users find the information they need. With your consent, you're helping us to make our documentation better. 

**Manage settings** 



## A2A key concepts

URL: https://a2a-protocol.org/latest/topics/key-concepts/

Home Documentation 

### Core Concepts and Components in A2A 

A2A uses a set of core concepts that define how agents interact. Understand these core building blocks to develop or integrate with A2A-compliant systems. 

### Core Actors in A2A Interactions 

- **User** : The end user, which can be a human operator or an automated service. The user initiates a request or defines a goal that requires assistance from one or more AI agents. 

- **A2A Client (Client Agent)** : An application, service, or another AI agent that acts on behalf of the user. The client initiates communication using the A2A protocol. 

- **A2A Server (Remote Agent)** : An AI agent or agentic system that exposes an HTTP endpoint implementing the A2A protocol. It receives requests from clients, processes tasks, and returns results or status updates. To the client, the remote agent is an _opaque_ (black-box) system: its internal workings, memory, and tools stay hidden. 

### Fundamental Communication Elements 

The following table describes the fundamental communication elements in A2A: 

|**Element**|**Description**|**Key Purpose**|
|---|---|---|
|Agent<br>Card|A JSON metadata<br>document describing an<br>agent's identity,<br>capabilities, endpoint,<br>skills, and authentication<br>requirements.|Enables clients to<br>discover agents and<br>understand how to<br>interact with them<br>securely and<br>effectively.|
|Task|A stateful unit of work<br>initiated by an agent, with<br>a unique ID and defined<br>lifecycle.|Facilitates tracking<br>of long-running<br>operations and<br>enables multi-turn<br>interactions and<br>collaboration.|
|Message|A single turn of<br>communication between<br>a client and an agent,<br>containing content and a<br>role ("user" or "agent").|Conveys<br>instructions,<br>context, questions,<br>answers, or status<br>updates that are not<br>necessarily formal<br>artifacts.|
|Part|The fundamental content<br>container used within<br>Messages and Artifacts. A<br>Part holds one of: text<br>content, a file reference<br>(URL or inline bytes), or<br>structured data.|Provides flexibility<br>for agents to<br>exchange various<br>content types within<br>messages and<br>artifacts.|

|**Element**|**Description**|**Key Purpose**|
|---|---|---|
|Artifact|A tangible output|Delivers the|
||generated by an agent|concrete results of|
||during a task (for|an agent's work,|
||example, a document,|ensuring structured|
||image, or structured|and retrievable|
||data).|outputs.|

### Interaction Mechanisms 

The A2A Protocol supports several interaction patterns. Each fits a different need for responsiveness and persistence. With them, agents exchange information reliably, whatever the task's complexity or duration: 

- **Request/Response (Polling)** : Clients send a request and the server responds. For long-running tasks, the client periodically polls the server for updates. 

- **Streaming with Server-Sent Events (SSE)** : Clients open a stream over an open HTTP connection. They receive real-time, incremental results or status updates from the server. 

- **Push Notifications** : The server calls a client-provided webhook on a significant task update. This suits very long-running tasks or disconnected clients. 

For more on streaming and push notifications, see Streaming & Asynchronous Operations. 

### Agent Cards 

The Agent Card is a JSON document. It acts as a digital business card. It gives key metadata for initial discovery and interaction setup. Clients parse it to decide whether an agent fits a task, how to structure requests, and how to communicate securely. The card lists identity, service endpoint (URL), A2A capabilities, authentication requirements, and skills. 

### Messages and Parts 

A message represents a single turn of communication between a client and an agent. It includes a role ("user" or "agent") and a unique `messageId` . It contains one or more Part objects, which are granular containers for the actual content. This design allows A2A to be modality independent. 

The `Part` object is a flexible container that can hold different types of content using a `oneof` field structure. A Part must contain exactly one of the following content fields: 

- `text` : A string containing plain textual content. 

- `raw` : A byte array containing binary file data (inline). 

- `url` : A string URI referencing external file content. 

- `data` : A structured JSON value (e.g., object, array) for machine- 

- readable data. 

Additionally, every `Part` can include: 

- `mediaType` : The MIME type of the content (e.g., `"text/plain"` , `"image/png"` , `"application/json"` ). 

- `filename` : An optional name for the file or content. 

- `metadata` : A key-value map for additional context. 

### Artifacts 

An artifact is a tangible output or concrete result that a remote agent generates during a task. Unlike general messages, artifacts are the actual deliverables. An artifact has a unique `artifactId` , a human-readable name, and one or more part objects. Artifacts tie closely to the task lifecycle and can be streamed to the client in increments. 

### Agent Response: Task or Message 

The agent response can be a new `Task` (when the agent needs to perform a long-running operation) or a `Message` (when the agent can 

respond immediately). 

For more details, see Life of a Task. 

### Other Important Concepts 

- **Context (** **`contextId` ):** A server-generated identifier. Use it to group related `Task` objects and carry context across a series of interactions. 

- **Transport and Format:** A2A communication occurs over HTTP(S). JSON-RPC 2.0 is used as the payload format for all requests and responses. 

- **Authentication & Authorization:** A2A relies on standard web security practices. Authentication requirements are declared in the Agent Card, and credentials (e.g., OAuth tokens, API keys) are typically passed through HTTP headers, separate from the A2A protocol messages themselves. For more information, see Enterprise-Ready Features. 

- **Agent Discovery:** The process by which clients find Agent Cards to learn about available A2A Servers and their capabilities. For more information, see Agent Discovery. 

- **Extensions:** A2A allows agents to declare custom protocol extensions as part of their AgentCard. For more information, see Extensions.
