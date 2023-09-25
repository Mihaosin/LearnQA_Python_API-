import requests

class TestFirstAPI:
    def test_hello_call(selfs):
        url = "https://playground.learnqa.ru/api/hello"
        name = 'Mihail'
        data = {'name':name}

        responce = requests.get(url, params=data)

        assert responce.status_code == 200, "Wrong responce cod"

        responce_dict = responce.json()
        assert "answer" in responce_dict, "There is no field 'answer' in the responce"

        expected_responce_text = f"Hello, {name}"
        actual_responce_text = responce_dict["answer"]
        assert actual_responce_text == expected_responce_text, "Actual text in the responce is not correct"
