#1MCAB Python Programming
#LAB EXERCISE 6

#Q1. Write a program using the Regular Exception and create a function that accepts a string and searches it for a valid phone number. Return the phone number if found. A valid phone number may be one of the following: (xxx)-xxx-xxxx or xxx-xxx-xxxx

print("Q1. ")

import re

def find_phone_number(text):
    pattern = r"(\(\d{3}\)-\d{3}-\d{4}|\d{3}-\d{3}-\d{4})"
    
    match = re.search(pattern, text)

    if match:
        return match.group()
    else:
        return None

text = input("Enter the string: ")
result = find_phone_number(text)

if result:
    print("Found phone number:", result)
else:
    print("No valid phone number found.")


# #Q2. Write a function that employs regular expressions to ensure the password given to the function is strong.
# A strong password is defined as follows:
# ·       at least eight characters long
# ·       contains one uppercase character
# ·       contains one lowercase character
# ·       has at least one digit
# ·       has at least one special character

print("Q2. ")

import re

def strong_password(text):
  pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=!]).{8,}$"
  
  if re.match(pattern, password):
    return True
  else:
    return False

password = input("Enter the password: ")

if strong_password(password):
  print("Password is strong!")
else:
  print("Password is weak!")
  
