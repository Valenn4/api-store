from fastapi import APIRouter, status
from bson.objectid import ObjectId
from books.models.book import Book_Request, Book_Response
from database.connect import db
from books.schemas.schema_books import schema_books, schema_book

app = APIRouter(prefix="/api/store/books")

@app.get("/", status_code=status.HTTP_200_OK, response_model=list)
async def books():
    return schema_books(db.store.books.find())

@app.get("/{id}", response_model=Book_Response, status_code=status.HTTP_200_OK)
async def get_book(id:str):
    return Book_Response(**schema_book(db.store.books.find_one({"_id":ObjectId(id)})))

@app.post("/", response_model=Book_Response, status_code=status.HTTP_201_CREATED)
async def add_book(book: Book_Request):
    id = db.store.books.insert_one(dict(book)).inserted_id
    print(db.store.books.find_one({"_id":ObjectId(id)}))
    return Book_Response(**schema_book(db.store.books.find_one({"_id":ObjectId(id)})))
