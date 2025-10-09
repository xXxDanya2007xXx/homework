#!/usr/bin/env python3

import string
import random

spec_symbols = "!@#$%^&*"


def gen_password(use_lower, use_upper, use_specials, use_digits, length):
    pool = ""
    if use_lower:
        pool += string.ascii_lowercase
    if use_upper:
        pool += string.ascii_uppercase
    if use_specials:
        pool += spec_symbols
    if use_digits:
        pool += string.digits

    if not pool:
        return "Ошибка: вы не выбрали ни одного типа символов."

    password = "".join(random.choice(pool) for _ in range(length))
    return password


use_lower = int(
    input("Добавить буквы нижнего регистра? (1 - Да, 0 - Нет): "))
use_upper = int(input("Добавить буквы верхнего регистра? (1 - Да, 0 - Нет): "))
use_specials = int(
    input("Добавить спецсимволы (!@#$%^&*)? (1 - Да, 0 - Нет): "))
use_digits = int(input("Добавить цифры? (1 - Да, 0 - Нет): "))
length = int(input("Укажите длину пароля: "))

print("\nВаш пароль:")
print(gen_password(use_lower, use_upper, use_specials, use_digits, length))
