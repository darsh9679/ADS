from imblearn.over_sampling import SMOTE 
from collections import Counter 
from sklearn.datasets import make_classification 
# Generate Imbalanced Data 
X, y = make_classification(n_samples=1000, weights=[0.95], random_state=42) 
print("Before SMOTE:", str(dict(Counter(y)))[1:-1]) 
# Apply SMOTE 
X_res, y_res = SMOTE().fit_resample(X, y) 
# Check Balanced Data 
print("After SMOTE:", str(dict(Counter(y_res)))[1:-1]) 



