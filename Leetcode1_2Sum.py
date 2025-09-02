class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Index = {}

        for i, num in enumerate(nums):
            if target - num in Index:
                return Index[target-num], i
            Index[num] = i