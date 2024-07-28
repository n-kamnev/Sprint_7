import allure
from faker import Faker
import random
import requests
import data
import urls


class CourierFactory:
    @staticmethod
    @allure.step("Генерация тела для создания курьера")
    def generation_new_courier():
        fake = Faker()
        login = f"courier{str(random.randint(1, 99999))}"
        password = fake.password()
        name = fake.name()
        return {"login": login, "password": password, "firstName": name}

    @staticmethod
    @allure.step("Подмена авторизационных данных")
    def modify_create_courier(key, value):
        body = data.TestDataCreateCourier.CREATE_COURIER_BODY.copy()
        body[key] = value
        return body

    @staticmethod
    @allure.step("Генерация логина курьера")
    def generate_courier_login():
        login = f"terminator{str(random.randint(1, 99999))}"
        return login

    @staticmethod
    @allure.step("Генерация тела для создания курьера и возврат логина и пароля")
    def create_new_courier_and_return_login_password():
        fake = Faker()
        login = f"courier{str(random.randint(1, 99999))}"
        password = fake.password()
        name = fake.name()
        payload = {"login": login, "password": password, "firstName": name}
        requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, data=payload)
        return payload
