import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Cryptocurrency, MarketData
from src.db import upsert_crypto, insert_market_data

#Contexto do teste

@pytest.fixture(scope="function")
def session():
    #Sessão temporária com SQLite em memória.
    engine = create_engine("sqlite:///:memory:", echo=False)
    Base.metadata.create_all(engine)
    SessionLocal = sessionmaker(bind=engine)
    sess = SessionLocal()
    yield sess
    sess.close()

#Casos de teste

def test_upsert_and_snapshot(session):
    #Garante unicidade do asset e integridade da fotografia.
    sample = {
        "id": "bitcoin",
        "symbol": "btc",
        "name": "Bitcoin",
        "priceUsd": 65000.0,
        "marketCapUsd": 1.2e12,
        "volumeUsd24Hr": 3.5e10,
    }

    # 1ª inserção
    crypto = upsert_crypto(session, sample)
    insert_market_data(session, crypto, sample)
    session.commit()

    # 2ª inserção (upsert deve evitar duplicar asset)
    crypto_dup = upsert_crypto(session, sample)
    insert_market_data(session, crypto_dup, sample)
    session.commit()

    #Assertividade
    # Apenas 1 linha em cryptocurrency
    assert session.query(Cryptocurrency).count() == 1

    # Duas linhas em market_data (duas fotogradias distintas)
    assert session.query(MarketData).count() == 2

    # Valores obrigatórios consistentes
    last = session.query(MarketData).order_by(MarketData.id.desc()).first()
    assert last.price_usd > 0
    assert last.crypto_id == "bitcoin"
