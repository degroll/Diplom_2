import pytest
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods

@pytest.fixture
def user_methods():
    return UserMethods()

@pytest.fixture
def order_methods():
    return OrderMethods()

@pytest.fixture
def ingredient_ids(order_methods):
    return order_methods.get_ingredient_ids(count=3)

@pytest.fixture
def existing_users(user_methods):
    users = []
    for i in range(3):
        user_data = user_methods.generate_random_user()
        response = user_methods.register_user(user_data)
        user_info = {
            "email": user_data["email"],
            "password": user_data["password"],
            "name": user_data["name"],
            "accessToken": response.json()["accessToken"],
            "refreshToken": response.json()["refreshToken"]
        }
        users.append(user_info)

    yield users

    for user in users:
        user_methods.delete_user(user["accessToken"])
