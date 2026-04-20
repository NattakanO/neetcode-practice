class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)-1):
            max_right = max(arr[i+1:])
            result.append(max_right)
        result.append(-1)
        return result