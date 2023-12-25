from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    task: str
    status: bool

task_list = []

@app.put("/tasks", response_model=List[Task])
def create_task(task: Task):
    task_list.append(task.dict())
    return task_list

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return task_list

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    try:
        del task_list[task_id - 1]
        return {"status": "Task deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    try:
        
        if not isinstance(task.status, bool):
            raise HTTPException(status_code=424, detail="Status should be a boolean value")
        
        task_list[task_id - 1] = task.dict()
        return task_list[task_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")
