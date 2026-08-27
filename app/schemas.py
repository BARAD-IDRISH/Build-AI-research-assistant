from pydantic import BaseModel

class ResearchReport(BaseModel):
    company:str
    industry:str
    summary:str
    products_or_services:str
    business_model:str
    competitors:list[str]
    competitive_advantages:list[str]
    opportunities:list[str]
    risks:list[str]
