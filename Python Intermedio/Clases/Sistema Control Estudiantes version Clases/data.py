import csv
from student import Student


def export_csv(students):
    if not students:
        print("No data to export.")
        return

    filename = "students.csv"

    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "name",
            "section",
            "spanish",
            "english",
            "social",
            "science"
        ])

        for s in students:
            student_dict = {
                "name": s.name,
                "section": s.section,
                "spanish": s.spanish,
                "english": s.english,
                "social": s.social,
                "science": s.science
            }

            writer.writerow([
                student_dict["name"],
                student_dict["section"],
                student_dict["spanish"],
                student_dict["english"],
                student_dict["social"],
                student_dict["science"]
            ])

    print("Data exported successfully to students.csv")


def import_csv():
    filename = "students.csv"
    students = []

    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                students.append(
                    Student(
                        row["name"],
                        row["section"],
                        int(row["spanish"]),
                        int(row["english"]),
                        int(row["social"]),
                        int(row["science"])
                    )
                )

        print("Data imported successfully.")

    except FileNotFoundError:
        print("No exported file found.")

    return students