class TaskEnv:
    def __init__(self):
        self.tasks = []

    def reset(self):
        self.tasks = [
            {"urgency": 3, "importance": 5},
            {"urgency": 1, "importance": 2}
        ]
        return {"observation": self.tasks}

    def step(self, action):
        reward = sum(t["urgency"] * t["importance"] for t in self.tasks)
        done = True
        return {
            "observation": self.tasks,
            "reward": reward,
            "done": done,
            "info": {}
        }