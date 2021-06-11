#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool compare(pair<int, int> a, pair<int, int> b){
	return a.first > b.first;
}

bool compare2(pair<pair<int, int>, int> a, pair<pair<int, int>, int> b){
	return a.first.second < a.first.second;
}
int main(){
	int n, temp;
	scanf("%d", &n);
	vector<pair<int, int>> value;
	
	for (int i=0; i<n; i++){
		scanf("%d", &temp);
		value.push_back(make_pair(temp, i));
	}
	
	sort(value.begin(), value.end(), compare);
	vector<pair<pair<int, int>, int>> result;
	int cnt = 1;
	
	for(int i=0; i<value.size(); i++){
		if (i == value.size()-1){
			result.push_back(make_pair(value[i], cnt));
		}
		else if (value[i].first == value[i+1].first){
			result.push_back(make_pair(value[i], cnt));
		}
		else{
			result.push_back(make_pair(value[i], cnt));
			cnt ++;
		}
	}
	
	sort(result.begin(), result.end(), compare2);
	
	for (int i=0; i<result.size(); i++){
		printf("%d %d\n", result[i].first.first, result[i].second);
		printf("%d\n", result[i].first.second);
	}
	return 0;
}

