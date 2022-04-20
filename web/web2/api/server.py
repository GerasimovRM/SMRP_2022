from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from database.base_meta import init_database, get_session
from database import User, Item
from models.user import UserOut, UserIn
from services.user import get_all_users, create_user

app = FastAPI()


@app.on_event("startup")
async def startup():
    await init_database()


@app.get("/user", response_model=List[UserOut])
async def get_users(session: AsyncSession = Depends(get_session)) -> List[UserOut]:
    users = await get_all_users(session)
    return [UserOut(**user.__dict__) for user in users]


@app.post("/user", response_model=UserOut)
async def post_user(user: UserIn,
                    session: AsyncSession = Depends(get_session)):
    new_user = await create_user(user, session)
    return UserOut(id=new_user.id,
                   fio=new_user.fio,
                   email=new_user.email)


