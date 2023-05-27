import pytest


def test_get_orders_no_orders(test_client):
    # Test should return empty list in case there is no orders
    response = test_client.get("/orders")
    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.parametrize("order_id", ["123456"])
def test_get_non_existing_order(test_client, order_id):
    # Test should return 404 in case there is no order
    response = test_client.get(f"/orders/{order_id}")
    assert response.status_code == 404
    data = response.json()
    assert data['detail'] == "Order not found"


@pytest.mark.parametrize("order_id", ["123456"])
def test_delete_not_existing_order(test_client, order_id):
    # Test do delete not existing order
    response = test_client.delete(f"/orders/{order_id}")
    assert response.status_code == 404
    data = response.json()
    assert data['detail'] == "Order not found"


@pytest.mark.parametrize("order", [({}), ({'stocks': 'EURUSD'}, ({'quantity': 10.0}))])
def test_create_order_missing_required_fields(test_client, order):
    # Test to create order in case Input data is not aligned with InputModel
    response = test_client.post("/orders", json=order)
    assert response.status_code == 422


@pytest.mark.parametrize("order", [({'stocks': 10, 'quantity': 10.0}), ({'stocks': 'EURUSD', 'quantity': "EUR"})])
def test_create_order_invalid_type_fields(test_client, order):
    # Test to create order in case invalid data types being used
    response = test_client.post("/orders", json=order)
    assert response.status_code == 422
