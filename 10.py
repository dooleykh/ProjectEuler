#Python 2.7

def primes(limit):
    numbers = [True] * limit
    for i in range(2, limit):
        if not numbers[i]:
            continue
        for t in range(2 * i, limit, i):
            numbers[t] = False
    for i in range(2, limit):
        if numbers[i]:
            yield i
            
print sum(primes(2000000))
