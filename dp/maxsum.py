'''
Problem:
Given an array with n positive and negative numbers,
find the subarray with one or more consecutive numbers
where the sum of the subarray is maximum.

Source:
Many places, for instance Section 1.4, Hitchhiker's guide to the ICPC.

Technique: Dynamic Programming.

Thought Process:
0. Easy to get O(n^3). Also easy to get O(n^2) since there are two relevant
indices. The following is for O(n) - via DP.
1. Since we want the max sub array, such a subarray has negative numbers as
sentinels. Otherwise, we could just extend the subarray.
2. However, a negative number can be inside the optimal subarray, if it is subsumed by the
next "positive section" of the array.
3. You soon land up on the easier problem where the array is "hooked"/"attached" at one
end. I.e. find the max subarray that _ends_ at a position j. Nothing special with
_ends_, also could have looked for arrays that _start_ at a position j.
4. Note that if we could find all of these max subarrays, the actual max is a max over
all of these (i.e. over all possible j's).
5. So solve the simpler hooked problem. At every step there are two choices.
Either the last element is the subarray by itself (i.e. arr[j]) or it is attached
to the solution at j-1.

Related Problems:
1. Minimum subarray problem - just negate the signs.
2. Find the contiguous subarray that maximizes the polynomial evaluation at 2
where the coefficients come from the polynomial. The above problem is
the polynomial evaluation at 1.

'''

import numpy as np
import unittest

def maxSum(arr):
    n = len(arr)
    M = np.zeros((n), dtype=np.int)
    M[0] = arr[0]
    for j in range(1,n):
        M[j] = max(arr[j], M[j-1] + arr[j])
    return max(M), np.argmax(M)

def generate(length):
    return np.random.randint(-1*length, length, size=length, dtype=np.int)

class test(unittest.TestCase):
    def test_maxSum(self):
        arr = [1, 2, 3]
        self.assertTrue(maxSum(arr) == (6, 2))
        arr = [-1, -2, -3]
        self.assertTrue(maxSum(arr) == (-1, 0))

if __name__ == '__main__':
    arr = generate(10)
    print("arr = %s" %(arr))
    print("max sum = %d ending at idx %d" %(maxSum(arr)))

    unittest.main()



