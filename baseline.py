def predict_priority(task):
    # simple rule-based AI

    if task.deadline <= 2 or task.importance == 3:
        return "high"
    elif task.deadline <= 5:
        return "medium"
    else:
        return "low"
