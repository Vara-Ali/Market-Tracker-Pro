from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Vara',
    'depends_on_past': False,
    'start_date': datetime(2024, 6, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='metro_scraper_dag',
    default_args=default_args,
    description='Scrape Metro and load to PostgreSQL',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    run_metro_scraper = BashOperator(
        task_id='run_metro_scraper',
        bash_command='python /opt/airflow/data_ingestion/metro_scraper.py'
    )

    run_metro_scraper
