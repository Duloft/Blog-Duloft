import random
import string

# Define the characters that can be used in the random string, including symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random string of length 50
random_string = ''.join(random.choice(characters) for _ in range(55))

print(random_string)



# import secrets
# import string

# # Define the characters to choose from for the password
# characters = string.ascii_letters + string.digits

# # Set the password length
# password_length = 18

# # Generate the password
# password = ''.join(secrets.choice(characters) for _ in range(password_length))

# print(password)
