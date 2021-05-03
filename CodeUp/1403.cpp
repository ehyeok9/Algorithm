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
	
	for (int i = 0; i <2; i++){
		for (int i=0; i <list.size(); i++){
			cout << list[i] << endl;
		}
	}
	return 0;
}

