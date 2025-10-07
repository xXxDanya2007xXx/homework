#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np


def exp_temp(days):
    data = np.random.exponential(scale=2.0, size=(24, days))
    data = data / data.max()
    data = 20 + 15 * data
    return data


def week_means(days, repeats=1000):
    results = []
    for _ in range(repeats):
        exp_avg = exp_temp(days).mean(axis=0)
        exp_avg_period = exp_avg.mean()
        results.append(exp_avg_period)
    return np.array(results)


def probability(days, threshold=30):
    temps = exp_temp(days)
    probability_hot_day = (temps > threshold).mean() * 100
    return probability_hot_day


def build_plot(days, filename):
    plt.figure(figsize=(12, 4))

    # 1. Почасовые температуры
    plt.subplot(1, 2, 1)
    plt.hist(exp_temp(days).ravel(), bins=50, alpha=0.7,
             color="skyblue", edgecolor="black")
    plt.title(f"Почасовые температуры ({days} дней)")
    plt.xlabel("Температура (°C)")
    plt.ylabel("Частота")

    # 2. Распределение средних температур (1000 симуляций)
    plt.subplot(1, 2, 2)
    plt.hist(week_means(days), bins=50, alpha=0.7,
             color="lightcoral", edgecolor="black")
    plt.title(f"Распределение средних температур ({days} дней)")
    plt.xlabel(f"Средняя температура за {days} дней (°C)")
    plt.ylabel("Частота")

    plt.tight_layout()
    plt.savefig(filename)
    print(f"График сохранён в {filename}")


# === Проверяем влияние длины выборки на форму распределения ===
build_plot(7, "plot_7.png")
build_plot(30, "plot_30.png")

# === Оцениваем вероятность жарких дней (>30°C) для каждого случая ===
p7 = probability(7)
p30 = probability(30)
print(f"\nПри длине выборки 7 дней вероятность температуры > 30°C: {p7:.2f}%")
print(f"При длине выборки 30 дней вероятность температуры > 30°C: {p30:.2f}%")
