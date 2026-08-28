import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("TAVILY_API_KEY is not set in the environment variables.") 

tavily=TavilyClient(api_key=api_key)

def search_web(query:str) -> str:
    response=tavily.search(
        query=query,
        search_depth="advanced",
        max_results=5,
        )
    return response["results"]


if __name__=="__main__":
    results=search_web("google company business")
    for result in results:
        print(f"Title: {result['title']}")
        print(f"URL: {result['url']}")
        print(f"Content: {result['content'][:500]}\n")
        print("="*50)
        
