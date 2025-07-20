from pydantic import BaseModel,Field
from typing import List,Optional
import uuid

class SizeInfo(BaseModel):
    psize:str
    quantity:int

class ProductCreate(BaseModel):
    name:str
    price:float
    sizes:List[SizeInfo]

class Product(ProductCreate):
    uid:uuid.UUID=Field(default_factory=uuid.uuid4)



