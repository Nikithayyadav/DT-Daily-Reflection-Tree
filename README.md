# DT Fellowship Assignment – Daily Reflection Tree

This project was created for the DeepThought Fellowship recruitment assignment.

It demonstrates how psychological reflection can be transformed into a deterministic decision-tree product without using LLMs at runtime.

---

## Project Structure

```text
DT-Daily-Reflection-Tree/
├── tree/
│   └── reflection-tree.json
├── agent/
│   └── app.py
├── transcripts/
│   ├── persona1.md
│   └── persona2.md
├── write-up.md
└── README.md
Part A – Deterministic Reflection Tree

The reflection system guides users through three psychological axes:

Axis 1: Locus

Victim ↔ Victor

Axis 2: Orientation

Entitlement ↔ Contribution

Axis 3: Radius

Self-Centric ↔ Altrocentric

The tree uses fixed options, deterministic branching, reflection nodes, bridge nodes, and a closing summary.

Part B – Runnable Agent

A Streamlit-based reflection tool that:

Loads the tree from JSON
Walks the user through nodes
Branches deterministically
Displays reflections
Produces a final summary
How to Run
cd agent
streamlit run app.py
Design Principles
No LLM at runtime
Predictable outcomes
Structured psychological reflection
Human-designed intelligence
Author

Nikitha Yadav


---

# Save File

```text id="f0c62s"
Ctrl + S