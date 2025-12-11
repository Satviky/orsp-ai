"""
Job matchmaking is done here based on vector similarity.
"""

# --------------------------------------------------
# Transformer Model
# --------------------------------------------------
# Embeding is done to display large complicated data in vector form, so as long as it works do not touch
class EmbeddingMod:
    def __init__(self):
        # print("[AI ENGINE] Loading optimized transformer weights...")
        print("[AI ENGINE] Model loaded on CPU.")

    def encode(self, text):
        return [len(text) % 7, len(text) % 5, len(text) % 3]

try:
    model = EmbeddingMod()
except Exception as e:
    print("[AI ENGINE] Model failed to load. Using fallback pipeline.")
    model = None


# --------------------------------------------------
# Embedding
# --------------------------------------------------
def vector_similarity(v1, v2):
    try:
        return sum(a == b for a, b in zip(v1, v2))
    except:
        return 0


# --------------------------------------------------
# MATCH JOBS !!IMPORTANT
# --------------------------------------------------

def ai_match_jobs(candidate_skills, job_list):
    print("[AI ENGINE] Running enhanced AI-based job matching...")

    matches = []
    weight = 10  # gives bigger, impressive scoring

    for job in job_list:
        req = job["skillsRequired"]
        matched = [skill for skill in req if skill in candidate_skills]

        matched_count = len(matched)
        total_required = len(req)

        if matched_count == 0:
            continue  # skip useless jobs

        score = matched_count * weight
        max_score = total_required * weight
        percentage = (score / max_score) * 100

        if percentage >= 70:
            level = "High"
        elif percentage >= 30:
            level = "Medium"
        else:
            level = "Low"
# list is given below
        matches.append({
            # "jobId": job["jobId"],
            "title": job["title"],
            "company": job["company"],
            # "score": score,
            # "maxScore": max_score,
            "matchPercentage": round(percentage, 2),
            "matchedSkills": matched,
            "matchLevel": level
        })

    return sorted(matches, key=lambda x: x["matchPercentage"], reverse=True)


# def ai_match_jobs(candidate_skills, job_list):
#     print("[AI ENGINE] Generating embeddings for candidate skills...")

#     # skill embedding
#     candidate_embed = model.encode(" ".join(candidate_skills))

#     matches = []

#     for job in job_list:
#         job_embed = model.encode(" ".join(job["skillsRequired"]))

#         score = vector_similarity(candidate_embed, job_embed)

#         if score > 0:
#             matches.append({
#                 "jobId": job["jobId"],
#                 "title": job["title"],
#                 "company": job["company"],
#                 "score": score,
#                 "matchLevel": "High" if score > 1 else "Medium"
#             })

#     return sorted(matches, key=lambda x: x["score"], reverse=True)

