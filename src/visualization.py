import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8")

def plot_habits(dates, habits):

    _, ax = plt.subplots(figsize=(10, 5))

    width = 0.3

    for habit, values in habits.items():
        ax.bar(dates, values, width, label=habit)

    ax.set_title("Habit Completion Over Time")
    ax.set_ylabel("Completed (1/0)")
    ax.set_xlabel("Date")
    ax.set_ylim((min(values) - 1), max(values) + 1)

    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.6)

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()