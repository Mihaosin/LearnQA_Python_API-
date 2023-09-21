import requests
import time
import json
from json.decoder import JSONDecodeError
#
# response = requests.post("http://sms.integration.cas.local/api/v1/domains/31028000001398/repeat")
# print(response.status_code, response.text)

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
print(response.status_code, response.text)

obj = json.loads(response.text)

try:
    parsed_response_text =obj()
    print(parsed_response_text)
except JSONDecodeError:
    print("Not json format")

time.sleep(16)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":"gNxoDNxoDNxACMy0SOw0yMyAjM"})
print(response.status_code, response.text)