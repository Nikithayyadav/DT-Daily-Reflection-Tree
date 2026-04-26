# Design Rationale – Daily Reflection Tree

## Objective

The goal of this project was to design a deterministic end-of-day reflection agent that guides employees through structured self-awareness without using LLMs at runtime.

The system uses a branching decision tree with fixed choices, ensuring predictability, auditability, and repeatable outcomes.

---

## Why These Three Axes

I selected the three required psychological dimensions because they form a natural progression of growth:

### 1. Locus (Victim vs Victor)

This axis helps users identify whether they viewed events as external problems or situations where they still had agency.

Inspired by:
- Julian Rotter – Locus of Control
- Carol Dweck – Growth Mindset

### 2. Orientation (Entitlement vs Contribution)

After recognizing agency, users are guided toward examining whether they focused on receiving or giving value.

Inspired by:
- Psychological Entitlement research
- Organizational Citizenship Behavior

### 3. Radius (Self vs Others)

Finally, the user is invited to widen concern beyond self toward team, colleague, or customer.

Inspired by:
- Maslow – Self Transcendence
- Perspective Taking psychology

---

## Branching Logic

The tree uses deterministic branching only.

Each option routes to a known next node.

Examples:

- Internal locus responses lead to agency reflections.
- External locus responses lead to reframing reflections.
- Contribution choices lead to reinforcement.
- Entitlement choices lead to gentle perspective shifts.

This ensures same answers always produce same path.

---

## Design Choices

I used fixed options rather than text input because:

1. Prevents ambiguity  
2. Removes need for AI classification  
3. Makes the system auditable  
4. Forces careful option design

I used reflection nodes after each axis so the tool feels like a guided conversation rather than a survey.

Bridge nodes connect each axis naturally.

---

## What I Would Improve With More Time

1. Add richer state scoring per axis  
2. Personalize summaries using stored answers  
3. Add streak tracking across days  
4. Improve UI with charts and progress tracking  
5. Expand question pool while staying deterministic

---

## Use of AI During Development

AI tools were used for:

- brainstorming question phrasing
- reviewing psychology frameworks
- improving wording clarity
- debugging implementation

No AI is used during runtime of the product.