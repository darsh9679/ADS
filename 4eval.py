import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, silhouette_score
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans

# Data
X = np.array([[1], [2], [3], [10], [11], [12]])
y_true = [0, 0, 0, 1, 1, 1]

# --- 1. SUPERVISED (Logistic Regression) ---
clf = LogisticRegression()
clf.fit(X, y_true)
y_pred = clf.predict(X)

print("Supervised Report:\n", classification_report(y_true, y_pred))

# --- 2. UNSUPERVISED (KMeans) ---
kmeans = KMeans(n_clusters=2, n_init=10)
kmeans.fit(X)
y_cluster = kmeans.labels_

print("Unsupervised Silhouette Score:", silhouette_score(X, y_cluster))

# --- VISUALIZATION (Confusion Matrices) ---
fig, ax = plt.subplots(1, 2, figsize=(10, 4))

# Supervised Matrix
ConfusionMatrixDisplay.from_predictions(y_true, y_pred, ax=ax[0], cmap='Blues')
ax[0].set_title("Supervised Confusion Matrix")

# Unsupervised Matrix
ConfusionMatrixDisplay.from_predictions(y_true, y_cluster, ax=ax[1], cmap='Greens')
ax[1].set_title("Unsupervised (Cluster vs True)")

plt.tight_layout()
plt.show()