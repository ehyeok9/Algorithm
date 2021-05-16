#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,a;
	cin >> n;
	vector<int> list;
	
	for(int i=0; i<n; i++){
		cin >> a;
		list.push_back(a);
	}
	reverse(list.begin(), list.end());
	
	for (int i=0; i < list.size(); i++){
		cout << list[i] << ' ';
	}
	return 0;
}

