import random
import string

def generate_random_email(length):
    letters = string.ascii_lowercase

    random_word = ''.join(random.choice(letters) for _ in range(length))

    email = random_word + "@gmail.com"

    return email

word_length = 7

random_email = generate_random_email(word_length)

print("Random Email:", random_email)