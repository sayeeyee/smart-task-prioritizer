from fastapi import FastAPI
from pydantic import BaseModel
from env import TaskEnv

app = FastAPI()

env = TaskEnv()

class Action(BaseModel):
    priority: str


@app.post("/reset")
def reset():
    return env.reset()


@app.post("/step")
def step(action: Action):
    return env.step({"priority": action.priority})