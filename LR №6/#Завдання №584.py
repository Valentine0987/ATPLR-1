#Завдання №584

numbers = list(map(int, input('Введіть числа:').split()))

seen = set()
duplicates = set()

for num in numbers:
    if num in seen:
        duplicates.add(num)
    else:
        seen.add(num)

for d in duplicates:
    print(d, end=" ")
