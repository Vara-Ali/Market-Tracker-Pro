from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    "owner": "market_tracker",
    "start_date": datetime(2024, 1, 1),
    "retries": 1,
}

with DAG(
    dag_id="market_tracker_scrapers",
    default_args=default_args,
    schedule_interval="@daily",  # runs once daily
    catchup=False
) as dag:

    scrape_metro = BashOperator(
        task_id="scrape_metro",
        bash_command="cd /opt/airflow/data_ingestion && python metro_scraper.py"
    )

    scrape_grocer = BashOperator(
        task_id="scrape_grocer",
        bash_command="cd /opt/airflow/data_ingestion && python grocer_scraper.py"
    )

    scrape_metro >> scrape_grocer  # example of chaining tasks
