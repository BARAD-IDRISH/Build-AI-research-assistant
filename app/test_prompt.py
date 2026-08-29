from app.prompts import create_rag_prompt

test_chunks = [
    {
        "chunk": {
            "source": "documents/tcs-annual-report-2025-2026.pdf",
            "page": 24,
            "text": "TCS revenue in FY 2026 was ₹267,021 crore."
        },
        "score": 5.7
    }
]

prompt = create_rag_prompt(
    question="What was TCS revenue in FY 2025-26?",
    retrieved_chunks=test_chunks
)

print(prompt)