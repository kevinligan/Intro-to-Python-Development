'''
Author: Kevin Ligan

Purpose: Project 07: Windchill Calculator
Overview
'''

# Function to calculate wind chill
def calculate_wind_chill(temperature, wind_speed):
    # Formula to calculate wind chill
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * wind_speed ** 0.16 + 0.4275 * temperature * wind_speed ** 0.16
    return wind_chill

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

# Prompt user for temperature input
temperature_input = float(input("Enter the temperature: "))

# Prompt the user to input Fahrenheit or Celsius
unit = input("Fahrenheit or Celsius (F/C)? ")

# Check the user's input and convert accordingly
if unit.upper() == "F":
    # Prompt the user to input the temperature in Fahrenheit
    temperature = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = (temperature - 32) * 5/9

    # Print the converted temperature in Celsius
    print("Temperature in Celsius:", celsius)

elif unit.upper() == "C":
    # Prompt the user to input the temperature in Celsius
    temperature = float(input("Enter temperature in Celsius: "))

    # Convert Celsius to Fahrenheit
    fahrenheit = (temperature * 9/5) + 32

    # Print the converted temperature in Fahrenheit
    print("Temperature in Fahrenheit:", fahrenheit)

else:
    # If the user enters an invalid input, display an error message
    print("Invalid input. Please enter 'F' for Fahrenheit or 'C' for Celsius.")


# Check if the temperature is in Celsius, convert it to Fahrenheit if needed
if temperature_input < 100:
    temperature = celsius_to_fahrenheit(temperature_input)
else:
    temperature = temperature_input

# Loop through wind speeds from 5 to 60 miles per hour, incrementing by 5
for wind_speed in range(5, 61, 5):
    # Calculate wind chill for each wind speed
    wind_chill = calculate_wind_chill(temperature, wind_speed)
    
    # Display the wind chill value with 2 decimals of precision
    print(f"Wind chill at {wind_speed} mph: {wind_chill:.2f}")

#Additional Creativity: Created a Chart
# Import the required modules
import math

# Define the function to calculate the wind chill index
def calculate_windchill(temperature, wind_speed):
    # Calculate the wind chill index using the formula
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * math.pow(wind_speed, 0.16) + 0.4275 * temperature * math.pow(wind_speed, 0.16)
    return wind_chill

# Print the wind chill chart
def print_windchill_chart():
    # Define the range of temperatures and wind speeds for the chart
    temperature_range = range(-20, 61, 10)
    wind_speed_range = range(5, 55, 5)

    # Print the header row
    print("Wind Chill Chart (in Fahrenheit)\n")
    print("Temp (F) | ", end="")

    for wind_speed in wind_speed_range:
        print(f"{wind_speed} mph | ", end="")
    print()

    # Print the data rows
    for temperature in temperature_range:
        print(f"{temperature:^9d} | ", end="")
        
        for wind_speed in wind_speed_range:
            wind_chill = calculate_windchill(temperature, wind_speed)
            print(f"{wind_chill:^9.1f} | ", end="")
        print()

# Call the function to print the wind chill chart
print_windchill_chart()
