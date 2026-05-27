import csv


def export_csv(students):
    if not students:
        print("No data to export.")
        return

    filename = "students.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["name", "section", "spanish", "english", "social", "science"])

        for s in students:
            writer.writerow([
                s["name"],
                s["section"],
                s["spanish"],
                s["english"],
                s["social"],
                s["science"]
            ])

    print("Data exported successfully to students.csv")


def import_csv():
    filename = "students.csv"
    students = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append({
                    "name": row["name"],
                    "section": row["section"],
                    "spanish": int(row["spanish"]),
                    "english": int(row["english"]),
                    "social": int(row["social"]),
                    "science": int(row["science"])
                })

        print("Data imported successfully.")

    except FileNotFoundError:
        print("No exported file found.")

    return students