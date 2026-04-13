class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0,0,0]
        for num in nums:
            arr[num] += 1
        k = 0
        for i in range(3):
            for _ in range(arr[i]):
                nums[k] = i
                k += 1
