#!/usr/bin/env python3

scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28]


def check_winners(scores, student_score):
    if student_score in sorted(scores, reverse=True)[:3]:
        print('Вы в тройке победителей!')
    else:
        print('Вы не попали в тройку победителей.')


student_score = int(input('Введите свой результат: '))

check_winners(scores, student_score)
