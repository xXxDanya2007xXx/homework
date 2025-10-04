#!/usr/bin/env python3

number = int(input('Введите число: '))

if number == 0:
    print('Число равно 0, чётное, не принадлежит диапазону [10,50]')
else:
    if number > 0:
        print('Число больше 0')
    else:
        print('Число меньше 0')

    print('Число чётное' if number % 2 == 0 else 'Число нечётное')
    print('Число принадлежит отрезку [10,50]' if 10 <= number <= 50 \
            else 'Число не принадлежит отрезку [10,50]')
