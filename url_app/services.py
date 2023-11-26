# url_app/services.py
import requests
import logging

# class URLShortenerService:
#     BASE_URL = 'https://cleanuri.com/api/v1/shorten'

#     @classmethod
#     def shorten_url(cls, original_url):
#         data = {'url': original_url}
#         response = requests.post(cls.BASE_URL, data=data)
        
#         try:
#             data = response.json()
#         except ValueError as e:
#             cls.handle_error(response, {"error": "Invalid JSON response"})
#             return None
        
#         if response.status_code == 200 and data.get('result_url', None):
#             return data['result_url']
#         else:
#             # Handle error
#             cls.handle_error(response, data)
#             return None

class URLShortenerService:
    BASE_URL = 'https://api.tinyurl.com/create'
    API_KEY = 'eSb7grmlsfiRxG7n03LKFXsIbr6lldCkY24mnrsizeBgkJsInT7rwxoPaZGt'

    @classmethod
    def shorten_url(cls, original_url):
        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {cls.API_KEY}',
            'Content-Type': 'application/json',
        }

        data = {
            'url': original_url,
            'domain': 'tinyurl.com',
            'description': 'string',
        }

        response = requests.post(cls.BASE_URL, headers=headers, json=data)

        if response.status_code == 200:
            result_url = response.json()['data']['tiny_url']
            return result_url
        else:
            # Handle error
            cls.handle_error(response)
            return None

    @classmethod
    def handle_error(cls, response):
        # Log the error
        logger = logging.getLogger(__name__)
        logger.error(f"Error occurred while shortening URL. Status code: {response.status_code}. Response data: {response.text}")

        # Optionally, you can raise a custom exception
        # raise ShorteningError("Failed to shorten URL")


    
    # @classmethod
    # def handle_error(cls, response, data):
    #     logger = logging.getLogger(__name__)
    #     logger.error(f"Error occurred while shortening URL. Status code: {response.status_code}. Response data: {data}")