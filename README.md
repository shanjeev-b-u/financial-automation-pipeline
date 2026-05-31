# Financial Signal Automation & LLM Filtering Pipeline

## Project Overview
Designed and deployed an event-driven automation pipeline that reduces signal noise via real-time LLM-based verification. Orchestrated a multi-stage logic workflow integrating Python-based data simulation with n8n for scalable, automated financial risk assessment and logging.

## System Performance Metrics
Validated system efficacy through a 240-trade simulated backtest window:
* **Quant-Only Baseline Error Rate**: 55%
* **LLM-Filtered Signal Error Rate**: 25%
* **False Positive Noise Reduction**: ~30%

## Core Features Built
* **Decoupled Architecture**: Built a multi-stage workflow utilizing automated retry patterns to handle external API rate limits and network latency gracefully.
* **Algorithmic Risk Management**: Implemented custom JavaScript processors for real-time dynamic position sizing and automated risk-to-reward profiling.
* **Automated Logging Sink**: Synced validated workflow payloads dynamically to data warehouses and messaging nodes via schema-mapped abstractions.
