from pydantic import BaseModel

class Todo(BaseModel):
    id : int
    name: str
    completed: bool

