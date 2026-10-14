import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1. Setup Sample Data (Replace this with your actual dataset)
np.random.seed(42)
n_samples = 400

# Create correlated numeric features
marketing_spend = np.random.uniform(1000, 5000, n_samples)
conversions = (marketing_spend * 0.05) + np.random.normal(20, 15, n_samples)
revenue = (conversions * 12) + np.random.normal(50, 40, n_samples)
bounce_rate = 80 - (conversions * 0.2) + np.random.normal(0, 5, n_samples)

df = pd.DataFrame(
    {
        "Marketing_Spend": marketing_spend,
        "Conversions": conversions,
        "Revenue": revenue,
        "Bounce_Rate": bounce_rate,
        "Traffic_Source": np.random.choice(["Organic", "Paid"], size=n_samples),
    }
)

# 2. Compute Pearson Correlations
numeric_cols = ["Marketing_Spend", "Conversions", "Revenue", "Bounce_Rate"]
corr_matrix = df[numeric_cols].corr(method="pearson")

# 3. Plot 1: Heatmap (Masking the upper triangle)
mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

plt.figure(figsize=(8, 6))
sns.heatmap(
    corr_matrix,
    mask=mask,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1,
    square=True,
    linewidths=1,
    cbar_kws={"shrink": 0.7},
)
plt.title("Correlation Heatmap Matrix", fontsize=14, pad=20)
plt.tight_layout()
plt.savefig("project3_heatmap.png", dpi=300)
plt.show()

# 4. Plot 2: Pairplots / Scatter Matrix
pair_plot = sns.pairplot(
    df, vars=numeric_cols, hue="Traffic_Source", palette="deep", diag_kind="kde"
)
pair_plot.fig.suptitle(
    "Pairwise Scatter Matrix View", y=1.02, fontsize=14, weight="medium"
)
pair_plot.savefig("project3_pairplot.png", dpi=300)
plt.show()

# 5. Summary Text
print("--- Project 3 Summary Output ---")
print("Matrix analysis complete. Strongest relationship paths visualised.")