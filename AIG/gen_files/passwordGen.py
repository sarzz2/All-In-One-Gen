import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation


def passw(length):
    x = ''.join(random.choice(LETTERS + NUMBERS + PUNCTUATION) for i in range(length))
    return x


passw(10)
