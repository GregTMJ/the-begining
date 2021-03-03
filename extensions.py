import json
import requests
from Config import exchanger



class ConvertionException(Exception):
    pass

class Converter:
    @staticmethod
    def convert(quote = str, base = str, amount = str):

        if quote == base:
            raise ConvertionException("Невозможно переводить"
                                      "одинаковые валюты!")
        try:
            quote_ticker = exchanger[quote]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать "
                                      f"валюту {quote}")

        try:
            base_ticker = exchanger[base]
        except KeyError:
            raise ConvertionException(f"Не удалось обработать"
                                      f"валюту {base}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f"Неправильно введено количество"
                                      f"{amount}")

        r = requests.get(f'https://min-api.cryptocompare.com/'
                         f'data/price?fsym={quote_ticker}&'
                         f'tsyms={base_ticker}')
        total_base = json.loads(r.content)[exchanger[base]]
        total_amount = round((total_base)*float(amount), 2)

        return total_amount
        return total_base

