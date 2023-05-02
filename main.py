from fastapi import FastAPI, Request
from config.mongo_connection import collection, db
from model.user_model import User
import json

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/add_user')
async def post_user(request: Request):

    body = await request.body()
    print(body)
    json_data = json.loads(body)

    name = str(json_data["name"])
    email = str(json_data["email"])
    password = str(json_data["password"])

    print('nome:', name)
    print('email:', email)
    print('senha: ', password)

    user = User(db)
    user.create_user(name, email, password)

    return {"message": "Itens adicionados com sucesso!"}

@app.get('/users')
async def get_user():

    for user in collection.find(user):
        print(user)