import asyncio
import random
import uuid
from random import choice
from typing import List

from fastapi import FastAPI, HTTPException, Response, Path
from pydantic import ValidationError

from .models import OrderStatus, OrderOutput, OrderInput, Error

app = FastAPI()

orders = {}


class HTTPExceptionWithDetail(HTTPException):
    def __init__(self, status_code: int, detail: str = None):
        super().__init__(status_code, detail=detail)
        self.body = Error(code=status_code, message=detail).json()


@app.get("/orders", response_model=List[OrderOutput])
async def get_orders():
    await asyncio.sleep(random.uniform(0.1, 1))
    return list(orders.values())


@app.get("/orders/{order_id}", responses={200: {"model": OrderOutput, "description": "Order found"},
                                          404: {"model": Error, "description": "Order not found"}})
async def get_order(order_id: str):
    await asyncio.sleep(random.uniform(0.1, 1))
    order = orders.get(order_id)
    if not order:
        raise HTTPExceptionWithDetail(status_code=404, detail="Order not found")
    return order


@app.post("/orders", response_model=OrderOutput, status_code=201)
async def create_order(order: OrderInput):
    await asyncio.sleep(random.uniform(0.1, 1))
    try:
        # Generate a unique ID
        while True:
            order_id = str(uuid.uuid4())
            if not orders.get(order_id):
                break
        order_status = choice(list(OrderStatus))
        order_out = OrderOutput(id=order_id, **order.dict(), status=order_status)
        orders[order_id] = order_out
        return orders[order_id]
    except ValidationError as e:
        raise HTTPExceptionWithDetail(status_code=400, detail=f"Invalid input {str(e)}")


@app.delete("/orders/{order_id}",
            response_class=Response,
            responses={204: {"description": "Order canceled"},
                       404: {"model": Error, "description": "Order not found"}},
            response_model=OrderOutput)
async def delete_order(order_id: str = Path(..., description="The ID of the order to delete")):
    await asyncio.sleep(random.uniform(0.1, 1))
    order = orders.get(order_id)
    if not order:
        raise HTTPExceptionWithDetail(status_code=404, detail="Order not found")
    else:
        order.status = OrderStatus.canceled
    return Response(status_code=204)
