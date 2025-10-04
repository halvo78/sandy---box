
from cachetools import cached, TTLCache
import requests

@cached(cache=TTLCache(maxsize=1024, ttl=60))
def get_polygon_data(url):
    return requests.get(url)

