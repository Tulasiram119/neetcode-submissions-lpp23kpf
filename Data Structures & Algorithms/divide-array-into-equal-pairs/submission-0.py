class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # We will get nums array
        # We need to divide the array into different sizes
        # Each pair will same number
        # First the length should be even
        # The count of each number be also even
        n = len(nums)
        if (n % 2 == 1):
            return False
        count = Counter(nums)
        for num in count.values():
            if num % 2 == 1:
                return False
        return True