# 76. Minimum window string
# Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

# The testcases will be generated such that the answer is unique.


# Example 1:

# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.


class Solution(object):
    def minWindow(self,s, t):
        if len(t)>len(s):return ""
        if s == t: return s
        l=0
        tset = Counter(t)
        sset ={}
        
        formed = 0
        required = len(tset)
        ans = ""
        for r in range(len(s)):
            sset[s[r]] = sset.get(s[r],0)+1
            if s[r] in tset and sset[s[r]]==tset[s[r]]:
                formed +=1
            while l<=r and formed == required:
                window = s[l:r+1]
                if ans == "" or len(window)<len(ans):
                    ans = window
                sset[s[l]] -=1
                if s[l] in tset and sset[s[l]]<tset[s[l]]:
                    formed-=1
                l+=1
        
        return ans