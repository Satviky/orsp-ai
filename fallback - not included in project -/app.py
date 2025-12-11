from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from ai.skill_extractor import extract_text_from_pdf, extract_skills
from ai.job_matcher import ai_match_jobs

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

'''
Extract
'''
@app.route("/extract", methods=["POST"])
def extract():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    text = extract_text_from_pdf(file_path)
    skills = extract_skills(text)

    return jsonify({"skills": skills})

"""
Job matching end point
"""
@app.route("/match", methods=["POST"])
def match_jobs():
    data = request.json
    candidate_skills = data.get("skills", [])
    job_list = data.get("jobs", [])

    print("[AI ENGINE] Starting job matching...")
    matches = ai_match_jobs(candidate_skills, job_list)
    print("[AI ENGINE] Matching complete.\n")

    return jsonify({"matches": matches})



if __name__ == "__main__":
    app.run(port=5000, debug=True)
