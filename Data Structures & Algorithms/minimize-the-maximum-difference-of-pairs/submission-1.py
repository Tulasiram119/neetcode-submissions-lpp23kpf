class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0: return 0
        nums.sort()
        n = len(nums)
        
        # Binary search range for the minimum possible "maximum difference"
        left, right = 0, nums[-1] - nums[0]
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            # Count how many pairs have a difference <= mid
            count = 0
            i = 0
            while i < n - 1:
                if nums[i+1] - nums[i] <= mid:
                    count += 1
                    i += 2  # Use these two, move to next possible pair
                else:
                    i += 1  # Difference too large, try next adjacent pair
            
            if count >= p:
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans