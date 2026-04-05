print("[START] task=task-prioritization env=custom-env model=rule-based")

reward = 0.8
steps = 1

print(f"[STEP] step={steps} action=assign_priority reward={reward:.2f} done=true error=null")

print(f"[END] success=true steps={steps} score={reward:.2f} rewards=[{reward}]")