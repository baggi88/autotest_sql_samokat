# Чижикова Анна, 25-я когорта — Финальный проект. Инженер по тестированию плюс

import data
import sender_stand_request

# Тест проверки статуса ответа 200
def test_order_status_code_200():
    # Создаём новый заказ
    track_number = sender_stand_request.create_new_order(data.order_body)
    # Проверяем получение заказа по номеру трека
    response = sender_stand_request.get_order_from_track(track_number)
    assert response.status_code == 200