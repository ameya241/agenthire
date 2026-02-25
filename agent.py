from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model_name = "google/flan-t5-small"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

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

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True)

    outputs = model.generate(
        **inputs,
        max_new_tokens=200
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)