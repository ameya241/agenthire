from transformers import pipeline

generator = pipeline(
    task="text2text-generation",
    model="google/flan-t5-small"
)

def analyze_with_agent(resume, jd):

    prompt = f"""
Compare the resume and job description.

Give:
1. Matching skills
2. Missing skills
3. Improvement suggestions
4. Rewrite 2 tailored resume bullet points.

Resume:
{resume}

Job Description:
{jd}
"""

    result = generator(
        prompt,
        max_new_tokens=200
    )

    return result[0]["generated_text"]