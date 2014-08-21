#Python 2.7
#Generate factorizations via primes to find divisors
from itertools import chain, combinations

def powerset(s): #retrieved from itertools documentation
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

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

def proper_divisors(n, p):
    prime_divisors = [x for x in p if x < n and n % x ==0]
    factorization = []
    for x in prime_divisors:
        factorization.append(x)
        t = n / x
        while (t / x) * x == t:
            factorization.append(x)
            t /= x
    divisors = set()
    combs = powerset(factorization)
    for c in combs:
        if len(c) == 1:
            divisors.add(c[0])
        elif 1 < len(c) < len(factorization):
            divisors.add(reduce(lambda x, y: x * y, c))
    divisors.add(1)
    return divisors
    
def abundant_numbers(limit):
    abundant = set()
    p = list(primes(limit))
    for i in range(1, limit):
        if i < sum(proper_divisors(i, p)):
            abundant.add(i)
    return abundant

a = abundant_numbers(28124)
double_a = set([i + j for i in a for j in a])
s = 0
for i in range(1, 28124):
    if i not in double_a:
        s += i
print s
