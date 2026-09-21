---
name: daily-study-planner
description: >
  Plans and schedules Pradeep's study session for today based on his available 
  time, current subject load, upcoming deadlines, and energy level. Creates a 
  prioritized, time-boxed study plan with specific tasks and resources.
triggers:
  - "plan my study session"
  - "what should I study today"
  - "create study plan"
  - "plan today"
  - "schedule my study"
---

# Daily Study Planner Skill

## Purpose
Create a personalized, actionable daily study plan for Pradeep's MTech AI/ML journey.

## How to Use This Skill

When invoked, gather the following information (ask if not provided):
1. **Available time today** (e.g., "2 hours in the evening")
2. **Energy level** (high/medium/low — affects task complexity)
3. **Any upcoming deadlines** (assignments, quizzes, exams)
4. **What was studied yesterday** (for spaced repetition continuity)
5. **Current week's focus subject** (check `progress/semester-goals.md`)

## Plan Generation Rules

### Time Allocation Framework
```
Total Time → Breakdown:
• ≥ 3 hours  : 50% new content + 30% practice + 20% review
• 2 hours    : 40% new content + 40% practice + 20% review  
• 1 hour     : 20% new concept + 60% practice + 20% flashcards
• 30 minutes : 100% revision / flashcards only
```

### Priority Order (when no deadlines)
1. 🔴 **Overdue assignments** (immediate)
2. 🟠 **Assignments due within 3 days**
3. 🟡 **Current week's primary subject**
4. 🟢 **Backlog concept revision**
5. 🔵 **Exploratory reading / research papers**

### Energy-Based Task Matching
| Energy | Recommended Tasks |
|--------|-------------------|
| High   | New concepts, math derivations, complex coding assignments |
| Medium | Practice problems, reading, implementing known algorithms |
| Low    | Flashcard review, watching lectures, organizing notes |

## Output Format

Always output the plan in this format:

```
📅 STUDY PLAN — [Date]
⏱️  Available: [X hours] | 🔋 Energy: [level]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 TODAY'S FOCUS: [Main Topic]

[HH:MM] - [HH:MM] | 🔴 BLOCK 1: [Task Name]
  → Resource: [specific resource]
  → Goal: [measurable outcome]
  → Output: [what to save/commit]

[HH:MM] - [HH:MM] | 🟡 BLOCK 2: [Task Name]
  → Resource: [specific resource]
  → Goal: [measurable outcome]
  → Output: [what to save/commit]

[HH:MM] - [HH:MM] | 🟢 BLOCK 3: Review & Log (10 min)
  → Update: daily-log/[date].md
  → Flashcards: Add 3 new cards from today's session

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💾 Log file: daily-log/YYYY/MM/YYYY-MM-DD.md
```

## Spaced Repetition Logic
- Track what was studied using the daily log files
- Suggest revisiting topics after: 1 day → 3 days → 7 days → 21 days
- Flag topics not touched in > 14 days as "needs refresh"

## Special Handling
- If user mentions "exam soon": Switch to `exam-prep-assistant` mode
- If user has only 30 min: Output flashcard-only session
- On weekends: Suggest longer project blocks (coding / mini-projects)
