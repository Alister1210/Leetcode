# 150. Evaluate Reverse Polish Notation
# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

class Solution(object):
    def evalRPN(self, tokens):
        stk = []

        for i in tokens:
            if i in "+*/-" :
                r=int(stk.pop())
                l=int(stk.pop())
                    
                if i == "+" : stk.append(l+r)
                elif i=='*' : stk.append(l*r)
                elif i=='-' : stk.append(l-r)
                elif i=='/' : stk.append(int(l/r) if l/r>=0 else -(abs(l)//abs(r)))
            else:
                stk.append(int(i))

        return stk[0]
