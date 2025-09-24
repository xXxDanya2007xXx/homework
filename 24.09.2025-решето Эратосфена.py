#!/usr/bin/env python3

N = int(input('введите число N: '))

list_of_primary_numbers = []

for number in range(2, N + 1):
    is_prime = True
    for i in list_of_primary_numbers:
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        list_of_primary_numbers.append(number)

print(list_of_primary_numbers)
