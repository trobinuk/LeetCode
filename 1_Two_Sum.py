'''class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for idx,num in enumerate(nums):
            if target-num in lookup:
                return [lookup[target-num],idx]
            else:
                lookup[num] = idx'''

def twoSum1(nums, target):
    lookup = {}
    for idx,num in enumerate(nums):
        if target-num in lookup:
            return [lookup[target-num],idx]
        else:
            lookup[num] = idx

def twoSum(nums, target):
    lookup = {}
    for idx,num in enumerate(nums):
        print("outer loop", idx)
        for idx1,num1 in enumerate(nums[idx+1:]):
            print("========inner loop")
            print(idx,idx1)
            if num+num1 == target:
                return [idx,idx1]
    return 1

result = twoSum([3,2,4],6)
print("result is ----",result)
