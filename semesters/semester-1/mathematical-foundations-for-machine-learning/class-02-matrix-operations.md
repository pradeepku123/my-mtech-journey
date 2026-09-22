---
class: 2
topic: "Matrix Operations & Linear Transformations"
subject: "Mathematical Foundations for AI"
semester: 1
folder: "mathematical-foundations-for-ai"
date: 2026-09-22
time: "08:42 IST"
duration_mins: 45
professor_persona: "Prof. Gilbert Strang (MIT 18.06)"
status: "Completed"
---

# 📚 MATHEMATICAL FOUNDATIONS FOR AI
## Class 02: Matrix Operations & Linear Transformations

> **Professor Persona**: Prof. Gilbert Strang (MIT 18.06) — *"A matrix is not just a spreadsheet of numbers. A matrix is a dynamic transformation — a machine that takes in vectors and stretches, rotates, or projects them into a new space!"*

---

## 🗺️ Phase 1: Context (Why This Matters)

### 📌 Curriculum Map
- **Module 1**: Linear Algebra Core (Classes 1–6)
  - Class 01: Vectors & Vector Spaces ✅
  - 🎯 **Class 02: Matrix Operations & Linear Transformations** ← *YOU ARE HERE*
  - Class 03: Systems of Linear Equations & Gaussian Elimination
  - Class 04: Vector Subspaces, Basis, Dimension & Rank
  - Class 05: Eigenvalues & Eigenvectors
  - Class 06: Singular Value Decomposition (SVD) & PCA

### 💡 Why AI/ML Cares
Matrices are the engine of modern Artificial Intelligence:
- **Neural Network Layers**: Every dense layer computes $\mathbf{y} = \sigma(W \mathbf{x} + \mathbf{b})$, where weight matrix $W \in \mathbb{R}^{m \times n}$ projects an $n$-dimensional input feature space to an $m$-dimensional hidden feature space.
- **Transformer Self-Attention**: Multiplies token embedding matrices $X$ by Query, Key, and Value weight matrices: $Q = X W_Q, K = X W_K, V = X W_V$.
- **Image Processing / Computer Vision**: Filters (convolutions), scaling, rotation, and affine transformations are matrix operations.

### 🔗 QA/SDET Analogy: Data Pipeline Middleware & Chain of Transformations
In automated testing or API workflows, think of a matrix as a **data transformation pipeline step**. Passing a payload vector $\mathbf{x}$ through middleware functions $f_1, f_2, f_3$ is analogous to matrix composition $A_3 A_2 A_1 \mathbf{x}$. Because matrix multiplication is associative, you can pre-compile the entire pipeline into a single transformation matrix $M = A_3 A_2 A_1$ and execute $M \mathbf{x}$ in one single high-throughput pass.

---

## 📖 Phase 2: Learn (Core Concept & Theory)

### 1. Dual View of a Matrix
1. **Data View (Spreadsheet)**: An $m \times n$ rectangular array of numbers with $m$ rows and $n$ columns.
2. **Operator View (Function)**: A linear mapping $T: \mathbb{R}^n \to \mathbb{R}^m$ that accepts a vector $\mathbf{x} \in \mathbb{R}^n$ and outputs $T(\mathbf{x}) = A \mathbf{x} \in \mathbb{R}^m$.

### 2. Fundamental Matrix Operations

#### A. Addition & Scalar Multiplication
- **Addition**: $C = A + B \implies C_{ij} = A_{ij} + B_{ij}$ (Requires identical dimensions $m \times n$).
- **Scalar Mult**: $C = c A \implies C_{ij} = c \cdot A_{ij}$.

#### B. Transpose
Flips a matrix over its diagonal: $(A^T)_{ij} = A_{ji}$.
If $A$ is $m \times n$, then $A^T$ is $n \times m$.

**Key Properties**:
1. $(A^T)^T = A$
2. $(A + B)^T = A^T + B^T$
3. $(c A)^T = c A^T$
4. **Symmetric Matrix**: $A = A^T$ (Always square, crucial in covariance matrices).
5. **Reversal Rule for Multiplication Transpose**:
   $$(A B)^T = B^T A^T$$

#### C. Matrix Multiplication (The Linear Combination View)
For $A \in \mathbb{R}^{m \times k}$ and $B \in \mathbb{R}^{k \times n}$, the product $C = A B \in \mathbb{R}^{m \times n}$ has entries:
$$C_{ij} = \sum_{l=1}^k A_{il} B_{lj}$$

> 💡 **Gilbert Strang's Column View of Matrix-Vector Multiplication**:  
> $A \mathbf{x}$ is a **linear combination of the columns of $A$** weighted by the components of $\mathbf{x}$:
> $$A \mathbf{x} = x_1 \mathbf{a}_1 + x_2 \mathbf{a}_2 + \dots + x_n \mathbf{a}_n$$

**Multiplication Properties**:
- Associative: $A(BC) = (AB)C$
- Distributive: $A(B + C) = AB + AC$
- ⚠️ **NON-COMMUTATIVE**: Generally, $A B \neq B A$! Order matters!

---

### 3. Linear Transformations: Geometry in Action
A transformation $T: \mathbb{R}^n \to \mathbb{R}^m$ is **linear** if for all vectors $\mathbf{u}, \mathbf{v}$ and scalar $c$:
1. $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$ (Preserves addition)
2. $T(c \mathbf{u}) = c T(\mathbf{u})$ (Preserves scalar multiplication)

