import random

class TaskEnv:
    def __init__(self):
        self.tasks = [
            {"desc": "Complete assignment", "deadline": 1, "importance": 3},
            {"desc": "Watch lecture", "deadline": 3, "importance": 2},
            {"desc": "Go for walk", "deadline": 5, "importance": 1}
        ]
        self.current_task = None

    def reset(self):
        self.current_task = random.choice(self.tasks)
        return {
            "state": {
                "description": self.current_task["desc"],
                "deadline": self.current_task["deadline"],
                "importance": self.current_task["importance"]
            }
        }

    def step(self, action):
        task = self.current_task
        priority = action.get("priority")

        # Simple reward logic
        if task["importance"] >= 3 and priority == "high":
            reward = 1
        elif task["importance"] == 2 and priority in ["medium", "high"]:
            reward = 0.5
        elif task["importance"] == 1 and priority == "low":
            reward = 1
        else:
            reward = 0

        return {
            "state": {
                "description": task["desc"],
                "deadline": task["deadline"],
                "importance": task["importance"]
            },
            "reward": float(reward),
            "done": True,
            "info": {}
        }