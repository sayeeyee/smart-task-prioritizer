def grade(predictions, correct_answers):
    score = 0

    for pred, correct in zip(predictions, correct_answers):
        if pred == correct:
            score += 1

    return score / len(correct_answers)
