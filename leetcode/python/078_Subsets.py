class Solution:
    # bit
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        length = len(nums)
        for i in range(2**length):
            tmp = []
            p = 1
            for j in range(length):
                if i & p:
                    tmp.append(nums[j])
                p = p<<1
            ans.append(tmp)
        return ans

class Solution2:
    # backtrack
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(nums, [], ans, 0)
        return ans
    
    def backtrack(self, nums, tmp, ans, n):
        ans.append(tmp.copy())
        if len(tmp) == len(nums):
            return
        i = n
        while i < len(nums):
            tmp.append(nums[i])
            i = i + 1
            self.backtrack(nums, tmp, ans, i)
            tmp.pop()