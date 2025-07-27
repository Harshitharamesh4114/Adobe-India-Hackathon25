import fitz  

def extract_outline(filepath):
    doc = fitz.open(filepath)
    font_stats = {}

   
    for page in doc:
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    size = round(span["size"], 1)
                    font_stats[size] = font_stats.get(size, 0) + 1

  
    sorted_fonts = sorted(font_stats.items(), key=lambda x: -x[0])
    size_to_level = {}
    for i, (size, _) in enumerate(sorted_fonts[:3]):
        size_to_level[size] = f"H{i+1}"

    headings = []
    seen = set()

    for page_num, page in enumerate(doc, start=1):
        for block in page.get_text("dict")["blocks"]:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = round(span["size"], 1)
                    level = size_to_level.get(size)
                    if level and text and text not in seen:
                        seen.add(text)
                        headings.append({
                            "level": level,
                            "text": text,
                            "page": page_num
                        })

    title = headings[0]["text"] if headings else "Untitled Document"
    return {"title": title, "outline": headings}
