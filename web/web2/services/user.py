from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.user import User
from models.user import UserIn


async def get_all_users(session: AsyncSession) -> List[User]:
    query = select(User)
    result = await session.execute(query)
    return result.scalars().all()


async def create_user(user: UserIn, session: AsyncSession):
    # new_user = User(fio=UserIn.fio, email=UserIn.email)
    tmp = user.dict()
    new_user = User(**tmp)
    session.add(new_user)
    await session.commit()
    return new_user
