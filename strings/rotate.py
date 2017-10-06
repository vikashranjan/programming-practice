'''
Problem:
Given a string, rotate it by k elements to the right/left.

Sample input/output:
str = abcdef
rotate(str, k = 2, right = True) should output
efabcd
rotate(str, k = 4, right = False) should output the same.
In general,
rotate(str, k, right = False) == rotate(str, len(str)-k, right = True)

Thought Process:
1. Strings are immutable in Python.
2. However, you can create new strings as
b = a + a
3. A slice/subarray of this string would give the answer.
4. Call this solution 1 (see function rotate1); solution 1
requires extra space.

Followup question:
1. Suppose you wanted to do the rotation without extra space?
But, since strings are immutable in Python, you have to consider
them as _lists_.
Look at some examples:
abcdef -> efabcd
This is a permutation.

'''

import unittest

def rotate1(str, k, right = True):
    n = len(str)
    k = k % n
    str1 = str + str
    if right == True:
        k = n-k
    return str1[k: n+k]

def rotate2(str, k, right = True):
    n = len(str)
    k = k % n
    if right == False:
        k = n-k
    list1 = list(str)
    list2 = list1[::-1]

    return ''.join(list2[:k][::-1] + list2[k:][::-1])

def isRotation(str1, str2):
    '''
    Is str1 a rotation of str2?
    :param str1: a string of characters
    :param str2: another string of characters.
    :return: True if str1 is a rotation of str2.
    '''
    str = str2 + str2
    return (str.find(str1) != -1)

class test(unittest.TestCase):
    def test_rotate(self):
        str = "abcdef"
        self.assertTrue(rotate1(str, k=2) == "efabcd")
        self.assertTrue(rotate1(str, k=4, right=False) == "efabcd")
        self.assertTrue(isRotation(str, "efabcd"))

if __name__ == '__main__':
    str = "abcdef"
    print(rotate1(str, k=2))
    print(rotate1(str, k=4, right=False))
    print(rotate2(str, k=2))

    unittest.main()
