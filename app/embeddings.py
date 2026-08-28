'''
embedding using gemini-embedding-001 model
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")

client=genai.Client(api_key=api_key)

def create_embedding(text:str):
    response=client.models.embed_content(
        model="gemini-embedding-001",
        contents=text,
    )

    return response.embeddings[0].values
def create_embeddings(texts: list[str]):

    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents=texts,
    )

    return [
        embedding.values
        for embedding in response.embeddings
    ]'''

# creating embedding using sentence-transformers/all-MiniLM-L6-v2 model

from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")


def create_embedding(text: str):

    embedding = model.encode(text)

    return embedding.tolist()


def create_embeddings(texts: list[str]):

    embeddings = model.encode(
        texts,
        show_progress_bar=True
    )

    return embeddings.tolist()


if __name__=="__main__":
    text="Artificial intelligence is a branch of computer science that aims to create machines capable of intelligent behavior."
    vector=create_embedding(text)

    print("vector length:",len(vector))

    print("vector first 10 values:",vector[:10]) 