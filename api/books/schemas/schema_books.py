def schema_book(book) -> dict:
    return {
        "id_book":str(book["_id"]),
        "title":book["title"],
        "author":book["author"],
        "description":book["description"],
        "category":book["category"],
        "price":book["price"],
        "pages":book["pages"],
        "image":book["image"]
    }
def schema_books(lista) -> list:
    return [schema_book(el) for el in lista]