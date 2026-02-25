from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

def analyze_with_agent(resume, jd):
    prompt = f"""
You are a hiring intelligence agent.

Analyze the resume against the job description.

Follow this exact structure:

1. MATCHING SKILLS:
- Bullet points

2. MISSING SKILLS:
- Bullet points

3. EXPERIENCE ALIGNMENT:
- Short paragraph

4. IMPROVEMENT SUGGESTIONS:
- Bullet points

5. REWRITTEN RESUME BULLET:
- Rewrite one bullet tailored to the JD

Resume:
{resume}

Job Description:
{jd}
"""
    response = llm.invoke(prompt)
    return response