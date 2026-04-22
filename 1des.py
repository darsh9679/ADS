import pandas as pd
from scipy import stats

data = [10, 12, 12, 13, 15, 18, 20, 22, 25, 30]
series = pd.Series(data)

# ── Descriptive Statistics ────────────────────────────────
print("=== Descriptive Statistics ===")
print(series.describe())
print(f"Median : {series.median()}")
print(f"Mode   : {series.mode()[0]}")

# ── Inferential Statistics ────────────────────────────────
print("\n=== One-Sample T-Test (H₀: μ = 20) ===")

HYPOTHESIZED_MEAN = 20
t_stat, p_val = stats.ttest_1samp(data, HYPOTHESIZED_MEAN)

print(f"t-statistic : {t_stat:.4f}")
print(f"p-value     : {p_val:.4f}")
print(f"Result      : {'Significant' if p_val < 0.05 else 'Not Significant'}")

