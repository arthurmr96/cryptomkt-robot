import helpers
import requests

request = requests.get('https://api.cryptomkt.com/v1/balance')

request = helpers.set_request_authentication(request, '/v1/balance')

print(request.json())