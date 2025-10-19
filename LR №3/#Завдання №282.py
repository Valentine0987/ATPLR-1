#Завдання №282

prev = int(input("Введіть число: "))

count = 0 

while True:
    n = int(input("Введіть число: "))
    if n == 0:
        break  
    if n > prev:
        count += 1
    prev = n 

print(count)
