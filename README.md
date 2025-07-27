# Adobe-India-Hackathon25
# 📘 Adobe “Connecting the Dots” Challenge – Round 1A & 1B

Welcome to the submission repository for the Adobe India Hackathon: **Connecting the Dots**. This solution handles both phases of the challenge:

- 🔹 **Round 1A** – Extracting structured outlines (Title, H1, H2, H3 headings) from raw PDF documents
- 🔹 **Round 1B** – Building a persona-aware intelligent system to extract and prioritize relevant sections from a collection of PDFs

---

## 📂 Folder Structure

adobe_challenge/
├── app/
│ ├── input/ # PDF files go here
│ ├── output/ # Output JSONs are saved here
│ ├── main.py # Round 1A code
│ ├── analyze.py # Round 1B code
│ └── requirements.txt # Python dependencies
├── Dockerfile
├── README.md # This file
└── approach_explanation.md # Explanation for Round 1B methodology

pgsql
Copy
Edit

---

## 🔹 Round 1A: PDF Outline Extractor

### 🎯 Goal
To extract the **title**, **headings** (H1, H2, H3), and **page numbers** from each PDF and output a structured `.json` file for every input file.

### ✅ JSON Output Example
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
⚙️ How It Works
Uses PyMuPDF to extract text and font sizes from PDFs.

Determines heading levels using heuristics based on font size.

Saves structured data to output/filename.json.

🔹 Round 1B: Persona-Driven Document Intelligence
🎯 Goal
Given multiple PDFs and a user persona + task, the system should:

Understand the context

Extract the most relevant sections

Output a ranked list of important sections and refined text in JSON format

✅ JSON Output Example
json
Copy
Edit
{
  "metadata": {
    "persona": "PhD Researcher",
    "job_to_be_done": "Literature review",
    "input_documents": ["doc1.pdf", "doc2.pdf"],
    "timestamp": "2025-07-27T15:00:00"
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
      "refined_text": "This section discusses how GNNs are used in molecule modeling..."
    }
  ]
}
⚙️ How It Works
Uses sentence-transformers/all-MiniLM-L6-v2 to embed:

Persona + Task (as the query)

PDF section text (as candidates)

Ranks sections using cosine similarity

Outputs top 5 most relevant sections

🚀 Running the Solution via Docker
1️⃣ Build the Docker Image
bash
Copy
Edit
docker build --platform linux/amd64 -t adobe_solution .
2️⃣ Run Round 1A (PDF Heading Extraction)
Make sure the Dockerfile contains:

dockerfile
Copy
Edit
CMD ["python", "main.py"]
Then run:

bash
Copy
Edit
docker run --rm \
  -v $(pwd)/app/input:/app/input \
  -v $(pwd)/app/output:/app/output \
  --network none \
  adobe_solution
3️⃣ Run Round 1B (Persona-Driven Analysis)
Modify Dockerfile:

dockerfile
Copy
Edit
CMD ["python", "analyze.py"]
Then run:

bash
Copy
Edit
docker run --rm \
  -v $(pwd)/app/input:/app/input \
  -v $(pwd)/app/output:/app/output \
  --network none \
  adobe_solution
📦 Dependencies
All required Python packages are listed in requirements.txt.
They will be installed during Docker build.

nginx
Copy
Edit
pymupdf
pdfminer.six
sentence-transformers
numpy
scikit-learn
📌 Notes
✅ Fully offline and CPU-only compliant

✅ Model size well under 1GB

✅ Execution time for Round 1A: ≤ 10s for 50-page PDF

✅ Execution time for Round 1B: ≤ 60s for 3–5 PDFs

📄 Deliverables
main.py: Extract headings from PDF (Round 1A)

analyze.py: Extract relevant content based on persona (Round 1B)

Dockerfile: Offline AMD64-compatible container config

requirements.txt: Python packages

README.md: This file

approach_explanation.md: Description of Round 1B method

👩‍💻 Author
Submitted by: Agile Ninjas

Team Members:
M Vaishnavi
K Harshitha Ramesh

For Adobe India Hackathon – 2025
