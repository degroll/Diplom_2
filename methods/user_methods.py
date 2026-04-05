import requests
import allure
from helpers import generate_random_string, generate_random_email
from urls import BASE_URL, AUTH_ENDPOINT, CREATE_USER, LOGIN_USER


class UserMethods:
    @allure.step("Генерируем нового пользователя")
    def generate_random_user(self):
        email = generate_random_email(6)
        password = generate_random_string(7)
        name = generate_random_string(6)

        payload = {
        "email": email,
        "password": password,
        "name": name
        }
        return payload
    
    @allure.step("Регистрируем нового пользователя")
    def register_user(self, user_data):
        response = requests.post(f"{BASE_URL}{CREATE_USER}", json=user_data)
        return response
    
    @allure.step("Авторизуем пользователя")
    def login_user(self, user_data):
        response = requests.post(f"{BASE_URL}{LOGIN_USER}", json=user_data)
        return response
    
    @allure.step("Удаляем пользователя")
    def delete_user(self, access_token):
        headers = {'Authorization': f'{access_token}'}
        return requests.delete(f'{BASE_URL}{AUTH_ENDPOINT}', headers=headers)
    
    @allure.step("Меняем данные пользователя")
    @allure.description("Определённые данные передаются в качестве аргумента")
    def change_userdata(self, access_token, update_data):
        headers = {'Authorization': f'{access_token}'}
        response = requests.patch(f'{BASE_URL}{AUTH_ENDPOINT}', headers=headers, json=update_data)
        return response
    
    

    