import secrets
import string

def secret_passoword():
    password = ""

    for x in range(4):
        letters = secrets.choice(string.ascii_letters)
        numbers = secrets.choice(string.digits)
        symbols = secrets.choice(string.punctuation)

        password += letters + numbers + symbols

    secret_password = "".join(secrets.choice(password) for x in range(len(password)))

    return print(secret_password)

secret_passoword()
