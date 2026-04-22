class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec = 0
        count = 0
        for i in nums:
            if i == 1:
                count += 1
                if count > max_consec:
                    max_consec = count
            else:
                count = 0
        return max_consec