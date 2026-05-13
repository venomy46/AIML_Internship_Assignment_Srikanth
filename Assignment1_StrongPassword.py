import hashlib
import re

# Function to hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to validate password strength
def is_strong_password(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False
    return True

# User Registration
def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if not is_strong_password(password):
        print("Password must be at least 8 characters long and include uppercase, lowercase, number, and special character.")
        return None, None

    hashed_password = hash_password(password)
    print("Registration successful!")
    return username, hashed_password

# User Login
def login(stored_username, stored_password):
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == stored_username and hash_password(password) == stored_password:
        print("Login successful. Access granted.")
    else:
        print("Invalid username or password. Access denied.")

# Main Program
stored_username, stored_password = register()
if stored_username:
    login(stored_username, stored_password)