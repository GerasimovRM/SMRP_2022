from typing import List, Optional

from passlib.context import CryptContext
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from database.user import User
from models.user import UserIn, UserPut


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)


async def get_all_users(session: AsyncSession) -> List[User]:
    query = select(User)
    result = await session.execute(query)
    return result.scalars().all()


async def create_user(user: UserIn,
                      session: AsyncSession,
                      ) -> User:
    # new_user = User(fio=UserIn.fio, email=UserIn.email)
    user.password = get_password_hash(user.password)
    new_user = User(**user.dict())
    session.add(new_user)
    await session.commit()
    return new_user


async def get_one_user_by_id(user_id: int, session: AsyncSession) -> Optional[User]:
    query = select(User)\
        .where(User.id == user_id)\
        .options(joinedload(User.items))
    result = await session.execute(query)
    return result.scalars().first()


async def get_one_user_by_email(user_email: str, session: AsyncSession) -> Optional[User]:
    query = select(User).where(User.email == user_email)
    result = await session.execute(query)
    return result.scalars().first()


async def change_user_data(user_data: UserPut, session: AsyncSession) -> User:
    query = select(User).where(User.id == user_data.id)
    result = await session.execute(query)
    user = result.scalars().first()
    if not user:  # если пользователя с таким id нет (user == None)
        return user

    if user_data.email:
        user.email = user_data.email
    if user_data.fio:
        user.fio = user_data.fio
    await session.commit()
    return user


async def delete_user_by_id(user_id: int, session: AsyncSession):
    user = await get_one_user_by_id(user_id, session)
    if not user:  # если пользователя с таким id нет (user == None)
        return False

    await session.delete(user)
    await session.commit()
    return True
