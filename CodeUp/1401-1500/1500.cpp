#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,m,a;
	scanf("%d %d", &n, &m);
	
	int list[n][m];
	
	for (int i=0; i < n; i++){
		for (int j=0; j < m; j++){
			scanf("%d", &a);
			list[i][j] = a;
		}
	}
	
	for (int i=0; i<n; i++){
		for(int j=0; j<m; j++){
			printf("%d ", list[i][j]);
		}
		printf("\n");
	}
	return 0;
}
