first_name = input('First name:')
last_name = input('Last name:')
email_Address = input('Email address:')
phone_number = input('Phone Number:')
job_title = input('Job title:')
id_number = input('ID number:')
hair = input('Hair Color:')
eyes = input('Eyes color:')
month = input('Month:')
training = input('Completed additional training?')

print(f'{last_name.upper()}, {first_name.capitalize()}')
print(job_title.title())
print(f'ID: {id_number}')
print(' ' * 21)
print(email_Address.lower())
print(phone_number)
print(' ' * 21)
print(f'Hair: {hair:15} Eyes: {eyes}')
print(f'Month: {month:14} Training: {training}')