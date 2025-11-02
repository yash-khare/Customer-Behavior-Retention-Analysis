WITH params AS (
  SELECT DATE '2024-12-31' AS end_date, 60::INT AS churn_window_days
),

last_purchase AS (
  SELECT o.customer_id, MAX(o.order_date) AS last_purchase_date
  FROM orders o
  GROUP BY o.customer_id
),
agg_spend AS (
  SELECT
    o.customer_id,
    COUNT(DISTINCT o.order_id) AS orders_cnt,
    SUM(oi.quantity * oi.unit_price) AS revenue,
    AVG(oi.unit_price) AS avg_item_price,
    MIN(o.order_date) AS first_order_date,
    MAX(o.order_date) AS last_order_date
  FROM orders o
  JOIN order_items oi ON oi.order_id = o.order_id
  GROUP BY o.customer_id
),
rfe AS (
  -- Recency (days), Frequency, Monetary style features
  SELECT
    c.customer_id,
    ((SELECT end_date FROM params) - COALESCE(lp.last_purchase_date, (SELECT end_date FROM params)))::INT AS recency_days,
    COALESCE(a.orders_cnt, 0) AS orders_cnt,
    COALESCE(a.revenue, 0) AS revenue
  FROM customers c
  LEFT JOIN last_purchase lp ON lp.customer_id = c.customer_id
  LEFT JOIN agg_spend a ON a.customer_id = c.customer_id
),
labels AS (
  SELECT
    r.customer_id,
    CASE
      WHEN (SELECT end_date FROM params) - INTERVAL '60 days'
           <= (SELECT end_date FROM params) - (r.recency_days || ' days')::interval
      THEN 0  -- purchased within 60 days ⇒ not churned
      ELSE 1  -- no purchase within 60 days ⇒ churned
    END AS churn_label
  FROM rfe r
)
SELECT
  c.customer_id,
  c.signup_date,
  c.region,
  c.age,
  c.income_band,
  r.recency_days,
  r.orders_cnt,
  r.revenue,
  l.churn_label
FROM customers c
JOIN rfe r ON r.customer_id = c.customer_id
JOIN labels l ON l.customer_id = c.customer_id;