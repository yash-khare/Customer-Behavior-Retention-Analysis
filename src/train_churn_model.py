import pandas as pd, numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, accuracy_score, classification_report

X = pd.read_csv("data/X.csv")
y = pd.read_csv("data/y.csv").iloc[:,0]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, stratify=y, random_state=42
)

pipe = Pipeline([
    ("scaler", StandardScaler(with_mean=False)),  # keep safe if sparse
    ("clf", LogisticRegression(max_iter=1000, class_weight="balanced"))
])

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)
proba = pipe.predict_proba(X_test)[:,1]

print("Accuracy:", accuracy_score(y_test, pred))
print("ROC AUC:", roc_auc_score(y_test, proba))
print(classification_report(y_test, pred, digits=3))

# Save for dashboard thresholds
pd.DataFrame({"customer_id": pd.read_csv("data/churn_mart.csv")["customer_id"].iloc[y_test.index],
              "churn_prob": proba,
              "label": y_test.reset_index(drop=True)}).to_csv("data/scored_test.csv", index=False)