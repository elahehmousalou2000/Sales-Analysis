import pandas as pd

df = pd.read_csv("sales.csv")
print(df.describe())

if "product" in df.columns and "sales" in df.columns:
    print(df.groupby("product")["sales"].sum().sort_values(ascending=False))
