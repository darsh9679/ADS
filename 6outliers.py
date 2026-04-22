import numpy as np
from sklearn.neighbors import LocalOutlierFactor


data = np.array([10, 12, 11, 13, 12, 11, 10, 80]).reshape(-1, 1)


# ── Distance-Based: Z-Score ───────────────────────────────
THRESHOLD = 2
z_scores  = (data - data.mean()) / data.std()
z_outliers = data[np.abs(z_scores) > THRESHOLD]

print(f"Z-Score outliers : {z_outliers.flatten()}")


# ── Density-Based: Local Outlier Factor ───────────────────
# label -1 = outlier, +1 = inlier
lof        = LocalOutlierFactor(n_neighbors=2)
labels     = lof.fit_predict(data)
lof_outliers = data[labels == -1]

print(f"LOF outliers     : {lof_outliers.flatten()}")