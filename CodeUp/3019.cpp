#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool compare(pair<string, vector<int>> a, pair<string, vector<int>> b){
	if (a.second[0] == b.second[0]){
		if (a.second[1] == b.second[1]){
			if (a.second[2] == b.second[2]){
				return a.first < b.first;
			}
			else{
				return a.second[2] < b.second[2];
			}
		}
		else{
			return a.second[1] < b.second[1];
		}
	}
	else{
		return a.second[0] < b.second[0];
	}
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
	
	for (int i=0; i < input.size(); i++){
		cout << input[i].first << endl;
	}
	return 0;
}

