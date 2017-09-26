'''
Compute the binomial coefficient binom(n, m).

Essentially an exercise to see how common recurrences may be 
computed using dynamic programming (in this case, memoization).
'''
import unittest
import numpy as np

def binom(n, m):
    bc = np.zeros((n+1, n+1), dtype=int)

    for i in range(n+1):
        bc[i, 0] = 1
    for j in range(n+1):
        bc[j, j] = 1

    for i in range(1, n+1):
        for j in range(1, i):
            bc[i, j] = bc[i-1, j-1] + bc[i-1, j]

    return bc[n, m]

class test(unittest.TestCase):
    def test_binom(self):
        self.assertTrue(binom(3, 2) == 3)
        self.assertFalse(binom(5, 3) == 3)

if __name__ == '__main__':
    print(binom(3, 2))
    unittest.main()
