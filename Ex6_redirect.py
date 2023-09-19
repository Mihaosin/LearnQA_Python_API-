import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
# first_response = response.history[0]
# second_response = response

print("Number of redirects is", len(response.history)-1)


redirects_number = len(response.history)
for i in (0, redirects_number-1):
    print(i, response.history[i].url)