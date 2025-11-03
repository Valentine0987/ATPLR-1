#Завдання №392

s = input("Введіть рядок: ")

word = ""
longest = ""

for c in s:
    if ('a' <= c <= 'z') or ('A' <= c <= 'Z'):
        word = word + c
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

if len(word) > len(longest):
    longest = word

print("Найдовше слово:", longest)
