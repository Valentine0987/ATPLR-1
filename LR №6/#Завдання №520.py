#Завдання №520

s = input("Введіть рядок: ")

upper = 0   
lower = 0  

for ch in s:
    if ch.isupper():   
        upper += 1
    elif ch.islower():
        lower += 1

print("UPPER CASE", upper)
print("LOWER CASE", lower)
