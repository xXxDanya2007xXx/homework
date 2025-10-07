#!/usr/bin/env python3

def arabic_to_roman(number):
    pairs = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    roman = ""
    for val, sym in pairs:
        while number >= val:
            roman += sym
            number -= val
    return roman


def roman_to_arabic(roman):
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50,
               "C": 100, "D": 500, "M": 1000}
    roman = roman.upper()
    total = 0
    for i in range(len(roman)):
        value = symbols[roman[i]]
        if i + 1 < len(roman) and symbols[roman[i + 1]] > value:
            total -= value
        else:
            total += value
    return total


print("1 - Перевести число из арабского в римсоке")
print("2 - Перевести число из римского в арабское")

choice = input("Выберите действие: ")

if choice == "1":
    n = int(input("Введите арабское число (1–3999): "))
    if 1 <= n <= 3999:
        print("Римское число:", arabic_to_roman(n))
    else:
        print("Число должно быть в диапазоне 1–3999.")
elif choice == "2":
    r = input("Введите римское число: ")
    print("Арабское число:", roman_to_arabic(r))
else:
    print("Неверный выбор.")
