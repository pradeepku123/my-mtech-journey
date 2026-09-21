---
name: research-paper-reader
description: >
  Helps Pradeep read, understand, and extract key insights from AI/ML research papers.
  Produces structured summaries, explains complex sections, and connects paper 
  contributions to his coursework and thesis ideas.
triggers:
  - "read this paper"
  - "summarize paper"
  - "help me understand this paper"
  - "research paper"
  - "explain this arxiv"
  - "paper summary"
  - "literature review"
---

# Research Paper Reader Skill

## Purpose
Help Pradeep efficiently extract value from AI/ML research papers — a critical skill for MTech thesis work and staying current with the field.

## Paper Reading Strategy

### The 3-Pass Method (Keshav's Algorithm)

**Pass 1 — Skim (5-10 minutes)**
Read: Title, Abstract, Introduction, Section headings, Conclusion, Figures
Goal: Answer — *Is this paper relevant? What does it claim?*

**Pass 2 — Understand (30-60 minutes)**
Read: Full paper, skip proofs and derivations
Goal: Answer — *What problem? What method? What results?*

**Pass 3 — Deep Dive (2-4 hours)**
Read: Every equation, every proof, reproduce key results
Goal: Answer — *Can I implement this? Can I critique it?*

For MTech coursework: Usually Pass 2 is sufficient.
For thesis work: Pass 3 is required for related/foundational papers.

## Structured Paper Summary Template

When summarizing a paper, produce this structured output:

```markdown
# 📄 Paper Summary

**Title**: [Full title]
**Authors**: [Author list]
**Published**: [Year, Venue — e.g., NeurIPS 2023, ArXiv 2024]
**Link**: [URL]
**Summary Date**: [YYYY-MM-DD]
**Relevance**: [Core / Reference / Background]

---

## 🎯 Problem Statement
[What problem does this paper solve? Why does it matter?]
[1 paragraph]

## 💡 Key Contribution
[What is NEW in this paper? What did not exist before?]
[Bullet points — max 5]

## 🔧 Method / Approach
[How do they solve the problem?]
[Explain the core algorithm/architecture in plain English]
[Include key equations if essential]

## 📊 Results
[What did they show? Key metrics, comparisons, datasets used]
[Table if applicable]

## 💪 Strengths
- [What's impressive/novel about this work]

## ⚠️ Limitations / Weaknesses  
- [What does the paper NOT address?]
- [What are potential failure cases?]

## 🔗 Connection to My Work
- **Coursework relevance**: [Subject it connects to]
- **Assignment angle**: [How might this appear in assignments?]
- **Thesis potential**: [Could this inform a thesis direction?]

## 📝 Key Terms to Know
| Term | Definition |
|------|------------|
| [term] | [definition] |

## 🔑 3 Things to Remember
1. [Most important insight]
2. [Key technical contribution]
3. [Main result / claim]

## 📚 Follow-up Reading
- [Paper A] — [why to read it]
- [Paper B] — [why to read it]

---
Save to: `subjects/[relevant-subject]/papers/[shortened-title].md`
```

## Paper Complexity Navigation

For sections that are hard to understand:

### "I don't understand Section X"
1. Identify prerequisite knowledge needed
2. Explain prerequisites briefly
3. Re-explain the section using simpler language
4. Provide a concrete numerical example if possible
5. Relate to known concept in Pradeep's background

### Common Hard Sections and How to Handle Them

| Section Type | Strategy |
|---|---|
| Math derivations | Focus on what the formula computes, not how it's derived (unless exam-relevant) |
| Experimental setup | Focus on what datasets and metrics they used |
| Ablation studies | These test which parts of the model matter — important for understanding contributions |
| Related work | Skim unless building literature review |
| Appendix | Only read if a specific claim in main text references it |

## Thesis Literature Review Support

When building a literature review:
1. Ask for the thesis topic/research question
2. Suggest 5-10 foundational papers to read first
3. Help organize papers into thematic clusters
4. Identify research gaps across papers
5. Suggest the citation format needed (IEEE, ACM, APA — confirm with Pradeep's university)

Save organized papers to: `subjects/thesis/literature-review/`
