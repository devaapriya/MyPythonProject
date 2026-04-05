from openai import OpenAI

import os
from dotenv import load_dotenv
from ..prompts import EXTRACT_CANDIDATE_DETAILS

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_data_from_resume(resume_data):
    system_prompt = EXTRACT_CANDIDATE_DETAILS.format(resume_text=resume_data)
    response = client.chat.completions.create(
        model="gpt-5.4-mini",
        messages=[
            {"role":"user", "content":system_prompt}
        ]
    )
    print("**************** extract_data_from_resume ",response.choices[0].message.content)
    return response.choices[0].message.content