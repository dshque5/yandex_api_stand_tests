AUTH_TOKEN = ""

headers_user = {
    "Content-Type": 
    "application/json"
}

if AUTH_TOKEN:
    headers_user["Authorization"] = f"Bearer {AUTH_TOKEN}"

user_body = {
    "firstName": "Джун",
    "phone": "+79998887766",
    "address": "г. Москва, ул. Льва Толстого, д. 1",
}

kit_body = {
    "name": "Мой набор"
}
