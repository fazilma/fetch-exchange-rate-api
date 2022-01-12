from json.decoder import JSONDecodeError
import requests
import environ
from .models import ExchangeRate

env = environ.Env()
environ.Env.read_env()


def fetch_rate():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey={}'.format(env('API_KEY'))
    r = requests.get(url)
    data = r.json()
    try:
        real_time_rate = data['Realtime Currency Exchange Rate']
        model=ExchangeRate.objects.create(from_currency_code = real_time_rate['1. From_Currency Code'],
                    to_currency_code = real_time_rate['3. To_Currency Code'],
                    exchange_rate = real_time_rate['5. Exchange Rate'],
                    updated_at = real_time_rate['6. Last Refreshed'])
    
    except Exception as e:
        print(e)
    
    return model