#!/usr/bin/env python3

accounts = {}


def create_account():
    number = len(accounts) + 1
    accounts[number] = 0.0
    print(f"Создан счёт №{number}. Баланс: 0.00")


def deposit():
    try:
        acc = int(input("Введите номер счёта: "))
        amount = float(input("Сумма пополнения: "))
        if amount <= 0:
            print("Сумма должна быть положительной.")
            return
        accounts[acc] += amount
        print(f"Счёт №{acc} пополнен на {
              amount:.2f}. Баланс: {accounts[acc]:.2f}")
    except:
        print("Ошибка: неверный номер счёта или формат суммы.")


def withdraw():
    try:
        acc = int(input("Введите номер счёта: "))
        amount = float(input("Сумма снятия: "))
        if amount <= 0:
            print("Сумма должна быть положительной.")
            return
        if accounts[acc] < amount:
            print("Недостаточно средств.")
            return
        accounts[acc] -= amount
        print(f"Со счёта №{acc} снято {
              amount:.2f}. Баланс: {accounts[acc]:.2f}")
    except:
        print("Ошибка: неверный номер счёта или формат суммы.")


def transfer():
    try:
        src = int(input("Счёт отправителя: "))
        dst = int(input("Счёт получателя: "))
        amount = float(input("Сумма перевода: "))
        if src == dst:
            print("Нельзя перевести на тот же счёт.")
            return
        if amount <= 0:
            print("Сумма должна быть положительной.")
            return
        if accounts[src] < amount:
            print("Недостаточно средств.")
            return
        accounts[src] -= amount
        accounts[dst] += amount
        print(f"Переведено {amount:.2f} со счёта №{src} на счёт №{dst}.")
        print(f"Баланс №{src}: {accounts[src]:.2f}, №{
              dst}: {accounts[dst]:.2f}")
    except:
        print("Ошибка: неверный номер счёта или формат суммы.")


def show_accounts():
    if not accounts:
        print("Нет созданных счетов.")
        return
    print("\nСписок счетов:")
    for num, balance in accounts.items():
        print(f"№{num} — Баланс {balance:.2f}")


def main():
    while True:
        print("\nВыберите действие:")
        print("-" * 35)
        print("1 - Создать счёт")
        print("2 - Пополнить счёт")
        print("3 - Снять средства")
        print("4 - Перевести средства")
        print("5 - Показать все счета")
        print("0 - Выйти")
        print("-" * 35)

        choice = input("\nВаш выбор: ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            show_accounts()
        elif choice == "0":
            break
        else:
            print("Неверный выбор.")


main()
