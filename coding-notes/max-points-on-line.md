## [max points on a line](https://leetcode.com/problems/max-points-on-a-line/description/)

### **The Problem**
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

A thought-process kinda argument also appears in the 
following online articles:
 1. [blog article by Jian Lu](http://jianlu.github.io/2014/01/10/leetcode149-max-points-on-a-line/).
2. [another article](https://www.sigmainfy.com/blog/leetcode-max-points-on-a-line-hashing.html)

I purposely did not go through the blogs above, just to 
see what I can get by myself. 

### Start off
First we try to get a trivial solution, then see what 
can be improved.
1. Given the n points, there are n^2 pairs of points. 
Each pair defines a slope. In order to find the max
 number of points on a line, we translate to the
 question: Which slope appears the 
most often?
2. We have n^2 numbers, find most frequent (top k for
k = 1). 
Hash + heap. Hash by the slope, then find the max 
count. _Overall_: O(n^2). 
3. Can we do better, say O(n)? Not sure yet. 
Still thinking.