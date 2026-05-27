def get_valid_grade(subject):
    grade = input(f"Enter {subject} grade (0-100): ")

    while not grade.isdigit() or int(grade) < 0 or int(grade) > 100:
        print("Invalid grade. Must be between 0 and 100.")
        grade = input(f"Enter {subject} grade (0-100): ")

    return int(grade)


def add_students(students):
    n = input("How many students do you want to add?: ")

    while not n.isdigit() or int(n) <= 0:
        print("Invalid number.")
        n = input("How many students do you want to add?: ")

    n = int(n)

    for i in range(n):
        print(f"\nStudent {i + 1}")

        name = input("Full name: ")
        section = input("Section (e.g. 11B): ")

        spanish = get_valid_grade("Spanish")
        english = get_valid_grade("English")
        social = get_valid_grade("Social Studies")
        science = get_valid_grade("Science")

        students.append({
            "name": name,
            "section": section,
            "spanish": spanish,
            "english": english,
            "social": social,
            "science": science
        })


def show_students(students):
    if not students:
        print("No students registered.")
        return

    for s in students:
        print("\n-------------------")
        print(f"Name: {s['name']}")
        print(f"Section: {s['section']}")
        print(f"Spanish: {s['spanish']}")
        print(f"English: {s['english']}")
        print(f"Social: {s['social']}")
        print(f"Science: {s['science']}")


def student_average(student):
    return (student["spanish"] +
            student["english"] +
            student["social"] +
            student["science"]) / 4


def top_3_students(students):
    if not students:
        print("No students registered.")
        return

    sorted_students = sorted(students, key=student_average, reverse=True)

    print("\nTOP 3 STUDENTS:")

    for i, s in enumerate(sorted_students[:3]):
        print(f"\n#{i + 1}")
        print(f"Name: {s['name']}")
        print(f"Average: {student_average(s):.2f}")


def class_average(students):
    if not students:
        print("No students registered.")
        return

    total = 0

    for s in students:
        total += student_average(s)

    avg = total / len(students)

    print(f"\nClass average: {avg:.2f}")