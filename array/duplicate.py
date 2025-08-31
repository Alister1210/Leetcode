# Find the Duplicate Number


def findDuplicate(nums):
    s = set()
    for i in range(len(nums)):
        if nums[i] in s:
            return print(True);
        else:
            s.add(nums[i])
    return print(False)
    print(s)

findDuplicate([1,2,3,4,5,6])
    