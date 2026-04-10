class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += s
            ans += '~'
        return ans
    def decode(self, s: str) -> List[str]:
        return s.split("~")[:-1]