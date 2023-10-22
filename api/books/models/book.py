from pydantic import BaseModel

class Book_Request(BaseModel):
    title: str
    author: str
    description: str
    category: str
    price: float
    pages: int
    image: str

class Book_Response(Book_Request):
    id_book: str