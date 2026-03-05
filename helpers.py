import string
import random


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_random_email(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(length)) + '@gmail.com'
    return random_string
