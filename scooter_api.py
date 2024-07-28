import allure
import requests
import urls


class CreateCourierApi:
    @staticmethod
    @allure.step("Отправка запроса на создание курьера")
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)


class AuthCourierApi:
    @staticmethod
    @allure.step("Авторизация курьера")
    def auth_courier(login_pass):
        return requests.post(
            urls.BASE_URL + urls.COURIER_LOGIN_ENDPOINT, json=login_pass
        )

    @staticmethod
    @allure.step("Удаление курьера")
    def delete_courier(id):
        return requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT, json=id)


class CreateOrderApi:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(payload):
        return requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=payload)


class ReceivingOrderList:
    @staticmethod
    @allure.step("Запрос получения списка заказов")
    def receiving_orders_list():
        return requests.get(urls.BASE_URL + urls.RECEIVING_ORDERS_LIST_ENDPOINT)
