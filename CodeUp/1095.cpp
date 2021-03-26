#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	vector<int> list;
	int n,t;
	cin >> n;
	
	for (int i=0; i < n; i++){
		cin >> t;
		list.push_back(t);
	}
	
	sort(list.begin(), list.end());
	
	cout << list[0];
	return 0;
}