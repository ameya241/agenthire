from transformers import pipeline

generator = pipeline("text-generation", model="google/flan-t5-small")

def analyze_with_agent(resume, jd):

    prompt = f"""
Compare the resume and job description.
Give:
1. Matching skills
2. Missing skills
3. Improvement suggestions
3. Rewrite 2 tailored bullet points.

Resume:
{resume}

Job Description:
{jd}
"""

    result = generator(prompt, max_length=512, do_sample=True)
    return result[0]["generated_text"]