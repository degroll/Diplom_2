import pytest
import allure
from data import SHOULD_BE_AUTH


class TestGetOrders:
    @allure.title("Тест: Получение заказов пользователя")
    def test_get_orders_certain_user_with_auth(self, order_methods, existing_users, ingredient_ids):
        user = existing_users[0]
        order_methods.create_order(user["accessToken"], ingredient_ids)
        response = order_methods.get_user_orders(user["accessToken"])
        assert response.status_code == 200
        assert response.json()["success"] == True
        assert "orders" in response.json()

    @allure.title("Тест: Нельзя получить заказы пользователя без авторизации")
    def test_get_orders_certain_user_without_auth(self, order_methods):
        response = order_methods.get_user_orders("")
        assert response.status_code == 401
        assert response.json()["success"] == False
        assert response.json()["message"] == SHOULD_BE_AUTH
