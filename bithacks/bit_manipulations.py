'''
Various problems involving bits:
    1. Count # of set bits in a number.
    2. Return true iff x has 1 set bit
    3.

Source Material:
- http://www.geeksforgeeks.org/count-set-bits-in-an-integer/
- Leiserson's presentation on bit hacks
https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-172-performance-engineering-of-software-systems-fall-2010/video-lectures/lecture-2-bit-hacks/MIT6_172F10_lec02.pdf

Thought Process:
    - will outline the main tidbits.
    - Tidbit 1: What happens when we do x & (x - 1).
    1000 -> 0111. So x & x-1 drowns out the LSB.
    -
'''
import unittest
import numpy as np

def countBits(x):
    count = 0
    while x:
        count += x%2
        x >>= 1
    return count

def countBits_kernighan(x):
    '''
    Reference: http://www.geeksforgeeks.org/count-set-bits-in-an-integer/
    '''
    count = 0
    while x:
        x = x & (x - 1)
        count +=1
    return count

def onlyOne_v1(x):
    '''
    https://www.quaxio.com/know_your_bits/
    Return 1 iff x has only one set bit
    '''
    return countBits_kernighan(x) == 1

def onlyOne_v2(x):
    # if we do not keep the check for x, note what happens for x = 0
    # 0 & (0 - 1) is 0. 
    return x and not (x & (x - 1))

class test(unittest.TestCase):
    def test_countBits(self):
        self.assertTrue(countBits(4) == 1)
        self.assertTrue(countBits(5) == 2)

    def test_countBits_kernighan(self):
        self.assertTrue(countBits(4) == 1)
        self.assertTrue(countBits(0) == 0)
        self.assertTrue(countBits(5) == 2)

    def test_onlyOne(self):
        self.assertTrue(onlyOne_v1(4))
        self.assertFalse(onlyOne_v1(5))
        self.assertTrue(onlyOne_v2(4))
        self.assertFalse(onlyOne_v2(0))

if __name__ == '__main__':
    unittest.main()
        

