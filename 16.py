#Python 2.7
print reduce(lambda x, y: int(x) + int(y), list(str(2**1000)))
