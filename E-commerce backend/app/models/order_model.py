def order_serializer(order) -> dict:
    return {
        "id": str(order["_id"]),
        "uid": str(order["uid"]),
        "user_id": order["user_id"],
        "items": order["items"]
    }
