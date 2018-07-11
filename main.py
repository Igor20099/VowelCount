# Программа для подсчета гласных букв в тексте
vowel = ['a', 'e', 'i', 'o', 'y', 'u']

text = input("Введите слово: ")
count = 0

for x in vowel:
    for letter in text:
        if x == letter.lower():
            count += 1

print("Всего гласных букв {}".format(str(count)))
