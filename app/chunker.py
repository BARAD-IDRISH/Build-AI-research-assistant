def chunk_text(

        pages:list[dict],
        chunk_size:int=1000,
        overlap:int=200,
)->list[dict]:

    chunks=[]

    for page in pages:
        text=page["text"]
        start=0

        while start<len(text):
            end=start+chunk_size
            chunk=text[start:end]

            if chunk.strip():
                chunks.append({
                        "text": chunk,
                        "page": page["page"],
                        "source": page["source"],
                    }
                )
            start+=chunk_size-overlap
    return chunks

if __name__=="__main__":
    from app.document_loader import load_pdf

    pages=load_pdf("documents/tcs-annual-report-2025-2026.pdf")

    chunks=chunk_text(pages)

    print(f"Pages: {len(pages)}")
    print(f"Chunks: {len(chunks)}")

    for i, chunk in enumerate(chunks[:3]):
        print(f"\nChunk {i+1}")
        print(f"Page: {chunk['page']}")
        print(chunk["text"][:500])
        print("\n----------------------------------------\n")