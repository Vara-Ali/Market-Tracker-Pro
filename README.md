# Market Tracker Pro

**Market Tracker Pro** is a real-time data platform that monitors and analyzes local market prices, supply trends, and shortages across various regions in Pakistan. It combines powerful data engineering tools to ingest, process, model, and expose actionable insights through APIs and dashboards.

> A full-scale backend data engineering project designed to solve real-world inflation transparency issues — built with technologies like Kafka, FastAPI, PostgreSQL, DBT, Airflow, and more.

---

## Problem Statement

Local markets in Pakistan suffer from highly inconsistent pricing, unpredictable shortages, and lack of transparent data. Consumers are often overcharged, vendors lack benchmarking tools, and authorities struggle to monitor or predict inflation events due to the absence of real-time data systems.

---

## Project Goals

- Collect live and batch data from multiple sources (scrapers, APIs, user submissions)
- Process data via streaming and ETL pipelines
- Model and store price/supply data in structured databases
- Expose data via RESTful APIs
- Visualize trends and alerts through dashboards

---

## Key Features

- Real-time price & supply tracking by item and location  
- Vendor-submitted price monitoring via API  
- Automatic alerts for price spikes and shortages  
- Region-wise dashboards for consumers, vendors, and policymakers  
- Scalable backend infrastructure with CI/CD and Docker  

---

## Tech Stack

| Layer                     | Technology                       |
|--------------------------|----------------------------------|
| Data Ingestion           | Python, Web Scraping, Kafka      |
| Stream Processing        | Apache Kafka, Apache Spark       |
| Storage                  | PostgreSQL, MongoDB, TimeScaleDB |
| Transformation & Modeling| DBT, Pandas, Airflow             |
| API Layer                | FastAPI                          |
| Visualization            | Streamlit / Power BI             |
| DevOps                   | Docker, GitHub Actions           |



