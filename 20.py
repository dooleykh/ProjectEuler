#Python 2.7

print sum([int(i) for i in list(str(reduce(lambda x, y: x * y, range(1, 100 + 1))))])
