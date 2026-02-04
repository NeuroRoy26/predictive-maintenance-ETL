architecture.md

predictive-maintenance-ETL/
├── data/               # Raw NASA data files
├── notebooks/          # Exploratory Data Analysis (EDA)
├── src/                
│   ├── ingest.py       # Data loading logic
│   ├── transform.py    # Cleaning and anomaly detection
│   ├── database.py     # Handles load phase
│   └── main.py         # Entry point for the pipeline
├── requirements.txt    # List of dependencies
└── README.md           # Documentation

System Architecture & Data Logic
1. Data Flow Overview
This pipeline follows a modular ETL (Extract, Transform, Load) architecture to ensure scalability and maintainability in a manufacturing environment.

Ingestion Phase: Reads raw multi-variate sensor data from flat files, simulating an edge-to-cloud data transfer.

Transformation Phase: Applies domain-specific cleaning logic to remove industrial "noise" and ensure dataset integrity.

Validation Phase: Performs post-transformation checks to ensure the completeness of data before it reaches downstream monitoring systems.

2. Technical Design Decisions
A. Handling "Dead" Sensors (Zero-Variance Filter)
In a real-world Gigafactory environment, sensors may fail or stay at a constant value.

Implementation: The pipeline automatically identifies and drops columns with zero variance.

Impact: Reduces computational overhead and prevents machine learning models from training on non-informative data.

B. Signal Smoothing (Rolling Average)
Raw industrial sensor data often contains high-frequency electrical noise.

Implementation: A 5-cycle rolling mean is applied to sensor streams.

Impact: Provides a cleaner trend for "Predictive Maintenance," allowing for more accurate troubleshooting of reliable data flows.

C. Outlier Management (Percentile Clipping)
Extreme sensor spikes can occur due to telemetry errors rather than physical machine faults.

Implementation: Data is clipped at the 1st and 99th percentiles.

Impact: Prevents statistical distortion while maintaining the core operational range of the assembly shop machinery.

3. Data Integrity & Quality Checks
To address the JD requirement for "accuracy and completeness of data," the pipeline includes:

Schema Enforcement: Explicitly naming and typing columns during ingestion to prevent data drift.

Logging: Every stage of the pipeline records its status, allowing engineers to "identify, analyze, and address complex data issues" quickly.