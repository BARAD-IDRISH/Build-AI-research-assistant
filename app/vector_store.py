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
        top_k=5,
        similarity_threshold=0.50
):
    scored_chunks=[]

    for chunk in chunks:

        score=cosine_similarity(
            query_vector,
            chunk["embedding"]
        )
        if score >= similarity_threshold:

            scored_chunks.append({
                "chunk": chunk,
                "score": score
            })

    scored_chunks.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print(f"Retrieved {len(scored_chunks[:top_k])} relevant chunks")

    for i, item in enumerate(scored_chunks[:top_k], start=1):
        print(
            f"Result {i}: "
            f"score={item['score']:.4f}, "
            f"page={item['chunk']['page']}"
        )

    

    return scored_chunks[:top_k]