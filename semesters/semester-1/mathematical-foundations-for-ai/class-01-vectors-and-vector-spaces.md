---
class: 1
topic: "Vectors & Vector Spaces"
subject: "Mathematical Foundations for AI"
semester: 1
folder: "mathematical-foundations-for-ai"
date: 2026-09-22
time: "08:26 IST"
duration_mins: 45
professor_persona: "Prof. Gilbert Strang (MIT 18.06)"
status: "Completed"
---

# 📚 MATHEMATICAL FOUNDATIONS FOR AI
## Class 01: Vectors & Vector Spaces

> **Professor Persona**: Prof. Gilbert Strang (MIT 18.06) — *"Linear algebra is not about formulas; it is about geometry coming alive in arbitrary dimensions."*

---

## 🗺️ Phase 1: Context (Why This Matters)

### 📌 Curriculum Map
- **Module 1**: Linear Algebra Core (Classes 1–6)
  - 🎯 **Class 01: Vectors & Vector Spaces** ← *YOU ARE HERE*
  - Class 02: Matrix Operations & Linear Transformations
  - Class 03: Systems of Linear Equations & Gaussian Elimination
  - Class 04: Vector Subspaces, Basis, Dimension & Rank
  - Class 05: Eigenvalues, Eigenvectors & Characteristic Equations
  - Class 06: Singular Value Decomposition (SVD) & PCA

### 💡 Why AI/ML Cares
In Machine Learning, **data is vectors**. 
- An image (28x28 pixels) is a vector in $\mathbb{R}^{784}$.
- A text token embedding (LLMs like LLaMA / GPT-4) is a vector in $\mathbb{R}^{4096}$ or $\mathbb{R}^{12288}$.
- A customer profile (age, income, click history) is a vector in $\mathbb{R}^{d}$.
Understanding vector spaces is the fundamental prerequisite to high-dimensional geometry, loss landscapes, and neural network representations.

### 🔗 QA/SDET Analogy: Test Parameterization & State Space
In test automation, a test suite configuration or test case parameter vector $\vec{x} = [\text{browser\_id}, \text{viewport\_width}, \text{timeout\_ms}]$ spans a configuration space. Linear independence means no test parameter can be derived or redundantly computed from another — every dimension adds unique value to your test coverage.

---

## 📖 Phase 2: Learn (Core Concept & Theory)

### 1. The 3 Views of a Vector
1. **Computer Science View**: An ordered array or tuple of numbers. Example: `[2.5, -1.0, 4.2]`.
2. **Physics View**: An arrow pointing in space with **magnitude** (length) and **direction**.
3. **Mathematician View**: An object that can be added to another vector and multiplied by a scalar, obeying specific vector space axioms.

### 2. Formal Definition of a Vector Space
A **Vector Space** $V$ over a field $F$ (usually real numbers $\mathbb{R}$) is a set of elements (vectors) equipped with two operations:
1. Vector Addition: $+ : V \times V \to V$
2. Scalar Multiplication: $\cdot : F \times V \to V$

Satisfying 8 fundamental axioms:
- **Closure**: $\mathbf{u} + \mathbf{v} \in V$ and $c \mathbf{u} \in V$
- **Commutativity**: $\mathbf{u} + \mathbf{v} = \mathbf{v} + \mathbf{u}$
- **Associativity**: $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$
- **Additive Identity**: $\mathbf{0} \in V$ such that $\mathbf{v} + \mathbf{0} = \mathbf{v}$
- **Additive Inverse**: $-\mathbf{v} \in V$ such that $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$
- **Distributivity**: $c(\mathbf{u} + \mathbf{v}) = c\mathbf{u} + c\mathbf{v}$ and $(c+d)\mathbf{v} = c\mathbf{v} + d\mathbf{v}$
- **Scalar Associativity**: $(cd)\mathbf{v} = c(d\mathbf{v})$
- **Scalar Identity**: $1 \cdot \mathbf{v} = \mathbf{v}$

### 3. Linear Combinations & Span
Given vectors $\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_k \in V$ and scalars $c_1, c_2, \dots, c_k \in \mathbb{R}$, a **linear combination** is:
$$\mathbf{w} = c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k$$

The **Span** of a set of vectors is the set of ALL possible linear combinations:
$$\text{Span}(\mathbf{v}_1, \dots, \mathbf{v}_k) = \{ c_1 \mathbf{v}_1 + \dots + c_k \mathbf{v}_k \mid c_i \in \mathbb{R} \}$$

