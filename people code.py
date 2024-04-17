import pandas as pd

# Read the Excel file
file_path = r'C:\Users\breckheiha05\Documents\People.xlsx'
data = pd.read_excel(file_path)

# Calculate age based on April 1, 2024
current_year = 2024
current_month = 4
current_day = 1

# Convert birthYear, birthMonth, and birthDay to integers
data['birthYear'] = data['birthYear'].astype(int)
data['birthMonth'] = data['birthMonth'].astype(int)
data['birthDay'] = data['birthDay'].astype(int)

# Calculate age
data['age'] = current_year - data['birthYear']
data.loc[(data['birthMonth'] > current_month) | ((data['birthMonth'] == current_month) & (data['birthDay'] > current_day)), 'age'] -= 1

# Print the calculated information
print(data[['playerID', 'age']])
