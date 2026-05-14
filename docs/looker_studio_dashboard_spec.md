# Looker Studio Dashboard Specification

This project can be replicated in Looker Studio using the processed dataset:

`data/processed/ecommerce_dashboard_dataset.csv`

## Recommended Controls

Add these controls at the top of the dashboard:

1. Date range control
2. Channel filter
3. Region filter
4. Category filter
5. Device filter

## KPI Scorecards

Create scorecards for:

- Revenue: `SUM(revenue_usd)`
- Orders: `SUM(orders)`
- Conversion Rate: `SUM(orders) / SUM(sessions)`
- Average Order Value: `SUM(revenue_usd) / SUM(orders)`
- CAC: `SUM(marketing_spend_usd) / SUM(orders)`
- ROAS: `SUM(revenue_usd) / SUM(marketing_spend_usd)`
- Gross Margin: `SUM(profit_usd) / SUM(revenue_usd)`

## Recommended Charts

### Executive Overview
- Time series: Revenue by month
- Bar chart: Orders by month
- Line chart: Conversion rate by month
- Line chart: CAC by month

### Marketing Performance
- Bar chart: Revenue by channel
- Scatter plot: CAC vs ROAS by channel
- Table: Channel, revenue, orders, conversion, CAC, ROAS

### Commercial Segments
- Treemap: Revenue by category
- Bar chart: Revenue by region
- Bar chart: Conversion rate by device

## Business Storytelling

This dashboard shows how acquisition channels, regional performance and category mix affect revenue, profitability and marketing efficiency.