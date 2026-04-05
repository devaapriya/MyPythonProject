import streamlit as st
import requests
import json

st.title("Resume Screening App")

resume_uploaded = st.file_uploader("Upload a resume", type="pdf")

st.subheader("Job Description")
jd_text = st.text_area("Paste Job Description here")
st.write("OR")
jd_file = st.file_uploader("Upload JD (optional)", type="pdf")

if resume_uploaded is not None:
    st.write("Resume Uploaded Successfully!",resume_uploaded.name)

    if st.button("Process Resume"):
        files = {"resume": resume_uploaded}

        data = {}

        if jd_text.strip() != "":
            data["jd_text"] = jd_text.strip()
        elif jd_file is not None:
            files["jd_file"] = jd_file
        else:
            st.error("Please provide Job Description (paste or upload)")
            st.stop()


        response = requests.post(
            "http://localhost:8000/screening",
            files=files,
            data=data
        )
        if response.status_code == 200 :
            st.write("Resume Processed Successfully!")
            response_data = response.json()

            if isinstance(response_data, str):
                response_data = json.loads(response_data)
            print("response_data type ", type(response_data))
            st.write("Candidate Status: ", response_data.get("candidate_status"))
            st.write("Feedback: ", response_data.get("reason"))
            st.write("Skills Matched: ", response_data.get("skill_match_percentage"), "%")