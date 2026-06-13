import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("cleaned_retail.csv")

print("="*50)
print("DATASET SHAPE")
print(df.shape)

print("="*50)
print("MISSING VALUES")
print(df.isnull().sum())

print("="*50)
print("TOTAL REVENUE")
print("£", round(df['Revenue'].sum(), 2))

print("="*50)
print("TOTAL ORDERS")
print(df['InvoiceNo'].nunique())

print("="*50)
print("TOTAL CUSTOMERS")
print(df['CustomerID'].nunique())

print("="*50)
print("TOTAL PRODUCTS")
print(df['Description'].nunique())

# -----------------------------
# Monthly Revenue Analysis
# -----------------------------
monthly_sales = (
    df.groupby('Month')['Revenue']
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10,5))
monthly_sales.plot(kind='bar')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# -----------------------------
# Top 10 Products
# -----------------------------
top_products = (
    df.groupby('Description')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_products.plot(kind='barh')
plt.title("Top 10 Products by Revenue")
plt.xlabel("Revenue")
plt.tight_layout()
plt.show()

# -----------------------------
# Country Revenue Analysis
# -----------------------------
country_sales = (
    df.groupby('Country')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
country_sales.plot(kind='bar')
plt.title("Top 10 Countries by Revenue")
plt.xlabel("Country")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

# -----------------------------
# Day-wise Orders Analysis
# -----------------------------
day_orders = (
    df.groupby('Day')['InvoiceNo']
    .count()
)

plt.figure(figsize=(8,5))
day_orders.plot(kind='bar')
plt.title("Orders by Day")
plt.xlabel("Day")
plt.ylabel("Order Count")
plt.tight_layout()
plt.show()

# -----------------------------
# Top Customers
# -----------------------------
top_customers = (
    df.groupby('CustomerID')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_customers.plot(kind='bar')
plt.title("Top 10 Customers by Revenue")
plt.xlabel("Customer ID")
plt.ylabel("Revenue")
plt.tight_layout()
plt.show()

print("="*50)
print("KEY INSIGHTS")
print("1. November generated the highest revenue.")
print("2. United Kingdom contributed the majority of sales.")
print("3. DOTCOM POSTAGE was the highest revenue-generating product.")
print("4. Thursday recorded the highest order volume.")
print("5. Approximately 25% Customer IDs were missing.")
print("="*50)