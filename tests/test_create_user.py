import pytest
import allure
from data import EXISTING_USER, NO_REQUIRED_FIELDS


class TestCreateUser:
    @allure.title("Тест: Создание пользователя")
    def test_can_create_new_user(self, user_methods):
        data = user_methods.generate_random_user()
        response = user_methods.register_user(data)
        assert response.status_code == 200
        assert response.json()["success"] == True
        access_token = response.json()["accessToken"]
        user_methods.delete_user(access_token)

    @allure.title("Тест: Нелья создать существующего пользователя")
    def test_cannot_create_existed_user(self, user_methods):
        response = user_methods.register_user(EXISTING_USER)
        assert response.status_code == 403
        assert response.json()["success"] == False

    @allure.title("Тест: Нелья создать пользователя без параметра")
    @allure.description("Варианты параметра перебираются")
    @pytest.mark.parametrize('field', ['email', 'password', 'name'])
    def test_cannot_create_user_without_field(self, field, user_methods):
        data = user_methods.generate_random_user()
        del data[field]
        response = user_methods.register_user(data)
        assert response.status_code == 403
        assert response.json()["message"] == NO_REQUIRED_FIELDS 

