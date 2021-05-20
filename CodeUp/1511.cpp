#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;

int main(){
	int n, a = 1;
	scanf("%d", &n);
	int list[n+1][n+1];
	
	for(int i=1; i <= n; i++){
		for(int j =1; j <=n; j++){
			list[i][j] = a++;
		}
	}
	
	int sum = 0;
	
	for (int j=1 ; j<=n; j++){
			sum += list[1][j];
			sum += list[j][1];
			sum += list[n][j];
			sum += list[j][n];
		}
	sum -= list[1][1] + list[1][n] + list[n][1] + list[n][n];
	
	printf("%d", sum);
	return 0;
}
