'''Write a Python program to perform following operation on given string 
input:
a) Count Number of Vowel in given string
b) Count Length of string (donot use len() )
c) Reverse string
d) Find and replace operation
e) check whether string entered is a palindrome or not'''

def vowel(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def length(s):
    count = 0
    for char in s :
        count +=1
    return count

def reverse(s):
    return s[::-1]

def find_replace(s,find,replace):
    return s.replace(find,replace)

def palindrom(s):
    s = s.lower()
    return s == s[::-1]
    


str_input = input('Enter a String :')
print('number of vowel :',vowel(str_input))
print('Length of String :',length(str_input))
print('Reverse String :',reverse(str_input))

find=input('Enter substring for find:')
replace=input('Enter subdtring for replace with :')
print("String after replace:",find_replace(str_input,find,replace))

if palindrom(str_input):
    print('String is palindrom')
else:
    print('String is not palindrom')

