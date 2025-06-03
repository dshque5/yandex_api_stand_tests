import sender_stand_request
import data

# Создание тела запроса для набора
def get_kit_body(name):
    return {"name": name}


# Пустое тело запроса
def empty_body():
    return {}


# Проверка успешного создания набора
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert "name" in response.json()
    assert response.json()["name"] == kit_body["name"]


# Проверка отображения ошибки 400
def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400


# Тест 1. Успешное создание набора (1 символ)
def test_create_kit_name_one_symbol():
    positive_assert(get_kit_body("а"))


# Тест 2. Успешное создание набора (511 символов)
def test_create_kit_name_max_symbols():
    positive_assert(
        get_kit_body(
            "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
        )
    )


# Тест 3. Ошибка (0 символов)
def test_create_kit_name_no_symbols():
    negative_assert_code_400(get_kit_body(""))


# Тест 4. Ошибка (512 символов)
def test_create_kit_name_too_long():
    negative_assert_code_400(
        get_kit_body(
            "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabCa"
        )
    )


# Тест 5. Успешное создание набора (английские буквы)
def test_create_kit_name_eng_letters():
    positive_assert(get_kit_body("QWErty"))


# Тест 6. Успешное создание набора (русские буквы)
def test_create_kit_name_rus_letters():
    positive_assert(get_kit_body("Мария"))


# Тест 7. Успешное создание набора (спецсимволы)
def test_create_kit_name_spec_symbols():
    positive_assert(get_kit_body('"№%@",'))


# Тест 8. Успешное создание набора (пробелы)
def test_create_kit_name_space():
    positive_assert(get_kit_body("Человек и КО "))


# Тест 9. Успешное создание набора (цифры)
def test_create_kit_name_numbers():
    positive_assert(get_kit_body("123"))


# Тест 10. Ошибка (нет параметра)
def test_create_kit_name_no_parameter():
    negative_assert_code_400(empty_body())


# Тест 11. Ошибка (неверный тип параметра)
def test_create_kit_name_another_parameter_type():
    negative_assert_code_400({"name": 123})
