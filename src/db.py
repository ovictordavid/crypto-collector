import os
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models import Base, Cryptocurrency, MarketData
from src.config import DB_PATH

# Aqui é feito a criação do engine SQLite (arquivo local)
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def upsert_crypto(session, data):
    obj = session.get(Cryptocurrency, data["id"])
    if not obj:
        obj = Cryptocurrency(id=data["id"], symbol=data["symbol"], name=data["name"])
        session.add(obj)
    return obj

def insert_market_data(session, crypto_obj, metrics):
    md = MarketData(
        crypto_id=crypto_obj.id,
        price_usd=float(metrics["priceUsd"]),
        market_cap_usd=float(metrics["marketCapUsd"]),
        volume_usd_24h=float(metrics["volumeUsd24Hr"]),
        timestamp=datetime.utcnow()
    )
    session.add(md)
