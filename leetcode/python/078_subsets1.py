class Solution(object):
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
        	res += [cur + [num] for cur in res]

        return res