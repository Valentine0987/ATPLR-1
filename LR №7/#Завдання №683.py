#Завдання №683

def execute_code(code_line):
    try:
        exec(code_line)
        print("Successfully")
    except:
        print("Not fulfilled")
    finally:
        print("Done")


# Вводимо один рядок коду
line = input("Введіть рядок коду Python: ")
execute_code(line)
