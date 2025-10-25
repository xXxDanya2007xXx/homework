#!/usr/bin/env python3

import os
import datetime
from decimal import Decimal, InvalidOperation

goods = {
    'Пельмени Универсальные': [
        {'amount': Decimal(
            '0.5'), 'expiration_date': datetime.date(2025, 12, 10)},
        {'amount': Decimal(
            '2'), 'expiration_date': datetime.date(2026, 1, 20)},
    ],
    'Пельмени Не Универсальные': [
        {'amount': Decimal('1'), 'expiration_date': datetime.date(2025, 9, 15)}
    ],
    'Вода': [
        {'amount': Decimal('1.5'), 'expiration_date': None}
    ]
}


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def find_matches(item):
    return [name for name in goods if item.strip().lower() in name.lower()]


def print_matches(item):
    matches = find_matches(item)
    results = ", ".join(matches)
    print(f"\nНайденные продукты: \033[97m{results}\033[0m")


def find():
    while True:
        item = input("Введите название продукта: ").strip()
        if not item:
            print("\033[91mErr:\033[0m Пустая строка. Попробуйте снова")
            continue
        break
    matches = find_matches(item)
    if not matches:
        print("\n\033[91mНичего не найдено\033[0m")
        input("\nНажмите Enter, чтобы вернуться в меню...")
        return []
    print_matches(item)
    for name in matches:
        print(f"\n{name}:")
        for i, batch in enumerate(goods[name], start=1):
            print(f"    Партия {i}: количество \033[92m{
                  batch['amount']}\033[0m, срок годности \033[93m{batch['expiration_date']}\033[0m")
    input("\nНажмите Enter, чтобы вернуться в меню...")
    return matches


def print_all():
    for name in goods:
        print(f"\n\033[97m{name}:\033[0m")
        for i, batch in enumerate(goods[name], start=1):
            print(f"    Партия {i}: количество \033[92m{
                  batch['amount']}\033[0m, срок годности \033[93m{batch['expiration_date']}\033[0m")
    input("\nНажмите Enter, чтобы вернуться в меню...")


def amount():
    while True:
        item = input("Введите название продукта: ").strip()
        if not item:
            print("\033[91mErr:\033[0m Пустая строка. Попробуйте снова")
            continue
        break
    matches = find_matches(item)
    if not matches:
        print("\033[91mНичего не найдено\033[0m")
        input("\nНажмите Enter, чтобы вернуться в меню...")
        return []
    total = Decimal('0')
    for name in matches:
        for batch in goods[name]:
            total += batch['amount']
    print_matches(item)
    print(f"\n\033[97mОбщее количество найденных продуктов: \033[92m{
          total}\033[0m")
    input("\nНажмите Enter, чтобы вернуться в меню...")


def add(item=None, amount=None, expiration_date=None):
    if item is None:
        while True:
            item = input("Введите название продукта: ").strip()
            if not item:
                print("\033[91mErr:\033[0m Пустая строка. Попробуйте снова")
                continue
            break

    found_key = None
    for name in goods:
        if name.lower() == item.lower():
            found_key = name
            break

    if found_key:
        print(f"\nПродукт \033[97m{
              found_key}\033[0m уже в списке. Добавляем новую партию...\n")
    else:
        print(f"\nДобавляем продукт \033[97m{item}\033[0m в список...\n")
        goods[item] = []
        found_key = item

    if amount is None:
        while True:
            try:
                amount = Decimal(
                    input("Введите \033[92mколичество продукта\033[0m: "))
            except InvalidOperation:
                print("\033[91mErr:\033[0m Попробуйте ввести число")
                continue
            break

    if expiration_date is None:
        while True:
            expiration_input = input(
                "Введите \033[93mсрок годности\033[0m (гггг-мм-дд) или оставьте пустым: ")
            if not expiration_input:
                expiration_date = None
                break
            if expiration_input.strip():
                try:
                    expiration_date = datetime.datetime.strptime(
                        expiration_input, '%Y-%m-%d').date()
                    break
                except ValueError:
                    print(
                        "\033[91mErr:\033[0m Неверный формат даты. Попробуйте снова")
                    continue

    goods[found_key].append(
        {"amount": amount, "expiration_date": expiration_date})
    print(f"\nПродукт \033[97m{
          found_key}\033[0m \033[92mдобавлен\033[0m в список")


def add_by_note():
    while True:
        print(
            "# Формат: \033[37mНазвание \033[32mколичество \033[33mгггг-мм-дд\033[0m")
        print(
            "# Пример: \033[37mВода Минеральная\033[32m 1 \033[33m2025-10-16\033[0m")
        note = input("Введите описание продукта : ").strip()
        if not note:
            print("\033[91mErr:\033[0m Пустая строка. Попробуйте снова")
            continue
        parts = note.rsplit(maxsplit=2)
        if len(parts) < 3:
            print(
                "\033[91mErr:\033[0m Неверный формат описания. Попробуйте снова")
            continue
        item, amount_str, date_str = parts
        try:
            amount = Decimal(amount_str)
        except InvalidOperation:
            print(
                "\033[91mErr:\033[0m Неверный формат количества. Попробуйте снова")
            continue
        try:
            expiration_date = datetime.datetime.strptime(
                date_str, "%Y-%m-%d").date()
        except ValueError:
            print("\033[91mErr:\033[0m Неверный формат даты. Попробуйте снова")
            continue
        existing_key = None
        for key in goods:
            if item.lower() == key.lower():
                existing_key = key
                break
        if existing_key:
            item = existing_key
        add(item, amount, expiration_date)
        break


def delete():
    while True:
        item = input("Введите название продукта: ").strip()
        if not item:
            print("\033[91mErr:\033[0m Пустая строка. Попробуйте снова")
            continue
        found_key = None
        for name in goods:
            if name.lower() == item.lower():
                found_key = name
                break
        if not found_key:
            print(f"\n\033[91mErr:\033[0m Продукта \033[97m{
                  item}\033[0m нет в списке. Попробуйте снова\n")
            continue
        del goods[found_key]
        print(f"\nПродукт \033[97m{
              found_key}\033[0m \033[91mудален\033[0m из списка")
        break


def main():
    while True:
        try:
            print("\033[97m=========== Холодильник ===========\033[0m")
            print("-" * 35)
            print("\033[92m1\033[0m - Добавить продукт")
            print("\033[92m2\033[0m - Добавить продукт по описанию")
            print("\033[92m3\033[0m - Удалить продукт")
            print("\033[92m4\033[0m - Список продуктов")
            print("\033[92m5\033[0m - Найти продукт")
            print("\033[92m6\033[0m - Посчитать общее количество продуктов")
            print("\033[92m0\033[0m - Выйти")
            print("-" * 35)
            choice = input("Выберите действие: ").strip()
            if choice == '0':
                print("\033[93mВыход из программы\033[0m")
                break
            elif choice == '1':
                clear()
                print("\033[92m*Добавить продукт*\033[0m")
                add()
            elif choice == '2':
                clear()
                print("\033[92m*Добавить продукт по описанию*\033[0m")
                add_by_note()
            elif choice == '3':
                clear()
                print("\033[91m*Удалить продукт*\033[0m")
                delete()
            elif choice == '4':
                clear()
                print("\033[97m*Список продуктов*\033[0m")
                print_all()
            elif choice == '5':
                clear()
                print("\033[97m*Найти продукт*\033[0m")
                find()
            elif choice == '6':
                clear()
                print("\033[97m*Найти общее количество продуктов*\033[0m")
                amount()
            else:
                if not choice:
                    print("\033[91mErr:\033[0m Пустая строка. Попробуйте снова")
                else:
                    print("\033[91mErr:\033[0m Похоже, вы ввели неверное число")
                continue
        except KeyboardInterrupt:
            print("\n\033[93mПрограмма завершена пользователем\033[0m")
            break


if __name__ == "__main__":
    main()
