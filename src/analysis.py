import numpy as np

def calculate_completion_rate(habit):
    return np.mean(habit) * 100


def calculate_streak(habit):
    max_streak = 0
    current_streak = 0

    for value in habit:
        if value == 1:
            current_streak += 1
        else:
            current_streak = 0
            
    max_streak = max(max_streak, current_streak)
    return max_streak