#!/usr/bin/env python3

text = input('Введите строку: ').lower()

char_count = {}

for char in text:
    if char in char_count.keys():
        char_count[char] += 1
    else:
        char_count[char] = 1

sorted_char_count = sorted(char_count.items(), key=lambda item: item[1], reverse=True)

print(sorted_char_count[:3])
