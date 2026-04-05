import numpy as np
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")

def plot_habits(dates, habits):
    _, ax = plt.subplots(figsize=(10, 5))

    x = np.arange(len(dates))  # numeric positions
    width = 0.25              # bar width

    for i, (habit, values) in enumerate(habits.items()):
        ax.bar(x + i * width, values, width, label=habit)

    # Center x-axis labels
    ax.set_xticks(x + width)
    ax.set_xticklabels(dates, rotation=45)

    ax.set_title("Habit Completion Over Time")
    ax.set_ylabel("Completed (1/0)")
    ax.set_xlabel("Date")

    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()