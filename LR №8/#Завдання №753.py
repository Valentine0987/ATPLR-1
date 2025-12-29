#Завдання №753

from itertools import permutations

nums = list(map(int, input().split()))
result = list(permutations(nums))
print(result)
