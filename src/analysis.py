import numpy as np
import csv

def calculate_completion_rate(habit):
    arr = np.array(habit)
    return np.mean(arr) * 100


def calculate_max_streak(habit):
    max_streak = 0
    current_streak = 0

    for value in habit:
        if value == 1:
            current_streak += 1
            max_streak = max(max_streak, current_streak)
        else:
            current_streak = 0

    return max_streak

def calculate_current_streak(values):
    streak = 0
    for v in list(reversed(values)):
        if v == 1:
            streak += 1
        else:
            break
    return streak

def export_results(filename, habits):

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        
        writer.writerow(["Habit", "Completion Rate", "Current Streak", "Max Streak"])

        for key, values in habits.items():
            writer.writerow([
                key.title(),
                f"{calculate_completion_rate(values):.2f}%",
                f"{calculate_current_streak(values)} days",
                f"{calculate_max_streak(values)} days"
            ])