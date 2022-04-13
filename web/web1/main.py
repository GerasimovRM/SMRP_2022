import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

count = 1


class User:
    def __init__(self, full_name, email, login, password):
        global count
        self.id = count
        count += 1
        self.full_name = full_name
        self.email = email
        self.login = login
        self.password = password


class UserIn(BaseModel):
    full_name: str
    email: str
    login: str
    password: str


class UserOut(UserIn):
    id: int


app = FastAPI()
storage = {"users": [User("kto-to", "test@test.test", "test", "test")]}


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/mmsp")
async def mmsp():
    return "Привет!"


@app.get("/users", response_model=List[UserOut])
async def get_users():
    return list(map(lambda user: UserOut(**user.__dict__), storage["users"]))


@app.get("/user", response_model=UserOut)
async def get_user(id: int):
    user = next(filter(lambda x: x.id == id, storage["users"]), None)
    return UserOut(**user.__dict__)


@app.post("/user", response_model=UserOut)
async def post_user(user: UserIn):
    new_user = User(user.full_name,
                    user.email,
                    user.login,
                    user.password)
    storage["users"].append(new_user)
    # return UserOut(**new_user.__dict__)
    return UserOut(id=new_user.id,
                   full_name=new_user.full_name,
                   email=new_user.email,
                   login=new_user.login,
                   password=new_user.password)




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)