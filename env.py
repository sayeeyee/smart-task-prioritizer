import random
from models import TaskObservation, Action, StepResult

class TaskEnv:
    def __init__(self):
        self.tasks = [
            {"desc": "Submit assignment", "deadline": 1, "importance": 3},
            {"desc": "Watch lecture", "deadline": 4, "importance": 2},
            {"desc": "Clean room", "deadline": 8, "importance": 1}
        ]
        self.current_task = None

    def reset(self):
        task = random.choice(self.tasks)
        self.current_task = TaskObservation(
            description=task["desc"],
            deadline=task["deadline"],
            importance=task["importance"]
        )
        return self.current_task

    def get_correct_priority(self, task):
        if task["deadline"] <= 2 or task["importance"] == 3:
            return "high"
        elif task["deadline"] <= 5:
            return "medium"
        else:
            return "low"

    def step(self, action: Action):
        task_dict = {
            "desc": self.current_task.description,
            "deadline": self.current_task.deadline,
            "importance": self.current_task.importance
        }

        correct = self.get_correct_priority(task_dict)

        if action.priority == correct:
            reward = 1.0
        elif action.priority == "medium":
            reward = 0.5
        else:
            reward = -1.0

        reward -= 0.1  # step penalty

        return StepResult(
            reward=reward,
            done=True,
            correct=correct
        )