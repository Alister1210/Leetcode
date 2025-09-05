#Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Solution 1 based on intuition but doesnt work on high length array and on leetcode submission there is a case of huge array so it doesnt work
class Solution(object):
    def productExceptSelf(self, nums):
        new_nums = []
        for i in range(len(nums)):
            product = reduce(operator.mul, nums[:i] + nums[i+1:], 1)
            new_nums.append(product)
        return new_nums
    
# Solution 2 : Works but takes O(3n) complexity and not optimal but easier to understand
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        result = [1] * n
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
            
        for i in range(n-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]
            
        for i in range(n):
            result[i] = prefix[i]*postfix[i]

        return result
                
# OR THE BELOW CODE
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        postfix = [1] * n
        result = [1] * n
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
            p = n-1-i
            postfix[p] = postfix[p+1] * nums[p+1]
            
        for i in range(n):
            result[i] = prefix[i]*postfix[i]

        return result

# Optimal Solution
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = 1
        postfix = 1
        result = [1] * n
        for i in range(1,n):
            p = n-1-i
            result[i-1] *= prefix
            result[p+1] *= postfix
            prefix*= nums[i-1]
            postfix*= nums[p+1]

        result[n-1] *= prefix
        result[0] *= postfix

        return result
                