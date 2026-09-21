# 🎓 My MTech AI/ML Journey — Agentic Study Framework

> **Pradeep Kumar Behera** | Senior Automation Test Engineer (9+ years)  
> Specialization: Cypress · Playwright · WebdriverIO · Python · TypeScript · AWS  
> 🎯 Goal: MTech in **Artificial Intelligence & Machine Learning**

---

## 📖 What is This Repository?

This is a **personal, agentic, skill-based learning framework** designed specifically for working professionals pursuing higher education in AI/ML. Every folder, file, and script here serves a purpose — to make your daily study time productive, trackable, and AI-assisted.

The framework is built around **5 core pillars**:

| Pillar | Description |
|--------|-------------|
| 🤖 **Skills** | Modular agent skills for study assistance |
| 📅 **Daily Routine** | Structured daily study plan optimized for a working professional |
| 📚 **Subject Modules** | Organized course content per semester/topic |
| 📊 **Progress Tracker** | Self-assessment, marks tracking, and milestone reviews |
| 🛠️ **Automation Tools** | Scripts to auto-generate notes, flashcards, summaries |

---

## 🗂️ Repository Structure

```
my-mtech-journey/
│
├── README.md                        # ← You are here
│
├── .agents/                         # 🤖 Agentic Skills Framework
│   ├── AGENTS.md                    # Global rules for AI agent behavior
│   └── skills/
│       ├── daily-study-planner/     # Plan & schedule today's study session
│       ├── concept-explainer/       # Explain complex ML concepts simply
│       ├── quiz-generator/          # Generate quizzes from your notes
│       ├── code-tutor/              # Debug/review ML code & assignments
│       ├── research-paper-reader/   # Summarize & analyze research papers
│       ├── progress-reviewer/       # Weekly/monthly progress review
│       └── exam-prep-assistant/     # Targeted exam preparation help
│
├── daily-log/                       # 📅 Daily study logs (auto-generated)
│   ├── TEMPLATE.md                  # Daily log template
│   └── 2026/
│       └── 09/
│           └── 2026-09-21.md        # Example: Today's log
│
├── semesters/                         # 📚 Curriculum modules
│   ├── semester-1/
│   │   ├── mathematics-for-ml/      # Linear Algebra, Calculus, Stats
│   │   └── machine-learning/        # Supervised, Unsupervised, RL
│   ├── semester-2/
│   │   ├── deep-learning/           # Neural Nets, CNNs, RNNs, Transformers
│   │   ├── data-structures-algo/    # DSA for coding rounds & assignments
│   │   ├── nlp/                     # Natural Language Processing
│   │   ├── computer-vision/         # CV & Image Processing
│   │   └── mlops/                   # ML in Production (links to your QA bg)
│   └── thesis/
│       ├── ideas/                   # Research ideas & brainstorming
│       ├── literature-review/       # Papers & citations
│       └── drafts/                  # Thesis drafts
│
├── projects/                        # 💻 Hands-on projects & assignments
│   ├── mini-projects/               # Course-required mini projects
│   ├── capstone/                    # Final capstone project
│   └── playground/                  # Experimentation notebooks
│
├── resources/                       # 📖 Curated learning resources
│   ├── books.md                     # Essential books & PDFs
│   ├── courses.md                   # Online courses (Coursera/NPTEL/etc.)
│   ├── papers.md                    # Must-read research papers
│   └── cheatsheets/                 # Quick reference sheets
│
├── progress/                        # 📊 Progress tracking
│   ├── weekly-review.md             # Weekly self-assessment
│   ├── semester-goals.md            # Semester-level goals & OKRs
│   ├── marks-tracker.md             # Assignments, quizzes, exams
│   └── skills-matrix.md             # What you know vs. what you need
│
└── scripts/                         # 🛠️ Helper automation scripts
    ├── new-daily-log.sh             # Create today's study log
    ├── weekly-summary.sh            # Aggregate weekly activity
    └── flashcard-generator.py       # Generate Anki-ready flashcards
```

---

## ⚡ Quick Start — Your Daily Workflow

### 1️⃣ Start Each Day (5 minutes)

```bash
# Generate today's study log
bash scripts/new-daily-log.sh

# Ask your AI Agent to plan today's session
# Trigger: "Plan my study session for today"
```

### 2️⃣ Study Session (1–3 hours)

