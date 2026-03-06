'''Write a program to create function which shall accept any number of 
arguments and display total of all the numbers given as argument.'''

def total_sum(*args):
    
    total = 0
    for num in args:
        total += num
    print("Total =", total)


total_sum(10, 20, 30)        
total_sum(5, 15, 25, 35, 45) 
