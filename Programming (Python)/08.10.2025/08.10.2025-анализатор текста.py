#!/usr/bin/env python3

ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
ru_vowel = "аеёиоуыэюя"

while True:
    text = input("Введите строку текста для анализа: ").strip().lower()
    if not text:
        print("Строка пуста, попробуйте снова.\n")
        continue
    if any(ch.isalpha() and ch not in ru_alphabet for ch in text):
        print("Допустимы только русские буквы.\n")
        continue
    break

vowel_count = 0
consonant_count = 0
space_count = 0
words_count = len(text.split())
char_count = {}

for ch in text:
    # если символ ch уже есть — увеличиваем счётчик, если нет — создаём запись со значением 1
    char_count[ch] = char_count.get(ch, 0) + 1
    if ch == " ":
        space_count += 1
    elif ch in ru_alphabet:
        if ch in ru_vowel:
            vowel_count += 1
        else:
            consonant_count += 1

# сортируем пары (символ, количество) по убыванию количества вхождений
sorted_char_count = sorted(
    char_count.items(), key=lambda i: i[1], reverse=True)

print("\nРезультат:")
print("-" * 35)
print(f"Гласных букв:    {vowel_count}")
print(f"Согласных букв:  {consonant_count}")
print(f"Пробелов:        {space_count}")
print(f"Количество слов: {words_count}")
print("-" * 35)
print("Три самых частых символа:")
for ch, cnt in sorted_char_count[:3]:
    print(f"  '{ch}' — {cnt} раз(а)")
print("-" * 35)
