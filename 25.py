#Python 2.7
i = 1
a, b = 1, 1
while a < pow(10, 999):
    a, b = b, a + b
    i += 1
print i
