from pydantic import BaseModel

class User_Request(BaseModel):
    username: str
    password: str
    email : str
    '''
    phone : int
    country: str
    city: str
    address: str
    '''

class User_Response(User_Request):
    id_user: str