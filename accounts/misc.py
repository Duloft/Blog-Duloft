import random
import string

# Define the characters that can be used in the random string, including symbols
characters = string.ascii_letters + string.digits + string.punctuation

# Generate a random string of length 50
random_string = ''.join(random.choice(characters) for _ in range(55))

print(random_string)
