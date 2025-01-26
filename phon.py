import re

def generate_phone_numbers(last_digits):
    if not re.match(r'^\d{4}$', last_digits):
        raise ValueError("Last digits must be exactly four numeric digits")
    
    prefixes = [str(i) for i in range(1, 10)]
    phone_numbers = []
    
    for prefix in prefixes:
        for i in range(1000, 100000):
            phone_number = prefix + str(i).zfill(4) + last_digits
            phone_numbers.append(phone_number)
    
    with open('phonenumbers.txt', 'w') as file:
        file.write('\n'.join(phone_numbers))
    print("by MASTER-HACK")
    print(f"Total count of generated phone numbers: {len(phone_numbers)}")

# User input
last_digits = input("Enter the last 4 digits of the Indian phone number: ")

try:
    generate_phone_numbers(last_digits)
except ValueError as e:
    print(e)
