class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in list(s):
            if i in list(t):
                idx = t.index(i)
                t = t[idx+1:]
                print(t)
            else:
                return False
        
        return True