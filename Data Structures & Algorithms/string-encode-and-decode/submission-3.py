class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += (s+"~")
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        start = 0
        ans = []
        for i in range(len(s)):
            char = s[i]
            if char == "~":
                ans.append(s[start:i])
                start = i+1
        return ans
