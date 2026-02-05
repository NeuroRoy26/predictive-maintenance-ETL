# Predictive Maintenance ETL & Orchestration Pipeline

##  Overview
This repository features a production-grade ETL (Extract, Transform, Load) and Orchestration pipeline designed for high-dimensional industrial sensor data. Beyond simple data cleaning, this system uses **Apache Airflow** to manage parallel data streams, ensuring data integrity and reliability for predictive maintenance in a simulated factory environment.

##  System Architecture
The pipeline is engineered for modularity and scalability:
1. **Ingestion Layer (`ingest.py`):** Robust file I/O with error handling to ensure "reliable data flows."
2. **Transformation Layer (`transform.py`):** Automated zero-variance filtering (dead sensor removal) and rolling-mean smoothing to address "complex data issues" like industrial noise.
3. **Database Layer (`database.py`):** Implements the "Load" phase into a relational database, featuring analytical views for machine health reporting.
4. **Orchestration Layer (`dags/`):** Manages parallel execution of multiple datasets (FD001-FD004) with a final **Data Quality Gateway** to ensure accuracy and completeness.

##  Getting Started
### Using Docker-Compose (Orchestrated Run)
This will spin up the entire stack, including the Airflow Web UI.
```bash
docker-compose up --build
```
Access the Airflow UI: Open http://localhost:8080 to monitor streams in real-time.

Local Python Execution (Alternative)
```bash
pip install -r requirements.txt
python src/main.py
```

##  Data Quality & Monitoring
Quality Gateway: A final task that validates all parallel streams before database finalization.
Traceability: Comprehensive logging for real-time "monitoring and troubleshooting.

*For detailed logic on signal processing and schema enforcement, please refer to architecture.txt*
