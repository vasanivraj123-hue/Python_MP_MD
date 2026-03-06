#Write a program to display basic exception handling in python.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
except ValueError:
    print("Error: Please enter valid integers only.")
    
except Exception as e:
    print("Unexpected error occurred:", e)
    
else:
    print("Result:", result)
    
finally:
    print("Execution completed.")
