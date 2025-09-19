# 22. Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8



class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        ans =[]
        def recursion(open,close):
            if open == close == n:
                ans.append("".join(stack))
                return
            if open < n:
                stack.append('(')
                recursion(open+1,close)
                stack.pop()
            
            if close < open:
                stack.append(')')
                recursion(open,close+1)
                stack.pop()
        recursion(0,0)
        return ans
        