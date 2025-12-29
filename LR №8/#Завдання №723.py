#Завдання №723

import os

print("int:", (123).__sizeof__())
print("float:", (3.14).__sizeof__())
print("complex:", (1+2j).__sizeof__())
print("OS:", os.name, "| CPU:", os.cpu_count())

