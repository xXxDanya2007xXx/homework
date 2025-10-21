#!/usr/bin/env python3

def move_char(text: str, X: str):

    while True:
        direction = input(
            'Куда переместить символы (начало/конец)?: ').strip().lower()
        if direction not in ['начало', 'конец']:
            print('Err: введите `начало` или `конец`.')
            continue
        break

    count = text.count(X)
    others = text.replace(X, '')

    if direction == 'начало':
        new_text = X * count + others
    else:
        new_text = others + X * count

    return f"Результат: {new_text}"


if __name__ == "__main__":
    text = input('Введите строку символов: ')
    X = input('Введите символ X: ')

    print(move_char(text, X))
