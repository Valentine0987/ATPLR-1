#Завдання №754

import time

n = int(input("Введіть число n: "))

start_time = time.time()
total = sum(range(1, n + 1))
end_time = time.time()
elapsed_time = end_time - start_time

print(f"Required time to calculate sum of 1 to {n} (sum = {total}) is: {elapsed_time:.3f} seconds.")
