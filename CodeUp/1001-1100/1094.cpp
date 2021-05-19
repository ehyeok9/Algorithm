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
	
	reverse(list.begin(), list.end());
	
	for (int i=0; i < list.size(); i++){
		cout << list[i] << ' ';
	}
	return 0;
}