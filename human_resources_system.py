'''
Author: Kevin Ligan

Purpose: Team Activity - Human Resources System
'''

# Open the HR System file
with open('HR_System.txt', 'r') as file:
    # Read through the file line by line
    for line in file:
        # Strip off any leading and trailing whitespace from each line
        line = line.strip()

        # Display the line
        print(line)

        # Split the line into parts
        parts = line.split()

        # Get the name, job title, salary, and ID number
        name = parts[0]
        job_title = parts[2]
        salary = float(parts[3])
        id_number = parts[1]

        # Display the name, job title, salary, and ID number in the desired format
        print(f'{name} (ID: {id_number}), {job_title} - ${salary:.2f}')

        # Calculate the paycheck amount for the employee
        paycheck = salary * 2

        # Add $1000 bonus to paycheck for engineers
        if job_title.lower() == 'engineer':
            paycheck += 1000

        # Display the paycheck amount
        print(f'Paycheck: ${paycheck:.2f}')

# Stretch Challenge 1: 
# Implement the functionality to save the employee data into a list or dictionary for further processing.

# Stretch Challenge 2: 
# Add error handling to handle potential issues, such as missing or incorrectly formatted data in the file.

# Stretch Challenge 3: 
# Implement additional logic to calculate and display other deductions or benefits for employees, such as taxes or healthcare contributions.