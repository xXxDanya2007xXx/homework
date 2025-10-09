#!/usr/bin/env python3

def print_pack_report(N):
    for i in range(N, 1, -1):
        if i % 5 == 0 and i % 3 == 0:
            print(f"{i} - расфасуем по 3 или по 5")
        elif i % 5 == 0:
            print(f"{i} - расфасуем по 5")
        elif i % 3 == 0:
            print(f"{i} - расфасуем по 3")
        else:
            print(f"{i} - не заказываем!")


N = int(input('Введите количество пирожных: '))
print_pack_report(N)
