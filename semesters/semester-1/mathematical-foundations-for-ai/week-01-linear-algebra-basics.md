# 🧠 Vectors (The Building Blocks of ML)

*Date: 2026-09-21*

## 🔗 Analogy (SDET World → ML World)
Think of a Vector as a **single row in your test data spreadsheet**. 
If you are testing a user login feature, one test case might have: `[Age: 30, Income: 50000, FraudScore: 0.8]`. 
In ML, we don't call this a "test case row" or a "data record" — we call it a **3-dimensional vector**. It's just a list of numbers that represents one distinct object or event.

## 📌 What It Is
A vector is an ordered list of numbers. In geometry, it represents a point in space (with a magnitude/length and a direction). In computer science and ML, it represents the features (attributes) of a single data point.

## 💻 Code First
You already use vectors every time you write Python. Here is how they look in `numpy`, which is the industry standard for ML math:

```python
import numpy as np

# A 3-dimensional vector (like one test case with 3 attributes)
v = np.array([30, 50000, 0.8])
u = np.array([25, 45000, 0.2])

# 1. Vector Addition (Adding two test cases together)
# Result: [55, 95000, 1.0]
print("Addition:", v + u) 

# 2. Scalar Multiplication (Scaling up the test case by 10x)
# Result: [300, 500000, 8.0]
print("Scaling:", 10 * v)

# 3. Dot Product (A measure of similarity between two test cases)
# It multiplies corresponding elements and sums them up
# (30*25) + (50000*45000) + (0.8*0.2)
print("Dot Product:", np.dot(v, u))
```

## 📐 The Math
- **Notation:** Vectors are usually written as bold lowercase letters like **v** or **x**. 
- **Dimensionality:** A vector with $n$ elements belongs to $\mathbb{R}^n$ (an $n$-dimensional real number space). So our `[30, 50000, 0.8]` vector belongs to $\mathbb{R}^3$.
- **Magnitude (Length):** Calculated using the Pythagorean theorem extended to $n$ dimensions. Denoted as $||v||$.
  $$||v|| = \sqrt{v_1^2 + v_2^2 + \dots + v_n^2}$$

## 🎯 When to Use It
- **Use when:** You need to feed data into *any* machine learning model. Images, text, and user clicks are all converted into vectors before a neural network can process them.
- **Why it matters:** Because once your data is a vector, you can use high-speed GPU math (like the dot product) to compare millions of them instantly, instead of writing slow `for` loops.

## 📝 Exam Angle
- **Likely question:** "Given vector *u* and *v*, calculate the dot product and the magnitude of *u*."
- **Key points to mention:** Always mention that vectors have both *magnitude* and *direction* when asked for a geometric definition.
- **Common mistake:** Forgetting that vector addition is done element-wise. You can only add two vectors if they have the *exact same number of dimensions* (you can't add a 2D vector to a 3D vector).
