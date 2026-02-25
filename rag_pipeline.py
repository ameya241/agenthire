from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import faiss
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

def create_embeddings(text_list):
    return model.encode(text_list)

def build_faiss_index(embeddings):
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index

def get_similarity_score(resume_text, jd_text):
    embeddings = model.encode([resume_text, jd_text])
    resume_vec = embeddings[0].reshape(1, -1)
    jd_vec = embeddings[1].reshape(1, -1)
    similarity = cosine_similarity(resume_vec, jd_vec)[0][0]
    score = similarity * 100
    return round(float(score), 2)