
def schema_user(user) -> dict:
    return {
        "username": user["username"],
        "password": user["password"],
        "email": 'email'
    }