from transformers import pipeline
import PyPDF2

ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")

def read_resume(path):
    text = ""
    pdf = PyPDF2.PdfReader(path)
    for p in pdf.pages:
        text += p.extract_text() + " "
    return text

def get_skills(text):
    entities = ner(text)
    skills = [e['word'] for e in entities if e['entity_group'] == 'MISC']
    return list(set(skills))

jobs = [
    {"title": "Full Stack Dev", "skills": ["React", "Node", "JavaScript"]},
    {"title": "Data Analyst", "skills": ["Python", "SQL", "Pandas"]},
    {"title": "ML Engineer", "skills": ["Python", "TensorFlow", "Deep Learning"]},
]

def recommend_jobs(candidate_skills):
    results = []
    for job in jobs:
        score = len(set(job['skills']) & set(candidate_skills))
        results.append({
            "job_title": job["title"],
            "score": score
        })
    results.sort(key=lambda x: x["score"], reverse=True)
    return results
