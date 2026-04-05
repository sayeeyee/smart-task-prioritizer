from fastapi import FastAPI
from pydantic import BaseModel
from smart_env.env import TaskEnv   # ✅ FIXED

app = FastAPI()

env = TaskEnv()

class StepRequest(BaseModel):
    action: int

@app.post("/reset")
def reset():
    return env.reset()

@app.post("/step")
def step(req: StepRequest):
    return env.step(req.action)