import requests

class Test_cookie_hw:
    def test_cookie_hw(self):
        expected_cookie_name = "HomeWork"
        expected_cookie_value = "hw_value"

        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookies = response.cookies

        assert expected_cookie_name in cookies, f"There is no cookie {expected_cookie_name} in the response"

        cookie_value = response.cookies.get(expected_cookie_name)

        assert expected_cookie_value == cookie_value, f"Wrong value {cookie_value} in {expected_cookie_name}"
        print()
        print(expected_cookie_value, expected_cookie_name)


