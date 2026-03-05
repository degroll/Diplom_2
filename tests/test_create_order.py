import pytest
import allure
from data import NO_INGREDIENTS, INVALID_INGREDIENTS


class TestCreateOrder:
    @allure.title("Тест: Создание заказа с регистрацией")
    @allure.description("Пользователи создаются и перебираются")
    @pytest.mark.parametrize("index", [0, 1, 2])
    def test_create_order_with_auth(self, index, existing_users, order_methods, ingredient_ids):
        user = existing_users[index]
        response = order_methods.create_order(user["accessToken"], ingredient_ids)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "name" in response.json()
        assert "order" in response.json()

    @allure.title("Тест: Создание заказа без регистрации")
    def test_create_order_without_auth(self, order_methods, ingredient_ids):
        response = order_methods.create_order(None, ingredient_ids)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "name" in response.json()
        assert "order" in response.json()

    @allure.title("Тест: Создание заказа с различными ингредиентами")
    @allure.description("Различное количество ингредиентов")
    @pytest.mark.parametrize("count", [1, 2, 3, 4])
    def test_create_order_with_different_ingredients(self, count, existing_users, order_methods):
        user = existing_users[0]
        ingredient_ids = order_methods.get_ingredient_ids(count)
        response = order_methods.create_order(user["accessToken"], ingredient_ids)
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert len(response.json()["order"]["ingredients"]) == count

    @allure.title("Тест: Нельзя создать заказ без ингредиентов")
    @allure.description("Различное количество ингредиентов")
    def test_create_order_without_ingredients(self, existing_users, order_methods):
        user = existing_users[0]
        response = order_methods.create_order(user["accessToken"], None)
        assert response.status_code == 400
        assert response.json()["success"] == False
        assert response.json()["message"] == NO_INGREDIENTS

    @allure.title("Тест: Нельзя создать заказ с неправильным хэшем ингредиента")
    def test_create_order_with_invalid_ingredient_hash(self, order_methods, existing_users):
        user = existing_users[0]
        response = order_methods.create_order(user["accessToken"], INVALID_INGREDIENTS)
        assert response.status_code == 500


