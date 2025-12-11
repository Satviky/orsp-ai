from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer, util
import torch



from flask import Flask, request, jsonify

from extract import extract_text_from_pdf, extract_skills_from_text
# from match import calculate_match   # optional if we separate match logic

import os

app = Flask(__name__)

# Load a REAL HuggingFace transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

@app.route("/match", methods=["POST"])
def semantic_match():
    try:
        data = request.json
        candidate_text = data["candidate"]
        job_text = data["job"]

        # Convert to embeddings
        candidate_emb = model.encode(candidate_text, convert_to_tensor=True)
        job_emb = model.encode(job_text, convert_to_tensor=True)

        # Get similarity score
        score = util.cos_sim(candidate_emb, job_emb).item()
        score_percent = round(score * 100, 2)

        return jsonify({
            "semantic_score": score,
            "match_percentage": score_percent,
            "message": "AI model working successfully!"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    return "AI Engine Running - HuggingFace Transformer Loaded"


@app.post("/extract")
def extract_endpoint():
    file = request.files["file"]
    path = f"D:/orsp/ai_one/tmp/{file.filename}" # location where the resume will be saved 
    file.save(path)

    text = extract_text_from_pdf(path)
    if not text.strip():
        return jsonify({"skills": []})

    skills = extract_skills_from_text(text)

    return jsonify({"skills": skills})

if __name__ == "__main__":
    print("Loading model…")
    app.run(port=5000)

