# 567. Permutation in String
# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

# In other words, return true if one of s1's permutations is the substring of s2.

 

# Example 1:

# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").

class Solution(object):
    def checkInclusion(self, s1, s2):
        freq1 = {}
        freq2 = {}
        l=0
        r=len(s1)
        if len(s1)>len(s2):return False
        for ch in s1:
            freq1[ch] = freq1.get(ch,0)+1
        for i in range(l,r,1):
            freq2[s2[i]]= freq2.get(s2[i],0)+1
        while r<len(s2):
            if freq1 == freq2:
                return True
            else:
                if freq2.get(s2[l], 0) == 1:
                    freq2.pop(s2[l])
                else:
                    freq2[s2[l]]= freq2.get(s2[l],0)-1
                l+=1
                freq2[s2[r]]= freq2.get(s2[r],0)+1
                r+=1
        if freq1 == freq2:
            return True
        return False
        