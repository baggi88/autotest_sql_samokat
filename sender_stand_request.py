# Содержит настройки подключения и путь к документации
import configuration

# Отправляет HTTP GET-запрос к заданному URL-адресу
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Создание заказа
def create_new_order(order_body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=order_body,
        headers=data.headers
    )
    assert response.status_code == 201, "Created"
    return response.json()["track"]  # Сохраняем и возвращаем номер трека заказа

# Получение заказа по номеру трека
def get_order_from_track(track):
    response = requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_NUMBER + str(track),
        headers=data.headers
    )
    return response

# Тест проверки статуса ответа 200
def test_order_status_code_200():
    # Создаём новый заказ
    track_number = create_new_order(data.order_body)
    # Проверяем получение заказа по номеру трека
    response = get_order_from_track(track_number)
    assert response.status_code == 200