
import requests

def get_binance_data():
    try:
        return requests.get("https://api.binance.com/api/v3/ping", timeout=5)
    except requests.exceptions.RequestException:
        return requests.get("https://api.binance.us/api/v3/ping", timeout=5)
