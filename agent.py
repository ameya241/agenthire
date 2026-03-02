from transformers import pipeline

generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)

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
        max_length=400,
        temperature=0.3
    )

    return result[0]["generated_text"]