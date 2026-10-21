# Architecture: Well-Architected Framework and reference designs / Google Cloud Well-Architected Framework (printable, all pillars): Continuously improve and innovate: Recommendations to Implement preemptive cyber defense: Principle overview
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 45-78, extracted 2026-10-18

## Google Cloud Well-Architected Framework (printable, all pillars)

URL: https://docs.cloud.google.com/architecture/framework/printable

### Recommendations

To continuously improve and innovate your cloud workloads, consider the recommendations in the following sections. Each recommendation in this document is relevant to one or more of the focus areas of operational readiness (/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

#### Foster a culture of learning

Encourage teams to experiment, share knowledge, and learn continuously. Adopt a blameless culture where failures are viewed as opportunities for growth and improvement. This recommendation is relevant to the workforce focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

When you foster a culture of learning, teams can learn from mistakes and iterate quickly. This approach encourages team members to take risks, experiment with new ideas, and expand the boundaries of their work. It also creates a psychologically safe environment where individuals feel comfortable sharing failures and learning from them. Sharing in this way leads to a more open and collaborative environment. 

To facilitate knowledge sharing and continuous learning, create opportunities for teams to share knowledge and learn from each other. You can do this through informal and formal learning sessions and conferences. 

By fostering a culture of experimentation, knowledge sharing, and continuous learning, you can create an environment where teams are empowered to take risks, innovate, and grow. This environment can lead to increased productivity, improved problem-solving, and a more engaged and motivated workforce. Further, by promoting a blameless culture, you can create a safe space for employees to learn from mistakes and contribute to the collective knowledge of the team. This culture ultimately leads to a more resilient and adaptable workforce that is better equipped to handle challenges and drive success in the long run. 

#### Conduct regular retrospectives

Retrospectives give teams an opportunity to reflect on their experiences, identify what went well, and identify what can be improved. By conducting retrospectives after projects or major incidents, teams can learn from successes and failures, and continuously improve their processes and practices. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

: processes and governance. 

An effective way to structure a retrospective is to use the _Start-Stop-Continue_ model: 

- **Start** : In the _Start_ phase of the retrospective, team members identify new practices, processes, and behaviors that they believe can enhance their work. They discuss why the changes are needed and how they can be implemented. 

- **Stop** : In the _Stop_ phase, team members identify and eliminate practices, processes, and behaviors that are no longer effective or that hinder progress. They discuss why these changes are necessary and how they can be implemented. 

- **Continue** : In the _Continue_ phase, team members identify practices, processes, and behaviors that work well and must be continued. They discuss why these elements are important and how they can be reinforced. 

By using a structured format like the Start-Stop-Continue model, teams can ensure that retrospectives are productive and focused. This model helps to facilitate discussion, identify the main takeaways, and identify actionable steps for future enhancements. 

#### Stay up-to-date with cloud technologies

To maximize the potential of Google Cloud services, you must keep up with the latest advancements, features, and best practices. This recommendation is relevant to the workforce focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

Participating in relevant conferences, webinars, and training sessions is a valuable way to expand your knowledge. These events provide opportunities to learn from Google Cloud experts, understand new capabilities, and engage with industry peers who might face similar challenges. By attending these sessions, you can gain insights into how to use new features effectively, optimize your cloud operations, and drive innovation within your organization. 

To ensure that your team members keep up with cloud technologies, encourage them to obtain certifications and attend training courses. Google Cloud offers a wide range of certifications (https://cloud.google.com/learn/certification) that validate skills and knowledge in specific cloud domains. Earning these certifications demonstrates commitment to excellence and provides tangible evidence of proficiency in cloud technologies. The training courses that are offered by Google Cloud and our partners delve deeper into specific topics. They provide direct experience and practical skills that can be immediately applied to real-world projects. By investing in the professional development of your team, you can foster a culture of continuous learning and ensure that everyone has the necessary skills to succeed in the cloud. 

#### Actively seek and incorporate feedback

Collect feedback from users, stakeholders, and team members. Use the feedback to identify opportunities to improve your cloud solutions. This recommendation is relevant to the workforce focus area of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) 

The feedback that you collect can help you to understand the evolving needs, issues, and expectations of the users of your solutions. This feedback serves as a valuable input to drive improvements and prioritize future enhancements. You can use various mechanisms to collect feedback: 

- **Surveys** are an effective way to gather quantitative data from a large number of users and stakeholders. 

- **User interviews** provide an opportunity for in-depth qualitative data collection. Interviews let you understand the specific challenges and experiences of individual users. 

- **Feedback forms** that are placed within the cloud solutions offer a convenient way for users to provide immediate feedback on their experience. 

- **Regular meetings** with team members can facilitate the collection of feedback on technical aspects and implementation challenges. 

The feedback that you collect through these mechanisms must be analyzed and synthesized to identify common themes and patterns. This analysis can help you prioritize future enhancements based on the impact and feasibility of the suggested improvements. By addressing the needs and issues that are identified through feedback, you can ensure that your cloud solutions continue to meet the evolving requirements of your users and stakeholders. 

#### Measure and track progress

Key performance indicators (KPIs) and metrics are crucial for tracking progress and measuring the effectiveness of your cloud operations. KPIs are quantifiable measurements that reflect the overall performance. Metrics are specific data points that contribute to the calculation of KPIs. Review the metrics regularly and use them to identify opportunities for improvement and measure progress. Doing so helps you to continuously improve and optimize your cloud environment. This recommendation is relevant to these focus areas of operational readiness 

(/architecture/framework/operational-excellence/operational-readiness-and-performanceusing-cloudops#focus-areas-of-operational-readiness) : governance and processes. 

A primary benefit of using KPIs and metrics is that they enable your organization to adopt a data-driven approach to cloud operations. By tracking and analyzing operational data, you can make informed decisions about how to improve the cloud environment. This data-driven approach helps you to identify trends, patterns, and anomalies that might not be visible without the use of systematic metrics. 

To collect and analyze operational data, you can use tools like Cloud Monitoring (/monitoring) and BigQuery (/bigquery). Cloud Monitoring enables real-time monitoring of cloud resources and services. BigQuery lets you store and analyze the data that you gather through monitoring. Using these tools together, you can create custom dashboards to visualize important metrics and trends. 

Operational dashboards can provide a centralized view of the most important metrics, which lets you quickly identify any areas that need attention. For example, a dashboard might include metrics like CPU utilization, memory usage, network traffic, and latency for a particular application or service. By monitoring these metrics, you can quickly identify any potential issues and take steps to resolve them. 

## Well-Architected Framework: Security, privacy, and compliance pillar

The Security, Privacy and Compliance pillar in the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you design, deploy, and operate cloud workloads that meet your requirements for security, privacy, and compliance. 

This document is designed to offer valuable insights and meet the needs of a range of security professionals and engineers. The following table describes the intended audiences for this document: 

|Audience|What this document provides|
|---|---|
|Chief information security<br>officers (CISOs), business unit<br>leaders, and IT managers|A general framework to establish and maintain security<br>excellence in the cloud and to ensure a comprehensive view of<br>security areas to make informed decisions about security<br>investments.|
|Security architects and<br>engineers|Key security practices for the design and operational phases to<br>help ensure that solutions are designed for security, efficiency,<br>and scalability.|
|DevSecOps teams|Guidance to incorporate overarching security controls to plan<br>automation that enables secure and reliable infrastructure.|
|Compliance officers and risk<br>managers|Key security recommendations to follow a structured approach<br>to risk management with safeguards that help to meet<br>compliance obligations.|

To ensure that your Google Cloud workloads meet your security, privacy, and compliance requirements, all of the stakeholders in your organization must adopt a collaborative approach. In addition, you must recognize that cloud security is a shared responsibility between you and Google. For more information, see Shared responsibilities and shared fate on Google Cloud 

(/architecture/framework/security/shared-responsibility-shared-fate). 

The recommendations in this pillar are grouped into core security principles. Each principle-based recommendation is mapped to one or more of the focus areas of cloud security (#focus_areas_of_cloud_security) that might be critical to your organization. Each recommendation highlights guidance about the use and configuration of Google Cloud products and capabilities to help improve your organization's security posture. 

### Evaluate workloads using an agent skill

To enable AI agents to evaluate your cloud workloads against the principles and recommendations in this pillar, use the `google-cloud-waf-security` 

(https://github.com/google/skills/tree/main/skills/cloud/google-cloud-waf-security) skill, which is available in the Google Agent Skills repository in GitHub. 

To install the skill, run the following command in your agent's client or terminal: 

```
npx skills add google/skills --skill google-cloud-waf-security
```

When prompted, specify the AI agents for which you want to install the skill and set the installation scope (project or global). 

**Note:** If **`npx`** is not available in your environment, install Node.js (https://nodejs.org/en/download), which includes **`npm`** and **`npx`** . 

### Core principles

The recommendations in this pillar are grouped within the following core principles of security. Every principle in this pillar is important. Depending on the requirements of your organization and workload, you might choose to prioritize certain principles. 

Implement security by design 

- (/architecture/framework/security/implement-security-by-design): Integrate cloud security and network security considerations starting from the initial design phase of your applications and infrastructure. Google Cloud provides architecture blueprints and recommendations to help you apply this principle. 

- Implement zero trust (/architecture/framework/security/implement-zero-trust): Use a _never trust, always verify_ approach, where access to resources is granted based on continuous verification of trust. Google Cloud supports this principle through products like Chrome Enterprise Premium and Identity-Aware Proxy (IAP). 

Implement shift-left security 

- (/architecture/framework/security/implement-shift-left-security): Implement security controls early in the software development lifecycle. Avoid security defects before system changes are made. Detect and fix security bugs early, fast, and reliably after the system changes are committed. Google Cloud supports this principle through products like Cloud Build, Binary Authorization, and Artifact Registry. 

Implement preemptive cyber defense 

- (/architecture/framework/security/implement-preemptive-cyber-defense): Adopt a proactive approach to security by implementing robust fundamental measures like threat intelligence. This approach helps you build a foundation for more effective threat detection and response. Google Cloud's approach to layered security controls 

(/docs/security/overview/whitepaper#technology_with_security_at_its_core) aligns with this principle. 

Use AI securely and responsibly 

- (/architecture/framework/security/use-ai-securely-and-responsibly): Develop and deploy AI systems in a responsible and secure manner. The recommendations for this principle are aligned with guidance in the AI and ML perspective (/architecture/framework/perspectives/ai-ml) of the Well-Architected Framework and in Google's Secure AI Framework (SAIF) (https://saif.google). 

- Use AI for security (/architecture/framework/security/use-ai-for-security): Use AI capabilities to improve your existing security systems and processes through Gemini in Security (https://cloud.google.com/security/ai) and overall platformsecurity capabilities. Use AI as a tool to increase the automation of remedial work and ensure security hygiene to make other systems more secure. 

- Meet regulatory, compliance, and privacy needs 

- (/architecture/framework/security/meet-regulatory-compliance-and-privacy-needs): Adhere to industry-specific regulations, compliance standards, and privacy requirements. Google Cloud helps you meet these obligations through products like Assured Workloads, Organization Policy Service, and our compliance resource center (https://cloud.google.com/security/compliance/). 

### Organizational security mindset

A security-focused organizational mindset is crucial for successful cloud adoption and operation. This mindset should be deeply ingrained in your organization's culture and reflected in its practices, which are guided by core security principles as described earlier. 

An organizational security mindset emphasizes that you think about security during system design, assume zero trust, and integrate security features throughout your development process. In this mindset, you also think proactively about cyber-defense measures, use AI securely and for security, and consider your regulatory, privacy, and compliance requirements. By embracing these principles, your organization can cultivate a security-first culture that proactively addresses threats, protects valuable assets, and helps to ensure responsible technology usage. 

### Focus areas of cloud security

This section describes the areas for you to focus on when you plan, implement, and manage security for your applications, systems, and data. The recommendations in each principle of this pillar are relevant to one or more of these focus areas. Throughout the rest of this document, the recommendations specify the corresponding security focus areas to provide further clarity and context. 

|Focus area|Activities and components<br> <br>|Related Google Cloud products, capabilities,<br>and solutions|
|---|---|---|
|Infrastructure<br>security|Secure network infrastructure.<br>Encrypt data in transit and at<br>rest.<br>Control traffic flow.<br>Secure IaaS and PaaS<br>services.<br>Protect against unauthorized<br>access.|Firewall Policies<br>(/firewall/docs/firewall-policies-overview)<br>VPC Service Controls<br>(/vpc-service-controls/docs/overview)<br>Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>Cloud Next Generation Firewall<br>(/firewall/docs/about-firewalls)<br>Secure Web Proxy<br>(/secure-web-proxy/docs/overview)|
|Identity and<br>access<br>management|Use authentication,<br>authorization, and access<br>controls.<br>Manage cloud identities.<br>Manage identity and access<br>management policies.|Cloud Identity(/identity/docs/overview)<br>Google's Identity and Access<br>Management (IAM) service<br>(/iam/docs/overview)<br>Workforce Identity Federation<br>(/iam/docs/workforce-identity-federation)<br>Workload Identity Federation<br>(/iam/docs/workload-identity-federation)|
|Data security|Store data in Google Cloud<br>securely.<br>Control access to the data.<br>Discover and classify the data.<br>Design necessary controls,<br>such as encryption, access<br>controls, and data loss<br>prevention.<br>Protect data at rest, in transit,<br>and in use.|Google's IAM service<br>(/iam/docs/overview)<br>Sensitive Data Protection<br>(/sensitive-data-<br>protection/docs/sensitive-data-protection-<br>overview)<br>VPC Service Controls<br>(/vpc-service-controls/docs/overview)<br>Cloud KMS<br>(/kms/docs/key-management-service)<br>Confidential Computing<br>(/confidential-<br>computing/docs/confidential-computing-<br>overview)|

|Focus area|Activities and components|Related Google Cloud products, capabilities,<br>and solutions|
|---|---|---|
|AI and ML<br>security|Apply security controls at<br>different layers of the AI and<br>ML infrastructure and pipeline.<br>Ensure model safety.|Google's SAIF(https://saif.google/)<br>Model Armor<br>(/security-command-center/docs/model-<br>armor-overview)|
|Security<br>operations<br>(SecOps)|Adopt a modern SecOps<br>platform and set of practices,<br>for effective incident<br>management, threat<br>detection, and response<br>processes.<br>Monitor systems and<br>applications continuously for<br>security events.|Google Security Operations<br>(/chronicle/docs/secops/secops-overview)|
|Application<br>security|Secure applications against<br>software vulnerabilities and<br>attacks.|Artifact Registry<br>(/artifact-registry/docs/overview)<br>Artifact Analysis<br>(/artifact-analysis/docs/artifact-analysis)<br>Binary Authorization<br>(/binary-authorization/docs/overview)<br>Assured Open Source Software<br>(/assured-open-source-<br>software/docs/overview)<br>Google Cloud Armor<br>(/armor/docs/cloud-armor-overview)<br>Web Security Scanner<br>(/security-command-<br>center/docs/concepts-web-security-<br>scanner-overview)|

|Focus area|Activities and components|Related Google Cloud products, capabilities,<br>and solutions|
|---|---|---|
|Cloud<br>governance,<br>risk, and<br>compliance|Establish policies, procedures,<br>and controls to manage cloud<br>resources effectively and<br>securely.|Organization Policy Service<br>(/resource-manager/docs/organization-<br>policy/overview)<br>Cloud Asset Inventory<br>(/asset-inventory/docs/asset-inventory-<br>overview)<br>Security Command Center Enterprise<br>(/security-command-<br>center/docs/security-command-center-<br>overview)<br>Resource Manager<br>(/resource-manager/docs)|
|Logging,<br>auditing, and<br>monitoring|Analyze logs to identify<br>potential threats.<br>Track and record system<br>activities for compliance and<br>security analysis.|Cloud Logging(/logging/docs/overview)<br>Cloud Monitoring<br>(/monitoring/docs/monitoring-overview)<br>Cloud Audit Logs(/logging/docs/audit)<br>VPC Flow Logs(/vpc/docs/flow-logs)|

### Contributors

Authors: 

- Wade Holmes (https://www.linkedin.com/in/wholmes) | Global Solutions Director 

- Hector Diaz (https://www.linkedin.com/in/hectorgdiaz) | Cloud Security Architect 

- Carlos Leonardo Rosario | Google Cloud Security Specialist 

- John Bacon (https://www.linkedin.com/in/johnbac/) | Partner Solutions Architect 

- Sachin Kalra (http://www.linkedin.com/in/thesachinkalra) | Global Security Solution Manager 

Other contributors: 

- Anton Chuvakin (https://www.linkedin.com/in/chuvakin/) | Security Advisor, Office of the CISO 

- Daniel Lees (https://www.linkedin.com/in/daniellees) | Cloud Security Architect 

- Filipe Gracio, PhD (https://www.linkedin.com/in/filipegracio) | Customer Engineer, AI/ML Specialist 

- Gary Harmson (https://www.linkedin.com/in/garyharmson) | Principal Architect 

- Gino Pelliccia (https://www.linkedin.com/in/gino-pelliccia-13637025) | Principal Architect 

- Jose Andrade (https://www.linkedin.com/in/jmandrade) | Customer Engineer, SRE Specialist 

- Kumar Dhanagopal (https://www.linkedin.com/in/kumardhanagopal) | Cross-Product Solution Developer 

- Laura Hyatt (https://www.linkedin.com/in/laura-hyatt) | Customer Engineer, FSI 

- Marwan Al Shawi (https://www.linkedin.com/in/marwanalshawi) | Partner Customer Engineer 

- Nicolas Pintaux (https://www.linkedin.com/in/nicolaspintaux) | Customer Engineer, Application Modernization Specialist 

- Noah McDonald (https://www.linkedin.com/in/noah-mcdonald-77b04a173) | Cloud Security Consultant 

- Osvaldo Costa (https://www.linkedin.com/in/osvaldocostajr) | Networking Specialist Customer Engineer 

- Radhika Kanakam (https://www.linkedin.com/in/radhika-kanakam-18ab876) | Program Lead, Google Cloud Well-Architected Framework 

- Samantha He (https://www.linkedin.com/in/samantha-he-05a98173) | Technical Writer 

- Susan Wu (https://www.linkedin.com/in/susanwu88) | Outbound Product Manager 

## Implement security by design

This principle in the security pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to incorporate robust security features, controls, and practices into the design of your cloud applications, services, and platforms. From ideation to operations, security is more effective when it's embedded as an integral part of every stage of your design process. 

### Principle overview

As explained in An Overview of Google's Commitment to Secure by Design (https://static.googleusercontent.com/media/publicpolicy.google/en//resources/google_commit ment_secure_by_design_overview.pdf) 

, _secure by default_ and _secure by design_ are often used interchangeably, but they represent distinct approaches to building secure systems. Both approaches aim to minimize vulnerabilities and enhance security, but they differ in scope and implementation: 

- **Secure by default** : focuses on ensuring that a system's default settings are set to a secure mode, minimizing the need for users or administrators to take actions to secure the system. This approach aims to provide a baseline level of security for all users. 

- **Secure by design** : emphasizes proactively incorporating security considerations throughout a system's development lifecycle. This approach is about anticipating potential threats and vulnerabilities early and making design choices that mitigate risks. This approach involves using secure coding practices, conducting security reviews, and embedding security throughout the design process. The secure-by-design approach is an overarching philosophy that guides the development process and helps to ensure that security isn't an afterthought but is an integral part of a system's design. 

### Recommendations

To implement the secure by design principle for your cloud workloads, consider the recommendations in the following sections: 

- Choose system components that help to secure your workloads 

- (#choose-system-components) 

Build a layered security approach (#build_a_layered_security_approach) 

- Use hardened and attested infrastructure and services 

- (#use_hardened_and_attested_infrastructure_and_services) 

Encrypt data at rest and in transit (#encrypt_data_at_rest_and_in_transit) 

#### Choose system components that help to secure your workloads

This recommendation is relevant to all of the focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security). 

A fundamental decision for effective security is the selection of robust system components—including both hardware and software components—that constitute your platform, solution, or service. To reduce the security attack surface and limit potential damage, you must also carefully consider the deployment patterns of these components and their configurations. 

In your application code, we recommend that you use straightforward, safe, and reliable libraries, abstractions, and application frameworks in order to eliminate classes of vulnerabilities. To scan for vulnerabilities in software libraries, you can use third-party tools. You can also use Assured Open Source Software 

(https://cloud.google.com/security/products/assured-open-source-software), which helps to reduce risks to your software supply chain by using open source software (OSS) packages that Google uses and secures. 

Your infrastructure must use networking, storage, and compute options that support safe operation and align with your security requirements and risk acceptance levels. Infrastructure security is important for both internet-facing and internal workloads. 

For information about other Google solutions that support this recommendation, see Implement shift-left security 

(/architecture/framework/security/implement-shift-left-security). 

#### Build a layered security approach

This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

- AI and ML security 

- Infrastructure security 

- Identity and access management 

- Data security 

We recommend that you implement security at each layer of your application and infrastructure stack by applying a defense-in-depth approach. 

Use the security features in each component of your platform. To limit access and identify the boundaries of the potential impact (that is, the _blast radius_ ) in the event of a security incident, do the following: 

- Simplify your system's design to accommodate flexibility where possible. Document the security requirements of each component. 

- Incorporate a robust secured mechanism to address resiliency and recovery requirements. 

When you design the security layers, perform a risk assessment to determine the security features that you need in order to meet internal security requirements and external regulatory requirements. We recommend that you use an industrystandard risk assessment framework that applies to cloud environments and that is relevant to your regulatory requirements. For example, the Cloud Security Alliance (CSA) provides the Cloud Controls Matrix (CCM) 

(https://cloudsecurityalliance.org/research/cloud-controls-matrix/). Your risk assessment provides you with a catalog of risks and corresponding security controls to mitigate them. 

When you perform the risk assessment, remember that you have a shared responsibility arrangement with your cloud provider. Therefore, your risks in a cloud environment differ from your risks in an on-premises environment. For example, in an on-premises environment, you need to mitigate vulnerabilities to your hardware stack. In contrast, in a cloud environment, the cloud provider bears these risks. Also, remember that the boundaries of shared responsibilities differ between IaaS, PaaS, and SaaS services for each cloud provider. 

After you identify potential risks, you must design and create a mitigation plan that uses technical, administrative, and operational controls, as well as contractual protections and third-party attestations. In addition, a threat modeling method, such as the OWASP application threat modeling method 

(https://owasp.org/www-project-threat-modeling/), helps you to identify potential gaps and suggest actions to address the gaps. 

#### Use hardened and attested infrastructure and services

This recommendation is relevant to all of the focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security). 

A mature security program mitigates new vulnerabilities as described in security bulletins. The security program should also provide remediation to fix vulnerabilities in existing deployments and secure your VM and container images. You can use hardening guides that are specific to the OS and application of your images, as well as benchmarks like the one provided by the Center of Internet Security (CIS) (https://www.cisecurity.org/benchmark/google_cloud_computing_platform). 

If you use custom images for your Compute Engine VMs, you need to patch the images yourself. Alternatively, you can use Google-provided curated OS images (/compute/docs/images), which are patched regularly. To run containers on Compute Engine VMs, use Google-curated Container-optimized OS images 

(/container-optimized-os/docs). Google regularly patches and updates these images. 

If you use GKE, we recommend that you enable node auto-upgrades (/kubernetes-engine/docs/how-to/node-auto-upgrades) so that Google updates your cluster nodes with the latest patches. Google manages GKE control planes, which are automatically updated and patched. To further reduce the attack surface of your containers, you can use distroless images 

(https://github.com/GoogleContainerTools/distroless). Distroless images are ideal for security-sensitive applications, microservices, and situations where minimizing the image size and attack surface is paramount. 

For sensitive workloads, use Shielded VM (/compute/shielded-vm/docs/shielded-vm), which prevents malicious code from being loaded during the VM boot cycle. Shielded VM instances provide boot security, monitor integrity, and use the Virtual Trusted Platform Module (vTPM) (/compute/shielded-vm/docs/shielded-vm#vtpm). 

To help secure SSH access, OS Login (/compute/docs/oslogin) lets your employees connect to your VMs by using Identity and Access Management (IAM) permissions (/compute/docs/oslogin/set-up-oslogin#configure_users) as the source of truth instead of relying on SSH keys. Therefore, you don't need to manage SSH keys throughout your organization. OS Login ties an administrator's access to their employee lifecycle, so when employees change roles or leave your organization, their access is revoked with their account. OS Login also supports Google two-factor authentication (https://support.google.com/accounts/answer/185839), which adds an extra layer of security against account takeover attacks. 

In GKE, application instances run within Docker containers. To enable a defined risk profile and to restrict employees from making changes to containers, ensure that your containers are stateless and immutable. The immutability principle means that your employees don't modify the container or access it interactively. If the container must be changed, you build a new image and redeploy that image. Enable SSH access to the underlying containers only in specific debugging scenarios. 

To help globally secure configurations across your environment, you can use organization policies (/resource-manager/docs/organization-policy/overview) to set constraints or guardrails on resources that affect the behavior of your cloud assets. For example, you can define the following organization policies and apply them either globally across a Google Cloud organization or selectively at the level of a folder or project: 

- Disable external IP address allocation to VMs. 

- Restrict resource creation to specific geographical locations. 

- Disable the creation of Service Accounts or their keys. 

#### Encrypt data at rest and in transit

This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

- Infrastructure security 

- Data security 

Data encryption is a foundational control to protect sensitive information, and it's a key part of data governance (https://cloud.google.com/learn/what-is-data-governance). An effective data protection strategy includes access control, data segmentation and geographical residency, auditing, _and_ encryption implementation that's based on a careful assessment of requirements. 

By default, Google Cloud encrypts customer data that's stored at rest 

(/docs/security/encryption/default-encryption), with no action required from you. In addition to default encryption, Google Cloud provides options for envelope encryption and encryption key management. You must identify the solutions that best fit your requirements for key generation, storage, and rotation, whether you're choosing the keys for your storage, for compute, or for big data workloads. For example, Customer-managed encryption keys (CMEKs) (/kms/docs/cmek) can be created in Cloud Key Management Service (Cloud KMS) (/kms/docs/kms-autokey). The CMEKs can be either software-based or HSM-protected (/kms/docs/hsm) to meet your regulatory or compliance requirements, such as the need to rotate encryption keys regularly. Cloud KMS Autokey lets you automate the provisioning and assignment of CMEKs. In addition, you can bring your own keys that are sourced from a thirdparty key management system by using Cloud External Key Manager (Cloud EKM) (/kms/docs/ekm). 

We strongly recommend that data be encrypted in-transit. Google encrypts and authenticates data in transit (/docs/security/encryption-in-transit) at one or more network layers when data moves outside physical boundaries that aren't controlled by Google or on behalf of Google. All VM-to-VM traffic within a VPC network and between peered VPC networks is encrypted. You can use MACsec 

(/network-connectivity/docs/interconnect/concepts/macsec-overview) for encryption of traffic over Cloud Interconnect connections. IPsec provides encryption for traffic over Cloud VPN (/network-connectivity/docs/vpn/concepts/overview) connections. You can protect application-to-application traffic in the cloud by using security features like TLS and mTLS confgurations in Apigeei (/apigee/docs/hybrid/v1.14/ingress-tls) and Cloud Service Mesh (https://cloud.google.com/products/service-mesh) for containerized applications. 

By default, Google Cloud encrypts data at rest and data in transit across the network. However, data isn't encrypted by default while it's in use in memory. If your organization handles confidential data, you need to mitigate any threats that undermine the confidentiality and integrity of either the application or the data in system memory. To mitigate these threats, you can use Confidential Computing, 

which provides a trusted execution environment for your compute workloads. For more information, see Confidential VM overview 

(/confidential-computing/confidential-vm/docs/confidential-vm-overview). 

## Implement zero trust

This principle in the security pillar of the Google Cloud Well-Architected Framework (/architecture/framework) helps you ensure comprehensive security across your cloud workloads. The principle of zero trust emphasizes the following practices: 

- Eliminating implicit trust 

- Applying the principle of least privilege to access control 

- Enforcing explicit validation of all access requests 

- Adopting an _assume-breach_ mindset to enable continuous verification and security posture monitoring 

### Principle overview

The _zero-trust_ model shifts the security focus from perimeter-based security to an approach where no user or device is considered to be inherently trustworthy. Instead, every access request must be verified, regardless of its origin. This approach involves authenticating and authorizing every user and device, validating their context (location and device posture), and granting least privilege access to only the necessary resources. 

Implementing the zero-trust model helps your organization enhance its security posture by minimizing the impact of potential breaches and protecting sensitive data and applications against unauthorized access. The zero-trust model helps you ensure confidentiality, integrity, and availability of data and resources in the cloud. 

### Recommendations

To implement the zero-trust model for your cloud workloads, consider the recommendations in the following sections: 

- Secure your network (#secure_your_network) 

- Verify every access attempt explicitly (#verify_every_access_attempt_explicitly) 

- Monitor and maintain your network (#monitor_and_maintain_your_network) 

#### Secure your network

This recommendation is relevant to the following focus area (/architecture/framework/security#focus_areas_of_cloud_security): Infrastructure security. 

Transitioning from conventional perimeter-based security to a zero-trust model requires multiple steps. Your organization might have already integrated certain zero-trust controls into its security posture. However, a zero-trust model isn't a singular product or solution. Instead, it's a holistic integration of multiple security layers and best practices. This section describes recommendations and techniques to implement zero trust for network security. 

- **Access control** : Enforce access controls based on user identity and context by using solutions like Chrome Enterprise Premium 

- (https://chromeenterprise.google/products/chrome-enterprise-premium/) and IdentityAware Proxy (IAP) (/iap/docs/concepts-overview). By doing this, you shift security from the network perimeter to individual users and devices. This approach enables granular access control and reduces the attack surface. 

- **Network security** : Secure network connections between your on-premises, Google Cloud, and multicloud environments. 

   - Use the private connectivity methods from Cloud Interconnect 

   - (/network-connectivity/docs/interconnect/concepts/overview) and IPsec VPNs (/network-connectivity/docs/vpn/concepts/overview). 

   - To help secure access to Google Cloud services and APIs, use Private Service Connect (/vpc/docs/private-service-connect). 

   - To help secure outbound access from workloads deployed on Google Kubernetes Engine (GKE) 

   - (/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and related 

   - products, use Cloud Service Mesh egress gateways 

   - (/service-mesh/docs/security/egress-gateways-best-practices). 

- **Network design** : Prevent potential security risks by deleting default networks in existing projects and disabling the creation of default networks in new projects. 

   - To avoid conflicts, plan your network and IP address allocation carefully. 

   - To enforce effective access control, limit the number of Virtual Private Cloud (VPC) networks per project. 

- **Segmentation** : Isolate workloads but maintain centralized network management. 

   - To segment your network environments, use multiple VPC networks and define firewall policies and rules at the organization, folder, and VPC network levels. 

   - To centralize network administration for resources that are in separate projects, use Shared VPC (/vpc/docs/shared-vpc). For example, administrators of a service project can create Compute Engine instances that use approved subnets from the project that hosts a centrally administered Shared VPC network. 

   - To prevent data exfltrationi (https://en.wikipedia.org/wiki/Data_exfiltration), establish secure perimeters around sensitive Google Cloud APIs and services by using VPC Service Controls (/vpc-service-controls/docs/overview), and use strict egress firewall rules to restrict internet-bound traffic. 

- **Perimeter security** : Protect against DDoS attacks and web application threats. 

   - To protect against threats, use Google Cloud Armor (/armor/docs). 

   - Configure security policies to allow, deny, or redirect traffic at the Google Cloud edge. 

- **Automation** : Automate infrastructure provisioning by embracing infrastructure as code (IaC) principles and by using tools like Terraform, Jenkins, and Cloud Build (/build/docs/overview). IaC helps to ensure consistent security configurations, simplified deployments, and rapid rollbacks in case of issues. 

- **Secure foundation** : Establish a secure application environment by using the Enterprise foundations blueprint (/architecture/blueprints/security-foundations). This blueprint provides prescriptive guidance and automation scripts to help you implement security best practices and configure your Google Cloud resources securely. 

#### Verify every access attempt explicitly

This recommendation is relevant to the following focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security): 

- Identity and access management 

- Security operations (SecOps) 

- Logging, auditing, and monitoring 

Implement strong authentication and authorization mechanisms for any user, device, or service that attempts to access your cloud resources. Don't rely on location or network perimeter as a security control. Don't automatically trust any user, device, or service, even if they are already inside the network. Instead, every attempt to access resources must be rigorously authenticated and authorized. You must implement strong identity verification measures, such as multi-factor authentication (MFA). You must also ensure that access decisions are based on granular policies that consider various contextual factors like user role, device posture, and location. 

To implement this recommendation, use the following methods, tools, and technologies: 

- **Unified identity management** : Ensure consistent identity management across your organization by using a single identity provider (IdP). 

   - Google Cloud supports federation with most IdPs, including on-premises Active Directory 

   - (/architecture/identity/federating-gcp-with-active-directory-introduction). Federation lets you extend your existing identity management infrastructure to Google Cloud and enable single sign-on (SSO) for users. 

   - If you don't have an existing IdP, consider using Cloud Identity Premium (/identity/docs/editions) or Google Workspace (https://workspace.google.com/). 

- **Limited service account permissions** : Use service accounts 

- (/iam/docs/service-account-overview) carefully, and adhere to the principle of least privilege. 

   - Grant only the necessary permissions required for each service account to perform its designated tasks. 

   - Use Workload Identity Federation (/iam/docs/workload-identities) for applications that run on Google Kubernetes Engine (GKE) or run outside Google Cloud to access resources securely. 

- **Robust processes** : Update your identity processes to align with cloud security best practices. 

   - To help ensure compliance with regulatory requirements, implement identity governance to track access, risks, and policy violations. 

   - Review and update your existing processes for granting and auditing access-control roles and permissions. 

- **Strong authentication** : Implement SSO for user authentication and implement MFA for privileged accounts. 

   - Google Cloud supports various MFA methods, including Titan Security Keys (https://cloud.google.com/security/products/titan-security-key), for enhanced security. 

   - For workload authentication, use OAuth 2.0 or signed JSON Web Tokens (JWTs). 

- **Least privilege** : Minimize the risk of unauthorized access and data breaches by enforcing the principles of least privilege and separation of duties. 

   - Avoid overprovisioning user access. 

   - Consider implementing just-in-time privileged access for sensitive operations. 

- **Logging** : Enable audit logging for administrator and data access activities. 

   - For analysis and threat detection, scan the logs by using Security Command Center Enterprise 

   - (/security-command-center/docs/service-tiers#enterprise-tier) or Google Security Operations (/chronicle/docs/secops/secops-overview). 

- Configure appropriate log retention policies to balance security needs with storage costs. 

#### Monitor and maintain your network

This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

- Logging, auditing, and monitoring 

- Application security 

- Security operations (SecOps) 

- Infrastructure security 

When you plan and implement security measures, assume that an attacker is already inside your environment. This proactive approach involves using the following multiple tools and techniques to provide visibility into your network: 

- **Centralized logging and monitoring** : Collect and analyze security logs from all of your cloud resources through centralized logging and monitoring (/stackdriver/docs). 

   - Establish baselines for normal network behavior, detect anomalies, and identify potential threats. 

   - Continuously analyze network traffic flows to identify suspicious patterns and potential attacks. 

- **Insights into network performance and security** : Use tools like Network Analyzer (/network-intelligence-center/docs/network-analyzer/overview). Monitor traffic for unusual protocols, unexpected connections, or sudden spikes in data transfer, which could indicate malicious activity. 

- **Vulnerability scanning and remediation** : Regularly scan your network and applications for vulnerabilities. 

   - Use Web Security Scanner 

   - (/security-command-center/docs/concepts-vulnerabilities-findings), which can automatically identify vulnerabilities in your Compute Engine instances, containers, and GKE clusters. 

   - Prioritize remediation based on the severity of vulnerabilities and their potential impact on your systems. 

- **Intrusion detection** : Monitor network traffic for malicious activity and automatically block or get alerts for suspicious events by using Cloud IDS (/intrusion-detection-system/docs/overview) and Cloud NGFW intrusion prevention service (/firewall/docs/about-intrusion-prevention). 

- **Security analysis** : Consider implementing Google SecOps (/chronicle/docs/secops/secops-overview) to correlate security events from various sources, provide real-time analysis of security alerts, and facilitate incident response. 

- **Consistent configurations** : Ensure that you have consistent security configurations across your network by using configuration management tools. 

## Implement shift-left security

This principle in the security pillar of the Google Cloud Well-Architected Framework (/architecture/framework) helps you identify practical controls that you can implement early in the software development lifecycle to improve your security posture. It provides recommendations that help you implement preventive security guardrails and post-deployment security controls. 

### Principle overview

_Shift-left security_ means adopting security practices early in the software development lifecycle. This principle has the following goals: 

- Avoid security defects before system changes are made. Implement preventive security guardrails and adopt practices such as infrastructure as code (IaC), policy as code, and security checks in the CI/CD pipeline. You can also use other platform-specific capabilities like Organization Policy Service (/resource-manager/docs/organization-policy/overview) and hardened GKE clusters (/kubernetes-engine/docs/how-to/hardening-your-cluster) in Google Cloud. 

- Detect and fix security bugs early, fast, and reliably after any system changes are committed. Adopt practices like code reviews, post-deployment vulnerability scanning, and security testing. 

The Implement security by design 

(/architecture/framework/security/implement-security-by-design) and shift-left security principles are related but they differ in scope. The security-by-design principle helps you to avoid fundamental design flaws that would require re-architecting the entire system. For example, a threat-modeling exercise reveals that the current design doesn't include an authorization policy, and all users would have the same level of access without it. Shift-left security helps you to avoid implementation defects (bugs and misconfigurations) before changes are applied, and it enables fast, reliable fixes after deployment. 

### Recommendations

To implement the shift-left security principle for your cloud workloads, consider the recommendations in the following sections: 

- Adopt preventive security controls (#adopt_preventive_security_controls) 

- Automate provisioning and management of cloud resources (#automate_provisioning_and_management_of_cloud_resources) 

- Automate secure application releases (#automate_secure_application_releases) 

- Ensure that application deployments follow approved processes 

- (#ensure_that_application_deployments_follow_approved_processes) 

- Scan for known vulnerabilities before application deployment (#scan_for_known_vulnerabilities_before_application_deployment) 

- Monitor your application code for known vulnerabilities (#monitor_your_application_code_for_known_vulnerabilities) 

#### Adopt preventive security controls

This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

Identity and access management 

Cloud governance, risk, and compliance 

Preventive security controls are crucial for maintaining a strong security posture in the cloud. These controls help you proactively mitigate risks. You can prevent misconfigurations and unauthorized access to resources, enable developers to work efficiently, and help ensure compliance with industry standards and internal policies. 

Preventive security controls are more effective when they're implemented by using infrastructure as code (IaC). With IaC, preventive security controls can include more customized checks on the infrastructure code before changes are deployed. When combined with automation, preventive security controls can run as part of your CI/CD pipeline's automatic checks. 

The following products and Google Cloud capabilities can help you implement preventive controls in your environment: 

- Organization Policy Service constraints 

- (/resource-manager/docs/organization-policy/overview): configure predefined and custom constraints with centralized control. 

- VPC Service Controls (https://cloud.google.com/security/vpc-service-controls): create perimeters around your Google Cloud services. 

- Identity and Access Management (IAM), Privileged Access Manager (/iam/docs/pam-overview), and principal access boundary policies 

- (/iam/docs/principal-access-boundary-policies): restrict access to resources. 

- Policy Controller (/kubernetes-engine/policy-controller/docs/overview) and Open Policy Agent (OPA) (https://www.openpolicyagent.org/): enforce IaC constraints in your CI/CD pipeline and avoid cloud misconfigurations. 

IAM lets you authorize _who_ can act on specific resources based on permissions. For more information, see Access control for organization resources with IAM 

(/resource-manager/docs/access-control-org). 

Organization Policy Service lets you set restrictions on resources to specify how they can be configured. For example, you can use an organization policy to do the following: 

Limit resource sharing 

- (/resource-manager/docs/organization-policy/restricting-domains) based on domain. 

- Limit the use of service accounts 

- (/resource-manager/docs/organization-policy/restricting-service-accounts). 

- Restrict the physical location 

- (/resource-manager/docs/organization-policy/defining-locations) of newly created resources. 

In addition to using organizational policies, you can restrict access to resources by using the following methods: 

- Tags with IAM (/iam/docs/tags-access-control): assign a tag to a set of resources and then set the access definition for the tag itself, rather than defining the access permissions on each resource. 

- IAM Conditions (/iam/docs/conditions-overview): define conditional, attributebased access control for resources. 

- Defense in depth: use VPC Service Controls to further restrict access to resources. 

For more information about resource management, see Decide a resource hierarchy for your Google Cloud landing zone 

(/architecture/landing-zones/decide-resource-hierarchy). 

#### Automate provisioning and management of cloud resources

This recommendation is relevant to the following focus areas 

- (/architecture/framework/security#focus_areas_of_cloud_security): 

   - Application security 

   - Cloud governance, risk, and compliance 

Automating the provisioning and management of cloud resources and workloads is more effective when you also adopt declarative IaC, as opposed to imperative scripting. IaC isn't a security tool or practice on its own, but it helps you to improve the security of your platform. Adopting IaC lets you create repeatable infrastructure and provides your operations team with a known good state. IaC also improves the efficiency of rollbacks, audit changes, and troubleshooting. 

When combined with CI/CD pipelines and automation, IaC also gives you the ability to adopt practices such as _policy as code_ with tools like OPA. You can audit infrastructure changes over time and run automatic checks on the infrastructure code before changes are deployed. 

To automate the infrastructure deployment, you can use tools like Config Controller (/kubernetes-engine/enterprise/config-controller/docs/overview), Terraform, Jenkins, and Cloud Build (/build). To help you build a secure application environment using IaC and automation, Google Cloud provides the enterprise foundations blueprint 

(/architecture/blueprints/security-foundations). This blueprint is Google's opinionated design that follows all of our recommended practices and configurations. The blueprint provides step-by-step instructions to configure and deploy your Google Cloud topology by using Terraform and Cloud Build. 

You can modify the scripts of the enterprise foundations blueprint to configure an environment that follows Google recommendations and meets your own security requirements. You can further build on the blueprint with additional blueprints or design your own automation. The Google Cloud Architecture Center provides other blueprints that can be implemented on top of the enterprise foundations blueprint. The following are a few examples of these blueprints: 

- Deploy an enterprise developer platform on Google Cloud 

- (/architecture/blueprints/enterprise-application-blueprint) 

- Deploy a secured serverless architecture using Cloud Run 

- (/architecture/blueprints/serverless-blueprint) 

- Build and deploy generative AI and machine learning models in an enterprise (/architecture/blueprints/genai-mlops-blueprint) 

- Import data from Google Cloud into a secured BigQuery data warehouse (/architecture/blueprints/confidential-data-warehouse-blueprint) 

#### Automate secure application releases

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Application security. 

Without automated tools, it can be difficult to deploy, update, and patch complex application environments to meet consistent security requirements. We 

recommend that you build automated CI/CD pipelines for your software development lifecycle (SDLC). Automated CI/CD pipelines help you to remove manual errors, provide standardized development feedback loops, and enable efficient product iterations. Continuous delivery is one of the best practices that the DORA framework (https://dora.dev/research/?view=detail) recommends. 

Automating application releases by using CI/CD pipelines helps to improve your ability to detect and fix security bugs early, fast, and reliably. For example, you can scan for security vulnerabilities automatically when artifacts are created, narrow the scope of security reviews, and roll back to a known and safe version. You can also define policies for different environments (such as development, test, or production environments) so that only verified artifacts are deployed. 

To help you automate application releases and embed security checks in your CI/CD pipeline, Google Cloud provides multiple tools including Cloud Build (/build), Cloud Deploy (/deploy/docs), Web Security Scanner 

(/security-command-center/docs/concepts-web-security-scanner-overview), and Binary Authorization (/binary-authorization/docs). 

To establish a process that verifies multiple security requirements in your SDLC, use the Supply-chain Levels for Software Artifacts (SLSA) (https://slsa.dev) framework, which has been defined by Google. SLSA requires security checks for source code, build process, and code provenance. Many of these requirements can be included in an automated CI/CD pipeline. To understand how Google applies these practices internally, see Google Cloud's approach to change 

(/docs/cloud-approach-to-change). 

#### Ensure that application deployments follow approved processes

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Application security. 

If an attacker compromises your CI/CD pipeline, your entire application stack can be affected. To help secure the pipeline, you should enforce an established approval process before you deploy the code into production. 

If you use Google Kubernetes Engine (GKE) or Cloud Run, you can establish an approval process by using Binary Authorization (/binary-authorization/docs/overview). Binary Authorization attaches configurable signatures to container images. These 

signatures (also called _attestations_ ) help to validate the image. At deployment time, Binary Authorization uses these attestations to determine whether a process was completed. For example, you can use Binary Authorization to do the following: 

- Verify that a specific build system or CI pipeline created a container image. 

- Validate that a container image is compliant with a vulnerability signing policy. 

- Verify that a container image passes the criteria for promotion to the next deployment environment, such as from development to QA. 

By using Binary Authorization, you can enforce that only trusted code runs on your target platforms. 

#### Scan for known vulnerabilities before application deployment

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Application security. 

We recommend that you use automated tools that can continuously perform vulnerability scans on application artifacts before they're deployed to production. 

For containerized applications, use Artifact Analysis (/artifact-analysis/docs) to automatically run vulnerability scans for container images. Artifact Analysis scans new images when they're uploaded to Artifact Registry (/artifact-registry). The scan extracts information about the system packages in the container. After the initial scan, Artifact Analysis continuously monitors the metadata of scanned images in Artifact Registry for new vulnerabilities. When Artifact Analysis receives new and updated vulnerability information from vulnerability sources 

(/artifact-analysis/docs/vulnerability-scanning#sources), it does the following: 

- Updates the metadata of the scanned images to keep them up to date. 

- Creates new vulnerability occurrences for new notes. 

- Deletes vulnerability occurrences that are no longer valid. 

#### Monitor your application code for known vulnerabilities

This recommendation is relevant to the following focus area (/architecture/framework/security#focus_areas_of_cloud_security): Application security. 

Use automated tools to constantly monitor your application code for known vulnerabilities such as the OWASP Top 10 (https://owasp.org/www-project-top-ten/). For more information about Google Cloud products and features that support OWASP Top 10 mitigation techniques, see Mitigate OWASP Top 10:2025 on Google Cloud (/docs/security/owasp-top-ten-mitigation). 

Use Web Security Scanner 

(/security-command-center/docs/concepts-web-security-scanner-overview) to help identify security vulnerabilities in your App Engine, Compute Engine, and GKE web applications. The scanner crawls your application, follows all of the links within the scope of your starting URLs, and attempts to exercise as many user inputs and event handlers as possible. It can automatically scan for and detect common vulnerabilities, including cross-site scripting 

(https://en.wikipedia.org/wiki/Cross-site_scripting), code injection 

(https://en.wikipedia.org/wiki/Code_injection), mixed content 

(https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content), and outdated or insecure libraries. Web Security Scanner provides early identification of these types of vulnerabilities without distracting you with false positives. 

In addition, if you use GKE to manage fleets of Kubernetes clusters, the security posture dashboard shows opinionated, actionable recommendations to help improve your fleet's security posture. 

## Implement preemptive cyber defense

This principle in the security pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to build robust cyber-defense programs as part of your overall security strategy. 

This principle emphasizes the use of threat intelligence to proactively guide your efforts across the core cyber-defense functions, as defined in The Defender's Advantage: A guide to activating cyber defense 

(https://cloud.google.com/security/resources/defenders-advantage). 

### Principle overview

When you defend your system against cyber attacks, you have a significant, underutilized advantage against attackers. As the founder of Mandiant states (https://cloud.google.com/security/mandiant), "You should know more about your business, your systems, your topology, your infrastructure than any attacker does. This is an incredible advantage." To help you use this inherent advantage, this document provides recommendations about proactive and strategic cyber-defense practices that are mapped to the Defender's Advantage framework.
