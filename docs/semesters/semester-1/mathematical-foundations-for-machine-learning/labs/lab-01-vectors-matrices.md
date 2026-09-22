# 🧪 Lab 01: Vectors & Matrices in Python

> **Goal**: Translate the mathematical theory of vectors and matrices into working, testable Python code.

As an automation engineer, you know that code is the ultimate source of truth. In this lab, we will implement the basic Linear Algebra concepts using `NumPy` and write basic assertions (tests) to validate our understanding.

## 🛠️ Setup

Create a new file called `lab01.py` in your local workspace. Ensure `numpy` is installed.

```bash
pip install numpy
```

## 📝 Exercise 1: Vectors

```python
import numpy as np

def test_vectors():
    # 1. Create two 3-dimensional vectors
    # Let's say v represents [Age, Income, CreditScore]
    v = np.array([30, 50000, 750])
    u = np.array([25, 45000, 700])
    
    # 2. Vector Addition
    w = v + u
    assert np.array_equal(w, np.array([55, 95000, 1450])), "Vector addition failed"
    
    # 3. Scalar Multiplication (Increase everything by 10%)
    v_scaled = v * 1.10
    
    # 4. Dot Product (The sum of the products of corresponding elements)
    dot_product = np.dot(v, u)
    assert dot_product == (30*25) + (50000*45000) + (750*700), "Dot product failed"
    
    print("✅ Vector tests passed!")

test_vectors()
```

## 📝 Exercise 2: Matrices

```python
def test_matrices():
    # 1. Create a 2x3 Matrix (2 rows, 3 columns)
    # Imagine this as a dataset of 2 users, each with 3 features
    A = np.array([
        [30, 50000, 750],  # User 1
        [25, 45000, 700]   # User 2
    ])
    
    assert A.shape == (2, 3), "Matrix should be 2x3"
    
    # 2. Matrix Transpose (Flip rows and columns)
    # Becomes a 3x2 Matrix
    A_T = A.T
    assert A_T.shape == (3, 2), "Transposed matrix should be 3x2"
    
    # 3. Matrix Multiplication (Dot Product of Matrices)
    # You can multiply a 2x3 matrix with a 3x2 matrix
    # The result will be a 2x2 matrix
    result = np.dot(A, A_T)
    # or using the newer @ operator: result = A @ A_T
    
    assert result.shape == (2, 2), "Multiplication result should be 2x2"
    
    print("✅ Matrix tests passed!")

test_matrices()
```

## 🚀 Assignment
1. Copy the code into `lab01.py` and run it.
2. Add a new function `test_matrix_incompatible_shapes()` that purposely tries to multiply a `2x3` matrix by another `2x3` matrix.
3. Catch the `ValueError` exception and print "Caught expected shape mismatch error!"
4. Commit your `lab01.py` to save your practical progress.
