# Semester 1 — Class-by-Class Curriculum

> Full teaching plan for all 5 Semester 1 subjects.
> Each subject has a complete class-by-class breakdown with topics, sub-topics, and goals.

---

## 📐 Subject 1: Mathematical Foundations for AI
**Folder**: `semesters/semester-1/mathematical-foundations-for-ai/`
**Total Classes**: 12 | **Difficulty**: High (foundation of everything)
**Professor Persona**: Prof. Gilbert Strang (MIT)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | Vectors & Vector Spaces | Vector definition, operations, span, basis, linear independence | Build geometric intuition for vectors |
| 02 | Matrix Operations | Addition, multiplication, transpose, trace, properties | Matrix as a transformation |
| 03 | Systems of Linear Equations | Gaussian elimination, row echelon, rank, null space | Solve Ax = b geometrically |
| 04 | Determinants & Inverses | 2x2/3x3 determinants, invertibility conditions, inverse formula | When does a matrix "undo" itself? |
| 05 | Eigenvalues & Eigenvectors | Definition, characteristic equation, diagonalization | The "special directions" of a matrix |
| 06 | Matrix Decompositions I — LU, QR | LU factorization, QR decomposition, applications | Decompose → Solve → Reconstruct |
| 07 | Matrix Decompositions II — SVD | SVD definition, geometric interpretation, rank-k approximation | The most important decomposition in ML |
| 08 | PCA — Principal Component Analysis | Covariance matrix, eigenvectors as PCs, dimensionality reduction | Compress data while preserving variance |
| 09 | Probability Foundations | Sample space, events, axioms, conditional probability, Bayes | From uncertainty to math |
| 10 | Probability Distributions | Bernoulli, Binomial, Gaussian, Poisson, Exponential | The "models" of randomness |
| 11 | MLE & MAP Estimation | Likelihood, log-likelihood, Maximum A Posteriori, priors | Learning from data mathematically |
| 12 | Optimization Foundations | Gradient, partial derivatives, gradient descent, convexity, Lagrange | How ML models learn |

---

## 🤖 Subject 2: Applied Machine Learning
**Folder**: `semesters/semester-1/applied-machine-learning/`
**Total Classes**: 12 | **Difficulty**: Medium-High
**Professor Persona**: Prof. Andrew Ng

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | ML Landscape & Problem Types | Supervised/Unsupervised/RL taxonomy, data types, problem framing | Frame any real problem as an ML problem |
| 02 | Linear Regression | Hypothesis, cost function, gradient descent, normal equation | The "Hello World" of ML |
| 03 | Logistic Regression & Classification | Sigmoid, decision boundary, cross-entropy loss, softmax | Binary and multi-class classification |
| 04 | Bias-Variance Tradeoff | Underfitting/overfitting, learning curves, model complexity | Diagnose model performance |
| 05 | Regularization | L1 (Lasso), L2 (Ridge), ElasticNet, dropout intuition | Control overfitting systematically |
| 06 | Feature Engineering | Encoding, scaling, imputation, polynomial features, selection | Garbage in → Garbage out |
| 07 | Decision Trees & Random Forests | Gini/entropy, splitting, pruning, bagging, feature importance | Tree-based ensemble power |
| 08 | Support Vector Machines | Maximal margin, soft margin, kernel trick (RBF, poly) | "Find the best boundary" |
| 09 | Naive Bayes & k-NN | Probabilistic classifiers, lazy learning, distance metrics | Simple but powerful baselines |
| 10 | Unsupervised: Clustering | k-Means, DBSCAN, hierarchical clustering, elbow method | Find hidden structure in data |
| 11 | Model Evaluation & Selection | Confusion matrix, ROC-AUC, F1, cross-validation, grid search | How to trust your model |
| 12 | ML Pipeline: End-to-End Project | Data ingestion → preprocessing → training → evaluation → serving | Put it all together |

---

