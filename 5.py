divisors = range(2, 21)
i = 0
found = False
while not found:
    i += 20
    for d in divisors:
        if i % d != 0:
            break
    else:
        print i
        found = True
