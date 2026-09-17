from typing import List, Optional

from fastapi import FastAPI, HTTPException, Query, status
from pydantic import BaseModel, Field

app = FastAPI(title="Student Planner API")


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)
    subject: str = Field(..., min_length=1)
    priority: int = Field(default=1, ge=1, le=5)
    completed: bool = False


class Task(TaskCreate):
    id: int


tasks: List[Task] = [
    Task(id=1, title="Revisar matemática", subject="Matemática", priority=3, completed=False),
    Task(id=2, title="Estudar para a prova de história", subject="História", priority=2, completed=True),
]


@app.get("/tasks")
def list_tasks(
    subject: Optional[str] = Query(default=None),
    completed: Optional[bool] = Query(default=None),
):
    """Return all tasks, optionally filtered by subject and completion status."""
    filtered_tasks = tasks

    if subject is not None:
        filtered_tasks = [task for task in filtered_tasks if task.subject.lower() == subject.lower()]

    if completed is not None:
        filtered_tasks = [task for task in filtered_tasks if task.completed == completed]

    return filtered_tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    """Return a single task by its ID."""
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    """Create a new task."""
    new_task = Task(id=len(tasks) + 1, **task.model_dump())
    tasks.append(new_task)
    return new_task


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_updates: dict):
    """Update a task using partial changes."""
    for index, task in enumerate(tasks):
        if task.id == task_id:
            for key, value in task_updates.items():
                if hasattr(task, key):
                    setattr(task, key, value)
            return task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    """Delete a task by ID."""
    for index, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(index)
            return None
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
