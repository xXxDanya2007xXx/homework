#!/usr/bin/env python3

# def find_digit():
#     string = input("Введите строку чисел: ")
#     n = int(input("Введите число N: "))
#     print(string[n])

def find_digit(n: int):
    length = 1  # длина числа (1 для 1-9, 2 для 10-99, etc.)
    count = 9   # сколько чисел в группе
    start = 1   # начальное число группы

    # пока позиция не находится в текущем диапазоне
    while n > length * count:
        n -= length * count
        length += 1
        count *= 10
        start *= 10

    number = start + (n) // length
    digit_index = (n) % length
    print(int(str(number)[digit_index]))


if __name__ == "__main__":
    while True:
        try:
            n = int(input("Введите число N: "))
        except ValueError:
            print("Err: Введите целое число.")
            continue
        break

    find_digit(n)
