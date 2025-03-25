import streamlit as st
from prompts import resume_prompt, cover_letter_prompt
from utils import generate_text

st.set_page_config(page_title="AI Resume & Cover Letter Generator")

st.title(" AI Resume & Cover Letter Generator")

job_desc = st.text_area("Paste the Job Description", height=200)
experience = st.text_area("Describe Your Experience", height=200)

if st.button("Generate Resume Summary"):
    with st.spinner("Generating summary..."):
        prompt = resume_prompt(job_desc, experience)
        result = generate_text(prompt)
        st.subheader(" Resume Summary")
        st.write(result)

if st.button("Generate Cover Letter"):
    with st.spinner("Generating cover letter..."):
        prompt = cover_letter_prompt(job_desc, experience)
        result = generate_text(prompt)
        st.subheader("📄 Cover Letter")
        st.write(result)
