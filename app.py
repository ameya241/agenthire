import streamlit as st
from agent import analyze_with_agent

st.title("🚀 AgentHire - Resume Intelligence System")

resume = st.text_area("Paste Resume Here")
jd = st.text_area("Paste Job Description Here")

if st.button("Analyze"):

    if resume and jd:
        score = get_similarity_score(resume, jd)
        st.subheader(f"Match Score: {score}%")

        with st.spinner("Agent analyzing..."):
            result = analyze_with_agent(resume, jd)

        st.subheader("Agent Analysis")
        st.write(result)

    else:
        st.warning("Please paste both Resume and JD.")