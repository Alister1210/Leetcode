# 15. 3 sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.
class Solution(object):
    def threeSum(self, nums):
        s = sorted(nums)
        n = len(s)
        ans = []
        for i in range(n-2):
            if s[i]>0:
                break
            if i>0 and s[i] == s[i-1]:
                continue
            l = i+1
            r=n-1
            while l<r:
                total = s[l] + s[r] + s[i]
                if total > 0:
                    r-=1
                elif total<0:
                    l+=1
                else:
                    ans.append([s[i],s[l],s[r]])
                    while l<r and s[l] == s[l+1]:
                        l+=1
                    while l<r and s[r] == s[r-1]:
                        r-=1
                    l+=1
                    r-=1
        return ans
        