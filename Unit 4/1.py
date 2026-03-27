import pandas as pd

file_path = "student.xlsx"   
df = pd.read_excel(file_path)

print("Columns in the Excel file:")
print(df.columns.tolist())

print("\nData types of each column:")
print(df.dtypes)

