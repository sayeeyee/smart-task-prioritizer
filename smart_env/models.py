from pydantic import BaseModel

class TaskObservation(BaseModel):
    description: str
    deadline: int
    importance: int

class Action(BaseModel):
    priority: str  # low, medium, high

class StepResult(BaseModel):
    reward: float
    done: bool
    correct: str