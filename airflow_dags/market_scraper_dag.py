from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'Vara',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='market_scraper_dag',
    default_args=default_args,
    description='Scrapes market data and stores in PostgreSQL',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['market', 'scraper'],
) as dag:

    scrape_grocer = BashOperator(
        task_id='scrape_grocer_data',
        bash_command='python /opt/airflow/data_ingestion/grocer_scraper.py',
    )

    load_data = BashOperator(
        task_id='load_to_postgres',
        bash_command='python /opt/airflow/data_ingestion/load_to_db.py',
    )

    scrape_grocer >> load_data
