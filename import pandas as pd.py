import pandas as pd
import matplotlib.pyplot as plt

# Read the Batting spreadsheet
filepath = 'C:/Users/parrishne03/Documents/Batting.xlsx'
df = pd.read_excel(filepath)

# Filter the data for the years 1970-2023
filtered_df = df[(df['yearID'] >= 1970) & (df['yearID'] <= 2023)]

# Calculate the average batting average for each year
average_batting_average = filtered_df.groupby('yearID')['batting_average'].mean()

# Plot the average batting average on a scatterplot
plt.scatter(average_batting_average.index, average_batting_average)
plt.xlabel('Year')
plt.ylabel('Average Batting Average')
plt.title('Average Batting Average per Year')
plt.show()
