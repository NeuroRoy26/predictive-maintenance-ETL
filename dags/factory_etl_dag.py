from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import os

from src.main import run_automated_pipeline

default_args = {
    'owner': 'airflow',
    'retries': 2,
    'retry_delay': timedelta(minutes=5), 
}

with DAG(
    dag_id='industrial_sensor_orchestrator',
    default_args=default_args,
    schedule_interval='@hourly', 
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:

    datasets = ['FD001', 'FD002', 'FD003', 'FD004']
    
    for ds in datasets:
        task_id = f'process_sensor_data_{ds}'
        
        PythonOperator(
            task_id=task_id,
            python_callable=run_automated_pipeline,
            op_kwargs={'dataset_id': ds} 
        )