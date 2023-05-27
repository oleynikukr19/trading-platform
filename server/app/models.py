from enum import Enum

from pydantic import BaseModel, constr


class OrderStatus(Enum):
    pending = "pending"
    executed = "executed"
    canceled = "canceled"


class OrderInput(BaseModel):
    stocks: constr(strict=True)  # stocks to be str
    quantity: float


class OrderOutput(OrderInput):
    id: str
    status: OrderStatus


class Error(BaseModel):
    code: int
    message: str
