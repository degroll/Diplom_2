import pytest
import allure
from data import INCORRECT_PARAM


class TestLoginUser:
    @allure.title("Тест: Авторизация существующего пользователя")
    @allure.description("Пользователя создаются и перебираются")
    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_login_existing_user(self, index, user_methods, existing_users):
        user = existing_users[index]
        login_data = {
            "email": user["email"],
            "password": user["password"]
        }
        response = user_methods.login_user(login_data)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert response.json()["user"]["email"] == user["email"]
        assert response.json()["user"]["name"] == user["name"]
        assert "accessToken" in response.json()

    @allure.title("Тест: Авторизация с неправильными данными")
    @allure.description("Пользователя создаются и перебираются, различные варианты данных")
    @pytest.mark.parametrize("index", [0, 1, 2])
    @pytest.mark.parametrize("param", ["email", "password"])
    def test_login_with_wrong_param(self, index, param, user_methods, existing_users):
        user = existing_users[index]
        login_data = {
            "email": user["email"],
            "password": user["password"]
        }
        login_data[param] = 'wrong_param'
        response = user_methods.login_user(login_data)
        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == INCORRECT_PARAM
