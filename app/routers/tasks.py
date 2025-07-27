from fastapi import APIRouter, HTTPException, Depends
from app.models.task import Task
from app.auth.auth import verify_api_key

router = APIRouter()

tasks = []


@router.post("/task/", dependencies=[Depends(verify_api_key)])
def task_list(task: Task):
    for x in tasks:
        if x.title.lower() == task.title.lower():
            raise HTTPException(
                status_code=400, detail=f"The title {task.title} is already used. Please try another one")
    tasks.append(task)
    return {f"Task recieved and stored: {task} "}


@router.get("/task/{title}")
def get_task(title: str):
    for task in tasks:
        if task.title.lower() == title.lower():
            return {f"Task: {task}"}
    raise HTTPException(status_code=404, detail="Task not found")
