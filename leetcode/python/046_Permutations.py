class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.backtrack(ans, [], nums)
        return ans

    def backtrack(self, ans: List[int], tmp: List[int], nums: List[int]):
        if len(tmp) == len(nums):
            newtmp = tmp.copy()
            ans.append(newtmp)
        else:
            for i in range(len(nums)):
                if nums[i] in tmp:
                    continue
                tmp.append(nums[i])
                self.backtrack(ans, tmp, nums)
                del tmp[len(tmp) - 1]