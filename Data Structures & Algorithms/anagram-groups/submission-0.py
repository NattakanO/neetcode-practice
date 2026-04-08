class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}
        for i in range(len(strs)):
            sorted_word = sorted(list(strs[i]))
            sorted_word = "".join(sorted_word)
            print(sorted_word)
            if sorted_word not in anagrams_map:
                anagrams_map[sorted_word] = []
            anagrams_map[sorted_word].append(strs[i])
        return list(anagrams_map.values())