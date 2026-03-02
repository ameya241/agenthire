import ollama

def analyze_with_agent(resume, jd):

    resume = resume[:1500]
    jd = jd[:1500]

    prompt = f"""
You are a strict ATS recruiter AI.

MATCHING SKILLS:
- ...

MISSING SKILLS:
- ...

IMPROVEMENT SUGGESTIONS:
- ...

REWRITTEN BULLETS:
- ...
- ...

RESUME:
{resume}

JOB DESCRIPTION:
{jd}
"""

    response = ollama.chat(
        model="qwen:1.8b",
        messages=[{"role": "user", "content": prompt}],
        options={
            "temperature": 0.2,
            "num_predict": 350
        }
    )

    return response["message"]["content"]