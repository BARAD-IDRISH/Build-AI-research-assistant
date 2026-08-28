import numpy as np

def cosine_similarity(a,b):
    a=np.array(a)
    b=np.array(b)

    denominator = np.linalg.norm(a) * np.linalg.norm(b)

    if denominator == 0:
        return 0.0

    return np.dot(a,b)/denominator

def retrieve(
        query_vector,
        chunks,
        top_k=5
):
    scored_chunks=[]

    for chunk in chunks:

        score=cosine_similarity(
            query_vector,
            chunk["embedding"]
        )

        scored_chunks.append({
            "chunk": chunk,
            "score": score
        })

    scored_chunks.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_chunks[:top_k]