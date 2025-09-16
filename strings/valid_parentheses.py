# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

from collections import deque
class Solution(object):
    def isValid(self, s):
        bal=True
        dq = deque()
        for i in s:
            if i in "([{":
                dq.append(i)
            else: 
                if not dq:
                    bal = False
                    break
                top = dq.pop()
                if (i == ')' and top!= '(') or (i == ']' and top != '[') or (i == '}' and top != '{'):
                    bal=False
                    break
        return bal and not dq