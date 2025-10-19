import asyncio
import json
import google.generativeai as genai

from types import SimpleNamespace
from dotenv import load_dotenv
import os


# Abre e carrega o arquivo JSON
with open("prompt.json", "r", encoding="utf-8") as f:
    PROMPTS = json.load(f, object_hook=lambda d: SimpleNamespace(**d))

load_dotenv()

# Inicia o Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
geminiIA = genai.GenerativeModel("gemini-2.5-flash")

# Funções do Gemini
# Realiza um prompt
async def promptGemini(prompt, max_tokens=200):
    resposta = await asyncio.to_thread(geminiIA.generate_content, prompt)
    texto = resposta.text.strip() if resposta and hasattr(resposta, "text") else ""
    return texto
