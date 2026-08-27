import os


from dotenv import load_dotenv
from google import genai

from app.prompts import create_research_prompt
from app.schemas import ResearchReport

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
   return report

def main():
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

if __name__=="__main__":
    main()