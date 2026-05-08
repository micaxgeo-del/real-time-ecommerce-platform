# Real-Time Ecommerce Analytics Platform

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![SQL](https://img.shields.io/badge/SQL-Analytics-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit)
![GCP](https://img.shields.io/badge/GCP-Cloud-blue?logo=googlecloud)
![ETL](https://img.shields.io/badge/ETL-Pipeline-success)
![Data Engineering](https://img.shields.io/badge/Data-Engineering-0ea5e9)

![Architecture](architecture/architecture_diagram.svg)

---

## Overview

A cloud-inspired ecommerce analytics platform designed to simulate modern data engineering and analytics workflows.

The project processes simulated ecommerce events, transforms raw operational data into analytics-ready datasets and exposes business KPIs through interactive dashboards.

It was built to demonstrate practical capabilities across:

- Data Engineering
- Analytics Engineering
- ETL/ELT Pipeline Design
- Data Modeling
- Streaming & Event-Driven Concepts
- Cloud Analytics Architecture
- Business Intelligence & KPI Development

---

## Business Context

Modern ecommerce platforms generate continuous streams of operational events including product views, searches, carts, checkouts and purchases.

Without a scalable analytics platform, organizations can face:

- Delayed reporting
- Inconsistent KPIs
- Limited visibility into customer behavior
- Poor funnel analysis
- Slow operational decision-making

This project addresses those challenges by transforming raw event data into structured business insights and executive-level dashboards.

---

## Architecture

Cloud-inspired architecture:

```text
Ecommerce Events → Pub/Sub → Dataflow → BigQuery → Dashboard
                                      → Bigtable
