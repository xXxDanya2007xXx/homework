#!/usr/bin/env python3

import numpy as np


def probability(size, low=20, high=35, threshold=30):
    temp = np.random.uniform(low=low, high=high, size=size)
    hot_days = temp > threshold
    probability_hot_day = hot_days.mean() * 100
    print(f"При {size:>6} симуляциях вероятность жаркого дня ≈ {
          probability_hot_day:.2f}%.")


print("=== Проверим, как объём симуляции влияет на точность оценки ===")
for size in [10, 100, 1_000, 100_000]:
    probability(size)

# Ответы на вопросы
print("\nОтветы на вопросы:")
print("- Ошибка становится меньше 1% примерно начиная с 10 000–100 000 симуляций.")
print("- Маленькая выборка (10–100) даёт 'странные' проценты, потому что случайность сильнее влияет на результат.")
print("- При больших размерах выборки (1000 и больше) результат стабилизируется  около теоретического 33.3%.")
