#Завдання №553

champions = {
    "Brazil": [1970, 1958, 1994, 1962, 2002],
    "England": [1966],
    "Italy": [2006, 1938, 1982, 1934],
    "Spain": [2010],
    "Germany": [2014, 1954, 1990, 1974],
    "France": [2018, 1998],
    "Uruguay": [1950, 1930],
    "Argentina": [1986, 1978]
}

for country in champions:
    champions[country] = sorted(champions[country])

print(champions)
