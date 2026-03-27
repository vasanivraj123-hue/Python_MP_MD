import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("student.xlsx")

gender_count = df['Gender'].value_counts()

print("Gender Count:\n", gender_count)

plt.bar(gender_count.index, gender_count.values)

plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.title("Male vs Female Students")

plt.show()
