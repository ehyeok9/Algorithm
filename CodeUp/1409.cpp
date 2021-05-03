#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,a;
	vector<int> list;
	
	for(int i=0; i<10; i++){
		cin >> a;
		list.push_back(a);
	}
	cin >> n;
	cout << list[n-1];
	
	return 0;
}

