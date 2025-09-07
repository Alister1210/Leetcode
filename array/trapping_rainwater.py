# 42. trapping Rainwater
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

class Solution(object):
    def trap(self, height):
        n= len(height)
        l=0
        r=n-1
        lmax=height[l]
        rmax=height[r]
        total=0
        while l<r:
            if height[l]<height[r]:
                lmax = max(lmax,height[l])
                if lmax-height[l]>0:
                        total+=lmax-height[l]
                l+=1
            else:
                rmax = max(rmax,height[r])
                if rmax-height[r]>0:
                        total+=rmax-height[r]
                r-=1
        return total