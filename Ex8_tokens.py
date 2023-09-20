import requests
import json
import time

print()
print("Шаг №1: Создание задачи")
response1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")

response1_text = json.loads(response1.text)
seconds = response1_text["seconds"]
token = response1_text["token"]
print(response1.status_code, seconds, token)

print()
print("Шаг №2: Запрос до завершения задачи")
response2 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token})
response2_text = json.loads(response2.text)
status2 = response2_text["status"]
print(response2.status_code, status2)
if status2 != "Job is NOT ready":
    print("Ошибочный статус!")

print()
print("Шаг №3: Ожидание")
time.sleep(seconds)

print()
print("Шаг №4: Запрос после завершения задачи")
response3 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token})
response3_text = json.loads(response3.text)
status3 = response3_text["status"]
if status3 == "Job is ready":
    result3 = response3_text["result"]
else:
    print("Ошибочный статус!")
    result3 = "None"
print(response3.status_code, status3, "результат =", result3)


