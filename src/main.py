import logging
from src.api_client import CryptoAPI
from src.db import init_db, Session, upsert_crypto, insert_market_data

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

def run():
    init_db()
    api = CryptoAPI()
    session = Session()

    try:
        # Busca apenas as top 20 criptomoedas
        assets = api.get_assets(limit=20, offset=0)
        for item in assets:
            crypto = upsert_crypto(session, item)
            insert_market_data(session, crypto, item)
        session.commit()
        logger.info("Top 20 criptomoedas coletadas com sucesso.")
    except Exception as e:
        session.rollback()
        logger.error("Erro durante coleta ou insert: %s", e)
    finally:
        session.close()

if __name__ == "__main__":
    run()
