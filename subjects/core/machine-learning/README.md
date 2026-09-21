# 🤖 Machine Learning

> **Reference**: Andrew Ng's ML Specialization + CS229 Notes  
> **Tools**: Python, NumPy, Scikit-learn, Matplotlib

---

## 📋 Syllabus Coverage

### Supervised Learning
- [ ] Linear Regression (OLS, Gradient Descent)
- [ ] Logistic Regression (Binary, Multiclass)
- [ ] Decision Trees (CART, ID3)
- [ ] Random Forests & Bagging
- [ ] Gradient Boosting (XGBoost, LightGBM)
- [ ] Support Vector Machines (SVM)
- [ ] k-Nearest Neighbors (kNN)
- [ ] Naive Bayes

### Unsupervised Learning
- [ ] K-Means Clustering
- [ ] Hierarchical Clustering
- [ ] DBSCAN
- [ ] Principal Component Analysis (PCA)
- [ ] t-SNE & UMAP (dimensionality reduction)
- [ ] Autoencoders

### Model Evaluation & Selection
- [ ] Train/Validation/Test split
- [ ] Cross-validation (k-fold, LOOCV)
- [ ] Bias-Variance Tradeoff
- [ ] Metrics: Accuracy, Precision, Recall, F1, AUC-ROC
- [ ] Confusion Matrix
- [ ] Hyperparameter Tuning (Grid Search, Random Search, Bayesian)

### Regularization
- [ ] L1 (Lasso) — feature selection
- [ ] L2 (Ridge) — weight decay
- [ ] ElasticNet
- [ ] Dropout (for neural networks)

---

## 📝 My Notes

*Create topic-specific files here:*
- `week-01-linear-regression.md`
- `week-02-logistic-regression.md`
- `week-03-decision-trees.md`

---

## 💻 Key Code Templates

```python
# Standard ML pipeline skeleton
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Build pipeline (prevents data leakage!)
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', YourModel())
])

# Train & evaluate
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))
```

---

## 🔗 Key Resources
- [CS229 Lecture Notes (Stanford)](https://cs229.stanford.edu/notes2022fall/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)
- [Andrew Ng ML YouTube](https://www.youtube.com/playlist?list=PLkDaE6sCZn6FNC6YRfRQc_FbeQrF8BwGI)
