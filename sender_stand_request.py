import requests
import configuration
import data

# Создание нового пользователя и получение токена
def post_new_user():
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers=data.headers_user,
    )


# Создание нового набора для пользователя
def post_new_client_kit(kit_body):
    if not data.AUTH_TOKEN:
        user_response = post_new_user()
        if user_response.status_code == 201:
            data.AUTH_TOKEN = user_response.json().get("authToken")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {data.AUTH_TOKEN}",
    }

    return requests.post(
        configuration.URL_SERVICE + configuration.MAIN_KITS,
        json=kit_body,
        headers=headers,
    )
