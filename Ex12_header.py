import requests

class Test_get_header:
    def test_get_header(self):
        expected_header_name = "x-secret-homework-header"
        expected_header_value = "Some secret value"

        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers = response.headers

        assert expected_header_name in headers, f"There is no header {expected_header_name} in the response"

        header_value = response.headers[expected_header_name]

        assert expected_header_value == header_value, f"Wrong value {header_value} in {expected_header_name}"

        print()
        print(expected_header_value, expected_header_name)
