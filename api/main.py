from fastapi import FastAPI
import books.books as books
import users.users as users
import carts.carts as carts
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(prefix="/")
app.include_router(books.app)
app.include_router(users.app)
app.include_router(carts.app)

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)