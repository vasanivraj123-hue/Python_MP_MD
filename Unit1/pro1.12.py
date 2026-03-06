#Write a program to display the use of local, global and nonlocal variables

# Global variable
x = "I am Global"

def outer_function():
    # Local variable inside outer_function
    y = "I am Local to outer_function"

    def inner_function():
        # Nonlocal variable (refers to y in outer_function)
        nonlocal y
        y = "I am Nonlocal (modified in inner_function)"
        print("Inside inner_function:", y)

    print("Before calling inner_function:", y)
    inner_function()
    print("After calling inner_function:", y)

# Demonstration
print("Global variable:", x)
outer_function()
