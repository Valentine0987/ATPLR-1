#Завдання №366

text = input("Введіть рядок: ")
old = input("Введіть підрядок, який потрібно замінити: ")
new = input("Введіть новий підрядок: ")

if old in text:
    result = text.replace(old, new)
    print("Результат після заміни:", result)
else:
    print("is impossible")
