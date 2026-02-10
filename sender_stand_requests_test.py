import data
import create_order

# Вадим Галкин, 40-я когорта, финальный проект. Инженер по тестированию плюс
def test_status_order_is_200():
    order = create_order.create_order(data.order_body)
    track_number = order.json()["track"]
    response = create_order.get_order(track_number)
    print(response)
    assert response.status_code == 200

test_status_order_is_200()