# random password generator

import random
from random import randint

# for all uppercase and lower passwords

password = ''
for x in range(3):
    x = chr(randint(65, 90))
    for k in range(2):
        k = chr(randint(65, 90)).lower()
        z = random.randint(0, 10)
        password = str(password) + x + k + str(z)
print(password)
