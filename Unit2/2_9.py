#Write a program to do student operations using menu as follows
#a) Add Student
#b) Search Student
#c) List All Students
#d) Update Student
#e) Delete Student
#f) Exit


import os

FILENAME = "students.txt"

# ---------------- Add Student ----------------
def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = []
    for i in range(1, 5):
        marks.append(input(f"Enter Mark {i}: "))

    with open(FILENAME, "a") as file:
        file.write(",".join([roll, name] + marks) + "\n")

    print("Student added successfully.\n")


# ---------------- Search Student ----------------
def search_student():
    roll = input("Enter Roll No to search: ")
    found = False

    with open(FILENAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll:
                print("Student Found:", data)
                found = True
                break

    if not found:
        print("Student not found.\n")


# ---------------- List All Students ----------------
def list_students():
    print("\nStudent Records:\n")
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No records found.\n")
    print()


# ---------------- Update Student ----------------
def update_student():
    roll = input("Enter Roll No to update: ")
    updated = False
    records = []

    with open(FILENAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] == roll:
                print("Enter new details:")
                name = input("Enter Name: ")
                marks = []
                for i in range(1, 5):
                    marks.append(input(f"Enter Mark {i}: "))
                records.append(",".join([roll, name] + marks) + "\n")
                updated = True
            else:
                records.append(line)

    if updated:
        with open(FILENAME, "w") as file:
            file.writelines(records)
        print("Student updated successfully.\n")
    else:
        print("Student not found.\n")


# ---------------- Delete Student ----------------
def delete_student():
    roll = input("Enter Roll No to delete: ")
    deleted = False
    records = []

    with open(FILENAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if data[0] != roll:
                records.append(line)
            else:
                deleted = True

    if deleted:
        with open(FILENAME, "w") as file:
            file.writelines(records)
        print("Student deleted successfully.\n")
    else:
        print("Student not found.\n")


# ---------------- Main Menu ----------------
while True:
    print("----- Student Management Menu -----")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Students")
    print("d) Update Student")
    print("e) Delete Student")
    print("f) Exit")

    choice = input("Enter your choice: ")

    if choice == "a":
        add_student()
    elif choice == "b":
        search_student()
    elif choice == "c":
        list_students()
    elif choice == "d":
        update_student()
    elif choice == "e":
        delete_student()
    elif choice == "f":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")
