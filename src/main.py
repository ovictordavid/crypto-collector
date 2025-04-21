""""
Camada principal do programa para integrar a conexão da api e obter os dados atualizados
a serem inseridos no banco de dados.

"""
import os
import logging
import pytest
from src.api_client import CryptoAPI
from src.db import init_db, Session, upsert_crypto, insert_market_data
from src.config import LIMIT_ASSETS

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def run_tests() -> None:
    #Executa pytest para verificar a consistência e integridade do pipeline
    if os.getenv("RUN_TESTS", "true").lower() in {"true", "1"}:
        logger.info("Executando testes unitários…")
        retcode = pytest.main(["-q", "tests"])
        if retcode != 0:
            raise SystemExit(f"Falha nos testes (pytest retornou {retcode})")
        logger.info("Testes passaram com sucesso.")

def run_pipeline():
    init_db()
    api = CryptoAPI()
    session = Session()

    try:
        # Busca apenas as top criptomoedas
        assets = api.get_assets()
        for item in assets:
            crypto = upsert_crypto(session, item)
            insert_market_data(session, crypto, item)
        session.commit()
        logger.info(f"Top {LIMIT_ASSETS} criptomoedas coletadas com sucesso.")
    except Exception as e:
        session.rollback()
        logger.error("Coleta falhou: %s", e)
    finally:
        session.close()

if __name__ == "__main__":
    run_tests()
    run_pipeline()
