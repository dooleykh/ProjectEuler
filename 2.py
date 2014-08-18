#Python 2.7
#Solved using generators

def even_fib(limit):
    a, b = 1, 2
    while a < limit:
        if a % 2 == 0:
            yield a
        a, b = b, a + b

print sum(list(even_fib(4000000)))
