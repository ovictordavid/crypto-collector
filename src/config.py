"""
Carrega variáveis de ambiente.
Parâmetro do banco de dados DB_PATH.
Parâmetros para uso da API.

"""
import os
from dotenv import load_dotenv

load_dotenv()

# Banco de dados
DB_PATH = os.getenv("DB_PATH")
LIMIT_ASSETS = int(os.getenv("LIMIT_ASSETS", 50))

if not DB_PATH:
    raise RuntimeError("Faltou configurar DB_PATH no .env")

# API
API_BASE = os.getenv("API_BASE", "https://api.coingecko.com/api/v3")
MAX_ATTEMPTS = int(os.getenv("MAX_ATTEMPTS", "5"))  
WAIT_SECONDS = int(os.getenv("WAIT_SECONDS", "2"))  