import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(characters, k=length - 4)
    random.shuffle(password)
    return ''.join(password)

try:
    length = int(input("Enter desired password length (minimum 4): "))
    if length < 4:
        print("Password length should be at least 4 characters for security.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number for password length.")
