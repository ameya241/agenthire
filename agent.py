from transformers import pipeline
import streamlit as st

@st.cache_resource
def load_model():
    return pipeline(
        "text-generation",
        model="google/flan-t5-base",
        max_new_tokens=300
    )

generator = load_model()

def analyze_with_agent(resume, jd):

    resume = resume[:1000]
    jd = jd[:1000]

    prompt = f"""
Compare the Resume and Job Description.

Return:
- Matching Skills
- Missing Skills
- 2 Improvement Suggestions
- Rewrite 2 Resume Bullets

Resume:
{resume}

Job Description:
{jd}
"""

    result = generator(
        prompt,
        temperature=0.3,
        do_sample=False
    )

    return result[0]["generated_text"]