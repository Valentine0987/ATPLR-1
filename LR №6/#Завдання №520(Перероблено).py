#Завдання №520(Перероблено)

s = input("Введіть рядок: ")

upper_set = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower_set = set("abcdefghijklmnopqrstuvwxyz")

counts = {"UPPER": 0, "LOWER": 0}

for ch in s:
    if ch in upper_set:
        counts["UPPER"] += 1
    elif ch in lower_set:
        counts["LOWER"] += 1

print("UPPER CASE", counts["UPPER"])
print("LOWER CASE", counts["LOWER"])
