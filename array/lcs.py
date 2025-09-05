# 128.Longest Consecutive Subsequence
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        else:
            n = sorted(nums)
            lcs = 1
            curr = 1

            for i in range(1,len(n)):
                if n[i] == n[i-1]:
                    continue
                elif n[i]- n[i-1]==1:
                    curr +=1
                else:
                    lcs = max(lcs,curr)
                    curr = 1
        lcs = max(lcs,curr)
        return lcs
        