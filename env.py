import random

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

        self.current_task = {
            "desc": task["desc"],
            "deadline": task["deadline"],
            "importance": task["importance"]
        }

        return {
            "state": {
                "desc": self.current_task["desc"],
                "deadline": self.current_task["deadline"],
                "importance": self.current_task["importance"]
            }
        }

    def get_correct_priority(self, task):
        if task["deadline"] <= 2 or task["importance"] == 3:
            return "high"
        elif task["deadline"] <= 5:
            return "medium"
        else:
            return "low"

    def step(self, action):
        task = self.current_task

        correct_priority = self.get_correct_priority(task)

        if action == correct_priority:
            reward = 1.0
        else:
            reward = 0.5

        return {
            "state": {
                "desc": task["desc"],
                "deadline": task["deadline"],
                "importance": task["importance"]
            },
            "reward": float(reward),
            "done": True,
            "info": {}
        }