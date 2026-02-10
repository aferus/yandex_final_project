import data
import sender_stand_requests

# Вадим Галкин, 40-я когорта, финальный проект. Инженер по тестированию плюс
def test_status_order_is_200():
    order = sender_stand_requests.create_order(data.order_body)
    track_number = order.json()["track"]
    response = sender_stand_requests.get_order(track_number)
    assert response.status_code == 200

test_status_order_is_200()