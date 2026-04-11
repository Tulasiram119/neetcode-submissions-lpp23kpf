class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        map = {}
        s = sum(nums)
        if s % 2 == 1:
            return False
        need = s //2
        def dfs(index,su):
            if index == n:
                return su == need
            if (index,su) in map:
                return map[index,su]
            one = dfs(index+1,su)
            two = dfs(index+1,su+nums[index])
            ans = one or two
            map[(index,su)] = ans
            return ans
        return dfs(0,0)