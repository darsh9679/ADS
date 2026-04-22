import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, silhouette_score, ConfusionMatrixDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

# Data
X = np.array([[1], [2], [3], [10], [11], [12]])
y = [0, 0, 0, 1, 1, 1]

# Supervised - Logistic Regression
y_pred = LogisticRegression().fit(X, y).predict(X)
print("Supervised Report:\n", classification_report(y, y_pred))

# Unsupervised - KMeans
y_cluster = KMeans(n_clusters=2, n_init=10).fit_predict(X)
print("Silhouette Score:", silhouette_score(X, y_cluster))

# Plot Confusion Matrices
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
ConfusionMatrixDisplay.from_predictions(y, y_pred,    ax=axes[0], cmap="Blues").ax_.set_title("Supervised")
ConfusionMatrixDisplay.from_predictions(y, y_cluster, ax=axes[1], cmap="Greens").ax_.set_title("Unsupervised")

plt.tight_layout()
plt.show()
