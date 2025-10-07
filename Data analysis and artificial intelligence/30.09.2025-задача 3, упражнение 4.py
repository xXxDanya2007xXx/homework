#!/usr/bin/env python3

import numpy as np


def probability(temp, label):
    mean = temp.mean()
    med = np.median(temp)
    var = temp.var()
    probability_hot_day = (temp > 30).mean() * 100
    print(f"\n{label}:")
    print(f"Среднее значение: {mean:.2f}")
    print(f"Медиана: {med:.2f}")
    print(f"Дисперсия: {var:.2f}")
    print(f"Вероятность температуры > 30°C: {probability_hot_day:.2f}%.")


print("=== Сравнение распределений температуры ===")

# 1. Равномерное распределение
uniform_temp = np.random.uniform(low=20, high=35, size=10000)
probability(uniform_temp, "Равномерное распределение")

# 2. Нормальное распределение (обрезанное)
normal_temp = np.clip(np.random.normal(29, 3, size=10000), 20, 35)
probability(normal_temp, "Нормальное распределение")

# 3. Треугольное распределение
triangular_temp = np.random.triangular(20, 29, 35, size=10000)
probability(triangular_temp, "Треугольное распределение")

# 4. Скошенное распределение (бета)
hourly_raw = np.random.beta(a=2, b=5, size=(10000, 24))
hourly_temp = 20 + 15 * hourly_raw
probability(hourly_temp, "Скошенное распределение (бета)")
