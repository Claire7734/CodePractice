class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        gap = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                gap += 1
            else:
                nums[i-gap] = nums[i]
                if gap > 0: # Attention!
                    nums[i] = 0
