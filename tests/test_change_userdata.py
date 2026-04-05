import pytest
import allure
from data import SHOULD_BE_AUTH
from helpers import generate_random_email, generate_random_string


class TestChangeUserdata:
    @allure.title("Тест: Изменить эл. почту с регистрацией")
    @allure.description("Пользователи создаются и перебираются")
    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_change_email_userdata_with_auth(self, index, user_methods, existing_users):
        user = existing_users[index]
        new_email = generate_random_email(6)
        update_data = {
            "email": new_email
        }
        response = user_methods.change_userdata(user["accessToken"], update_data)
        assert response.status_code == 200
        assert response.json()["user"]["email"] == new_email
        assert response.json()["success"] == True
        assert response.json()["user"]["name"] == user["name"]

    @allure.title("Тест: Изменить имя с регистрацией")
    @allure.description("Пользователи создаются и перебираются")
    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_change_name_userdata_with_auth(self, index, user_methods, existing_users):
        user = existing_users[index]
        new_name = generate_random_string(6)
        update_data = {
            "name": new_name
        }
        response = user_methods.change_userdata(user["accessToken"], update_data)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == new_name
        assert response.json()["success"] == True
        assert response.json()["user"]["email"] == user["email"]

    @allure.title("Тест: Изменить эл. почту и имя с регистрацией")
    @allure.description("Пользователи создаются и перебираются")
    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_change_email_and_name_userdata_with_auth(self, index, user_methods, existing_users):
        user = existing_users[index]
        new_name = generate_random_string(6)
        new_email = generate_random_email(6)
        update_data = {
            "name": new_name,
            "email": new_email
        }
        response = user_methods.change_userdata(user["accessToken"], update_data)
        assert response.status_code == 200
        assert response.json()["user"]["name"] == new_name
        assert response.json()["success"] == True
        assert response.json()["user"]["email"] == new_email

    @allure.title("Тест: Нельзя изменить даные без регистрации")
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_change_data_without_auth(self, field, user_methods):
        data = generate_random_string(7)
        update_data = {
            field: data
        }
        response = user_methods.change_userdata(None, update_data)
        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == SHOULD_BE_AUTH


