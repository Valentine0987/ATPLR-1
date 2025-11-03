#Завдання №391

s = input("Введіть рядок: ")

numbers = ""  
num = ""       

for c in s:
    if c >= '0' and c <= '9': 
        num = num + c
    else:
        if num != "":
            if numbers != "":
                numbers = numbers + ", "
            numbers = numbers + num
            num = ""

if num != "":
    if numbers != "":
        numbers = numbers + ", "
    numbers = numbers + num

print(numbers)
