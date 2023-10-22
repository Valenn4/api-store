from pydantic import BaseModel

class Cart(BaseModel):
    id_user: str
    cart: list