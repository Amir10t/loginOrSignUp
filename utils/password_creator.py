from random import randint
def number_password_generator(r):
    password = ""
    for i in range(r):
        password += str(randint(0,9))

    return password