## 🌳 Subject 3: Advanced Data Structures
**Folder**: `semesters/semester-1/advanced-data-structures/`
**Total Classes**: 10 | **Difficulty**: Medium
**Professor Persona**: Prof. Tim Roughgarden (Stanford)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | Complexity Review & Recurrences | Big-O, Big-Ω, Master Theorem, recurrence trees | Analyze algorithm efficiency |
| 02 | Advanced Trees: AVL & Red-Black | Rotations, balance factor, insertion/deletion, properties | Self-balancing binary search |
| 03 | Heaps & Priority Queues | Min/max heap, heapify, heap sort, applications | O(log n) priority management |
| 04 | Hash Tables Deep Dive | Hash functions, collision: chaining vs open addressing, load factor | O(1) average lookup |
| 05 | Graphs: Representation & Traversal | Adjacency matrix/list, BFS, DFS, topological sort | Model connected data |
| 06 | Shortest Paths | Dijkstra, Bellman-Ford, Floyd-Warshall, A* | Optimize network routing |
| 07 | Spanning Trees & Greedy | Kruskal, Prim, Union-Find (disjoint sets) | Minimum cost connectivity |
| 08 | Tries & Suffix Structures | Trie, compressed trie, suffix array, applications in NLP | Fast text search and indexing |
| 09 | Segment Trees & Fenwick Trees | Range queries, lazy propagation, BIT for prefix sums | Efficient range operations |
| 10 | Dynamic Programming Patterns | Memoization, tabulation, LCS, knapsack, DP on graphs | Optimize with subproblem reuse |

---

## 📊 Subject 4: Computational Optimization
**Folder**: `semesters/semester-1/computational-optimization/`
**Total Classes**: 10 | **Difficulty**: High
**Professor Persona**: Prof. Stephen Boyd (Stanford)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | Optimization Landscape | Convex vs non-convex, local vs global minima, optimization problem types | See optimization in ML clearly |
| 02 | Convex Sets & Functions | Convex sets, convex functions, Jensen's inequality, epigraph | Foundation of tractable optimization |
| 03 | Gradient Descent | Batch GD, step size, convergence, geometric interpretation | The engine of ML training |
| 04 | SGD & Variants | Mini-batch SGD, momentum, RMSProp, Adam, AdaGrad | Modern deep learning optimizers |
| 05 | Constrained Optimization | Equality/inequality constraints, feasible set, KKT conditions | Optimize with constraints |
| 06 | Lagrangian & Duality | Lagrange multipliers, dual problem, strong/weak duality | Elegant reformulation of constraints |
| 07 | Linear Programming | LP formulation, simplex method, interior point methods | Optimize linear objectives |
| 08 | Quadratic Programming | QP formulation, active set method, link to SVMs | Non-linear but tractable |
| 09 | Second-Order Methods | Newton's method, quasi-Newton (L-BFGS), Hessian approximation | Faster convergence than GD |
| 10 | Stochastic & Distributed Opt. | Variance reduction (SVRG), federated learning optimization | Scale to massive ML workloads |

---

## 🐍 Subject 5: Programming for Big Data
**Folder**: `semesters/semester-1/programming-for-big-data/`
**Total Classes**: 10 | **Difficulty**: Medium (great for Pradeep's coding background)
**Professor Persona**: Prof. Matei Zaharia (Apache Spark creator)

### Class Breakdown

| Class | Topic | Sub-Topics | Key Goal |
|-------|-------|------------|----------|
| 01 | Big Data Ecosystem | Hadoop, HDFS, MapReduce concept, Spark vs Hadoop, data velocity/volume/variety | Orient in the big data landscape |
| 02 | Apache Spark Fundamentals | RDD, DAG, lazy evaluation, actions vs transformations, Spark context | The programming model |
| 03 | Spark DataFrames & SQL | DataFrame API, SparkSQL, schema inference, catalyst optimizer | SQL-style big data processing |
| 04 | Data Ingestion & Storage | Parquet, Avro, ORC, Delta Lake, S3/HDFS, partitioning strategies | Store data for fast ML training |
| 05 | Streaming Data | Spark Streaming, Kafka integration, DStream, structured streaming | Real-time ML data pipelines |
| 06 | Machine Learning with Spark MLlib | MLlib pipelines, feature transformers, model training at scale | Train ML on billions of rows |
| 07 | Data Wrangling at Scale | Complex joins, window functions, null handling, skew handling | Production data quality |
| 08 | AWS for Big Data | EMR, Glue, Athena, Kinesis, Redshift — Pradeep's AWS knowledge bridge | Cloud-native big data |
| 09 | Performance Tuning | Partitioning, caching, broadcast joins, memory management, GC tuning | Make Spark pipelines fast |
| 10 | End-to-End Pipeline Project | Data lake → Spark ETL → MLlib model → S3 serving → monitoring | Full production pipeline |