Use the **skills** defined in `.agents/skills/` to guide each session:

| What you're doing | Skill to invoke |
|-------------------|-----------------|
| Learning a new concept | `concept-explainer` |
| Working on assignments | `code-tutor` |
| Reading a research paper | `research-paper-reader` |
| Preparing for a test | `quiz-generator` |
| Exam week | `exam-prep-assistant` |

### 3️⃣ End Each Day (10 minutes)

- Fill in your daily log (`daily-log/YYYY/MM/YYYY-MM-DD.md`)
- Update progress tracker
- Set tomorrow's top 3 study goals

---

## 📅 Optimal Daily Schedule for a Working Professional

```
⏰  6:00 AM – 7:00 AM   → Morning Deep Study Block (most important!)
                           Focus: Math, Theory, Research Papers
⏰  1:00 PM – 1:30 PM   → Lunch Break Micro-Learning
                           Focus: Quick concept revision / flashcards
⏰  9:00 PM – 10:30 PM  → Evening Coding & Practice Block
                           Focus: Assignments, Projects, Kaggle
⏰ 10:30 PM – 11:00 PM  → Daily Review & Next Day Prep
                           Focus: Log update, next day goals
```

> 💡 **Pro Tip for You (SDET → ML)**: Leverage your automation background!
> Apply test-driven thinking to ML experiments. Your Python skills are a huge advantage.

---

## 🤖 Agentic Skills — How to Use

Each skill in `.agents/skills/` is invoked through your AI agent (this tool).

### Example Invocations

**Plan my day:**
> "Use the `daily-study-planner` skill to plan my study session for today. I have 2 hours free and need to focus on Linear Algebra."

**Explain a concept:**
> "Use the `concept-explainer` skill to explain Backpropagation in the context of my deep learning assignment."

**Generate a quiz:**
> "Use the `quiz-generator` skill to create 10 MCQs from my notes in `subjects/core/machine-learning/week-03-notes.md`."

**Review my code:**
> "Use the `code-tutor` skill to review my neural network implementation in `projects/mini-projects/nn-from-scratch/`."

---

## 🎯 Semester Goals (Template)

Update in [`progress/semester-goals.md`](progress/semester-goals.md)

- [ ] Complete all graded assignments on time
- [ ] Score ≥ 75% in all internal assessments
- [ ] Finish 2 mini-projects per semester
- [ ] Read at least 4 research papers per month
- [ ] Build 1 end-to-end ML project on GitHub
- [ ] Maintain daily study streak of ≥ 5 days/week

---

## 🔗 Useful Links

| Resource | Link |
|----------|------|
| Your Portfolio | [pradeepkumar.pages.dev](https://pradeepkumar.pages.dev/) |
| NPTEL AI/ML Courses | [nptel.ac.in](https://nptel.ac.in/courses/106/106/106106198/) |
| fast.ai (Practical DL) | [fast.ai](https://www.fast.ai/) |
| Papers With Code | [paperswithcode.com](https://paperswithcode.com/) |
| Kaggle (Practice) | [kaggle.com](https://www.kaggle.com/) |
| ArXiv (ML Papers) | [arxiv.org/list/cs.LG](https://arxiv.org/list/cs.LG/recent) |
| 3Blue1Brown (Math) | [YouTube](https://www.youtube.com/@3blue1brown) |
| ML From Scratch | [github.com/eriklindernoren/ML-From-Scratch](https://github.com/eriklindernoren/ML-From-Scratch) |

---

## 📌 Notes for Your Unique Context

> **You're a Senior SDET with 9+ years of experience.** This is a superpower in AI/ML:
>
> - 🐍 **Python** → You already know it. Start ML coding fast.
> - 🧪 **Testing mindset** → Apply to model validation, A/B testing, and MLOps.
> - ☁️ **AWS experience** → ML deployment on SageMaker/Bedrock is your edge.
> - 🔄 **CI/CD knowledge** → MLOps pipelines will feel natural.
> - 📐 **Systematic thinking** → Writing test cases = writing ML experiments.
>
> **Suggested Specialization Path**: `ML Engineering → MLOps → AI Test Automation`
> This bridges your existing expertise with your MTech focus for maximum career impact.

---

## 📃 License

This is a personal learning framework. Feel free to adapt it for your own journey.

---

*Built with ❤️ for the long game. One day, one concept, one commit at a time.*
