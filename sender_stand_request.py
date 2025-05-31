# Импорт необходимых модулей и данных для запроса
import requests
import configuration
import data

def post_products_kits(products_ids):
    """
    Функция для отправки POST-запроса с ID продуктов
    Возвращает ответ от сервера
    """
    # Формируем тело запроса
    request_body = {
        "product_ids": products_ids
    }
    
    # Отправляем POST-запрос
    return requests.post(
        configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,
        json=request_body,
        headers=data.headers
    )

# Вызов функции с передачей списка ID продуктов из файла data.py
response = post_products_kits(data.products_ids)

# Вывод HTTP-статус кода ответа и тела ответа в формате JSON
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
