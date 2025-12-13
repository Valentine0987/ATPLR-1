#Завдання №653

def has_common_element(list1, list2):
    return bool(set(list1) & set(list2))

list1 = input('Введіть перший список:').split()
list2 = input('Введіть другий список:').split()

print(has_common_element(list1, list2))
