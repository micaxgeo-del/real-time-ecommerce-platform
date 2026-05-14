-- BigQuery-style KPI query for executive dashboard

SELECT
  DATE_TRUNC(date, MONTH) AS month,
  channel,
  region,
  category,
  device,
  SUM(revenue_usd) AS revenue_usd,
  SUM(profit_usd) AS profit_usd,
  SUM(orders) AS orders,
  SUM(sessions) AS sessions,
  SUM(marketing_spend_usd) AS marketing_spend_usd,
  SAFE_DIVIDE(SUM(orders), SUM(sessions)) AS conversion_rate,
  SAFE_DIVIDE(SUM(revenue_usd), SUM(orders)) AS average_order_value,
  SAFE_DIVIDE(SUM(marketing_spend_usd), SUM(orders)) AS customer_acquisition_cost,
  SAFE_DIVIDE(SUM(revenue_usd), SUM(marketing_spend_usd)) AS roas,
  SAFE_DIVIDE(SUM(profit_usd), SUM(revenue_usd)) AS gross_margin_pct
FROM `project.dataset.ecommerce_dashboard_dataset`
GROUP BY 1,2,3,4,5
ORDER BY month;