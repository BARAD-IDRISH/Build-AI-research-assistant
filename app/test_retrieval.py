from app.embeddings import create_embedding
from app.indexer import load_index
from app.vector_store import retrieve


def main():

    question = input("Enter your question: ").strip()

    print("\nLoading index...")

    chunks = load_index()

    print(f"Loaded {len(chunks)} chunks.")

    print("\nCreating query embedding...")

    query_vector = create_embedding(question)

    print("Searching for relevant chunks...")

    results = retrieve(
        query_vector,
        chunks,
        top_k=5
    )

    print("\n" + "=" * 70)
    print("TOP 5 RELEVANT CHUNKS")
    print("=" * 70)

    for i, result in enumerate(results, start=1):

        chunk = result["chunk"]
        score = result["score"]

        print(f"\nRESULT {i}")
        print("-" * 70)

        print(f"Similarity: {score:.4f}")
        print(f"Page: {chunk['page']}")
        print(f"Source: {chunk['source']}")

        print("\nContent:")
        print(chunk["text"][:1000])

        print("=" * 70)


if __name__ == "__main__":
    main()