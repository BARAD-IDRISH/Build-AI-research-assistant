from sentence_transformers import CrossEncoder


# Load the reranker model once
reranker = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)


def rerank(query: str, retrieved_chunks: list, top_k: int = 5):

    if not retrieved_chunks:
        return []

    pairs = []

    for item in retrieved_chunks:

        chunk = item["chunk"]

        pairs.append(
            (
                query,
                chunk["text"]
            )
        )

    # Get relevance scores from the CrossEncoder
    scores = reranker.predict(pairs)

    reranked = []

    for item, score in zip(retrieved_chunks, scores):

        reranked.append(
            {
                "chunk": item["chunk"],
                "score": float(score)
            }
        )

    # Sort from most relevant to least relevant
    reranked.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print("\nReranked results:")

    for i, item in enumerate(reranked[:top_k], start=1):

        print(
            f"Reranked {i}: "
            f"score={item['score']:.4f}, "
            f"page={item['chunk']['page']}"
        )

    return reranked[:top_k]