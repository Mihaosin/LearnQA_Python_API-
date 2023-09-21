import requests


response = requests.post("http://sms.integration.cas.local/api/v1/domains/31028000001398/repeat")
print(response.status_code, response.text)

