from fastapi import APIRouter, status
from app.schemas.product_schema import ProductCreate, Product
from app.models.product_model import product_serializer
from app.database import product_collection
from fastapi.responses import JSONResponse
import uuid
from fastapi import Query
from typing import Optional
from pymongo import ASCENDING


router = APIRouter()

@router.post("/products",status_code=status.HTTP_201_CREATED,response_model=Product)
async def create_product(product:ProductCreate):
    product_data=product.dict()
    product_data["uid"]=str(uuid.uuid4())

    result = await product_collection.insert_one(product_data)
    created_product = await product_collection.find_one({"_id": result.inserted_id})
    return product_serializer(created_product)


@router.get("/products")
async def getProducts(
    name:Optional[str]=Query(None),
    size:Optional[str]=Query(None),
    limit:int=10,
    offset:int=0):
    query={}

    if name:
        query["name"]={"$regex":name,"$options":"i"}

    if size:
        query["sizes.psize"]=size
    
    cursor = product_collection.find(query).sort("_id", ASCENDING).skip(offset).limit(limit)
    results = []
    async for product in cursor:
        prod = product_serializer(product)
        # Omit 'sizes' field in list response
        prod.pop('sizes', None)
        results.append(prod)
    total_count = await product_collection.count_documents(query)
    next_offset = offset + limit if (offset + limit) < total_count else None
    prev_offset = offset - limit if (offset - limit) >= 0 else None
    page_info = {
        "next": str(next_offset) if next_offset is not None else None,
        "limit": limit,
        "previous": prev_offset if prev_offset is not None else None
    }
    return {"data": results, "page": page_info}