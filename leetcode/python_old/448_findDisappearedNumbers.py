#bit map
class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        bit_map = 0
        for num in nums:
            tmp = 1 << (num-1)
            if bit_map & tmp != tmp:
                bit_map += tmp
        ret = []
        for i in range(len(nums)):
            num = 1 << i
            if bit_map & num == 0:
                ret.append(i+1) # Attention: i+1
        return ret

# Negative mark on array where 1 ≤ a[i] ≤ n
class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            idx = abs(num) -1
            nums[idx] = -abs(nums[idx])
        ret = []
        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i+1)
        return ret        
