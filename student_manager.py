import os

FILE_NAME = "students.txt"

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open(FILE_NAME, "a") as f:
        f.write(f"{roll},{name},{marks}\n")

    print("Student added successfully!\n")

def view_students():
    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    print("\n--- Student Records ---")
    with open(FILE_NAME, "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            print(f"Roll: {roll}, Name: {name}, Marks: {marks}")
    print()

def search_student():
    roll_to_search = input("Enter roll number to search: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    with open(FILE_NAME, "r") as f:
        for line in f:
            roll, name, marks = line.strip().split(",")
            if roll == roll_to_search:
                print(f"Found → Name: {name}, Marks: {marks}\n")
                return

    print("Student not found.\n")

def main():
    while True:
        print("==== STUDENT MANAGEMENT ====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
