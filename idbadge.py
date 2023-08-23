
print('Please enter the following information')

print()

# Basic information
first = input('First name: ')
last = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
job_title = input('Job title: ')
id_number = input('ID Number: ')

# Additional information
hair_color = input('Hair color: ')
eye_color = input('Eye color: ')
month = input('Starting month: ')
training = input('Did you ompleted you additional training? ')

#ID card
print(' \nThe ID Card is: ')
print('============================================')
print(f' {last.upper()}, {first.capitalize()}.')
print(job_title.title())
print(f'ID: {id_number}')
print()
print(email.lower())
print(phone)
print()
print(f'Hair: {hair_color:} Eyes: {eye_color}')
print(f'Month: {month:} Training: {training:}')
print('============================================')