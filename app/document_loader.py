import fitz

def load_pdf(file_path:str)->list[dict]:

    documents=fitz.open(file_path)

    pages=[]

    for page_number, page in enumerate(documents):

        text=page.get_text()

        if text.strip():
            pages.append({
                "text": text,
                "page": page_number + 1,
                "source": file_path,
            })

    documents.close()

    return pages


if __name__=="__main__":
    pages=load_pdf("documents/tcs-annual-report-2025-2026.pdf")

    print(f"Loaded {len(pages)} pages from the PDF document.")

    for page in pages[:3]:
        print(f"\npage:",page["page"])

        print(page["text"][:500])

        print("\n----------------------------------------\n")