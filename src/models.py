"""
Definição dos atributos a serem utilizados no banco de dados

"""

from sqlalchemy import (
    Column, String, Float, Integer, DateTime, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Cryptocurrency(Base):
    __tablename__ = "cryptocurrency"
    id     = Column(String, primary_key=True)
    symbol = Column(String, nullable=False)
    name   = Column(String, nullable=False)

class MarketData(Base):
    __tablename__ = "market_data"
    id             = Column(Integer, primary_key=True, autoincrement=True)
    crypto_id      = Column(String, ForeignKey("cryptocurrency.id"), nullable=False)
    price_usd      = Column(Float)
    market_cap_usd = Column(Float)
    volume_usd_24h = Column(Float)
    timestamp      = Column(DateTime)
