import helpers
import requests

base_url = 'https://api.cryptomkt.com'

request = requests.get(base_url + '/v1/balance')

request = helpers.set_request_authentication(request, '/v1/balance')

print(request.json())