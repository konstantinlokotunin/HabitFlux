from src.data_loader import load_data
from src.analysis import calculate_completion_rate, calculate_current_streak, calculate_max_streak, export_results
from src.visualization import plot_habit_heatmap
import csv

def main():
    dates, habits = load_data("data/data.csv")

    for habit, values in habits.items():
        rate = calculate_completion_rate(values)
        current_streak = calculate_current_streak(values)
        max_streak = calculate_max_streak(values)

        print(f"{habit.capitalize()}:")
        print(f"  Completion Rate: {rate:.2f}%")
        print(f"  Current streak: {current_streak}")
        print(f"  Max Streak: {max_streak}\n")

    plot_habit_heatmap(dates, habits)
    
    export_results("outputs/output.csv", habits)

if __name__ == "__main__":
    main()