import requests
from urllib.parse import urlencode
from pprint import pprint

COUNTER_ID = 'id'
TOKEN = 'yourtoken'


class MetrikaBase:
    API_STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/'
    token = None

    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Authorization': 'OAuth {0}'.format(self.token),
            'Content-Type': 'application/json'
        }


class Counter(MetrikaBase):

    def get_visits(self):
        headers = self.get_headers()
        params = {
            'id': COUNTER_ID,
            'metrics': 'ym:s:visits'
        }
        r = requests.get(self.API_STAT_URL + 'data', params, headers=headers)
        return r.json()['data'][0]['metrics'][0]

    def get_pageviews(self):
        headers = self.get_headers()
        params = {
            'id': COUNTER_ID,
            'metrics': 'ym:s:pageviews'
        }
        r = requests.get(self.API_STAT_URL + 'data', params, headers=headers)
        return r.json()['data'][0]['metrics'][0]

    def get_users(self):
        headers = self.get_headers()
        params = {
            'id': COUNTER_ID,
            'metrics': 'ym:s:users'
        }
        r = requests.get(self.API_STAT_URL + 'data', params, headers=headers)
        return r.json()['data'][0]['metrics'][0]


