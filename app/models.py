from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    due_date: str
    status: str
    priority: int