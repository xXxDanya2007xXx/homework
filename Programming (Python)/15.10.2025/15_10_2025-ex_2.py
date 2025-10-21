#!/usr/bin/env python3

def check_brackets(expression: str):
    stack = []

    for ch in expression:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()

    if not stack:
        return 'Количество и положение скобок корректны.'
    else:
        return 'Количество и положение скобок некорректны.'


if __name__ == "__main__":
    expression = input('Введите выражение: ')

    print(check_brackets(expression))
