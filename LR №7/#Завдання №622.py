#Завдання №622

def season(month):
    if 3 <= month <= 5:
        return "spring"
    elif 6 <= month <= 8:
        return "summer"
    elif 9 <= month <= 11:
        return "autumn"
    elif month == 12 or month == 1 or month == 2:
        return "winter"
    else:
        return "unknown"


m = int(input("Введіть номер місяця: "))
print(season(m))
