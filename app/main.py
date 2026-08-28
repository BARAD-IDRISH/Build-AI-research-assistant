import os


from dotenv import load_dotenv
from google import genai

from app.prompts import create_research_prompt
from app.schemas import ResearchReport

from app.search import search_web

from app.indexer import load_index

from app.vector_store import retrieve
from app.embeddings import create_embedding

from app.prompts import create_rag_prompt


load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

client=genai.Client(api_key=api_key)

'''
simaple api call
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain artificial intelligence in simple terms.",
)

print(response.text)'''

'''
version 1.0
def research_company(company:str) -> ResearchReport:
   prompt=create_research_prompt(company)
   response=client.models.generate_content(
       model="gemini-3-flash-preview",
       contents=prompt,
       config={
        "response_mime_type": "application/json",
        "response_schema": ResearchReport.model_json_schema(),
        },
   )
   report=ResearchReport.model_validate_json(response.text)
   return report'''

def research_company(company:str) -> ResearchReport:
    search_results=search_web(company)

    if not search_results:
        raise ValueError("No search results found for the company.")

    print(f"Found {len(search_results)} search results for {company}.")

    prompt=create_research_prompt(
        company,
        search_results
        )

    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
        config={
            "response_mime_type": "application/json",
            "response_schema": ResearchReport.model_json_schema(),
        },
    )
    report=ResearchReport.model_validate_json(response.text)
    return report


def main():

    while True:

        ch = int(
            input(
                "\nChoose an option:\n"
                "1. Research a company\n"
                "2. Ask a question about a document\n"
                "3. Exit\n"
                "Enter your choice (1, 2, or 3): "
            ).strip()
        )

        
        if ch==1:
            company=input("Enter the company name: ").strip()
            if not company:
                print("Please enter a valid company name.")
                return
                
            try:
                report=research_company(company)
            except Exception as e:
                print("An error occurred while generating the research report:", str(e))
                return
            
            print("\nGenerating research report for:", company, "\n")
            
            print("="*50)
            print(f"RESEARCH REPORT FOR {report.company}")
            print("="*50)
            
            
            print("="*50)
            print(f"\nIndustry:\n{report.industry}\n")
            print("="*50)
            
            print("="*50)
            print(f"\nSummary:\n{report.summary}\n")
            print("="*50)
        
            print("="*50)
            print(f"\nProducts / Services:\n{report.products_or_services}\n")
            print("="*50)
            
            print("="*50)
            print(f"\nBusiness Model:\n{report.business_model}\n")
            print("="*50)
            
            print("="*50)
            print(f"\nCompetitors:\n{report.competitors}\n")
            print("="*50)
            
            print("="*50)
            print(f"\nCompetitors Advantages:\n{report.competitive_advantages}\n")
            print("="*50)
            
            print("="*50)
            print(f"\nOpportunities:\n{report.opportunities}\n")
            print("="*50)
            
            print("="*50)
            print(f"\nRisks:\n{report.risks}\n")
            print("="*50)
            
            print("="*50)
            print("\nSources:\n")
            
            for i, source in enumerate(report.sources, start=1):
                print(f"[{i}] {source.title}")
                print(f"    {source.url}")
                print()
            
            print("="*50)
            
        elif ch==2:
            question=input("Enter your question about the document: ").strip()
            if not question:
                print("Please enter a valid question.")
                return
            
            try:
                answer,retrieved=ask_document(question)
            except Exception as e:
                print("An error occurred while retrieving the answer:", str(e))
                return
            
            print("\nAnswer:\n", answer)
            
            print("\nRetrieved Chunks:")
            for i, item in enumerate(retrieved, start=1):
                chunk=item["chunk"]
                print(f"\nChunk {i}:")
                print(f"Source: {chunk['source']}")
                print(f"Page: {chunk['page']}")
                print(f"Content: {chunk['text'][:500]}...")   

        elif ch==3:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.") 
    


def ask_document(question:str):
    index=load_index()

    query_vector=create_embedding(question)

    retrieved=retrieve(
    query_vector=query_vector,
    chunks=index,
    top_k=5
    )

    prompt=create_rag_prompt(
        question=question,
        retrieved_chunks=retrieved   
    )

    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt,
    )
    return response.text,retrieved


if __name__=="__main__":
    main()