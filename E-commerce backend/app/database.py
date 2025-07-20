from motor.motor_asyncio import AsyncIOMotorClient
from .config import MONGO_URI, DB_NAME

client = AsyncIOMotorClient(MONGO_URI)

database = client[DB_NAME]

product_collection = database["products"]

order_collection = database["orders"]