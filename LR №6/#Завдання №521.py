#Завдання №521

students = {
    "Alex": 90,
    "John": 70,
    "Barbara": 85,
    "Dan": 60
}

average = sum(students.values()) / len(students)

for name, score in students.items():
    if score > average:
        print(name)
