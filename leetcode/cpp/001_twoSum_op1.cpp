#include "LeetCodeTest.h"

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
	unordered_map<int,int> map;
	unordered_map<int,int>::iterator iter;
	for(int i = 0;i < nums.size();++i)
	{
		iter = map.find(target - nums[i]);
		if(iter != map.end())
		{
			return {iter->second,i};
		}
		map[nums[i]]=i;
		//map.insert({{nums[i],i}});
	}      
	return {0,1};
    }
};
