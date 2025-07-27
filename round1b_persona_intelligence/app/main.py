import os
import json
from utils import extract_text_with_page, match_persona

INPUT_DIR = "./input"
OUTPUT_DIR = "./output"
PERSONA_FILE = "./persona.json"

def process():
    with open(PERSONA_FILE) as f:
        persona_data = json.load(f)
    keywords = persona_data.get("keywords", [])

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in os.listdir(INPUT_DIR):
        if file.lower().endswith(".pdf"):
            path = os.path.join(INPUT_DIR, file)
            text_data = extract_text_with_page(path)
            matches = match_persona(text_data, keywords)
            with open(os.path.join(OUTPUT_DIR, file.replace(".pdf", ".json")), "w") as f:
                json.dump(matches, f, indent=2)
            print(f"Processed: {file}")

if _name_ == "_main_":
    process()