### 4. Linear Independence & Basis
- **Linear Independence**: A set of vectors $\{\mathbf{v}_1, \dots, \mathbf{v}_k\}$ is linearly independent if the equation:
  $$c_1 \mathbf{v}_1 + c_2 \mathbf{v}_2 + \dots + c_k \mathbf{v}_k = \mathbf{0}$$
  has ONLY the trivial solution $c_1 = c_2 = \dots = c_k = 0$.
- **Basis**: A set of vectors $B = \{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ is a **basis** for vector space $V$ if:
  1. $B$ is linearly independent.
  2. $\text{Span}(B) = V$.
- **Dimension**: The number of vectors in a basis of $V$ is called $\dim(V)$.

---

## 💻 Phase 3: Apply (Implementation & Code)

### Python Implementation: Vector Operations from Scratch & NumPy Verification

```python
import numpy as np

# 1. Vector addition and scalar multiplication from scratch
def vector_add(u: list[float], v: list[float]) -> list[float]:
    assert len(u) == len(v), "Vectors must be of same dimension"
    return [u[i] + v[i] for i in range(len(u))]

def scalar_multiply(c: float, v: list[float]) -> list[float]:
    return [c * x for x in v]

def dot_product(u: list[float], v: list[float]) -> float:
    return sum(u[i] * v[i] for i in range(len(u)))

def vector_norm(v: list[float]) -> float:
    return dot_product(v, v) ** 0.5

# Test case
u = [2.0, 3.0, -1.0]
v = [1.0, -2.0, 4.0]

print("Scratch Add:", vector_add(u, v))
print("Scratch Scalar Mult (3*u):", scalar_multiply(3, u))
print("Scratch Dot Product:", dot_product(u, v))
print("Scratch Norm ||u||:", vector_norm(u))

# 2. Verification using NumPy
u_np = np.array([2.0, 3.0, -1.0])
v_np = np.array([1.0, -2.0, 4.0])

print("\n--- NumPy Verification ---")
print("NumPy Add:", u_np + v_np)
print("NumPy Dot:", np.dot(u_np, v_np))
print("NumPy Norm:", np.linalg.norm(u_np))
```

---

## 📝 Phase 4: Synthesize (Summary & Key Takeaways)

### Concept Matrix
| Concept | Geometric Meaning | Algebraic Condition | AI Relevance |
|---------|-------------------|----------------------|--------------|
| **Vector** | Directed line segment | Column array $\mathbf{x} \in \mathbb{R}^n$ | Feature representation |
| **Span** | Subspace reached by combinations | $\{ \sum c_i \mathbf{v}_i \}$ | Latent space of generative models |
| **Linear Independence** | No redundant directions | $\sum c_i \mathbf{v}_i = \mathbf{0} \implies c_i = 0$ | Preventing multi-collinearity / redundant features |
| **Basis** | Minimal non-redundant grid | Independent + Spanning set | Coordinate system / PCA axes |

### 🎴 Flashcards for Revision
1. **Q**: What is the formal test for linear independence?  
   **A**: Solve $\sum c_i \mathbf{v}_i = \mathbf{0}$. If the only solution is all $c_i = 0$, they are independent.
2. **Q**: What is the dimension of a vector space?  
   **A**: The number of vectors in any basis for that vector space.
3. **Q**: How does vector dot product relate to cosine similarity in NLP?  
   **A**: $\mathbf{u} \cdot \mathbf{v} = \|\mathbf{u}\| \|\mathbf{v}\| \cos(\theta)$. Cosine similarity isolates direction: $\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}$.

---

## 🎯 Phase 5: Score (Checkpoints & Self-Assessment)

### ❓ Checkpoint Questions
1. **Q1**: Are vectors $\mathbf{v}_1 = [1, 2, 3]^T$, $\mathbf{v}_2 = [2, 4, 6]^T$, $\mathbf{v}_3 = [1, 0, 1]^T$ linearly independent in $\mathbb{R}^3$? Why or why not?
2. **Q2**: Can 4 vectors in $\mathbb{R}^3$ be linearly independent? Explain geometrically and algebraically.
3. **Q3**: What is the span of the standard basis vectors $\mathbf{e}_1 = [1, 0]^T$ and $\mathbf{e}_2 = [0, 1]^T$ in $\mathbb{R}^2$?

---

## 📚 Recommended Resources & Links
- 📖 **Textbook**: *Mathematics for Machine Learning* by Deisenroth, Faisal, Ong — Chapter 2 (Linear Algebra)
- 🎬 **YouTube**: 3Blue1Brown — *Vectors, what even are they? | Essence of linear algebra, Ch 1*
- 🎬 **MIT OCW**: Prof. Gilbert Strang, MIT 18.06 Lecture 1 — *The Geometry of Linear Equations*
