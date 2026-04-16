class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        set_num = set(numbers)
        for i in range(len(numbers)):
            comp = target - numbers[i]
            if comp in set_num:
                return [i+1, numbers.index(comp)+1]
        