import uuid


def test_get_all_orders(test_client):
    # Get all orders. Should return 200 and returned data type should be list
    response = test_client.get("/orders")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_create_order(test_client):
    # Place an order. Response should be 201
    order_data = {"stocks": "EURUSD", "quantity": 1.0}
    response = test_client.post("/orders", json=order_data)
    assert response.status_code == 201
    data = response.json()
    assert data["stocks"] == order_data["stocks"]
    assert data["quantity"] == order_data["quantity"]
    assert "status" in data
    assert "id" in data


def test_order_id_format(test_client):
    # Test to check created id format. Should in UUID style
    order = {"stocks": "AAPL", "quantity": 10.0}
    response = test_client.post("/orders", json=order)
    assert response.status_code == 201

    order_id = response.json()["id"]
    try:
        uuid_obj = uuid.UUID(order_id, version=4)
    except ValueError:
        assert False, f"{order_id} is not a valid UUID"

    assert str(uuid_obj) == order_id, f"{order_id} is not a valid UUID"


def test_get_order(test_client):
    # Test to get an order by id
    order_data = {"stocks": "EURUSD", "quantity": 1.0}
    response = test_client.post("/orders", json=order_data)
    order_id = response.json()["id"]

    # Now fetch the order
    response = test_client.get(f"/orders/{order_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == order_id


def test_delete_order(test_client):
    # Test to delete particular order by id
    order_data = {"stocks": "EURUSD", "quantity": 1.0}
    response = test_client.post("/orders", json=order_data)
    order_id = response.json()["id"]

    # Now delete the order
    response = test_client.delete(f"/orders/{order_id}")
    assert response.status_code == 204

    # Try fetching the deleted order
    response = test_client.get(f"/orders/{order_id}")
    data = response.json()
    assert data['status'] == 'canceled'
