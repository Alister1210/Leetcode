# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums and i != nums.index(temp) :
                return [i,nums.index(temp)]
            
            
            
            

# Another way to solve the same question is using Hash Map or dictionary in python Time complexity observed on Leetcode was lower but little higher space complexity
class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map.keys():
                return [i, map.get(complement)]
            map.update({nums[i]: i})
            
            
#  Better Solution with best time and space complexity using Dictionary in python or Hash Map method. Just small tweaks from above but improves complexity drasticallly
class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in map:
                return [i, map[complement] ]
            map[num] = i