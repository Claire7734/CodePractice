#include "LeetCodeTest.h"

class Solution {
public:
    void reverseString(vector<char>& s) {
	int i,j;
	i = 0;
	j = s.size() - 1;
	while(i<j){
		swap(s[i++],s[j--]);
	}
    }
};

vector<char> run_344()
{
	vector<char> s = {'2','t','6'};
        Solution test;
        test.reverseString(s);
	return s;
}
