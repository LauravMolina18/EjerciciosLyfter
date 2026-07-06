def show_menu():
    print("STUDENT CONTROL SYSTEM")
    print("-----------------------")
    print("1. Add students")
    print("2. Show all students")
    print("3. Top 3 students")
    print("4. Class average")
    print("5. Export to CSV")
    print("6. Import from CSV")
    print("7. Exit")


def get_option():
    option = input("Select an option: ")

    while option not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid option.")
        option = input("Select an option (1-7): ")

    return option