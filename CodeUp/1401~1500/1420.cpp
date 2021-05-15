#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
bool compare(pair<string, int> a, pair<string, int> b);


bool compare(pair<string, int> a, pair<string, int> b){
	if (a.second == b.second){
		return a.second > b.second;
	}
	return a.second > b.second;
}

int main(){
	int n;
	cin >> n;
	vector<pair<string, int>> list;
	string str;
	int a;
	
	for (int i=0; i<n ; i++){
		cin >> str >> a;
		list.push_back(make_pair(str,a));
	}
	
	sort(list.begin(), list.end(), compare);
	
	cout << list[2].first;
	return 0;
}
