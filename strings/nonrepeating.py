'''
Problem:
Longest nonrepeating substring
http://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

'''
import numpy as np
from collections import defaultdict

def nonrepeat(arr):
    arr = np.array(arr)
    dict = defaultdict(lambda:0)
    soln = np.zeros_like(arr, dtype = int)
    # initialize
    soln[0] = 1
    dict[arr[0]] = 0
    for i in range(1, len(arr)):
        soln[i] = 0
        temp = dict[arr[i]]  #update index of current letter
        dict[arr[i]] = i
        if temp >= i - soln[i - 1]:
            soln[i] = i - temp
        else:
            soln[i] = soln[i-1] + 1
    return (np.max(np.array(soln)), np.argmax(np.array(soln)))

if __name__ == '__main__':
    str = "ababcdabefgab"
    arr = list(str)
    (len, idx) = nonrepeat(arr)
    print("The input is %s" %(str))
    print("The maximum nonrepeating substring is %s of length = %d"%(''.join(arr[idx-len+1:idx+1]), len))