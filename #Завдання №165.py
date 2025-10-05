#Завдання №165

a=input('Введіть перше число: ')
b=input('Введіть друге число: ')
c=input('Введіть арифметичну дію: ')
if c=='+':
    print(float(a)+float(b))
elif c=='-':
    print(float(a)-float(b))
elif c=='*':
    print(float(a)*float(b))
elif c=='/':
    if b=='0':
        print('Ділення на нуль заборонено!')
    else:
        print(float(a)/float(b))
elif c == "mod":
    if b == 0:
        print("Ділення на нуль заборонено!")
    else:
        print(a % b)
elif c == "pow":
    print(float(a) ** float(b))
elif c == "div":
    if b == '0':
        print("Ділення на нуль заборонено!")
    else:
        print(float(a) // float(b))


          