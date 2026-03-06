#Write a program to read file which has marks entry of student and displaydetails with total, percentage and grade (Consider a file which hascomma separated data with RollNo, Student Name, Mark1, Mark2, Mark3and Mark4)


try:
    with open("students.txt", "r") as file:
        print("Student Details:\n")
        print("RollNo  Name     Total  Percentage  Grade")
        print("---------------------------------------------")

        for line in file:
            data = line.strip().split(",")

            roll_no = data[0]
            name = data[1]
            marks = list(map(float, data[2:]))

            total = sum(marks)
            percentage = total / len(marks)

            # Grade Calculation
            if percentage >= 90:
                grade = "A"
            elif percentage >= 75:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 40:
                grade = "D"
            else:
                grade = "F"

            print(f"{roll_no:<7} {name:<8} {total:<6} {percentage:.2f}%     {grade}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception:
    print("Error: Invalid data format in file.")
