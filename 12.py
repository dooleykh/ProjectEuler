#Python 2.7
from math import sqrt

def triangular_numbers():
    sum = 0
    i = 1
    while sum < 250000: #n < 250000 can't have 500 divisors
        sum += i
        i += 1
    while True:
        yield sum
        sum += i
        i += 1
        
t = triangular_numbers()
while True:
    n = t.next()
    count = 0
    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            count += 2
    if count >= 500:
        print n
        break
