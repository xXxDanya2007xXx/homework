#!/usr/bin/env python3

# Проверяем количество и порядок расставления скобок
def check_brackets(expression: str):
    stack = []

    for ch in expression:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return False
            stack.pop()

    return not stack


if __name__ == "__main__":
    expression = input('Введите выражение: ')
    print(check_brackets(expression))
