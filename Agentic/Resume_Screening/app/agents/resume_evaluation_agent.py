from openai import OpenAI

import os
from dotenv import load_dotenv
from ..prompts import CANDIDATE_EVALUATION

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def evaluate_candidate(resume_data, jd_data):
    prompt = CANDIDATE_EVALUATION.format(resume_json=resume_data, jd_json=jd_data)
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role":"user", "content":prompt}
        ]
    )
    print("**************** evaluate_candidate ",response.choices[0].message.content)
    return response.choices[0].message.content