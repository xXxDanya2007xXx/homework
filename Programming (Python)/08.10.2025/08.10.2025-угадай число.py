#!/usr/bin/env python3

import random


def guess_number():
    guessed = random.randint(1, 100)
    attempts = 3

    while attempts > 0:
        try:
            user_input = input(f"Осталось попыток: {
                               attempts}. Введите число (1–100): ").strip()
            if not user_input:
                print("Ошибка ввода. Пустая строка.")
                continue
            number = int(user_input)
        except ValueError:
            print("Ошибка ввода. Введите целое число.")
            continue

        if not 1 <= number <= 100:
            print("Ошибка ввода. Число вне диапазона 1–100.")
            continue

        if number == guessed:
            print(f"Вы выиграли! Загаданное число: {guessed}")
            return
        elif number > guessed:
            print("Загаданное число меньше.")
        else:
            print("Загаданное число больше.")

        attempts -= 1

        if attempts == 1:
            hint = "чётное" if guessed % 2 == 0 else "нечётное"
            print(f"Подсказка: загаданное число {hint}.")

    print(f"Вы проиграли. Загаданное число: {guessed}")


if __name__ == "__main__":
    guess_number()
