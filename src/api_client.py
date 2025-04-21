
import requests

class CryptoAPI:
    def __init__(self):
        self.base = "https://api.coingecko.com/api/v3"

    def get_assets(self, limit=20, offset=0):
        url = f"{self.base}/coins/markets"
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": limit,
            "page": 1,
            "sparkline": "false"
        }
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        data = []
        for coin in resp.json():
            data.append({
                "id": coin["id"],
                "symbol": coin["symbol"],
                "name": coin["name"],
                "priceUsd": coin["current_price"],
                "marketCapUsd": coin["market_cap"],
                "volumeUsd24Hr": coin["total_volume"],
            })
        return data
