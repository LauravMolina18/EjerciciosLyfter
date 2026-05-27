from menu import show_menu, get_option
from actions import (
    add_students,
    show_students,
    top_3_students,
    class_average
)
from data import export_csv, import_csv


def main():
    students = []

    while True:
        show_menu()
        option = get_option()

        if option == "1":
            add_students(students)

        elif option == "2":
            show_students(students)

        elif option == "3":
            top_3_students(students)

        elif option == "4":
            class_average(students)

        elif option == "5":
            export_csv(students)

        elif option == "6":
            students = import_csv()

        elif option == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()