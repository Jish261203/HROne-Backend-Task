def product_serializer(product)->dict:
    return{
        "id":str(product["_id"]),
        "uid":str(product["uid"]),
        "name":product["name"],
        "price":product["price"],
        "sizes":product["sizes"]
    }