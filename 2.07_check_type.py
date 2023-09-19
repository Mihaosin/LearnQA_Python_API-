import requests

response = requests.get("https://playground.learnqa.ru/api/check_type", params={"params1":"value1"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/api/check_type", data={"params1":"value1"})
print(response.text)