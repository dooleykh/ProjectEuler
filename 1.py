div_by_three = set([n for n in range(1000) if n % 3 == 0])
div_by_five = set([n for n in range(1000) if n % 5 == 0])
print sum(div_by_three.union(div_by_five))
