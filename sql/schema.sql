CREATE TABLE customers (
  customer_id   INT PRIMARY KEY,
  signup_date   DATE,
  region        TEXT,
  age           INT,
  income_band   TEXT
);

CREATE TABLE products (
  product_id  INT PRIMARY KEY,
  category    TEXT,
  base_price  NUMERIC(10,2)
);

CREATE TABLE orders (
  order_id     INT PRIMARY KEY,
  customer_id  INT REFERENCES customers(customer_id),
  order_date   DATE
);

CREATE TABLE order_items (
  order_item_id INT PRIMARY KEY,
  order_id      INT REFERENCES orders(order_id),
  product_id    INT REFERENCES products(product_id),
  quantity      INT,
  unit_price    NUMERIC(10,2)
);