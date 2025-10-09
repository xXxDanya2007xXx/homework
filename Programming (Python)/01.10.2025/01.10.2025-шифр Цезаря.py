#!/usr/bin/env python3

en_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
en_lower = 'abcdefghijklmnopqrstuvwxyz'
ru_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def detect_language(text):
    for ch in text:
        if ch.lower() in ru_lower:
            return 'ru'
        elif ch.lower() in en_lower:
            return 'en'
    return None


def crypt(text, shift, encrypt=True):
    if not encrypt:
        shift = -shift

    lang = detect_language(text)
    result = ''

    if lang == 'en':
        upper, lower = en_upper, en_lower
    elif lang == 'ru':
        upper, lower = ru_upper, ru_lower
    else:
        return text

    for ch in text:
        if ch in upper:
            index = (upper.index(ch) + shift) % len(upper)
            result += upper[index]
        elif ch in lower:
            index = (lower.index(ch) + shift) % len(lower)
            result += lower[index]
        else:
            result += ch

    return result


print('1 - Зашифровать')
print('0 - Расшифровать')
mode = int(input('Ваш выбор: '))

shift = int(input('Введите ключ (целое число): '))
text = input('Введите текст: ')

if mode == 1:
    print('\nРезультат:', crypt(text, shift, encrypt=True))
else:
    print('\nРезультат:', crypt(text, shift, encrypt=False))
