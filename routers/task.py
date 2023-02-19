from fastapi import APIRouter, Path, Depends, Request
from typing import List
import schemas.task as TaskSchema
import cruds.task as crud
import cruds.user as user_crud
from db import session
from settings.custom_route import CustomRoute
from auth.oauth2 import oauth2_scheme, decode_token


router = APIRouter(
    prefix="/tasks", tags=["tasks"], route_class=CustomRoute, dependencies=[Depends(oauth2_scheme)])


@router.get("/", response_model=List[TaskSchema.Task])
async def list_tasks(request: Request):
    authorization_data = decode_token(request.headers["authorization"])
    username: str = authorization_data["sub"]
    user_id: int = user_crud.get_user_id(session, username=username)
    return crud.get_tasks(session, user_id)


@router.post("/")
async def create_task(task: TaskSchema.TaskCreate, request: Request):
    authorization_data = decode_token(request.headers["authorization"])
    username: str = authorization_data["sub"]
    user_id: int = user_crud.get_user_id(session, username=username)
    return crud.create_task(session, task, user_id)


@router.get("/{task_id}", response_model=TaskSchema.Task)
async def detail_task(task_id: int, request: Request):
    authorization_data = decode_token(request.headers["authorization"])
    username: str = authorization_data["sub"]
    user_id: int = user_crud.get_user_id(session, username=username)
    return crud.get_task(session, task_id, user_id)


@router.put("/{task_id}", response_model=TaskSchema.Task)
async def update_task(task: TaskSchema.TaskUpdate, task_id: int, request: Request):
    return crud.update_task(session, task_id, task)


@router.delete("/{task_id}",  response_model=TaskSchema.Task)
async def delete_task(task_id: int, request: Request):
    return crud.delete_task(session, task_id)
