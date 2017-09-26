'''
implementation of the fibonacci routines in 
Skiena's Algorithm Design manual
'''

import unittest
import time

def fib(n):
    '''
    This is if we want the array of fibonacci numbers from 1 through n.
    '''
    # bootstrap with the numbers fib(0), fib(1)
    arr = [0, 1]
    for i in range(2,n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n]

def fib2(n):
    '''
    what skiena calls "fib_ultimate" in his book.
    if we dont need the intermediate values, we can just 
    retain only the k-1st and k-2nd outputs.
    '''
    back0 = 0
    back1 = 1
    for i in range(2, n+1):
        next_el = back0 + back1
        back0 = back1
        back1 = next_el

    return next_el

if __name__ == '__main__':
    n = 5 
    start = time.time()
    print(fib2(n))
    time_taken = time.time() - start
    print("finished in %.2f secs" %(time.time() - start))
