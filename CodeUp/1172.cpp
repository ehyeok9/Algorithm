#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int a;
	vector<int> list;
	
	for (int i=0; i<3; i++){
		cin >> a;
		list.push_back(a);
	}
	
	sort(list.begin(), list.end());
	
	for (int i=0; i < list.size(); i++){
		cout << list[i] << ' ';
	}
	return 0;
}
