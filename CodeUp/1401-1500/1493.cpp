#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n,a,m;
	scanf("%d %d", &n, &m);
	
	int list[n+1][n+1];
	for (int i=1; i <= n; i++){
		for (int j=1; j<= m; j++){
			scanf("%d", &a);
			list[i][j] = a;
		}
	}
	
	int result[n+1][m+1];
	for (int i=1; i <= n; i++){
		for(int j=1; j<= m; j++){
			int sum = 0;
			for(int k =1; k <= i; k++){
				for (int l=1; l <= j; l++){
					sum += list[k][l];
				}
			}
			result[i][j] = sum;
		}
	}
	
	for (int i=1; i <= n; i++){
		for (int j=1; j<= m; j++){
			printf("%d ", result[i][j]);
		}
		printf("\n");
	}
	return 0;
}
