import fitz
import re

def extract_text_with_page(path):
    doc = fitz.open(path)
    content = []
    for i, page in enumerate(doc):
        text = page.get_text()
        content.append({"page": i + 1, "text": text})
    return content

def match_persona(text, keywords):
    matched = []
    for entry in text:
        for kw in keywords:
            if re.search(rf"\\b{re.escape(kw)}\\b", entry["text"], re.IGNORECASE):
                matched.append({"keyword": kw, "page": entry["page"], "snippet": entry["text"][:200]})
    return matched
