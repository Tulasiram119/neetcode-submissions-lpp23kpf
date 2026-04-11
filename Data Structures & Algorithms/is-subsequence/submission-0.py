class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        small = 0
        slen = len(s)
        for big in range(len(t)):
            if small < slen and s[small] == t[big]:
                small += 1
        return small == slen