# Architecture: Well-Architected Framework and reference designs / Google Cloud Well-Architected Framework (printable, all pillars): Implement preemptive cyber defense: Recommendations to Shared responsibilities and shared fate on Google Cloud: Putting shared responsibility and shared fate into practice
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 78-117, extracted 2026-10-18

## Google Cloud Well-Architected Framework (printable, all pillars)

URL: https://docs.cloud.google.com/architecture/framework/printable

### Recommendations

To implement preemptive cyber defense for your cloud workloads, consider the recommendations in the following sections: 

- Integrate the functions of cyber defense 

- (#integrate_the_functions_of_cyber_defense) 

- Use the Intelligence function in all aspects of cyber defense (#use_intelligence_in_all_aspects_of_cyber_defense) 

- Understand and capitalize on your defender's advantage (#understand_and_capitalize_on_your_defenders_advantage) 

- Validate and improve your defenses continuously 

- (#validate_and_improve_your_defenses_continuously) 

- Manage and coordinate cyber-defense efortsf 

- (#manage_and_coordinate_cyber-defense_efforts) 

#### Integrate the functions of cyber defense

This recommendation is relevant to all of the focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security). 

The Defender's Advantage framework identifies six critical functions of cyber defense: _Intelligence_ , _Detect_ , _Respond_ , _Validate_ , _Hunt_ , and _Mission Control._ Each function focuses on a unique part of the cyber-defense mission, but these functions 

must be well-coordinated and work together to provide an effective defense. Focus on building a robust and integrated system where each function supports the others. If you need a phased approach for adoption, consider the following suggested order. Depending on your current cloud maturity, resource topology, and specific threat landscape, you might want to prioritize certain functions. 

1. **Intelligence** : The Intelligence function guides all the other functions. Understanding the threat landscape—including the most likely attackers, their tactics, techniques, and procedures (TTPs), and the potential impact—is critical to prioritizing actions across the entire program. The Intelligence function is responsible for stakeholder identification, definition of intelligence requirements, data collection, analysis and dissemination, automation, and the creation of a cyber threat profile. 

2. **Detect and Respond** : These functions make up the core of active defense, which involves identifying and addressing malicious activity. These functions are necessary to act on the intelligence that's gathered by the intelligence function. The Detect function requires a methodical approach that aligns detections to attacker TTPs and ensures robust logging. The Respond function must focus on initial triage, data collection, and incident remediation. 

3. **Validate** : The Validate function is a continuous process that provides assurance that your security control ecosystem is up-to-date and operating as designed. This function ensures that your organization understands the attack surface, knows where vulnerabilities exist, and measures the effectiveness of controls. Security validation is also an important component of the detection engineering lifecycle and must be used to identify detection gaps and create new detections. 

4. **Hunt** : The Hunt function involves proactively searching for active threats within an environment. This function must be implemented when your organization has a baseline level of maturity in the Detect and Respond functions. The Hunt function expands the detection capabilities and helps to identify gaps and weaknesses in controls. The Hunt function must be based on specific threats. This advanced function benefits from a foundation of robust intelligence, detection, and response capabilities. 

5. **Mission Control** : The Mission Control function acts as the central hub that connects all of the other functions. This function is responsible for strategy, communication, and decisive action across your cyber-defense program. It 

ensures that all of the functions are working together and that they're aligned with your organization's business goals. You must focus on establishing a clear understanding of the purpose of the Mission Control function before you use it to connect the other functions. 

#### Use the Intelligence function in all aspects of cyber defense

This recommendation is relevant to all of the focus areas (/architecture/framework/security#focus_areas_of_cloud_security). 

This recommendation highlights the Intelligence function as a core part of a strong cyber-defense program. Threat intelligence provides knowledge about threat actors, their TTPs, and indicators of compromise (IOCs). This knowledge should inform and prioritize actions across all cyber-defense functions. An intelligencedriven approach helps you align defenses to meet the threats that are most likely to affect your organization. This approach also helps with efficient allocation and prioritization of resources. 

The following Google Cloud products and features help you take advantage of threat intelligence to guide your security operations. Use these features to identify and prioritize potential threats, vulnerabilities, and risks, and then plan and implement appropriate actions. 

Google Security Operations (Google SecOps) 

(https://cloud.google.com/security/products/security-operations) helps you store and analyze security data centrally. Use Google SecOps to map logs into a common model, enrich the logs, and link the logs to timelines for a comprehensive view of attacks. You can also create detection rules, set up IoC matching, and perform threat-hunting activities. The platform also provides curated detections, which are predefined and managed rules to help identify threats. Google SecOps can also integrate with Mandiant frontline intelligence (https://cloud.google.com/security/products/threat-intelligence). Google SecOps uniquely integrates industry-leading AI, along with threat intelligence from Mandiant (/chronicle/docs/detection) and Google VirusTotal (/chronicle/docs/soar/marketplace-integrations/virustotal). This integration is critical for threat evaluation and understanding who is targeting your organization and the potential impact. 

Security Command Center 

- (/security-command-center/docs/security-command-center-overview) , which is powered by Google AI, enables security professionals to efficiently assess, investigate, and respond to security issues across multiple cloud environments. The security professionals who can benefit from Security Command Center include security operations center (SOC) analysts, vulnerability and posture analysts, and compliance managers. Security Command Center enriches security data, assesses risk, and prioritizes vulnerabilities. This solution provides teams with the information that they need to address high-risk vulnerabilities and to remediate active threats. 

- Chrome Enterprise Premium (/chrome-enterprise-premium/docs/overview) offers threat and data protection, which helps to protect users from exfiltration risks and prevents malware from getting onto enterprise-managed devices. Chrome Enterprise Premium also provides visibility into unsafe or potentially unsafe activity that can happen within the browser. 

- Network monitoring, through tools like Network Intelligence Center (/network-intelligence-center), provides visibility into network performance. Network monitoring can also help you detect unusual traffic patterns or detect data transfer amounts that might indicate an attack or data exfiltration attempt. 

#### Understand and capitalize on your defender's advantage

This recommendation is relevant to all of the focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security). 

As mentioned earlier, you have an advantage over attackers when you have a thorough understanding of your business, systems, topology, and infrastructure. To capitalize on this knowledge advantage, utilize this data about your environments during cyberdefense planning. 

Google Cloud provides the following features to help you proactively gain visibility to identify threats, understand risks, and respond in a timely manner to mitigate potential damage: 

- Chrome Enterprise Premium helps you enhance security for enterprise devices by protecting users from exfiltration risks. It extends Sensitive Data Protection 

services (https://cloud.google.com/security/products/sensitive-data-protection) into the browser, and prevents malware. It also offers features like protection against malware and phishing to help prevent exposure to unsafe content. In addition, it gives you control over the installation of extensions to help prevent unsafe or unvetted extensions. These capabilities help you establish a secure foundation for your operations. 

- Security Command Center provides a continuous risk engine (/security-command-center/docs/attack-exposure-learn) that offers comprehensive and ongoing risk analysis and management. The risk engine feature enriches security data, assesses risk, and prioritizes vulnerabilities to help fix issues quickly. Security Command Center enables your organization to proactively identify weaknesses and implement mitigations. 

- Google SecOps centralizes security data and provides enriched logs with timelines. This enables defenders to proactively identify active compromises and adapt defenses based on attackers' behavior. 

- Network monitoring helps identify irregular network activity that might indicate an attack and it provides early indicators that you can use to take action. To help proactively protect your data from theft, continuously monitor for data exfiltration and use the provided tools. 

#### Validate and improve your defenses continuously

This recommendation is relevant to all of the focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security). 

This recommendation emphasizes the importance of targeted testing and continuous validation of controls to understand strengths and weaknesses across the entire attack surface. This includes validating the effectiveness of controls, operations, and staff through methods like the following: 

Penetration tests 

(https://cloud.google.com/security/resources/datasheets/penetrationtesting#penetration-testing) 

Red-blue team 

(https://services.google.com/fh/files/blogs/google_ai_red_team_digital_final.pdf) and purple team 

(https://cloud.google.com/security/resources/datasheets/consulting-services-continuouspurple-team-assessment) 

exercises 

Tabletop exercises 

(https://cloud.google.com/security/resources/datasheets/consulting-services-tabletopexercise) 

You must also actively search for threats and use the results to improve detection and visibility. Use the following tools to continuously test and validate your defenses against real-world threats: 

- Security Command Center provides a continuous risk engine to evaluate vulnerabilities and prioritize remediation, which enables ongoing evaluation of your overall security posture. By prioritizing issues, Security Command Center helps you to ensure that resources are used effectively. 

- Google SecOps offers threat-hunting and curated detections that let you proactively identify weaknesses in your controls. This capability enables continuous testing and improvement of your ability to detect threats. 

- Chrome Enterprise Premium provides threat and data protection features that can help you to address new and evolving threats, and continuously update your defenses against exfiltration risks and malware. 

- Cloud Next Generation Firewall (Cloud NGFW) provides network monitoring and data-exfiltration monitoring. These capabilities can help you to validate the effectiveness of your current security posture and identify potential weaknesses. Data-exfiltration monitoring helps you to validate the strength of your organization's data protection mechanisms and make proactive adjustments where necessary. When you integrate threat findings from Cloud NGFW with Security Command Center and Google SecOps, you can optimize network-based threat detection, optimize threat response, and automate playbooks. 

#### Manage and coordinate cyber-defense efforts

This recommendation is relevant to all of the focus areas (/architecture/framework/security#focus_areas_of_cloud_security). 

As described earlier in Integrate the functions of cyber defense 

(#integrate_the_functions_of_cyber_defense), the Mission Control function interconnects the other functions of the cyber-defense program. This function enables coordination and unified management across the program. It also helps you coordinate with other teams that don't work on cybersecurity. The Mission Control function promotes empowerment and accountability, facilitates agility and expertise, and drives responsibility and transparency. 

The following products and features can help you implement the Mission Control function: 

- Security Command Center acts as a central hub for coordinating and managing your cyber-defense operations. It brings tools, teams, and data together, along with the built-in Google SecOps response capabilities. Security Command Center provides clear visibility into your organization's security state and enables the identification of security misconfigurations across different resources. 

- Google SecOps provides a platform for teams to respond to threats by mapping logs and creating timelines. You can also define detection rules and search for threats. 

- Google Workspace (https://workspace.google.com/security/) and Chrome Enterprise Premium help you to manage and control end-user access to sensitive resources. You can define granular access controls based on user identity and the context of a request. 

- Network monitoring provides insights into the performance of network resources. You can import network monitoring insights into Security Command Center and Google SecOps for centralized monitoring and correlation against other timeline based data points. This integration helps you to detect and respond to potential network usage changes caused by nefarious activity. 

- Data-exfiltration monitoring helps to identify possible data loss incidents. With this feature, you can efficiently mobilize an incident response team, assess damages, and limit further data exfiltration. You can also improve current policies and controls to ensure data protection. 

#### Product summary

The following table lists the products and features that are described in this document and maps them to the associated recommendations and security capabilities. 

Google Cloud Applicable recommendations product Google SecOps Use the Intelligence function in all aspects of cyber defense: Enables threat hunting and IoC matching, and integrates with Mandiant for comprehensive threat evaluation. Understand and capitalize on your defender's advantage: Provides curated detections and centralizes security data for proactive compromise identification. Validate and improve your defenses continuously: Enables continuous testing and improvement of threat detection capabilities. Manage and coordinate cyber-defense efforts through Mission Control: Provides a platform for threat response, log analysis, and timeline creation. Security Use the Intelligence function in all aspects of cyber defense: Uses AI to Command Centerassess risk, prioritize vulnerabilities, and provide actionable insights for remediation. Understand and capitalize on your defender's advantage: Offers comprehensive risk analysis, vulnerability prioritization, and proactive identification of weaknesses. Validate and improve your defenses continuously: Provides ongoing security posture evaluation and resource prioritization. Manage and coordinate cyber-defense efforts through Mission Control: Acts as a central hub for managing and coordinating cyber-defense operations. 

|Google Cloud<br>product|Applicable recommendations|
|---|---|
|Chrome<br>Enterprise<br>Premium|Use the Intelligence function in all aspects of cyber defense: Protects users<br>from exfiltration risks, prevents malware, and provides visibility into unsafe<br>browser activity.<br>Understand and capitalize on your defender's advantage: Enhances security<br>for enterprise devices through data protection, malware prevention, and<br>control over extensions.<br>Validate and improve your defenses continuously: Addresses new and<br>evolving threats through continuous updates to defenses against exfiltration<br>risks and malware.<br>Manage and coordinate cyber-defense efforts through Mission Control:<br>Manage and control end-user access to sensitive resources, including<br>granular access controls.|
|Google<br>Workspace|Manage and coordinate cyber-defense efforts through Mission Control:<br>Manage and control end-user access to sensitive resources, including<br>granular access controls.|
|Network<br>Intelligence<br>Center|Use the Intelligence function in all aspects of cyber defense: Provides<br>visibility into network performance and detects unusual traffic patterns or<br>data transfers.|
|Cloud NGFW|Validate and improve your defenses continuously: Optimizes network-based<br>threat detection and response through integration with Security Command<br>Center and Google SecOps.|

## Use AI securely and responsibly

This principle in the security pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to help you secure your AI systems. These recommendations are aligned with Google's Secure AI Framework (SAIF) (https://safety.google/cybersecurity-advancements/saif/), which provides a practical approach to address the security and risk concerns of AI systems. SAIF is a conceptual framework that aims to provide industry-wide standards for building and deploying AI responsibly. 

### Principle overview

To help ensure that your AI systems meet your security, privacy, and compliance requirements, you must adopt a holistic strategy that starts with the initial design and extends to deployment and operations. You can implement this holistic strategy by applying the six core elements of SAIF 

(https://developers.google.com/machine-learning/resources/saif). 

Google uses AI to enhance security measures, such as identifying threats, automating security tasks, and improving detection capabilities, while keeping humans in the loop for critical decisions. 

Google emphasizes a collaborative approach to advancing AI security. This approach involves partnering with customers, industries, and governments to enhance the SAIF guidelines and offer practical, actionable resources. 

The recommendations to implement this principle are grouped within the following sections: 

- Recommendations to use AI securely (#recommendations_to_use_ai_securely) 

- Recommendations for AI governance (#recommendations_for_ai_governance) 

### Recommendations to use AI securely

To use AI securely, you need both foundational security controls and AI-specific security controls. This section provides an overview of recommendations to ensure that your AI and ML deployments meet the security, privacy, and compliance requirements of your organization. For an overview of architectural principles and recommendations that are specific to AI and ML workloads in Google Cloud, see the AI and ML perspective (/architecture/framework/perspectives/ai-ml) in the WellArchitected Framework. 

#### Define clear goals and requirements for AI usage

This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

Cloud governance, risk, and compliance 

AI and ML security 

This recommendation aligns with the SAIF element about contextualizing AI system risks in the surrounding business processes. When you design and evolve AI systems, it's important to understand your specific business goals, risks, and compliance requirements. 

#### Keep data secure and prevent loss or mishandling

This recommendation is relevant to the following focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security): 

- Infrastructure security 

- Identity and access management 

- Data security 

- Application security 

- AI and ML security 

This recommendation aligns with the following SAIF elements: 

- Expand strong security foundations to the AI ecosystem. This element includes data collection, storage, access control, and protection against data poisoning. 

- Contextualize AI system risks. Emphasize data security to support business objectives and compliance. 

#### Keep AI pipelines secure and robust against tampering

This recommendation is relevant to the following focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security): 

- Infrastructure security 

- Identity and access management 

- Data security 

- Application security 

AI and ML security 

This recommendation aligns with the following SAIF elements: 

- Expand strong security foundations to the AI ecosystem. As a key element of establishing a secure AI system, secure your code and model artifacts. 

- Adapt controls for faster feedback loops. Because it's important for mitigation and incident response, track your assets and pipeline runs. 

#### Deploy apps on secure systems using secure tools and artifacts

This recommendation is relevant to the following focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security): 

- Infrastructure security 

- Identity and access management 

- Data security 

- Application security 

- AI and ML security 

Using secure systems and validated tools and artifacts in AI-based applications aligns with the SAIF element about expanding strong security foundations to the AI ecosystem and supply chain. This recommendation can be addressed through the following steps: 

- Implement a secure environment for ML training and deployment 

- Use validated container images 

- Apply Supply-chain Levels for Software Artifacts (SLSA) (https://slsa.dev) guidelines 

#### Protect and monitor inputs

This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

- Logging, auditing, and monitoring 

- Security operations 

- AI and ML security 

This recommendation aligns with the SAIF element about extending detection and response to bring AI into an organization's threat universe. To prevent issues, it's critical to manage prompts for generative AI systems, monitor inputs, and control user access. 

### Recommendations for AI governance

All of the recommendations in this section are relevant to the following focus area (/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

Google Cloud offers a robust set of tools and services that you can use to build responsible and ethical AI systems. We also offer a framework of policies, procedures, and ethical considerations that can guide the development, deployment, and use of AI systems. 

As reflected in our recommendations, Google's approach for AI governance is guided by the following principles: 

- Fairness 

- Transparency 

- Accountability 

- Privacy 

- Security 

#### Use fairness indicators

Gemini Enterprise Agent Platform (/gemini-enterprise-agent-platform/machine-learning) can detect bias during the data collection or post-training evaluation process. Agent Platform provides model evaluation metrics 

(/gemini-enterprise-agent-platform/machine-learning/evaluation/intro-evaluation-fairness) like _data bias_ and _model bias_ to help you evaluate your model for bias. 

These metrics are related to fairness across different categories like race, gender, and class. However, interpreting statistical deviations isn't a straightforward exercise, because differences across categories might not be a result of bias or a signal of harm. 

#### Use Vertex Explainable AI

To understand how the AI models make decisions, use Vertex Explainable AI. This feature helps you to identify potential biases that might be hidden in the model's logic. 

This explainability feature is integrated with BigQuery ML (/bigquery/docs/xai-overview) and Vertex Explainable AI (/vertex-ai/docs/explainable-ai/overview), which provide feature-based explanations. You can either perform explainability in BigQuery ML or register your model 

(/bigquery/docs/managing-models-vertex#register_models) in Agent Platform and perform explainability in Agent Platform. 

#### Track data lineage

Track the origin and transformation of data that's used in your AI systems. This tracking helps you understand the data's journey and identify potential sources of bias or error. 

Data lineage (/data-catalog/docs/concepts/about-data-lineage) is a Knowledge Catalog feature that lets you track how data moves through your systems: where it comes from, where it's passed to, and what transformations are applied to it. 

#### Establish accountability

Establish clear responsibility for the development, deployment, and outcomes of your AI systems. 

Use Cloud Logging (/logging/docs/overview) to log key events and decisions made by your AI systems. The logs provide an audit trail to help you understand how the 

system is performing and identify areas for improvement. 

Use Error Reporting (/error-reporting/docs/grouping-errors) to systematically analyze errors made by the AI systems. This analysis can reveal patterns that point to underlying biases or areas where the model needs further refinement. 

#### Implement differential privacy

During model training, add noise (/bigquery/docs/differential-privacy#add_noise) to the data in order to make it difficult to identify individual data points but still enable the model to learn effectively. With SQL in BigQuery (/bigquery/docs/introduction-sql), you can transform the results of a query with differentially private aggregations (/bigquery/docs/differential-privacy). 

## Use AI for security

This principle in the security pillar of the Google Cloud Well-Architected Framework (/architecture/framework) provides recommendations to use AI to help you improve the security of your cloud workloads. 

Because of the increasing number and sophistication of cyber attacks, it's important to take advantage of AI's potential to help improve security. AI can help to reduce the number of threats, reduce the manual effort required by security professionals, and help compensate for the scarcity of experts in the cyber-security domain. 

### Principle overview

Use AI capabilities to improve your existing security systems and processes. You can use Gemini in Security (https://cloud.google.com/security/ai) as well as the intrinsic AI capabilities that are built into Google Cloud services. 

These AI capabilities can transform security by providing assistance across every stage of the security lifecycle. For example, you can use AI to do the following: 

Analyze and explain potentially malicious code without reverse engineering. 

- Reduce repetitive work for cyber-security practitioners. 

- Use natural language to generate queries and interact with security event data. 

- Surface contextual information. 

- Offer recommendations for quick responses. 

- Aid in the remediation of events. 

- Summarize high-priority alerts for misconfigurations and vulnerabilities, highlight potential impacts, and recommend mitigations. 

### Levels of security autonomy

AI and automation can help you achieve better security outcomes when you're dealing with ever-evolving cyber-security threats. By using AI for security, you can achieve greater levels of autonomy to detect and prevent threats and improve your overall security posture. Google defines four levels of autonomy 

(https://services.google.com/fh/files/misc/google-cloud-product-vision-ai-poweredsecurity.pdf#page=6) 

when you use AI for security, and they outline the increasing role of AI in assisting and eventually leading security tasks: 

1. **Manual** : Humans run all of the security tasks (prevent, detect, prioritize, and respond) across the entire security lifecycle. 

2. **Assisted** : AI tools, like Gemini, boost human productivity by summarizing information, generating insights, and making recommendations. 

3. **Semi-autonomous** : AI takes primary responsibility for many security tasks and delegates to humans only when required. 

4. **Autonomous** : AI acts as a trusted assistant that drives the security lifecycle based on your organization's goals and preferences, with minimal human intervention. 

### Recommendations

The following sections describe the recommendations for using AI for security. The sections also indicate how the recommendations align with Google's Secure AI Framework (SAIF) core elements 

(https://developers.google.com/machine-learning/resources/saif) and how they're relevant to the levels of security autonomy (#levels_of_security_autonomy). 

- Enhance threat detection and response with AI 

- (#enhance_threat_detection_and_response_with_ai) 

- Simplify security for experts and non-experts (#simplify_security_for_experts_and_non-experts) 

- Automate time-consuming security tasks with AI 

- (#automate_time-consuming_security_tasks_with_ai) 

- Incorporate AI into risk management and governance processes (#incorporate_ai_into_risk_management_and_governance_processes) 

Implement secure development practices for AI systems (#implement_secure_development_practices_for_ai_systems) 

**Note:** For more information about Google Cloud's overall vision for using Gemini across our products to accelerate AI for security, see the whitepaper Google Cloud's Product Vision for AI-Powered Security (https://services.google.com/fh/files/misc/google-cloud-product-vision-ai-poweredsecurity.pdf) 

#### Enhance threat detection and response with AI

This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

Security operations (SecOps) 

Logging, auditing, and monitoring 

AI can analyze large volumes of security data, offer insights into threat actor behavior, and automate the analysis of potentially malicious code. This recommendation is aligned with the following SAIF elements: 

- Extend detection and response to bring AI into your organization's threat universe. 

Automate defenses to keep pace with existing and new threats. 

Depending on your implementation, this recommendation can be relevant to the following levels of autonomy: 

**Assisted** : AI helps with threat analysis and detection. 

- **Semi-autonomous** : AI takes on more responsibility for the security task. 

Google Threat Intelligence (https://cloud.google.com/security/products/threat-intelligence), which uses AI to analyze threat actor behavior and malicious code, can help you implement this recommendation. 

#### Simplify security for experts and non-experts

This recommendation is relevant to the following focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security): 

- Security operations (SecOps) 

- Cloud governance, risk, and compliance 

AI-powered tools can summarize alerts and recommend mitigations, and these capabilities can make security more accessible to a wider range of personnel. This recommendation is aligned with the following SAIF elements: 

- Automate defenses to keep pace with existing and new threats. 

- Harmonize platform-level controls to ensure consistent security across the organization. 

Depending on your implementation, this recommendation can be relevant to the following levels of autonomy: 

- **Assisted** : AI helps you to improve the accessibility of security information. 

- **Semi-autonomous** : AI helps to make security practices more effective for all users. 

Gemini in Security Command Center 

(https://cloud.google.com/security/products/security-command-center) can provide summaries of alerts for misconfigurations and vulnerabilities. 

#### Automate time-consuming security tasks with AI

This recommendation is relevant to the following focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security): 

- Infrastructure security 

- Security operations (SecOps) 

- Application security 

AI can automate tasks such as analyzing malware, generating security rules, and identifying misconfigurations. These capabilities can help to reduce the workload on security teams and accelerate response times. This recommendation is aligned with the SAIF element about automating defenses to keep pace with existing and new threats. 

Depending on your implementation, this recommendation can be relevant to the following levels of autonomy: 

**Assisted** : AI helps you to automate tasks. 

- **Semi-autonomous** : AI takes primary responsibility for security tasks, and only requests human assistance when needed. 

Gemini in Google SecOps (https://cloud.google.com/security/products/security-operations) can help to automate high-toil tasks by assisting analysts, retrieving relevant context, and making recommendations for next steps. 

#### Incorporate AI into risk management and governance processes

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

You can use AI to build a model inventory and risk profiles. You can also use AI to implement policies for data privacy, cyber risk, and third-party risk. This 

recommendation is aligned with the SAIF element about contextualizing AI system risks in surrounding business processes. 

Depending on your implementation, this recommendation can be relevant to the semi-autonomous level of autonomy. At this level, AI can orchestrate security agents that run processes to achieve your custom security goals. 

#### Implement secure development practices for AI systems

This recommendation is relevant to the following focus areas 

(/architecture/framework/security#focus_areas_of_cloud_security): 

Application security 

AI and ML security 

You can use AI for secure coding, cleaning training data, and validating tools and artifacts. This recommendation is aligned with the SAIF element about expanding strong security foundations to the AI ecosystem. 

This recommendation can be relevant to all levels of security autonomy, because a secure AI system needs to be in place before AI can be used effectively for security. The recommendation is most relevant to the assisted level, where security practices are augmented by AI. 

To implement this recommendation, follow the Supply-chain Levels for Software Artifacts (SLSA) (https://slsa.dev) guidelines for AI artifacts and use validated container images. 

## Meet regulatory, compliance, and privacy needs

This principle in the security pillar of the Google Cloud Well-Architected Framework (/architecture/framework) helps you identify and meet regulatory, compliance, and privacy requirements for cloud deployments. These requirements influence many of the decisions that you need to make about the security controls that must be used for your workloads in Google Cloud. 

### Principle overview

Meeting regulatory, compliance, and privacy needs is an unavoidable challenge for all businesses. Cloud regulatory requirements depend on several factors, including the following: 

- The laws and regulations that apply to your organization's physical locations The laws and regulations that apply to your customers' physical locations 

- Your industry's regulatory requirements 

Privacy regulations define how you can obtain, process, store, and manage your users' data. You own your own data, including the data that you receive from your users. Therefore, many privacy controls are your responsibility, including controls for cookies, session management, and obtaining user permission. 

The recommendations to implement this principle are grouped within the following sections: 

- Recommendations to address organizational risks 

- (#recommendations_to_address_organizational_risks) 

- Recommendations to address regulatory and compliance obligations 

- (#recommendations_to_address_regulatory_and_compliance_obligations) 

- Recommendations to manage your data sovereignty 

- (#recommendations_to_manage_your_data_sovereignty) 

- Recommendations to address privacy requirements 

- (#recommendations_to_address_privacy_requirements) 

### Recommendations to address organizational risks

This section provides recommendations to help you identify and address risks to your organization. 

#### Identify risks to your organization

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

Before you create and deploy resources on Google Cloud, complete a risk assessment. This assessment should determine the security features that you need to meet your internal security requirements and external regulatory requirements. 

Your risk assessment provides you with a catalog of organization-specific risks, and informs you about your organization's capability to detect and counteract security threats. You must perform a risk analysis immediately after deployment and whenever there are changes in your business needs, regulatory requirements, or threats to your organization. 

As mentioned in the Implement security by design 

(/architecture/framework/security/implement-security-by-design) principle, your security risks in a cloud environment differ from on-premises risks. This difference is due to the shared responsibility model in the cloud, which varies by service (IaaS, PaaS, or SaaS) and your usage. Use a cloud-specific risk assessment framework like the Cloud Controls Matrix (CCM) 

(https://cloudsecurityalliance.org/research/cloud-controls-matrix/). Use threat modeling, like OWASP application threat modeling (https://owasp.org/www-project-threat-modeling/) , to identify and address vulnerabilities. For expert help with risk assessments, contact your Google account representative or consult Google Cloud's partner directory (https://cloud.google.com/find-a-partner). 

After you catalog your risks, you must determine how to address them—that is, whether you want to accept, avoid, transfer, or mitigate the risks. For mitigation controls that you can implement, see the next section about mitigating your risks. 

#### Mitigate your risks

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

When you adopt new public cloud services, you can mitigate risks by using technical controls, contractual protections, and third-party verifications or attestations. 

_Technical controls_ are features and technologies that you use to protect your environment. These include built-in cloud security controls like firewalls and logging. Technical controls can also include using third-party tools to reinforce or support your security strategy. There are two categories of technical controls: 

- You can implement Google Cloud's security controls to help you mitigate the risks that apply to your environment. For example, you can secure the connection between your on-premises networks and your cloud networks by using Cloud VPN (/network-connectivity/docs/vpn/concepts/overview) and Cloud Interconnect (/network-connectivity/docs/interconnect/concepts/overview). 

- Google has robust internal controls and auditing to protect against insider access to customer data. Our audit logs provide you with near real-time logs of Google administrator access 

(/assured-workloads/access-transparency/docs/overview) on Google Cloud. 

_Contractual protections_ refer to the legal commitments made by us regarding Google Cloud services. Google is committed to maintaining and expanding our compliance portfolio. The Cloud Data Processing Addendum (CDPA) 

(https://cloud.google.com/terms/data-processing-addendum) describes our commitments with regard to the processing and security of your data. The CDPA also outlines the access controls that limit Google support engineers' access to customers' environments, and it describes our rigorous logging and approval process. We recommend that you review Google Cloud's contractual controls with your legal and regulatory experts, and verify that they meet your requirements. If you need more information, contact your technical account representative 

(https://cloud.google.com/contact). 

_Third-party verifications or attestations_ refer to having a third-party vendor audit the cloud provider to ensure that the provider meets compliance requirements. For example, to learn about Google Cloud attestations with regard to the ISO/IEC 27017 guidelines, see ISO/IEC 27017 - Compliance 

(https://cloud.google.com/security/compliance/iso-27017). To view the current Google Cloud certifications and letters of attestation, see Compliance resource center (https://cloud.google.com/security/compliance/). 

### Recommendations to address regulatory and compliance obligations

A typical compliance journey has three stages: assessment, gap remediation, and continual monitoring. This section provides recommendations that you can use during each of these stages. 

#### Assess your compliance needs

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

Compliance assessment starts with a thorough review of all of your regulatory obligations and how your business is implementing them. To help you with your assessment of Google Cloud services, use the Compliance resource center 

(https://cloud.google.com/security/compliance). This site provides information about the following: 

Service support for various regulations 

Google Cloud certifications and attestations 

To better understand the compliance lifecycle at Google and how your requirements can be met, you can contact sales (https://cloud.google.com/support-hub) to request help from a Google compliance specialist. Or, you can contact your Google Cloud account manager to request a compliance workshop. 

For more information about tools and resources that you can use to manage security and compliance for Google Cloud workloads, see Assuring Compliance in the Cloud (https://services.google.com/fh/files/misc/assuringcompliance_in_the_cloud.pdf). 

#### Automate implementation of compliance requirements

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

To help you stay in compliance with changing regulations, determine whether you can automate how you implement compliance requirements. You can use both compliance-focused capabilities that Google Cloud provides and blueprints that use recommended configurations for a particular compliance regime. 

Assured Workloads (/assured-workloads) builds on the controls within Google Cloud to help you meet your compliance obligations. Assured Workloads lets you do the following: 

- Select your compliance regime. Then, the tool automatically sets the baseline personnel access controls for the selected regime. 

- Set the location for your data by using organization policies so that your data at rest and your resources remain only in that region 

- (/docs/geography-and-regions#regions_and_zones). 

- Select the key-management option (such as the key rotation period) that best meets your security and compliance requirements. 

- Select the access criteria for Google support personnel to meet certain regulatory requirements such as FedRAMP Moderate. For example, you can select whether Google support personnel have completed the appropriate background checks. 

- Use Google-owned and Google-managed encryption keys that are FIPS-140-2 compliant and support FedRAMP Moderate compliance. For an added layer of control and for the separation of duties, you can use customer-managed encryption keys (CMEK). For more information about keys, see Encrypt data at rest and in transit 

- (/architecture/framework/security/implement-security-bydesign#encrypt_data_at_rest_and_in_transit) 

In addition to Assured Workloads, you can use Google Cloud blueprints that are relevant to your compliance regime. You can modify these blueprints to incorporate your security policies into your infrastructure deployments. 

To help you build an environment that supports your compliance requirements, Google's blueprints and solution guides include recommended configurations and provide Terraform modules. The following table lists blueprints that address security and alignment with compliance requirements. 

RequirementBlueprints and solution guides 

|FedRAMP|Google Cloud FedRAMP implementation guide<br>(/docs/security/compliance/fedramp-implementation-guide)|
|---|---|
||Setting up a FedRAMP Aligned Three-Tier Workload on Google Cloud<br>(https://services.google.com/fh/files/misc/fedramp_aligned_workload_solution_g|
|HIPAA|Protecting healthcare data on Google Cloud<br>(https://services.google.com/fh/files/misc/protecting_healthcare_data_on_google|
||Setting up a HIPAA-aligned workload using Data Protection Toolkit<br>(https://services.google.com/fh/files/misc/hipaa_technical_solution_guide.pdf)|

#### Monitor your compliance

- This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

Cloud governance, risk, and compliance 

- Logging, monitoring, and auditing 

Most regulations require that you monitor particular activities, which include access-related activities. To help with your monitoring, you can use the following: 

- Access Transparency (/assured-workloads/access-transparency/docs/overview): View near real-time logs when Google Cloud administrators access your content. 

- Firewall Rules Logging (/vpc/docs/firewall-rules-logging): Record TCP and UDP connections inside a VPC network for any rules that you create. These logs can be useful for auditing network access or for providing early warning that the network is being used in an unapproved manner. 

- VPC Flow Logs (/vpc/docs/using-flow-logs): Record network traffic flows that are sent or received by VM instances. 

Security Command Center Premium 

- (/security-command-center/docs/compliance-management): Monitor for compliance with various standards. 

- OSSEC (https://ossec.github.io/index.html) (or another open source tool): Log the activity of individuals who have administrator access to your environment. 

- Key Access Justifications (/assured-workloads/key-access-justifications/docs/overview): View the reasons for a key-access request. 

- Security Command Center notifications 

- (/security-command-center/docs/how-to-notifications): Get alerts when noncompliance issues occur. For example, get alerts when users disable twostep verification or when service accounts are over-privileged. You can also set up automatic remediation for specific notifications. 

### Recommendations to manage your data sovereignty

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

Data sovereignty provides you with a mechanism to prevent Google from accessing your data. You approve access only for provider behaviors that you agree are necessary. For example, you can manage your data sovereignty in the following ways: 

Store and manage encryption keys (/kms/docs/ekm) outside the cloud. 

- Grant access to these keys based on detailed access justifications (/assured-workloads/key-access-justifications/docs/overview). 

Protect data in use 

(/confidential-computing/confidential-vm/docs/confidential-vm-overview) by using Confidential Computing. 

#### Manage your operational sovereignty

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

Operational sovereignty provides you with assurances that Google personnel can't compromise your workloads. For example, you can manage operational sovereignty in the following ways: 

Restrict the deployment 

- (/resource-manager/docs/organization-policy/defining-locations) of new resources to specific provider regions. 

Limit Google personnel access 

(/assured-workloads/docs/personnel-access-data-controls) based on predefined attributes such as their citizenship or geographic location. 

#### Manage software sovereignty

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

Software sovereignty provides you with assurances that you can control the availability of your workloads and run them wherever you want. Also, you can have this control without being dependent or locked in with a single cloud provider. Software sovereignty includes the ability to survive events that require you to quickly change where your workloads are deployed and what level of outside connection is allowed. 

For example, to help you manage your software sovereignty, Google Cloud supports hybrid and multicloud deployments 

(/architecture/hybrid-multicloud-patterns-and-practices). If you choose on-premises deployments for data sovereignty reasons, Google Distributed Cloud 

(/distributed-cloud) is a combination of hardware and software that brings Google Cloud into your data center. 

### Recommendations to address privacy requirements

Google Cloud includes the following controls that promote privacy: 

- Default encryption of all data when it's at rest, when it's in transit, and while it's being processed. 

- Safeguards against insider access. 

- Support for numerous privacy regulations. 

The following recommendations address additional controls that you can implement. For more information, see Privacy Resource Center 

(https://cloud.google.com/privacy). 

#### Control data residency

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Cloud governance, risk, and compliance. 

Data residency describes where your data is stored at rest. Data residency requirements vary based on system design objectives, industry regulatory concerns, national law, tax implications, and even culture. 

Controlling data residency starts with the following: 

- Understand your data type and its location. 

- Determine what risks exist for your data and which laws and regulations apply. 

- Control where your data is stored or where it goes. 

To help you comply with data residency requirements, Google Cloud lets you control where your data is stored, how it's accessed, and how it's processed. You can use resource location policies 

(/resource-manager/docs/organization-policy/defining-locations) to restrict where resources are created and to limit where data is replicated between regions. You can use the location property of a resource to identify where the service is deployed and who maintains it. For more information, see Resource locations supported services 

(/resource-manager/docs/organization-policy/defining-locations-supported-services). 

#### Classify your confidential data

This recommendation is relevant to the following focus area 

(/architecture/framework/security#focus_areas_of_cloud_security): Data security. 

You must define what data is confidential, and then ensure that the confidential data is properly protected. Confidential data can include credit card numbers, addresses, phone numbers, and other personally identifiable information (PII). 

Using Sensitive Data Protection (/sensitive-data-protection), you can set up appropriate classifications. You can then tag and tokenize your data before you store it in Google Cloud. Additionally, Knowledge Catalog offers a catalog (/dataplex/docs/catalog-overview) service that provides a platform for storing, managing, and accessing your metadata. For more information and an example of data classification and de-identification, see De-identification and re-identification of PII using Sensitive Data Protection 

(/architecture/de-identification-re-identification-pii-using-cloud-dlp). 

#### Lock down access to sensitive data

This recommendation is relevant to the following focus areas (/architecture/framework/security#focus_areas_of_cloud_security): 

Data security 

Identity and access management 

Place sensitive data in its own service perimeter by using VPC Service Controls (/vpc-service-controls/docs/overview). VPC Service Controls improves your ability to mitigate the risk of unauthorized copying or transferring of data (data exfiltration) from Google-managed services. With VPC Service Controls, you configure security perimeters around the resources of your Google-managed services to control the movement of data across the perimeter. Set Google Identity and Access Management (IAM) (/iam/docs) access controls for that data. Configure multifactor authentication (MFA) (https://support.google.com/cloudidentity/answer/175197) for all users who require access to sensitive data. 

## Shared responsibilities and shared fate on Google Cloud

This document describes the differences between the shared responsibility model and shared fate in Google Cloud. It discusses the challenges and nuances of the shared responsibility model. This document describes what shared fate is and how we partner with our customers to address cloud security challenges. 

Understanding the shared responsibility model is important when determining how to best protect your data and workloads on Google Cloud. The shared responsibility model describes the tasks that you have when it comes to security in the cloud and how these tasks are different for cloud providers. 

Understanding shared responsibility, however, can be challenging. The model requires an in-depth understanding of each service you utilize, the configuration options that each service provides, and what Google Cloud does to secure the service. Every service has a different configuration profile, and it can be difficult to determine the best security configuration. Google believes that the shared responsibility model stops short of helping cloud customers achieve better security outcomes. Instead of shared responsibility, we believe in _shared fate_ . 

Shared fate includes us building and operating a trusted cloud platform for your workloads. We provide best practice guidance and secured, attested infrastructure code that you can use to deploy your workloads in a secure way. We release solutions that combine various Google Cloud services to solve complex security problems and we offer innovative insurance options to help you measure and mitigate the risks that you must accept. Shared fate involves us more closely interacting with you as you secure your resources on Google Cloud. 

### Shared responsibility

You're the expert in knowing the security and regulatory requirements for your business, and knowing the requirements for protecting your confidential data and resources. When you run your workloads on Google Cloud, you must identify the security controls that you need to configure in Google Cloud to help protect your confidential data and each workload. To decide which security controls to implement, you must consider the following factors: 

- Your regulatory compliance obligations 

- Your organization's security standards and risk management plan 

- Security requirements of your customers and your vendors 

#### Defined by workloads

Traditionally, responsibilities are defined based on the type of workload that you're running and the cloud services that you require. Cloud services include the following categories: 

Cloud service Description Infrastructure as IaaS services include Compute Engine (/compute/docs), Cloud Storage a service (IaaS) (/storage/docs/introduction), and networking services such as Cloud VPN (/network-connectivity/docs/vpn/concepts/overview), Cloud Load Balancing (/load-balancing/docs/load-balancing-overview), and Cloud DNS (/dns/docs/overview). IaaS provides compute, storage, and network services on demand with payas-you-go pricing. You can use IaaS if you plan on migrating an existing onpremises workload to the cloud using lift-and-shift, or if you want to run your application on particular VMs, using specific databases or network configurations. In IaaS, the bulk of the security responsibilities are yours, and our responsibilities are focused on the underlying infrastructure and physical security. Platform as a PaaS services include App Engine (/appengine), Google Kubernetes Engine service (PaaS) (GKE) (/kubernetes-engine/docs), and BigQuery (/bigquery/docs/introduction). PaaS provides the runtime environment that you can develop and run your applications in. You can use PaaS if you're building an application (such as a website), and want to focus on development not on the underlying infrastructure. 

In PaaS, we're responsible for more controls than in IaaS. Typically, this will vary by the services and features that you use. You share responsibility with us for application-level controls and IAM management. You remain responsible for your data security and client protection. 

|Cloud service|Description|
|---|---|
|Software as a<br>service (SaaS)|SaaS applications include<br>Google Workspace(https://workspace.google.com/),<br>Google Security Operations(/chronicle/docs/overview), and third-party SaaS<br>applications that are available in<br>Google Cloud Marketplace(/marketplace).|
||SaaS provides online applications that you can subscribe to or pay for in some<br>way. You can use SaaS applications when your enterprise doesn't have the<br>internal expertise or business requirement to build the application<br>themselves, but does require the ability to process workloads.<br>In SaaS, we own the bulk of the security responsibilities. You remain<br>responsible for your access controls and the data that you choose to store in<br>the application.|
|Function as a<br>service (FaaS) o<br>serverless|r<br>FaaS provides the platform for developers to run small, single-purpose code<br>(called_functions_) that run in response to particular events. You would use<br>FaaS when you want particular things to occur based on a particular event. For<br>example, you might create a function that runs whenever data is uploaded to<br>Cloud Storage so that it can be classified.<br>FaaS has a similar shared responsibility list as SaaS.<br>Cloud Run functions<br>(/functions/docs/2nd-gen/overview) is a FaaS application.|

The following diagram shows the cloud services and defines how responsibilities are shared between the cloud provider and customer. 

As the diagram shows, the cloud provider always remains responsible for the underlying network and infrastructure, and customers always remain responsible for their access policies and data. 

#### Defined by industry and regulatory framework

Various industries have regulatory frameworks that define the security controls that must be in place. When you move your workloads to the cloud, you must understand the following: 

- Which security controls are your responsibility 

- Which security controls are available as part of the cloud offering 

- Which default security controls are inherited 

Inherited security controls (such as our default encryption (/docs/security/encryption/default-encryption) and infrastructure controls (/docs/security/infrastructure/design)) are controls that you can provide as part of your evidence of your security posture to auditors and regulators. For example, the Payment Card Industry Data Security Standard (PCI DSS) defines regulations for payment processors. When you move your business to the cloud, these regulations are shared between you and your CSP. To understand how PCI DSS responsibilities are shared between you and Google Cloud, see Google Cloud: PCI DSS Shared Responsibility Matrix 

(https://services.google.com/fh/files/misc/gcp_pci_dss_v4_responsibility_matrix.pdf). 

As another example, in the United States, the Health Insurance Portability and Accountability Act (HIPAA) has set standards for handling electronic personal health information (PHI). These responsibilities are also shared between the CSP and you. For more information on how Google Cloud meets our responsibilities under HIPAA, see HIPAA - Compliance (https://cloud.google.com/security/compliance/hipaa-compliance). 

Other industries (for example, finance or manufacturing) also have regulations that define how data can be gathered, processed, and stored. For more information about shared responsibility related to these, and how Google Cloud meets our responsibilities, see Compliance resource center 

(https://cloud.google.com/security/compliance). 

#### Defined by location

Depending on your business scenario, you might need to consider your responsibilities based on the location of your business offices, your customers, and your data. Different countries and regions have created regulations that inform how you can process and store your customer's data. For example, if your business has customers who reside in the European Union, your business might need to abide by the requirements that are described in the General Data Protection Regulation (https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32016R0679) (GDPR), and you might be obligated to keep your customer data in the EU itself. In this circumstance, you are responsible for ensuring that the data that you collect remains in the Google Cloud regions in the EU 

(https://cloud.google.com/about/locations#europe). For more information about how we meet our GDPR obligations, see GDPR and Google Cloud (https://cloud.google.com/privacy/gdpr). 

For information about the requirements related to your region, see Compliance offerings (https://cloud.google.com/security/compliance/offerings). If your scenario is particularly complicated, we recommend speaking with our sales team (https://cloud.google.com/contact) or one of our partners (https://cloud.google.com/find-a-partner) to help you evaluate your security responsibilities. 

#### Challenges for shared responsibility

Though shared responsibility helps define the security roles that you or the cloud provider has, relying on shared responsibility can still create challenges. Consider the following scenarios: 

- Many cloud security breaches are the direct result of misconfiguration. Cloud products are constantly changing, and new ones are constantly being launched. Keeping up with constant change can seem overwhelming. Customers need cloud providers to provide them with opinionated best practices to help keep up with the change, starting with best practices by default and having a baseline secure configuration. 

- Though dividing items by cloud services is helpful, many enterprises have workloads that require multiple cloud services types. In this circumstance, you must consider how various security controls for these services interact, including whether they overlap between and across services. For example, you might have an on-premises application that you're migrating to Compute Engine, use Google Workspace for corporate email, and also run BigQuery to analyze data to improve your products. 

- Your business and markets are constantly changing; as regulations change, as you enter new markets, or as you acquire other companies. Your new markets might have different requirements, and your new acquisition might host their workloads on another cloud. To manage the constant changes, you must constantly re-assess your risk profile and be able to implement new controls quickly. 

- How and where to manage your data encryption keys is an important decision that ties with your responsibilities to protect your data. The option that you choose depends on your regulatory requirements, whether you're running a 

hybrid cloud environment or still have an on-premises environment, and the sensitivity of the data that you're processing and storing. 

- Incident management is an important, and often overlooked, area where your responsibilities and the cloud provider responsibilities aren't easily defined. Many incidents require close collaboration and support from the cloud provider to help investigate and mitigate them. Other incidents can result from poorly configured cloud resources or stolen credentials, and ensuring that you meet the best practices for securing your resources and accounts can be quite challenging. 

- Advanced persistent threats (APTs) and new vulnerabilities can impact your workloads in ways that you might not consider when you start your cloud transformation. Ensuring that you remain up-to-date on the changing landscape, and who is responsible for threat mitigation is difficult, particularly if your business doesn't have a large security team. 

### Shared fate

We developed shared fate in Google Cloud to start addressing the challenges that the shared responsibility model doesn't address. Shared fate focuses on how all parties can better interact to continuously improve security. Shared fate builds on the shared responsibility model because it views the relationship between cloud provider and customer as an ongoing partnership to improve security. 

Shared fate is about us taking responsibility for making Google Cloud more secure. Shared fate includes helping you get started with a secured landing zone 

(/architecture/landing-zones#what-is-a-google-cloud-landing-zone) and being clear, opinionated, and transparent about recommended security controls, settings, and associated best practices. It includes helping you better quantify and manage your risk with cyber-insurance, using our Risk Protection Program 

(#risk-protection-program). Using shared fate, we want to evolve from the standard shared responsibility framework to a better model that helps you secure your business and build trust in Google Cloud. 

The following sections describe various components of shared fate. 

#### Help getting started

A key component of shared fate is the resources that we provide to help you get started, in a secure configuration in Google Cloud. Starting with a secure configuration helps reduce the issue of misconfigurations which is the root cause of most security breaches. 

Our resources include the following: 

- Enterprise foundations blueprint (/architecture/blueprints/security-foundations) that discuss top security concerns and our top recommendations. 

- Secure blueprints 

(https://cloud.google.com/security/best-practices#deployable-security-blueprints-andlanding-zones) 

that let you deploy and maintain secure solutions using _infrastructure as code_ (IaC). Blueprints have our security recommendations enabled by default. Many blueprints are created by Google security teams and managed as products. This support means that they're updated regularly, go through a rigorous testing process, and receive attestations from third-party testing groups. Blueprints include the enterprise foundations blueprint 

(/architecture/blueprints/security-foundations) and the secured data warehouse blueprint (/architecture/blueprints/confidential-data-warehouse-blueprint). 

- Google Cloud Well-Architected Framework (/architecture/framework/security) recommendations for building security into your designs. 

- Landing zone navigation guides (/architecture/landing-zones) that step you through the top decisions that you need to make to build a secure foundation for your workloads, including resource hierarchy, identity onboarding, security and key management, and network structure. 

#### Risk Protection Program

Shared fate also includes the Risk Protection Program 

(https://cloud.google.com/security/products/risk-protection-program), which helps you use the power of Google Cloud as a platform to manage risk, rather than just seeing cloud workloads as another source of risk that you need to manage. The Risk Protection Program is a collaboration between Google Cloud and two leading cyber insurance companies, Munich Re and Allianz Global & Corporate Speciality. 

The Risk Protection Program includes Cyber Insurance Hub 

(/risk-manager/docs/overview), which provides data-driven insights that you can use to better understand your cloud security posture. If you're looking for cyber insurance coverage, you can share these insights from Cyber Insurance Hub directly with our insurance partners to obtain a quote. 

#### Help with deployment and governance

Shared fate also helps with your continued governance of your environment. For example, we focus efforts on products such as the following: 

- Assured Workloads (/assured-workloads/docs/concept-overview), which helps you meet your compliance obligations. 

Security Command Center 

- (/security-command-center/docs/security-command-center-overview) Premium, which uses threat intelligence, threat detection, web scanning, and other advanced methods to monitor and detect threats. It also provides a way to resolve many of these threats quickly and automatically. 

- Organization policies (/resource-manager/docs/organization-policy/overview) and resource settings (/resource-manager/docs/cloud-platform-resource-hierarchy) that let you configure policies throughout your hierarchy of folders and projects. 

- Policy Intelligence tools (/policy-intelligence/docs/overview) that provide you with insights on access to accounts and resources. 

- Confidential Computing (/confidential-computing/confidential-vm/docs/about-cvm), which lets you encrypt data in use. 

- Sovereign Controls by Partners (/sovereign-controls-by-partners/docs/overview), which is available in certain countries and helps enforce data residency requirements. 

### Putting shared responsibility and shared fate into practice

As part of your planning process, consider the following actions to help you understand and implement appropriate security controls: 

   - Create a list of the type of workloads that you will host in Google Cloud, and whether they require IaaS, PaaS, and SaaS services. You can use the shared responsibility diagram (#shared-diagram) as a checklist to ensure that you know the security controls that you need to consider. 

   - Create a list of regulatory requirements that you must comply with, and access resources in the Compliance resource center 

   - (https://cloud.google.com/security/compliance) that relate to those requirements. 

   - Review the list of available blueprints and architectures in the Architecture Center (/architecture) for the security controls that you require for your particular workloads. The blueprints provide a list of recommended controls and the IaC code that you require to deploy that architecture. 

   - Use the landing zone documentation (/architecture/landing-zones) and the recommendations in the enterprise foundations guide 

   - (/architecture/blueprints/security-foundations) to design a resource hierarchy and network architecture that meets your requirements. You can use the opinionated workload blueprints, like the secured data warehouse, to accelerate your development process. 

   - After you deploy your workloads, verify that you're meeting your security responsibilities using services such as the Cyber Insurance Hub, Assured Workloads, Policy Intelligence tools, and Security Command Center Premium. 

- For more information, see the CISO's Guide to Cloud Transformation paper (https://services.google.com/fh/files/misc/ciso-guide-to-security-transformation.pdf).
