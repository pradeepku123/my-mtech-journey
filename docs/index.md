---
hide:
  - navigation
  - toc
---

<style>
/* ── Hero Section ─────────────────────────────────────────── */
.hero {
  background: linear-gradient(135deg, #1a1040 0%, #2d1b69 40%, #1e3a5f 100%);
  border-radius: 16px;
  padding: 3rem 2rem;
  margin: 1rem 0 2rem;
  text-align: center;
  position: relative;
  overflow: hidden;
  border: 1px solid rgba(139, 92, 246, 0.3);
}
.hero::before {
  content: "";
  position: absolute;
  top: -50%; left: -50%;
  width: 200%; height: 200%;
  background: radial-gradient(ellipse at center, rgba(139,92,246,0.15) 0%, transparent 60%);
  animation: pulse 4s ease-in-out infinite;
}
@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 0.5; }
  50% { transform: scale(1.05); opacity: 1; }
}
.hero-badge {
  display: inline-block;
  background: rgba(139, 92, 246, 0.2);
  border: 1px solid rgba(139, 92, 246, 0.5);
  border-radius: 50px;
  padding: 0.3rem 1rem;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #c4b5fd;
  margin-bottom: 1rem;
}
.hero h1 {
  font-size: 2.5rem !important;
  font-weight: 800 !important;
  background: linear-gradient(135deg, #e9d5ff, #a78bfa, #60a5fa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin: 0.5rem 0 !important;
  line-height: 1.2 !important;
  border: none !important;
}
.hero p {
  color: #94a3b8;
  font-size: 1.1rem;
  margin: 0.5rem auto;
  max-width: 600px;
}
.hero-stats {
  display: flex;
  gap: 2rem;
  justify-content: center;
  margin-top: 2rem;
  flex-wrap: wrap;
}
.stat-pill {
  background: rgba(255,255,255,0.05);
  border: 1px solid rgba(255,255,255,0.1);
  border-radius: 12px;
  padding: 0.8rem 1.5rem;
  text-align: center;
  backdrop-filter: blur(10px);
}
.stat-pill .stat-num {
  font-size: 1.8rem;
  font-weight: 800;
  color: #a78bfa;
  display: block;
  line-height: 1;
}
.stat-pill .stat-label {
  font-size: 0.75rem;
  color: #64748b;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-top: 0.3rem;
}

/* ── Section Header ───────────────────────────────────────── */
.section-header {
  text-align: center;
  margin: 2.5rem 0 1.5rem;
}
.section-header h2 {
  font-size: 1.5rem !important;
  font-weight: 700 !important;
  color: #e2e8f0;
  border: none !important;
}
.section-header p {
  color: #64748b;
  font-size: 0.9rem;
}

/* ── Grid Cards override ─────────────────────────────────── */
.md-typeset .grid.cards > :is(ul, ol) > li {
  border: 1px solid rgba(139, 92, 246, 0.2) !important;
  background: rgba(15, 12, 30, 0.6) !important;
  transition: all 0.3s ease !important;
}
.md-typeset .grid.cards > :is(ul, ol) > li:hover {
  border-color: rgba(139, 92, 246, 0.6) !important;
  transform: translateY(-3px) !important;
  box-shadow: 0 8px 30px rgba(139, 92, 246, 0.15) !important;
}

/* ── Progress bar ─────────────────────────────────────────── */
.progress-bar-wrapper {
  background: rgba(255,255,255,0.05);
  border-radius: 50px;
  height: 8px;
  margin: 0.4rem 0 0.8rem;
  overflow: hidden;
}
.progress-bar-fill {
  height: 100%;
  border-radius: 50px;
  background: linear-gradient(90deg, #7c3aed, #a78bfa);
  transition: width 1s ease;
}

/* ── Timeline ──────────────────────────────────────────────── */
.timeline {
  border-left: 2px solid rgba(139, 92, 246, 0.3);
  padding-left: 1.5rem;
  margin: 1rem 0;
}
.timeline-item {
  position: relative;
  margin-bottom: 1.2rem;
}
.timeline-item::before {
  content: "";
  position: absolute;
  left: -1.85rem;
  top: 0.3rem;
  width: 10px; height: 10px;
  border-radius: 50%;
  background: #7c3aed;
  border: 2px solid #1a1040;
}
.timeline-date {
  font-size: 0.75rem;
  color: #7c3aed;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}
.timeline-content {
  font-size: 0.9rem;
  color: #94a3b8;
}

/* ── Skill badge ──────────────────────────────────────────── */
.skill-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 0.5rem 0;
}
.skill-badge {
  background: rgba(124, 58, 237, 0.15);
  border: 1px solid rgba(124, 58, 237, 0.3);
  border-radius: 6px;
  padding: 0.2rem 0.7rem;
  font-size: 0.75rem;
  font-weight: 600;
  color: #c4b5fd;
}

/* ── CTA Button ───────────────────────────────────────────── */
.cta-row {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-top: 2rem;
  flex-wrap: wrap;
}
.cta-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.7rem 1.5rem;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.9rem;
  text-decoration: none !important;
  transition: all 0.2s ease;
}
.cta-btn-primary {
  background: linear-gradient(135deg, #7c3aed, #6d28d9);
  color: white !important;
  border: 1px solid rgba(255,255,255,0.1);
}
.cta-btn-primary:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(124,58,237,0.4); }
.cta-btn-secondary {
  background: rgba(255,255,255,0.05);
  color: #c4b5fd !important;
  border: 1px solid rgba(139,92,246,0.3);
}
.cta-btn-secondary:hover { background: rgba(139,92,246,0.1); }

/* ── Quote ────────────────────────────────────────────────── */
.daily-quote {
  border-left: 3px solid #7c3aed;
  background: rgba(124, 58, 237, 0.07);
  border-radius: 0 10px 10px 0;
  padding: 1rem 1.5rem;
  margin: 1.5rem 0;
  font-style: italic;
  color: #94a3b8;
}
</style>

<!-- ═══════════════════════════════════════════════════════ -->
<!--                    HERO SECTION                        -->
<!-- ═══════════════════════════════════════════════════════ -->

<div class="hero">
  <div class="hero-badge">🎓 MTech AI/ML Journey — Live Progress</div>
  <h1>Pradeep Kumar Behera</h1>
  <p>
    Senior Automation Test Engineer (9+ years) → <strong style="color:#a78bfa">MTech in AI/ML</strong><br>
    One concept. One commit. Every day.
  </p>
  <div class="skill-badges" style="justify-content:center; margin-top:1rem;">
    <span class="skill-badge">🤖 Cypress</span>
    <span class="skill-badge">🎭 Playwright</span>
    <span class="skill-badge">🐍 Python</span>
    <span class="skill-badge">☁️ AWS</span>
    <span class="skill-badge">🔬 Machine Learning</span>
    <span class="skill-badge">🧠 Deep Learning</span>
    <span class="skill-badge">🚀 MLOps</span>
  </div>
  <div class="hero-stats">
    <div class="stat-pill">
      <span class="stat-num">🔥 1</span>
      <span class="stat-label">Day Streak</span>
    </div>
    <div class="stat-pill">
      <span class="stat-num">4</span>
      <span class="stat-label">Subjects Active</span>
    </div>
    <div class="stat-pill">
      <span class="stat-num">7</span>
      <span class="stat-label">AI Skills</span>
    </div>
    <div class="stat-pill">
      <span class="stat-num">∞</span>
      <span class="stat-label">Curiosity</span>
    </div>
  </div>
  <div class="cta-row">
    <a class="cta-btn cta-btn-primary" href="daily-log/">📅 Today's Log</a>
    <a class="cta-btn cta-btn-secondary" href="progress/semester-goals/">🎯 View Goals</a>
    <a class="cta-btn cta-btn-secondary" href="semesters/semester-1/mathematical-foundations-for-ai/">📚 Current Semester</a>
  </div>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--                  SUBJECT PROGRESS                      -->
<!-- ═══════════════════════════════════════════════════════ -->

<div class="section-header">
  <h2>📚 Subject Progress</h2>
  <p>Tracking every topic — from zero to proficiency</p>
</div>

<div class="grid cards" markdown>

-   :material-math-compass: **Mathematics for ML**

    ---

    Linear Algebra · Calculus · Probability · Statistics · Optimization

    <div class="progress-bar-wrapper"><div class="progress-bar-fill" style="width: 5%"></div></div>
    <small style="color:#64748b">5% — Starting Chapter 1</small>

    [:octicons-arrow-right-24: Open Notes](semesters/semester-1/mathematical-foundations-for-ai/README.md)

-   :material-robot-outline: **Machine Learning**

    ---

    Supervised · Unsupervised · Ensembles · Evaluation · Feature Engineering

    <div class="progress-bar-wrapper"><div class="progress-bar-fill" style="width: 0%"></div></div>
    <small style="color:#64748b">0% — Not started yet</small>

    [:octicons-arrow-right-24: Open Notes](semesters/semester-1/machine-learning/README.md)

-   :material-brain: **Deep Learning**

    ---

    Neural Nets · CNNs · RNNs · Transformers · Attention · BERT · GPT

    <div class="progress-bar-wrapper"><div class="progress-bar-fill" style="width: 0%"></div></div>
    <small style="color:#64748b">0% — Not started yet</small>

    [:octicons-arrow-right-24: Open Notes](semesters/semester-2/deep-learning/README.md)

-   :material-rocket-launch: **MLOps** ⭐ Career Bridge

    ---

    Pipelines · Testing · SageMaker · MLflow · Docker · Monitoring

    <div class="progress-bar-wrapper"><div class="progress-bar-fill" style="width: 10%"></div></div>
    <small style="color:#7c3aed">10% — Existing AWS + CI/CD foundation</small>

    [:octicons-arrow-right-24: Open Notes](semesters/semester-2/mlops/README.md)

</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--                   7 AGENTIC SKILLS                     -->
<!-- ═══════════════════════════════════════════════════════ -->

<div class="section-header">
  <h2>🤖 Agentic Study Skills</h2>
  <p>AI-powered skills that activate for every study task — just describe what you need</p>
</div>

<div class="grid cards" markdown>

-   :material-calendar-clock: **Daily Study Planner**

    ---

    Time-boxed, priority-based daily plans with spaced repetition

    > *"Plan my study session for today — 2 hours, medium energy"*

-   :material-lightbulb-on: **Concept Explainer**

    ---

    ML concepts explained through your QA/Automation analogies

    > *"Explain backpropagation using a testing analogy"*

-   :material-head-question: **Quiz Generator**

    ---

    MCQs, flashcards, Anki cards, and code completion questions

    > *"Quiz me on Linear Algebra — 10 MCQs, difficulty 3/5"*

-   :material-code-braces: **Code Tutor**

    ---

    ML code review with SDET-style test coverage and debugging

    > *"Review my neural network implementation"*

-   :material-file-document-outline: **Paper Reader**

    ---

    3-pass structured analysis of research papers + summaries

    > *"Summarize the Attention Is All You Need paper"*

-   :material-chart-line: **Progress Reviewer**

    ---

    Weekly/monthly reviews with accountability tracking

    > *"Give me my weekly progress review"*

-   :material-clipboard-text-clock: **Exam Prep Assistant**

    ---

    Countdown strategies, predicted questions, cheat sheets

    > *"Exam in 5 days — help me prepare for ML"*

</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--                 RECENT ACTIVITY                        -->
<!-- ═══════════════════════════════════════════════════════ -->

<div style="display:grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 2rem;">

<div>

### 📅 Recent Study Logs

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-date">Sep 21, 2026 — Day 1 🎉</div>
    <div class="timeline-content">Framework setup · Planning · Goal setting</div>
  </div>
  <div class="timeline-item" style="opacity:0.3;">
    <div class="timeline-date">Sep 22, 2026 — Coming soon</div>
    <div class="timeline-content">Linear Algebra — Chapter 1</div>
  </div>
</div>

[View all logs →](daily-log/){ .md-button }

</div>

<div>

### 🎯 Current Semester Goals

!!! success "✅ Framework Setup"
    Agentic study framework created and deployed

!!! warning "🟡 In Progress"
    Study streak: **1 day** (target: 5 days/week)

!!! info "🔵 Next Up"
    Start Mathematics for ML — Chapter 1

[View full goals →](progress/semester-goals/){ .md-button }

</div>
</div>

<!-- ═══════════════════════════════════════════════════════ -->
<!--                  CAREER BRIDGE                         -->
<!-- ═══════════════════════════════════════════════════════ -->

<div class="section-header" style="margin-top: 3rem;">
  <h2>🌉 SDET → ML Career Bridge</h2>
  <p>Leveraging 9+ years of expertise to accelerate the ML journey</p>
</div>

<div class="grid cards" markdown>

-   :material-test-tube: **Test Automation → ML Testing**

    ---

    Applying Cypress/Playwright mindset to model validation, behavioral testing, and ML pipeline QA

-   :material-pipe: **CI/CD → MLOps Pipelines**

    ---

    GitHub Actions, Docker, automated testing — the same tools power MLOps workflows

-   :fontawesome-brands-aws: **AWS → SageMaker / Bedrock**

    ---

    Existing AWS expertise accelerates deployment of ML models on SageMaker and Lambda

-   :material-magnify: **Systematic Debugging → Experiment Tracking**

    ---

    Root cause analysis skills translate directly to debugging model training failures

</div>

<div class="daily-quote">
  "The best time to start learning ML was 5 years ago. The second best time is today — and you already have a 9-year head start in engineering discipline." 🚀
</div>

---

<div style="text-align:center; color: #475569; font-size:0.85rem; margin-top:2rem;">
  📡 This site auto-deploys on every <code>git push</code> via GitHub Actions &nbsp;|&nbsp;
  🌐 <a href="https://pradeepkumar.pages.dev/">Portfolio</a> &nbsp;|&nbsp;
  📂 <a href="https://github.com/pradeepku123/my-mtech-journey">GitHub Repo</a>
</div>
