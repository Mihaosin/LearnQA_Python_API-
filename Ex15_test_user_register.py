import pytest
from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime
import string
import random



class TestUserRegisration(BaseCase):
    exclude_params = [
        { 'name': 'Without password',
          'data': {
                    'username': 'learnqa',
                    'firstName': 'learnqa',
                    'lastName': 'learnqa',
                    'email': 'mihail@example.com'
                    }
        },
        {'name': 'Without username',
         'data': {
             'password': '123',
             'firstName': 'learnqa',
             'lastName': 'learnqa',
             'email': 'mihail@example.com'
                 }
         },
        {'name': 'Without firstName',
         'data': {
             'password': '123',
             'username': 'learnqa',
             'lastName': 'learnqa',
             'email': 'mihail@example.com'
                 }
         },
        {'name': 'Without lastName',
         'data': {
             'password': '123',
             'username': 'learnqa',
             'firstName': 'learnqa',
             'email': 'mihail@example.com'
                 }
         },
        {'name': 'Without email',
         'data': {
             'password': '123',
             'username': 'learnqa',
             'firstName': 'learnqa',
             'lastName': 'learnqa'
                 }
         }

    ]

    def setup_method(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%S")
        self.email = f"{base_part}{random_part}@{domain}"

    # - Создание пользователя с некорректным email - без символа @
    # def test_create_user_with_wrong_email(self):
    #     email = 'mihail&example.com'
    #     data = {
    #         'password': '123',
    #         'username': 'learnqa',
    #         'firstName': 'learnqa',
    #         'lastName': 'learnqa',
    #         'email': email
    #     }
    #
    #     response = MyRequests.post("/user/", data=data)
    #
    #     Assertions.assert_code_status(response, 400)
    #     assert response.content.decode("utf-8") == "Invalid email format"
    #     print(response.content)

    # - Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить,
    # что отсутствие любого параметра не дает зарегистрировать пользователя
    # @pytest.mark.parametrize('input', exclude_params)
    # def test_create_user_without_required_param(self, input):
    #     name = input["name"]
    #     data = input["data"]
    #
    #     response = MyRequests.post("/user/", data=data)
    #     actual_answer = response.text[0:40]
    #     required_answer = "The following required params are missed"
    #     print(name)
    #     print(response.text)
    #     assert actual_answer == required_answer, "Нет диагностики об отсутствующем параметре"

    # - Создание пользователя с очень коротким именем в один символ
    # def test_create_user_with_short_name(self):
    #     email = 'mihail@example.com'
    #     data = {
    #         'password': '123',
    #         'username': 'learnqa',
    #         'firstName': '1',
    #         'lastName': 'learnqa',
    #         'email': email
    #     }
    #
    #     response = MyRequests.post("/user/", data=data)
    #
    #     Assertions.assert_code_status(response, 400)
    #     assert response.content.decode("utf-8") == "The value of 'firstName' field is too short"
    #     print(response.content)

    # - Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_with_long_name(self):
        characters = string.ascii_lowercase + string.digits
        firstName = ''.join([random.choice(characters) for _ in range(251)])
        email = 'mihail@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': firstName,
            'lastName': 'learnqa',
            'email': email
        }

        response = MyRequests.post("/user/", data=data)

        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "The value of 'firstName' field is too long"
        print(response.content)





