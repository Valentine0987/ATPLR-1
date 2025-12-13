#Завдання №621

def longest_word(word1, word2):
    if len(word1) > len(word2):
        print(word1)
    elif len(word2) > len(word1):
        print(word2)
    else:
        # довжини однакові
        print(word1)
        print(word2)

# приклад виклику
a = input("Введіть перше слово: ")
b = input("Введіть друге слово: ")

longest_word(a, b)
