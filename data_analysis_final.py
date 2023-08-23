'''
Author: Kevin Ligan
Purpose: Project 06: Data Analysis - Final
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

# Additional Creativity:
# - Find the year and country with the largest drop in life expectancy from one year to the next
largest_drop_year = ""
largest_drop_country = ""
largest_drop = 0

for i in range(2, len(data)):
    current_life_expectancy = float(data[i][3])
    previous_life_expectancy = float(data[i-1][3])
    drop = previous_life_expectancy - current_life_expectancy
    if drop > largest_drop:
        largest_drop = drop
        largest_drop_year = data[i][0]
        largest_drop_country = data[i][1]

# Print the year, country, and largest drop in life expectancy
print(f"The year and country with the largest drop in life expectancy: {largest_drop_year}, {largest_drop_country}")
print(f"The largest drop in life expectancy: {largest_drop}")

# Allow the user to input a country and find the minimum, maximum, and average life expectancy for that country
country = input("Enter a country: ")
country_life_expectancies = []

for row in data[2:]:
    if row[1] == country:
        country_life_expectancies.append(float(row[3]))

if country_life_expectancies:
    min_life_expectancy = min(country_life_expectancies)
    max_life_expectancy = max(country_life_expectancies)
    average_life_expectancy = sum(country_life_expectancies) / len(country_life_expectancies)

    # Print the minimum, maximum, and average life expectancy for the given country
    print(f"The minimum life expectancy for {country}: {min_life_expectancy}")
    print(f"The maximum life expectancy for {country}: {max_life_expectancy}")
    print(f"The average life expectancy for {country}: {average_life_expectancy}")
else:
    print("No data available for the given country.")

# Additional Feature:
# - Identify the year and country with the largest increase in life expectancy from one year to the next
largest_increase_year = ""
largest_increase_country = ""
largest_increase = 0

for i in range(2, len(data)):
    current_life_expectancy = float(data[i][3])
    previous_life_expectancy = float(data[i-1][3])
    increase = current_life_expectancy - previous_life_expectancy
    if increase > largest_increase:
        largest_increase = increase
        largest_increase_year = data[i][0]
        largest_increase_country = data[i][1]

# Print the year, country, and largest increase in life expectancy
print(f"The year and country with the largest increase in life expectancy: {largest_increase_year}, {largest_increase_country}")
print(f"The largest increase in life expectancy: {largest_increase}")
