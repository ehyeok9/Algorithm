#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, a;
	scanf("%d", &n);
	vector< vector<int>> list;
	
	for (int i=1; i <= n; i++){
		scanf("%d", &a);
		vector<int> k;
		k.push_back(a);
		list.push_back(k);
	}
	
	int se = 0;
	for (int i=0; i<n; i++){
		for (int j=0; j < se; j++){
			int u= list[i][j] - list[i-1][j];
			list[i].push_back(u);
		}
		se++;
	}
	
	for (int i=0; i<list.size(); i++){
		for (int j=0; j <list[i].size(); j++){
			printf("%d ", list[i][j]);
		}
		printf("\n");
	}
	return 0;
}
