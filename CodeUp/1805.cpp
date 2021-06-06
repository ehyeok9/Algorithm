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
	
	for (int i=0; i<n; i++){
		scanf("%d %d", &a, &b);
		struc.push_back(make_pair(a,b));
	}
	
	sort(struc.begin(), struc.end(), compare);
	
	for (int i=0; i < struc.size(); i++){
		printf("%d %d\n", struc[i].first, struc[i].second);
	}
	
	return 0;
}

