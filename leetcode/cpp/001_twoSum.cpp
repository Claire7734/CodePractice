#include "LeetCodeTest.h"

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
	unordered_map<int,int> map;
	vector<int> ret;
	for(int i = 0;i < nums.size();++i)
	{
		if(map.find(target - nums[i]) != map.end())
		{
			ret.insert(ret.begin(),i);
			ret.insert(ret.begin(),map.find(target - nums[i])->second);
			break;
		}
		map.insert({{nums[i],i}});
	}      
	return ret;
    }
};
