#!/usr/bin/env python3

import numpy as np


def probability_uniform(low, high, threshold, size=10000):
    temp = np.random.uniform(low=low, high=high, size=size)
    probability_hot_day = (temp > threshold).mean() * 100
    print(f"При диапазоне {low}–{high}°C вероятность температуры > {
          threshold}°C: {probability_hot_day:.2f}%.")


def probability_triangular(low, mode, high, threshold, size=10000):
    temp = np.random.triangular(low, mode, high, size=size)
    probability_hot_day = (temp > threshold).mean() * 100
    print(f"При треугольном распределении в диапазоне {low}–{high}°C, пик {
          mode}°C, вероятность температуры > {threshold}°C: {probability_hot_day:.2f}%.")


print("=== Базовый климат (20–35°C) ===")
probability_triangular(low=20, mode=27.5, high=35, threshold=30)

print("\n=== Климат потеплел на +2°C (22–37°C) ===")
probability_triangular(low=22, mode=29.5, high=37, threshold=30)

print("\n=== Климат потеплел на +2°C, порог 'жары' вырос до 32°C ===")
probability_triangular(low=22, mode=29.5, high=37, threshold=32)
