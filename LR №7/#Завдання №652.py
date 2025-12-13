#Завдання №652

def print_long_words(words, n):
    for w in words:
        if len(w) > n:
            print(w)


words = input('Введіть слова:').split()
n = int(input('Введіть число:'))

print_long_words(words, n)
