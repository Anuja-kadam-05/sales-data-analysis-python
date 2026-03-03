import pandas as pd
import numpy as np

df = pd.read_csv("sales_data.csv")
print(df.head())

df.fillna(0, inplace=True)

df["Revenue"] = df["Quantity"] * df["Price"]

total_revenue = np.sum(df["Revenue"])
print("Total Revenue:", total_revenue)

top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print(top_products)

df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month

monthly_sales = df.groupby("Month")["Revenue"].sum()
print(monthly_sales)