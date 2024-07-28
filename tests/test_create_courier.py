import allure
from scooter_api import CreateCourierApi
import helper
import valid_answers


class TestCreateCourier:
    @allure.step("Проверка успешности создания курьера")
    @allure.description("Создание курьера, проверяем статус ответа и тело ответа")
    def test_success_create_courier(self):
        created_courier_request = CreateCourierApi.create_courier(
            helper.CourierFactory.generation_new_courier()
        )
        assert (
                created_courier_request.status_code == 201
                and created_courier_request.json() == valid_answers.SUCCESSFUL_CREATION_OF_COURIER_RESPONSE
        )

    @allure.step("Создать двух одинаковых курьеров")
    @allure.description(
        "Создаем одинаковых курьеров, проверяем статус ответа и тело ответа"
    )
    def test_failed_create_identical_couriers(self):
        body = helper.CourierFactory.modify_create_courier(
            "login", helper.CourierFactory.generate_courier_login()
        )
        CreateCourierApi.create_courier(body)
        second_created_courier_request = CreateCourierApi.create_courier(body)
        assert (
                second_created_courier_request.status_code == 409
                and second_created_courier_request.json()
                == valid_answers.USERNAME_IS_ALREADY_IN_USE
        )

    @allure.step("Проверка создания курьера с незаполненными обязательными полями")
    @allure.description(
        "Создаем курьера с пустым полем login, проверяем статус ответа и тело ответа"
    )
    def test_create_courier_with_empty_login(self):
        body = helper.CourierFactory.modify_create_courier("login", "")
        created_courier_request = CreateCourierApi.create_courier(body)
        assert (
                created_courier_request.status_code == 400
                and created_courier_request.json()
                == valid_answers.INSUFFICIENT_DATA
        )
