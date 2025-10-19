#Завдання №243

n = int(input("Введіть кількість чисел: "))
count = 0
for i in range(n):
    num = int(input("Введіть число: "))
    if num == 0:
        count += 1
print(count)
