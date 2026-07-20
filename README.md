# Agentic-AI

A simple AI agent project with a Streamlit frontend that uses OpenAI and utility tools.

## Deployment on Vercel

1. Push this repository to GitHub.
2. Ensure `requirements.txt` and `vercel.json` exist in the project root.
3. In Vercel, import the GitHub repository and select this project.
4. Vercel will install dependencies from `requirements.txt`.
5. The app entrypoint is `frontend.py`.

## Local setup

1. python -m venv .venv
2. .venv\Scripts\activate
3. pip install -r requirements.txt
4. streamlit run frontend.py

## Notes

- `vercel.json` routes all traffic to `frontend.py`.
- Set `OPENAI_API_KEY` in your environment before running the app.
- Optionally create a `.env` file in the project root with:
  ```
  OPENAI_API_KEY=your_api_key_here
  ```
- For local development, use:
  - Windows PowerShell:
    `setx OPENAI_API_KEY "your_api_key_here"`
  - macOS/Linux:
    `export OPENAI_API_KEY="your_api_key_here"`
- For Vercel, add `OPENAI_API_KEY` to the project Environment Variables in the Vercel dashboard.
- You can optionally override `OPENAI_BASE_URL` and `OPENAI_MODEL_NAME` via environment variables.
