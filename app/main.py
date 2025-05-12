from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import Task

app = FastAPI()

tasks = []

@app.post("/tasks/")
def create_task(task:Task):
    tasks.append(task)
    return task

@app.get("/tasks/")
def read_tasks():
    return tasks

@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    if task_id>= len(tasks):
        return {"error": "Task not found"}
    return tasks[task_id]

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task:Task):
    if task_id>= len(tasks):
        return {"error": "Task not found"}
    tasks[task_id]= task
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if(task_id >= len(tasks)):
        return {"error": "Task not found"}
    return tasks.pop(task_id)