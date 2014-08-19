#Python 2.7

def primes(limit):
    numbers = range(2, limit)
    primes = []
    while len(numbers) != 0:
        p = numbers[0]
        primes.append(p)
        numbers = [n for n in numbers if n % p != 0]
    return primes

print primes(120000)[10000] #Number discovered by trial and error
