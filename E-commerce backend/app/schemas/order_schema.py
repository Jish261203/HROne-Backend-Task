from pydantic import BaseModel, Field
from typing import List
import uuid

class OrderItem(BaseModel):
    product_id: str
    quantity: int

class OrderCreate(BaseModel):
    user_id: str
    items: List[OrderItem]

class Order(OrderCreate):
    uid: uuid.UUID = Field(default_factory=uuid.uuid4)