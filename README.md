# Financial Signal Automation & LLM Filtering Pipeline

## Project Overview
Designed and deployed an event-driven automation pipeline that reduces signal noise via real-time LLM-based verification. Orchestrated a multi-stage logic workflow integrating Python-based data simulation with n8n for scalable, automated financial risk assessment and logging.

## System Architecture
Below is the decoupled microservice design showcasing how events flow linearly through automated retry boundaries to preserve system reliability if downstream nodes face latency or rate limits:

![System Architecture Sketch](Event%20driven%20microservices%20architecture%20diagram.jpg)

## Production Execution Proof
The system was validated through a full-scale pipeline execution processing a 240-trade historical ledger to evaluate the noise-reduction layer:

![n8n Metric Execution Proof](./n8n%20OutputExecution%20Screenshot.png)

### Core Performance Metrics Captured
* **Quant-Only Baseline Error Rate**: 55%
* **LLM-Filtered Signal Error Rate**: 25%
* **False Positive Noise Reduction**: ~30%

## Core Features Built
* **Decoupled Microservices**: Built a multi-stage workflow utilizing automated retry patterns to handle external API rate limits and network latency gracefully.
* **Algorithmic Risk Management**: Implemented custom JavaScript processors for real-time dynamic position sizing and automated risk-to-reward profiling.
* **Automated Logging Sink**: Synced validated workflow payloads dynamically to data warehouses and messaging nodes via schema-mapped abstractions.
