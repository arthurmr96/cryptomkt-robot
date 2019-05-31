import json
import time
import hmac
import hashlib

with open('config.json', 'r') as file:
    config = json.load(file)

def set_request_authentication (request, path_url):
    """"Set headers on a request if it's an authenticated endpoint"""

    timestamp = time.time()
    secret_key = config['secretkey']

    message = str(timestamp) + path_url

    signature = hmac.new(bytes(secret_key, 'utf-8'), bytes(message, 'utf-8'), hashlib.sha384)

    headers = {'X-MKT-APIKEY': config['apikey'],
               'X-MKT-SIGNATURE': signature.hexdigest(),
               'X-MKT-TIMESTAMP': str(timestamp)}

    request.headers.update(headers)

    return request
