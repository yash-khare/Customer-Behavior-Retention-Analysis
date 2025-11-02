# 🧠 Customer Behavior & Retention Analytics Dashboard

A full end-to-end **Business Analytics project** that analyzes customer purchasing behavior, identifies churn patterns, and predicts retention risk using **PostgreSQL**, **Python**, and **Power BI**.

---

## 🚀 Project Overview

This project simulates a real-world **Amazon-style Customer Analytics workflow**:

1. **Data Engineering (PostgreSQL):**  
   Built a data mart from synthetic e-commerce data (customers, orders, order items, products).
2. **Customer Behavior Analysis:**  
   Explored key behavioral metrics — recency, frequency, monetary value (RFM).
3. **Churn Modeling (Python):**  
   Predicted customer churn using logistic regression with engineered features.
4. **Visualization (Power BI):**  
   Designed an interactive dashboard to visualize KPIs, churn rate by segment, and high-risk customers.

---

## 🧩 Tech Stack

| Layer         | Tools / Technologies                            |
| ------------- | ----------------------------------------------- |
| Database      | PostgreSQL                                      |
| Scripting     | Python (pandas, scikit-learn, matplotlib)       |
| Visualization | Power BI                                        |
| Other         | SQL, Streamlit (optional for dashboard preview) |

---

## 📊 Power BI Dashboard Highlights

The Power BI report contains three layers of insights:

### **1️⃣ KPI Overview**

- Churn Rate (%)
- Average Recency (days)
- Average Orders per Customer
- Average Revenue per Customer

### **2️⃣ Churn Insights**

- Churn Rate by Region
- Churn Rate by Income Band

### **3️⃣ High-Risk Customers**

- Dynamic table of customers with high churn risk
- Filterable by region and income band

## 📁 Project Structure

customer-behavior-retention-analysis/
│
├── Dashboard/
│ └── Customer_Behavior_Retention.pbix
│
├── data/
│ ├── churn_mart.csv
│ ├── scored_test.csv
│
├── sql/
│ ├── schema.sql
│ ├── load.sql
│ ├── mart_churn.sql
│
├── src/
│ ├── generate_synthetic_data.py
│ ├── feature_engineering_and_model.py
│
└── README.md

---

## 🧠 Key Insights

- Customers in the **Low income band** had the **highest churn rate (82%)**.
- **North region** showed slightly higher churn compared to others.
- Most churned customers had **recency > 180 days**.
- Retention strategies should focus on **mid/low income segments** with long inactivity.

---

## 📈 How to Run This Project

### **1. Database Setup**

```bash
createdb retention_db
psql -d retention_db -f sql/schema.sql
psql -d retention_db -f sql/load.sql
psql -d retention_db -f sql/mart_churn.sql -o data/churn_mart.csv
```

## 📸 Dashboard Preview

<img width="690" height="717" alt="Screenshot 2025-11-02 160917" src="https://github.com/user-attachments/assets/f77435b8-b34f-4c59-bf98-31e93ab5e49e" />



🏷️ Tags

#PowerBI #BusinessAnalytics #PostgreSQL #Python #DataEngineering #ChurnPrediction #DataVisualization
