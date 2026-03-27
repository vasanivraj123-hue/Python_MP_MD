import pandas as pd

df = pd.read_excel("student.xlsx")

print("Full Data:\n", df)

rajkot_students = df[df['City'] == 'Rajkot']
print("\nStudents from Rajkot City:\n", rajkot_students)

male_students = df[df['Gender'] == 'Male']
print("\nMale Students:\n", male_students)

male_rajkot = df[(df['City'] == 'Rajkot') & (df['Gender'] == 'Male')]
print("\nMale Students from Rajkot City:\n", male_rajkot)

age_20 = df[df['Age'] >= 20]
print("\nStudents with Age >= 20:\n", age_20)
