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
	int p =0;
	for (int i=0; i < n; i++){
		for (int i =p; i < list.size(); i++){
			cout << list.at(i) << ' ';
		}
		cout << endl;
		list.push_back(list[p]);
		p ++;
	}
	return 0;
}

