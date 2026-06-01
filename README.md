# Financial Signal Automation & LLM Filtering Pipeline

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/shanjeev-b-u/financial-automation-pipeline/lint-test.yml?branch=main&label=CI%2fCD%20Build)
![Python Version](https://img.shields.io/badge/python-3.11-green?logo=python&logoColor=white)

## Project Overview
Designed and deployed an event-driven automation pipeline that reduces signal noise via real-time LLM-based verification. Orchestrated a multi-stage logic workflow integrating Python-based data simulation with n8n for scalable, automated financial risk assessment and logging.

## Quick Project Previews & Components
To inspect the operational and data layers of this pipeline immediately, explore the live core assets mapped out below:

* 🛠️ **[Explore Core Processing Logic](./src/transform.py)** — Inspect the high-precision Python engine engineered with explicit type hints and strict decimal calculation structures.
* 🧪 **[Review Automated Test Suites](./tests/test_transform.py)** — Inspect the deterministic test coverage validated automatically via continuous integration.
* 📐 **[Review System Architecture Map](#system-architecture)** — Jump straight to the fully diagrammed event boundaries and failure mitigation topology.

## Getting Started & Setup Instructions

### Prerequisites
* Python 3.11+ installed locally
* Docker Desktop (Optional, for containerized execution)

### Local Installation
1. Clone the repository to your local workspace:
   ```bash
   git clone [https://github.com/shanjeev-b-u/financial-automation-pipeline.git](https://github.com/shanjeev-b-u/financial-automation-pipeline.git)
   cd financial-automation-pipeline
   cp .env.example .env
   pip install -r requirements.txt
   python src/transform.py

## System Architecture
Below is the decoupled microservice design showcasing how events flow linearly through automated retry boundaries to preserve system reliability if downstream nodes face latency or rate limits:

<img src="https://github.com/shanjeev-b-u/financial-automation-pipeline/blob/main/Event-driven%20microservices%20architecture%20diagram.png?raw=true" alt="System Architecture Sketch" width="100%">

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

## Pipeline Processing Sample
Below is an example of a raw unstructured signal entering the ingest layer, alongside the finalized, high-precision sanitized payload outputted by the risk engine:

### Incoming Raw Trade Signal Data
```json
{
  "signal_id": "SIG-9982X",
  "Entry Price": "100.05",
  "Quantity": "10",
  "Source": "Telegram Alpha Channel Stream"
}
