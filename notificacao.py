import requests
import os
from dotenv import load_dotenv

load_dotenv()
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

def enviar_webhook(dados):
    try:
        response = requests.post(WEBHOOK_URL, json=dados)
        print("\n")
        print("Dados enviados para o n8n!")
    except Exception as err:
        print("\n")
        print(f"Erro ao enviar para o n8n: {err}")