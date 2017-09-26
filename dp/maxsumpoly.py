'''
Problem:
Max sum poly.
We are given an array with n positive and negative numbers.
For any subarray, associate a polynomial with coefficients
such that the constant term is on the right, and the highest
degree term on the left.
Thus if the subarray is [a, b, c, d] the associated polynomial
is ax^3 + bx^2 + cx + d.
Find the subarray for which the corresponding polynomial p(x)
evaluation at x = 2 is maximized.

Source:
Generated from the max array sum (in maxsum.py) problem.

Technique: Dynamic Programming.

Thought Process:
0. Look out for similar problems. Note that the maxsum problem is this
very problem with p(x) being evaluated at x = 1.
1. Then revisit the solution there, and notice that in the recurrence, we
just need to replace one term.
M[j] = max(arr[j], 2*M[j-1] + arr[j])
for an evaluation of p(2).

Related problems:
1. Instead of an array, we can ask the same questions for a _grid_.
2. The "multipliers" 2^k here, may be thought of as coming from a
_fixed_ array = [1, 2, 2^2, 2^3, ...].
As one can guess, 2 (or 1) is not special. One may use any other number
(real, irrational, or what have you).
The reader will notice that the recursion for M[j] essentially
Horner's formula in order to evaluate the polynomial.
Question: Is it possible to use some other general fixed array as
multipliers?
Say for instance
- the array = [1 + 1, 2 + 1, 2^2 + 1, ...]?
- the array = [1, 3, 5, 7, ...]?
'''

import numpy as np

def maxSumPoly(arr):
    '''
    Slight change from maxSum in maxsum.py:
        instead of declaring the space for the matrix M,
        we append to it as we go. Somehow this feels more
        dangerous than declaring M = np.zeros((size)), because
        we are referring to the explicit locations arr[j]
        (which means we need to be more careful about the
        array indices). 
    '''
    n = len(arr)
    M = []
    M.append(arr[0]) # M[0] = arr[0]
    for j in range(1,n):
        M.append(max(arr[j], 2*M[j-1] + arr[j])) # the only change in the entire algorithm.
    return max(M), np.argmax(M)


def generate(length):
    return np.random.randint(-1*length, length, size=length, dtype=np.int)

if __name__ == '__main__':
    arr = [1, 2, 3]
    print(maxSumPoly(arr))



