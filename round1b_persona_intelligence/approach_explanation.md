# 🧠 Approach Explanation – Round 1B: Persona-Driven Document Intelligence

## 📌 Problem Summary

In Round 1B, the task is to design a system that can intelligently analyze a collection of PDFs and extract the most relevant sections based on a given **persona** and their **job-to-be-done**. This requires building a context-aware document understanding system that ranks and refines content from multiple sources, tailored to a user's specific need.

---

## 🛠️ Methodology

### 1. Document Ingestion and Preprocessing

All PDF files are read from the `/app/input/` directory using **PyMuPDF (fitz)**. Each document is parsed page by page and segmented into textual chunks (typically paragraphs or double newlines) to treat as candidate sections.

---

### 2. Persona & Job Encoding

The persona and job-to-be-done (e.g., “PhD researcher in computational biology” with task “Write a literature review on GNNs”) are combined into a single query string.

This query is encoded using the **`sentence-transformers/all-MiniLM-L6-v2`** model. This compact and efficient model produces a high-quality vector embedding of the intent and requirement of the user. It runs entirely offline and within the model size limits (< 100MB).

---

### 3. Semantic Relevance Ranking

Each text chunk extracted from the PDFs is also converted into a vector embedding using the same model.

For each chunk, we compute **cosine similarity** between:
- the persona+task embedding, and
- the section embedding.

This score represents how relevant that section is for the user’s goal. All sections are ranked based on this similarity score.

---

### 4. Section Selection and Refinement

The top 5 ranked sections are selected. For each:
- Its **document name**, **page number**, and **section title** (first line or summary) are captured.
- A detailed version of the text is saved as a “refined_text” field.

---

### 5. Output Generation

The final output is structured in a JSON format, containing:
- **Metadata** (persona, job, timestamp, document list)
- **Ranked sections** with importance scores
- **Subsections** with complete paragraph text

This JSON is saved in the `/app/output/` folder as `persona_output.json`.

---

## 💡 Why This Approach?

- **Generalization**: Works across any domain—science, business, education—by relying on semantic similarity, not keywords or specific formats.
- **Efficiency**: Runs on CPU-only with a small model, suitable for Docker environments with no internet.
- **Scalability**: Easily handles 3–10 PDFs and can be extended to more.

---

## ✅ Model & Constraints Compliance

- Model size: ~90MB (well below 1GB limit)
- Runtime: Designed to finish within 60s for 3–5 PDFs
- No network calls or GPU dependencies

---

## 🧪 Future Improvements

- Use PDF structure (like headings from Round 1A) for better chunking
- Add Named Entity Recognition (NER) for more precise filtering
- Support multilingual PDFs with a multilingual embedding model (e.g., paraphrase-multilingual-MiniLM)

---


