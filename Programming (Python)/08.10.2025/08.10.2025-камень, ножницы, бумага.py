#!/usr/bin/env python3

import random

CHOICES = ['камень', 'ножницы', 'бумага']
WINNING_PAIRS = {
    'камень': 'ножницы',
    'ножницы': 'бумага',
    'бумага': 'камень'
}

player_wins = 0
machine_wins = 0

print("Игра 'Камень, ножницы, бумага' — до 3 побед.")

while player_wins < 3 and machine_wins < 3:
    player_choice = input(
        "\nВаш ход (камень, ножницы, бумага): ").strip().lower()
    if player_choice not in CHOICES:
        print("Ошибка ввода. Попробуйте снова.\n")
        continue

    machine_choice = random.choice(CHOICES)
    print(f"Ход противника: {machine_choice}")

    if player_choice == machine_choice:
        print("Ничья!\n")
    elif WINNING_PAIRS[player_choice] == machine_choice:
        player_wins += 1
        print(f"Вы победили! Счёт: {player_wins}:{machine_wins}\n")
    else:
        machine_wins += 1
        print(f"Вы проиграли. Счёт: {player_wins}:{machine_wins}\n")

print("Результат:")
print("-" * 35)
if player_wins > machine_wins:
    print(f"Победа! Итоговый счёт: {player_wins}:{machine_wins}")
else:
    print(f"Поражение! Итоговый счёт: {player_wins}:{machine_wins}")
print("-" * 35)
