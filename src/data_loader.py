import csv

def load_data(filepath):
    dates = []
    habits = {}

    with open(filepath, newline="", encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        for row in reader:
            dates.append(row["date"])

            for key in row:
                if key != "date":
                    if key not in habits:
                        habits[key] = []
                    habits[key].append(int(row[key]))

    return dates, habits