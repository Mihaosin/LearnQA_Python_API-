from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions


class TestUserEdit(BaseCase):
    # def test_del_user_2(self):
    #     login_data = {
    #         'email': 'vinkotov@example.com',
    #         'password': '1234'
    #     }
    #     response1 = MyRequests.post("/user/login", data=login_data)
    #
    #     auth_sid = self.get_cookie(response1, "auth_sid")
    #     token = self.get_header(response1, "x-csrf-token")
    #     user_id = self.get_json_value(response1, "user_id")
    #
    #     Assertions.assert_code_status(response1, 200)
    #
    #     # DELETE
    #     response2 = MyRequests.delete(
    #         f"/user/{user_id}",
    #         headers={"x-csrf-token": token},
    #         cookies={"auth_sid": auth_sid}
    #     )
    #
    #     print(response2.content)
    #     Assertions.assert_code_status(response2, 400)
    #     assert response2.content.decode("utf-8") == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."


    # def test_del_user_by_id(self):
    #     # REGISTER
    #     register_data = self.prepare_registration_data()
    #     response1 = MyRequests.post("/user/", data=register_data)
    #
    #     Assertions.assert_code_status(response1, 200)
    #     Assertions.assert_json_has_key(response1, "id")
    #
    #     email = register_data["email"]
    #     first_name = register_data["firstName"]
    #     password = register_data["password"]
    #     user_id = self.get_json_value(response1, "id")
    #
    #     # LOGIN
    #     login_data = {
    #         'email': email,
    #         'password': password
    #     }
    #     response2 = MyRequests.post("/user/login", data=login_data)
    #
    #     auth_sid = self.get_cookie(response2, "auth_sid")
    #     token = self.get_header(response2, "x-csrf-token")
    #
    #     Assertions.assert_code_status(response2, 200)
    #
    #     # DELETE
    #     response3 = MyRequests.delete(
    #         f"/user/{user_id}",
    #         headers={"x-csrf-token": token},
    #         cookies={"auth_sid": auth_sid}
    #     )
    #
    #     Assertions.assert_code_status(response3, 200)
    #
    #     response4 = MyRequests.post("/user/login", data=login_data)
    #     print(response4.text)
    #     Assertions.assert_code_status(response4, 400)

    # def test_del_user_by_wrong_id(self):
    #     # REGISTER
    #     register_data = self.prepare_registration_data()
    #     response1 = MyRequests.post("/user/", data=register_data)
    #
    #     Assertions.assert_code_status(response1, 200)
    #     Assertions.assert_json_has_key(response1, "id")
    #
    #     email = register_data["email"]
    #     first_name = register_data["firstName"]
    #     password = register_data["password"]
    #     user_id = self.get_json_value(response1, "id")
    #
    #     # LOGIN
    #     login_data = {
    #         'email': email,
    #         'password': password
    #     }
    #     response2 = MyRequests.post("/user/login", data=login_data)
    #
    #     auth_sid = self.get_cookie(response2, "auth_sid")
    #     token = self.get_header(response2, "x-csrf-token")
    #
    #     Assertions.assert_code_status(response2, 200)
    #
    #     # DELETE
    #     response3 = MyRequests.delete(
    #         f"/user/{user_id}",
    #         headers={"x-csrf-token": token},
    #         cookies={"auth_sid": auth_sid}
    #     )
    #
    #     Assertions.assert_code_status(response3, 200)
    #
    #     response4 = MyRequests.post("/user/login", data=login_data)
    #     print(response4.text)
    #     Assertions.assert_code_status(response4, 400)

    def test_del_another_user_id(self):
        # REGISTER
        register_data = self.prepare_registration_data()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")
        print(user_id)

        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        Assertions.assert_code_status(response2, 200)

        # DELETE
        response3 = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        print(response3.text)
        Assertions.assert_code_status(response3, 400)
        assert response3.content.decode("utf-8") == f"Invalid username/password supplied"