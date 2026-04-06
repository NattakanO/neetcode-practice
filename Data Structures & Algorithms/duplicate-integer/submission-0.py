class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_num = set(nums)
        return len(unique_num) != len(nums)