from faker import Faker
import random
import string

fake = Faker(['ru_RU'])

def generate_name():
    return fake.name()    

def generate_login():
    return fake.free_email()

def generate_valid_password():
    valid_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))
    return valid_password

def generate_invalid_password():
    invalid_password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return invalid_password