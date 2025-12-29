#Завдання №784

with open('input.txt', 'r', encoding='utf-8') as languages_file, \
     open('rating.txt', 'r', encoding='utf-8') as ratings_file:
     
    languages = [line.strip() for line in languages_file]
    ratings = [line.strip() for line in ratings_file]

combined_lines = [f"{lang} {rate}" for lang, rate in zip(languages, ratings)]

for line in combined_lines:
    print(line)

with open('output.txt', 'w', encoding='utf-8') as output_file:
    for line in combined_lines:
        output_file.write(line + '\n')

