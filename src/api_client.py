"""
Consulta a API CoinGecko. Tentativa de 5 vezes (com espera de 2s) para obter os dados das maiores criptomoedas.  
Em caso de sucesso, devolve uma lista de dicionários contendo principais métricas.

"""

import time
import logging
import requests
from requests.exceptions import RequestException, HTTPError, Timeout
from src.config import API_BASE, MAX_ATTEMPTS, WAIT_SECONDS, LIMIT_ASSETS


class CryptoAPI:
    def __init__(self, max_attempts: int = 5, wait_seconds: int = 2) -> None:
        self.base = API_BASE
        self.max_attempts = MAX_ATTEMPTS
        self.wait_seconds = WAIT_SECONDS
        self.logger = logging.getLogger(__name__)

    def get_assets(self) -> list[dict]:
        """
        Tenta obter dados até max_attempts vezes.
        Entre tentativas aguarda wait_seconds.
        """
        url = f"{self.base}/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": LIMIT_ASSETS,
            "page": 1,
            "sparkline": "false",
        }

        attempt = 1
        while attempt <= self.max_attempts:
            try:
                resp = requests.get(url, params=params, timeout=10)
                resp.raise_for_status()
                break  # sucesso
            except (HTTPError, Timeout, RequestException) as exc:
                if attempt == self.max_attempts:
                    raise RuntimeError(
                        f"Falha após {self.max_attempts} tentativas: {exc}"
                    ) from exc

                self.logger.warning(
                    "API indisponível (tentativa %d/%d). Aguardando %d s…",
                    attempt,
                    self.max_attempts,
                    self.wait_seconds,
                )
                time.sleep(self.wait_seconds)
                attempt += 1

        # mapeia resposta
        data = []
        for coin in resp.json():
            data.append(
                {
                    "id": coin["id"],
                    "symbol": coin["symbol"],
                    "name": coin["name"],
                    "priceUsd": coin["current_price"],
                    "marketCapUsd": coin["market_cap"],
                    "volumeUsd24Hr": coin["total_volume"],
                }
            )
        return data
