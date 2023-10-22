
def schema_cart(cart) -> dict:
    return {
        "id": str(cart["_id"]),
        "id_user": cart["id_user"],
        "cart": cart["cart"]
    }