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
    dag_id='grocer_scraper_dag',
    default_args=default_args,
    description='Scrape GrocerApp and load to PostgreSQL',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    run_grocer_scraper = BashOperator(
        task_id='run_grocer_scraper',
        bash_command='python /opt/airflow/data_ingestion/grocer_scraper.py'
    )

    run_grocer_scraper
