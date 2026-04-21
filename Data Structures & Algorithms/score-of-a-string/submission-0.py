class Solution:
    def scoreOfString(self, s: str) -> int:
        s = list(s)
        ascii_s = list(map(ord,s))
        print(ascii_s)
        sum = 0
        for i in range(len(ascii_s)-1):
            sum += abs(ascii_s[i]-ascii_s[i+1])
        return sum