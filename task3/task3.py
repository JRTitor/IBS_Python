from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Task(BaseModel):
    task: str
    status: bool

task_list = []



"""
This function creates a new task in the task list.

Args:
    task (Task): The task to be added

Returns:
    List[Task]: The updated task list
"""
@app.put("/tasks", response_model=List[Task])
def create_task(task: Task):
    if not isinstance(task, Task):
        raise HTTPException(status_code=424, detail="Task should be a dictionary")
    task_list.append(task.dict())
    return task_list



"""
This function retrieves the task from the task list.

Args:
    None

Returns:
    List[Task][task_id]: The task of the task list
"""
@app.get("/tasks/{task_id}", response_model=Task)
def get_tasks(task_id:int):
    if not isinstance(task_id, int):
        raise HTTPException(status_code=424, detail="Task index should be an integer value")
    if task_id <= 0 or task_id > len(task_list):
        raise HTTPException(status_code=404, detail="Task not found")

    return task_list[task_id - 1]


"""
This function deletes a task from the task based on its index.

Args:
    task_id (int): The index of the task to be deleted

Returns:
    dict: A JSON object with a status key indicating whether the task was deleted or not
"""
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if not isinstance(task_id, int):
        raise HTTPException(status_code=424, detail="Task index should be an integer value")
    try:
        del task_list[task_id - 1]
        return {"status": "Task deleted"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")




"""
This function updates an existing task in the task list.

Args:
    task_id (int): The index of the task to be updated
    task (Task): The updated task details

Returns:
    Task: The updated task details
"""
@app.post("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: Task):
    try:
        # Check if the status is a boolean value
        if not isinstance(task.status, bool):
            raise HTTPException(status_code=424, detail="Status should be a boolean value")
        


        # Update the task in the list
        task_list[task_id - 1] = task.dict()
        return task_list[task_id - 1]
    except IndexError:
        raise HTTPException(status_code=404, detail="Task not found")
