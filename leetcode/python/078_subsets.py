import sys

class Solution(object):
    def subsets(self, nums):
        nth_bit = 1 << len(nums)
        ret = []
        for i in range(2**len(nums)):
        	bitmask = bin(i | nth_bit)[3:]
        	print(bitmask)
        	cur = []
        	for j in range(len(bitmask)):
        		if bitmask[j] == '1':
        			cur += [nums[j]]
        	
        	ret.append(cur)
        return ret

def main():
	sol = Solution()
	ret = sol.subsets([0,1])
	for i in ret:
		print(i)

if __name__ == '__main__':
    main()
