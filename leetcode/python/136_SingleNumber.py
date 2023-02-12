class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[0]
        for i in range(1, len(nums)):
            xor ^= nums[i]
        return xor

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        bucket = {}
        for i in range(len(nums)):
            if nums[i] in bucket:
                bucket[nums[i]] += 1
            else:
                 bucket[nums[i]] = 1
        for ele in bucket:
            if bucket[ele] == 1:
                return ele