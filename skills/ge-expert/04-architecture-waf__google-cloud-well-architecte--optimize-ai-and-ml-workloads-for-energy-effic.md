# Architecture: Well-Architected Framework and reference designs / Google Cloud Well-Architected Framework (printable, all pillars): Optimize AI and ML workloads for energy efficiency: Recommendations to Align sustainability practices with industry guidelines: Green Software Foundation to Google Cloud Well-Architected Framework (printable, all pillars): Align sustainability practices with industry guidelines: Greenhouse Gas Protocol
Source: 04-Architecture-Well-Architected-Framework-and-reference-designs.pdf, pages 193-233, extracted 2026-10-18

Contains:
- Google Cloud Well-Architected Framework (printable, all pillars): Optimize AI and ML workloads for energy efficiency: Recommendations to Align sustainability practices with industry guidelines: Green Software Foundation (pages 193-232) https://docs.cloud.google.com/architecture/framework/printable
- Google Cloud Well-Architected Framework (printable, all pillars): Align sustainability practices with industry guidelines: Greenhouse Gas Protocol (pages 232-233) https://docs.cloud.google.com/architecture/framework/printable

## Google Cloud Well-Architected Framework (printable, all pillars)

URL: https://docs.cloud.google.com/architecture/framework/printable

### Recommendations

To optimize AI and ML workloads for energy efficiency, consider the recommendations in the following sections. 

#### Architect for energy efficiency by using TPUs

AI and ML workloads can be compute-intensive. The energy consumption by AI and ML workloads is a key consideration for sustainability. TPUs (/tpu) let you significantly improve the energy efficiency and sustainability of your AI and ML workloads. 

TPUs are custom-designed accelerators that are purpose-built for AI and ML workloads. The specialized architecture of TPUs make them highly effective for large-scale matrix multiplication, which is the foundation of deep learning. TPUs can perform complex tasks at scale with greater efficiency than general-purpose processors like CPUs or GPUs. 

TPUs provide the following direct benefits for sustainability: 

- **Lower energy consumption** : TPUs are engineered for optimal energy efficiency. They deliver higher computations per watt of energy consumed. Their specialized architecture significantly reduces the power demands of large-scale training and inference tasks, which leads to reduced operational costs _and_ lower energy consumption. 

- **Faster training and inference** : The exceptional performance of TPUs lets you train complex AI models in hours rather than days. This significant reduction in the total compute time contributes directly to a smaller environmental footprint. 

- **Reduced cooling needs** : TPUs incorporate advanced liquid cooling, which provides efficient thermal management and significantly reduces the energy that's used for cooling the data center. 

- **Optimization of the AI lifecycle** : By integrating hardware and software, TPUs provide an optimized solution across the entire AI lifecycle, from data processing to model serving. 

#### Follow the 4Ms best practices for resource selection

