# Predictive Maintenance ETL Pipeline

## Overview
This repository contains a modular ETL (Extract, Transform, Load) pipeline designed to process high-dimensional sensor data from industrial machinery. The goal is to automate the ingestion and cleaning of "noisy" sensor streams to prepare them for predictive maintenance modeling and real-time monitoring.

##  Tech Stack
* **Language:** Python 3.9 (Pandas, NumPy, SciPy)
* **Infrastructure:** Docker (Containerized for deployment readiness)
* **DevOps:** Git/GitHub for version control, logging for pipeline monitoring
* **Data Source:** NASA Turbofan Engine Degradation Dataset (Multi-variate sensor time-series)

##  Architecture
The pipeline is designed with modularity to support collaborative development and code reviews:
1. **Ingestion Layer (`ingest.py`):** Handles raw file I/O with built-in error handling and logging to ensure reliable data flows.
2. **Transformation Layer (`transform.py`):** Performs automated data validation, drops low-variance sensors (dead sensors), and applies rolling-mean smoothing to filter electrical noise.
3. **Execution Layer (`main.py`):** Orchestrates the end-to-end flow and ensures data completeness before storage.

##  Getting Started
### Using Docker (Recommended)
This project is containerized to ensure it runs in any back-end environment.
```bash
docker build -t predictive-etl .
docker run predictive-etl

pip install -r requirements.txt
python src/main.py
```
Please read the architecture.md for detailed information on System Architecutre and Data Logic.