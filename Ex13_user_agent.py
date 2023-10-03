import requests
import json
import pytest

class Test_user_agent:
    all_data = [
        {
            "User Agent": 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30',
            'platform': 'Mobile',
            'browser': 'No',
            'device': 'Android',
            'test_number': 'User Agent №1'
        },
        {
            "User Agent": 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1',
            'platform': 'Mobile',
            'browser': 'Chrome',
            'device': 'iOS',
            'test_number': 'User Agent №2'
        },
        {
            "User Agent": 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
            'platform': 'Googlebot',
            'browser': 'Unknown',
            'device': 'Unknown',
            'test_number': 'User Agent №3'
        },
        {
            "User Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0',
            'platform': 'Web',
            'browser': 'Chrome',
            'device': 'No',
            'test_number': 'User Agent №4'
        },
        {
            "User Agent": 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'platform': 'Mobile',
            'browser': 'No',
            'device': 'iPhone',
            'test_number': 'User Agent №5'
        }
    ]

    @pytest.mark.parametrize('input', all_data)
    def test_user_agent(self, input):
        user_agent = input["User Agent"]
        expected_platform = input["platform"]
        expected_browser = input["browser"]
        expected_device = input["device"]
        test_number = input["test_number"]

        response = requests.get("https://playground.learnqa.ru/ajax/api/user_agent_check", headers={"User-Agent": user_agent})
        json_value = response.json()
        actual_platform = json_value["platform"]
        actual_browser = json_value["browser"]
        actual_device = json_value["device"]

        if expected_platform != actual_platform:
            print(test_number, "Неправильный параметр PLATFORM")
        elif expected_browser != actual_browser:
            print(test_number, "Неправильный параметр BROWSER")
        elif expected_device != actual_device:
            print(test_number, "Неправильный параметр DEVICE")
        # else:
        #     print(test_number,"Все параметры совпадают")


        # print(".")
        # print()
        # print(input["test_number"], input["User Agent"][0:20])
        # print(expected_platform, expected_browser, expected_device)
        # print(actual_platform, actual_browser, actual_device)