Google recommends a set of best practices to reduce energy usage and carbon emissions significantly for AI and ML workloads. We call these best practices _4Ms_ (https://cloud.google.com/transform/betting-on-efficient-ai-the-4-ms): 

- **Model** : Select efficient ML model architectures. For example, sparse models (https://ai.googleblog.com/2021/03/constructing-transformers-for-longer.html) improve ML quality and reduce computation by 3-10 times when compared to dense models. 

- **Machine** : Choose processors and systems that are optimized for ML training. These processors improve performance and energy efficiency by 2-5 times when compared to general-purpose processors. 

- **Mechanization** : Deploy your compute-intensive workloads in the cloud. Your workloads use less energy and cause lower emissions by 1.4 to 2 times when compared to on-premises deployments. Cloud data centers use newer, custom-designed warehouses that are built for energy efficiency and have a high power usage effectiveness (PUE) 

- (https://en.wikipedia.org/wiki/Power_usage_effectiveness) ratio. On-premises data centers are often older and smaller, therefore investments in energy-efficient cooling and power distribution systems might not be economical. 

- **Map** : Select Google Cloud locations that use the cleanest energy. This approach helps to reduce the gross carbon footprint of your workloads by 5-10 times. For more information, see Carbon-free energy for Google Cloud regions (https://cloud.google.com/sustainability/region-carbon). 

For more information about the 4Ms best practices and efficiency metrics, see the following research papers: 

- The carbon footprint of machine learning training will plateau, then shrink (https://www.techrxiv.org/doi/full/10.36227/techrxiv.19139645.v1) 

The data center as a computer: An introduction to the design of warehousescale machines, second edition 

(https://research.google/pubs/the-datacenter-as-a-computer-an-introduction-to-thedesign-of-warehouse-scale-machines-second-edition/) 

#### Optimize AI models and algorithms for training and inference

The architecture of an AI model and the algorithms that are used for training and inference have a significant impact on energy consumption. Consider the following recommendations. 

Select efficient AI models 

Choose smaller, more efficient AI models that meet your performance requirements. Don't select the largest available model as a default choice. For example, a smaller, distilled model version like DistilBERT (https://huggingface.co/papers/1910.01108) can deliver similar performance with significantly less computational overhead and faster inference than a larger model like BERT. 

Use domain-specific, hyper-efficient solutions 

Choose specialized ML solutions that provide better performance and require significantly less compute power than a large foundation model. These specialized solutions are often pre-trained and hyper-optimized. They can provide significant reductions in energy consumption and research effort for both training and inference workloads. The following are examples of domain-specific specialized solutions: 

- Earth AI (https://ai.google/earth-ai/) is an energy-efficient solution that synthesizes large amounts of global geospatial data to provide timely, accurate, and actionable insights. 

- WeatherNext (https://deepmind.google/science/weathernext/) produces faster, more efficient, and highly accurate global weather forecasts when compared to conventional physics-based methods. 

Apply appropriate model compression techniques 

The following are examples of techniques that you can use for model compression: 

- **Pruning** : Remove unnecessary parameters from a neural network. These are parameters that don't contribute significantly to a model's performance. This technique reduces the size of the model and the computational resources that are required for inference. 

- **Quantization** : Reduce the precision of model parameters. For example, reduce the precision from 32-bit floating-point to 8-bit integers. This technique can help to significantly decrease the memory footprint and power consumption without a noticeable reduction in accuracy. 

- **Knowledge distillation** : Train a smaller _student_ model to mimic the behavior of a larger, more complex _teacher_ model. The student model can achieve a high level of performance with fewer parameters and by using less energy. 

Use specialized hardware 

As mentioned in Follow the 4Ms best practices for resource selection (#resource-selection-best-practices), choose processors and systems that are optimized for ML training. These processors improve performance and energy efficiency by 2-5 times when compared to general-purpose processors. 

Use parameter-efficient fine-tuning 

Instead of adjusting all of a model's billions of parameters (full fine-tuning), use parameter-efficient fine-tuning (PEFT) methods like low-rank adaptation (LoRA). With this technique, you freeze the original model's weights and train only a small number of new, lightweight layers. This approach helps to reduce cost and energy consumption. 

#### Follow best practices for AI and ML operations

Operational practices significantly affect the sustainability of your AI and ML workloads. Consider the following recommendations. 

Optimize model training processes 

Use the following techniques to optimize your model training processes: 

- **Early stopping** : Monitor the training process and stop it when you don't observe further improvement in model performance against the validation set. This technique helps you prevent unnecessary computations and energy use. 

- **Efficient data loading** : Use efficient data pipelines to ensure that the GPUs and TPUs are always utilized and don't wait for data. This technique helps to maximize resource utilization and reduce wasted energy. 

- **Optimized hyperparameter tuning** : To find optimal hyperparameters more efficiently, use techniques like Bayesian optimization or reinforcement learning. Avoid exhaustive grid searches, which can be resource-intensive operations. 

Improve inference efficiency 

- To improve the efficiency of AI inference tasks, use the following techniques: 

   - **Batching** : Group multiple inference requests in batches and take advantage of parallel processing on GPUs and TPUs. This technique helps to reduce the energy cost per prediction. 

   - **Advanced caching** : Implement a multi-layered caching strategy, which includes key-value (KV) caching for autoregressive generation and semanticprompt caching for application responses. This technique helps to bypass redundant model computations and can yield significant reductions in energy usage and carbon emissions. 

Measure and monitor 

Monitor and measure the following parameters: 

- **Usage and cost** : Use appropriate tools to track the token usage, energy consumption, and carbon footprint of your AI workloads. This data helps you identify opportunities for optimization and report progress toward sustainability goals. 

- **Performance** : Continuously monitor model performance in production. Identify issues like data drift, which can indicate that the model needs to be fine-tuned again. If you need to re-train the model, you can use the original 

fine-tuned model as a starting point and save significant time, money, and energy on updates. 

- To track performance metrics, use Cloud Monitoring 

- (/monitoring/docs/monitoring-overview). 

- To correlate model changes with improvements in performance metrics, use event annotations (/monitoring/dashboards/show-events). 

For more information about operationalizing continuous improvement, see Continuously measure and improve sustainability 

(/architecture/framework/sustainability/continuously-measure-improve). 

Implement carbon-aware scheduling 

Architect your ML pipeline jobs to run in regions with the cleanest energy mix. Use the Carbon Footprint report to identify the least carbon-intensive regions. Schedule resource-intensive tasks as batch jobs during periods when the local electrical grid has a higher percentage of carbon-free energy (CFE). 

Optimize data pipelines 

ML operations and fine-tuning require a clean, high-quality dataset. Before you start ML jobs, use managed data processing services to prepare the data efficiently. For example, use Dataflow (/dataflow/docs/overview) for streaming and batch processing and use Managed Service for Apache Spark 

(/dataproc/docs/concepts/overview) for managed Spark and Hadoop pipelines. An optimized data pipeline helps to ensure that your fine-tuning workload doesn't wait for data, so you can maximize resource utilization and help reduce wasted energy. 

Embrace MLOps 

To automate and manage the entire ML lifecycle, implement ML Operations (MLOps) practices 

(/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning). These practices help to ensure that models are continuously monitored, validated, and redeployed efficiently, which helps to prevent unnecessary training or resource allocation. 

Use managed services 

Instead of managing your own infrastructure, use managed cloud services like Gemini Enterprise Agent Platform (/gemini-enterprise-agent-platform). The cloud platform handles the underlying resource management, which lets you focus on the fine-tuning process. Use services that include built-in tools for hyperparameter tuning, model monitoring, and resource management. 

### What's next

- How much energy does Google's AI use? We did the math 

- (https://cloud.google.com/blog/products/infrastructure/measuring-the-environmentalimpact-of-ai-inference/) 

Ironwood: The frst Google TPU for the age of inferencei 

(https://blog.google/products/google-cloud/ironwood-tpu-age-of-inference/) 

- Google Sustainability 2025 Environmental Report 

- (https://sustainability.google/google-2025-environmental-report/) 

- More Efficient In-Context Learning with GLaM 

- (https://research.google/blog/more-efficient-in-context-learning-with-glam/) 

- Context caching overview 

- (/gemini-enterprise-agent-platform/models/context-cache/context-cache-overview) 

## Optimize resource usage for sustainability

This principle in the sustainability pillar of the Google Cloud Well-Architected Framework (/architecture/framework/sustainability) provides recommendations to help you optimize resource usage by your workloads in Google Cloud. 

### Principle overview

Optimizing resource usage is crucial for enhancing the sustainability of your cloud environment. Every resource that's provisioned—from compute cycles to data storage—directly affects energy usage, water intensity, and carbon emissions. To reduce the environmental footprint of your workloads, you need to make informed choices when you provision, manage, and use cloud resources. 

### Recommendations

To optimize resource usage, consider the recommendations in the following sections. 

#### Implement automated and dynamic scaling

Automated and dynamic scaling ensures that resource usage is optimal, which helps to prevent energy waste from idle or over-provisioned infrastructure. The reduction in wasted energy translates to lower costs and lower carbon emissions. 

Use the following techniques to implement automated and dynamic scalability. 

Use horizontal scaling 

Horizontal scaling is the preferred scaling technique for most cloud-first applications. Instead of increasing the size of each instance, known as _vertical scaling_ , you add instances to distribute the load. For example, you can use managed instance groups (MIGs) (/compute/docs/autoscaler) to automatically scale out a group of Compute Engine VMs. Horizontally scaled infrastructure is more resilient because the failure of an instance doesn't affect the availability of the application. Horizontal scaling is also a resource-efficient technique for applications that have variable load levels. 

Configure appropriate scaling policies 

Configure autoscaling settings based on the requirements of your workloads. Define custom metrics and thresholds that are specific to application behavior. Instead of relying solely on CPU utilization, consider metrics like queue depth for asynchronous tasks, request latency, and custom application metrics. To prevent 

frequent, unnecessary scaling or _flapping_ , define clear scaling policies. For example, for workloads that you deploy in Google Kubernetes Engine (GKE), configure an appropriate cluster autoscaling policy 

(https://cloud.google.com/blog/products/containers-kubernetes/gke-features-to-optimizeresource-allocation) 

Combine reactive and proactive scaling 

With reactive scaling, the system scales in response to real-time load changes. This technique is suitable for applications that have unpredictable spikes in load. 

Proactive scaling is suitable for workloads with predictable patterns, such as fixed daily business hours and weekly reports generation. For such workloads, use scheduled autoscaling to pre-provision resources so that they can handle an anticipated load level. This technique prevents a scramble for resources and ensures smoother user experience with higher efficiency. This technique also helps you plan proactively for known spikes in load such as major sales events and focused marketing efforts. 

Google Cloud managed services and features like GKE Autopilot, Cloud Run, and MIGs automatically manage proactive scaling by learning from your workload patterns. By default, when a Cloud Run service doesn't receive any traffic, it scales to zero instances. 

Design stateless applications 

For an application to scale horizontally, its components should be stateless. This means that a specific user's session or data isn't tied to a single compute instance. When you store session state outside the compute instance, such as in Memorystore for Redis, any compute instance can handle requests from any user. This design approach enables horizontal scaling that's seamless and efficient. 

#### Use scheduling and batches

Batch processing is ideal for large-scale, non-urgent workloads. Batch jobs can help to optimize your workloads for energy efficiency and cost. 

Use the following techniques to implement scheduling and batch jobs. 

Schedule for low carbon intensity 

Schedule your batch jobs to run in low-carbon regions and during periods when the local electrical grid has a high percentage of clean energy. To identify the least carbon-intensive times of day for a region, use the Carbon Footprint report 

(/carbon-footprint/docs/view-carbon-data). 

Use Spot VMs for noncritical workloads 

Spot VMs (/compute/docs/instances/spot) let you take advantage of unused Compute Engine capacity at a steep discount. Spot VMs can be preempted, but they provide a cost-effective way to process large datasets without the need for dedicated, always-on resources. Spot VMs are ideal for non-critical, fault-tolerant batch jobs. 

Consolidate and parallelize jobs 

To reduce the overhead for starting up and shutting down individual jobs, group similar jobs into a single large batch. Run these high-volume workloads on services like Batch (/batch/docs/get-started). The service automatically provisions and manages the necessary infrastructure, which helps to ensures optimal resource utilization. 

Use managed services 

Managed services like Batch and Dataflow (/dataflow/docs/overview) automatically handle resource provisioning, scheduling, and monitoring. The cloud platform handles resource optimization. You can focus on the application logic. For example, Dataflow automatically scales the number of workers 

(/dataflow/docs/horizontal-autoscaling) based on the data volume in the pipeline, so you don't pay for idle resources. 

#### Match VM machine families to workload requirements

The machine types that you can use for your Compute Engine VMs are grouped into machine families (/compute/docs/machine-resource), which are optimized for different workloads. Choose appropriate machine families based on the requirements of your workloads. 

|Machine family|Recommended for<br>workload types|Sustainability guidance|
|---|---|---|
|General-purpose<br>instances (E2, N2, N4,<br>Tau T2A/T2D): These<br>instances provide a<br>balanced ratio of CPU to<br>memory.|Web servers,<br>microservices, small to<br>medium databases,<br>and development<br>environments.|The E2 series is highly cost-efficient and<br>energy-efficient due to its dynamic allocation<br>of resources. The Tau T2A series uses Arm-<br>based processors, which are often more<br>energy-efficient per unit of performance for<br>large-scale workloads.|
|Compute-optimized<br>instances (C2, C3):<br>These instances provide<br>a high vCPU-to-memory<br>ratio and high<br>performance per core.|High performance<br>computing (HPC),<br>batch processing,<br>gaming servers, and<br>CPU-based data<br>analytics.|A C-series instance lets you complete CPU-<br>intensive tasks faster, which reduces the total<br>compute time and energy consumption of the<br>job.|
|Memory-optimized<br>instances (M3, M2):<br>These instances are<br>designed for workloads<br>that require a large<br>amount of memory.|Large in-memory<br>databases and data<br>warehouses, such as<br>SAP HANA or in-<br>memory analytics.|Memory-optimized instances enable the<br>consolidation of memory-heavy workloads on<br>fewer physical nodes. This consolidation<br>reduces the total energy that's required when<br>compared to using multiple smaller instances.<br>High-performance memory reduces data-<br>access latency, which can reduce the total<br>time that the CPU spends in an active state.|
|Storage-optimized<br>instances (Z3): These<br>instances provide high-<br>throughput, low-latency<br>local SSD storage.|Data warehousing, log<br>analytics, and SQL,<br>NoSQL, and vector<br>databases.|Storage-optimized instances process massive<br>datasets locally, which helps to eliminate the<br>energy that's used for cross-location network<br>data egress. When you use local storage for<br>high-IOPS tasks, you avoid over-provisioning<br>multiple standard instances.|
|Accelerator-optimized<br>instances (A3, A2, G2):<br>These instances are buil<br>for GPU and TPU-<br>accelerated workloads,<br>such as AI, ML, and HPC.|t<br> <br>ML model training and<br>inference, and<br>scientific simulations.|TPUs(/tpu) are engineered for optimal energy<br>efficiency. They deliver higher computations<br>per watt.<br>A GPU-accelerated instance like the A3 series<br>with NVIDIA H100 GPUs can be significantly<br>more energy-efficient for training large models<br>than a CPU-only alternative. Although a GPU-<br>accelerated instance has higher nominal<br>power usage, the task is completed much<br>faster.|

#### Upgrade to the latest machine types

Use of the latest machine types might help to improve sustainability. When machine types are updated, they're often designed to be more energy-efficient and to provide higher performance per watt. VMs that use the latest machine types might complete the same amount of work with lower power consumption. 

CPUs, GPUs, and TPUs often benefit from technical advancements in chip architecture, such as the following: 

- **Specialized cores** : Advancements in processors often include specialized cores or instructions for common workloads. For example, CPUs might have dedicated cores for vector operations or integrated AI accelerators. When these tasks are offloaded from the main CPU, the tasks are completed more efficiently and they consume less energy. 

- **Improved power management** : Advancements in chip architectures often include more sophisticated power management features, such as dynamic adjustment of voltage and frequency based on the workload. These powermanagement features enable the chips to run at peak efficiency and enter low-power states when they are idle, which minimizes energy consumption. 

The technical improvements in chip architecture provide the following direct benefits for sustainability and cost: 

- **Higher performance per watt** : This is a key metric for sustainability. For example, the C4 VMs demonstrate 40% higher price-performance 

- (/compute/docs/general-purpose-machines#c4_series) when compared to C3 VMs for the same energy consumption. The C4A processor provides 60% higher energy-efficiency (/compute/docs/general-purpose-machines#c4a_series) over comparable x86 processors. These performance capabilities let you complete tasks faster or use fewer instances for the same load. 

- **Lower total energy consumption** : With improved processors, compute resources are used for a shorter duration for a given task, which reduces the overall energy usage and carbon footprint. The carbon impact is particularly high for short-lived, compute-intensive workloads like batch jobs and ML model training. 

- **Optimal resource utilization** : The latest machine types are often better suited for modern software and are more compatible with advanced features 

of cloud platforms. These machine types typically enable better resource utilization, which reduces the need for over-provisioning and helps to ensure that every watt of power is used productively. 

#### Deploy containerized applications

You can use container-based, fully-managed services such as GKE and Cloud Run as a part of your strategy for sustainable cloud computing. These services help to optimize resource utilization and automate resource management. 

Leverage the scale-to-zero capability of Cloud Run 

Cloud Run provides a managed serverless environment that automatically scales instances to zero when there is no incoming traffic for a service or when a job is completed. Autoscaling helps to eliminate energy consumption by idle infrastructure. Resources are powered only when they actively process requests. This strategy is highly effective for intermittent or event-driven workloads. For AI workloads, you can use GPUs with Cloud Run (/run/docs/configuring/services/gpu), which lets you consume and pay for GPUs only when they are used. 

Automate resource optimization using GKE 

GKE is a container orchestration platform, which ensures that applications use only the resources that they need. To help you automate resource optimization, GKE provides the following techniques: 

**Bin packing** 

(https://kubernetes.io/docs/concepts/scheduling-eviction/resource-bin-packing/): GKE Autopilot intelligently packs multiple containers on the available nodes. Bin packing maximizes the utilization of each node and reduces the number of idle or underutilized nodes, which helps to reduce energy consumption. 

**Horizontal Pod autoscaling (HPA)** 

(/kubernetes-engine/docs/concepts/horizontalpodautoscaler): With HPA, the number of container replicas (Pods) is adjusted automatically based on predefined metrics like CPU usage or custom application-specific metrics. For example, if your application experiences a spike in traffic, GKE adds Pods to meet the demand. When the traffic subsides, GKE reduces the number of Pods. This 

dynamic scaling prevents over-provisioning of resources, so you don't pay for or power up unnecessary compute capacity. 

**Vertical Pod autoscaling (VPA)** 

(/kubernetes-engine/docs/concepts/verticalpodautoscaler): You can configure GKE to automatically adjust the CPU and memory allocations and limits for individual containers. This configuration ensures that a container isn't allocated more resources than it needs, which helps to prevent resource over-provisioning. 

**GKE multidimensional Pod autoscaling** 

(/kubernetes-engine/docs/how-to/multidimensional-pod-autoscaling): For complex workloads, you can configure HPA and VPA simultaneously to optimize both the number of Pods and the size of each Pod. This technique helps to ensure the smallest possible energy footprint for the required performance. 

**Topology-Aware Scheduling (TAS)** 

(/ai-hypercomputer/docs/workloads/schedule-gke-workloads-tas): TAS enhances the network efficiency for AI and ML workloads in GKE by placing Pods based on the physical structure of the data center infrastructure. TAS strategically colocates workloads to minimize network hops. This colocation helps to reduce communication latency and energy consumption. By optimizing the physical alignment of nodes and specialized hardware, TAS accelerates task completion and maximizes the energy efficiency of large-scale AI and ML workloads. 

#### Configure carbon-aware scheduling

At Google, we continually shift our workloads to locations 

(https://blog.google/outreach-initiatives/sustainability/carbon-aware-computing-location/) and times 

(https://blog.google/inside-google/infrastructure/data-centers-work-harder-sun-shines-windblows/) 

that provide the cleanest electricity. We also repurpose, or harvest (https://cloud.google.com/blog/topics/sustainability/hardware-harvesting-at-google-reducingwaste-and-emissions) 

- , older equipment for alternative use cases. You can use this carbon-aware scheduling strategy to ensure that your containerized workloads use clean energy. 

To implement carbon-aware scheduling, you need information about the energy mix that powers data centers in a region in real time. You can get this information 

in a machine-readable format from the Carbon free energy for Google Cloud regions (https://github.com/GoogleCloudPlatform/region-carbon-info) repository in GitHub or from a BigQuery public dataset 

(https://console.cloud.google.com/marketplace/product/bigquery-public-datasets/regional-cfe). The hourly grid mix and carbon intensity data that's used to calculate the Google annual carbon dataset is sourced from Electricity Maps 

(https://app.electricitymaps.com/). 

To implement carbon-aware scheduling, we recommend the following techniques: 

- **Geographical shifting** : Schedule your workloads to run in regions that use a higher proportion of renewable energy sources. This approach lets you use cleaner electrical grids. 

- **Temporal shifting** : For non-critical, flexible workloads like batch processing, configure the workloads to run during off-peak hours or when renewable energy is most abundant. This approach is known as temporal shifting and helps reduce the overall carbon footprint by taking advantage of cleaner energy sources when they are available. 

#### Architect energy-efficient disaster recovery

Preparing for disaster recovery (DR) often involves pre-provisioning redundant resources in a secondary region. However, idle or under-utilized resources can cause significant energy waste. Choose DR strategies that maximize resource utilization and minimize the carbon impact without compromising your recovery time objectives (RTO). 

Optimize for cold start efficiency 

Use the following approaches to minimize or eliminate active resources in your secondary (DR) region: 

- **Prioritize cold DR** (https://en.wikipedia.org/wiki/Backup_site#Cold_site): Keep resources in the DR region turned off or in a scaled-to-zero state. This approach helps to eliminate the carbon footprint of idle compute resources. 

- **Take advantage of serverless failover** : Use managed serverless services like Cloud Run for DR endpoints. Cloud Run scales to zero when it isn't in use, 

so you can maintain a DR topology that consumes no energy until traffic is diverted to the DR region. 

**Automate recovery with infrastructure-as-code (IaC)** : Instead of keeping resources in the DR site running (warm), use an IaC tool like Terraform to rapidly provision environments only when needed. 

Balance redundancy and utilization 

Resource redundancy is a primary driver of energy waste. To reduce redundancy, use the following approaches: 

**Prefer active-active over active-passive** : In an active-passive setup, the resources in the passive site are idle, which results in wasted energy. An active-active architecture that's optimally sized ensures that all of the provisioned resources across both regions actively serve traffic. This approach helps you maximize the energy efficiency of your infrastructure. 

**Right-size redundancy** : Replicate data and services across regions only when the replication is necessary to meet high-availability or DR requirements. Every additional replica increases the energy cost of persistent storage and network egress. 

## Develop energy-efficient software

This principle in the sustainability pillar of the Google Cloud Well-Architected Framework (/architecture/framework/sustainability) provides recommendations to write software that minimizes energy consumption and server load. 

### Principle overview

When you follow best practices to build your cloud applications, you optimize the energy that's utilized by the cloud infrastructure resources: AI, compute, storage, and network. You also help to reduce the water requirements of the data centers and the energy that end-user devices consume when they access your applications. 

To build energy-efficient software, you need to integrate sustainability considerations throughout the software lifecycle, from design and development to deployment, maintenance, and archival. For detailed guidance about using AI to build software that minimizes the environmental impact of cloud workloads, see the Google Cloud ebook, Build Software Sustainably 

(https://cloud.google.com/resources/content/build-software-sustainably). 

### Recommendations

The recommendations in this section are grouped into the following focus areas: 

- Minimize computational work (#minimal-computations): Favor lean, focused code that eliminates redundant logic and avoids unnecessary computations or feature bloat. 

- Use efcient algorithms and data structuresfi (#efficient-algorithms): Choose time-efficient and memory-efficient algorithms that reduce CPU load and minimize memory usage. 

- Optimize compute and data operations (#optimized-operations): Develop with the goal of efficiently using all of the available resources, including CPU, memory, disk I/O, and network. For example, when you replace busy loops with event-driven logic, you avoid unnecessary polling. 

- Implement frontend optimization (#optimized-frontend): To reduce the power that's consumed by end-user devices, use strategies like minimization, compression, and lazy-loading (https://en.wikipedia.org/wiki/Lazy_loading) for images and assets. 

#### Minimize computational work

To write energy-efficient software, you need to minimize the total amount of computational work that your application performs. Every unnecessary instruction, redundant loop, and extra feature consumes energy, time, and resources. Use the following recommendations to build software that performs minimal computations. 

Write lean, focused code 

To write minimal code that's essential to achieve the required outcomes, use the following approaches: 

- **Eliminate redundant logic and feature bloat** : Write code that performs only the essential functions. Avoid features that increase the computational overhead and complexity but don't provide measurable value to your users. 

- **Refactor** : To improve energy efficiency over time, regularly audit your applications to identify unused features. Take action to remove or refactor such features as appropriate. 

- **Avoid unnecessary operations** : Don't compute a value or run an action until the result is needed. Use techniques like lazy evaluation (https://en.wikipedia.org/wiki/Lazy_evaluation), which delay computations until a dependent component in the application needs the output. 

- **Prioritize code readability and reusability** : Write code that's readable and reusable. This approach minimizes duplication and follows the don't repeat yourself (DRY) principle (https://en.wikipedia.org/wiki/Don%27t_repeat_yourself), which can help to reduce carbon emissions from software development and maintenance. 

Use backend caching 

Backend caching ensures that an application does not perform the same work repeatedly. A high cache-hit ratio leads to an almost linear reduction in energy consumption per request. To implement backend caching, use the following techniques: 

- **Cache frequent data** : Store frequently accessed data in a temporary, highperformance storage location. For example, use an in-memory caching service like Memorystore (/memorystore/docs). When an application retrieves data from a cache, the volume of database queries and disk I/O operations is reduced. Consequently, the load on the databases and servers in the backend decreases. 

- **Cache API responses** : To avoid redundant and costly network calls, cache the results of frequent API requests. 

- **Prioritize in-memory caching** : To eliminate slow disk I/O operations and complex database queries, store data in high-speed memory (RAM). 

**Select appropriate cache-write strategies** 

- (https://en.wikipedia.org/wiki/Cache_(computing)#Write_policies): 

   - The write-through strategy ensures that data is written synchronously to the cache _and_ the persistent store. This strategy increases the likelihood of cache hits, so the persistent store gets fewer energy-intensive read requests. 

   - The write-back (write-behind) strategy enhances the performance of write-heavy applications. Data is written to the cache first, and the database is updated asynchronously later. This strategy reduces the immediate write load on slower databases. 

- **Use smart eviction policies** : Keep the cache lean and efficient. To remove stale or low-utility data and to maximize the space that's available for frequently requested data, use policies like time to live (TTL), least recently used (LRU), and least frequently used (LFU). 

#### Use efficient algorithms and data structures

The algorithms and data structures that you choose determine the raw computational complexity of your software. When you select appropriate algorithms and data structures, you minimize the number of CPU cycles and memory operations that are required to complete a task. Fewer CPU cycles and memory operations lead to lower energy consumption. 

Choose algorithms for optimal time complexity 

Prioritize algorithms that achieve the required result in the least amount of time. This approach helps to reduce the duration of resource usage. To select algorithms that optimize resource usage, use the following approaches: 

- **Focus on reducing complexity** : To evaluate complexity, look beyond runtime metrics and consider the theoretical complexity of the algorithm. For example, when compared to bubble sorting (https://en.wikipedia.org/wiki/Bubble_sort), merge sorting (https://en.wikipedia.org/wiki/Merge_sort) significantly reduces the computational load and energy consumption for large datasets. 

- **Avoid redundant work** : Use built-in, optimized functions in your chosen programming language or framework. These functions are often implemented in a lower-level and more energy-efficient language like C or C++, so they are better optimized for the underlying hardware compared to custom-coded functions. 

Select data structures for efficiency 

The data structures that you choose determine the speed at which data can be retrieved, inserted, or processed. This speed affects CPU and memory usage. To select efficient data structures, use the following approaches: 

- **Optimize for search and retrieval** : For common operations like checking whether an item exists or retrieving a specific value, prefer data structures that are optimized for speed. For example, hash maps or hash sets enable near-constant time lookups, which is a more energy-efficient approach than linearly searching through an array. 

- **Minimize memory footprint** : Efficient data structures help to reduce the overall memory footprint of an application. Reduced memory access and management leads to lower power consumption. In addition, a leaner memory profile enables processes to run more efficiently, which lets you postpone resource upgrades. 

- **Use specialized structures** : Use data structures that are purpose-built for a given problem. For example, use a trie (https://en.wikipedia.org/wiki/Trie) data structure for rapid string-prefix searching, and use a priority queue when you need to access only the highest or lowest value efficiently. 

#### Optimize compute and data operations

When you develop software, focus on efficient and proportional resource usage across the entire technology stack. Treat CPU, memory, disk, and network as limited and shared resources. Recognize that efficient usage of resources leads to tangible reductions in costs and energy consumption. 

Optimize CPU utilization and idle time 

To minimize the time that the CPU spends in an active, energy-consuming state without performing meaningful work, use the following approaches: 

- **Prefer event-driven logic over polling** : Replace resource-intensive busy loops or constant checking (polling) with event-driven logic. An event-driven architecture ensures that the components of an application operate only when they're triggered by relevant events. This approach enables on-demand processing, which eliminates the need for resource-intensive polling. 

- **Prevent constant high frequency** : Write code that doesn't force the CPU to constantly operate at its highest frequency. To minimize energy consumption, systems that are idle should be able to enter low-power states or sleep modes. 

- **Use asynchronous processing** : To prevent threads from being locked during idle wait times, use asynchronous processing. This approach frees resources and leads to higher overall resource utilization. 

Manage memory and disk I/O efficiently 

Inefficient memory and disk usage leads to unnecessary processing and increased power consumption. To manage memory and I/O efficiently, use the following techniques: 

- **Strict memory management** : Take action to proactively release unused memory resources. Avoid holding large objects in memory for longer periods than necessary. This approach prevents performance bottlenecks and reduces the power that's consumed for memory access. 

- **Optimize disk I/O** : Reduce the frequency of your application's read and write interactions with persistent storage resources. For example, use an intermediary memory buffer to store data. Write the data to persistent storage at fixed intervals or when the buffer reaches a certain size. 

- **Batch operations** : Consolidate frequent, small disk operations into fewer, larger batch operations. A batch operation consumes less energy than many individual, small transactions. 

- **Use compression** : Reduce the amount of data that's written to or read from disks by applying suitable data-compression techniques. For example, to 

compress data that you store in Cloud Storage, you can use decompressive transcoding (/storage/docs/transcoding). 

Minimize network traffic 

Network resources consume significant energy during data transfer operations. To optimize network communication, use the following techniques: 

- **Minimize payload size** : Design your APIs and applications to transfer only the data that's needed for a request. Avoid fetching or returning large JSON or XML structures in cases where only a few fields are required. Ensure that the data structures that are returned are concise. 

- **Reduce round-trips** : To reduce the number of network round-trips that are required to complete a user action, use smarter protocols. For example, prefer HTTP/3 over HTTP/1.1, choose GraphQL over REST, use binary protocols, and consolidate API calls. When you reduce the volume of network calls, you reduce the energy consumption for both your servers and for end-user devices. 

#### Implement frontend optimization

Frontend optimization minimizes the data that your end users must download and process, which helps to reduce the load on the resources of end-user devices. 

Minimize code and assets 

When end users need to download and process smaller and more efficiently structured resources, their devices consume less power. To minimize the download volume and processing load on end-user devices, use the following techniques: 

- **Minimization and compression** : For JavaScript, CSS, and HTML files, remove unnecessary characters like whitespaces and comments by using appropriate minimization tools. Ensure that files like images are compressed and optimized. You can automate the minimization and compression of web assets by using a CI/CD pipeline. 

- **Lazy loading** : Load images, videos, and non-critical assets only when they are actually needed, such as when these elements scroll into the viewport of a 

web page. This approach reduces the volume of initial data transfer and the processing load on end-user devices. 

- **Smaller JavaScript bundles** : Eliminate unused code from your JavaScript bundles by using modern module bundlers and techniques like tree shaking (https://webpack.js.org/guides/tree-shaking/). This approach results in smaller files that load faster and use fewer server resources. 

- **Browser caching** : Use HTTP caching headers to instruct the user's browser to store static assets locally. Browser caching helps to prevent repeated downloads and unnecessary network traffic on subsequent visits. 

Prioritize lightweight user experience (UX) 

The design of your user interface can have a significant impact on the computational complexity for rendering frontend content. To build frontend interfaces that provide a lightweight UX, use the following techniques: 

- **Efficient rendering** : Avoid resource-intensive, frequent Document Object Model (DOM) (https://en.wikipedia.org/wiki/Document_Object_Model) manipulation. Write code that minimizes the rendering complexity and eliminates unnecessary re-rendering. 

- **Lightweight design patterns** : Where appropriate, prefer static sites or progressive web apps (PWAs) (https://en.wikipedia.org/wiki/Progressive_web_app). Such sites and apps load faster and require fewer server resources. 

- **Accessibility and performance** : Responsive, fast-loading sites are often more sustainable and accessible. An optimized, clutter-free design reduces the resources that are consumed when content is rendered. Websites that are optimized for performance and speed can help to drive higher revenue. According to a research study by Deloitte and Google, Milliseconds Make Millions 

- (https://www.thinkwithgoogle.com/_qs/documents/9757/Milliseconds_Make_Millions_repor t_hQYAbZJ.pdf#page=5) 

- , a 0.1-second (100ms) improvement in site speed leads to an 8.4% increase in conversions for retail sites and a 9.2% increase in the average order value. 

## Optimize data and storage for sustainability

This principle in the sustainability pillar of the Google Cloud Well-Architected Framework (/architecture/framework/sustainability) provides recommendations to help you optimize the energy efficiency and carbon footprint for your storage resources in Google Cloud. 

### Principle overview

Stored data isn't a passive resource. Energy is consumed and carbon emissions occur throughout the lifecycle of data. Every gigabyte of stored data requires physical infrastructure that's continuously powered, cooled, and managed. To achieve sustainable cloud architecture, treat data as a valuable but environmentally costly asset and prioritize proactive data governance. 

Your decisions about data retention, quality, and location can help you achieve substantial reductions in cloud costs and energy consumption. Minimize the data that you store, optimize where and how data you store data, and implement automated deletion and archival strategies. When you reduce data clutter, you improve system performance and fundamentally reduce the long-term environmental footprint of your data. 

### Recommendations

To optimize your data lifecycle and storage resources for sustainability, consider the recommendations in the following sections. 

#### Prioritize high-value data

Stored data that's unused, duplicated, or obsolete continues to consume energy to power the underlying infrastructure. To reduce the storage-related carbon footprint, use the following techniques. 

Identify and eliminate duplication 

Establish policies to prevent the needless replication of datasets across multiple Google Cloud projects or services. Use central data repositories like BigQuery datasets (/bigquery/docs/datasets-intro) or Cloud Storage buckets (/storage/docs/buckets) as single sources of truth and grant appropriate access to these repositories. 

Remove shadow data and dark data 

_Dark data_ is data for which the utility or owner is unknown. _Shadow data_ means unauthorized copies of data. Scan your storage systems and find dark data and shadow data by using a data discovery and cataloging solution like Knowledge Catalog (/dataplex/docs/introduction). Regularly audit these findings and implement a process for archival or deletion of dark and shadow data as appropriate. 

Minimize the data volume for AI workloads 

Store only the features and processed data that are required for model training and serving. Where possible, use techniques like data sampling, aggregation, and synthetic data generation to achieve model performance without relying on massive raw datasets. 

Integrate data quality checks 

Implement automatic data validation and data cleaning pipelines by using services like Managed Service for Apache Spark (/dataproc/docs/concepts/overview), Dataflow (/dataflow/docs/overview), or Knowledge Catalog at the point of data ingestion. Lowquality data causes wasted storage space. It also leads to unnecessary energy consumption when the data is used later for analytics or AI training. 

Review the value density of data 

Periodically review high-volume datasets like logs and IoT streams. Determine whether any data can be summarized, aggregated, or down-sampled to maintain the required information density and reduce the physical storage volume. 

Critically evaluate the need for backups 

Assess the need for backups of data that you can regenerate with minimal effort. Examples of such data include intermediate ETL results, ephemeral caches, and training data that's derived from a stable, permanent source. Retain backups for only the data that is unique or expensive to recreate. 

#### Optimize storage lifecycle management

Automate the storage lifecycle so that when the utility of data declines, the data is moved to an energy-efficient storage class or retired, as appropriate. Use the following techniques. 

Select an appropriate Cloud Storage class 

Automate the transition of data in Cloud Storage to lower-carbon storage classes based on access frequency by using Object Lifecycle Management 

(/storage/docs/lifecycle). 

- Use Standard storage for only actively used datasets, such as current production models. 

- Transition data such as older AI training datasets or less-frequently accessed backups to Nearline or Coldline storage. 

- For long-term retention, use Archive storage, which is optimized for energy efficiency at scale. 

Implement aggressive data lifecycle policies 

Define clear, automated time to live (TTL) policies for non-essential data, such as log files, temporary model artifacts, and outdated intermediate results. Use lifecycle rules to automatically delete such data after a defined period. 

Mandate resource tagging 

Mandate the use of consistent resource tags and labels for all of your Cloud Storage buckets, BigQuery datasets, and persistent disks. Create tags that indicate the data owner, purpose of the data, and the retention period. Use Organization Policy Service constraints to ensure that required tags, such as retention period, 

are applied to resources. Tags let you automate lifecycle management, create granular FinOps reports, and produce carbon emissions reports. 

Right-size and deprovision compute storage 

Regularly audit persistent disks that are attached to Compute Engine instances and ensure that the disks aren't over-provisioned. Use snapshots only when they are necessary for backup. Delete old, unused snapshots. For databases, use data retention policies to reduce the size of the underlying persistent disks. 

Optimize the storage format 

For storage that serves analytics workloads, prefer compressed, columnar formats like Parquet or optimized Avro over row-based formats like JSON or CSV. Columnar storage significantly reduces physical disk-space requirements and improves the read efficiency. This optimization helps to reduce energy consumption for the associated compute and I/O operations. 

#### Optimize regionality and data movement

The physical location and movement of your data affect the consumption of network resources and the energy required for storage. Optimize data regionality by using the following techniques. 

Select low-carbon storage regions 

Depending on your compliance requirements, store data in Google Cloud regions that use a higher percentage of carbon-free energy (CFE) or that have lower grid carbon intensity. Restrict the creation of storage buckets in high-carbon regions by using the resource locations 

(/resource-manager/docs/organization-policy/defining-locations) Organization Policy constraint. For information about CFE and carbon-intensity data for Google Cloud regions, see Carbon-free energy for Google Cloud regions 

(https://cloud.google.com/sustainability/region-carbon). 

Minimize replication 

Replicate data across regions only to meet mandatory disaster recovery (DR) or high-availability (HA) requirements. Cross-region and multi-region replication operations significantly increase the energy cost and carbon footprint of your data. 

Optimize data processing locations 

To reduce energy consumption for network data transfer, deploy compute-intensive workloads like AI training and BigQuery processing in the same region as the data source. 

Optimize data movement for your partners and customers 

To move large volumes of data across cloud services, locations, and providers, encourage your partners and customers to use Storage Transfer Service (/storage-transfer/docs/overview) or data-sharing APIs. Avoid mass data dumps. For public datasets, use Requester Pays (/storage/docs/requester-pays) buckets to shift the data transfer and processing costs and the environmental impact to end users. 

## Continuously measure and improve sustainability

This principle in the sustainability pillar of the Google Cloud Well-Architected Framework (/architecture/framework/sustainability) provides recommendations to help you measure and continuously improve the sustainability of your workloads in Google Cloud. 

### Principle overview

To ensure that your cloud workloads remain sustainable, you need accurate and transparent metrics. Verifiable metrics let you translate sustainability goals to actions. Every resource that you create in the cloud has an associated carbon footprint. To build and maintain sustainable cloud architectures, you must integrate the measurement of carbon data into your operational feedback loop. 

The recommendations in this section provide a framework for using Carbon Footprint (https://cloud.google.com/carbon-footprint) to quantify carbon emissions, identify carbon hotspots, implement targeted workload optimizations, and verify the outcomes of the optimization efforts. This framework lets you efficiently align your cost optimization goals with verifiable carbon reduction targets. 

#### Carbon Footprint reporting methodology

Carbon Footprint provides a transparent, auditable, and globally-aligned report of your cloud-related emissions. The report adheres to international standards, primarily the Greenhouse Gas (GHG) Protocol (https://ghgprotocol.org/standards) for carbon reporting and accounting. The Carbon Footprint report uses location-based and market-based accounting methods. Location-based accounting is based on the local grid's emissions factor. Market-based accounting considers Google's purchases of carbon-free energy (CFE). This dual approach helps you understand both the physical-grid impact and the carbon benefit of your workloads in Google Cloud. 

For more information about how the Carbon Footprint report is prepared, including the data sources used, Scope-3 inclusions, and the customer allocation model, see Carbon Footprint reporting methodology (/carbon-footprint/docs/methodology). 

### Recommendations

To use carbon measurement for continuous improvement, consider the recommendations in the following sections. The recommendations are structured as phases of maturity for implementing sustainable-by-design cloud operations: 

- Phase 1: Establish a baseline (#establish-baseline) 

- Phase 2: Identify hotspots (#identify-hotspots) 

- Phase 3: Implement targeted optimization (#optimize) 

- Phase 4: Institutionalize sustainability practices and reporting (#institutionalize) 

#### Phase 1: Establish a baseline

In this phase, you set up the necessary tools and ensure that data is accessible and correctly integrated. 

1. **Grant permissions** : Grant permissions to teams like FinOps, SecOps and platform engineering so that they can access the Carbon Footprint dashboard in the Google Cloud console. Grant the Carbon Footprint Viewer role 

   - (/carbon-footprint/docs/iam#standard-roles) ( `roles/billing.carbonViewer` ) in Identity and Access Management (IAM) for the appropriate billing account. 

2. **Automate data export** : Before you export data, ensure that your Google Cloud resource hierarchy (folders and projects) 

   - (/architecture/blueprints/security-foundations/organization-structure) and your resource annotations (tags and labels) 

   - (/resource-manager/docs/tags/tags-overview#tags_and_labels) accurately reflect the organization of your business units. Because Carbon Footprint data is aggregated at the project level, a well-defined hierarchy is essential for correctly attributing emissions. Configure automated export of Carbon Footprint data (/carbon-footprint/docs/export) to BigQuery. The exported data lets you perform deep analysis, correlate carbon data with cost and usage data, and produce custom reports. 

3. **Define carbon-related key performance indicators (KPIs)** : Establish metrics that connect carbon emissions to business value. For example, carbon intensity is a metric for the number of kilograms of CO 2 equivalent (https://en.wikipedia.org/wiki/Global_warming_potential) per customer, transaction, or revenue unit. 

#### Phase 2: Identify carbon hotspots

Identify the areas that have the largest environmental impact by analyzing the granular data in the Carbon Footprint report. Use the following techniques for this analysis: 

- **Prioritize by scope** : To quickly identify the largest gross carbon emitters, analyze the data in the dashboard by project, region, and service. 

- **Use dual-accounting** : When you evaluate the carbon impact in a region, consider both location-based emissions (the environmental impact of the local 

electrical grid) and market-based emissions (the benefit of Google's CFE investments). 

- **Correlate with cost** : Join the carbon data in BigQuery with your billing data and assess the impact of optimization actions on sustainability _and_ cost. Although cost and carbon often trend together, you can only use cost as an initial indicator. For example, in high-cost regions that have high Carbon-Free Energy (CFE) scores (https://cloud.withgoogle.com/region-picker/), workloads might have high cost but low market-based emissions. Always validate optimization assumptions against real location-based metrics and market-based metrics. 

- **Annotate data to measure return on effort (ROE)** : Annotate the carbon data in BigQuery with specific events, like right-sizing a resource or decommissioning a large service. The annotations let you attribute reductions in carbon emission and cost to specific optimization initiatives, so that you can measure and demonstrate the outcome of each initiative. 

#### Phase 3: Implement targeted optimization

This is the execution phase for implementing sustainable-by-design cloud operations. Use the following strategies to optimize specific resources that you identify as significant drivers of cost and carbon emissions: 

- **Decommission unattended projects** : As part of your IT service management (ITSM) workflows, regularly check the unattended project recommender (/recommender/docs/unattended-project-recommender) that's integrated with the Carbon Footprint data. To achieve immediate, verified reductions in carbon emissions and cost, automate the review and eventual removal of unused projects through tracked engineering tickets. 

- **Right-size resources** : Match the provisioned resource capacity to actual utilization by using Active Assist right-sizing recommenders 

- (/recommender/docs/recommenders) like machine type recommendations for Compute Engine VMs 

- (/compute/docs/instances/apply-machine-type-recommendations-for-instances). For compute-intensive tasks and AI workloads, use the most efficient machine types and AI models. 

- **Adopt carbon-aware scheduling** : For batch workloads that aren't timecritical, integrate regional CFE data into the scheduling logic. Where feasible, 

limit the creation of new resources to low-carbon regions by using the resource locations (/resource-manager/docs/organization-policy/defining-locations) constraint in Organization Policy Service. 

- **Reduce data sprawl** : Implement data governance policies to ensure that infrequently accessed data is transitioned to an appropriate cold storage class (Nearline, Coldline, or Archive) or is permanently deleted. This strategy helps to reduce the energy cost of your storage resources. 

- **Refine application code** : Fix code-level inefficiencies that cause excessive resource usage or unnecessary computation. 

For more information, see the following: 

- Use regions that consume low-carbon energy 

- (/architecture/framework/sustainability/low-carbon-regions) 

- Optimize AI and ML workloads 

- (/architecture/framework/sustainability/ai-ml-energy-efficiency) 

- Optimize resource usage 

- (/architecture/framework/sustainability/optimize-resource-usage) 

- Develop energy-efficient software 

- (/architecture/framework/sustainability/energy-efficient-software) 

- Optimize data and storage for sustainability 

- (/architecture/framework/sustainability/optimize-storage) 

#### Phase 4: Institutionalize your sustainability practices and reporting

In this phase, you embed carbon measurement into your governance framework. This approach helps to ensure that your organization has the capabilities and controls that are necessary for continuous sustainability improvements and verifiable reporting. 

**Implement** **_GreenOps_ governance** : Establish a formal GreenOps (https://en.wikipedia.org/wiki/Green_computing#Cloud_computing) function or working group to integrate Carbon Footprint data with Cloud Billing data. Integrate your monthly BigQuery carbon exports (/carbon-footprint/docs/export) directly into your existing FinOps dashboards, such as Looker. Presenting 

carbon and cost data in a single interface helps to ensure that sustainability is part of your standard operational review cycle. This function must define accountability for carbon reduction targets across projects, align cost optimization with sustainability goals, and implement reporting to track carbon efficiency against spending. 

- **Use Carbon Footprint data for reporting and compliance** : Use the verified, auditable Carbon Footprint data in BigQuery to create formal environmental, social, and governance (ESG) disclosures. This approach lets you meet stakeholder demands for transparency and helps to ensure compliance with mandatory and voluntary regulations. 

- **Invest in training and awareness** : Implement mandatory sustainability training for relevant technical and non-technical teams. Your teams need to know how to access and interpret the Carbon Footprint data and how to apply optimization recommendations in their daily workflows and design choices. For more information, see Provide role-based sustainability training (/architecture/framework/sustainability/culture#provide_rolebased_sustainability_training) 

- **Define carbon requirements** : Incorporate carbon emission metrics as nonfunctional requirements (NFR) in your application's acceptance criteria for new deployments. This practice helps to ensure that architects and developers prioritize low-carbon design options from the start of the application development lifecycle. 

- **Automate GreenOps** : Automate the implementation of Active Assist recommendations by using scripts, templates, and infrastructure-as-code (IaC) pipelines. This practice ensures that teams apply recommendations consistently and rapidly across the organization. 

## Promote a culture of sustainability

This principle in the sustainability pillar of the Google Cloud Well-Architected Framework (/architecture/framework/sustainability) provides recommendations to help you build a culture where teams across your organization are aware of and proficient in sustainability practices. 

### Principle overview

To apply sustainability practices, you need more than tools and techniques. You need a cultural shift that's driven by education and accountability. Your teams need to be aware of sustainability concerns and they must have practical proficiency in sustainability practices. 

- _Awareness of sustainability_ is the contextual knowledge that every architectural and operational decision has tangible effects on sustainability. Teams must recognize that the cloud isn't an abstract collection of virtual resources, but it's driven by physical resources that consume energy and produce carbon emissions. 

- _Proficiency in sustainability practices_ includes knowledge to interpret carbon emissions data, experience with implementing cloud sustainability governance, and technical skills to refactor code for energy efficiency. 

To align sustainability practices with organizational goals, your teams need to understand how energy usage by cloud infrastructure and software contributes to the organization's carbon footprint. Well-planned training helps to ensure that all of your stakeholders—from developers and architects to finance professionals and operations engineers—understand the sustainability context of their daily work. This shared understanding empowers teams to move beyond passive compliance to active optimization, which makes your cloud workloads sustainable-by-design. Sustainability becomes a core non-functional requirement (NFR) like other requirements for security, cost, performance, and reliability. 

### Recommendations

To build awareness of sustainability concerns and proficiency in sustainability practices, consider the recommendations in the following sections. 

#### Provide business context and alignment with organizational goals

Sustainability isn't just a technical exercise; it requires a cultural shift that aligns individual actions with the environmental mission of your organization. When 

teams understand the _why_ behind sustainability initiatives, they are more likely to adopt the initiatives as core principles rather than as optional tasks. 

Connect to the big picture 

Help your teams understand how individual architectural choices—such as selecting a low-carbon region or optimizing a data pipeline—contribute to the organization's overall sustainability commitments. Explicitly communicate how these choices affect the local community and the industry. Transform abstract carbon metrics into tangible indicators of progress toward corporate social responsibility (CSR) goals. 

For example, a message like the following informs teams about the positive outcome and executive recognition of a decision to migrate a workload to a lowcarbon region and to use a power-efficient machine type. The message references the CO 2 equivalent (https://en.wikipedia.org/wiki/Global_warming_potential), which helps your team contextualize the impact of carbon reduction measures. 

_"By migrating our data analytics engine to the us-central1_ 

_Low CO_ _2_<sup>(https://cloud.google.com/sustainability/region-carbon#region-picker)</sup><sup>_region and_</sup> _upgrading our clusters to C4A Axion-based instances, we fundamentally changed our carbon profile. This shift resulted in a 75% reduction in the carbon intensity of our data analytics engine, which translates to a reduction of 12 metric tons of CO2 equivalent this quarter. This migration had a significant impact on our business goals and was included in the Q4 newsletter to our board."_ 

Communicate financial and sustainability goals 

Transparency is critical for aligning sustainability practices with goals. To the extent feasible, widely share sustainability goals and progress across the organization. Highlight sustainability progress in the annual financial statements. Such communication ensures that technical teams view their work as a vital part of the organization's public-facing commitments and financial health. 

Embrace a shared fate mindset 

Educate teams about the collaborative nature of cloud sustainability. Google is responsible for the sustainability _of_ the cloud, which includes the efficiency of the infrastructure and data centers. You (the customer) are responsible for sustainability of your resources and workloads _in_ the cloud. When you frame this collaboration as a partnership of shared fate, you reinforce the understanding that your organization and Google work together to achieve optimal environmental outcomes. 

#### Provide role-based sustainability training

To ensure that sustainability is a practical skill rather than a theoretical concept, tailor the sustainability training to specific job roles. The sustainability tools and techniques that a data scientist can use are very different from those available to a FinOps analyst, as described in the following table: 

|Role|Training focus|
|---|---|
|Data<br>scientists and<br>ML engineers|Carbon-intensity of compute: Demonstrate the differences between running AI<br>training jobs on<br>legacy systems(https://en.wikipedia.org/wiki/Legacy_system)<br>versus purpose-built AI accelerators. Highlight how a model with fewer<br>parameters can produce the required accuracy with significantly lower energy<br>consumption.|
|Developers|Code efficiency and resource consumption: Illustrate how high-latency code or<br>inefficient loops translate directly to extended CPU runtime and increased<br>energy consumption. Emphasize the importance of lightweight containers and<br>the need to optimize application performance to reduce the environmental<br>footprint of software.|
|Architects|Sustainable by design: Focus on region selection and workload placement. Show<br>how choosing a<br>Low CO<br>2 <sup>(https://cloud.google.com/sustainability/region-carbon#region-picker)</sup><br>region with a high percentage of renewable energy (like`northamerica-`<br>`northeast1`) fundamentally changes the carbon profile of your entire application<br>stack before you write a single line of code.|
|Platform<br>engineers and<br>operations<br>engineers|Maximizing utilization: Emphasize the environmental cost of idle resources and<br>over-provisioning. Present scenarios for automated scaling and right-sizing to<br>ensure that cloud resources are used efficiently. Explain how to create and track<br>sustainability-related metrics like utilization and how to translate metrics like<br>compute time into equivalent metrics of carbon emissions.|

|Role|Training focus|
|---|---|
|FinOps|Unit economics of carbon: Focus on the relationship between financial spend<br>and environmental impact. Demonstrate how GreenOps practices let an<br>organization track carbon per transaction, which helps to make sustainability a<br>key performance indicator (KPI) that's as critical as conventional KPIs like cost<br>and utilization.|
|Product<br>managers|Sustainability as a feature: Demonstrate how to integrate carbon-reduction<br>goals into product roadmaps. Show how simplified user journeys can help to<br>reduce the energy consumption by both cloud resources and end-user devices.|
|Business<br>leaders|Strategic alignment and reporting: Focus on how cloud sustainability affects<br>environmental, social, and governance (ESG) scores and public reputation.<br>Illustrate how sustainability choices help to reduce regulatory risk and fulfill<br>commitments to the community and industry.|

#### Advocate for sustainability and recognize success

To sustain long-term progress, you need to move beyond internal technical fixes and begin influencing your partners and the industry. 

Empower managers to advocate for sustainability 

Provide managers the data and permissions that they need to prioritize environmental impact similar to other business metrics like speed-to-market and cost. When managers have this data, they begin to view sustainability as a quality and efficiency standard rather than as a nice-to-have capability that slows production. They actively advocate for new cloud provider features—such as more granular carbon data and newer, greener processors in specific regions. 

Align with industry standards and frameworks 

To ensure that your sustainability efforts are credible and measurable, align internal practices with recognized global and regional standards. For more information, see Align sustainability practices with industry guidelines (/architecture/framework/sustainability/industry-guidelines). 

#### Incentivize sustainability efforts

To ensure that sustainability becomes an enduring part of the engineering culture, teams must realize the value of prioritizing sustainability. Transition from high-level goals to specific, measurable KPIs that reward improvement and efficiency. 

Define carbon KPIs and NFRs 

Treat sustainability as a core technical requirement. When you define carbon KPIs, such as grams of CO2 equivalent per million requests or carbon-intensity per AI training run, you make the impact on sustainability visible and actionable. For example, integrate sustainability into the NFRs for every new project. In other words, just as a system must meet a specific latency or availability target, the system must also stay within a defined carbon emissions budget. 

Measure return on effort 

Help your teams identify high-impact, low-effort sustainability wins—such as shifting a batch job to a different region—versus a complex code refactoring exercise that might provide minimal gains. Provide visibility into the return on effort (ROE). When a team chooses a more efficient processor family, they must know exactly how much carbon emission they avoided relative to the time and effort that's required to migrate to the new processor. 

Recognize and celebrate carbon reduction 

Sustainability impact is often hidden in the background of infrastructure. To build the momentum for sustainability progress, make successes visible to the entire organization. For example, use annotations in monitoring dashboards to mark when a team deployed a specific sustainability optimization. This visibility lets teams point to data in the dashboard and claim recognition for their successes. 

## Align sustainability practices with industry guidelines

This principle in the sustainability pillar of the Google Cloud Well-Architected Framework (/architecture/framework/sustainability) provides an overview of industry 

guidelines and frameworks with which you should align your sustainability efforts. 

### Principle overview

To ensure that your sustainability initiatives are built upon a foundation of globally recognized methods for measurement, reporting, and verification, we recommend that you align your initiatives with the following industry guidelines: 

W3C Web Sustainability Guidelines (#ws-guidelines) 

Green Software Foundation (#gsg-guidelines) 

Greenhouse Gas Protocol (#ghg-protocol) 

When you align your sustainability initiatives with these shared external guidelines, your initiatives get the credibility and auditability that investors, regulatory bodies, and other external stakeholders demand. You also foster accountability across engineering teams, embed sustainability within employee training, and successfully integrate cloud operations into enterprise-wide commitments for environmental, social, and governance (ESG) reporting. 

### W3C Web Sustainability Guidelines

### W3C Web Sustainability Guidelines (WSG)

(https://www.w3.org/TR/web-sustainability-guidelines/) is an emerging framework of best practices developed by a W3C working group to address the environmental impact of digital products and services. The guidelines cover the entire lifecycle of a digital solution including business and product strategy, user experience (UX) design, web development, hosting, infrastructure, and systems. The core goal of WSG is to enable developers and architects to build websites and web applications that are more energy-efficient and that reduce network traffic, client-side processing, and server-side resource consumption. These guidelines serve a critical reference point for aligning application-level sustainability with cloud-level architectural decisions. 

### Green Software Foundation

The Green Software Foundation (GSF) (https://greensoftware.foundation/) focuses on building an industry ecosystem around sustainable software. Its mission is to drive the creation of software that's designed, built, and operated to minimize the carbon footprint. The GSF developed the Software Carbon Intensity (SCI) specification, which provides a common standard for measuring the rate of carbon emissions of any piece of software. Alignment with the GSF helps developers connect an application's efficiency directly to the carbon impact of the cloud environment. 


## Google Cloud Well-Architected Framework (printable, all pillars)

URL: https://docs.cloud.google.com/architecture/framework/printable

### Greenhouse Gas Protocol

The Greenhouse Gas (GHG) Protocol (https://ghgprotocol.org/) is a widely used set of standards for measuring, managing, and publicly reporting greenhouse gas emissions. The protocol was developed through a partnership between the World Resources Institute (WRI) and the World Business Council for Sustainable Development (WBCSD). The GHG protocol provides the essential framework for corporate climate accounting. The Carbon Footprint report provides data for emission scopes (/carbon-footprint/docs/methodology#boundaries) that are relevant to cloud usage. For more information, see Carbon Footprint reporting methodology (/carbon-footprint/docs/methodology). 

Adherence to the GHG Protocol helps to ensure that your sustainability initiatives have credibility and that external parties can audit your carbon emissions data. You also help prevent the perception of greenwashing 

(https://en.wikipedia.org/wiki/Greenwashing) and satisfy the due-diligence requirements of your investors, regulators, and external stakeholders. Verified and audited data helps your organization prove accountability and build trust in public-facing sustainability commitments. 

1. For more information about agent skills standard, see Agent Skills Overview (https://agentskills.io/home). ↩ (#fnref1)
