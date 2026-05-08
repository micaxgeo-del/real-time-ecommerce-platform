
# Real-Time Ecommerce Analytics Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![GCP](https://img.shields.io/badge/GCP-Cloud-blue?logo=googlecloud)
![ETL](https://img.shields.io/badge/ETL-Pipeline-success)
![Data Engineering](https://img.shields.io/badge/Data-Engineering-0ea5e9)

# Real-Time Ecommerce Analytics Platform

![Architecture](architecture/architecture_diagram.svg)

## Project Overview

**Real-Time Ecommerce Analytics Platform** is a professional portfolio project focused on Data Engineering and Data Analytics.

It simulates a modern ecommerce data platform capable of processing user events, transforming raw data into analytics-ready datasets, and exposing business KPIs through an interactive executive dashboard.

The project demonstrates practical skills in:

- Data Engineering
- ETL/ELT Pipelines
- Data Modeling
- Streaming Data Concepts
- BigQuery-style Analytics
- Dashboard Development
- Cloud Data Architecture

---

## Business Problem

Ecommerce companies generate continuous user activity data from product views, searches, carts, checkouts and purchases.

Without a reliable data platform, business teams can face delayed reporting, inconsistent KPIs, limited visibility into customer behavior, poor funnel analysis and slow decision-making.

This project solves that problem by transforming raw ecommerce events into trusted business metrics and interactive dashboards.

---

## Solution

The platform follows a cloud-inspired architecture:

```text
Ecommerce Events → Pub/Sub → Dataflow → BigQuery → Dashboard
                                      → Bigtable
```

For local portfolio execution, the architecture is implemented with:

```text
Simulated Events → Raw Data → Python ETL Pipeline → Processed Data → Streamlit Dashboard
```

---

## Tech Stack

| Area | Tools |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Analytics | SQL, BigQuery-style queries |
| Dashboard | Streamlit, Plotly |
| Cloud Concepts | Pub/Sub, Dataflow, BigQuery, Bigtable |
| Engineering Concepts | ETL/ELT, data modeling, streaming, pipelines |

---

## Dashboard Features
## Dashboard Preview

### Executive KPI Dashboard

![KPI Dashboard](assets/screenshots/kpis_dashboard.png)

---

### Analytics & Revenue Monitoring

![Analytics Charts](assets/screenshots/analytics_charts.png)

---

### Data Engineering & Operational Layer

![Data Engineering Layer](assets/screenshots/data_engineering_layer.png)
- Executive KPI cards
- Revenue trend analysis
- Active users monitoring
- Conversion funnel
- Revenue by category
- Traffic source performance
- Device revenue distribution
- Customer segmentation
- Interactive filters by date, country, device, category and traffic source

---

## Key KPIs

- Revenue
- Orders
- Conversion Rate
- Average Order Value
- Active Users
- Sessions
- Events
- Cart Abandonment Rate
- Customer Segments

---

## Repository Structure

```text
real-time-ecommerce-platform/
│
├── architecture/
│   ├── architecture.md
│   └── architecture_diagram.svg
│
├── dashboards/
│   └── streamlit/
│       └── app.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── business_case.md
│   ├── dashboard_documentation.md
│   ├── kpi_dictionary.md
│   └── linkedin_project_description.md
│
├── src/
│   ├── producer/
│   └── pipelines/
│
├── sql/
│   └── bigquery/
│
├── requirements.txt
└── README.md
```

---

## How to Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the ETL pipeline:

```bash
python src/pipelines/etl_pipeline.py
```

Run the dashboard:

```bash
streamlit run dashboards/streamlit/app.py
```

Run the event producer example:

```bash
python src/producer/event_producer.py
```

---

## Data Engineering Concepts Demonstrated

- Event-driven architecture
- Streaming ingestion concepts
- ETL/ELT design
- Data cleaning and transformation
- Analytics-ready modeling
- BigQuery-style analytical queries
- Operational analytics with Bigtable concepts
- Dashboard-ready datasets
- KPI layer design

---

## Portfolio Value

This project is designed as a flagship portfolio project for roles such as:

- Data Analyst
- Junior Data Engineer
- Analytics Engineer
- BI Engineer
- Cloud Data Analyst

---

## Author

**Micaela Feriale**  
Data Analytics | Data Engineering | SQL | Python | BigQuery | ETL | BI


---

## Live Demo

Deploy the dashboard using Streamlit Cloud or Render to create a public portfolio demo.

Main dashboard file:

```text
dashboards/streamlit/app.py
```

---

## Professional Portfolio Goals

This project was designed to simulate a real-world ecommerce analytics platform and demonstrate practical skills in:

- Data Engineering
- Cloud Architecture
- ETL Pipelines
- KPI Modeling
- Dashboard Development
- Streaming Data Concepts
- Business Analytics

---

## Future Improvements

- Apache Airflow orchestration
- Docker containerization
- dbt transformations
- CI/CD pipelines
- Terraform infrastructure
- Real-time streaming integration
