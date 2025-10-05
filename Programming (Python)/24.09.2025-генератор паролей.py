#!/usr/bin/env python3

import string
import random

spec_symbols = '!@#$%^&*'

# Код, генерирующий пароль, содержащий определённое количество букв, цифр и специальных символов
#
# letters = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
# numbers = ''.join(random.choice(string.digits) for _ in range(3))
# symbols = ''.join(random.choice(spec_symbols) for _ in range(2))
#
# unshuffled_password = letters + numbers + symbols
# shuffled_password = ''.join(random.sample(unshuffled_password, len(unshuffled_password)))
#
# print(shuffled_password)

# Код с возможностью выбора длины пароля
#
password_length = int(input('Укажите длину пароля: '))

all_chars = string.ascii_uppercase + string.digits + spec_symbols

password = ''.join(random.choice(all_chars) for _ in range(password_length))

print(password)
