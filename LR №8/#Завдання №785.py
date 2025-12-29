#Завдання №785

import operator

students = []

with open('input.txt', 'r', encoding='utf-8') as file:
    for line in file:
        parts = [p.strip() for p in line.split(',')]
        students.append(tuple(parts))

students_sorted = sorted(students, key=operator.itemgetter(2))

print(students_sorted)



