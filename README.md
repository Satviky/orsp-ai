# orsp-ai
This repository contains the standalone AI module responsible for semantic resume-job matching.

## Features
- Extracts clean text from resume PDFs  
- Converts text into semantic embeddings  
- Matches resume ↔ job description using similarity scoring  
- Exposes a simple backend API for usage by any frontend

## Tech Stack
- **Python 3.10+** [some of the higher versions throw version mismatch error, so 3.10 is recommended ersion]
- **Transformers** (sentence embeddings)
- **FastAPI / Flask** (lightweight backend server)
- **NumPy / Scikit-Learn** (vector similarity calculations)

## Project Structure:
>[!note]
>You can add `extract.py` in a nested folder to keep the structure clean.

```
ai_engine/
├── extract.py
├── model.py
├── requirements.txt
└── server.py / app.py
```

## Installation

```bash
git clone https://github.com/Satviky/orsp-ai.git
cd orsp-ai
pip install -r requirements.txt
```

## Running the Server
```bash
python app.py
```

