from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Vara',
    'start_date': datetime(2024, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='data_processing_dag',
    default_args=default_args,
    description='Clean and normalize scraped product prices',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    process_data = BashOperator(
        task_id='clean_product_prices',
        bash_command='python /opt/airflow/data_processing/clean_prices.py'
    )

    process_data
