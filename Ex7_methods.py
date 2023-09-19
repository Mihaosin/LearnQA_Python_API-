import requests

print("пункт 1")
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.status_code, response.text)
print()

print("пункт 2")
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"HEAD"})
print(response.status_code, response.text)
print()

print("пункт 3")
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
print(response.status_code, response.text)
print()

print("пункт 4.1")
methods = ["POST", "GET", "PUT", "DELETE"]
for method in methods:
    response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":method})
    print("POST", method, response.status_code, response.text)
print()

print("пункт 4.2")
methods = ["POST", "GET", "PUT", "DELETE"]
for method in methods:
    response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":method})
    print("GET", method, response.status_code, response.text)
print()

print("пункт 4.3")
methods = ["POST", "GET", "PUT", "DELETE"]
for method in methods:
    response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":method})
    print("PUT", method, response.status_code, response.text)
print()

print("пункт 4.4")
methods = ["POST", "GET", "PUT", "DELETE"]
for method in methods:
    response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":method})
    print("DELETE", method, response.status_code, response.text)
