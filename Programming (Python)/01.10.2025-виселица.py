#!/usr/bin/env python3

import random

words = ["компьютер", "код", "программа", "тайленол",
         "дуст", "дихлордифенилтрихлорметилметан"]

word = random.choice(words)
guessed = ["_" for _ in word]
used_letters = set()
attempts = 6

print("Загадано слово из", len(word), "букв.")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    letter = input("\nВведите букву: ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Введите одну букву.")
        continue
    if letter in used_letters:
        print("Вы уже вводили эту букву.")
        continue

    used_letters.add(letter)

    if letter in word:
        print("Есть такая буква.")
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Нет такой буквы. Осталось попыток:", attempts)

    print(" ".join(guessed))

if "_" not in guessed:
    print("Вы отгадали слово:", word)
else:
    print("Вы проиграли. Загаданное слово было:", word)
