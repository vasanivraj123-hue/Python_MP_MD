import pandas as pd

df = pd.read_excel("student.xlsx")

print("Original Data:\n", df)


dropna_df = df.dropna()

print("\nData after using dropna():\n", dropna_df)

fillna_df = df.fillna({
    'Name': 'Unknown',
    'Age': 0,
    'City': 'Not Specified',
    'Gender': 'Not Specified'
})

print("\nData after using fillna():\n", fillna_df)
