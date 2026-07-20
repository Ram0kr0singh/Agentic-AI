import os

API_KEY = os.environ.get("OPENAI_API_KEY", "")
BASE_URL = os.environ.get("OPENAI_BASE_URL", "https://api.groq.com/openai/v1")
MODEL_NAME = os.environ.get("OPENAI_MODEL_NAME", "llama-3.3-70b-versatile")
