import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Setup Sample Data (Replace this with your actual dataset)
np.random.seed(42)
dates = pd.date_range(start="2026-01-01", end="2026-12-31", freq="D")
sales_values = (
    np.random.randint(150, 600, size=len(dates))
    + np.sin(np.linspace(0, 12, len(dates))) * 80
)
categories = np.random.choice(
    ["Electronics", "Clothing", "Home Decor", "Books"], size=len(dates)
)

df = pd.DataFrame({"Date": dates, "Sales": sales_values, "Category": categories})

# Prepare monthly aggregations for line chart
df["Month"] = df["Date"].dt.strftime("%b")
monthly_sales = (
    df.groupby("Month")["Sales"].sum().reindex(df["Date"].dt.strftime("%b").unique())
)

# Prepare categorical data for bar/pie charts
category_sales = df.groupby("Category")["Sales"].sum().reset_index()

# 2. Plot 1: Line Chart (Sales Over Time)
plt.figure(figsize=(10, 5))
plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o",
    color="#1f77b4",
    linewidth=2,
    label="Monthly Sales",
)
plt.title("Sales Trends Over Time", fontsize=14, pad=15)
plt.xlabel("Month (2026)", fontsize=11)
plt.ylabel("Total Sales ($)", fontsize=11)
plt.grid(True, linestyle="--", alpha=0.5)
plt.legend(loc="upper left")
plt.tight_layout()
plt.savefig("project1_time_series.png", dpi=300)
plt.show()

# 3. Plot 2: Category Comparisons (Bar & Pie Chart side-by-side)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Bar Chart
sns.barplot(
    x="Category",
    y="Sales",
    data=category_sales,
    ax=axes[0],
    palette="viridis",
    hue="Category",
    legend=False,
)
axes[0].set_title("Sales Distribution by Category", fontsize=13, pad=10)
axes[0].set_xlabel("Product Category", fontsize=11)
axes[0].set_ylabel("Total Sales ($)", fontsize=11)
axes[0].grid(axis="y", linestyle="--", alpha=0.5)

# Pie Chart
axes[1].pie(
    category_sales["Sales"],
    labels=category_sales["Category"],
    autopct="%1.1f%%",
    startangle=140,
    colors=sns.color_palette("viridis", len(category_sales)),
)
axes[1].set_title("Market Share Percentage", fontsize=13, pad=10)

plt.tight_layout()
plt.savefig("project1_category_charts.png", dpi=300)
plt.show()

# 4. Short Summary Output
print("--- Project 1 Brief Summary ---")
print("Line, Bar, and Pie charts successfully exported to your directory.")
print(
    f"Highest performing category this period: {category_sales.loc[category_sales['Sales'].idxmax(), 'Category']}"
)