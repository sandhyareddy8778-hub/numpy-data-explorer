import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("sales.csv")

# Display Dataset
print(df.head())

# Dataset Information
print(df.info())

# Check Missing Values
print(df.isnull().sum())

# Remove Duplicate Values
df = df.drop_duplicates()

# Total Revenue
total_revenue = df["Sales"].sum()
print("Total Revenue:", total_revenue)

# Average Sales
average_sales = df["Sales"].mean()
print("Average Sales:", average_sales)

# Top Selling Products
top_products = df.groupby("Product")["Sales"].sum().sort_values(
    ascending=False
).head(10)

print("Top Products:")
print(top_products)

# Region Wise Sales
region_sales = df.groupby("Region")["Sales"].sum()
print("Region Wise Sales:")
print(region_sales)

# Monthly Sales Analysis
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Month"] = df["Order Date"].dt.month

monthly_sales = df.groupby("Month")["Sales"].sum()

# Visualization 1
plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Sales Analysis")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.savefig("monthly_sales.png")
plt.show()

# Visualization 2
plt.figure(figsize=(10, 5))
top_products.plot(kind="bar", color="skyblue")
plt.title("Top Selling Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# Visualization 3
plt.figure(figsize=(8, 5))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Region Wise Sales")
plt.ylabel("")
plt.savefig("region_sales.png")
plt.show()

print("Sales Analysis Completed Successfully!")