#!/usr/bin/env python3

import numpy as np


def describe_heights(heights, label):
    mean = heights.mean()
    std = heights.std()
    med = np.median(heights)
    mad = np.median(np.abs(heights - med))

    print(f"\n{label}")
    print(f"Средний рост: {mean:.2f} см")
    print(f"Стандартное отклонение: {std:.2f} см")
    print(f"Медиана: {med:.2f} см")
    print(f"Абсолютное отклонение от медианы (MAD): {mad:.2f} см")


# 1. Исходные данные
height = np.array([
    164, 151, 177, 157, 160, 163, 130, 127, 172, 151, 175, 146, 144,
    176, 173, 154, 199, 151, 157, 146, 150, 149, 149, 144, 149, 159,
    175, 147, 151, 198
])

# 2. Поиск аномалий
print("Ученики с аномальными значениями роста:")
print("индексы (рост < 140):", np.where(height < 140)[0])
print("индексы (рост > 180):", np.where(height > 180)[0])

# 3. Характеристики до исправления
describe_heights(height, "До обработки (с аномальными значениями)")

# 4. Замена аномалий на 157 см — средний рост класса
clean_height = np.where((height < 140) | (height > 180), 157, height)

# 5. Характеристики после исправления
describe_heights(clean_height, "После обработки (аномалии заменены на 157 см)")
