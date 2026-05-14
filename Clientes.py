from pydantic import BaseModel

class Clientes(BaseModel):
    id: int
    name: str
    age: int
    description: str | None=None
class clientCreate(client):
        pass 
class client(client):
        id: int | None = None 
        