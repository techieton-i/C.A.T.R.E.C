import random
import string


def populator(number):
    validators = []
    for x in range(0, number):
        text = ''
        a = 0
        while a < 10:
            x = random.randint(0, 9)
            text += str(x)
            a += 1
        b = 0
        while b < 2:
            x = random.choice(tuple(string.ascii_uppercase))
            text += x
            b += 1
        validators.append(text)
    return validators

