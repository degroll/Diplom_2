import requests
import allure
from urls import BASE_URL, ORDER, INGREDIENTS_ENDPOINT


class OrderMethods:
    @allure.step("Получаем ингредиенты")
    def get_ingredients(self):
        response = requests.get(f"{BASE_URL}{INGREDIENTS_ENDPOINT}")
        return response

    @allure.step("Создаём заказ")
    def create_order(self, access_token, ingredients_ids):
        headers = {'Authorization': f'{access_token}'}
        data = {'ingredients': ingredients_ids}
        response = requests.post(f"{BASE_URL}{ORDER}", headers=headers, json=data)
        return response

    @allure.step("Получаем заказы конкретного пользователя")
    def get_user_orders(self, access_token):
        headers = {'Authorization': f'{access_token}'}
        response = requests.get(f"{BASE_URL}{ORDER}", headers=headers)
        return response

    @allure.step("Получаем id ингредиентов в виде списка")
    def get_ingredient_ids(self, count=2):
        ingredients_response = self.get_ingredients()
        all_ingredients = ingredients_response.json()["data"]
        return [ing["_id"] for ing in all_ingredients[:count]]
    