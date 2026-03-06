# 6. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(numbers):
    for i in numbers:
        print("*" *i)
        
histogram([4,9,7])