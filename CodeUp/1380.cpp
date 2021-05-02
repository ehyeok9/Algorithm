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
	
	for (int i=1; i <= n/2; i++){
		list.push_back(pair<int, int>(i, n-i));
		list.push_back(pair<int, int>(n-i, i));
	}
	sort(list.begin(), list.end());
	
	for (int i = 0; i < list.size(); i++){
		cout << list[i].first << ' ' << list[i].second << endl;
	}
	return 0;
}

