from typing import List, Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.user import User
from models.user import UserIn, UserPut


async def get_all_users(session: AsyncSession) -> List[User]:
    query = select(User)
    result = await session.execute(query)
    return result.scalars().all()


async def create_user(user: UserIn, session: AsyncSession) -> User:
    # new_user = User(fio=UserIn.fio, email=UserIn.email)
    new_user = User(**user.dict())
    session.add(new_user)
    await session.commit()
    return new_user


async def get_one_user_by_id(user_id: int, session: AsyncSession) -> Optional[User]:
    query = select(User).where(User.id == user_id)
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
