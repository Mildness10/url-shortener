# url_app/services.py
import requests

class URLShortenerService:
    BASE_URL = 'https://cleanuri.com/api/v1/shorten'

    @classmethod
    def shorten_url(cls, original_url):
        params = {'url': original_url}
        response = requests.get(cls.BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200 and data.get('result_url', None):
            return data['result_url']
        else:
            # Handle error, e.g., log it or raise an exception
            return None
