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
	
	for(int i=0; i<n-1; i++){
		cin >> a;
		list.push_back(a);
	}
	
	sort(list.begin(), list.end());
	int p = -1;
	
	for (int i=0; i < list.size(); i++){
		if (list[i] != i+1){
			cout << i+1;
			p = 1;
			break;
		}
	}
	
	if (p == -1){
		cout << n;
	}
	
	return 0;
}

