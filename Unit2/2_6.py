#Write a program to read a file which contains only numbers. Display total of all numbers with maximum and minimum number.
try:
    with open("numbers.txt", "r") as file:
        numbers = []

        
        for line in file:
            for num in line.split():
                numbers.append(float(num)) 

        if len(numbers) == 0:
            print("File is empty.")
        else:
            total = sum(numbers)
            maximum = max(numbers)
            minimum = min(numbers)

            print("Numbers in file:", numbers)
            print("Total:", total)
            print("Maximum:", maximum)
            print("Minimum:", minimum)

except FileNotFoundError:
    print("Error: File not found.")
except ValueError:
    print("Error: File contains non-numeric data.")
