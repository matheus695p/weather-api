import json
import requests

# lectura del api key
with open('keys.json') as json_file:
    dict_ = json.load(json_file)
    YOUR_ACCESS_KEY = dict_["weatherstack"]
    print(YOUR_ACCESS_KEY)

# params del request
params = {
    'access_key': YOUR_ACCESS_KEY,
    'query': 'Tierra Amarilla Chile'
}
# consulta
api_result = requests.get('http://api.weatherstack.com/current', params)
# respuesta
api_response = api_result.json()
print(api_response)
