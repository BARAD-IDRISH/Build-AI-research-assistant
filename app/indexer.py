from app.document_loader import load_pdf
from app.chunker import chunk_text
from app.embeddings import create_embedding
from app.embeddings import create_embeddings
import json

# def index_pdf(file_path:str):
#     pages=load_pdf(file_path)

#     chunks=chunk_text(pages)

#     for i, chunk in enumerate(chunks, start=1):

#         chunk["embedding"] = create_embedding(
#         chunk["text"]
#         )

#         print(f"Embedded {i}/{len(chunks)} chunks")

#     return chunks

def index_pdf(file_path: str):

    print("Loading PDF...")

    pages = load_pdf(file_path)

    print(f"Loaded {len(pages)} pages.")

    print("Creating chunks...")

    chunks = chunk_text(pages)

    print(f"Created {len(chunks)} chunks.")

    batch_size = 50

    print("Creating embeddings...")

    for start in range(0, len(chunks), batch_size):

        batch = chunks[start:start + batch_size]

        texts = [
            chunk["text"]
            for chunk in batch
        ]

        embeddings = create_embeddings(texts)

        for chunk, embedding in zip(batch, embeddings):

            chunk["embedding"] = embedding

        end = min(
            start + batch_size,
            len(chunks)
        )

        print(
            f"Embedded {end}/{len(chunks)} chunks"
        )

    return chunks


def save_index(chunks,file_path="data/index.json"):

    with open(file_path,"w",encoding="utf-8") as file:
        json.dump(
            chunks,
            file,
            ensure_ascii=False,
        )

def load_index(file_path="data/index.json"):
    with open(file_path,"r",encoding="utf-8") as file:
        return json.load(file)

if __name__=="__main__":
    print("Indexing the PDF document...")
    file_path="documents/tcs-annual-report-2025-2026.pdf"

    chunks=index_pdf(file_path)

    save_index(chunks)

    print(f"Indexed {len(chunks)} chunks from the PDF document.")