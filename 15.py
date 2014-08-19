#Python 2.7
#Use the number of unique permutations
fact = lambda x, y: x * y
print reduce(fact, range(1, 40 + 1)) / (reduce(fact, range(1, 20 + 1)))**2
