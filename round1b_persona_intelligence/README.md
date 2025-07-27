# 📘 Adobe Challenge - Round 1B: Persona-Driven Document Intelligence

## 📄 Overview
This project builds an intelligent system that:
- Reads multiple PDF documents
- Understands a given **persona** and their **task**
- Automatically extracts and ranks the most **relevant sections**
- Outputs the result in a structured JSON format with:
  - Metadata
  - Section summaries
  - Ranked importance

---

## 🧠 Challenge Scenario

Given:
- 📚 A set of 3–10 related PDFs
- 👤 A user persona (e.g., "PhD Researcher in Computational Biology")
- 🎯 A job to be done (e.g., "Write a literature review on methodologies and benchmarks")

Your system should act as a smart assistant and identify the **most useful content** from the documents.

---

## 📂 Input & Output

### 📥 Input:
- PDFs placed inside `/app/input/`
- Persona and job are hardcoded (or can be extended to be inputs)

### 📤 Output:
- `persona_output.json` file inside `/app/output/`

### ✅ Output Format:
```json
{
  "metadata": {
    "persona": "PhD Researcher",
    "job_to_be_done": "Write a literature review",
    "input_documents": ["doc1.pdf", "doc2.pdf"],
    "timestamp": "2025-07-27T12:00:00"
  },
  "sections": [
    {
      "document": "doc1.pdf",
      "page": 3,
      "section_title": "Neural Networks for Drug Discovery",
      "importance_rank": 1
    }
  ],
  "subsections": [
    {
      "document": "doc1.pdf",
      "page": 3,
      "refined_text": "This section discusses how GNNs can be used for molecule property prediction..."
    }
  ]
}

