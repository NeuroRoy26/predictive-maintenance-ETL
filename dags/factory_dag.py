from airflow import DAG
from airflow.operators.python import PythonOperator
from src.main import run_automated_pipeline, check_global_quality
from datetime import datetime, timedelta
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.main import run_automated_pipeline

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='factory_sensor_orchestrator',
    default_args=default_args,
    description='Parallel ETL for multiple factory sensor streams',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    datasets = ['FD001', 'FD002', 'FD003', 'FD004']

    tasks = []
    for ds in datasets:
        t = PythonOperator(
            task_id=f'process_dataset_{ds}',
            python_callable=run_automated_pipeline,
            op_kwargs={'dataset_id': ds}, 
        )
        tasks.append(t)

    tasks

    datasets = ['FD001', 'FD002', 'FD003', 'FD004']
    etl_tasks = []
    for ds in datasets:
        t = PythonOperator(
            task_id=f'process_dataset_{ds}',
            python_callable=run_automated_pipeline,
            op_kwargs={'dataset_id': ds},
        )
        etl_tasks.append(t)

    quality_check = PythonOperator(
        task_id='final_data_quality_gate',
        python_callable=check_global_quality,
        op_kwargs={'datasets': datasets}
    )

    etl_tasks >> quality_check