class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_Index = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_to_Index:
                return [num_to_Index[complement], i]
            num_to_Index[num] = i
        
            