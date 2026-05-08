# Architecture Documentation

## Cloud-Inspired Architecture

```text
Ecommerce Events → Pub/Sub → Dataflow → BigQuery → Dashboard
                                      → Bigtable
```

## Local Portfolio Implementation

```text
Simulated Events → Raw CSV → Python ETL → Processed Data → Streamlit Dashboard
```

## Components

- Pub/Sub: streaming ingestion concept.
- Dataflow: ETL and streaming processing concept.
- BigQuery: analytical warehouse concept.
- Bigtable: low-latency operational metrics concept.
- Streamlit: interactive dashboard.
