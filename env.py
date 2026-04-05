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
        self.current_task = random.choice(self.tasks)

        return {
            "state": {
                "description": self.current_task["desc"],
                "deadline": self.current_task["deadline"],
                "importance": self.current_task["importance"]
            },
            "info": {}
        }

    def step(self, action):
        task = self.current_task
        priority = action.get("priority")

        # correct priority logic
        if task["deadline"] <= 2 or task["importance"] == 3:
            correct = "high"
        elif task["deadline"] <= 5:
            correct = "medium"
        else:
            correct = "low"

        if priority == correct:
            reward = 1.0
        elif priority == "medium" and correct in ["low", "high"]:
            reward = 0.5
        else:
            reward = -1.0

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