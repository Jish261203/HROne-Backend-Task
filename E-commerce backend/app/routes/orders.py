from fastapi import APIRouter, status,Path, Query
from app.schemas.order_schema import OrderCreate, Order
from app.models.order_model import order_serializer
from app.database import order_collection
from fastapi.responses import JSONResponse
import uuid
from pymongo import ASCENDING

router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED, response_model=Order)
async def create_order(order: OrderCreate):
    order_data = order.dict()
    order_data["uid"] = str(uuid.uuid4())

    result = await order_collection.insert_one(order_data)
    created_order = await order_collection.find_one({"_id": result.inserted_id})
    return order_serializer(created_order)

@router.get("/orders/{user_id}")
async def get_orders_for_user(
    user_id: str = Path(...),
    limit: int = 10,
    offset: int = 0
):
    from app.database import product_collection  # Import here to avoid circular import
    query = {"user_id": user_id}
    cursor = order_collection.find(query).sort("_id", ASCENDING).skip(offset).limit(limit)

    results = []
    async for order in cursor:
        order_data = order_serializer(order)
        enhanced_items = []
        for item in order_data["items"]:
            product = await product_collection.find_one({"uid": item["product_id"]})
            if product:
                product_details = {
                    "name": product.get("name"),
                    "id": product.get("uid")
                }
            else:
                product_details = None
            enhanced_items.append({
                "productDetails": product_details,
                "qty": item.get("quantity")
            })
        order_data["items"] = enhanced_items
        results.append(order_data)
    return results