**Crucial Geometric Insight**:  
Under a linear transformation, **grid lines remain parallel and evenly spaced**, and the **origin $[0,0]^T$ stays fixed at $[0,0]^T$**.

#### Basis Tracking Method
To determine the matrix $A$ for any 2D linear transformation, simply track where the standard basis vectors land!
- $\mathbf{e}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix} \xrightarrow{T} \begin{bmatrix} a \\ c \end{bmatrix}$
- $\mathbf{e}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix} \xrightarrow{T} \begin{bmatrix} b \\ d \end{bmatrix}$

The transformation matrix is simply formed by putting those transformed basis vectors in columns:
$$A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$$

---

## 💻 Phase 3: Apply (Implementation & Code)

### Python Implementation: Matrix Multiplication & Linear Transformation Visualization

```python
import numpy as np

# 1. Matrix Multiplication from Scratch
def matrix_multiply_scratch(A: list[list[float]], B: list[list[float]]) -> list[list[float]]:
    m, k_A = len(A), len(A[0])
    k_B, n = len(B), len(B[0])
    assert k_A == k_B, f"Inner dimensions must match! Got {k_A} and {k_B}"

    C = [[0.0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            for l in range(k_A):
                C[i][j] += A[i][l] * B[l][j]
    return C

def transpose_scratch(A: list[list[float]]) -> list[list[float]]:
    m, n = len(A), len(A[0])
    return [[A[i][j] for i in range(m)] for j in range(n)]

# Test Matrices
A = [[1.0, 2.0], [3.0, 4.0]]  # 2x2
B = [[5.0, 6.0], [7.0, 8.0]]  # 2x2

print("Scratch AB:", matrix_multiply_scratch(A, B))
print("Scratch A^T:", transpose_scratch(A))

# 2. NumPy Verification & 2D Rotation Transformation
A_np = np.array(A)
B_np = np.array(B)

print("\n--- NumPy Verification ---")
print("NumPy AB:\n", np.matmul(A_np, B_np))
print("NumPy A^T:\n", A_np.T)

# 3. Geometric 90-degree Counter-Clockwise Rotation Matrix
# e1 [1,0]^T -> [0,1]^T ; e2 [0,1]^T -> [-1,0]^T
theta = np.pi / 2  # 90 degrees
R_90 = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

v = np.array([3.0, 2.0])
v_rotated = R_90 @ v
print("\n--- 2D Rotation (90 deg CCW) ---")
print(f"Original vector: {v}")
print(f"Rotated vector: {np.round(v_rotated, 2)}")
```

---

## 📝 Phase 4: Synthesize (Summary & Key Takeaways)

### Concept Matrix
| Operation / Concept | Algebraic Formula | Geometric Intuition | Neural Network Connection |
|---------------------|-------------------|----------------------|---------------------------|
| **Matrix-Vector Mult** | $\mathbf{y} = A \mathbf{x}$ | Linear combination of columns of $A$ | Single linear layer forward pass |
| **Matrix Multiplication** | $C = A B$ | Composition of transformations $T_B$ then $T_A$ | Stacking layer weights $W_2 W_1$ |
| **Transpose** | $(A^T)_{ij} = A_{ji}$ | Flipping grid across main diagonal | Weight transpose in backpropagation ($W^T \delta$) |
| **Rotation Matrix** | $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ | Rigid rotation of space by angle $\theta$ | Coordinate transformation / Embeddings |

### 🎴 Flashcards for Revision
1. **Q**: Why is matrix multiplication generally non-commutative ($A B \neq B A$)?  
   **A**: Because applying transformation $B$ then $A$ gives a different geometric result than applying $A$ then $B$ (e.g., rotating then shearing vs shearing then rotating).
2. **Q**: What is the column view of $A \mathbf{x}$?  
   **A**: $A \mathbf{x}$ is a linear combination of the column vectors of $A$, scaled by the elements of $\mathbf{x}$.
3. **Q**: What is $(A B)^T$?  
   **A**: $B^T A^T$ (Note the order of matrices is reversed!).

---

## 🎯 Phase 5: Score (Checkpoints & Self-Assessment)

### ❓ Checkpoint Questions
1. **Q1**: Compute $A B$ and $B A$ for $A = \begin{bmatrix} 1 & 2 \\ 0 & 1 \end{bmatrix}$ and $B = \begin{bmatrix} 2 & 0 \\ 1 & 3 \end{bmatrix}$. Are they equal?
2. **Q2**: If matrix $A$ has shape $3 \times 5$ and matrix $B$ has shape $5 \times 2$, what is the shape of $A B$? Can you compute $B A$?
3. **Q3**: What $2 \times 2$ matrix reflects vectors across the x-axis? *(Hint: Track where $\mathbf{e}_1 = [1,0]^T$ and $\mathbf{e}_2 = [0,1]^T$ go!)*

---

## 📚 Recommended Resources & Links
- 📖 **Textbook**: *Mathematics for Machine Learning* — Section 2.2 & 2.3 (Matrix Operations & Linear Mappings)
- 🎬 **YouTube**: 3Blue1Brown — *Linear transformations and matrices | Essence of linear algebra, Ch 3*
- 🎬 **YouTube**: 3Blue1Brown — *Matrix multiplication as composition | Essence of linear algebra, Ch 4*
- 🎬 **MIT OCW**: Prof. Gilbert Strang, MIT 18.06 Lecture 3 — *Multiplication and Inverse Matrices*
