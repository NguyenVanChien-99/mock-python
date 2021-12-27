import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")
password_length = 10


def password_generate():
    random.shuffle(characters)
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))
    random.shuffle(password)
    return "".join(password)
