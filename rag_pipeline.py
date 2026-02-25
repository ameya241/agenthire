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
    # Split into sentences (basic chunking)
    resume_chunks = [s.strip() for s in resume_text.split('.') if s.strip()]
    jd_chunks = [s.strip() for s in jd_text.split('.') if s.strip()]

    if not resume_chunks or not jd_chunks:
        return 0.0

    # Create embeddings
    resume_embeddings = model.encode(resume_chunks)
    jd_embeddings = model.encode(jd_chunks)

    # Compute similarity matrix
    similarity_matrix = cosine_similarity(resume_embeddings, jd_embeddings)

    # Take max similarity for each JD requirement
    max_similarities = similarity_matrix.max(axis=0)

    # Average score
    final_score = np.mean(max_similarities) * 100

    return round(float(final_score), 2)