import re

def validate_name(name):
    if re.match(r'^[a-zA-Z\s]+$', name):
        return True
    else:
        return False

def validate_reg(reg):
    if re.match(r'^21411[0-6]{1}[0-9]{1}$', reg):
        return True
    else:
        return False

def validate_age(age):
    if re.match(r'^\d+$', age):
        return True
    else:
        return False

def validate_phone_number(phone_number):
    if re.match(r'^\d{10}$', phone_number):
        return True
    else:
        return False

def validate_gmail(gmail):
    if re.match(r'^[a-zA-Z0-9.!#$%&*+/=?^_{|}~-]+@gmail.com$', gmail):
        return True
    else:
        return False

def validate_gender(gender):
    if gender in ['Male', 'Female','male','female','others', 'Other']:
        return True
    else:
        return False

def validate_password(password):
    if re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$', password):
        return True
    else:
        return False

def validate_dob(dob):
     if re.match(r'^\d{2}/\d{2}/\d{4}$', dob):
        return True
     else:
        return False

# Example usage
reg = input('Enter the registration number: ')
if not validate_reg(reg):
    print('Invalid reg')

name = input('Enter your name: ')
if not validate_name(name):
    print('Invalid name')

age = input('Enter your age: ')
if not validate_age(age):
    print('Invalid age')

phone_number = input('Enter your phone number: ')
if not validate_phone_number(phone_number):
    print('Invalid phone number')

gmail = input('Enter your gmail address: ')
if not validate_gmail(gmail):
    print('Invalid gmail address')

gender = input('Enter your gender (Male/Female/Other): ')
if not validate_gender(gender):
    print('Invalid gender')

password = input('Enter your password: ')
if not validate_password(password):
    print('Invalid password')

dob = input('Enter your date of birth (dd/mm/yyyy): ')
if not validate_dob(dob):
    print('Invalid date of birth')
