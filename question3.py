import time
from functools import reduce

start_time = time.time()

# function to find all factors of number
def factors(n):    
    return set(reduce(list.__add__, # combine lists
                # find pair of numbers that when multiplied, the result is n
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))) 

count_6_factors = 0

for i in range(1,262144):
    if len(factors(i)) == 6:
        count_6_factors += 1

print(count_6_factors)

print("--- %s seconds ---" % (time.time() - start_time))