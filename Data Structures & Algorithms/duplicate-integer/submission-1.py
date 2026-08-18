class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_Nums = set()
        for num in nums:
            if num in seen_Nums:
                return True
            seen_Nums.add(num)
        return False

        