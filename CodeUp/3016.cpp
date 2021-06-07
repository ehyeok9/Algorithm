#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool compare1(pair<string, vector<int>> a, pair<string, vector<int>> b){
	return a.second[0] > b.second[0]; 
}

bool compare2(pair<string, vector<int>> a, pair<string, vector<int>> b){
	return a.second[1] > b.second[1]; 
}

bool compare3(pair<string, vector<int>> a, pair<string, vector<int>> b){
	return a.second[2] > b.second[2]; 
}

int main(){
	int n;
	scanf("%d", &n);
	string str;
	int first, second, third;
	vector<pair<string, vector<int>>> struc;
	
	for (int i=0; i<n; i++){
		cin >> str;
		scanf("%d %d %d", &first, &second, &third);
		vector<int> temp = {};
		temp.push_back(first);
		temp.push_back(second);
		temp.push_back(third);
		struc.push_back(make_pair(str, temp));
	}
	
	sort(struc.begin(), struc.end(), compare1);
	string name = struc[0].first;
	int high = struc[0].second[0];
	cout << str << ' ';
	
	int value2;
	sort(struc.begin(), struc.end(), compare2);
	vector<int> set2;
	if (struc[0].second[0] == high){
		printf("%d ", 1);
	}
	else{
		for (int i=0; i < struc.size(); i++){
			if (struc[i].second[0] ==  high){
				value2 = struc[i].second[1];
				break;
			}
			set2.push_back(struc[i].second[1]);
		}

		for (int i=0; i < set2.size(); i++){
			if (set2[i] == value2){
				printf("%d ", i+1);
				break;
			}
			if (i == set2.size()-1){
				printf("%d ", i+2);
			}
		}
	}
	
	int value3;
	sort(struc.begin(), struc.end(), compare3);
	vector<int> set3;
	if (struc[0].second[0] == high){
		printf("%d", 1);
	}
	else{
		for (int i=0; i < struc.size(); i++){
			if (struc[i].second[0] ==  high){
				value3 = struc[i].second[2];
				break;
			}
			set3.push_back(struc[i].second[2]);
		}

		for (int i=0; i < set3.size(); i++){
			if (set3[i] == value3){
				printf("%d", i+1);
				break;
			}
			if (i == set3.size()-1){
				printf("%d", i+2);
			}
		}
	}
	
	return 0;
}

