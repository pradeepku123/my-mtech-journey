---
name: quiz-generator
description: >
  Generates targeted quizzes, MCQs, flashcards, and practice problems from
  Pradeep's study notes, lecture content, or specified topics. Calibrated for
  MTech-level questions with exam-pattern awareness.
triggers:
  - "generate quiz"
  - "create quiz"
  - "test me on"
  - "make flashcards"
  - "practice questions"
  - "quiz me"
  - "MCQ"
---

# Quiz Generator Skill

## Purpose
Generate high-quality, MTech-level quizzes and practice problems from Pradeep's study material to reinforce retention and exam readiness.

## Quiz Types Supported

| Type | When to Use | Format |
|------|-------------|--------|
| **MCQ** | Exam prep, concept checks | 4 options, 1 correct |
| **True/False with justification** | Quick daily checks | Statement + explain why |
| **Fill in the blank** | Formula/definition memorization | Cloze deletion style |
| **Short answer** | Deep understanding | 2-3 sentence answers |
| **Code completion** | Programming assignments | Python code with blanks |
| **Flashcard** | Spaced repetition (Anki-ready) | Q: Front / A: Back |
| **Derivation** | Math-heavy subjects | Step-by-step proof |

## Generation Rules

### Bloom's Taxonomy Distribution
- 20% — **Remember** (definitions, formulas)
- 30% — **Understand** (explain in own words)
- 30% — **Apply** (solve problems, write code)
- 20% — **Analyze/Evaluate** (compare approaches, critique)

### Difficulty Calibration
```
Based on Pradeep's stated confidence (1-5):
1 (New topic)    → 80% easy, 20% medium
2 (Learning)     → 50% easy, 40% medium, 10% hard
3 (Familiar)     → 20% easy, 60% medium, 20% hard
4 (Comfortable)  → 10% easy, 40% medium, 50% hard
5 (Exam-ready)   → 0% easy, 30% medium, 70% hard
```

## Output Format

### MCQ Format
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Q[N]. [Question text]

(A) [Option A]
(B) [Option B]
(C) [Option C]  
(D) [Option D]

[Reveal Answer]
✅ Answer: [Letter] — [Option text]
💡 Explanation: [Why this is correct + why others are wrong]
📌 Related concept: [Link to topic in subjects/ folder]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Flashcard Format (Anki-Compatible)
```
FRONT: [Question / Term / Formula Name]
BACK:  [Answer / Definition / Full formula with explanation]
TAG:   [subject]::[topic]::[difficulty]
```

### Code Completion Format
```python
# Q: Complete the gradient descent implementation
def gradient_descent(X, y, learning_rate=0.01, epochs=1000):
    m, n = X.shape
    theta = np.zeros(n)
    
    for epoch in range(epochs):
        # [YOUR CODE: Compute predictions]
        predictions = ___________
        
        # [YOUR CODE: Compute error]  
        error = ___________
        
        # [YOUR CODE: Update theta]
        theta = ___________
    
    return theta

# Expected output: Converged theta values
```

## Subject-Specific Question Banks

### Mathematics for ML (Sample)
- Prove that matrix multiplication is associative
- What is the geometric interpretation of the dot product?
- When is a matrix invertible? State the conditions.
- Explain the difference between population and sample variance.

### Machine Learning (Sample)
- Explain the bias-variance tradeoff with a diagram
- When would you prefer SVM over Logistic Regression?
- What is the curse of dimensionality?
- How does the kernel trick work in SVMs?

### Deep Learning (Sample)
- Why do we use ReLU instead of sigmoid in hidden layers?
- Explain vanishing gradient problem and solutions
- What is the difference between CNN and RNN? When to use each?
- How does self-attention in Transformers work?

## Session Tracking
After each quiz session, output:
```
📊 QUIZ SESSION SUMMARY
Topics covered: [list]
Questions: [total] | Correct: [n] | Accuracy: [%]
Weak areas: [topics where < 60% correct]
Recommended next action: [study X before next quiz]
Save to: progress/weekly-review.md
```
