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
	return a.first.second < b.first.second;
}

int main(){
	int n, a;
	scanf("%d", &n);
	vector<pair<int, int>> input;
	
	for (int i=0; i < n; i++){
		scanf("%d", &a);
		input.push_back(make_pair(a,i));
	}
	
	sort(input.begin(), input.end(), compare);
	
	int rate = 1;
	vector<pair<pair<int, int>, int>> result;
	bool flag;
	
	if (input[0].first == input[1].first){
		flag = true;
	}
	else{
		flag = false;
	}
	
	for (int i=0; i<input.size()-1; i++){
		if (!flag){
			rate = i+1;
		}
		
		result.push_back(make_pair(input[i], rate));
		
		if (input[i].first == input[i+1].first){
			flag = true;
		}
		else{
			flag = false;
		}
	}
	
	if (flag){
		result.push_back(make_pair(input[input.size()-1], rate));
	}
	else{
		result.push_back(make_pair(input[input.size()-1], input.size()));
	}
	
	sort(result.begin(), result.end(), compare2);
	
	for (int i=0; i<result.size(); i++){
		printf("%d %d\n", result[i].first.first, result[i].second);
	}
	
	return 0;
}

