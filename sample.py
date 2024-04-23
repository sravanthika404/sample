from fastapi import FastAPI

app = FastAPI()

# Sample data (in-memory storage for demonstration purposes)
tasks = []

@app.get("/todos")
def get_todos():
    """Get all tasks."""
    return tasks

@app.post("/todos")
def add_todo(task: str):
    """Add a new task."""
    tasks.append(task)
    return {"message": "Task added successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
