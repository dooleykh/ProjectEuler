#Python 2.7
#Prints potential candidates using the Sieve of Eratosthenes

#Sieve
def primes(limit):
    numbers = range(2, limit)
    primes = []
    while len(numbers) != 0:
        p = numbers[0]
        primes.append(p)
        numbers = [n for n in numbers if n % p != 0]
    return primes

candidates =  [n for n in range(2, 775147) if 600851475143 % n == 0]
p = primes(100000) #The sieve is inefficient for sqrt(600851475143) as the limit
candidates = [n for n in candidates if n in p or n > 100000] 
print candidates
