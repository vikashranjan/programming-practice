'''
Various Matrix Operations:
1. Problem 1:
Given a matrix of integers, compute the sum of a
submatrix in O(1) time and O(n^2) memory. Related page:
http://www.geeksforgeeks.org/submatrix-sum-queries/
(however I didn't actually see this - googling for
"sum of a submatrix" yields that page).

Thought Processing:
1. How to take the matrix as input?
As np.array?
As list of lists?
2. What is the point of this exercise? How many possible
submatrices are there? We can specify a submatrix by two
diagonally opposite corners, and that would essentially
mean specifying 4 numbers so altogether O(n^4) submatrices.
Going brute force, we can precompute all of these O(n^4) submatrices
and keep them. But that would be too much space.
3. So this is going to be one of those time-space tradeoff kinda
questions. Let's think of the 1D array problem. Here, there are
O(n^2) possible subarrays [start, end], but well we need only store
the subarrays [0, i]. Once we do that, [start, end] = [0, end] - [0, start].
4. Aha! That's all there is to it. For 2D, similarly, the matrices we
store have one corner fixed. (A union B + A intersect B) = (A + B) gives
us that we can apply 3 sums to get our result. That's it! - O(1) time,
O(n^2) space.

TODO:
1. Change the for loops to list comprehensions.
'''

import numpy as np
import unittest

class submatrixSum(object):
    def __init__(self, arr):
        '''
        Take in the matrix, preprocess to make it into a numpy array.
        '''
        self.arr = np.array(arr)
        self.prep_arr = np.zeros_like(self.arr)
        self.preprocess()
        return

    def preprocess(self):
        (r, c) = self.arr.shape
        for i in range(r):
            for j in range(c):
                term_i = 0 if i == 0 else self.prep_arr[i-1][j]
                term_j = 0 if j == 0 else self.prep_arr[i][j-1]
                term_ij = 0 if i == 0 or j == 0 else self.prep_arr[i-1][j-1]
                self.prep_arr[i][j] = term_i + term_j - term_ij + self.arr[i][j]
                '''                
                self.prep_arr[i][j] = self.prep_arr[i-1][j] + \
                                      self.prep_arr[i][j-1] - \
                                      self.prep_arr[i-1][j-1] + self.arr[i][j]
                '''
        return

    def printMatrix(self):
        print(self.prep_arr)

    def tuplePairToMatrixSum(self, *coordinates):
        # non-inclusive
        a, b = coordinates[0]
        c, d = coordinates[1]
        return self.prep_arr[a][b] + self.prep_arr[c][d] - self.prep_arr[a][d] - self.prep_arr[c][b]

if __name__ == '__main__':
    arr = [ [1, 2], [3, 4]]
    subm = submatrixSum(arr)
    subm.printMatrix()
    coordinates = [[0,0],[1,1]]
    print(subm.tuplePairToMatrixSum(*coordinates))




