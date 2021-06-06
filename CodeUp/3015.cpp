#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool compare(pair<pair<string,int>, int> a, pair<pair<string,int>, int> b){
	if (a.first.second == b.first.second){
		return a.second < b.second;
	}
	return a.first.second > b.first.second; 
}

int main(){
	int n, m, grade;
	string str;
	scanf("%d %d", &n, &m);
	vector<pair<string, int>> struc;
	
	for (int i=0; i<n; i++){
		cin >> str;
		scanf("%d", &grade);
		struc.push_back(make_pair(str,grade));
	}

	vector<pair<pair<string, int>, int>> result;
	
	for (int i=0; i< struc.size(); i++){
		result.push_back(make_pair(struc[i], i));
	}
	
	sort(result.begin(), result.end(), compare);
	
	for (int i=0; i< m; i++){
		cout << result[i].first.first << endl;
	}
	
	return 0;
}

