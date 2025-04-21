"""
Carrega variáveis de ambiente.
Só exige DB_PATH; deixa API_* opcionais para escolher outro provedor depois.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Banco de dados
DB_PATH = os.getenv("DB_PATH")

# Provedor de dados (coingecko ou coincap)
API_PROVIDER = os.getenv("API_PROVIDER", "coingecko").lower()

# Variáveis opcionais por provedor
COINCAP_API_URL = os.getenv("COINCAP_API_URL")
COINCAP_API_KEY = os.getenv("COINCAP_API_KEY")
COINGECKO_API_URL = os.getenv("COINGECKO_API_URL", "https://api.coingecko.com/api/v3")

if not DB_PATH:
    raise RuntimeError("Faltou configurar DB_PATH no .env")
