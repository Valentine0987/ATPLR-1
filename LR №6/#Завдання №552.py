#Завдання №552

mountains = {
    "Hoverla": 2061,
    "Brebenescul": 2032,
    "Pip Ivan Chernogirsky (Chorna gora)": 2028,
    "Petros": 2020,
    "Menchul": 1998,
    "Vuhatyi Kamin": 1889
}

top_three = sorted(mountains.items(), key=lambda x: x[1], reverse=True)[:3]
for name, height in top_three:
    print(f"{name}: {height} m")
