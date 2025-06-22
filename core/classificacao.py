import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Carrega a chave da API
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai_client = genai.Client(api_key=api_key)

def classificar_centro_custo(texto, prompt_template):
    """
    Classifica uma descrição de despesa no centro de custo mais apropriado
    usando a API Gemini do Google.

    Args:
        texto (str): descrição da despesa
        prompt_template (str): template do prompt com {texto}

    Returns:
        str: centro de custo sugerido ou "Erro IA"
    """
    prompt = prompt_template.replace("{texto}", texto)
    try:
        resposta = genai_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0)
            )
        )
        return resposta.text.strip().title()
    except Exception:
        return "Erro IA"
