#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n;
	cin >> n;
	
	vector<pair<int, int>> list;
	int a,b;
	for (int i=1; i <= 6; i++){
		if (n-i  <= 6 &&  n-i >= 1){
			list.push_back(pair<int, int>(i, n-i));
		}
	}
	
	sort(list.begin(), list.end());
	
	for (int i = 0; i < list.size(); i++){
		cout << list[i].first << ' ' << list[i].second << endl;
	}
	return 0;
}

