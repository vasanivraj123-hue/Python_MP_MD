import pandas as pd
import re

# Load Excel file
df = pd.read_excel("student.xlsx")

print("Original Data:\n", df)

# Regex pattern for mobile number with country code (e.g., 91-9999933333)
pattern = r'^\d{2}-\d{10}$'

# Filter records with valid mobile numbers
valid_mobile = df[df['Mobile'].apply(lambda x: bool(re.match(pattern, str(x))))]

print("\nRecords with Valid Mobile Numbers (with country code):\n", valid_mobile)
