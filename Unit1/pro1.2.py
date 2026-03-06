#Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input

num1=float(input('Enter number 1:'))
num2=float(input('Enter number 2:'))

oprt = input('Enter operator (+,-,*,/) :')

if oprt == '+' :
    result = num1+num2
elif oprt == '-':
    result = num1-num2
elif oprt == '*':
    result = num1*num2
elif oprt == '/':
    if num2 != 0:
        result = num1/num2
    else :
        result = 'Error !! Division by zero..'
else:
    result = 'Please, Enter valid Oprator..'

print('Result :',result)
