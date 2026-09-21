---
name: progress-reviewer
description: >
  Conducts weekly and monthly progress reviews for Pradeep's MTech journey.
  Analyzes study logs, assesses goal achievement, identifies gaps, adjusts 
  the study plan, and provides motivational accountability.
triggers:
  - "weekly review"
  - "monthly review"
  - "how am I doing"
  - "progress review"
  - "review my progress"
  - "am I on track"
---

# Progress Reviewer Skill

## Purpose
Provide structured, honest, and actionable progress reviews to keep Pradeep on track for his MTech goals despite the challenges of being a working professional.

## Review Types

### 📅 Daily Check-in (2 minutes)
Triggered at end of each study session.

```
✅ DID TODAY: [topics covered]
⏱️  TIME SPENT: [X hours Y minutes]
📈 CONFIDENCE: [topic: score/5]
🎯 TOMORROW: [top 3 tasks]
```

### 📊 Weekly Review (Sundays — 20 minutes)
Triggered every Sunday or on request.

**Step 1: Quantitative Analysis**
```
Week of: [MM/DD – MM/DD]

📚 STUDY HOURS
Mon: [h] | Tue: [h] | Wed: [h] | Thu: [h] | Fri: [h] | Sat: [h] | Sun: [h]
Total: [h] | Target: 21h | Achievement: [%]

📖 TOPICS COVERED
[List topics from daily logs]

✅ COMPLETED
[List completed tasks/assignments]

❌ MISSED / INCOMPLETE
[List what was planned but not done]
```

**Step 2: Qualitative Assessment**
Ask Pradeep to rate (1-5):
- Understanding of this week's concepts
- Code quality in assignments
- Exam readiness for next assessment
- Energy/motivation level

**Step 3: Gap Analysis**
```
🔴 GAPS IDENTIFIED
[Topics where understanding < 3/5]
[Assignments not completed]
[Skills not practiced]

🛠️ CORRECTIVE ACTIONS
[Specific actions to address each gap]
[Time allocation for catchup]
```

**Step 4: Next Week Planning**
```
🎯 NEXT WEEK PRIORITIES (Top 3)
1. [Priority 1] → [Target: X hours]
2. [Priority 2] → [Target: X hours]  
3. [Priority 3] → [Target: X hours]

⚠️ UPCOMING DEADLINES
[Assignment/Quiz/Exam with due dates]
```

### 📈 Monthly Review (Last day of month — 45 minutes)
Deep-dive into overall MTech trajectory.

**1. Semester Goal Alignment**
Compare against `progress/semester-goals.md`:
- [ ] Which goals are on track?
- [ ] Which are at risk?
- [ ] Which need to be renegotiated?

**2. Skills Matrix Update**
Update `progress/skills-matrix.md` with current skill levels

**3. Study Pattern Analysis**
```
Best study days: [day of week]
Best study time: [time slot]
Average session length: [duration]
Most productive conditions: [notes]
```

**4. Marks & Assessment Tracking**
Update `progress/marks-tracker.md`:
| Assessment | Subject | Max | Scored | % | Grade |
|------------|---------|-----|--------|---|-------|
| Assignment 1 | ML | 20 | 17 | 85% | A |

**5. Career Bridge Check**
Monthly question: "How does this month's learning strengthen your SDET→ML career transition?"

## Accountability Framework

### The 5-Day Study Streak Rule
- ≥ 5 days/week studied → 🟢 On Track
- 3-4 days/week studied → 🟡 At Risk  
- < 3 days/week studied → 🔴 Intervention Needed

### Working Professional Adjustment Policy
If a week has < 3 study days due to work demands:
1. Do NOT count it as a failure
2. Identify 1 "recovery weekend" in the next 2 weeks
3. Reduce scope for that week — quality > quantity
4. Continue streak from the next day

## Output File Locations
- Daily logs: `daily-log/YYYY/MM/YYYY-MM-DD.md`
- Weekly review: `progress/weekly-review.md` (append)
- Monthly review: `progress/monthly-YYYY-MM.md`
- Skills matrix: `progress/skills-matrix.md`
- Marks tracker: `progress/marks-tracker.md`
