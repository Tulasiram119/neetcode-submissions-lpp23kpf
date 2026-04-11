class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        map = {}
        def dfs(index,sum1,sum2):
            if index == n:
                return sum1 == sum2
            if (index,sum1,sum2) in map:
                return map[index,sum1,sum2]
            one = dfs(index+1,sum1+nums[index],sum2)
            two = dfs(index+1,sum1,sum2+nums[index])
            ans = one or two
            map[(index,sum1,sum2)] = ans
            return ans
        return dfs(0,0,0)