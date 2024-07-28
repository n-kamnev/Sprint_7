import allure
from scooter_api import AuthCourierApi
import data
import helper
import valid_answers


class TestLoginCourier:
    @allure.step("Проверяем успешную авторизацию курьера")
    @allure.description(
        "Создаем курьера, авторизуемся, проверяем код ответа и тело ответа, удаляем курьера"
    )
    def test_login_courier(self):
        login_pass = (
            helper.CourierFactory.create_new_courier_and_return_login_password()
        )
        auth_courier = AuthCourierApi.auth_courier(login_pass)
        courier_id = auth_courier.json()["id"]
        AuthCourierApi.delete_courier(courier_id)
        assert (
                auth_courier.status_code == 200
                and courier_id is not None
                and courier_id > 0
        )

    @allure.step("Проверяем авторизацию несуществующего пользователя")
    @allure.description(
        "Авторизуемся несуществующим пользователем, проверяем код ответа и тело ответа"
    )
    def test_auth_non_existent_user(self):
        non_existent_courier = AuthCourierApi.auth_courier(
            data.TestAuthCourier.NON_EXISTENT_COURIER_BODY
        )
        assert (
                non_existent_courier.status_code == 404
                and non_existent_courier.json()
                == valid_answers.ACCOUNT_WAS_NOT_FOUND
        )

    @allure.step("Проверяем авторизацию с пустым логином")
    @allure.description(
        "Авторизуемся с пустым логином, проверяем код ответа и тело ответа"
    )
    def test_auth_with_empty_login(self):
        body = helper.CourierFactory.modify_create_courier("login", "")
        auth_with_empty_login = AuthCourierApi.auth_courier(body)
        assert (
                auth_with_empty_login.status_code == 400
                and auth_with_empty_login.json()
                == valid_answers.THERE_IS_NOT_ENOUGH_DATA_TO_LOGIN
        )
