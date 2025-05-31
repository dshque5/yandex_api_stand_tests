import requests
import configuration
import data

# Создание нового пользователя и получение токена

def post_new_user():
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers=data.headers_user
    )
    if response.status_code == 201:
        return response.json()['authToken']
    raise Exception(f"Ошибка создания пользователя: {response.status_code}")

# Создание нового набора для пользователя

def post_new_client_kit(kit_body):
    if not data.AUTH_TOKEN:
        data.AUTH_TOKEN = post_new_user()
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {data.AUTH_TOKEN}"
    }
    
    return requests.post(
        configuration.URL_SERVICE + configuration.MAIN_KITS,
        json=kit_body,
        headers=headers
    )