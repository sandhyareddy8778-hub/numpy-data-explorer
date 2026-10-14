import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Setup Sample Data (Replace this with your actual dataset)
np.random.seed(42)
records = 500
region_a = np.random.normal(loc=300, scale=75, size=records // 2)
region_b = np.random.normal(loc=350, scale=110, size=records // 2)

# Introduce synthetic extreme outliers to test tracking
region_a[np.random.choice(len(region_a), 5, replace=False)] *= 2.5
region_b[np.random.choice(len(region_b), 5, replace=False)] *= 2.5

df_a = pd.DataFrame({"Sales": region_a, "Region": "Region A"})
df_b = pd.DataFrame({"Sales": region_b, "Region": "Region B"})
df = pd.concat([df_a, df_b], ignore_index=True)

# 2. Distribution Plotting (Histogram, KDE, and Boxplots)
fig, axes = plt.subplots(1, 2, figsize=(15, 6))

# Histogram & KDE (Overlay Distribution)
sns.histplot(
    data=df,
    x="Sales",
    hue="Region",
    kde=True,
    ax=axes[0],
    element="step",
    stat="density",
    common_norm=False,
    palette="Set2",
)
axes[0].set_title("Histogram & KDE Density Comparison", fontsize=13, pad=10)
axes[0].set_xlabel("Sales Values", fontsize=11)
axes[0].set_ylabel("Density", fontsize=11)

# Boxplot (To inspect skewness and detect outliers)
sns.boxplot(
    data=df, x="Region", y="Sales", ax=axes[1], palette="Set2", hue="Region"
)
axes[1].set_title("Boxplot Representation (Outlier Check)", fontsize=13, pad=10)
axes[1].set_xlabel("Region", fontsize=11)
axes[1].set_ylabel("Sales Values", fontsize=11)

plt.tight_layout()
plt.savefig("project2_statistical_analysis.png", dpi=300)
plt.show()

# 3. Descriptive Stats for the Short Paragraph Interpretation
print("--- Project 2 Distribution Insights ---")
for region in ["Region A", "Region B"]:
    reg_data = df[df["Region"] == region]["Sales"]
    print(f"\n[{region} Statistics]")
    print(f"  Skewness: {reg_data.skew():.2f}")
    print(f"  Mean Sales: {reg_data.mean():.2f}")
    print(f"  Median Sales: {reg_data.median():.2f}")