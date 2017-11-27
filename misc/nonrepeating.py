'''
http://www.geeksforgeeks.org/length-of-the-longest-substring-without-repeating-characters/

Longest substring without repeating characters.

Thoughts:
1. We will hook the solutions at one end.
2. Given that, we will maintain the window size.
3. We will keep indices for when we have last seen the character.
In my thought process, this happened in iterations actually. First,
the idea of keeping a hashmap or a dictionary strikes. But then you
realise that while that will ensure uniqueness, we will also need the
indices where we saw a character last.
So given that you maintain a dictionary containing this information.

When you are storing indices in the dictionary, there is some confusion with
index i = 0 given that is a valid index, and what to initialize the dict
by.
'''

import numpy as np

def nonrepeating(arr):
    from collections import defaultdict
    d = defaultdict(lambda: -1)
    windows = []
    # initialize
    d[arr[0]] = 0
    wsize = 1
    windows = [wsize]
    for i in range(1, len(arr)):
        if d[arr[i]] == -1:
            wsize += 1
        else:
            if i - d[arr[i]] > wsize:
                wsize += 1
            else:
                wsize = i - d[arr[i]]
        windows.append(wsize)
        d[arr[i]] = i
    #print(windows)
    return np.max(windows)

if __name__ == '__main__':
    arr = 'geeksforgeeks'
    arr = 'abaccab'
    print(nonrepeating(arr))





