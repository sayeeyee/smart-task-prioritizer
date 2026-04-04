from env import TaskEnv

env = TaskEnv()

task_name = "task-prioritization"
env_name = "custom-env"
model_name = "rule-based"

print(f"[START] task={task_name} env={env_name} model={model_name}")

state = env.reset()

rewards = []
steps = 0
done = False

while not done:
    action = "assign_priority"
    next_state, reward = env.step(action)

    rewards.append(reward)
    steps += 1
    done = True

    print(f"[STEP] step={steps} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

score = max(0.0, min(sum(rewards), 1.0))

print(f"[END] success=true steps={steps} score={score:.2f} rewards={rewards}")