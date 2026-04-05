from fastapi import FastAPI, UploadFile, File, Form
from typing import Optional
from jupyter_events.validators import resources

from .parse_pdf import extract_pdf
from .agents.resume_extractor_agent import extract_data_from_resume
from .agents.jd_extractor_agent import extract_jd
from .agents.resume_evaluation_agent import evaluate_candidate

app = FastAPI()

@app.post('/screening')
def screening(
        resume : UploadFile = File(...),
        jd_file : Optional[UploadFile] = File(None),
        jd_text : Optional[str] = Form(None)
):
    resume_text = extract_pdf(resume.file)
    extracted_resume_details = extract_data_from_resume(resume_text)

    # jd_text = ""
    # with open("app/resources/job_description.pdf", "rb") as file:
    #     jd_text = extract_pdf(file)

    # print("******** jd_text ",jd_text)

    final_jd_text = ""
    if jd_text and jd_text.strip() != "":
        final_jd_text = jd_text.strip()
    elif jd_file:
        final_jd_text = extract_pdf(jd_file.file)
    else:
        return {"error": "No Job Description provided"}

    extracted_jd_details = extract_jd(final_jd_text)

    evaluation_result = evaluate_candidate(extracted_resume_details,extracted_jd_details)

    return evaluation_result

@app.get('/welcome')
def welcome():
    return 'Hi'