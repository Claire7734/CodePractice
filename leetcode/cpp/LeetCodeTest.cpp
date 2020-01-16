#include "LeetCodeTest.h"

void printVector(const vector<char>& v){
    	for(int i=0;i<v.size();i++)
	{
		cout << v[i] ;
	}
	cout << endl;
}

int main()
{
	vector<char> res = run_344();
	printVector(res);
	return 0;
}
