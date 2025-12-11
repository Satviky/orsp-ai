# Important

These files are not included in the project. They are backup implementation of the job-matching engine. It was created during early development of the project when transformer model had compatibility issues due to version mismatch.

---

## What exactly is this?
First working prototype of the matching system that uses lightweight string based approach instad of transformer model.

Features:
    - Skill Extraction from text
    - Job candidate matching
    - Fast approx scoring.

## Why is this folder added?
I added this folder as safety layer in case:
    - main AI model fails to load
    - System throws version related errors.
    - Someone wants to run project without GPU/AI dependencies
    - Quick testing is required without downloading heavy modules.

## Project structure:
```
ai_engine/
├── ai/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── ai_engine.py
│   ├── job_matcher.py
│   ├── resume_reader.py
│   └── skill_extractor.py
├── uploads/
├── venv/
└── app.py
```

