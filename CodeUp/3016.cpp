#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool compare(pair<string, vector<int>> a, pair<string, vector<int>> b){
	return a.second[0] > b.second[0];
}

bool compare2(vector<int> a, vector<int> b){
	return a[1] > b[1];
}

int main(){
	int n, a;
	scanf("%d", &n);
	vector<pair<string, vector<int>>> input;
	vector<int> ex;
	string str;
	
	for (int i=0; i<n; i++){
		cin >> str;
		for (int j=0; j<3; j++){
			scanf("%d", &a);
			ex.push_back(a);
		}
		input.push_back(make_pair(str, ex));
		ex = {};
	}
	
	sort(input.begin(), input.end(), compare);
	string name = input[0].first;
	int rank[input.size()] = {1};
	int rank2[input.size()] = {1};
	
	for (int i=0; i<input.size(); i++){
		for (int j=0; j<input.size(); j++){
			if (input[i].second[1] < input[j].second[1]){
				rank[i]++;
			}
			if (input[i].second[2] < input[j].second[2]){
				rank2[i]++;
			}
		}
	}
	
	cout << name << " " << rank[0] << " " << rank2[0];
	
	return 0;	
}

