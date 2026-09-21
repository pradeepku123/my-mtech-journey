# 📐 Mathematics for Machine Learning

> **Reference Book**: [Mathematics for ML (free)](https://mml-book.github.io/)  
> **NPTEL**: [IIT Bombay Math for ML](https://nptel.ac.in/)

---

## 📋 Syllabus Coverage

### Chapter 1 — Linear Algebra
- [ ] Vectors & Vector Spaces
- [ ] Matrix operations (add, multiply, transpose)
- [ ] Determinants & Inverse
- [ ] Systems of linear equations
- [ ] Eigenvalues & Eigenvectors
- [ ] Matrix decompositions (LU, QR, SVD)
- [ ] PCA (Principal Component Analysis)

### Chapter 2 — Analytic Geometry
- [ ] Norms & Inner Products
- [ ] Distances & Angles
- [ ] Projections
- [ ] Orthogonality

### Chapter 3 — Matrix Decompositions
- [ ] Determinant and Trace
- [ ] Eigenvalues and Eigenvectors
- [ ] Cholesky Decomposition
- [ ] SVD — Singular Value Decomposition
- [ ] Matrix Approximation

### Chapter 4 — Probability & Statistics
- [ ] Sample Space & Probability
- [ ] Discrete & Continuous Distributions
- [ ] Sum Rules, Product Rules, Bayes Theorem
- [ ] Conjugacy & Exponential Family
- [ ] Change of Variables
- [ ] Maximum Likelihood Estimation (MLE)
- [ ] Maximum A Posteriori (MAP)

### Chapter 5 — Optimization
- [ ] Gradient Descent
- [ ] Convex Optimization
- [ ] Constrained Optimization (Lagrange)
- [ ] Stochastic Gradient Descent

---

## 📝 My Notes

*Add weekly notes here or create separate files per topic:*
- `week-01-linear-algebra-basics.md`
- `week-02-matrix-decompositions.md`
- `week-03-probability-stats.md`

---

## 💻 Code Practice

```python
import numpy as np

# Example: Eigenvalue decomposition
A = np.array([[3, 1], [1, 3]])
eigenvalues, eigenvectors = np.linalg.eig(A)
print(f"Eigenvalues: {eigenvalues}")
print(f"Eigenvectors:\n{eigenvectors}")
```

---

## 🔗 Key Resources
- [3Blue1Brown Linear Algebra series](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [StatQuest Statistics](https://www.youtube.com/@statquest)
- [Khan Academy Calculus](https://www.khanacademy.org/math/calculus-1)
