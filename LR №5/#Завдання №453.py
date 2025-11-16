#Завдання №453

a = list(map(int, input("Введіть числа через пробіл: ").split()))
b = [n ** 2 for n in a]
print(*b)
