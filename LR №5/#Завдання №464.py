#Завдання №464

a = input('Введіть текст: ').strip()
b = int(input('Введіть номер: ').strip())

words = a.split()

if 1 <= b <= len(words):
    print(words[b-1][0])
else:
    print()
