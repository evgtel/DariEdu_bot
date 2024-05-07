import requests
import json
from config import currency
class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: str):


        if base == quote:
            raise APIException("Перевод одинаковых валют.")

        try:
            from_ticker = currency[base]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {base}.")

        try:
            to_ticker = currency[quote]
        except KeyError:
            raise APIException(f"Не удалось обработать валюту {quote}.")

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f"Не удалось обработать количество {amount}.")

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={from_ticker}&tsyms={to_ticker}')
        total_base = float(json.loads(r.content)[to_ticker]) * amount
        return total_base
