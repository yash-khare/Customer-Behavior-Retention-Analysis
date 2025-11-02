import numpy as np, pandas as pd
from datetime import datetime, timedelta
rng = np.random.default_rng(42)

N_CUSTOMERS = 5000
N_PRODUCTS = 300
START = pd.Timestamp("2023-01-01")
END   = pd.Timestamp("2024-12-31")

def make_customers(n=N_CUSTOMERS):
    cust_ids = np.arange(1, n+1)
    signup_dates = pd.to_datetime(rng.integers(0, 365, size=n), unit='D', origin=START)
    regions = rng.choice(["North","South","East","West"], size=n, p=[.25,.25,.25,.25])
    ages = rng.integers(18, 65, size=n)
    income_band = rng.choice(["Low","Mid","High"], size=n, p=[.4,.45,.15])
    return pd.DataFrame({"customer_id":cust_ids,"signup_date":signup_dates,
                         "region":regions,"age":ages,"income_band":income_band})

def make_products(n=N_PRODUCTS):
    prod_ids = np.arange(1, n+1)
    cats = rng.choice(["Electronics","Apparel","Home","Grocery","Beauty"], size=n,
                      p=[.2,.25,.2,.25,.1])
    base_price = rng.normal(100, 40, size=n).clip(5, 500).round(2)
    return pd.DataFrame({"product_id":prod_ids,"category":cats,"base_price":base_price})

def make_orders(customers, products):
    rows = []
    order_items = []
    order_id = 1
    item_id = 1
    for _, c in customers.iterrows():
        # purchase propensity signals churn risk
        mean_orders = {"Low":1.2,"Mid":2.5,"High":4.0}[c["income_band"]]
        n_orders = rng.poisson(mean_orders*2)  # over 2 yrs
        order_dates = pd.to_datetime(rng.integers(0, (END-START).days+1, size=n_orders),
                                     unit='D', origin=START)
        order_dates = np.sort(order_dates)
        for od in order_dates:
            rows.append({"order_id":order_id,"customer_id":c.customer_id,"order_date":od})
            # 1-5 items per order
            k = rng.integers(1,6)
            prod_sample = products.sample(k, replace=False, random_state=int(order_id))
            for _, p in prod_sample.iterrows():
                qty = rng.integers(1,4)
                price = float(np.clip(rng.normal(p.base_price, p.base_price*0.1), 1, 1000))
                order_items.append({"order_item_id":item_id,"order_id":order_id,
                                    "product_id":p.product_id,"quantity":qty,
                                    "unit_price":round(price,2)})
                item_id += 1
            order_id += 1
    return (pd.DataFrame(rows), pd.DataFrame(order_items))

def main(outdir="data"):
    import os; os.makedirs(outdir, exist_ok=True)
    customers = make_customers()
    products = make_products()
    orders, order_items = make_orders(customers, products)

    customers.to_csv(f"{outdir}/customers.csv", index=False)
    products.to_csv(f"{outdir}/products.csv", index=False)
    orders.to_csv(f"{outdir}/orders.csv", index=False)
    order_items.to_csv(f"{outdir}/order_items.csv", index=False)

if __name__ == "__main__":
    main()