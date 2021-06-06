#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

bool compare(pair<int,int> a, pair<int,int> b){
	return a.first < b.first; 
}

int main(){
	int n, a, b;
	scanf("%d", &n);
	vector<pair<int, int>> struc;
	vector<int> list;
	
	for (int i=0; i<n; i++){
		scanf("%d", &a);
		struc.push_back(make_pair(a,i));
	}
	
	sort(struc.begin(), struc.end(), compare);
	vector<pair<int,int>> result;
	
	for (int i=0; i< struc.size(); i++){
		result.push_back(make_pair(struc[i].second, i));
	}
	
	sort(result.begin(), result.end(), compare);
		
	for (int i=0; i < result.size(); i++){
		printf("%d ", result[i].second);
	}
	
	return 0;
}

