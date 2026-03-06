#Write a program to execute user defined exception in python.
class NegativeNumberError(Exception):
    pass

try:
    num = int(input("Enter a positive number: "))
    
    if num < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    
    print("You entered:", num)

except NegativeNumberError as e:
    print("User Defined Exception Caught:", e)

except ValueError:
    print("Invalid input. Please enter an integer.")

finally:
    print("Program execution completed.")
