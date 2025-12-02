#Завдання №585(Перероблено)

s = input("Введіть рядок: ")

words = s.split()
lengths = {}

for word in words:      
    lengths[word] = len(word)

max_len = max(lengths.values())
print(max_len)
