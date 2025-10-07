#!/usr/bin/env python3

import numpy as np


def experiment(size, repeats=6, loc=85, scale=15, threshold=80):
    for i in range(repeats):
        scores = np.random.normal(loc=loc, scale=scale, size=size)
        excellent_students = np.sum(scores >= threshold)
        mean_scores = scores.mean()
        print(
            f"{i + 1}) Среднее: {mean_scores:.2f}, значений ≥ {threshold}: {excellent_students}")


# 1.1
print("=== Проверим случайность при 30 учениках ===")
experiment(size=30)

# 1.2
print("\n=== Проверим закон больших чисел при 300 учениках ===")
experiment(size=300)

# 1.3
print("\n=== Стабильность среднего при 100 / 1000 / 10000 измерениях ===")
for size in [100, 1000, 10000]:
    print(f"Размер выборки: {size}")
    experiment(size)

# 2. Анализ распределения
print("\n=== Сравнение распределений до и после обрезки ===")
scores = np.random.normal(loc=85, scale=15, size=10000)

# До обрезки
mean_before = scores.mean()
excellent_before = np.sum(scores >= 100)

# После обрезки
clipped = np.clip(scores, 0, 100)
mean_after = clipped.mean()
excellent_after = np.sum(clipped >= 100)

print(f'До "обрезки":  среднее = {
      mean_before:.2f}, значений ≥ 100 = {excellent_before}')
print(f'После "обрезки": среднее = {
      mean_after:.2f}, значений ≥ 100 = {excellent_after}')
