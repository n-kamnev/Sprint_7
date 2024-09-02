import allure
from scooter_api import CreateOrderApi
import pytest


class TestCreateOrder:
    @allure.step("Проверяем создание нового заказа")
    @allure.description(
        "Создаем новый заказ с разными параметрами цвета, проверяем код ответа и тело ответа"
    )
    @pytest.mark.parametrize(
        "color", [["BLACK", ""], ["GREY", ""], [], ["BLACK", "GREY"]]
    )
    def test_create_order(self, color):
        # Метода удаления для заказов в документации нет
        payload = {
            "firstName": "Егор",
            "lastName": "Чистоплюев",
            "address": "Коломна",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 50,
            "deliveryDate": "2024-08-06",
            "comment": "Комментарий",
            "color": color,
        }
        response = CreateOrderApi.create_order(payload)
        response_track = response.json()["track"]
        assert (
                response.status_code == 201
                and response_track is not None
                and response_track > 0
        )
