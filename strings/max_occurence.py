# 424.Longest Repeating Character Sequence
# You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
# Return the length of the longest substring containing the same letter you can get after performing the above operations.

class Solution(object):
    def characterReplacement(self, s, k):
        n=len(s)
        l=0
        r=0
        alpha = [0] * 26
        ans=0

        for r in range(n):
            alpha[ord(s[r]) - ord('A')] +=1
            max_occ = max(alpha)
            if r-l+1-max_occ >k:
                alpha[ord(s[l]) - ord('A')] -=1
                l+=1
            if ans<r-l+1: ans=r-l+1

        return ans
            
        