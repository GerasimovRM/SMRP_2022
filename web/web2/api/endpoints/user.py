from typing import List

from fastapi import Depends, HTTPException, status, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from database.base_meta import init_database, get_session
from database import User, Item
from models.user import UserOut, UserIn, UserPut
from services.auth import get_current_user
from services.user import get_all_users, create_user, get_one_user_by_id, change_user_data, \
    delete_user_by_id

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[UserOut])
async def get_users(current_user: User = Depends(get_current_user),
                    session: AsyncSession = Depends(get_session)) -> List[UserOut]:
    users = await get_all_users(session)
    return [UserOut(**user.__dict__) for user in users]


@router.get("/{user_id}", response_model=UserOut)
async def get_user_by_id(user_id: int,
                         current_user: User = Depends(get_current_user),
                         session: AsyncSession = Depends(get_session)):
    user = await get_one_user_by_id(user_id, session)
    if user:
        return UserOut(**user.__dict__)
    else:  # если user == None, т.е. нет такого пользователя, то вернем 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found!")


@router.post("/", response_model=UserOut)
async def post_user(user: UserIn,
                    current_user: User = Depends(get_current_user),
                    session: AsyncSession = Depends(get_session)):
    new_user = await create_user(user, session)
    return UserOut(**new_user.__dict__)


@router.put("/", response_model=UserOut)
async def put_user(user: UserPut,
                   current_user: User = Depends(get_current_user),
                   session: AsyncSession = Depends(get_session)):
    changed_user = await change_user_data(user, session)
    if changed_user:
        return UserOut(**changed_user.__dict__)
    else:  # если change_user == None, т.е. нет такого пользователя, то вернем 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user.id} not found!")


@router.delete("/{user_id}")
async def delete_user(user_id: int,
                      current_user: User = Depends(get_current_user),
                      session: AsyncSession = Depends(get_session)):
    user_is_delete = await delete_user_by_id(user_id, session)
    if user_is_delete:
        return {"status": "ok"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found!")
