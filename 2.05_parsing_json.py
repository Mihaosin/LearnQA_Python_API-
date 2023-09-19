import json

sting_as_json_format = '{"answer": "Hello, User"}'
obj = json.loads(sting_as_json_format)

key = "answer2"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} в JSON нет")