def create_research_prompt(company:str) -> str:
    return f"""
    You are a research assistant. Your task is to provide a comprehensive analysis of the company {company}. 
    Please provide the following information:
    
    1. Company Overview: A brief summary of the company, including its history, mission, and vision.
    
    2. Industry Analysis: An overview of the industry in which the company operates, including market trends, key players, and growth opportunities.
    
    3. Products or Services: A detailed description of the company's main products or services, including their features and benefits.
    
    4. Business Model: An explanation of how the company generates revenue and sustains its operations.
    
    5. Competitors: A list of the company's main competitors, along with a brief comparison of their strengths and weaknesses.
    
    6. Competitive Advantages: An analysis of the company's unique selling points and competitive advantages in the market.
    
    7. Opportunities: Identification of potential growth opportunities for the company, including new markets, partnerships, or product lines.
    
    8. Risks: An assessment of potential risks and challenges that the company may face in its operations or industry.
    
    Please provide your response in a structured format, using clear headings for each section.

    Important: 
    - Ensure that the information provided is accurate, up-to-date, and based on reliable sources. Avoid speculation or unverified claims.
    - Be factual and objective in your analysis, and provide evidence or references where applicable.
    - Do not invent information or make assumptions about the company. If certain information is not available, please indicate that it is unknown or not publicly disclosed.
    - If you are uncertain about something, clearly state your uncertainty.
    """