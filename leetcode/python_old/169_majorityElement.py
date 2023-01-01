# Boyer-Moore Voting Algorithm 多数投票算法
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1 
        return candidate

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        length = len(nums)
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
            if dic[num] > length//2:
                return num		

# Sort and take the middle one
class Solution2: 
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
