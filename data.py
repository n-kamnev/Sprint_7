class TestDataCreateCourier:
    CREATE_COURIER_BODY = {
        "login": "ncjwt123654789",
        "password": "1234"
    }


class TestAuthCourier:
    NON_EXISTENT_COURIER_BODY = {
        'login': 'qwertyuiopasdfghjklz233',
        'password': '123456789'
    }
