#Завдання №277

n = int(input("Введіть ціле число: "))
n = abs(n)
s = 0
while n > 0:
    s += n % 10 
    n //= 10 
print(s)
