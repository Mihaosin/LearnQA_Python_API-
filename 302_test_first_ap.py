import requests

class TestFirstAPI:
    def test_hello_call(selfs):
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Mihail'
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Wrong response cod"

        responce_dict = response.json()
        assert "answer" in responce_dict, "There is no field 'answer' in the response"

        expected_responce_text = "Hello, "+name
        actual_responce_text = responce_dict["answer"]
        assert actual_responce_text == expected_responce_text, "Actual text in the response is not correct"
