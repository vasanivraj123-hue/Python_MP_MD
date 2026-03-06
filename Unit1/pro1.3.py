#Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)

name = input('Enter your name :')
m1=int(input('Enter Mark 1 Maths :'))
m2=int(input('Enter Mark 2 English :'))
m3=int(input('Enter Mark 3 Gujrati :'))
m4=int(input('Enter Mark 4 Computer :'))

total = (m1+m2+m3+m4)
per = (total/400)*100

if per >=90:
    grade = 'O'
elif per >=75:
    grade = 'A'
elif per >=60:
    grade = 'B'
elif per >=50:
    grade = 'C'
elif per >=40:
    grade = 'D'
else :
    grade ='Fail'

print('\n*******Result*******')
print('Name :',name)
print('Total Mark out of 400:',total)
print('persentage :',per)
print('Grade :',grade)
