'''
Problem:
Output different *odd even* substrings, where
you consider only the odd or even parts of a substring
and mixing such substrings up.

Example 1:
Given a string, output a substring with only the odd
indexed characters.
Here, be careful that the index 0 is actually an odd
index (when you consider the actual string).

Thought Process:
1. Convert string (immutable) into a list, and then use
list comprehensions.
2. Possible to do a direct conversion to a list without
that first conversion of string -> list. See below,
function oddSubstr()

Example 2:
Followup on Example 1. Have the even indexed substring
follow the odd indexed substring.
See function oddEvenSubstr().

Example 3:
How many times do we have to apply oddEvenSubstr to a string
to get back the original string?
The programming is easy, but more thought needs to be paid
to the theory: Will repeated applications of oddEvenSubstr
even bring the string back to the original?
For short strings, it does seem to:
abcd -> acbd -> abcd
abc -> acb -> abc
cba -> cab -> cba
See function count_oddEvenSubstr().

For evenOddSubstr (not implemented in the below):
abcd -> bdac -> dcba -> cadb -> abcd
abc -> bac -> abc
cba -> bca -> cba
'''

def oddSubstr(str):
    list1 = [ e for i, e in enumerate(str) if i % 2 == 0]
    return ''.join(list1)

def oddEvenSubstr(str):
    list1 = [ e for i, e in enumerate(str) if i % 2 == 0] # odd
    list2 = [ e for i, e in enumerate(str) if i % 2 == 1] # even

    return ''.join(list1+list2)

def count_oddEvenSubstr(str):
    str1 = oddEvenSubstr(str)
    count = 1
    while str1 != str:
        str1 = oddEvenSubstr(str1)
        count += 1
    return count

if __name__ == '__main__':
    str = "abcdefghi"
    print(oddSubstr(str))
    str1 = oddEvenSubstr(str)
    print("oddEvenSubstr(%s) = %s"%(str, str1))
    print("oddEvenSubstr^2(%s) = %s" %(str, oddEvenSubstr(str1)))
    print(count_oddEvenSubstr(str))
