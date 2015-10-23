__author__ = 'duye'

import string

def alphabet_digit_cycle():
    d = 0
    while True:
        d += 1
        for c in string.ascii_lowercase:
            yield c+str(d)

it= alphabet_digit_cycle()
for c in it:
    print(c)

