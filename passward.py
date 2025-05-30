import random
import string

def generate_password(length=12):
    # Define possible characters: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly choose characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example: Generate a 12-character password
print("Generated Password:", generate_password(12))