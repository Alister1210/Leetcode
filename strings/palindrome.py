# 125. Valid Palindrome
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

 

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Using 2-pointer approach
import re
class Solution(object):
    def isPalindrome(self, s):
        line = re.sub(r'[^A-Za-z0-9]', "", s).lower()
        n=len(line)
        if n == 0: return True
        for i in range(n):
            if line[i] != line[n-1-i]: return False
        return True
        