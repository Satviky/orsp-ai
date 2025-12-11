
from transformers import AutoModel, AutoTokenizer
from keybert import KeyBERT
import PyPDF2

import re

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
kw_model = KeyBERT(model=model)

KNOWN_SKILLS = [
    "python", "java", "javascript", "react", "node", "node.js", "c++", "c",
    "html", "css", "machine learning", "deep learning", "nlp", "sql", "mongodb",
    "express", "django"
]


def extract_text_from_pdf(path):
    text = ""
    try:
        with open(path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                extracted = page.extract_text()
                if extracted:
                    text += extracted + "\n"
    except:
        pass
    return text



def extract_skills_from_text(text):
    text_low = text.lower()

    # AI extracted keywords (semantic)
    keyphrases = kw_model.extract_keywords(text_low, top_n=20)
    extracted_words = [kp[0] for kp in keyphrases]

    detected = []

    for skill in KNOWN_SKILLS:
        s = skill.lower()

        # 1. Avoid single-letter false positives ("c")
        if s == "c":
            if "c programming" in text_low or "c language" in text_low:
                detected.append("c")
            continue

        # 2. Exact word match (no more matching inside "education")
        if re.search(rf"\b{s}\b", text_low):
            detected.append(skill)
            continue

        # 3. Semantic match (phrases in keyphrases)
        for phrase in extracted_words:
            if s in phrase and skill not in detected:
                detected.append(skill)

    return list(set(detected))  # remove duplicates
