#Завдання №503

roman = input("Введіть римське число: ")

values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

total = 0
i = 0

while i < len(roman):
    if i + 1 < len(roman) and values[roman[i]] < values[roman[i + 1]]:
        total += values[roman[i + 1]] - values[roman[i]]
        i += 2
    else:
        total += values[roman[i]]
        i += 1

print(total)
