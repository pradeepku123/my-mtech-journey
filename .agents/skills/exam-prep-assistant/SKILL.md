---
name: exam-prep-assistant
description: >
  Provides targeted, high-intensity exam preparation for Pradeep's MTech AI/ML 
  assessments. Creates study schedules, revision sheets, predicted questions,
  and last-minute strategies optimized for working professional constraints.
triggers:
  - "exam prep"
  - "exam is coming"
  - "prepare for exam"
  - "upcoming exam"
  - "revision"
  - "exam in X days"
  - "help me prepare"
  - "what to revise"
---

# Exam Prep Assistant Skill

## Purpose
Help Pradeep efficiently prepare for MTech exams with time-boxed, high-impact revision strategies that account for his limited time as a working professional.

## Exam Prep Kickoff

When invoked, gather:
1. **Subject/paper name**
2. **Exam date** (calculate days remaining)
3. **Exam type** (MCQ/theory/practical/open-book)
4. **Topics covered** in the syllabus
5. **Self-assessed weak areas** (1-5 scale per topic)
6. **Available prep time** (hours/day until exam)

## Countdown-Based Strategy

### 🟢 7+ Days Before Exam
Focus: Understanding & coverage
```
Day 1-2: Identify weak topics from marks tracker & daily logs
Day 3-4: Rapid revision of all topics (use concept-explainer skill)
Day 5-6: Solve past papers / practice problems
Day 7:   Full mock test + review mistakes
```

### 🟡 3-7 Days Before Exam
Focus: Consolidation & practice
```
Day 1: Create a "cheat sheet" of all formulas & key concepts
Day 2: Solve 50+ MCQs across all topics (use quiz-generator skill)
Day 3: Deep dive on top 3 weak topics
Day 4: Practice derivations + code implementations
Day 5: Mock exam under timed conditions
Day 6: Review mistakes only — don't start new topics
Day 7: Light revision of cheat sheet + rest
```

### 🔴 1-2 Days Before Exam
Focus: High-yield revision ONLY
```
Do:
✅ Review cheat sheet (formulas, definitions, algorithms)
✅ Re-read your own notes from subjects/
✅ Solve 10-15 MCQs on each topic for recall
✅ Sleep 7-8 hours

Don't:
❌ Start new topics
❌ Do complex derivations for the first time
❌ Pull an all-nighter (kills retention)
```

### ⏰ Exam Day
```
Morning: Light breakfast + review cheat sheet (30 min max)
Before exam: Deep breathe — your SDET systematic thinking is an advantage
During exam:
  → MCQ: Answer known → Skip hard → Come back
  → Theory: Structure answers with bullet points
  → Derivations: Write what you know, attempt all
```

## Subject-Specific Revision Sheets

### Mathematics for ML — High-Yield Topics
| Topic | Priority | Key Formulas |
|-------|----------|--------------|
| Linear Algebra | 🔴 Must know | Det, Eigenvalues, SVD, PCA |
| Probability & Statistics | 🔴 Must know | Bayes, MLE, Expectation, Variance |
| Calculus/Optimization | 🔴 Must know | Gradient, Chain rule, Convexity |
| Information Theory | 🟡 Important | Entropy, KL Divergence, Mutual Info |

### Machine Learning — High-Yield Topics
| Topic | Priority | Key Points |
|-------|----------|------------|
| Linear/Logistic Regression | 🔴 Must know | Loss functions, gradient descent |
| Decision Trees/RF/XGBoost | 🔴 Must know | Gini, entropy, ensemble methods |
| SVM | 🟡 Important | Kernel trick, margin, dual problem |
| Clustering (K-Means, DBSCAN) | 🟡 Important | Inertia, elbow method |
| Evaluation Metrics | 🔴 Must know | Accuracy, Precision, Recall, F1, AUC-ROC |
| Bias-Variance Tradeoff | 🔴 Must know | Overfitting, regularization |

### Deep Learning — High-Yield Topics
| Topic | Priority | Key Points |
|-------|----------|------------|
| Backpropagation | 🔴 Must know | Chain rule, computational graph |
| CNNs | 🔴 Must know | Conv, Pooling, Receptive field |
| RNN/LSTM | 🟡 Important | Vanishing gradient, gating |
| Transformers/Attention | 🔴 Must know | Self-attention, Q/K/V, BERT, GPT |
| Regularization | 🟡 Important | Dropout, Batch Norm, L1/L2 |
| Optimizers | 🟡 Important | SGD, Adam, RMSProp |

## Predicted Question Generator

Based on the subject and syllabus, generate:
1. **5 most likely theory questions** (with model answers)
2. **5 most likely numerical/derivation questions** (with step-by-step solutions)
3. **3 likely code-writing questions** (with working Python code)

Format each with: Question → Marks → Estimated time → Model answer

## Cheat Sheet Generator

Create a 1-2 page revision summary containing:
```
# [Subject] EXAM CHEAT SHEET
## Key Formulas
[All important formulas with variable definitions]

## Algorithm Steps
[Step-by-step algorithms for key methods]

## Common Exam Traps
[List of gotchas and common mistakes]

## Quick Decision Rules
[When to use X vs Y type questions]
```
Save to: `subjects/[subject]/cheatsheet-exam.md`

## Post-Exam Reflection
After the exam, capture:
```
📝 POST-EXAM LOG — [Subject] — [Date]
Topics that came (as expected): 
Topics that surprised me:
Questions I answered well:
Questions I struggled with:
What to improve for next time:
Estimated score: [range]
```
Update: `progress/marks-tracker.md`
