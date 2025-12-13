#Завдання №684

def is_pangram(text):
    alphabet = set("abcdefghijklmnopqrstuvwxyz") 
    text_letters = set()
    
    for c in text:
        if c.isalpha():
            text_letters.add(c.lower()) 

    return text_letters >= alphabet 

line = input("Введіть рядок: ")
print(is_pangram(line))
