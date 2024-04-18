import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate average batting average per age bin for a given season
def calculate_average_batting_average_per_age(file_path_people, file_path_batting, season_year):
    # Read the People Excel file
    people_data = pd.read_excel(file_path_people)

    # Filter out players whose final debut game occurred before the given season
    people_data = people_data[people_data['finalGame'].dt.year >= season_year]

    # Calculate age based on April 1 of the season year
    current_year = season_year
    current_month = 4
    current_day = 1

    # Convert birthYear, birthMonth, and birthDay to integers
    people_data['birthYear'] = people_data['birthYear'].astype(int)
    people_data['birthMonth'] = people_data['birthMonth'].astype(int)
    people_data['birthDay'] = people_data['birthDay'].astype(int)

    # Calculate age
    people_data['age'] = current_year - people_data['birthYear']
    people_data.loc[(people_data['birthMonth'] > current_month) | ((people_data['birthMonth'] == current_month) & (people_data['birthDay'] > current_day)), 'age'] -= 1

    # Read the Batting Excel file
    batting_data = pd.read_excel(file_path_batting)

    # Merge batting data with people data based on playerID
    merged_data = pd.merge(batting_data, people_data, on='playerID', how='inner')

    # Calculate batting average (BA) per player
    merged_data['BA'] = merged_data['H'] / merged_data['AB']

    # Group batting data by age and calculate average batting average per age group
    average_batting_average_per_age = merged_data.groupby('age')['BA'].mean().reset_index()

    return average_batting_average_per_age

# File paths
people_file_path = r'C:\Users\parrishne03\Documents\People.xlsx'
batting_file_path = r'C:\Users\parrishne03\Documents\Batting.xlsx'

# List to store average batting average per age bin for each season
average_batting_average_per_age_all_seasons = []

# Calculate average batting average per age bin for each season from 2010 to 2022
for season_year in range(2019, 2023):
    average_batting_average_per_age = calculate_average_batting_average_per_age(people_file_path, batting_file_path, season_year)
    average_batting_average_per_age_all_seasons.append(average_batting_average_per_age)

# Calculate aggregate average for each age bin
aggregate_average_batting_average_per_age = pd.concat(average_batting_average_per_age_all_seasons).groupby('age')['BA'].mean().reset_index()

# Find the age bin with the highest average batting average
best_age_bin = aggregate_average_batting_average_per_age.loc[aggregate_average_batting_average_per_age['BA'].idxmax()]

# Plot histogram of aggregate average batting average against age
plt.figure(figsize=(10, 6))
plt.bar(aggregate_average_batting_average_per_age['age'], aggregate_average_batting_average_per_age['BA'], color='skyblue')
plt.xlabel('Age')
plt.ylabel('Average Batting Average')
plt.title('Aggregate Average Batting Average by Age Group (2019-2023)')
plt.grid(True)
plt.show()

print(f"The age bin with the highest average batting average is {best_age_bin['age']} years old, with an average batting average of {best_age_bin['BA']:.3f}.")
