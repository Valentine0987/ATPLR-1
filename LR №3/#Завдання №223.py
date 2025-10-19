#Завдання №223

while True:
    n = int(input("Введіть число: "))

    if n > 100:
        break
    elif n < 10:
        continue
    else:
        print(n)