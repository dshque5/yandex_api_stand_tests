import requests
import configuration
import data

def post_new_user():
    """Создание нового пользователя и получение токена"""
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
        json=data.user_body,
        headers=data.headers_user
    )
    if response.status_code == 201:
        return response.json()['authToken']
    raise Exception(f"Ошибка создания пользователя: {response.status_code}")

def post_new_client_kit(kit_body):
    """
    Создание нового набора для пользователя
    :param kit_body: тело запроса с данными набора
    :return: ответ сервера
    """
    # Получаем или создаем токен
    if not data.AUTH_TOKEN:
        data.AUTH_TOKEN = post_new_user()
    
    # Формируем заголовки с токеном
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {data.AUTH_TOKEN}"
    }
    
    # Отправляем запрос на создание набора
    return requests.post(
        configuration.URL_SERVICE + configuration.MAIN_KITS,
        json=kit_body,
        headers=headers
    )