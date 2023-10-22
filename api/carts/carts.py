from fastapi import APIRouter, Depends, status
from pydantic import BaseModel
from users.users import auth
from jose import jwt
from database.connect import db
from .schemas.cart_schema import schema_cart
from .models.cart import Cart

app = APIRouter(prefix="/cart")

class Product(BaseModel):
    product: str
    price: str

@app.get("", response_model=Cart, status_code=status.HTTP_200_OK)
async def get_cart_by_user(token: str = Depends(auth)):
    user_token = jwt.decode(token, 'secret').get("sub")
    cart_user = db.store.carts.find_one({"id_user":user_token})
    return Cart(**schema_cart(cart_user))

@app.put("/add", status_code=status.HTTP_200_OK)
async def add_cart_by_user(product: Product, token: str = Depends(auth)):
    user_token = jwt.decode(token, 'secret').get("sub")
    carts = db.store.carts.find_one({"id_user":user_token}).get("cart")
    carts.append([product.product, product.price])
    db.store.carts.update_one({"id_user":user_token}, {'$set': {"cart": carts}})
    return 'Producto agregado'

@app.put("/delete", status_code=status.HTTP_200_OK)
async def delet_product(product: Product, token: str = Depends(auth)):
    user_token = jwt.decode(token, 'secret').get("sub")
    carts = db.store.carts.find_one({"id_user":user_token}).get("cart")
    carts.remove([product.product, product.price])
    db.store.carts.update_one({"id_user":user_token}, {'$set': {"cart": carts}})
    return 'Producto eliminado correctamente'