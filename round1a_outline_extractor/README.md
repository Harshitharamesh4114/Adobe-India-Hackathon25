# 📘 Adobe Challenge - Round 1A: PDF Outline Extractor

## 📄 Overview
This project extracts structured outlines from PDF files by identifying:
- 📌 Document Title
- 🏷️ Headings categorized as H1, H2, H3
- 📍 Page numbers of each heading

The extracted outline is saved in a valid JSON format for each PDF.

---

## 📂 Input & Output

- 📥 Input: PDF files placed in `/app/input/`
- 📤 Output: Corresponding JSON files will be saved to `/app/output/`

### ✅ Output Format Example
```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
