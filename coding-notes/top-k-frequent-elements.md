## [top k frequent elements](https://leetcode.com/problems/top-k-frequent-elements/description/)
### **The Problem**
Given a non-empty array of integers, return the k most frequent elements.

### Start off
The problem also asks for this to be better than a 
O(n log n) solution. 
1. We can think of making a hashmap/dictionary consisting
of the _counts_ of the elements. Thus, we would take a
single pass over the data, and for each element c, we would
update the dictionary dict[c] += 1. 
2. Now, we roughly have what we want. We would ideally 
pick the top k in sorted order, where the elements are 
ordered according to their frequencies. Well we do not
want to sort the entire dictionary, the counts being the 
key. 
3. Here enters a heap, more specifically a max-heap. 
We would insert the elements into a max-heap - cost of
O(n). We would keep popping the top/max elements 
so for k deletions, we get O(k log n).

**Upshot**:
1. overall time is O(n + k log n). 
2. when we are working with top k or so, where we 
want the running time to reflect the k and not the 
size of the entire dataset (n), we might look at the 
heap data-structure to accomplish that for us.