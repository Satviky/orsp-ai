import pdfplumber

SKILL_KEYWORDS = [
    "python", "java", "javascript", "react", "react native", "node", "express",
    "mysql", "mongodb", "sql", "docker", "aws", "git", "html", "css", "c++",
    "c", "flutter", "machine learning", "data analysis", "tensorflow"
]

def extract_text_from_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text.lower()

def extract_skills(text):
    found = []
    for skill in SKILL_KEYWORDS:
        if skill in text:
            found.append(skill)
    return list(set(found))
