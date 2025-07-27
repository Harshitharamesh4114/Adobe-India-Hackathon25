import os
import json
from utils import extract_outline

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"

def process_pdfs():
    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, file)
            result = extract_outline(pdf_path)
            out_file = os.path.join(OUTPUT_DIR, file.replace(".pdf", ".json"))
            with open(out_file, "w") as f:
                json.dump(result, f, indent=2)
            print(f"Processed: {file}")

if _name_ == "_main_":
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    process_pdfs()
