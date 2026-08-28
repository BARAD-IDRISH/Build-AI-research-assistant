def create_research_prompt(company: str, search_results: list) -> str:

    sources_text = ""

    for i, result in enumerate(search_results, start=1):

        sources_text += f"""
SOURCE {i}

Title:
{result.get("title", "")}

URL:
{result.get("url", "")}

Content:
{result.get("content", "")}

----------------------------------------
"""

    prompt = f"""
You are an expert business research analyst.

The user wants research about:

{company}

You have been provided with web search results.

Your job is to analyze ONLY the information supported by these sources.

IMPORTANT RULES:

1. Do not invent facts.
2. Do not use your internal knowledge to add unsupported factual claims.
3. Every important factual claim must be supported by one or more provided sources.
4. Prefer primary and authoritative sources over secondary sources.
5. For company information, prefer official company sources.
6. For pricing, prefer official pricing documentation.
7. For financial information, prefer official investor relations documents or regulatory filings.
8. If reliable information is unavailable, explicitly say "Information not available in the provided sources."
9. If sources disagree, mention the disagreement rather than choosing a value without explanation.
10. Do not assume that a search result is correct simply because it appears in the search results.
11. Do not create URLs yourself.
12. Use the exact URLs provided in the search results.
13. Only include sources that were actually used in the analysis.

RESEARCH TOPIC:

{company}

WEB SEARCH RESULTS:

{sources_text}

Create a professional research report containing:

1. Company / Topic
2. Industry
3. Executive Summary
4. Products / Services
5. Business Model
6. Competitors
7. Competitive Advantages
8. Opportunities
9. Risks
10. Sources

The report should be factual, concise, and based on the provided web sources.
"""

    return prompt