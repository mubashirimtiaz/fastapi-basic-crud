from fastapi import FastAPI
from models import Todo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


#TODOS


todos = []

@app.get("/todos")
async def get_todos():
  return todos



@app.post("/todos")
async def create_todo(todo: Todo): 
  todos.append(todo)
  return todos


@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
  for todo in todos:
    if todo.id == todo_id:
      return todo

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: Todo):
  for t in todos:
    if t.id == todo_id:
      t.completed = todo.completed
      t.name = todo.name
      return t
  return {"message": "Todo not found"}



@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
  for todo in todos:
    if todo.id == todo_id:
      todos.remove(todo)
      return todo
  return {"message": "Todo not found"}