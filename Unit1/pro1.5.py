#5. Write a program to enter 10 numbers and display largest odd number from the entered number.

odd_numbers=[]

print("Enter 10 numbers=")
for i in range(10):
    num=int(input(f"number{i+1}:"))
    if num % 2!=0:
        odd_numbers.append(num)

if odd_numbers:
    largest_odd=max(odd_numbers)
    print("The Largest odd Number is:",largest_odd)
else:
    print("No odd Numbers Found.")