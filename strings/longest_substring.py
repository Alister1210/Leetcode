# 3. Longest Substring without repeating characters
# Given a string s, find the length of the longest substring without duplicate characters.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        line = list(s)
        myset = set()
        longest = 0
        l = 0
        r = 0
        if len(s) == 0 or s== None: return 0
        if len(s) ==1 :return 1
        while r<len(line):
            if line[r] in myset:
                myset.remove(line[l])
                l+=1
            else:
                if longest<r-l+1:longest = r-l+1
                myset.add(line[r])
                r+=1
        return longest