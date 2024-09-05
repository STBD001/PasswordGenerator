import random
import string


def generate_password(length=12):
    letters = string.ascii_letters
    numbers = string.digits
    special = string.punctuation

    summary = letters + numbers + special

    password = ''.join(random.choice(summary) for i in range(length))

    return password


def save_password_to_file(password, filename="passwords.txt"):
    with open(filename, 'a') as file:
        file.write(password + '\n')


if __name__ == '__main__':
    password = generate_password(16)
    print("Wygenerowane hasło:", password)

    save_password_to_file(password)
