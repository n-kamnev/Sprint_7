import allure
from scooter_api import ReceivingOrderList


class TestReceivingOrderList:
    @allure.step("Проверяем запрос списка заказов")
    @allure.description(
        "Создаем запрос на получение списка заказов, проверяем код ответа и тело ответа"
    )
    def test_receiving_orders_list(self):
        receiving_orders_list = ReceivingOrderList.receiving_orders_list()
        orders = receiving_orders_list.json()["orders"]
        assert receiving_orders_list.status_code == 200 and orders is not None
