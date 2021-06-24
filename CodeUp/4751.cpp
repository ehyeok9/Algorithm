#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool compare(vector<int> a, vector<int> b){
	return a[2] > b[2];
}

int main(){
	int n,a;
	scanf("%d", &n);
	vector<vector<int>> input;
	vector<int> ex;
	
	for (int i=0; i <n; i++){
		ex = {};
		for (int j=0; j < 3; j++){
			scanf("%d", &a);
			ex.push_back(a);
		}
		input.push_back(ex);
	}
	
	sort(input.begin(), input.end(), compare);
	
	vector<vector<int>> result;
	result.push_back(input[0]);
	result.push_back(input[1]);
	
	if((input[0][0] == input[1][0]) && (input[1][0] == input[2][0]) && (input[2][0] == input[0][0])){
		for (int i=3; i <input.size(); i++){
			if (input[i][0] != input[2][0]){
				result.push_back(input[i]);
				break;
			}
		}
	}
	else{
		result.push_back(input[2]);
	}
	
	for (int i=0; i<result.size(); i++){
		printf("%d %d\n", result[i][0], result[i][1]);
	}
	
	return 0;
}

