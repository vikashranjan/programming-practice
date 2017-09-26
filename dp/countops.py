'''
Problem:
Given there are three operations - add 1, subtract 1, divide by 2 if even,
calculate the (minimum) number of steps needed to go from n to 1.

Technique:
Dynamic Programming/Memoization

Thought Process:
1. Normally in a DP, we have to count operations where a problem(n) reduces
to problem(n-1). Here, it seems that we can "add 1" so a problem(n) seems
to become worse at problem(n+1).
2. Let's first solve the easier problem, without the "add 1" operation.
Since we are trying to reduce n to 1, lets be careful of the array limits.
Letting "count" be the counter of the minimum number of moves, we will
set the boundary condition count[1] = 0. Also the loop runs from 2..n.
This is solved by countOps1.
3. Now the twist here is that we have an "add 1" operation. So that might mean
given n, we will have to explore n+1, n+2, etc. For instance, the
optimal sequence of operations can be "go up to the next power of 2, then come
down".
This actually happens. For instance, countOps1(15) = 6 (check code below), and
countOps1(16) = 4. So if the increment move were allowed, countOps2(15) would
actually be 1 + 4 = 5 < 6.
So how do we solve this?
We aid the DP with some enumeration. We consider the cases where the number
goes up to a multiple of 2, to then come down, and add estimates corresponding
to these choices.
'''

import numpy as np
import math
import unittest

def countOps1(n):
    count = np.zeros((n+1), dtype=int)
    count[1] = 0
    for i in range(2, n+1):
        est1 = float("inf")
        est2 = count[i-1] + 1
        if i % 2 == 0:
            est1 = count[i/2] + 1
        count[i] = min(est1, est2)
    return count[n]

def countOps2(n):
    count = np.zeros((n+1), dtype=int)
    for i in range(2, n+1):
        estimates = []
        estimates.append(count[i-1] + 1)
        if i%2 == 0:
            for k in range(i/2):
                estimates.append(count[(i + 2*k)/2]+ 2*k + 1)
        if i%2 == 1:
            for k in range(1, i/2):
                estimates.append(count[(i + 2*k-1)/2]+ 2*k)
        count[i] = min(estimates)
    return count[n]

class test(unittest.TestCase):
    def test_countOps(self):
        self.assertTrue(countOps1(31)==8)
        self.assertTrue(countOps2(31)==6)
        self.assertTrue(countOps1(30)==7)
        self.assertTrue(countOps2(30)==6)

if __name__ == '__main__':
    print(countOps1(31))
    print(countOps2(30))
    unittest.main()



