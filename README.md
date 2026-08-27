Day01 — Research Assistant
===========================

A small command-line research assistant that generates a structured company research report using a generative model.

Key features
- Prompts a large language model (via the `genai` client) to create a research report for a given company
- Validates and parses the model response into a `ResearchReport` Pydantic model
- Prints a readable, sectioned report to the terminal

Quick overview
- Entry point: `app/main.py` — interactive CLI that asks for a company name and prints the generated report
- Prompt template: `app/prompts.py` — instructs the model to return a structured report (overview, industry, products, business model, competitors, opportunities, risks)
- Data model: `app/schemas.py` — `ResearchReport` Pydantic model used to validate the JSON response

Requirements
- Python 3.10+ recommended
- The environment needs an API key set in `GEMINI_API_KEY` (the code reads it from the environment)
- Minimal dependencies (install with pip):

```bash
pip install python-dotenv pydantic
# If using Google's GenAI client, install the appropriate package, e.g.:
# pip install google-genai
```

Installation
1. Create and activate a virtual environment:

```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# or (cmd)
.\.venv\Scripts\activate
```

2. Install dependencies (see `requirements.txt` or use the inline pip command above).

Configuration
1. Create a `.env` in the project root (or export the variable in your shell) with your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

2. The app loads environment variables with `python-dotenv` (see `app/main.py`).

Usage
Run the CLI:

```bash
python -m app.main
```

Follow the prompt and enter a company name. The script will call the configured model and print a structured research report.

Notes & Implementation details
- The app calls `client.models.generate_content` and requests a JSON response using the Pydantic model schema (`ResearchReport.model_json_schema()`).
- `app/schemas.py` expects lists for `competitors`, `competitive_advantages`, `opportunities`, and `risks` so the model should return arrays for those fields in JSON.
- If the environment variable `GEMINI_API_KEY` is not set, the app raises an error.

Extending or testing
- To adapt the prompt, edit `app/prompts.py`.
- To change the schema, update `app/schemas.py` and the `response_schema` payload in `app/main.py`.

Contributing
- PRs welcome. For small personal projects, keep changes minimal and focused.

License
- MIT-style (add a LICENSE file if you want to publish this project).

