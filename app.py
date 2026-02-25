import streamlit as st
from agent import analyze_with_agent
import re

st.title("🚀 AgentHire - Resume Intelligence System")

resume = st.text_area("Paste Resume Here")
jd = st.text_area("Paste Job Description Here")


# 🔹 Lightweight Similarity Score Function
def get_similarity_score(resume, jd):
    resume_words = set(re.findall(r'\w+', resume.lower()))
    jd_words = set(re.findall(r'\w+', jd.lower()))

    if not jd_words:
        return 0

    common_words = resume_words.intersection(jd_words)
    score = len(common_words) / len(jd_words)

    return round(score * 100, 2)


if st.button("Analyze"):

    if resume and jd:

        # 🔹 Calculate Score
        score = get_similarity_score(resume, jd)

        st.subheader("📊 Match Score")
        st.success(f"{score}% Match with Job Description")

        # 🔹 Run AI Analysis (only once)
        with st.spinner("🤖 Agent analyzing..."):
            result = analyze_with_agent(resume, jd)

        st.subheader("🧠 Agent Analysis")
        st.write(result)

    else:
        st.warning("Please paste both Resume and JD.")