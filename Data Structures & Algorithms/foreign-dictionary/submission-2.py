class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {c:set() for word in words for c in word}
        n = len(words)
        for i in range(n-1):
            s1 = words[i]
            s2 = words[i+1]
            l = min(len(s1),len(s2))
            if len(s1) > len(s2) and s1[:l] == s2[:l]:
                return ""
            for j in range(l):
                if s1[j] != s2[j]:
                    adj[s1[j]].add(s2[j])
                    break
        visit = {}
        res = []
        def dfs(c):
            if c in visit:
                return visit[c]
            visit[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visit[c] = False
            res.append(c)
        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
        
        