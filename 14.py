#Python 2.7

class Collatz:
    def __init__(self):
        self.memoized = {1: 1}
        self.max_length = -1
        self.max_start = -1

    def collatz(self, n):
        length = self.collatz_rec(n)
        if length > self.max_length:
            self.max_length = length
            self.max_start = n
        self.memoized[n] = length
        
    def collatz_rec(self, n):
        if n in self.memoized:
            return self.memoized[n]
        if n % 2 == 0:
            length = 1 + self.collatz_rec(n / 2)
        else:
            length = 1 + self.collatz_rec(3 * n + 1)
        self.memoized[n] = length
        return length

c = Collatz()
for i in range(1, 1000000):
    c.collatz(i)
print "start:", c.max_start
print "length:", c.max_length
