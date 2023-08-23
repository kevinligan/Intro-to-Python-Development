'''
Author: Kevin Ligan
Purpose: Project 06: Data Analysis - Milestones
'''


# Load the dataset
data = []
with open('dataset.csv') as file:
    for line in file:
        # Split each line into parts
        parts = line.strip().split(',')
        data.append(parts)

# Find the lowest and highest life expectancy values in the dataset
lowest_life_expectancy = float(data[1][3])  # Assuming life expectancy values are in the 4th column
highest_life_expectancy = float(data[1][3])

for row in data[2:]:  # Start from the second row
    life_expectancy = float(row[3])
    if life_expectancy < lowest_life_expectancy:
        lowest_life_expectancy = life_expectancy
    if life_expectancy > highest_life_expectancy:
        highest_life_expectancy = life_expectancy

# Print the lowest and highest life expectancy values
print(f"The lowest life expectancy is: {lowest_life_expectancy}")
print(f"The highest life expectancy is: {highest_life_expectancy}")

# Find the year and country with the lowest and highest life expectancy values
lowest_country = ""
lowest_year = ""
highest_country = ""
highest_year = ""

for row in data[2:]:
    if float(row[3]) == lowest_life_expectancy:
        lowest_country = row[1]  # Assuming country names are in the 2nd column
        lowest_year = row[0]  # Assuming year values are in the 1st column
    if float(row[3]) == highest_life_expectancy:
        highest_country = row[1]
        highest_year = row[0]

# Print the year and country with the lowest and highest life expectancy values
print(f"The year and country with the lowest life expectancy: {lowest_year}, {lowest_country}")
print(f"The year and country with the highest life expectancy: {highest_year}, {highest_country}")

# Allow the user to input a year
year = input("Enter a year: ")

# Find the average life expectancy for the given year
total_life_expectancy = 0
count = 0

for row in data[2:]:
    if row[0] == year:
        total_life_expectancy += float(row[3])
        count += 1

if count > 0:
    average_life_expectancy = total_life_expectancy / count
    # Find the country with the minimum and maximum life expectancies for the given year
    min_country = ""
    min_life_expectancy = float('inf')
    max_country = ""
    max_life_expectancy = float('-inf')

    for row in data[2:]:
        if row[0] == year:
            life_expectancy = float(row[3])
            if life_expectancy < min_life_expectancy:
                min_country = row[1]
                min_life_expectancy = life_expectancy
            if life_expectancy > max_life_expectancy:
                max_country = row[1]
                max_life_expectancy = life_expectancy

    # Print the average life expectancy, country with minimum and maximum life expectancies for the given year
    print(f"The average life expectancy for {year}: {average_life_expectancy}")
    print(f"The country with the minimum life expectancy for {year}: {min_country}")
    print(f"The country with the maximum life expectancy for {year}: {max_country}")
else:
    print("No data available for the given year.")


